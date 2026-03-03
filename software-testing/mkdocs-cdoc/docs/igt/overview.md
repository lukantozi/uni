# IGT GPU Tools Support

The plugin has built-in support for test source trees that use structured doc comments and test macros. While designed around [IGT GPU Tools](https://gitlab.freedesktop.org/drm/igt-gpu-tools) conventions, the approach works for any C test codebase that follows a similar comment structure.

## What is IGT GPU Tools?

[IGT GPU Tools](https://gitlab.freedesktop.org/drm/igt-gpu-tools) is a collection of low-level tools and tests for developing and testing DRM (Direct Rendering Manager) drivers in the Linux kernel. It is maintained by the freedesktop.org community and used by GPU driver developers working on Intel (i915/Xe), AMD, Qualcomm, and other DRM drivers.

The test suite contains hundreds of test files under `tests/`, each with structured doc comments documenting the test purpose, metadata (category, feature area, functionality), and individual subtests. The codebase also uses gtk-doc conventions in its `lib/` library headers — both of which mkdocs-cdoc was designed to handle.

## Full IGT config example

```yaml
plugins:
  - cdoc:
      project_name: igt-gpu-tools
      version_file: meson.build
      clang_args: ["-Ilib", "-Itests", "-Iinclude"]

      custom_index_pages:
        - docs/api_ref.md

      sources:
        - root: lib
          nav_title: Core API
          output_dir: api_reference/lib
          custom_index_pages:
            - docs/lib-intro.md

        - root: tests
          nav_title: Tests
          output_dir: api_reference/tests
          extensions: [".c"]
          custom_index_pages:
            - docs/tests-intro.md
          igt:
            group_by: [category, mega_feature, sub_category, functionality]

      convert_rst: true
      convert_gtkdoc: true
      appendix_code_usages: true
```
