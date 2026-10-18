# Free local-first data preparation helper for Windows PowerShell.
# Run from repository root: powershell -ExecutionPolicy Bypass -File .\scripts\prepare_free_datasets.ps1
# No cloud GPU, paid API, subscription or hosted training is used.
$ErrorActionPreference = "Stop"
$root = Join-Path (Get-Location) "datasets"
New-Item -ItemType Directory -Force -Path $root | Out-Null

Write-Host "C3PI is prescription-pill imagery for computer-vision tooling experiments."
Write-Host "It is NOT illicit narcotics ground truth and cannot validate narcotics identification."
Write-Host "Check source terms, disk space and your internet/data plan first."
Write-Host ""
$choice = Read-Host "Download the C3PI sample archive (~493 MB)? Type YES to proceed"
if ($choice -ceq "YES") {
    $zip = Join-Path $root "C3PI_sampleData.zip"
    $url = "https://data.lhncbc.nlm.nih.gov/public/Pills/sampleData.zip"
    if (-not (Test-Path $zip)) {
        Invoke-WebRequest -Uri $url -OutFile $zip
    } else {
        Write-Host "Archive already exists; not downloading again: $zip"
    }
    Write-Host "Archive saved: $zip"
    Write-Host "Official source and terms: https://catalog.data.gov/dataset/computational-photography-project-for-pill-identification-c3pi"
    $extract = Read-Host "Extract archive locally? Type YES to proceed"
    $dest = Join-Path $root "C3PI_sampleData"
    if ($extract -ceq "YES" -and -not (Test-Path $dest)) {
        Expand-Archive -LiteralPath $zip -DestinationPath $dest
        Write-Host "Extracted to $dest"
    }
} else {
    Write-Host "Skipped C3PI download."
}
Write-Host ""
Write-Host "Potential forensic image source (602 JPG images; about 5.6 GB):"
Write-Host "https://zenodo.org/records/4124562"
Write-Host "Do NOT download/use it until the record's explicit licence and conditions have been verified."
Write-Host "For real narcotics research, use authorized data with authoritative laboratory ground truth."
Write-Host "Next: inventory allowed local images with tools\dataset_inventory.py; manually review rights and labels."
Write-Host "Do not commit datasets or model weights to Git."
