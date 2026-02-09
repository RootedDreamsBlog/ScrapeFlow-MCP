from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

class WebScout:
    """Modular scraper class for 2026 agentic workflows."""

    async def get_clean_content(self, url: str) -> str:
        async with async_playwright() as p:
            # Launching a stealth-oriented browser
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            try:
                # Optimized for 2026 web standards
                await page.goto(url, wait_until="networkidle", timeout=30000)
                content = await page.content()

                # Cleanup logic
                soup = BeautifulSoup(content, "html.parser")
                for element in soup(["script", "style", "nav", "footer", "header"]):
                    element.decompose()

                return soup.get_text(separator="\n", strip=True)

            except Exception as e:
                return f"Scraping Error: {str(e)}"
            finally:
                await browser.close()