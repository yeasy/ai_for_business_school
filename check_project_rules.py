#!/usr/bin/env python3
"""Validate the book's Markdown structure and local references."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
NUMBERED_CHAPTER_RE = re.compile(r"^\d+\.\d+_.*\.md$")
CONTENT_DIR_RE = re.compile(r"^\d{2}_")


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _local_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    if not target or target.startswith("#"):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
        return None
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def _book_markdown(root: Path) -> list[Path]:
    paths = [root / "README.md", root / "epilogue.md"]
    for child in root.iterdir():
        if child.is_dir() and CONTENT_DIR_RE.match(child.name):
            paths.extend(child.rglob("*.md"))
    return sorted(path for path in paths if path.is_file())


def collect_issues(root: Path | str) -> list[str]:
    root = Path(root).resolve()
    issues: list[str] = []
    summary = root / "SUMMARY.md"
    markdown = _book_markdown(root)

    assets = root / ".gitbook" / "assets"
    if assets.exists():
        issues.append(".gitbook/assets must not exist; use each chapter's _images directory")

    scan_paths = markdown + ([summary] if summary.is_file() else [])
    for path in scan_paths:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        if "\\*\\*" in text:
            issues.append(f"{rel}: escaped bold syntax is not allowed")
        if ".gitbook/assets" in text:
            issues.append(f"{rel}: .gitbook/assets reference is not allowed")

        if NUMBERED_CHAPTER_RE.match(path.name):
            first_heading = next(
                (line for line in text.splitlines() if re.match(r"^#+\s+", line)), ""
            )
            if not first_heading.startswith("## ") or first_heading.startswith("### "):
                issues.append(f"{rel}: numbered chapter heading level must be ##")

        in_fence = False
        offset = 0
        for line in text.splitlines(keepends=True):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if not in_fence:
                for match in LINK_RE.finditer(line):
                    target = _local_target(match.group(1))
                    if target is None:
                        continue
                    candidate = (path.parent / target).resolve()
                    if candidate.is_dir():
                        candidate = candidate / "README.md"
                    if not candidate.exists():
                        number = _line_number(text, offset + match.start())
                        issues.append(f"{rel}:{number}: broken link -> {target}")
            offset += len(line)

    if not summary.is_file():
        issues.append("SUMMARY.md: missing")
        return sorted(set(issues))

    summary_text = summary.read_text(encoding="utf-8")
    if not summary_text.startswith("# Summary\n"):
        issues.append("SUMMARY.md: first heading must be '# Summary'")

    entries: list[str] = []
    for match in LINK_RE.finditer(summary_text):
        target = _local_target(match.group(1))
        if target is not None:
            entries.append(Path(target).as_posix())
    seen: set[str] = set()
    for entry in entries:
        if entry in seen:
            issues.append(f"SUMMARY.md: duplicate SUMMARY entry -> {entry}")
        seen.add(entry)

    expected = {path.relative_to(root).as_posix() for path in markdown}
    for missing in sorted(expected - set(entries)):
        issues.append(f"{missing}: missing from SUMMARY")

    return sorted(set(issues))


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    issues = collect_issues(root)
    if issues:
        for issue in issues:
            print(issue)
        return 1
    print("Project rules: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
