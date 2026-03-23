import argparse
import asyncio
import hashlib
import os
import urllib.parse
from browserforge.fingerprints import Screen
from camoufox.async_api import AsyncCamoufox

SCRAPE_DIR = "/tmp/claude-scrape"


async def scrape(url: str, wait_time: int):
    os.makedirs(SCRAPE_DIR, exist_ok=True)

    # Use percent-encoding for a readable but filesystem-safe filename
    # We encode everything (safe="") to ensure characters like : and / are handled
    encoded_name = urllib.parse.quote(url, safe="")

    # Filesystems (especially NTFS/EXT4) have a 255-char limit.
    # Percent encoding can make names very long, so we truncate ONLY if necessary.
    if len(encoded_name) > 250:
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        filename_base = f"{encoded_name[:240]}_{url_hash}"
    else:
        filename_base = encoded_name

    html_path = os.path.join(SCRAPE_DIR, f"{filename_base}.html")

    print(f"Navigating to: {url}")

    async with AsyncCamoufox(headless=True, screen=Screen(max_width=1920, max_height=1080)) as browser:
        page = await browser.new_page()

        try:
            # Navigate and wait for load state or timeout
            await page.goto(url, wait_until="networkidle", timeout=wait_time * 1000)
        except Exception as e:
            print(f"Warning: Navigation timed out or encountered an error: {e}")
            # We continue anyway to capture whatever loaded

        # Save HTML
        content = await page.content()
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved HTML to: {html_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a URL using Camoufox.")
    parser.add_argument("url", help="The URL to scrape")
    parser.add_argument("--wait-time", type=int, default=30, help="Maximum wait time in seconds (default: 30)")

    args = parser.parse_args()

    asyncio.run(scrape(args.url, args.wait_time))
