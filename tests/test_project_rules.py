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

    def test_contributing_documents_the_pdf_and_html_publication_checks(self):
        text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("npm ci --prefix tools/mermaid --ignore-scripts", text)
        self.assertIn("tools/render_mermaid.py", text)
        self.assertIn("tools/build_html_reader.py", text)
        self.assertIn("--html /tmp/ai-for-business-school.html", text)
        self.assertIn("--source-root .", text)

    def test_moderna_metric_matches_the_primary_source(self):
        for relative in ("11_org_talent/summary.md", "13_appendix/discussion.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("750 多个", text, relative)
            self.assertIn("750 个", text, relative)

    def test_references_do_not_call_linked_primary_sources_unlinked(self):
        text = (ROOT / "13_appendix" / "references.md").read_text(encoding="utf-8")
        self.assertIn("正文已为 SignalFire 报告", text)
        self.assertIn("少数材料仍没有稳定的一手链接", text)
        claims = [
            paragraph
            for paragraph in text.split("\n\n")
            if "正文未附" in paragraph or "未附外部链接" in paragraph
        ]
        for claim in claims:
            self.assertNotIn("SignalFire", claim)
            self.assertNotIn("ADP", claim)
            self.assertNotIn("BCG", claim)

    def test_guangzhou_ai_case_uses_the_accessible_official_pdf(self):
        official = "https://gxj.gz.gov.cn/attachment/7/7953/7953403/10620000.pdf"
        stale = "https://gxj.gz.gov.cn/attachment/7/7952/7952889/10620000.pdf"
        for relative in (
            "08_cases/8.1_manufacturing.md",
            "13_appendix/evidence_index.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn(official, text, relative)
            self.assertNotIn(stale, text, relative)

    def test_mit_nanda_evidence_note_matches_the_exact_numbers_used_in_body(self):
        body = (ROOT / "07_value" / "7.4_budget.md").read_text(encoding="utf-8")
        evidence = (ROOT / "13_appendix" / "evidence_index.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("9 个月以上", body)
        self.assertIn("约 90 天", body)
        self.assertNotIn("正文只采用“通常需数月且供应商方案更快”的方向结论", evidence)

    def test_python_caches_are_ignored(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")

        self.assertIn("__pycache__/", text)
        self.assertIn("*.py[cod]", text)


if __name__ == "__main__":
    unittest.main()
