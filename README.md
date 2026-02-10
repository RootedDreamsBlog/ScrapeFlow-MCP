# ScrapeFlow-MCP

An implementation of the **Model Context Protocol (MCP)** that gives AI Agents like Claude the ability to scrape and interpret live web data with high precision.

## Features
- **FastMCP Framework:** Built using the latest 2026 standards for AI-interop.
- **Headless Automation:** Uses Playwright to handle JavaScript-heavy sites.
- **Context Optimization:** Automatically cleans HTML to save LLM tokens.
- **Smart Caching:** Caches scraped content for 10 minutes to avoid redundant requests.
- **Configurable:** Adjustable character limits and metadata options.

---

## Prerequisites

Before you begin, make sure you have:
- **Python 3.8+** installed ([Download here](https://www.python.org/downloads/))
- **Claude Desktop App** installed ([Download here](https://claude.ai/download))
- Basic familiarity with the terminal/command line

---

## Installation

### 1. Clone or Download This Repository
```bash
git clone https://github.com/RootedDreamsBlog/ScrapeFlow-MCP
cd ScrapeFlow-MCP
```

Or download and extract the ZIP file, then navigate to the folder in your terminal.

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browser
```bash
playwright install chromium
```

This downloads the Chromium browser that Playwright uses for scraping.

---

## Setup with Claude Desktop

### Step 1: Find Your `server.py` Absolute Path

You need the **full path** to your `server.py` file.

**On Mac/Linux:**
```bash
cd /path/to/ScrapeFlow-MCP
echo "$(pwd)/server.py"
```

**On Windows (PowerShell):**
```powershell
cd C:\path\to\ScrapeFlow-MCP
Write-Host "$(Get-Location)\server.py"
```

**Copy the output!** Example:
- Mac: `/Users/yourname/Documents/ScrapeFlow-MCP/server.py`
- Windows: `C:\Users\yourname\Documents\ScrapeFlow-MCP\server.py`

---

### Step 2: Locate Your Claude Desktop Config File

**On Mac:**
```bash
open ~/Library/Application\ Support/Claude/
```

**On Windows (Command Prompt):**
```cmd
explorer %APPDATA%\Claude
```

**On Windows (PowerShell):**
```powershell
explorer $env:APPDATA\Claude
```

This opens the Claude configuration folder. Look for `claude_desktop_config.json`.

---

### Step 3: Edit the Config File

If the file doesn't exist, create it. Then add this configuration:

**Mac Example:**
```json
{
  "mcpServers": {
    "scrapeflow": {
      "command": "python3",
      "args": ["/Users/yourname/Documents/ScrapeFlow-MCP/server.py"]
    }
  }
}
```

**Windows Example:**
```json
{
  "mcpServers": {
    "scrapeflow": {
      "command": "python",
      "args": ["C:/Users/yourname/Documents/ScrapeFlow-MCP/server.py"]
    }
  }
}
```

**Important Notes:**
- Replace the path with YOUR actual path from Step 1
- On Windows, use forward slashes (`/`) or double backslashes (`\\`)
- If you use a virtual environment, use the full path to that Python executable

---

### Step 4: Restart Claude Desktop

**Completely quit** Claude Desktop (don't just close the window), then reopen it.

**On Mac:** `Cmd + Q` to quit
**On Windows:** Right-click the taskbar icon and select "Quit"

---

## Testing Your MCP Server

Once Claude Desktop is restarted, open a new chat and try these test prompts:

###  Easy Test Sites (Start Here)
```
Can you scrape https://example.com and tell me what it says?
```
```
Use the search_and_summarize tool to get content from https://news.ycombinator.com
```
```
Scrape https://lite.cnn.com and summarize the top headlines
```

### Advanced Tests
```
Get the content from https://www.bbc.com/news with max_chars set to 3000
```
```
Scrape https://github.com/trending and tell me what's trending
```

### ⚠Sites That May Not Work
Some websites have strong anti-bot protection and may timeout:
- Forbes, Medium (paywalls)
- Amazon, eBay (heavy JavaScript)
- Sites with CAPTCHAs

For these sites, the tool will return an error message with suggestions.

---

## Alternative Testing Method: MCP Inspector

If you want to test without Claude Desktop, use the MCP Inspector:

### 1. Install Node.js
Download from [nodejs.org](https://nodejs.org/)

### 2. Run the Inspector
```bash
cd /path/to/ScrapeFlow-MCP
npx @modelcontextprotocol/inspector python server.py
```

### 3. Open the Browser Interface
- The terminal will show a URL like `http://localhost:6274`
- Click it or paste it into your browser
- Click "Connect" → Go to "Tools" tab
- You'll see `search_and_summarize` - try entering a URL there

---

## How It Works

When you ask Claude to scrape a website:

1. Claude recognizes it should use the `search_and_summarize` tool
2. Your MCP server receives the URL
3. Playwright launches a headless browser and visits the page
4. The HTML is cleaned (removing scripts, ads, navigation)
5. Text content is extracted and cached
6. Claude receives the cleaned content and can answer your questions

---

## Troubleshooting

### "Tool not found" or Claude doesn't use the tool

**Solution:**
1. Check the config file path is correct
2. Make sure you completely quit and restarted Claude Desktop
3. Check Claude Desktop logs:
    - Mac: `~/Library/Logs/Claude/mcp*.log`
    - Windows: `%APPDATA%\Claude\logs\mcp*.log`

### "Command not found: python"

**Solution:**
Try changing `"command": "python"` to `"command": "python3"` in your config file.

### Timeout errors on specific websites

**Solution:**
This is normal for sites with heavy JavaScript or anti-bot protection. Try:
- Simpler news sites (BBC, Reuters)
- Technical sites (GitHub, Stack Overflow)
- Documentation sites

### Server doesn't start

**Solution:**
Test manually in terminal:
```bash
cd /path/to/ScrapeFlow-MCP
python server.py
```

If you see errors, check that all dependencies are installed.

---

## Configuration Options

The `search_and_summarize` tool accepts these parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | *required* | The webpage URL to scrape |
| `max_chars` | integer | 5000 | Maximum characters to return |
| `include_metadata` | boolean | true | Include URL and character count info |

Example usage in Claude:
```
Scrape https://example.com with max_chars set to 10000
```

---

## Project Structure
```
ScrapeFlow-MCP/
├── server.py           # FastMCP server configuration
├── scraper.py          # WebScout scraping class
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

---

## Contributing

Found a bug or want to improve the scraper? Contributions are welcome!

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## License

MIT License - feel free to use this project for learning and development!

---

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Web scraping powered by [Playwright](https://playwright.dev/)
- HTML parsing by [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

---

## Questions or Issues?

If you run into problems:
1. Check the Troubleshooting section above
2. Review the Claude Desktop logs
3. Open an issue on GitHub with:
    - Your operating system
    - Error messages from logs
    - Steps you've already tried

Happy scraping!

This project is part of a deep-dive tutorial on my blog: [https://www.rooteddreams.net/web-scraping-mcp-guide/]
