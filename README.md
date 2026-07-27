# 🚀 AI Startup MCP

<div align="center">

# 💻 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/MCP-Model_Context_Protocol-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Anthropic-Claude-191919?style=for-the-badge" />
</p>


</div>
<br>

An AI-powered **Model Context Protocol (MCP)** server that acts as a virtual startup consultant. It helps founders, entrepreneurs, and product teams validate ideas, analyze competitors, research pricing, audit websites, and generate investor-focused insights using Large Language Models.

---

# ✨ Features

* 💡 Startup Idea Validation
* 🏆 Competitor Discovery & Analysis
* 💰 Pricing Landscape Analysis (USD & INR)
* 🌍 Market Research
* 🌐 Website & Landing Page Audit
* 📋 Suggested Product Features
* 💼 Investor's Point of View
* 📊 Complete Startup Report

All responses are AI-generated using Groq-powered LLMs.

---

# 🛠️ Tech Stack

* Python
* FastMCP
* Model Context Protocol (MCP)
* Groq API
* Llama 3.3 70B
* STDIO Transport

---

# 📁 Project Structure

```text
AI-Startup-MCP/
│
├── mcp_server.py
├── requirements.txt
├── LICENSE
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ArshZaidi/AI-Startup-MCP
cd AI-Startup-MCP
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

*Never commit your `.env` file.*

---

# ▶️ Running the MCP Server

Start the server:

```bash
python mcp_server.py
```

The server communicates using the **STDIO transport**, making it compatible with MCP clients such as Claude Desktop, Cursor, Cline, Continue, and other MCP-compatible applications.

---

# 🔌 Connecting to Claude Desktop

Open Claude Desktop's MCP configuration.

Add your server to claude_desktop_config.json:

```json

{
  "mcpServers": {
    "startup-ai": {
      "command": "python",
      "args": [
        "/absolute/path/to/mcp_server.py"
      ]
    }
  }
}


```

Restart Claude Desktop. completely.

Your tools should now appear under **Connectors**, where Claude can discover and invoke them automatically. Claude Desktop supports local MCP servers through its configuration or packaged desktop extensions.

---

# 💻 Connecting from Cursor

Cursor supports MCP servers.

Add a new MCP server in Cursor's MCP settings using the same command and arguments used for Claude Desktop.

After restarting Cursor, the available tools will be automatically discovered.

---

# 🤖 Connecting from Other MCP Clients

This server follows the standard Model Context Protocol and should work with any compatible client that supports launching local MCP servers.

Typical configuration requires:

* Python executable
* Path to `mcp_server.py`
* Required environment variables

---

# 🧰 Available Tools

| Tool                    | Description                               |
| ----------------------- | ----------------------------------------- |
| Startup Validation      | Evaluate startup ideas                    |
| Competitor Analysis     | Discover competitors and compare products |
| Pricing Analysis        | Analyze pricing landscape                 |
| Website Audit           | UX, SEO and CRO evaluation                |
| Suggested Features      | AI-powered product roadmap                |
| Investor's POV          | VC-style investment analysis              |
| Complete Startup Report | Full business analysis                    |

---

# 💡 Example Prompt

```
Evaluate my AI startup for students.

Generate a complete startup report including:
- Competitor analysis
- Pricing analysis
- Website audit
- Investor's perspective
```

Claude will automatically invoke the relevant MCP tools.

---

# 🌍 Making This Server Public

This repository currently provides a **local MCP server**.

Anyone can:

1. Clone the repository
2. Install the dependencies
3. Add it to their preferred MCP client
4. Start using the tools locally

---

# 🤝 Contributing

Contributions are welcome.

Feel free to open issues, submit pull requests, or suggest new startup analysis tools.

---

# 📄 License

MIT License

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
