# powershell
# Save as `scripts\run-ci-local.ps1` and run from repo root: `.\scripts\run-ci-local.ps1`
# Requires the Windows Python launcher `py` and Python versions installed.

$versions = @('3.10','3.11','3.12', '3.13', '3.14')

foreach ($v in $versions) {
  Write-Host "=== Testing with Python $v ==="
  $venv = ".venv$v"
  py -$v -m venv $venv

  # Activate (PowerShell)
  & "$venv\Scripts\Activate.ps1"
  python -m pip install --upgrade pip

  # Install project deps if you have a requirements file
  if (Test-Path 'requirements.txt') {
    pip install -r requirements.txt
  }

  # Ensure test/lint/type-check tools are present
  pip install --upgrade pytest flake8 mypy
  pip install -e .

  # Run linters and tests
  flake8 ismain
  mypy ismain
  pytest -q --maxfail=1

  # Deactivate venv
  deactivate
}
