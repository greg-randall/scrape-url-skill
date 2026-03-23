---
name: scrape-url
description: Scrape a URL using the Camoufox headless browser when WebFetch returns blocked, empty, or JS-rendered content. Use as a fallback for bot-protected or JavaScript-heavy pages.
argument-hint: <url> [--wait-time <seconds>]
allowed-tools: Bash(cd *), Bash(python3 *), Read
---

Scrape a URL using the Camoufox headless browser (bypasses JS rendering and bot detection) and return the page content for extraction.

Use this as a fallback when WebFetch returns blocked, empty, or JS-rendered content.

Given a URL as $ARGUMENTS:

1. Run the scraper:
   ```
   cd "${CLAUDE_SKILL_DIR}" && python3 scrape_url.py $ARGUMENTS
   ```

2. Determine the saved HTML filename:
   - Compute `urllib.parse.quote(url, safe="")`
   - If len > 250: truncate to 240 chars + "_" + first 8 chars of md5(url.encode()).hexdigest()
   - Append `.html`
   - Full path: `/tmp/claude-scrape/{filename}`

3. Read the HTML file and parse it with BeautifulSoup to extract the page content and links relevant to the task at hand.
