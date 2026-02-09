# ScrapeFlow-MCP

An implementation of the **Model Context Protocol (MCP)** that gives AI Agents the ability to scrape and interpret live web data with high precision.

## Features
- **FastMCP Framework:** Built using the latest 2026 standards for AI-interop.
- **Headless Automation:** Uses Playwright to handle JavaScript-heavy sites.
- **Context Optimization:** Automatically cleans HTML to save LLM tokens.

## Getting Started
1. Clone this repo: `git clone https://github.com/RootedDreamsBlog/ScrapeFlow-MCP.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Install Playwright: `playwright install chromium`
4. Run the server: `python server.py`

## 1. How to use with Claude Desktop
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "scrapeflow": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```
## 2. How to use with MCP Inspector

1. Open your terminal in your project folder.
2. Run this command:

```bash
npx @modelcontextprotocol/inspector python server.py
```
3. Click the URL provided (usually http://localhost:6274).
4. In the browser, click "Connect", then go to the "Tools" tab. You should see search_and_summarize. You can enter a URL there and see the results immediately.

## Preview

