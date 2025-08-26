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

## 🚀 Quick Start & Prerequisites (one-time)

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
   > You can use **Secrets** instead of **Variables** if your org policy requires it; the examples below read from `vars.*`.

6. **Allow Actions to write**
   - Repo → **Settings → Actions → General → Workflow permissions** → **Read and write**.

7. **Call Action into any Workflow**
   - Repos call this action with *mayaealexander/AutoDocs@v1* inside your own workflow
   - The calling workflow should include the following permissions:
      - contents: write
      - pull-requests: write
      - id-token: write
   - See a minimal example case below

## Minimal Usage (example of calling the action)
   ```yaml
   name: AutoDocs
   on:
   push:
      branches: [ main ]
      paths:
         - 'samples/**/*.py' #customizable

   jobs:
   autodocs:
      runs-on: ubuntu-latest
      permissions:
         contents: write                     # commit generated files
         pull-requests: write                # open/update a PR (optional)
         id-token: write                     # OIDC -> Entra ID login
      steps:
         - uses: actions/checkout@v4         # must checkout your repo before calling the action
         - uses: mayaealexander/AutoDocs@v1  # call AutoDocs
         with:
            azure-tenant-id:              ${{ vars.AZURE_TENANT_ID }}
            azure-client-id:              ${{ vars.AZURE_CLIENT_ID }}
            azure-openai-endpoint:        ${{ vars.AZURE_OPENAI_ENDPOINT }}
            azure-openai-deployment-name: ${{ vars.AZURE_OPENAI_DEPLOYMENT_NAME }}
   ```
   That’s it. Push a change to a file under samples/ and AutoDocs will:
   1. Diff to find changed .py files
   2. Comment them with Azure OpenAI (OIDC auth)
   3. Build Markdown docs into docs/
   4. Commit the changes (and open a PR if enabled)


## Inputs (action options)
| Input                           | Required | Default                            | Description                                                                 |
|---------------------------------|:--------:|------------------------------------|-----------------------------------------------------------------------------|
| `azure-tenant-id`               |   ✅     | —                                  | Entra Directory (tenant) ID used for OIDC                                   |
| `azure-client-id`               |   ✅     | —                                  | App Registration (client) ID with a federated credential for this repo      |
| `azure-openai-endpoint`         |   ✅     | —                                  | Azure OpenAI endpoint, e.g. `https://NAME.openai.azure.com/`                |
| `azure-openai-deployment-name`  |   ✅     | —                                  | Azure OpenAI deployment name (e.g., `gpt-4.1`)                              |
| `samples-root`                  |    ❌    | `samples`                          | Root folder of sample `.py` files                                           |
| `docs-root`                     |    ❌    | `docs`                             | Output folder for Markdown docs                                             |
| `sample-glob`                   |    ❌    | `samples/**/*.py`                  | Glob for files to watch                                                     |
| `sample-paths`                  |    ❌    | —                                  | Comma-separated explicit paths (skips diff)                                 |
| `python-version`                |    ❌    | `3.10`                             | Python version used in the runner                                           |
| `create-pr`                     |    ❌    | `true`                             | Open/update a PR with changes                                               |
| `pr-branch`                     |    ❌    | `bot/auto-comment`                 | Bot branch for PRs                                                          |
| `pr-title`                      |    ❌    | `Add inline comments and docs via AI assistant` | PR title                                                       |
| `pr-body`                       |    ❌    | `Auto-generated; please review`    | PR description                                                              |
| `commit-user-name`              |    ❌    | `AI Comment Assistant`             | Commit author name                                                          |
| `commit-user-email`             |    ❌    | `${{ github.actor }}@users.noreply.github.com` | Commit author email                                             |
| `commenter-script`              |    ❌    | *(bundled)*                        | Path to code commenter (override to customize)                              |
| `doc-builder-script`            |    ❌    | *(bundled)*                        | Path to doc builder (override to customize)                                 |
| `requirements-path`             |    ❌    | *(bundled)*                        | Requirements file (override to pin deps)                                    |

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
