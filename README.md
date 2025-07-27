# AutoDocs

**Documentation automation for SDK samples.**

> **Note:** This version of AutoDocs is tailored for use with Azure, leveraging Azure OpenAI and Azure Identity for authentication and LLM access. Support for other LLM providers may be added in the future.

Welcome to **AutoDocs** — the easiest way to automate descriptive comments and documentation for your code samples.

As developers, we all know the pain of writing clear comments and documentation after the fun part of coding is done. AutoDocs helps you skip the grunt work by using an LLM (Large Language Model) to auto-generate meaningful comments and markdown docs for your code.

## ✨ What It Does

AutoDocs is a GitHub Action that:

* Analyzes Python files in your `samples/` directory when changes are pushed to `main`
* Adds descriptive inline comments and step summaries using Azure OpenAI
* Creates or updates markdown documentation in a `docs/` folder
* Optionally creates pull requests with the generated changes

## 🚀 Getting Started

1. **Drop the GitHub Action into your repo**

   Copy the `comment-and-doc.yml` file into your `.github/workflows/` directory.

2. **Configure Azure OpenAI secrets**

   In your GitHub repo settings, add these repository secrets:
   * `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI endpoint URL
   * `AZURE_OPENAI_DEPLOYMENT_NAME` - Your Azure OpenAI deployment name
   * `AZURE_TENANT_ID` - Your Azure tenant ID
   * `AZURE_CLIENT_ID` - Your Azure client ID

3. **Add your Python samples**

   Place your Python sample files in a `samples/` directory in your repository.

4. **Push to main**

   Every time you push Python files to the `main` branch in the `samples/` directory, AutoDocs will:

   * Scan the changed Python files
   * Generate inline comments and step summaries using Azure OpenAI
   * Create markdown documentation in the `docs/` folder
   * Commit the changes back to your repository
   * Optionally create a pull request with the changes

## 🛠 Configuration

The workflow is configured to:

* **Trigger on**: Changes to `samples/**/*.py` files pushed to `main`
* **Skip if**: The commit message contains `[skip comment]`
* **Output**: Markdown docs in `docs/` folder with step-by-step walkthroughs
* **Features**: Link validation, clean code blocks, and comprehensive documentation

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
