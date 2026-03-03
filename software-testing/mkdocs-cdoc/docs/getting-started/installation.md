# Installation

## Basic install

```bash
pip install mkdocs-cdoc
```

This gives you the plugin with regex-based parsing, which works without any system dependencies.

## With libclang (recommended)

For full-accuracy parsing with function signatures, type information, and struct member details, install libclang:

=== "Ubuntu / Debian"

    ```bash
    sudo apt install python3-clang libclang-dev
    ```

=== "macOS"

    ```bash
    brew install llvm
    ```

=== "pip extras"

    ```bash
    pip install mkdocs-cdoc[clang]
    ```

## Verify

Check that the plugin is available:

```bash
python -c "import mkdocs_cdoc; print(mkdocs_cdoc.__version__)"
```

To verify clang is detected:

```bash
python -c "from mkdocs_cdoc.parser import CLANG_AVAILABLE; print('clang:', CLANG_AVAILABLE)"
```

## Requirements

- Python 3.9+
- MkDocs 1.5+
- libclang (optional but recommended)
