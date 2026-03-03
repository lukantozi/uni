# Multi-Source Setup

For projects with multiple source trees (libraries, drivers, tests), use `sources:`:

```yaml
plugins:
  - cdoc:
      project_name: My Project
      version_file: version.json

      sources:
        - root: src/core
          nav_title: Core API
          output_dir: api/core

        - root: src/drivers
          nav_title: Driver API
          output_dir: api/drivers
          extensions: [".c"]
          exclude: ["*_test.c"]

        - root: src/utils
          nav_title: Utilities
          output_dir: api/utils
          index: false
          pages:
            - docs/utils-guide.md
```

## Version detection

The `version_file` is scanned for a line matching `version: 'X.Y'` (or `VERSION = "1.2.3"`, `"version": "2.0"`, etc.) — it works with JSON, YAML, Python, meson.build, or any file with a version key-value pair.

## Generated navigation

With multiple source groups a top-level overview page is generated automatically, showing the project name, a version badge, and links to each group:

```
API Reference
  Core API
    Overview
  Driver API
    Overview
  Utilities
```

All generated pages are marked as `NOT_IN_NAV` internally, so MkDocs won't warn about them not being included in your `nav` configuration.
