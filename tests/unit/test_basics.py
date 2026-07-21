<<<<<<< HEAD
"""Basic tests that do not require Django."""

import unittest

import toml  # type: ignore
from nornir_pyntc import __version__ as project_version


class TestVersion(unittest.TestCase):
    """Test Version is the same."""

    def test_version(self):
        """Verify that pyproject.toml version is same as version specified in the package."""
        poetry_version = toml.load("./pyproject.toml")["tool"]["poetry"]["version"]
        self.assertEqual(project_version, poetry_version)
=======
"""Basic tests that do not require Nornir Pyntc."""

import os
import re
import unittest

import toml


class TestDocsReleaseNotes(unittest.TestCase):
    """Test that mkdocs has the release notes for the current version."""

    def test_version_file_found(self):
        """Verify that if the current version has no letters, which would see in alpha or beta has an associated release note file."""
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        poetry_path = os.path.join(parent_path, "pyproject.toml")
        project_version = toml.load(poetry_path)["tool"]["poetry"]["version"]

        docs_path = os.path.join(parent_path, "docs")
        release_notes_files = [file for file in os.listdir(f"{docs_path}/admin/release_notes/") if file.endswith(".md")]
        version_pattern = re.compile(r"^(\d+)\.(\d+)\.\d+$")

        match = version_pattern.match(project_version)
        # If there is no match, then it is likely an alpha or beta version and we can skip this test.
        if match:
            major, minor = match.groups()
            version_str = f"version_{major}.{minor}.md"
            if version_str not in release_notes_files:
                self.fail(f"Release note file for version {version_str} not found in release notes folder.")
>>>>>>> 5442b74 (Cookie initially baked targeting develop by NetworkToCode Cookie Drift Manager Tool)
