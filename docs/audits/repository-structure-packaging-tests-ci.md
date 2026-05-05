# Repository structure, packaging, tests, CI audit

Scope: `peshay/tpm`

## Findings
- Repo is a single-module package: `tpm.py`, `setup.py`, `requirements.txt`, `tests/`.
- No `pyproject.toml` yet; packaging still uses `distutils.core.setup` in `setup.py`.
- Runtime dependencies are legacy-pinned (`requests<=2.26.0`, `future`, `urllib3`).
- CI is Travis-based, targets Python 3.6-3.9 plus nightly, installs with `python setup.py -q install`, and runs `nose2 -v --with-coverage`.
- Tests are fixture-driven under `tests/resources/` and cover API v4/v5 behavior.
- Cross-cutting gap: the request layer disables TLS verification by default (`verify=False`).

## Risks / gaps
- Packaging path is outdated for current Python tooling.
- CI/runtime support matrix is stale and likely misses current supported versions.
- TLS verification default is unsafe for production use.

## Follow-up
- Modernize packaging to `pyproject.toml`.
- Refresh the test/CI matrix.
- Revisit transport security defaults in a separate hardening card.
