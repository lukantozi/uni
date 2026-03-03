# Enabling Test Mode

Add an `igt:` block to any source group:

```yaml
sources:
  - root: tests
    nav_title: Tests
    output_dir: api/tests
    extensions: [".c"]
    igt:
      group_by: [category, mega_feature, sub_category, functionality]
```

That's all you need. The presence of `igt:` enables test parsing for that source group.

## IGT options

| Option | Default | Description |
|--------|---------|-------------|
| `group_by` | `[]` | Metadata fields to generate "By …" index pages for |
| `fields` | same as `group_by` | Which metadata fields to show on each test page |
| `extract_steps` | `false` | Parse subtest code bodies for step-by-step tables |

When `fields` is not specified it defaults to the same list as `group_by`, so you don't need to repeat yourself.

## Metadata fields

Any `Key: Value` pair in the doc comment becomes a metadata field. Common conventions:

| Field | Level | Typical values |
|-------|-------|----------------|
| `Category` | test | Core, Display, … |
| `Mega feature` | test | KMS, Memory Management, … |
| `Sub-category` | test | GEM, Framebuffer, … |
| `Functionality` | subtest | addfb, gem_create, … |
| `Description` | both | Free-form text (supports multi-line) |

Test-level fields (like Category) group all tests in a file. Subtest-level fields (like Functionality) group individual subtests and produce a different table layout on the "By …" pages.

The plugin matches field names flexibly across underscore, hyphen, and space variations — `sub_category` in config matches `Sub-category` or `Sub category` in source comments.
