from mcp.server.fastmcp import FastMCP
from scraper import WebScout

# Initialize FastMCP
mcp = FastMCP("ScrapeFlow")
scout = WebScout()

@mcp.tool()
async def search_and_summarize(
        url: str,
        max_chars: int = 5000,
        include_metadata: bool = True
) -> str:
    """
    Scrapes a specific URL and returns cleaned content.

    Args:
        url: The webpage URL to scrape
        max_chars: Maximum characters to return (default 5000)
        include_metadata: Whether to include URL and length info

    Returns:
        Cleaned text content from the webpage
    """
    # Validate URL format
    if not url.startswith(('http://', 'https://')):
        return "Error: URL must start with http:// or https://"

    try:
        # Call the modular scraper
        text = await scout.get_clean_content(url)

        # Check if scraping failed
        if text.startswith("Scraping Error:"):
            return text

        # Limit characters for LLM context window efficiency
        truncated_text = text[:max_chars]

        # Add metadata if requested
        if include_metadata:
            metadata = f"Content from {url} (Total: {len(text)} chars, Showing: {len(truncated_text)} chars)\n\n"
            return metadata + truncated_text

        return truncated_text

    except Exception as e:
        return f"Unexpected error while processing {url}: {str(e)}"

if __name__ == "__main__":
    mcp.run()