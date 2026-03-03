# Source Group Options

Each entry under `sources:` accepts:

| Option | Default | Description |
|--------|---------|-------------|
| `root` | *(required)* | Path to the source tree |
| `nav_title` | `API (<dirname>)` | Nav section heading |
| `output_dir` | `API Reference/<dirname>` | Where generated pages go |
| `extensions` | `[".c", ".h"]` | File extensions to scan |
| `exclude` | `[]` | Glob patterns to skip |
| `clang_args` | `[]` | Extra flags, appended to global `clang_args` |
| `index` | `true` | Generate an overview page |
| `custom_index_pages` | `[]` | Markdown files to embed in the overview page (before the source file table) |
| `pages` | `[]` | Extra hand-written pages to include in the nav |
| `igt` | — | IGT test framework options ([see IGT docs](../igt/enabling.md)) |

## Example

```yaml
sources:
  - root: src/core
    nav_title: Core API
    output_dir: api/core
    extensions: [".c", ".h"]
    exclude: ["**/internal/*"]
    clang_args: ["-Iinclude/core"]
    custom_index_pages:
      - docs/core-intro.md
    pages:
      - docs/core-conventions.md

  - root: src/drivers
    nav_title: Drivers
    output_dir: api/drivers
    extensions: [".c"]

  - root: tests
    nav_title: Tests
    output_dir: api/tests
    extensions: [".c"]
    igt:
      group_by: [category, functionality]
```

## Per-group clang flags

Each group can specify its own `clang_args` which are appended to the global ones. This is useful when different source trees need different include paths:

```yaml
plugins:
  - cdoc:
      clang_args: ["-Iinclude"]    # global
      sources:
        - root: lib
          clang_args: ["-Ilib/private"]    # lib gets: -Iinclude -Ilib/private
        - root: drivers
          clang_args: ["-Idrivers/hw"]     # drivers gets: -Iinclude -Idrivers/hw
```
