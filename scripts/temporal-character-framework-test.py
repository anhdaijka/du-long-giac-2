from pathlib import Path
import runpy
import tempfile
import unittest

api = runpy.run_path(str(Path(__file__).with_name("temporal-character-framework-check.py")))


class FrameworkCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        destination = self.root / "migration/restructure_2026_09/temporal-character-framework.md"
        destination.parent.mkdir(parents=True)
        required = "\n".join(f"| {key} | approved |" for key in api["REQUIRED"])
        destination.write_text("D-065 R-91 NOT GAME FACT NOT PROSE AUTHORIZATION không thay receipt Không tạo registry\n" + required, encoding="utf-8")
        for name in api["ROUTERS"]:
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("temporal-character-framework.md", encoding="utf-8")

    def test_complete_framework_passes(self):
        self.assertEqual(api["check"](self.root), [])

    def test_missing_decision_fails(self):
        p = self.root / "migration/restructure_2026_09/temporal-character-framework.md"
        p.write_text(p.read_text(encoding="utf-8").replace("| TQ-01 | approved |\n", ""), encoding="utf-8")
        self.assertTrue(api["check"](self.root))

    def test_missing_router_fails(self):
        (self.root / "AGENTS.md").write_text("", encoding="utf-8")
        self.assertTrue(api["check"](self.root))


if __name__ == "__main__":
    unittest.main()
