# Contributing

Thank you for considering contributing to mkdocs-cdoc! Here's how to get started.

## Development setup

```bash
git clone https://github.com/pawelsikora/mkdocs-cdoc.git
cd mkdocs-cdoc
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

For full parsing support, install libclang:

```bash
# Ubuntu / Debian
sudo apt install python3-clang libclang-dev
```

## Running tests

```bash
pytest tests/ -v
```

All 144+ tests should pass. Tests cover parsing (both clang and regex), rendering, cross-references, IGT metadata extraction, configuration handling, and more.

## Code style

The project uses [Black](https://github.com/psf/black) for formatting and [flake8](https://flake8.pycqa.org/) for linting:

```bash
black --check mkdocs_cdoc/ tests/
flake8 mkdocs_cdoc/
```

Please run both before submitting a PR. The CI pipeline enforces these checks.

## Project structure

```
mkdocs_cdoc/
  __init__.py         # Version
  plugin.py           # MkDocs plugin — discovery, registration, rendering
  parser.py           # libclang-based C/C++ comment parser
  regex_parser.py     # Regex fallback parser
  igt_parser.py       # IGT TEST:/SUBTEST: metadata parser
  renderer.py         # Markdown rendering for doc comments
  convert.py          # gtk-doc → reST conversion (runtime + CLI)
tests/                # pytest test suite
example/              # Working example project with sample C sources
docs/                 # Documentation site (this site)
```

## How to contribute

### Bug reports

Open an issue with a minimal reproducer — ideally a small `.c` file and `mkdocs.yml` that demonstrates the problem.

### Feature requests

Open an issue describing the use case. If you're proposing a config change, include a sample `mkdocs.yml` showing how you'd expect it to work.

### Pull requests

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Add or update tests as appropriate
5. Run `black`, `flake8`, and `pytest` locally
6. Open a PR with a clear description of what changed and why

### Documentation

The documentation site lives in `docs/` and is built with MkDocs Material. To preview locally:

```bash
pip install mkdocs-material
mkdocs serve -f mkdocs-site.yml
```

The example project builds separately:

```bash
cd example
mkdocs serve
```

## Release process

1. Update version in `mkdocs_cdoc/__init__.py`, `pyproject.toml`, and `setup.py`
2. Update documentation if needed
3. Tag the release: `git tag v1.0.6`
4. Push: `git push origin main --tags`
5. CI builds and deploys docs automatically
