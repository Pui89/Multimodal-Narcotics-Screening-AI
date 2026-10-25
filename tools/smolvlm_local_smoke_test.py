#!/usr/bin/env python3
"""Exploratory SmolVLM inference with already-present local files only.

Never downloads model files, installs packages, calls a hosted endpoint, or controls
hardware. Use a permitted image and treat output as free text for human review.
"""
from __future__ import annotations
import argparse, hashlib, json, os, platform, sys, time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODEL_ID = "HuggingFaceTB/SmolVLM-256M-Instruct"

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def model_manifest(model_dir: Path) -> dict[str, Any]:
    files = sorted(p for p in model_dir.rglob("*") if p.is_file())
    lines = [f"{p.relative_to(model_dir).as_posix()}\t{p.stat().st_size}" for p in files]
    return {"file_count": len(files), "total_file_bytes": sum(p.stat().st_size for p in files),
            "manifest_sha256": hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest(),
            "files": [{"path": p.relative_to(model_dir).as_posix(), "bytes": p.stat().st_size} for p in files]}

def run_local_smoke_test(model_dir: Path, image_path: Path, prompt: str,
                         max_new_tokens: int = 64, device_request: str = "cpu") -> dict[str, Any]:
    if not model_dir.is_dir():
        raise FileNotFoundError("MODEL_DIRECTORY_MISSING: supply an existing local model directory.")
    if not image_path.is_file():
        raise FileNotFoundError("IMAGE_FILE_MISSING: choose an existing permitted local image.")
    if not prompt.strip():
        raise ValueError("prompt must not be empty")
    if not 1 <= max_new_tokens <= 128:
        raise ValueError("max_new_tokens must be between 1 and 128")
    if device_request not in {"cpu", "cuda"}:
        raise ValueError("device_request must be 'cpu' or 'cuda'")
    required = ("config.json", "model.safetensors", "preprocessor_config.json")
    missing = [name for name in required if not (model_dir / name).is_file()]
    if missing:
        raise FileNotFoundError("LOCAL_MODEL_FILES_MISSING: " + ", ".join(missing)
                                + ". Missing files will not be downloaded.")

    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    try:
        import torch
        from PIL import Image
        import transformers
        from transformers import AutoModelForVision2Seq, AutoProcessor
    except ImportError as exc:
        raise RuntimeError(
            "DEPENDENCIES_MISSING: torch, transformers and Pillow must be installed manually "
            "in an isolated environment after reviewing resources and licences.") from exc

    if device_request == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA_REQUESTED_BUT_UNAVAILABLE: retry using --device cpu.")
        free_bytes, total_bytes = torch.cuda.mem_get_info()
        free_vram_gib = free_bytes / (1024**3)
        if free_vram_gib < 1.5:
            raise RuntimeError(f"CUDA_PREFLIGHT_BLOCKED: only {free_vram_gib:.2f} GiB free VRAM.")
        device = "cuda"
        device_summary = {"requested": "cuda", "gpu_name": torch.cuda.get_device_name(0),
                          "free_vram_gib_before_load": round(free_vram_gib, 3),
                          "total_vram_gib": round(total_bytes / (1024**3), 3)}
    else:
        device = "cpu"
        device_summary = {"requested": "cpu", "note": "CPU selected to reduce VRAM pressure."}

    manifest = model_manifest(model_dir)
    weight_hash = sha256_file(model_dir / "model.safetensors")
    image_hash = sha256_file(image_path)
    started = time.perf_counter()
    with Image.open(image_path) as source:
        image = source.convert("RGB")
    processor = model = None
    try:
        processor = AutoProcessor.from_pretrained(str(model_dir), local_files_only=True, trust_remote_code=False)
        model = AutoModelForVision2Seq.from_pretrained(
            str(model_dir), local_files_only=True, trust_remote_code=False, low_cpu_mem_usage=True)
        model.to(device)
        model.eval()
        messages = [{"role": "user", "content": [{"type": "image"},
                    {"type": "text", "text": prompt}]}]
        prompt_text = processor.apply_chat_template(messages, add_generation_prompt=True)
        inputs = processor(text=prompt_text, images=[image], return_tensors="pt")
        inputs = {key: value.to(device) for key, value in inputs.items()}
        with torch.inference_mode():
            output_ids = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
        generated = output_ids[:, inputs["input_ids"].shape[1]:]
        answer = processor.batch_decode(generated, skip_special_tokens=True)[0].strip()
        return {
            "schema_version": 1, "status": "COMPLETED_EXPLORATORY_LOCAL_SMOKE_TEST",
            "model_id": MODEL_ID, "model_directory": str(model_dir.resolve()),
            "model_manifest": manifest, "model_safetensors_sha256": weight_hash,
            "image_path": str(image_path.resolve()), "image_sha256": image_hash,
            "image_dimensions": list(image.size), "prompt": prompt, "max_new_tokens": max_new_tokens,
            "software": {"python": platform.python_version(), "torch": torch.__version__,
                         "transformers": transformers.__version__,
                         "pillow": getattr(__import__("PIL"), "__version__", "unknown")},
            "device": device_summary, "observed_latency_ms": round((time.perf_counter()-started)*1000, 3),
            "generated_text": answer, "download_performed": False, "hardware_actuation": False,
            "interpretation_limit": "Single exploratory caption only; not a detector benchmark. Human review required.",
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
        }
    finally:
        del model
        del processor
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-dir", type=Path, required=True, help="Existing local model folder; no download.")
    parser.add_argument("--image", type=Path, required=True, help="Existing permitted local image.")
    parser.add_argument("--prompt", default="Describe only visible objects and scene; state uncertainty.")
    parser.add_argument("--max-new-tokens", type=int, default=64)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--output", type=Path, default=Path("reports/smolvlm-local-smoke.json"))
    args = parser.parse_args()
    try:
        report = run_local_smoke_test(args.model_dir, args.image, args.prompt, args.max_new_tokens, args.device)
    except (OSError, RuntimeError, ValueError, ImportError) as exc:
        print(f"SMOLVLM_LOCAL_SMOKE_TEST_BLOCKED: {exc}", file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"status={report['status']} model={report['model_id']} download_performed=false hardware_actuation=false")
    print(f"report={args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
