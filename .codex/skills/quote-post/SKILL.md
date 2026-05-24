---
name: quote-post
description: Write a quote-post in English based on an attached article. Produces a 15-20 line post with short punchy lines, lowercase style, no em dashes, and `>` blocks for key facts. Use when the user shares an article and wants a sharp, practitioner-style quote-post ready to copy-paste.
---

# Quote-Post from Article

Write a quote-post in English based on the attached article.

## Style Rules

- all sentences start with a lowercase letter
- use `-` instead of `—`
- no em dashes anywhere
- 15-20 lines total
- short punchy lines, one idea per line
- use `>` for list items and key facts
- no bullet points outside of `>` blocks
- use straight ASCII quotes (`"`) only, never curly/smart quotes

## Structure

- open with a contrast or "before/after" setup (what the common approach is vs what actually works)
- middle section: concrete practices, numbers, or mechanics from the article - only facts that are actually in the text, no invented details
- close with a reframe or insight that ties it together - can be a short original conclusion drawn from the article's logic, but keep it grounded

## Hook Diversity

The first line is the hook. Do NOT default to "most people..." or any crowd-contrast opener. Rotate between these hook categories:

**1. Number-first** - lead with a specific cost, count, percentage, or threshold from the article.
```
$97/month tool replaced my $2,400/month agency.
3 API calls. that is the entire backend.
14 deployment environments. 1 YAML file.
```

**2. Concrete failure** - lead with something that broke, failed, or produced zero results.
```
the agent ran for 72 hours. it completed 0 tasks.
i shipped to 12,000 users with a broken env variable.
the checkout page loaded 11 analytics scripts before the buy button.
```

**3. Command / artifact / setting** - lead with a file, config, tool name.
```
one line in .env changed the response from 800 tokens to 140.
found the setting buried in Project > Advanced > Model behavior.
CONTEXT_WINDOW=8192. that was the entire fix.
```

**4. Timeline / timestamp** - lead with a time reference that creates urgency or surprise.
```
6 months ago this setup did not exist.
between 2am and 5am the API costs drop 40%.
the deadline is July 1. after that the free tier disappears.
```

**5. Personal action / discovery** - lead with "i did X" or "i stopped doing X".
```
i stopped opening Claude 12 times a day.
i replaced the entire review pipeline with one prompt.
i ran the same deploy 3 times before checking the logs.
```

**6. Counter-intuitive claim** - lead with a statement that contradicts the obvious assumption.
```
the model was right. the prompt was feeding it last week's schema.
faster inference made the output worse.
the cheapest plan had the best rate limits for batch jobs.
```

**7. Direct question** - open with a question the reader would actually ask.
```
why does the agent keep re-reading the same file?
what happens when your context window is 90% old JSON?
how many of your API calls are actually retries?
```

If generating multiple posts, never use the same hook category twice in a row. If you catch yourself starting with "most..." or any crowd-contrast phrasing, stop and rewrite using one of the 7 categories above.

## Tone

Direct, no fluff, no AI-sounding phrases. Reads like a sharp practitioner sharing what actually works.

Prefer concrete lines like:
- Apple does not pay you just because the app is live.
- TikTok rented you reach. YouTube paid for searchable attention.
- the problem was not the model. it was the shell output filling the context window.

## Prohibited Patterns

Words and phrases - never use in post copy:
- "game-changer", "revolutionize", "unlock", "signal", "noise"
- "this changes everything", "the future is here", "here is why it matters"
- "most people...", "most people use...", "most people think...", "most people are doing..."
- "the trick is not X. it is Y.", "the move is not X. it is Y."
- "that is the scary part", "that is the important part", "here is the part nobody talks about"
- "build smarter, not harder", "reach your full potential"

Symbols - never use:
- em dash `—` (use `-` instead)
- curly quotes (use straight `"` only)

## Fact-Check

After writing, check: does every factual claim trace back to something in the article? If not, cut it or rephrase as a conclusion drawn from the article's logic.

Do not invent numbers, stats, revenue, user counts, deadlines, salaries, benchmark results, or policy details.

## Output

Put the post in a fenced code block for clean copying.
