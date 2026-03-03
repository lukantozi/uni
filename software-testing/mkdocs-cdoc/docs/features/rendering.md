# Rendering

## Parameter tables

Function parameters render as a table. When type information is available (from clang), a Type column is added with cross-reference links for struct/custom types.

## Pointer return types

Functions returning pointers (e.g. `char *get_name(...)`) render as "Pointer to `char`" rather than showing `*` in the name.

## Example sections

If a doc comment contains `Example:`, the description and code render side-by-side, similar to the Stripe API documentation layout:

```c
/**
 * Create a new engine instance.
 *
 * Example:
 *
 *     struct engine_config cfg = { .debug = true };
 *     struct engine *e = engine_create(&cfg);
 */
struct engine *engine_create(struct engine_config *cfg);
```

## Notes/Note sections

If a doc comment contains `Notes:` or `Note:`, the content renders as a Material Design warning admonition:

```
!!! warning "Note"
    This function is not thread-safe.
    Call only from the main thread.
```

## Underscore-prefixed symbols

Functions with `_` or `__` prefix sort by the name without the prefix. `__engine_reset` sorts under **E** in the A–Z index.

## Signature styles

The `signature_style` option controls how function signatures are displayed:

- `"code"` (default) — rendered in a code block with syntax highlighting
- `"plain"` — rendered as inline text

## Source links

When `show_source_link` is enabled with a `source_uri` template, each symbol gets a `[source]` link pointing to the file and line in your repository:

```yaml
show_source_link: true
source_uri: "https://github.com/you/repo/blob/main/{filename}#L{line}"
```
