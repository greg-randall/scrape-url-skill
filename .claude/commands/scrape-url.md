Scrape a URL using the Camoufox headless browser (bypasses JS rendering and bot detection) and return the page content for extraction.

Use this as a fallback when WebFetch returns blocked/empty/JS-rendered content.

Given a URL as $ARGUMENTS:

1. Run the scraper:
   ```
   cd "/path/to/scrape-url-skill" && python3 scrape_url.py $ARGUMENTS
   ```

2. Determine the saved HTML filename:
   - Compute `urllib.parse.quote(url, safe="")`
   - If len > 250: truncate to 240 chars + "_" + first 8 chars of md5(url.encode()).hexdigest()
   - Append `.html`
   - Full path: `/tmp/claude-scrape/{filename}`

3. Read the HTML file and parse it with BeautifulSoup to extract the page content and links relevant to the task at hand.
