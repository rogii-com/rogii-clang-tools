# rogii-clang-tools

A tiny pip-installable package that ships the LLVM helper tools **PyPI does not
provide** for the version we pin, so they can be delivered through the standard
`pip` mechanism.

Bundles (all from a single pinned LLVM release — see [NOTICE](NOTICE) for the
exact version):

| Tool | Kind | Provided as |
|------|------|-------------|
| `clang-apply-replacements` | native binary (win_amd64) | executable on `PATH` (env `Scripts/`) |
| `run-clang-tidy` | LLVM Python script | console entry point |
| `clang-tidy-diff` | LLVM Python script | console entry point |

`clang-tidy` itself is **not** bundled — it is already available on PyPI (ssciwr
wheel). This package fills only the gaps: a matching `clang-apply-replacements`
and the two tool scripts, none of which PyPI provides at the required version.

## Why this exists

PyPI does not offer `clang-apply-replacements` at the version matching our
`clang-tidy` — only older releases. That matters because the replacement-YAML
format differs across major versions, so an older `clang-apply-replacements`
**cannot apply fixes produced by a newer `clang-tidy`**. The two tool scripts
(`run-clang-tidy`, `clang-tidy-diff`) ship in no wheel at all. Publishing them
here (public, under our org) lets `pip` fetch them over its managed,
proxy-aware channel with no authentication required.

## Install

From a published GitHub Release wheel (substitute the release tag / filename):

```
pip install https://github.com/rogii-com/rogii-clang-tools/releases/download/<tag>/<wheel-filename>.whl
```

After install, the environment's `Scripts/` directory contains
`clang-apply-replacements.exe`, `run-clang-tidy.exe`, and `clang-tidy-diff.exe`,
all on `PATH` for that environment.

## Versioning

The package version mirrors the bundled LLVM release. To bump: replace
`bin/clang-apply-replacements.exe` and the two scripts from the new `llvmorg-*`
release, update `__version__` in `src/rogii_clang_tools/__init__.py` and the
versions recorded in [NOTICE](NOTICE), then cut a new release.

## Build (on Windows / win_amd64)

```
python -m pip install --upgrade build
python -m build --wheel
```

The wheel is platform-tagged `win_amd64` (it carries a native binary) but
Python-version agnostic (`py3-none`).

## License

Apache License v2.0 with LLVM Exceptions — see [LICENSE](LICENSE) and
[NOTICE](NOTICE). All bundled artifacts are unmodified LLVM components except
for local glue recorded in git history.
