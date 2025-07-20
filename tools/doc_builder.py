#!/usr/bin/env python
"""
AutoDocs – turn commented Python samples into Markdown docs (docs/ folder).
"""

from __future__ import annotations
import argparse, datetime, pathlib, re, sys

# ── regex patterns ────────────────────────────────────────────────────────────
TITLE_RE   = re.compile(r"^#\s*DOC_TITLE:\s*(.+)",            re.I)
SUMMARY_RE = re.compile(r"^#\s*DOC_(SUMMARY|BLURB):\s*(.+)",  re.I)
NOTES_RE   = re.compile(r"^#\s*DOC_NOTES?:\s*(.+)",           re.I)
LINKS_RE   = re.compile(r"^#\s*DOC_LINKS?:\s*(.+)",           re.I)
STEP_RE    = re.compile(r"^\s*###\s+(.*)")                    # ### Step heading

# helper: any metadata line?
def _is_meta(line: str) -> bool:
    return any(r.match(line) for r in (TITLE_RE, SUMMARY_RE, NOTES_RE, LINKS_RE))

# ── Markdown template ─────────────────────────────────────────────────────────
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
    hdr, block = "Prelude," []
    for ln in lines:
        if _is_meta(ln): #skip metadata lines entirely
            continue
        if m := STEP_RE.match(ln):
            sections.append((hdr, block))
            hdr, block = m.group(1).strip(), []
        else:
            block.append(ln)
    sections.append((hdr, block))
    return sections


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
    for idx, (hdr, code_lines) in enumerate(split_sections(lines), 1):
        if not hdr or not code_lines:
            continue
        snippet = "\n".join(code_lines)
        step_md.append(
            f"### {idx}. {hdr}\n```python\n{snippet}\n```\n")

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
    print("wrote", dst)


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