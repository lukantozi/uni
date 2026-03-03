# Cross-References

The plugin builds a symbol registry at build time and resolves references across all pages — generated API pages and hand-written docs alike.

## reST roles in doc comments

Use reST roles (portable to Sphinx):

```c
/**
 * Initialize the engine.
 *
 * Must be called before :func:`engine_run`. Configure with
 * :struct:`engine_config` first.
 *
 * :param flags: Init flags.
 * :returns: 0 on success.
 */
int engine_init(unsigned int flags);
```

### Available roles

| Role | Links to | Example |
|------|----------|---------|
| `:func:` | Function | `:func:`engine_init`` |
| `:struct:` | Struct | `:struct:`engine_config`` |
| `:union:` | Union | `:union:`my_union`` |
| `:enum:` | Enum | `:enum:`color_mode`` |
| `:macro:` | Macro | `:macro:`MAX_SIZE`` |
| `:type:` | Typedef | `:type:`uint32_t`` |
| `:var:` | Variable | `:var:`global_state`` |
| `:const:` | Constant | `:const:`DEFAULT_FLAGS`` |
| `:member:` | Struct member | `:member:`engine_config.debug`` |
| `:class:` | Class (C++) | `:class:`MyClass`` |
| `:file:` | Source file page | `:file:`engine.h`` |
| `:test:` | Test (IGT) | `:test:`kms_addfb`` |
| `:subtest:` | Subtest (IGT) | `:subtest:`kms_addfb@basic`` |

Domain-qualified forms like `:c:func:` also work.

For struct members use dot notation: `:member:`engine_config.debug``.

For files, use the bare filename if unique or qualify with the path: `:file:`core/engine.h``.

## reST roles in Markdown pages

The same roles work in hand-written Markdown:

```markdown
Call :func:`engine_init` with the appropriate flags, then pass
an :struct:`engine_config` to :func:`engine_run`.
```

## Auto-linking

When `auto_xref` is enabled (the default), backticked identifiers that match known symbols become links automatically:

```markdown
Call `engine_init()` first, then create an `engine_config` and
pass it to `engine_run()`.
```

Trailing `()` signals a function reference. Bare backticked names link if they match a struct, enum, type, etc. Filenames with C/C++ extensions also auto-link. Unknown names stay as plain code.

## Cross-referencing tests

Tests and subtests are registered in the symbol registry:

```markdown
See :test:`kms_addfb` for framebuffer tests.
The :subtest:`kms_addfb@basic` subtest covers the happy path.
```

The `test@subtest` notation mirrors IGT's `--run-subtest` convention. Short-form `:subtest:`basic`` works if the subtest name is unique across all tests.
