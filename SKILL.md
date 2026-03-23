---
name: scrape-url
description: Scrapes a URL using the Camoufox headless browser when WebFetch returns blocked, empty, or JS-rendered content. Use as a fallback for bot-protected or JavaScript-heavy pages.
dependencies: camoufox[geoip], beautifulsoup4
argument-hint: <url> [--wait-time <seconds>]
allowed-tools: Bash(cd *), Bash(python3 *), Read
---

Scrape a URL using the Camoufox headless browser (bypasses JS rendering and bot detection) and return the page content for extraction.

Given a URL as $ARGUMENTS:

1. Run the scraper:
   ```
   cd "${CLAUDE_SKILL_DIR}" && python3 scrape_url.py "$ARGUMENTS"
   ```

2. The script prints the saved HTML file path to stdout. Read that file and parse it with BeautifulSoup to extract the page content and links relevant to the task at hand.

3. If the content appears blocked or empty, retry with a longer `--wait-time` (default: 30 seconds).
