# Quick Start

## Minimal setup

Add the plugin to your `mkdocs.yml` and point it at a source directory:

```yaml
plugins:
  - search
  - cdoc:
      source_root: src/
```

This scans all `.c` and `.h` files under `src/`, generates per-file API pages, and adds them to the nav under "API Reference".

## What you get

For a source tree like:

```
src/
  engine.h
  engine.c
  utils.c
```

The plugin generates:

```
API Reference
  Overview          ← file table + A–Z symbol index
    engine.h        ← functions, structs, enums from this file
    engine.c
    utils.c
```

Each file page includes function signatures with parameter tables, struct/enum member listings, and cross-reference links to related symbols.

## Doc comment format

The plugin extracts `/** ... */` style comments:

```c
/**
 * Initialize the engine.
 *
 * Must be called before :func:`engine_run`. Configure with
 * :struct:`engine_config` first.
 *
 * :param flags: Init flags.
 * :returns: 0 on success.
 */
int engine_init(unsigned int flags);
```

reST field lists (`:param:`, `:returns:`) are converted to Markdown automatically. Cross-references like `:func:` and `:struct:` become clickable links.

## Multiple source groups

For larger projects, organize sources into groups:

```yaml
plugins:
  - cdoc:
      project_name: My Project
      sources:
        - root: src/core
          nav_title: Core API
        - root: src/drivers
          nav_title: Drivers
```

Each group gets its own overview page and A–Z index. A top-level "API Reference" page links to all groups.

## Next steps

- [Single-source configuration](../configuration/single-source.md) — all options for simple projects
- [Multi-source configuration](../configuration/multi-source.md) — options for multi-group setups
- [Cross-references](../features/cross-references.md) — linking between symbols and pages
