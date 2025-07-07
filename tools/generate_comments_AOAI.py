import os, sys, pathlib
from openai import AzureOpenAI # pip install openai>=1.14.0

#  Azure client setup 
ENDPOINT        = os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/"
API_KEY         = os.environ["AZURE_OPENAI_KEY"]
DEPLOYMENT_NAME = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
API_VERSION     = "2025-01-01-preview"      

client = AzureOpenAI(
    azure_endpoint = ENDPOINT,
    api_key        = API_KEY,
    api_version    = API_VERSION,
)

# Prompt template
SYSTEM_PROMPT = (
    # ────────── ROLE ──────────
    "You are an expert Python reviewer tasked with:\n"
    "• Adding concise, helpful inline comments.\n"
    "• Emitting structured metadata lines that downstream tooling will turn into a doc page.\n\n"

    # ────────── INLINE COMMENT RULES ──────────
    "INLINE-COMMENT RULES:\n"
    "1. Use `#` for short, line-level explanations.\n"
    "2. Comments must be briefer than the code they annotate.\n"
    "3. Do NOT wrap the file in markdown fences or add prose before/after.\n\n"

    # ────────── DOC METADATA RULES ──────────
    "DOC-METADATA RULES (optional, but encouraged):\n"
    "• Place these *above* the code, one per line, starting with `# DOC_`.\n"
    "  # DOC_TITLE:  One-line title for the doc page\n"
    "  # DOC_BLURB:  Short tagline shown under the title\n"
    "  # DOC_NOTE:   Free-form paragraph (repeatable) for background or tips\n"
    "  # DOC_LINKS:  Markdown links to external resources (repeatable)\n"
    "• Metadata lines will be stripped from the code and fed into a doc builder.\n\n"

    # ────────── STEP HEADINGS ──────────
    "STEP HEADINGS:\n"
    "• Use `### Step heading` *inside* the code to mark major sections.\n"
    "• The doc builder will turn each heading into a numbered step with the "
    "following code block.\n\n"

    # ────────── HARD CONSTRAINTS ──────────
    "HARD CONSTRAINTS:\n"
    "• Output must be syntactically valid Python.\n"
    "• Absolutely no ``` fences, HTML, or extra wrappers.\n"
)

def annotate_source(code: str) -> str:
    """Call the Azure OpenAI deployment and return the commented code."""
    response = client.chat.completions.create(
        model     = DEPLOYMENT_NAME,    
        messages  = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": code},
        ],
        temperature = 0.3,
        max_tokens  = 1000,
    )
    return response.choices[0].message.content


# File IO helpers
def process_file(rel_path: str, repo_root: pathlib.Path) -> None:
    file_path = repo_root / rel_path
    print("▶ commenting", file_path)
    original = file_path.read_text(encoding="utf-8")
    commented = annotate_source(original)
    file_path.write_text(commented, encoding="utf-8")

def main() -> None:
    if len(sys.argv) != 3:
        print("usage: generate_comments_AOAI.py <updated_files.txt> <repo_root>")
        sys.exit(1)

    updated_list = pathlib.Path(sys.argv[1])
    repo_root    = pathlib.Path(sys.argv[2])

    py_files = [ln.strip() for ln in updated_list.read_text().splitlines() if ln.strip().endswith(".py")]
    print(f"Found {len(py_files)} Python file(s) to process.")
    for rel in py_files:
        process_file(rel, repo_root)

if __name__ == "__main__":
    main()
