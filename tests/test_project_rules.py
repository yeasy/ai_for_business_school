import tempfile
import unittest
from pathlib import Path

from check_project_rules import collect_issues


ROOT = Path(__file__).resolve().parents[1]


class ProjectRulesTests(unittest.TestCase):
    def make_valid_project(self, root):
        (root / "01_topic").mkdir()
        (root / "README.md").write_text("# Book\n", encoding="utf-8")
        (root / "01_topic" / "1.1_intro.md").write_text(
            "## 1.1 Intro\n\nValid text.\n", encoding="utf-8"
        )
        (root / "SUMMARY.md").write_text(
            "# Summary\n\n* [Book](README.md)\n* [Intro](01_topic/1.1_intro.md)\n",
            encoding="utf-8",
        )

    def test_flags_gitbook_bot_escape_asset_and_heading_remnants(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_valid_project(root)
            chapter = root / "01_topic" / "1.1_intro.md"
            chapter.write_text(
                "# 1.1 Intro\n\n\\*\\*escaped\\*\\*\n"
                "![asset](../.gitbook/assets/chart.png)\n",
                encoding="utf-8",
            )
            assets = root / ".gitbook" / "assets"
            assets.mkdir(parents=True)
            (assets / "chart.png").write_bytes(b"duplicate")

            issues = collect_issues(root)

            self.assertTrue(any("escaped bold" in issue for issue in issues), issues)
            self.assertTrue(any(".gitbook/assets" in issue for issue in issues), issues)
            self.assertTrue(any("heading level" in issue for issue in issues), issues)

    def test_flags_summary_duplicates_missing_entries_and_broken_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_valid_project(root)
            (root / "01_topic" / "1.2_missing.md").write_text(
                "## 1.2 Missing\n\n[Broken](not-there.md)\n", encoding="utf-8"
            )
            (root / "SUMMARY.md").write_text(
                "# Summary\n\n* [Book](README.md)\n* [Again](README.md)\n"
                "* [Broken](no-such-file.md)\n",
                encoding="utf-8",
            )

            issues = collect_issues(root)

            self.assertTrue(any("duplicate SUMMARY" in issue for issue in issues), issues)
            self.assertTrue(any("missing from SUMMARY" in issue for issue in issues), issues)
            self.assertTrue(any("broken link" in issue for issue in issues), issues)

    def test_repository_passes_project_rules(self):
        self.assertEqual(collect_issues(ROOT), [])

    def test_evidence_index_has_chinese_quotes_and_explicit_sources(self):
        text = (ROOT / "13_appendix" / "evidence_index.md").read_text(encoding="utf-8")
        forbidden_quotes = (
            '"灯塔工厂"',
            '"天眼"',
            '"超级工厂"',
            '"超级智能黑灯工厂"',
            '"化合物设计"',
            '"用 AI 开发新药"',
            '"AI 制药公司"',
            '"前端环节"',
            '"新药上市周期砍半"',
            '"前端"',
            '"约"',
        )

        self.assertFalse(any(quote in text for quote in forbidden_quotes))
        self.assertNotIn("正文未附链接", text)

    def test_contributing_commands_are_portable(self):
        text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertNotIn("/Users/", text)
        self.assertIn("python3 ../format_checker.py .", text)
        self.assertIn("python3 ../validate_codeblocks.py .", text)

    def test_moderna_metric_matches_the_primary_source(self):
        for relative in ("11_org_talent/summary.md", "13_appendix/discussion.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("750 多个", text, relative)
            self.assertIn("750 个", text, relative)


if __name__ == "__main__":
    unittest.main()
