# Post Patterns Reference

Use this file to compare your posts against proven patterns. If a post feels soft, generic, or too summary-like, check it against these examples.

## Strong Hook Patterns

### Number-First Hooks
```
$97/month tool replaced my $2,400/month agency.
```
```
3 API calls. That is the entire backend.
```
```
1 YAML file controls 14 deployment environments.
```

### Concrete Failure Hooks
```
The agent ran for 72 hours. It completed 0 tasks.
```
```
I shipped to 12,000 users with a broken env variable.
```
```
The model was right. The prompt was feeding it last week's schema.
```

### Setup/Discovery Hooks
```
Found the setting buried in Project > Advanced > Model behavior.
```
```
One line in .env changed the response from 800 tokens to 140.
```
```
The fix was not a better model. It was a 4-line system prompt.
```

## Strong Payoff Patterns

### Exact Mechanism Payoffs
```
The difference: retrieval ran before the prompt, not after.
```
```
Revenue doubled when the checkout page stopped loading the analytics bundle.
```
```
The API was fine. The timeout was set to 3 seconds on a 4-second call.
```

### Action-Oriented Payoffs
```
Set CONTEXT_WINDOW=8192. The rest fixes itself.
```
```
Run the audit monthly. Export to the same spreadsheet. Review takes 6 minutes.
```
```
Add the budget cap before you add the agent. Not after.
```

## Weak Patterns to Avoid

### Vague Drama (rewrite these)
```
BAD: This changes everything.
WHY: Does not name what changed or for whom.

BAD: The future of coding is here.
WHY: Every AI tool says this. Zero information content.

BAD: Most people are sleeping on this.
WHY: Does not name the thing or the consequence.
```

### Abstract Contrasts (rewrite these)
```
BAD: It is not about the tool. It is about the system.
WHY: Neither "tool" nor "system" names anything specific.

BAD: The hard part is not building it. The hard part is maintaining it.
WHY: True of everything. Add the specific maintenance failure.
```

### Generic Advice (rewrite these)
```
BAD: Start small and iterate.
WHY: Applies to everything. Name the specific first step.

BAD: The key is consistency.
WHY: Motivational poster energy. Name the specific cadence and output.
```

## Format-Specific Patterns

### TLDR Guide — Strong Opening Lines
```
You are paying for GPT-4 tokens on a task that needs 3 lines of regex.
```
```
Apple takes 30%. That is not news. The news: they keep 30% of renewals forever if the user signed up through the App Store.
```

### Opinion — Strong Thesis Lines
```
The MCP hype assumes every developer wants to wire tools at the protocol layer. Most want a button that works.
```
```
Cursor is not an IDE. It is a prompt surface with syntax highlighting.
```

### Vibe — Strong Realization Arcs
```
Me realizing the agent was not slow

> it was re-reading the entire file on every loop
> the file grew by 200 lines per run
> by hour 3 it was reading a novel before each edit

The model was fast. My file was not.
```
```
Me realizing why my Claude Project worked once then broke

> first run: clean context
> second run: leftover tool outputs in history
> third run: 90% of context was old JSON
> added a "flush history" step

The model did not get dumber. The context got dirtier.
```

## Hook Diversity Checklist

When writing multiple posts, verify hook variety:

- [ ] No two posts in the same batch start with the same hook category
- [ ] No post starts with "most people..." or any crowd-contrast opener
- [ ] At least 3 different hook categories are used across a 3-post batch

Hook categories to rotate:
1. Number-first ($X, N%, count)
2. Concrete failure (broke, failed, zero results)
3. Command / artifact / setting (file name, config, flag)
4. Timeline / timestamp (date, deadline, time window)
5. Personal action ("I did X", "I stopped X")
6. Counter-intuitive claim (the opposite of what you'd expect)
7. Direct question (a real question the reader would ask)

## Checklist Before Publishing

- [ ] First line works as a standalone hook
- [ ] Hook does NOT start with "most people..." or similar crowd-contrast
- [ ] Hook category differs from the previous post in this batch
- [ ] At least one specific number, date, cost, or threshold
- [ ] Reader knows what to do after reading
- [ ] No prohibited words (expensive, noise, signal, unlock, operator, state)
- [ ] No curly quotes
- [ ] No generic contrast templates
- [ ] Passes the "could this fit any article?" test (if yes, rewrite)
