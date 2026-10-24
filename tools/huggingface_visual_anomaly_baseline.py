#!/usr/bin/env python3
"""Local image-level visual anomaly baseline using a Hugging Face DINOv2 backbone.

This is an exploratory embedding-distance baseline, not a validated anomaly model
and not a narcotics, concealed-item, or chemical-identification detector.
Use only consented, non-sensitive test images of objects/scenes.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_MODEL = "facebook/dinov2-small"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare a query image with a reference set using local DINOv2 embeddings."
    )
    parser.add_argument("image", type=Path, help="Query image to compare")
    parser.add_argument(
        "--normal-dir", type=Path, required=True,
        help="Directory of reference images representing an expected baseline",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Hugging Face model ID")
    parser.add_argument(
        "--threshold", type=float, default=None,
        help="Optional exploratory anomaly-score threshold (1 - cosine similarity); not calibrated",
    )
    parser.add_argument("--json-out", type=Path, help="Optional JSON report path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(f"Query image does not exist: {args.image}", file=sys.stderr)
        return 2
    if not args.normal_dir.is_dir():
        print(f"Reference directory does not exist: {args.normal_dir}", file=sys.stderr)
        return 2
    if args.threshold is not None and args.threshold < 0:
        print("--threshold must be non-negative.", file=sys.stderr)
        return 2
    reference_paths = sorted(
        path for path in args.normal_dir.iterdir()
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    )
    if not reference_paths:
        print("Reference directory contains no supported image files.", file=sys.stderr)
        return 2

    try:
        import torch
        import torch.nn.functional as F
        from PIL import Image
        from transformers import AutoImageProcessor, AutoModel
    except ImportError as exc:
        print(
            "Missing optional dependency. Install compatible local PyTorch, Transformers, "
            "and Pillow versions in a project virtual environment. No packages are installed automatically.",
            file=sys.stderr,
        )
        print(f"Import error: {exc}", file=sys.stderr)
        return 2

    try:
        processor = AutoImageProcessor.from_pretrained(args.model)
        model = AutoModel.from_pretrained(args.model)
        model.eval()
        device = torch.device("cpu")
        model.to(device)

        def embed(path: Path):
            with Image.open(path) as source:
                image = source.convert("RGB")
            inputs = processor(images=image, return_tensors="pt")
            inputs = {key: value.to(device) for key, value in inputs.items()}
            with torch.inference_mode():
                outputs = model(**inputs)
                vector = outputs.last_hidden_state[:, 0, :]
                return F.normalize(vector, p=2, dim=1)

        query_embedding = embed(args.image)
        reference_embeddings = torch.cat([embed(path) for path in reference_paths], dim=0)
        reference_center = F.normalize(reference_embeddings.mean(dim=0, keepdim=True), p=2, dim=1)
        similarity = float(F.cosine_similarity(query_embedding, reference_center).item())
        score = max(0.0, min(2.0, 1.0 - similarity))
    except Exception as exc:
        print(f"Anomaly baseline failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    flagged = score >= args.threshold if args.threshold is not None else None
    report = {
        "task": "image-level embedding-distance anomaly baseline",
        "backbone": args.model,
        "query_image": str(args.image),
        "reference_image_count": len(reference_paths),
        "reference_directory": str(args.normal_dir),
        "cosine_similarity_to_reference_center": similarity,
        "exploratory_anomaly_score": score,
        "user_supplied_threshold": args.threshold,
        "threshold_flag": flagged,
        "status": "exploratory; not calibrated or independently validated",
        "limitations": (
            "This compares visual embeddings against a reference set. It does not localise anomalies, "
            "identify narcotics, detect chemical composition, see through clothing, or establish that an "
            "object is dangerous or illegal. Scores depend on image content, reference-set quality, model "
            "and acquisition conditions. A flag is not evidence of wrongdoing. Do not use for person scoring, "
            "search, detention, or enforcement decisions. Validate on representative, rights-cleared object "
            "images before any limited intended use."
        ),
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
