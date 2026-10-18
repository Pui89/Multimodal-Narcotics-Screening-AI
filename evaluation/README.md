# Evaluation and reproducible experiments

This directory provides dependency-free metrics and a JSONL evaluation runner.

## Run the included synthetic example

From the repository root:

```bash
python evaluation/run_evaluation.py evaluation/examples/synthetic_predictions.jsonl --output reports/synthetic-evaluation.json
python -m unittest evaluation.test_metrics evaluation.test_runner -v
```

A checked-in example output is available at [`reports/synthetic-evaluation.json`](../reports/synthetic-evaluation.json). Re-run the command above to regenerate it.

The included file is **synthetic teaching data only**. It demonstrates the evaluation pipeline; it is not a narcotics dataset, model output, a representative sample, or a claim of screening performance. Do not cite its metrics as research results.

## Bring your own authorized results

Each JSONL line should contain:

- `y_true`: reference label assigned under a documented annotation protocol.
- `y_pred`: prediction produced by the evaluated system.
- `confidence`: confidence value in the range 0–1.
- `correct`: optional boolean; if omitted, correctness is computed by comparing `y_true` and `y_pred`.

Use lawful, appropriately licensed data with provenance and a clear train/validation/test split. Report class definitions, dataset version, annotation process, model/software version, thresholds, hardware, and limitations. For safety-relevant screening, include per-class precision/recall, false-positive and false-negative counts, unknown/abstention coverage, missing-sensor robustness, calibration, latency, and subgroup/error analysis where lawful and appropriate.

**Important:** the current Streamlit/API demo uses manually entered features and heuristic rules. Evaluating the sample file does not evaluate that API or a trained detector unless the records genuinely come from the evaluated system and the stated reference labels. Never publish invented benchmark values.

## Input validation and positive-class convention

The runner rejects empty input, malformed JSON lines, missing required fields, non-finite or out-of-range confidence scores, non-boolean `correct` flags, and any `correct` value that contradicts `y_true == y_pred`. Calibration correctness is derived from the labels, not trusted from a hand-entered flag. The lower-level metric functions also reject empty labels, non-finite confidence, invalid bin counts, and non-boolean correctness values.

For this screening project, `review` is the default positive class when it appears in the labels. You can explicitly select a class with:

```bash
python evaluation/run_evaluation.py path/to/real_test_predictions.jsonl --positive-label review --output reports/real-test-v1.json
python -m unittest apps.pui89_app.test_main evaluation.test_metrics evaluation.test_runner -v
```

Precision, recall and F1 in this compact report are for the selected positive class, not a substitute for per-class reporting. For real screening evaluation, also publish the confusion matrix and metrics for every class. The synthetic report remains a pipeline smoke test only.
