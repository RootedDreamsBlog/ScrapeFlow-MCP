from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import Optional
import asyncio

class WebScout:
    """Modular scraper class for 2026 agentic workflows."""

    def __init__(self, cache_duration_minutes: int = 10):
        self.cache = {}
        self.cache_duration = timedelta(minutes=cache_duration_minutes)

    def _get_from_cache(self, url: str) -> Optional[str]:
        if url in self.cache:
            cached_time, cached_content = self.cache[url]
            if datetime.now() - cached_time < self.cache_duration:
                return cached_content
        return None

    def _add_to_cache(self, url: str, content: str) -> None:
        self.cache[url] = (datetime.now(), content)

    async def get_clean_content(self, url: str, timeout: int = 60000) -> str:
        """
        Scrape a URL and return cleaned text content.

        Args:
            url: The webpage URL to scrape
            timeout: Timeout in milliseconds (default 60000 = 60 seconds)

        Returns:
            Cleaned text content or error message
        """
        # Check cache first
        cached_content = self._get_from_cache(url)
        if cached_content:
            return cached_content

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                viewport={'width': 1920, 'height': 1080}
            )
            page = await context.new_page()

            try:
                # Navigate with longer timeout
                await page.goto(url, wait_until="domcontentloaded", timeout=timeout)

                # Wait a bit for dynamic content
                await asyncio.sleep(2)

                content = await page.content()

                # Parse and clean the HTML
                soup = BeautifulSoup(content, "html.parser")

                # Remove unwanted elements
                for element in soup(["script", "style", "nav", "footer", "header", "aside", "iframe", "noscript"]):
                    element.decompose()

                # Try to extract main content first
                main_content = soup.find('main') or soup.find('article') or soup.find('body')

                if main_content:
                    text = main_content.get_text(separator="\n", strip=True)
                else:
                    text = soup.get_text(separator="\n", strip=True)

                # Clean up excessive whitespace
                lines = [line.strip() for line in text.split('\n') if line.strip()]
                cleaned_text = '\n'.join(lines)

                # Cache the result
                self._add_to_cache(url, cleaned_text)

                return cleaned_text

            except Exception as e:
                return f"Scraping Error: {str(e)}\n\nTip: This site may have anti-bot protection. Try a simpler website like https://example.com or a news article."

            finally:
                await context.close()
                await browser.close()

    def clear_cache(self) -> None:
        self.cache.clear()

    def get_cache_stats(self) -> dict:
        return {
            "cached_urls": len(self.cache),
            "urls": list(self.cache.keys())
        }