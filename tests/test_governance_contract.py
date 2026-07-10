import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = ("利益相关者影响", "公平性", "无障碍", "申诉", "禁止用途", "退出机制")
CONTRACT_FILES = (
    ROOT / "12_governance" / "12.1_risk_map.md",
    ROOT / "12_governance" / "12.3_governance_system.md",
    ROOT / "13_appendix" / "toolkit.md",
    ROOT / "13_appendix" / "discussion.md",
    ROOT / "13_appendix" / "teaching_guide.md",
)


class GovernanceContractTests(unittest.TestCase):
    def test_six_dimensions_are_present_in_every_governance_artifact(self):
        missing = []
        for path in CONTRACT_FILES:
            text = path.read_text(encoding="utf-8")
            for dimension in DIMENSIONS:
                if dimension not in text:
                    missing.append(f"{path.relative_to(ROOT)}: {dimension}")
        self.assertEqual(missing, [])

    def test_teaching_rubric_makes_governance_a_scored_deliverable(self):
        text = (ROOT / "13_appendix" / "teaching_guide.md").read_text(encoding="utf-8")
        self.assertIn("治理六维契约", text)
        self.assertRegex(text, r"治理六维契约[^\n]*\d+\s*分")


if __name__ == "__main__":
    unittest.main()
