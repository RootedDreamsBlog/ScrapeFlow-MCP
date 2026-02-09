from mcp.server.fastmcp import FastMCP
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Initialize FastMCP - this name appears in the AI interface
mcp = FastMCP("ScrapeFlow")

@mcp.tool()
async def search_and_summarize(url: str) -> str:
    """
    Scrapes a specific URL and returns a cleaned summary of the content.
    Useful for providing real-time web context to the LLM.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            # Navigate to the URL
            await page.goto(url, wait_until="networkidle", timeout=30000)

            # Get content and clean it with BeautifulSoup
            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")

            # Remove non-content tags
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)
            return text[:5000] # Limit characters for LLM context window efficiency

        except Exception as e:
            return f"Failed to scrape {url}: {str(e)}"
        finally:
            await browser.close()

if __name__ == "__main__":
    mcp.run()