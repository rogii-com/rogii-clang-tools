"""Console-script shim for the bundled clang-apply-replacements binary.

setuptools cannot ship a native binary as a plain script (it tries to tokenize
it), so the binary is packaged as package data and exposed here through a
console_scripts entry point. The shim forwards all arguments and the exit code,
with stdio inherited, so it is transparent to callers (e.g. run-clang-tidy).
"""
import subprocess
import sys
from pathlib import Path

_BINARY = Path(__file__).with_name("_bin") / "clang-apply-replacements.exe"


def main() -> None:
    if not _BINARY.is_file():
        sys.stderr.write(f"clang-apply-replacements binary not found: {_BINARY}\n")
        sys.exit(1)
    sys.exit(subprocess.run([str(_BINARY), *sys.argv[1:]]).returncode)
