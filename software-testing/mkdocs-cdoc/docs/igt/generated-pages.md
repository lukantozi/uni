# Generated Pages

## Navigation structure

The nav sidebar shows:

```
Tests
  Overview              ← file table + A–Z symbol index
  By Category           ← tests grouped by Category field
  By Mega Feature       ← tests grouped by Mega Feature field
  By Sub Category       ← tests grouped by Sub-category field
  By Functionality      ← subtests grouped by Functionality field
```

## "By …" pages

Each **"By …" page** groups tests under headings matching the field values. Under each value, every test gets its own subheading with a table of its subtests and descriptions.

Test-level fields (like Category) produce pages where tests are listed under each value. Subtest-level fields (like Functionality) produce pages where individual subtests are grouped, with links back to their parent test page.

## Test pages

Each **test page** shows:

- A metadata table with the test-level fields
- The full subtest listing with anchor links per subtest
- Optionally step-by-step tables when `extract_steps: true` is set

## Cross-referencing

Tests and subtests are registered in the symbol registry:

```markdown
See :test:`kms_addfb` for framebuffer tests.
The :subtest:`kms_addfb@basic` subtest covers the happy path.
```

The `test@subtest` notation mirrors IGT's `--run-subtest` convention. Short-form `:subtest:`basic`` works if the subtest name is unique across all tests.
