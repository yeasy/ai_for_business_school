import json
import math
import unittest
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "13_appendix" / "data" / "quantitative_cases.json"
STUDENT = ROOT / "13_appendix" / "quantitative_cases.md"
ANSWERS = ROOT / "13_appendix" / "quantitative_case_answers.md"


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class QuantitativeCaseTests(unittest.TestCase):
    def load_cases(self):
        payload = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema_version"], 1)
        return payload["cases"]

    def test_four_case_types_have_unique_ids(self):
        cases = self.load_cases()
        self.assertEqual({case["type"] for case in cases}, {"tco", "npv", "break_even", "expected_loss"})
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), 4)
        self.assertEqual(len(ids), len(set(ids)))

    def test_expected_answers_recompute_from_inputs(self):
        for case in self.load_cases():
            inputs = case["inputs"]
            if case["type"] == "tco":
                actual = (
                    Decimal(str(inputs["implementation_cost"]))
                    + Decimal(str(inputs["data_preparation_cost"]))
                    + Decimal(str(inputs["monthly_model_cost"])) * inputs["months"]
                    + Decimal(str(inputs["monthly_platform_cost"])) * inputs["months"]
                    + Decimal(str(inputs["annual_operations_cost"])) * inputs["years"]
                )
                self.assertEqual(money(actual), money(case["expected"]["tco"]))
            elif case["type"] == "npv":
                rate = Decimal(str(inputs["discount_rate"]))
                actual = -Decimal(str(inputs["initial_investment"]))
                for year, cash_flow in enumerate(inputs["annual_net_cash_flows"], 1):
                    actual += Decimal(str(cash_flow)) / ((Decimal("1") + rate) ** year)
                self.assertEqual(money(actual), money(case["expected"]["npv"]))
            elif case["type"] == "break_even":
                monthly_net = Decimal(str(inputs["monthly_benefit"])) - Decimal(
                    str(inputs["monthly_operating_cost"])
                )
                actual = math.ceil(Decimal(str(inputs["initial_investment"])) / monthly_net)
                self.assertEqual(actual, case["expected"]["break_even_month"])
            else:
                actual = sum(
                    Decimal(str(item["probability"])) * Decimal(str(item["loss"]))
                    for item in inputs["risk_scenarios"]
                )
                self.assertEqual(money(actual), money(case["expected"]["expected_loss"]))

    def test_student_and_teacher_materials_reference_every_case(self):
        cases = self.load_cases()
        student = STUDENT.read_text(encoding="utf-8")
        answers = ANSWERS.read_text(encoding="utf-8")
        for case in cases:
            self.assertIn(case["id"], student)
            self.assertIn(case["id"], answers)

    def test_book_routes_to_quantitative_cases(self):
        summary = (ROOT / "SUMMARY.md").read_text(encoding="utf-8")
        self.assertIn("13_appendix/quantitative_cases.md", summary)
        self.assertIn("13_appendix/quantitative_case_answers.md", summary)
        self.assertIn("../13_appendix/quantitative_cases.md", (ROOT / "07_value" / "7.3_cost_benefit.md").read_text(encoding="utf-8"))
        self.assertIn("../13_appendix/quantitative_cases.md", (ROOT / "07_value" / "7.4_budget.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
