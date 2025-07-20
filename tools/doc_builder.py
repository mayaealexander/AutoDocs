#!/usr/bin/env python
"""
AutoDocs – turn commented Python samples into Markdown docs.

Usage examples
--------------
# Build docs for all samples
python tools/doc_builder.py

# Build docs only for files in a list (GitHub Action)
python tools/doc_builder.py --list-file /tmp/updated_files.txt

# Build docs for explicit files
python tools/doc_builder.py samples/foo.py samples/bar.py
"""

from __future__ import annotations
import pathlib, re, datetime, argparse, sys

# ── regexes ──────────────────────────────────────────────────────────────
TITLE_RE   = re.compile(r"^#\s*DOC_TITLE:\s*(.+)",   re.I)
SUMMARY_RE = re.compile(r"^#\s*DOC_(SUMMARY|BLURB):\s*(.+)", re.I)  # accept either tag
NOTES_RE   = re.compile(r"^#\s*DOC_NOTES?:\s*(.+)",  re.I)
LINKS_RE   = re.compile(r"^#\s*DOC_LINKS?:\s*(.+)",  re.I)
STEP_RE    = re.compile(r"^\s*###\s+(.*)")           # headings inside code

# ── markdown template ────────────────────────────────────────────────────
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

def split_sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    """Return [(heading, code_lines)] blocks, incl. pre‑heading code as 'Prelude'."""
    sections: list[tuple[str, list[str]]] = []
    hdr, block = "Prelude", []
    for ln in lines:
        if m := STEP_RE.match(ln):
            sections.append((hdr, block))
            hdr, block = m.group(1).strip(), []
        else:
            block.append(ln)
    sections.append((hdr, block))
    return sections

def render_markdown(meta: dict[str, list[str] | str],
    sections: list[tuple[str, list[str]]],
    source_rel: pathlib.Path,
    full_source: str) -> str:
    """Fill the MD template with formatted pieces."""
    summary_block = f"_{meta.get('summary', '')}_\n" if meta.get("summary") else ""
    notes_block = "\n".join(f"- {n}" for n in meta["notes"]) if meta["notes"] else ""
    links_block = ("## Resources\n" +
    "\n".join(f"* {l}" for l in meta["links"]) + "\n") if meta["links"] else ""
    step_md: list[str] = []
    for idx, (hdr, code_lines) in enumerate(sections, 1):
        if not hdr or not code_lines:
            continue
        snippet = "\n".join(code_lines)
        step_md.append(f"### {idx}. {hdr}\n```python\n{snippet}\n```\n")

    return MD_TEMPLATE.format(
        source_rel   = source_rel,
        title        = meta.get("title", source_rel.stem),
        summary_block= summary_block,
        notes_block  = notes_block,
        steps_block  = "\n".join(step_md),
        links_block  = links_block,
        full_source  = full_source,
        timestamp    = datetime.date.today().isoformat(),
    )

def build_doc(sample: pathlib.Path, in_root: pathlib.Path, out_root: pathlib.Path) -> None:
    """Convert one Python sample into its .md doc."""
    lines = sample.read_text().splitlines()
    meta = extract_metadata(lines)
    if "title" not in meta:
        print(f"‑ Skipping {sample} (no DOC_TITLE)")
        return

    markdown = render_markdown(
        meta      = meta,
        sections  = split_sections(lines),
        source_rel= sample.relative_to(in_root),
        full_source="\n".join(lines),
    )

    dst = out_root / sample.relative_to(in_root).with_suffix(".md")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(markdown, encoding="utf-8")
    print("wrote", dst)


def main() -> None:
    ap = argparse.ArgumentParser(description= "Generate docs from commented samples")
    ap.add_argument("files", nargs="*", help="Specific .py files to process")
    ap.add_argument("--list-file", help="Text file of .py paths (one per line)")
    ap.add_argument("--input-root", default="samples", help="Sample root dir")
    ap.add_argument("--output-root", default="docs/autodocs", help="Docs output dir")
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
        print("No Python files to process.")
        sys.exit(0)

    for fp in paths:
        try:
            build_doc(fp, in_root, out_root)
        except Exception as exc:
            print(f"Failed on {fp}: {exc}")

if __name__ == "__main__":
    main()