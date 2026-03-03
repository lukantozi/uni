# Single-Source Setup

When you have a single source tree, use the flat `autodoc_*` shortcuts:

```yaml
plugins:
  - cdoc:
      source_root: src/
      autodoc_nav_title: My API
      autodoc_output_dir: reference
      autodoc_extensions: [".c", ".h", ".hpp"]
      autodoc_exclude: ["**/internal/*", "test_*.c"]
      autodoc_index: true
      custom_index_pages:
        - docs/api-intro.md
        - docs/conventions.md
      autodoc_pages:
        - docs/getting-started.md
        - docs/migration-guide.md
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `source_root` | `""` | Path to the source tree |
| `autodoc_nav_title` | `"API Reference"` | Nav section heading |
| `autodoc_output_dir` | `"API Reference"` | Where generated pages go |
| `autodoc_extensions` | `[".c", ".h"]` | File extensions to scan |
| `autodoc_exclude` | `[]` | Glob patterns to skip |
| `autodoc_index` | `true` | Generate an overview page with file table and A–Z index |
| `custom_index_pages` | `[]` | Markdown files to embed in the overview page (before the source file table) |
| `autodoc_pages` | `[]` | Extra hand-written pages to include in the nav section |
| `autodoc` | `true` | Enable autodoc page generation (set `false` to only use inline directives) |

## Disabling features

Setting `autodoc_index: false` disables the overview page — useful if you only want individual file pages without a landing page.

Setting `autodoc: false` disables all automatic page generation entirely. You'd then use [inline directives](../features/inline-directives.md) to pull specific symbols into hand-written pages.
