# scrape-url: Claude Code Skill

A Claude Code slash command that gives Claude a fallback web scraper using [Camoufox](https://camoufox.com/) — a hardened Firefox-based browser that bypasses bot detection, JS rendering, and most anti-scraping measures.

When `WebFetch` returns a blocked page, empty content, or JS-rendered shell, Claude can invoke `/scrape-url <url>` to get the real page content.

## How it works

1. Claude calls `/scrape-url https://example.com`
2. `scrape_url.py` launches a headless Camoufox browser, navigates to the URL, waits for network idle, then saves `{encoded_url}.html` — full rendered HTML
3. Claude reads the saved HTML, parses it with BeautifulSoup, and extracts whatever you need

HTML files are saved to `/tmp/claude-scrape/` and can be deleted at any time.

## Setup

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

Camoufox also needs its browser binary on first use:

```bash
python3 -m camoufox fetch
```

**2. Install the skill**

Copy `.claude/commands/scrape-url.md` into your project's `.claude/commands/` folder (or `~/.claude/commands/` for global use).

Edit the path in `scrape-url.md` to point to wherever you've placed `scrape_url.py`.

**3. Allow the Bash command in Claude Code settings**

Add permission rules so Claude can run the script without prompting every time. In `~/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(cd:*)",
      "Bash(python3:*)"
    ]
  }
}
```

`cd:*` is needed because the skill runs `cd /path/to/script && python3 scrape_url.py ...`.

## Usage

Once installed, Claude can use it automatically as a fallback, or you can invoke it directly:

```
/scrape-url https://some-js-heavy-site.com/funders/
```

Optional argument:

```
/scrape-url https://example.com --wait-time 60
```

`--wait-time` controls how long (in seconds) to wait for network idle before giving up (default: 30).

## Requirements

- Python 3.8+
- [Camoufox](https://camoufox.com/) (`pip install camoufox[geoip]`)
- beautifulsoup4
