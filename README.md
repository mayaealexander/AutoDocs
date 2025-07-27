---

# AutoDocs

**Documentation automation for SDK samples.**

Welcome to **AutoDocs** — the easiest way to automate descriptive comments and documentation for your code samples.

As developers, we all know the pain of writing clear comments and documentation after the fun part of coding is done. AutoDocs helps you skip the grunt work by using an LLM (Large Language Model) to auto-generate meaningful comments and markdown docs for your code.

## ✨ What It Does

AutoDocs is a GitHub Action that:

* Analyzes the code in your repo when changes are pushed to `main`
* Adds descriptive inline comments using an LLM of your choice
* Creates or updates markdown documentation based on your code sample

## 🚀 Getting Started

1. **Drop the GitHub Action into your repo**

   Copy the AutoDocs GitHub Action YAML file into your `.github/workflows/` directory.

2. **Add your LLM API as a secret**

   In your GitHub repo settings, add a secret named `LLM_API_KEY` (or whatever your action expects). This could be an OpenAI API key, a local inference endpoint, etc.

3. **Push to main**

   Every time you push to the `main` branch, AutoDocs will:

   * Scan your code for undocumented functions or unclear sections
   * Send the code to your LLM endpoint
   * Automatically commit changes with updated comments and new documentation

## 🛠 Configuration

You can customize:

* The LLM provider and endpoint
* Which directories or file types to include
* The format of the generated docs (e.g., Markdown, reStructuredText)

Details are configurable via the action's input parameters (see the [workflow file](./.github/workflows/autodocs.yml)).

## 📁 Output Example

After running, you'll typically see:

* Improved inline code comments
* A new `docs/` folder with generated documentation

## ⚠️ Disclaimer

AutoDocs relies on AI-generated output, so you should still review and validate the changes before publishing or merging to production.

## 📄 License

MIT

---
