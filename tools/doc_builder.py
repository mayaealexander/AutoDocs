#!/usr/bin/env python
"""
AutoDocs: Convert commented Python samples into Markdown documentation.

Usage:
    python doc_builder.py [file1.py file2.py ...] [--input-root samples] [--output-root docs]

- Scans Python files (default: in samples/)
- Extracts DOC_TITLE / DOC_SUMMARY / DOC_STEPS / etc. lines
- Converts every leading "### " inline comment into a step heading
- Writes docs/<same-relative-path>.md wrapped in AUTO-GENERATED markers

This script is designed to be called by a GitHub Action or manually.
"""

import pathlib, re, textwrap, datetime, argparse, sys

TITLE_RE  = re.compile(r"^#\s*DOC_TITLE:\s*(.+)", re.I)
SUMMARY_RE  = re.compile(r"^#\s*DOC_SUMMARY:\s*(.+)", re.I)
NOTES_RE   = re.compile(r"^#\s*DOC_NOTES:\s*(.+)", re.I)
STEPS_RE   = re.compile(r"^#\s*DOC_STEPS:\s*(.+)", re.I)
LINKS_RE   = re.compile(r"^#\s*DOC_LINKS:\s*(.+)", re.I)
STEP_RE   = re.compile(r"^\s*###\s+(.*)")           # step headings

TEMPLATE = """\
# {title}

{summary}

{notes}

## Step-by-step walk-through
{steps}

{links}
<details><summary>Full source</summary>

```python
{full_source}
```

</details>
Last updated: {ts}
"""

def build(sample_path: pathlib.Path, input_root: pathlib.Path, output_root: pathlib.Path):
    code = sample_path.read_text().splitlines()
    title = summary = ""
    notes = []
    steps = []
    links = []

    # Extract DOC_* metadata
    for ln in code:
        if (m:=TITLE_RE.match(ln)):   title  = m.group(1).strip(); continue
        if (m:=SUMMARY_RE.match(ln)):   summary  = m.group(1).strip(); continue
        if (m:=NOTES_RE.match(ln)):    notes.append(m.group(1).strip()); continue
        if (m:=STEPS_RE.match(ln)):    steps.append(m.group(1).strip()); continue
        if (m:=LINKS_RE.match(ln)):    links.append(m.group(1).strip()); continue

    # Extract step headings and blocks
    cur_head, cur_block = None, []
    for ln in code:
        if STEP_RE.match(ln):
            if cur_head: steps.append((cur_head, "\n".join(cur_block)))
            cur_head = STEP_RE.match(ln).group(1).strip()
            cur_block = []
        else:
            cur_block.append(ln)
    if cur_head: steps.append((cur_head, "\n".join(cur_block)))

    # Format steps for markdown
    md_steps = []
    for idx,(hd,blk) in enumerate([s for s in steps if isinstance(s, tuple)],1):
        snippet = "\n".join(
            l for l in blk.splitlines() if not NOTES_RE.match(l) and not TITLE_RE.match(l)
        )
        md_steps.append(f"### {idx}. {hd}\n```python\n{snippet}\n```\n")

    rendered = TEMPLATE.format(
        title=title or sample_path.stem,
        summary=summary or "",
        notes="\n\n".join(f"- {n}" for n in notes),
        steps="\n".join(md_steps),
        links="\n".join(f"* {l}" for l in links),
        full_source="\n".join(code),
        ts=datetime.date.today().isoformat()
    )

    out_path = output_root / sample_path.relative_to(input_root).with_suffix(".md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    banner = f"<!-- AUTO-GENERATED doc for {sample_path} -->"
    content = f"{banner}\n{rendered}\n"

    out_path.write_text(content)
    print("Wrote doc ->", out_path)


def main():
    parser = argparse.ArgumentParser(description="AutoDocs: Convert commented Python samples into Markdown docs.")
    parser.add_argument('files', nargs='*', help='Python files to process (default: all in samples/)')
    parser.add_argument('--input-root', default='samples', help='Root directory for input samples')
    parser.add_argument('--output-root', default='docs', help='Root directory for output docs')
    args = parser.parse_args()

    input_root = pathlib.Path(args.input_root)
    output_root = pathlib.Path(args.output_root)

    if args.files:
        files = [pathlib.Path(f) for f in args.files]
    else:
        files = list(input_root.rglob('*.py'))

    if not files:
        print("No Python files found to process.")
        sys.exit(0)

    for f in files:
        try:
            build(f, input_root, output_root)
        except Exception as e:
            print(f"Failed to process {f}: {e}")

if __name__ == "__main__":
    main()
