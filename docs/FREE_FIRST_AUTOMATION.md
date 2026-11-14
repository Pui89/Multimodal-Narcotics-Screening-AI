# Free-first local automation

Use the repository's existing CI, agent tests, benchmark checks, and security checks. This helper adds a simple local entry point; it does not replace those workflows.

## Run locally (Windows PowerShell)

From the repository root:

```powershell
python tools/free_first_check.py --syntax-only
python tools/free_first_check.py --report reports/free-first-check.json
```

The first command uses only Python's standard library. The second also runs the existing pytest suite and writes a JSON report; pytest must already be installed. The script never installs dependencies, downloads models, edits files, or calls paid services.

## Inspection and evidence boundary

Software tests do not establish physical mobility, terrain capability, inspection accuracy or field readiness. Measure perception errors, localisation drift, uncertainty, fault response and human-review behaviour on documented test scenarios. Keep consequential actions under human supervision.

## Safe automation loop

1. Run checks and capture the report.
2. Inspect the first failing test or syntax error.
3. Make a small, reviewable change.
4. Re-run the same checks and benchmark validators.
5. Keep the change unmerged until review and CI support it.

Automatic repair is intentionally limited: this helper diagnoses failures but does not certify physical robot capability or make consequential decisions.
