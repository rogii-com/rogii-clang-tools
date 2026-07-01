"""Console-script wrappers for the bundled LLVM tool scripts.

run-clang-tidy's main() is a coroutine, so it needs an asyncio wrapper to be
usable as a setuptools console_scripts entry point. clang-tidy-diff's main() is
synchronous and is exposed directly.
"""
import asyncio

from . import clang_tidy_diff, run_clang_tidy


def run_clang_tidy_main() -> None:
    asyncio.run(run_clang_tidy.main())


def clang_tidy_diff_main() -> None:
    clang_tidy_diff.main()
