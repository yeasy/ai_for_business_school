"""附录速查表必须与它自己列出的工具小节对得上。

`13_appendix/toolkit.md` 的开头声明「N 件工具」，中间用一张表做索引，
结尾的「一条使用动线」再声明一次「N 件工具」。三处是同一个数字的三份副本，
新增工具小节时极易只改其一——本测试把它们钉在一起。
"""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLKIT = ROOT / "13_appendix" / "toolkit.md"

# 结尾的「一条使用动线」是串讲，不是工具本身，不计入。
NON_TOOL_SECTIONS = ("一条使用动线",)

CN_NUMERALS = {
    "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
    "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
    "十一": 11, "十二": 12,
}


def _cn_to_int(token: str) -> int:
    return CN_NUMERALS[token]


class ToolkitIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = TOOLKIT.read_text(encoding="utf-8")

    def _table_rows(self) -> list[str]:
        # 索引表在第一个 `### ` 小节之前，后面各小节里的表格不算。
        head = self.text.split("\n### ", 1)[0]
        rows = []
        for line in head.splitlines():
            if not line.startswith("| "):
                continue
            first = line.strip().strip("|").split("|")[0].strip()
            if first == "工具" or not first or set(first) <= set("-: "):
                continue
            rows.append(first)
        return rows

    def _tool_sections(self) -> list[str]:
        titles = re.findall(r"^### (.+)$", self.text, re.M)
        return [t.strip() for t in titles if t.strip() not in NON_TOOL_SECTIONS]

    def test_every_tool_section_has_a_row_in_the_lookup_table(self):
        rows = self._table_rows()
        sections = self._tool_sections()
        self.assertEqual(
            len(sections),
            len(rows),
            f"速查表 {len(rows)} 行，工具小节 {len(sections)} 个：{sections}",
        )

    def test_declared_counts_match_the_table(self):
        rows = len(self._table_rows())
        declared = re.findall(r"([一二三四五六七八九十]+)件工具", self.text)
        self.assertTrue(declared, "toolkit.md 里找不到「N 件工具」的声明")
        for token in declared:
            self.assertEqual(
                _cn_to_int(token),
                rows,
                f"正文声明「{token}件工具」，但速查表有 {rows} 行",
            )


if __name__ == "__main__":
    unittest.main()
