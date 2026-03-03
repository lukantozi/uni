# Adapting for Your Own Test Framework

The `igt:` parser key specifically enables the IGT-style parser, but the comment format is generic enough for any C test suite.

## Requirements

If your tests use `/** ... */` comments with structured `TEST:` / `SUBTEST:` blocks and key-value metadata, they will work as-is. You only need IGT-specific macros (`igt_subtest`, `igt_describe`) if you want code-level subtest discovery.

## Steps

1. Add `/** TEST: my_test_name */` comments with any metadata fields you like
2. Optionally add `/** SUBTEST: name */` blocks with per-subtest metadata
3. Set `group_by` to whichever field names you used

## Example

```c
/**
 * TEST: memory_allocation
 * Category: Core
 * Feature: Memory
 * Description: Tests for the memory allocator.
 *
 * SUBTEST: alloc-basic
 * Description: Basic allocation and free.
 * Feature: Allocation
 *
 * SUBTEST: alloc-stress
 * Description: Stress test with concurrent allocations.
 * Feature: Stress
 */
```

```yaml
sources:
  - root: tests
    nav_title: Tests
    extensions: [".c"]
    igt:
      group_by: [category, feature]
```

This generates "By Category" and "By Feature" index pages, with test metadata tables on each test page, regardless of whether you use IGT macros.
