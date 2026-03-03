# Inline Directives

Pull specific symbols into hand-written pages:

```markdown
::: c:autofunction
    :file: engine.h
    :name: engine_init

::: c:autodoc
    :file: uart.c
```

## Available directives

| Directive | What it renders |
|-----------|----------------|
| `autodoc` | All documented symbols from the file |
| `autofunction` | A single function |
| `autostruct` | A single struct with members |
| `autounion` | A single union with members |
| `autoenum` | A single enum with values |
| `automacro` | A single macro |
| `autovar` | A single variable |
| `autotype` | A single typedef |

## Using without automatic page generation

When using inline directives without automatic page generation, set `autodoc: false`:

```yaml
plugins:
  - cdoc:
      source_root: src/
      autodoc: false
```

Then use directives in your hand-written pages to include only the symbols you want. This gives you full control over the documentation layout while still getting parsed signatures, parameter tables, and cross-references.

## Mixed mode

You can also combine automatic page generation with inline directives. The auto-generated pages cover the full API, while your hand-written pages use directives to highlight specific symbols in tutorials or guides.
