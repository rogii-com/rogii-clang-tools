"""Build shim.

All package metadata lives in pyproject.toml. This file only customizes the
wheel tag: the distribution bundles a native win_amd64 binary
(clang-apply-replacements.exe), so the wheel must be platform-specific rather
than "any". It carries no compiled Python extension, so the tag is forced to
py3-none-<platform> — installable on any Python 3 for the matching OS/arch.

Build on the target platform (win_amd64) so <platform> resolves correctly.
"""
from setuptools import setup

try:  # setuptools >= 70.1 vendors bdist_wheel
    from setuptools.command.bdist_wheel import bdist_wheel as _bdist_wheel
except ImportError:  # older setuptools -> use the standalone wheel package
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        # Bundles a native binary -> not a pure-Python wheel.
        self.root_is_pure = False

    def get_tag(self):
        # Keep the resolved platform tag, but make it Python-version agnostic.
        _impl, _abi, plat = super().get_tag()
        return "py3", "none", plat


setup(cmdclass={"bdist_wheel": bdist_wheel})
