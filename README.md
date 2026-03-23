# scrape-url: Claude Code Skill

A Claude Code skill that gives Claude a fallback web scraper using [Camoufox](https://camoufox.com/) — a hardened Firefox-based browser that bypasses bot detection, JS rendering, and most anti-scraping measures.

When `WebFetch` returns a blocked page, empty content, or JS-rendered shell, Claude can invoke `/scrape-url <url>` to get the real page content.

## How it works

1. Claude calls `/scrape-url https://example.com`
2. `scrape_url.py` launches a headless Camoufox browser, navigates to the URL, waits for network idle, then saves `{encoded_url}.html` to `/tmp/claude-scrape/`
3. Claude reads the saved HTML, parses it with BeautifulSoup, and extracts whatever you need

## Setup

**1. Install the skill**

Clone into your personal skills directory:

```bash
git clone https://github.com/greg-randall/scrape-url-skill ~/.claude/skills/scrape-url
```

**2. Install dependencies**

```bash
pip install -r ~/.claude/skills/scrape-url/requirements.txt
python3 -m camoufox fetch
```

That's it. No path editing required — the skill uses `${CLAUDE_SKILL_DIR}` to find `scrape_url.py` automatically.

## Usage

Invoke directly:

```
/scrape-url https://some-js-heavy-site.com
```

Or Claude will use it automatically when WebFetch returns blocked/empty content.

Optional argument:

```
/scrape-url https://example.com --wait-time 60
```

`--wait-time` controls how long (in seconds) to wait for network idle before giving up (default: 30).

## Updating

```bash
git -C ~/.claude/skills/scrape-url pull
```

## Requirements

- Python 3.8+
- [Camoufox](https://camoufox.com/) (`pip install camoufox[geoip]`)
- beautifulsoup4
