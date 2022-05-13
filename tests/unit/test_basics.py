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
