"""Discoverable integration tests for the repository's stdlib test scripts."""
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryChecks(unittest.TestCase):
    def run_script(self, name):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tests" / name)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)

    def test_skill_contract(self):
        self.run_script("test_skill_contract.py")

    def test_new_layers(self):
        self.run_script("test_new_layers.py")
