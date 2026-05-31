# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`ismain` is a single-function PyPI package. The entire library is `is_main()` in `ismain/is_main.py` — a more readable replacement for `if __name__ == "__main__":`. There are no runtime dependencies.

## Architecture

The one detail that matters: `is_main()` works by walking the call stack with `inspect.stack()[1].frame.f_locals.get("__name__")` — it reads `__name__` from the **caller's** frame, not the module where `is_main` is defined. This is why it can be called from any module and report whether *that* module is being run as `__main__`. Any change to the call depth (e.g. adding a wrapper function) breaks the `[1]` index assumption.

`ismain/__version__.py` is the single source of truth for package metadata (`__version__`, `__author__`, etc.), re-exported through `ismain/__init__.py`. `pyproject.toml` reads the version dynamically from it via `[tool.setuptools.dynamic]` (`attr = "ismain.__version__.__version__"`), so bumping `__version__.py` is all that's needed.

## Common commands

Run from the repo root. The Windows `.bat` scripts assume a venv at `venv/` created by `make_venv.bat` (uses Python 3.14).

```
python -m pytest                          # run the test suite
python -m pytest test_is_main/test_is_main.py::test_is_main   # single test
flake8 . --max-line-length=127 --per-file-ignores="benchmark/*.py:E402"
mypy .
pytest -q --cov=ismain --cov-report=term-missing   # tests with coverage
black -l 132 ismain test_is_main example setup.py source   # format
```

`scripts/` holds Windows convenience wrappers (`coverage.bat`, `run_flake8.bat`, `run_mypy.bat`, `blackify.bat`, `pypi.bat` for build+twine upload). `scripts/run-ci-local.ps1` replays the CI matrix locally across Python versions.

## Testing notes

`test_is_main.py` has two parts. The in-process `is_main()` call must return `False` (pytest is the `__main__`, not the test module). It then re-runs itself as a subprocess to assert it returns `True` when actually run as main — **this subprocess branch is skipped when the `CI` env var is set**, because it depends on a local `venv/Scripts/python.exe` that doesn't exist in CI.

## CI

Two GitHub Actions workflows (`ci.yml`, `python-package.yml`) run flake8 + mypy + pytest on the Python 3.8–3.14 matrix on every push/PR to `master`. Coverage uploads to Codecov. flake8 uses `--max-line-length=127` in CI even though `pyproject.toml` sets `max-line-length = 132` for local runs.

## Benchmarks

`benchmark/` compares `is_main()` overhead against the native idiom (`benchmark_ismain.py` vs `benchmark_legacy.py`); results in `benchmark/benchmark_results.md`.
