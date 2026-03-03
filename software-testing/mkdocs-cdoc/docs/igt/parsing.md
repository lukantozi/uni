# What It Parses

## Structured doc comments

File-scope `TEST:` blocks with nested `SUBTEST:` blocks:

```c
/**
 * TEST: kms_addfb
 * Category: Display
 * Mega feature: KMS
 * Sub-category: Framebuffer
 * Description: Tests for the DRM framebuffer creation ioctl.
 *
 * SUBTEST: basic
 * Description: Check if addfb2 works with a valid handle.
 * Functionality: addfb
 */
```

## Standalone subtest blocks

Placed above individual functions:

```c
/**
 * SUBTEST: attach-debug-metadata
 * Functionality: metadata
 * Description:
 *      Read debug metadata when vm_bind has it attached.
 */
static void test_metadata_attach(int fd, unsigned int flags) { ... }
```

## Test macros in code

`igt_subtest()`, `igt_describe()`, and `igt_subtest_with_dynamic()`:

```c
igt_describe("Check that invalid legacy set-property calls are "
             "correctly rejected by the kernel.");
igt_subtest("invalid-properties-legacy") {
    ...
}
```

## How sources are merged

Both doc comments and code macros are parsed and merged:

1. Subtests from `SUBTEST:` blocks and `igt_subtest()` calls are combined
2. `igt_describe()` takes priority for descriptions
3. Then standalone `SUBTEST:` blocks
4. Then the main `TEST:` block

Multi-line `igt_describe()` strings (concatenated across lines) are handled. Format-string subtests like `igt_subtest("%s")` are automatically excluded.
