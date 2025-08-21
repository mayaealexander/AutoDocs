# AutoDocs

**Documentation automation for SDK samples.**

> **Note:** This version of AutoDocs is tailored for use with **Azure**, leveraging **Azure OpenAI** and **Azure Identity (OIDC to Entra ID)** for authentication and LLM access. Support for other LLM providers may be added in the future.

Welcome to **AutoDocs** — the easiest way to automate descriptive comments and documentation for your code samples.

As developers, we all know the pain of writing clear comments and documentation after the fun part of coding is done. AutoDocs helps you skip the grunt work by using an LLM (Large Language Model) to auto-generate meaningful comments and markdown docs for your code.

---

## ✨ What It Does

AutoDocs is a GitHub Action that:

- Analyzes Python files in your `samples/` directory when changes are pushed to `main`
- Adds **concise inline `#` comments** and **step summaries** using Azure OpenAI
- Creates or updates **Markdown documentation** in your `docs/` folder
- Optionally creates a **pull request** with the generated changes
- Uses **GitHub OIDC → Entra ID** (no API keys in your repo)

---

## 🚀 Quick Start (as a reusable GitHub Action)

Most users will consume AutoDocs as a **reusable action** in their own repo.

### 1) Prerequisites (one-time)

1. **Azure OpenAI resource + model deployment**
   - You have an Azure OpenAI resource (e.g., `https://YOUR-RESOURCE.openai.azure.com/`).
   - You’ve deployed a model (e.g., deployment name: `gpt-4.1`).

2. **Entra ID app registration for GitHub OIDC**
   - In **Microsoft Entra ID → App registrations → New registration**.
   - Save your **Application (client) ID** and **Directory (tenant) ID**.

3. **Add a GitHub federated credential to your app**
   - App → **Certificates & secrets → Federated credentials → Add credential**.
   - **Provider:** GitHub.
   - Scope it to your repo and branch (usually `main`).
   - This lets GitHub Actions exchange its **OIDC token** for an **Entra access token**.

4. **Grant the app access to Azure OpenAI**
   - Azure Portal → your **Azure OpenAI** resource → **Access control (IAM)** → **Add role assignment**.
   - Assign a role that can invoke the endpoint (e.g., **Cognitive Services User** or **Contributor**).

5. **Add GitHub Actions *Variables*** (repo settings)
   - Repo → **Settings → Secrets and variables → Actions → Variables → New variable**:
     - `AZURE_OPENAI_ENDPOINT` → `https://YOUR-RESOURCE.openai.azure.com/`
     - `AZURE_OPENAI_DEPLOYMENT_NAME` → your deployment name (e.g., `gpt-4.1`)
     - `AZURE_TENANT_ID` → your Entra **Directory (tenant) ID**
     - `AZURE_CLIENT_ID` → your app’s **Application (client) ID**
   > You can use **Secrets** instead of **Variables** if your org policy requires it; the included workflow defaults to `vars.*`.

6. **Allow Actions to write**
   - Repo → **Settings → Actions → General → Workflow permissions** → **Read and write**.

### 2) Add a small workflow in your repo

Create **`.github/workflows/autodocs.yml`** in your repository:

```yaml
name: AutoDocs (Azure)

on:
  push:
    branches: [main]
    paths:
      - 'samples/**/*.py'   # adjust if your samples live elsewhere

permissions:
  contents: write
  pull-requests: write
  id-token: write   # required for OIDC → Entra ID

jobs:
  autodocs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout your repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # Call the AutoDocs composite action (this repository)
      - name: Run AutoDocs
        uses: mayaealexander/AutoDocs@v1
        with:
          # Required: your Azure/OpenAI OIDC settings (usually from repo Variables)
          azure-openai-endpoint:        ${{ vars.AZURE_OPENAI_ENDPOINT }}
          azure-openai-deployment-name: ${{ vars.AZURE_OPENAI_DEPLOYMENT_NAME }}
          azure-tenant-id:              ${{ vars.AZURE_TENANT_ID }}
          azure-client-id:              ${{ vars.AZURE_CLIENT_ID }}

          # Optional overrides (defaults shown):
          sample-glob:        'samples/**/*.py'
          working-directory:  '.'
          commenter-script:   'tools/generate_comments_AOAI.py'
          doc-builder-script: 'tools/doc_builder.py'
          docs-output-dir:    'docs'
          pr-branch:          'bot/auto-comment'
          create-pr:          'true'   # set to 'false' if your org blocks

## 🔧 Customization

AutoDocs can be customized for different use cases:

### **File Patterns**
Modify the trigger path in `.github/workflows/comment-and-doc.yml`:
```yaml
paths:
  - 'your-directory/**/*.py'  # Change to your preferred directory
  - 'src/**/*.js'            # Add other file types
  - 'examples/**/*.py'       # Multiple directories
```

### **Different LLM Providers**
Replace Azure OpenAI with other providers by modifying `tools/generate_comments_AOAI.py`:
* **OpenAI**: Use `openai.OpenAI()` instead of `AzureOpenAI()`
* **Local Models**: Connect to local inference endpoints
* **Other Cloud Providers**: Adapt for AWS, Google Cloud, etc.

### **Documentation Formats**
Modify `tools/doc_builder.py` to generate different output formats:
* **reStructuredText**: For Sphinx documentation
* **HTML**: For web-based documentation
* **Custom Templates**: Modify `MD_TEMPLATE` for your needs

### **Integration Examples**
* **SDK Documentation**: Perfect for API client libraries
* **Tutorial Generation**: Convert code examples into step-by-step guides
* **Code Review**: Automated commenting for pull requests
* **Educational Content**: Generate explanations for learning materials

### **Advanced Customization**
* **Custom Prompts**: Modify `SYSTEM_PROMPT` in the commenter script
* **Step Detection**: Change regex patterns for different code structures
* **Output Structure**: Customize markdown templates and sections
* **Validation Rules**: Add custom checks for code quality or style

## 📁 Output Example

After running, you'll typically see:

* **Enhanced Python files** with inline comments and step summaries
* **Markdown documentation** in `docs/` folder with:
  * Step-by-step walkthroughs
  * Clean code examples
  * Resource links
  * Full source code with comments

## ⚠️ Disclaimer

AutoDocs relies on AI-generated output, so you should still review and validate the changes before publishing or merging to production.


## 📄 License

MIT
