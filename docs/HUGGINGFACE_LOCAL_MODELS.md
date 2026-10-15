## Free local Hugging Face model plan

**Goal:** build a local, human-reviewed computer-vision research workflow without paid APIs, cloud GPUs, or subscriptions.

### Suggested model
- **Model ID:** [microsoft/Florence-2-base](https://huggingface.co/microsoft/Florence-2-base)
- **License shown on model card:** MIT; inspect custom model code and the licence before use.
- **Tasks:** image captioning and object-grounding experiments on authorized images of visible objects.
- **Limit:** it is not a narcotics classifier. Ordinary RGB images cannot reliably reveal drugs hidden inside closed luggage or establish chemical identity.

### Optional anomaly-detection track
Explore [Anomalib](https://github.com/open-edge-platform/anomalib) with suitable, legally usable screening imagery. Verify the software licence, each pretrained backbone/checkpoint licence, and dataset terms independently. Start with a small offline experiment and keep all results as hypotheses for authorized human review.

### Local setup
Install PyTorch from the official [local installation selector](https://pytorch.org/get-started/locally/), then:
```bash
python -m pip install transformers accelerate pillow
```
Use only authorized, non-sensitive test images at first. Florence-2 uses custom model code in common examples; inspect it before enabling `trust_remote_code=True`.

### Zero-cost / no-surprise-bill policy
- No hosted inference endpoints, cloud GPU, paid notebook, paid API, or subscription.
- Do not upload sensitive screening images to public services or GitHub.
- Do not add model weights or sensitive datasets to repository history.
- Preserve `UNKNOWN` for missing, conflicting, or out-of-scope evidence.
- Do not infer guilt, chemical identity, or enforcement action from a model output; require validated sensors/procedures and authorized human review.

### Status
This is a research integration plan, not a trained narcotics detector, chemical identification system, or validated security screening product.