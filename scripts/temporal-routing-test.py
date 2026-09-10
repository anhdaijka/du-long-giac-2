"""Regression tests for routing; no claim of semantic temporal validation."""
from pathlib import Path
import runpy
import tempfile
import unittest

api = runpy.run_path(str(Path(__file__).with_name("temporal-routing-check.py")))


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in api["SURFACES"] + [api["CONTRACT"]]:
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("D-064\n" + api["CONTRACT"], encoding="utf-8")

    def test_current_routing(self):
        self.assertEqual(api["check"](self.root), [])

    def test_missing_policy_fails(self):
        (self.root / api["CONTRACT"]).unlink()
        self.assertTrue(api["check"](self.root))

    def test_stale_reference_fails_even_with_override(self):
        p = self.root / "GEMINI.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nplot/timeline.md", encoding="utf-8")
        self.assertTrue(api["check"](self.root))

    def test_missing_entry_routing_fails(self):
        (self.root / "GEMINI.md").write_text("No router", encoding="utf-8")
        self.assertTrue(api["check"](self.root))


if __name__ == "__main__":
    unittest.main()
