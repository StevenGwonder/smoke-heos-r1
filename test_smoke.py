import unittest
from pathlib import Path


class TestSmoke(unittest.TestCase):
    def test_smoke_agy(self):
        smoke_file = Path(__file__).resolve().parent / "smoke" / "agy.txt"
        self.assertTrue(smoke_file.is_file(), f"{smoke_file} does not exist")
        self.assertEqual(smoke_file.read_text(encoding="utf-8"), "smoke-ok")

    def test_smoke_codex(self):
        smoke_file = Path(__file__).resolve().parent / "smoke" / "codex.txt"
        self.assertEqual(smoke_file.read_text(encoding="utf-8"), "smoke-ok")


if __name__ == "__main__":
    unittest.main()
