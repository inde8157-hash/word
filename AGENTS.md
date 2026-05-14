# X High-Signal Posts — Codex Setup

This project uses Codex with MCP servers to produce high-quality, human-sounding X (Twitter) posts from source material.

## MCP Servers

The following MCP servers are configured in `.codex/config.toml` to improve post quality:

| Server | Purpose | API Key |
|--------|---------|---------|
| **fetch** | Read source articles as clean markdown | None required |
| **intercept** | Robust web fetching with fallback chain (handles paywalls, JS pages) | None required |
| **brave-search** | Real-time search for fact-checking claims, prices, deadlines | `BRAVE_API_KEY` (free at brave.com/search/api) |
| **ai-humanizer** | Rewrite AI-generated text to sound natural and human | Via text2go.ai |

## How MCP Servers Improve Results

1. **fetch + intercept** — The skill requires reading full source material before writing. These servers let Codex fetch any URL and extract clean text, even from sites that block bots.

2. **brave-search** — The skill requires verifying claims: numbers, dates, costs, platform policies. Brave Search provides real-time web results to fact-check before writing, preventing invented stats.

3. **ai-humanizer** — After generating posts, run them through the humanizer to eliminate AI-sounding patterns. This catches generic phrasing the skill's Output Hygiene section warns against.

## Workflow

When using the `x-high-signal-posts` skill:

1. User provides a URL or source text
2. Codex uses **fetch** or **intercept** to read the full source as markdown
3. Codex uses **brave-search** to verify any claims, numbers, deadlines, or pricing
4. Codex writes posts following the skill's formats (TLDR, Opinion, Vibe)
5. Codex uses **ai-humanizer** to polish the final text for naturalness
6. Output passes the skill's quality bar and output hygiene checks

## Setup

### Environment Variables

Set these before running Codex:

```bash
export BRAVE_API_KEY="your-brave-api-key"
```

### Get API Keys

- **Brave Search**: https://brave.com/search/api/ — free tier gives 2000 queries/month
- **Text2Go (AI Humanizer)**: https://www.text2go.ai/ — sign up for access

### Verify MCP Servers

After starting Codex, type `/mcp` to confirm all 4 servers are connected.

## Skill Location

The writing skill is at `.codex/skills/x-high-signal-posts/SKILL.md`. It defines the exact post formats, quality bar, and prohibited phrasing.

## Quality Expectations

Posts must:
- Have a hook that stands alone
- Name specific mechanisms, not themes
- Include real numbers (not invented)
- Give the reader an action to take
- Pass the Output Hygiene checks (no prohibited words/phrases)
- Sound human, not AI-generated
