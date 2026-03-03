# Custom Index Pages

`custom_index_pages` lets you embed hand-written Markdown content into the generated overview pages — before the source file table and A–Z symbol index.

## Where the content appears

The generated overview page layout is:

1. **Title** and version badge
2. A–Z navigation bar
3. **→ Your custom content goes here ←**
4. Source Files table
5. Symbol Index (A–Z)

## Usage

### Single-source

```yaml
plugins:
  - cdoc:
      source_root: src/
      custom_index_pages:
        - docs/api-intro.md
        - docs/conventions.md
```

### Multi-source — per group

```yaml
plugins:
  - cdoc:
      sources:
        - root: lib
          nav_title: Core API
          custom_index_pages:
            - docs/lib-intro.md
        - root: tests
          nav_title: Tests
          custom_index_pages:
            - docs/tests-intro.md
```

### Multi-source — top-level

For the main "API Reference" page that links to all groups:

```yaml
plugins:
  - cdoc:
      custom_index_pages:
        - docs/api-overview.md
      sources:
        - root: lib
          nav_title: Core API
        - root: tests
          nav_title: Tests
```

Both levels can be combined — the top-level config adds content to the main overview page, while per-group configs add content to each group's overview.

## `custom_index_pages` vs `pages`

| | `custom_index_pages` | `pages` |
|---|---|---|
| **Where it appears** | Embedded in the overview page | Separate page in the nav sidebar |
| **Use for** | Introductory text, conventions, quick-start guides | Standalone docs that deserve their own page |
| **Cross-references** | `:file:`, `:func:`, etc. all work | Same |

## Nav warnings

Files listed in `custom_index_pages` are automatically marked as `NOT_IN_NAV` so MkDocs won't warn about them not being included in your `nav` configuration. You don't need to add them to `nav` manually.
