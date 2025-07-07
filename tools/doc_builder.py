#!/usr/bin/env python
"""
Convert commented samples into Markdown docs.

• Scans sdk/ai/azure-ai-agents/samples/**/*.py
• Extracts DOC_TITLE / DOC_SUMMARY / DOC_STEPS/ etc.. lines
• Converts every leading "### " inline comment into a step heading
• Writes docs/samples/<same-relative-path>.md wrapped in AUTO-GENERATED markers
"""

import pathlib, re, textwrap, datetime, hashlib

DOC_ROOT = pathlib.Path("doc/samples")      # mirror of the samples tree
SAMPLE_ROOT = pathlib.Path("sdk/ai/azure-ai-agents/samples")

TITLE_RE  = re.compile(r"^#\s*DOC_TITLE:\s*(.+)", re.I)
SUMMARY_RE  = re.compile(r"^#\s*DOC_SUMMARY:\s*(.+)", re.I)
NOTES_RE   = re.compile(r"^#\s*DOC_NOTES:\s*(.+)", re.I)
STEPS_RE   = re.compile(r"^#\s*DOC_STEPS:\s*(.+)", re.I)
LINKS_RE   = re.compile(r"^#\s*DOC_LINKS:\s*(.+)", re.I)
STEP_RE   = re.compile(r"^\s*###\s+(.*)")           # step headings

TEMPLATE = """\
# {title}

_{summary}_

{notes}

## Step-by-step walk-through
{steps}
<details><summary>Full source</summary>

```python
{full_source}

</details>
Last updated: {ts}
"""

def build(sample_path: pathlib.Path):
    code = sample_path.read_text().splitlines()
    title = summary = ""
    notes = []
    steps = []
    links = []

for ln in code:
    if (m:=TITLE_RE.match(ln)):   title  = m.group(1).strip(); continue
    if (m:=SUMMARY_RE.match(ln)):   summary  = m.group(1).strip(); continue
    if (m:=NOTES_RE.match(ln)):    notes.append(m.group(1).strip()); continue
    if (m:=STEPS_RE.match(ln)):    steps.append(m.group(1).strip()); continue
    if (m:=LINKS_RE.match(ln)):    links.append(m.group(1).strip()); continue

cur_head, cur_block = None, []
for ln in code:
    if STEP_RE.match(ln):
        if cur_head: steps.append((cur_head, "\n".join(cur_block)))
        cur_head = STEP_RE.match(ln).group(1).strip()
        cur_block = []
    else:
        cur_block.append(ln)
if cur_head: steps.append((cur_head, "\n".join(cur_block)))

md_steps = []
for idx,(hd,blk) in enumerate(steps,1):
    snippet = "\n".join(
        l for l in blk.splitlines() if not NOTES_RE.match(l) and not TITLE_RE.match(l)
    )
    md_steps.append(f"### {idx}. {hd}\n```python\n{snippet}\n```\n")

rendered = TEMPLATE.format(
    title=title or sample_path.stem,
    summary=summary or "",
    notes="\n".join(notes),
    steps="\n".join(md_steps),
    links="\n".join(links),
    full_source="\n".join(code),
    ts=datetime.date.today().isoformat()
)

out_path = DOC_ROOT / sample_path.relative_to(SAMPLE_ROOT).with_suffix(".md")
out_path.parent.mkdir(parents=True, exist_ok=True)

banner = f"<!-- AUTO-GENERATED doc for {sample_path} -->"
content = f"{banner}\n{rendered}\n"

out_path.write_text(content)
print("Wrote doc ->", out_path)
