# Global Options

These apply to all source groups:

| Option | Default | Description |
|--------|---------|-------------|
| `project_name` | `""` | Project name on the top-level overview page |
| `version_file` | `""` | File to extract version from |
| `clang_args` | `[]` | Global clang flags (merged with per-group flags) |
| `convert_rst` | `true` | Convert reST markup to Markdown |
| `convert_gtkdoc` | `false` | Convert gtk-doc markup to reST at parse time |
| `auto_xref` | `true` | Auto-link backticked symbol names |
| `appendix_code_usages` | `false` | Append a "Referenced by" section to each symbol |
| `heading_level` | `2` | Heading depth for symbols (`2` = `##`, `3` = `###`) |
| `members` | `true` | Show struct/union/enum members |
| `signature_style` | `"code"` | How to render function signatures (`"code"` or `"plain"`) |
| `show_source_link` | `false` | Append `[source]` links to each symbol |
| `source_uri` | `""` | URI template: `https://github.com/you/repo/blob/main/{filename}#L{line}` |
| `fallback_parser` | `true` | Use regex parser when clang is unavailable |
| `parser` | `"auto"` | Parser backend: `"auto"`, `"clang"`, or `"regex"` |
| `language` | `"c"` | Source language (`"c"` or `"cpp"`) |

## Parser configuration

The `parser` option controls which parser backend is used:

- `auto` (default) — use clang if available, fall back to regex if `fallback_parser: true`
- `clang` — require libclang, error if not installed
- `regex` — always use regex parser, skip clang even if installed

The build log shows which parser is active:

```
INFO - cdoc: libclang available, parser: auto
INFO - cdoc: using libclang for parsing
```

## Full example

```yaml
plugins:
  - cdoc:
      project_name: My Project
      version_file: meson.build
      clang_args: ["-Iinclude", "-DDEBUG=0"]
      convert_rst: true
      convert_gtkdoc: true
      auto_xref: true
      appendix_code_usages: true
      heading_level: 2
      members: true
      signature_style: code
      show_source_link: true
      source_uri: "https://github.com/you/repo/blob/main/{filename}#L{line}"
      fallback_parser: true
      language: c

      sources:
        - root: src
          nav_title: API
          output_dir: api
```

## Legacy flat config

The following flat keys still work for IGT test configuration but are superseded by the nested `igt:` block in source groups:

| Flat key | Equivalent | Description |
|----------|-----------|-------------|
| `test_mode: igt` | presence of `igt:` block | Enable IGT test parsing |
| `test_group_by` | `igt.group_by` | Metadata fields for "By …" pages |
| `test_fields` | `igt.fields` | Metadata fields to display |
| `extract_test_steps` | `igt.extract_steps` | Parse subtest bodies for steps |
