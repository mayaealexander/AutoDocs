#!/usr/bin/env python
"""
AutoDocs – turn commented Python samples into Markdown docs (docs/ folder).
"""

from __future__ import annotations
import argparse, datetime, pathlib, re, sys

# regex patterns
TITLE_RE   = re.compile(r"^#\s*DOC_TITLE:\s*(.+)",            re.I)
SUMMARY_RE = re.compile(r"^#\s*DOC_(SUMMARY|BLURB):\s*(.+)",  re.I)
NOTES_RE   = re.compile(r"^#\s*DOC_NOTES?:\s*(.+)",           re.I)
LINKS_RE   = re.compile(r"^#\s*DOC_LINKS?:\s*(.+)",           re.I)
STEP_RE    = re.compile(r"^\s*###\s+(.*)")                    # ### Step heading

# helper: any metadata line?
def _is_meta(line: str) -> bool:
    return any(r.match(line) for r in (TITLE_RE, SUMMARY_RE, NOTES_RE, LINKS_RE))

# Markdown template
MD_TEMPLATE = """\
<!-- AUTO‑GENERATED doc for {source_rel} -->
# {title}

{summary_block}

{notes_block}

## Step‑by‑step walk‑through
{steps_block}

{links_block}
<details><summary>Full source</summary>

```python
{full_source}
```
</details>
Last updated: {timestamp}
"""

#Helper functions:

def extract_metadata(lines: list[str]) -> dict[str, list[str] | str]:
    """Pull DOC_* tags from the top comments."""
    meta: dict[str, list[str] | str] = {"notes": [], "links": []}
    for ln in lines:
        if m := TITLE_RE.match(ln):
            meta["title"] = m.group(1).strip()
        elif m := SUMMARY_RE.match(ln):
            meta["summary"] = m.group(2).strip()
        elif m := NOTES_RE.match(ln):
            meta["notes"].append(m.group(1).strip())
        elif m := LINKS_RE.match(ln):
            meta["links"].append(m.group(1).strip())
        elif not ln.startswith("#"): # real code starts → stop scanning
            break
    return meta

def split_sections(lines: list[str]) -> list[tuple[str, list[str], list[str]]]:
    """Return [(heading, summary_lines, code_lines)] blocks, incl. pre‑heading code as 'Prelude'.
    summary_lines: contiguous leading # comments (not metadata) for each section.
    code_lines: rest of the code in the section (comments removed).
    """
    sections: list[tuple[str, list[str], list[str]]] = []
    hdr: str = "Prelude"
    block: list[str] = []
    for ln in lines:
        if _is_meta(ln): #skip metadata lines entirely
            continue
        if m := STEP_RE.match(ln):
            sections.append((hdr, [], block))  # summary will be extracted later
            hdr, block = m.group(1).strip(), []
        else:
            block.append(ln)
    sections.append((hdr, [], block))

    # Extract summary and code for each section
    def extract_summary_and_code(block: list[str]) -> tuple[list[str], list[str]]:
        summary = []
        code = []
        in_summary = True
        for ln in block:
            if in_summary and ln.strip().startswith("#") and not _is_meta(ln):
                summary.append(ln.lstrip("# ").rstrip())
            elif ln.strip() == '' and in_summary:
                # allow blank lines in summary
                summary.append('')
            else:
                in_summary = False
                code.append(ln)
        # Remove trailing blank lines from summary
        while summary and summary[-1].strip() == '':
            summary.pop()
        return summary, code

    result = []
    for hdr, _, block in sections:
        summary, code = extract_summary_and_code(block)
        result.append((hdr, summary, code))
    return result


def build_doc(sample: pathlib.Path, in_root: pathlib.Path, out_root: pathlib.Path) -> None:
    """Convert one Python sample into its .md doc."""
    lines = sample.read_text().splitlines()
    meta = extract_metadata(lines)
    if "title" not in meta:
        print(f"‑ Skipping {sample} (no DOC_TITLE)")
        return

    # filter metadata from full‑source accordion as well
    clean_source = "\n".join(ln for ln in lines if not _is_meta(ln))

    # build step blocks
    step_md: list[str] = []
    sections = split_sections(lines)
    # Prelude suppression: skip if first section is Prelude and has no real code
    start_idx = 0
    if sections:
        prelude_hdr, prelude_summary, prelude_code = sections[0]
        if prelude_hdr == "Prelude":
            # Check if prelude_code is empty or only whitespace/comments
            if not any(ln.strip() and not ln.strip().startswith('#') for ln in prelude_code):
                start_idx = 1  # skip Prelude
    for idx, (hdr, summary_lines, code_lines) in enumerate(sections[start_idx:], 1):
        if not hdr or (not code_lines and not summary_lines):
            continue
        summary_md = ("\n".join(summary_lines) + "\n") if summary_lines else ""
        snippet = "\n".join(code_lines)
        step_md.append(
            f"Step {idx}: {hdr}\n"
            + (f"{summary_md}\n" if summary_md else "")
            + (f"```python\n{snippet}\n```\n" if snippet.strip() else "")
        )

    md = MD_TEMPLATE.format(
        source_rel   = sample.relative_to(in_root),
        title        = meta.get("title", sample.stem),
        summary_block= f"_{meta.get('summary','')}_\n" if meta.get("summary") else "",
        notes_block  = "\n".join(f"- {n}" for n in meta["notes"]) if meta["notes"] else "",
        steps_block  = "\n".join(step_md),
        links_block  = ("## Resources\n" +
                    "\n".join(f"* {l}" for l in meta["links"]) + "\n") if meta["links"] else "",
        full_source  = clean_source,
        timestamp    = datetime.date.today().isoformat(),
    )

    dst = out_root / f"{sample.stem}.md"              # flat docs/ folder
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(md, encoding="utf-8")
    action = "updated" if dst.exists() else "created"
    print(f"{action} {dst}")


def main() -> None:
    ap = argparse.ArgumentParser(description= "Generate docs from commented samples")
    ap.add_argument("files", nargs="*", help="Specific .py files to process")
    ap.add_argument("--list-file", help="Text file of .py paths (one per line)")
    ap.add_argument("--input-root", default="samples", help="Sample root dir")
    ap.add_argument("--output-root", default="docs", help="Docs output dir")
    args = ap.parse_args()
    in_root  = pathlib.Path(args.input_root)
    out_root = pathlib.Path(args.output_root)

# Build list of files to process
    paths: list[pathlib.Path] = []
    if args.list_file:
        paths += [pathlib.Path(p.strip())
            for p in pathlib.Path(args.list_file).read_text().splitlines()
            if p.strip()]
    paths += [pathlib.Path(p) for p in args.files]
    if not paths:
        paths = list(in_root.rglob("*.py"))

    if not paths:
        print("No Python files to process."); sys.exit(0)

    for fp in paths:
        try:
            build_doc(fp, in_root, out_root)
        except Exception as exc:
            print(f"Failed on {fp}: {exc}")

if __name__ == "__main__":
    main()