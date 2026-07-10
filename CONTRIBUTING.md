# 贡献指南

本仓库的可编辑真相源是 Markdown 与各章节本地图片。请保持改动小、来源可核验，并在提交前完成下列检查。

## 内容与图片

- `SUMMARY.md` 必须以 `# Summary` 开头，并收录每个正文与附录 Markdown 文件且不重复。
- `1.1_xxx.md` 这类编号小节的文档标题使用二级标题（`##`），其下小节从三级标题开始。
- 图片放在所属章节的 `_images/` 目录，并用相对路径引用。禁止新增 `.gitbook/assets/` 或把同一图片复制到多个位置。
- 不要提交 GitBook 自动转义的粗体语法（例如反斜杠转义的星号），也不要让自动格式化工具批量改写表格、标题层级或链接目标。
- 事实、数字和直接引语须给出可访问来源；优先引用原始报告、监管文件或机构公告，并在证据索引说明口径和局限。

## 提交前验证

在仓库根目录运行：

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 check_project_rules.py .
PUPPETEER_SKIP_DOWNLOAD=true npm ci --prefix tools/mermaid --ignore-scripts
export PATH="$PWD/tools/mermaid/node_modules/.bin:$PATH"
python3 tools/render_mermaid.py --book-dir . --svg-out /tmp/ai-for-business-school-mermaid
python3 tools/build_html_reader.py \
  --book-dir . \
  --title "商学院 AI 必修课：企业如何迎接智能体浪潮" \
  --svg-dir /tmp/ai-for-business-school-mermaid \
  --out /tmp/ai-for-business-school.html
mdpress build --format pdf --output /tmp/ai-for-business-school.pdf
python3 tools/verify_artifacts.py \
  --title "商学院 AI 必修课：企业如何迎接智能体浪潮" \
  --pdf /tmp/ai-for-business-school.pdf \
  --html /tmp/ai-for-business-school.html \
  --source-root . \
  --checksums /tmp/SHA256SUMS
```

如果本仓库位于 `books` 协调工作区内，再运行协调层校验器：

```bash
python3 ../format_checker.py .
python3 ../validate_codeblocks.py .
```

最后用 `git diff --check` 检查空白错误，并人工打开生成的 PDF 与 HTML，抽查目录、中文字体、表格、图片、Mermaid 图和翻页导航是否完整。
