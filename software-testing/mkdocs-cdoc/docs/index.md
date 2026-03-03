# mkdocs-cdoc

**Generate browsable API documentation from C/C++ source comments directly in MkDocs** — with cross-referencing, symbol indexing, and first-class support for [IGT GPU Tools](https://gitlab.freedesktop.org/drm/igt-gpu-tools) test catalogs.

---

## What it does

mkdocs-cdoc parses `/** ... */` doc comments using libclang (with a regex fallback), converts reST and gtk-doc markup to Markdown, and builds a fully linked API reference with per-symbol anchors, an A–Z index, and automatic cross-references across all your source files and hand-written pages.

## Features

- **Autodoc from C/C++ sources** — scans source trees, extracts doc comments, generates per-file pages with function signatures, parameter tables, and struct/enum member listings.
- **Cross-reference everything** — `:func:`, `:struct:`, `:file:`, backtick auto-linking. Works across generated pages and hand-written Markdown alike.
- **Multiple source groups** — separate nav sections for core libraries, drivers, tests, etc., each with their own A–Z index and overview.
- **IGT test catalog** — parses `TEST:` / `SUBTEST:` structured comments and `igt_subtest()` / `igt_describe()` macros to build test documentation with metadata tables, "By Category" / "By Functionality" index pages, and per-subtest anchors.
- **gtk-doc migration** — converts `#TypeName`, `function()`, `%CONSTANT`, `@param` markup at parse time, plus a CLI for one-time batch conversion of source files.
- **Clang + regex** — uses libclang when available for accurate signatures and types, falls back to regex parsing so it works everywhere.

## Quick example

```yaml
plugins:
  - cdoc:
      source_root: src/
```

That's it. This scans all `.c` and `.h` files under `src/`, generates per-file API pages, and adds them to the nav under "API Reference".

For multi-source projects:

```yaml
plugins:
  - cdoc:
      project_name: My Project
      sources:
        - root: src/core
          nav_title: Core API
        - root: src/drivers
          nav_title: Drivers
        - root: tests
          nav_title: Tests
          igt:
            group_by: [category, functionality]
```

## Build output

During a build, the plugin logs progress so you always know what's happening:

```
INFO - cdoc: libclang available, parser: auto
INFO - cdoc: using libclang for parsing
INFO - cdoc: project version 1.4 (from meson.build)
INFO - cdoc: [Core API] 287 files in lib
INFO - cdoc: [Tests] 423 files in tests
INFO - cdoc: symbol registry built, 4821 symbols indexed
INFO - cdoc: rendering pages... (1/465)
INFO - cdoc: rendering pages... (50/465)
INFO - cdoc: rendering pages... (100/465)
...
INFO - cdoc: rendering complete, 465 pages
INFO - Documentation built in 34.12 seconds
```

## Next steps

- [Installation](getting-started/installation.md) — get up and running
- [Quick Start](getting-started/quickstart.md) — minimal working config
- [Configuration](configuration/single-source.md) — all the options
- [Live Demo](example/demo.md) — see the built example project
