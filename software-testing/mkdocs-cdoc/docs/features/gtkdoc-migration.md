# gtk-doc Migration

If your codebase uses gtk-doc markup, the plugin can convert it automatically at parse time.

## Enable in config

```yaml
plugins:
  - cdoc:
      convert_gtkdoc: true
```

## Conversion table

| gtk-doc | Converts to |
|---------|------------|
| `function_name()` | `:func:`function_name`` |
| `#TypeName` | `:type:`TypeName`` |
| `#Struct.field` | `:member:`Struct.field`` |
| `%CONSTANT` | `:const:`CONSTANT`` |
| `@param: desc` | `:param param: desc` |
| `Returns:` | `:returns:` |
| `\|[ code ]\|` | fenced code block |

## Batch conversion CLI

To permanently migrate source files from gtk-doc to reST markup (one-time operation):

```bash
# Preview changes
python -m mkdocs_cdoc.convert src/ --dry-run

# Convert in-place
python -m mkdocs_cdoc.convert src/

# Convert with backup files
python -m mkdocs_cdoc.convert src/ --backup
```

This modifies the actual source files, converting gtk-doc notation to reST roles that work with both mkdocs-cdoc and Sphinx. After migration, you can set `convert_gtkdoc: false` since the source files already use reST markup.
