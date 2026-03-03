# Multi-Group Projects: Library + Tests

Most C/C++ projects have at least two source areas: the library code and the tests that exercise it. mkdocs-cdoc lets you document both in a single site with separate navigation sections, cross-references working across groups, and per-group overview pages.

## Typical project layout

```
my-project/
  include/
    mylib.h
  src/
    core.c
    utils.c
    io.c
  tests/
    test_core.c
    test_utils.c
    test_io.c
  docs/
    index.md
    lib-intro.md
    tests-intro.md
  mkdocs.yml
```

## Configuration

```yaml
site_name: My Project

plugins:
  - search
  - cdoc:
      project_name: My Project
      version_file: version.h
      clang_args: ["-Iinclude"]

      custom_index_pages:
        - docs/api-overview.md

      sources:
        - root: src
          nav_title: Library API
          output_dir: api/lib
          extensions: [".c", ".h"]
          custom_index_pages:
            - docs/lib-intro.md

        - root: include
          nav_title: Public Headers
          output_dir: api/headers
          extensions: [".h"]

        - root: tests
          nav_title: Tests
          output_dir: api/tests
          extensions: [".c"]
          custom_index_pages:
            - docs/tests-intro.md

      convert_rst: true
      auto_xref: true
```

## What gets generated

The navigation sidebar will show:

```
My Project
  API Reference          ← top-level overview linking all groups
    Library API
      Overview           ← file table + A–Z symbol index
      core.c             ← functions, structs from this file
      utils.c
      io.c
    Public Headers
      Overview
      mylib.h
    Tests
      Overview
      test_core.c
      test_utils.c
      test_io.c
```

## Cross-references between groups

References work across all groups. A test file can link to a library function:

```c
/**
 * Test the initialization path.
 *
 * Verifies that :func:`mylib_init` returns 0 on success
 * and populates the :struct:`mylib_context` correctly.
 */
void test_init(void) { ... }
```

The links resolve to the correct pages in the Library API section, regardless of which group the reference appears in.

Similarly, hand-written pages in `docs/` can reference any symbol:

```markdown
The library provides `mylib_init()` for setup and `mylib_cleanup()`
for teardown. See the full API in the Library API section.
```

With `auto_xref: true`, backticked symbols become links automatically.

## Custom overview content

The `custom_index_pages` option embeds your hand-written content at the top of each group's overview page — before the source file table and symbol index. This is the place for introductions, architecture overviews, or getting-started guides:

**`docs/lib-intro.md`:**

```markdown
## About the Library

The core library provides device management, I/O helpers, and a
configuration framework. Start with `mylib_init()` to create a
context, then use the module-specific APIs.

### Key modules

- `core.c` — initialization, context management, lifecycle
- `utils.c` — string helpers, memory pools, logging
- `io.c` — file I/O, buffered readers, async operations
```

**`docs/tests-intro.md`:**

```markdown
## Test Suite

Each test file corresponds to a library module. Tests use
standard assertions and are designed to run independently.
```

## Adding structured test metadata

If your tests use structured doc comments, you can enable test mode for richer documentation with metadata tables, subtest listings, and "By …" index pages:

```yaml
sources:
  - root: tests
    nav_title: Tests
    output_dir: api/tests
    extensions: [".c"]
    igt:
      group_by: [category, feature]
```

This requires `TEST:` / `SUBTEST:` blocks in your doc comments:

```c
/**
 * TEST: test_core
 * Category: Core
 * Feature: Initialization
 * Description: Tests for the core initialization path.
 *
 * SUBTEST: init-basic
 * Description: Basic init and cleanup cycle.
 *
 * SUBTEST: init-double
 * Description: Verify double-init is handled gracefully.
 */
```

See [Enabling Test Mode](../igt/enabling.md) for the full reference on test metadata options.

## Separating public and private APIs

A common pattern is to document public headers separately from implementation files:

```yaml
sources:
  - root: include
    nav_title: Public API
    output_dir: api/public
    extensions: [".h"]

  - root: src
    nav_title: Implementation
    output_dir: api/internal
    extensions: [".c"]
    exclude: ["**/test_*"]
```

This gives users a clean "Public API" section with just the headers, while keeping the full implementation details accessible in a separate section.

## Source links

To add links back to your repository from each symbol:

```yaml
plugins:
  - cdoc:
      show_source_link: true
      source_uri: "https://github.com/you/my-project/blob/main/{filename}#L{line}"
```

Each function, struct, and enum heading will get a `[source]` link pointing to the exact file and line in your repo.
