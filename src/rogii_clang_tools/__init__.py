"""rogii-clang-tools — pip-installable LLVM helper tools.

Ships the pieces PyPI does not provide for LLVM 22:
  * clang-apply-replacements (native binary, bundled as a script)
  * run-clang-tidy       (LLVM tool script, console entry point)
  * clang-tidy-diff      (LLVM tool script, console entry point)

Versioned as <bundled LLVM release>.<packaging revision>, e.g. 22.1.7.1.
"""

__version__ = "22.1.7.1"
