---
name: x-high-signal-posts
description: Write sharp English X posts from dense articles, guides, threads, product updates, or research links. Use when the user wants posts that feel like concrete opportunity guides, teardown threads, sharp quote posts, or "me realizing" meme posts with numbers, mechanisms, setup steps, urgency, and useful insight instead of generic summaries or AI slop.
---

# X Sharp Posts

Turn source material into copy-paste-ready X posts that make the reader feel they learned a specific money mechanic, setup, risk, workflow, or decision rule.

## Workflow

1. Read the full source first.
2. Verify claims that may be current, factual, pricing-related, legal, platform-policy-related, or easy to challenge. Use official or primary sources when possible. If the source is wrong or outdated, say the correction before the posts and write around the corrected fact.
3. Extract the post payload:
   - who is affected
   - what they are doing wrong
   - what hidden system, mechanic, deadline, or setup matters
   - exact numbers, dates, costs, thresholds, percentages, tools, commands, or product names
   - what the reader should do next
4. Choose one dominant angle before writing. Prefer:
   - hidden payment/setup layer
   - platform or incentive arbitrage
   - one-file or one-command setup
   - overlooked checklist with high downside
   - deadline/window closing
   - everyone is learning the visible tool instead of the durable layer
   - the app/system was not broken, the business/setup was
5. Produce exactly three formats unless the user asks for a different count:
   - TLDR guide
   - reasoned opinion
   - vibe realization
6. Put each post in its own fenced code block for clean copying.
7. Include videos only when the user asks, when another active skill requires them, or when the current task clearly asks for X post packages with matching media.

## Post Standards

Make every post pass these tests:

- The first line can stand alone as a strong X hook.
- The reader can act after reading it.
- The post names the actual mechanism, not just the theme.
- Numbers are specific and not invented.
- Urgency comes from a real constraint, deadline, platform rule, cost, or market window.
- The payoff explains money, time saved, risk avoided, credibility gained, or capability gained.

Prefer concrete lines like:

- Apple does not pay you just because the app is live.
- TikTok rented you reach. YouTube paid for searchable attention. Instagram captured intent.
- The problem was not the model. It was the shell output filling the context window.

Avoid generic lines like:

- This changes everything.
- The future is here.
- Build smarter, not harder.
- It is not just X, it is Y.
- Here is why it matters.
- Reach your full potential.
- That is the scary part.
- That is the important part.
- Here is the part nobody talks about.
- The demo is the easy part.
- The hard part is...
- The agents are the easy part.
- Most people...
- Most people use...
- Most people think...
- Most people are doing...
- It needed a better vibe.
- It did not need a better vibe.
- The good pattern is not X. It is Y.
- The trick is not X. It is Y.
- The move is not X. It is Y.

## Hook Diversity

Every post opens with a hook - the first line. Hooks must rotate across categories. Never use the same hook category twice in a row when producing multiple posts. Never default to "most people..." as an opener.

### Hook Categories (rotate between these)

**1. Number-first** — lead with a specific cost, count, percentage, or threshold from the source.
```
$97/month tool replaced my $2,400/month agency.
3 API calls. That is the entire backend.
14 deployment environments. 1 YAML file.
```

**2. Concrete failure** — lead with a specific thing that broke, failed, or produced zero results.
```
The agent ran for 72 hours. It completed 0 tasks.
I shipped to 12,000 users with a broken env variable.
The checkout page loaded 11 analytics scripts before the buy button.
```

**3. Command / artifact / setting** — lead with a file, flag, config line, or tool name.
```
One line in .env changed the response from 800 tokens to 140.
Found the setting buried in Project > Advanced > Model behavior.
CONTEXT_WINDOW=8192. That was the entire fix.
```

**4. Timeline / timestamp** — lead with a time reference that creates urgency or surprise.
```
6 months ago this setup did not exist.
Between 2am and 5am the API costs drop 40%.
The deadline is July 1. After that the free tier disappears.
```

**5. Personal action / discovery** — lead with "I did X" or "I stopped doing X".
```
I stopped opening Claude 12 times a day.
I replaced the entire review pipeline with one prompt.
I ran the same deploy 3 times before checking the logs.
```

**6. Counter-intuitive claim** — lead with a statement that contradicts the obvious assumption.
```
The model was right. The prompt was feeding it last week's schema.
Faster inference made the output worse.
The cheapest plan had the best rate limits for batch jobs.
```

**7. Direct question** — open with a question the reader would actually ask themselves.
```
Why does the agent keep re-reading the same file?
What happens when your context window is 90% old JSON?
How many of your API calls are actually retries?
```

### Hook rotation rule

When generating multiple posts in one session, track which hook category was used and pick a different one for the next post. If you catch yourself starting with "most..." or any crowd-contrast phrasing, stop and rewrite using one of the 7 categories above.

## Formats

### TLDR Guide

Do not write an executive summary. Write a practical mini-guide.

Shape:

1. Start with the painful mistake or surprising math.
2. Reveal the hidden layer or system.
3. List the exact setup, steps, thresholds, or tools.
4. Explain the money/time/risk consequence.
5. End with a direct action or decision rule.

Use line breaks aggressively. Use numbered steps or `>` rhythm when it improves scanability.

### Reasoned Opinion

Give a sharp but fair thesis.

Use this format when the source has a strategic lesson:

- the common assumption or surface-level reading (do NOT open with "most people..." - name the specific belief or behavior instead)
- why that first reading misses the mechanism
- what the real operating layer is
- what to build, learn, skip, or check instead

Do not dunk on people unless the user asks for aggression. Be direct, not mean.

### Vibe Realization

Write the late-night "I was doing this wrong" post.

Use `> ` lines for a sequence of mistakes, discoveries, fixes, or checklist items when it fits. Keep enough prose around the rhythm so it does not become a vertical wall.

Prefer `>` rhythm over hyphen bullets in vibe posts. Hyphen lists often make the post feel like a generic checklist; `>` keeps the late-night realization cadence. If the post says "it was:" or "the fix was:", the following lines should usually use `>`, not `-`.

```text
Bad:
It was:

- job descriptions
- off-laptop hosting
- live monitoring

Good:
It was:

> job descriptions
> off-laptop hosting
> live monitoring
```

Good vibe post structure:

```text
Me realizing [specific false belief]

> did X
> expected Y
> checked Z
> found the missing setup
> money/context/revenue finally made sense

The app/model/platform was not broken

the [specific hidden layer] was
```

## Output Hygiene

Before finalizing, scan every generated post. Rewrite any line that uses the terms, phrases, or symbols below. These are allowed only when directly naming this checklist or showing the bad examples below, not in X post copy.

Prohibited words:

- `expensive`
- `noise`
- `signal`
- `unlock`
- `operator`
- `state`

Prohibited phrases:

- `real unlock`
- `treat it like`
- `blank chat box`
- `wrong frame`
- `the interesting part`
- `that was the shift`
- `wrong layer`

Prohibited symbols:

- left curly double quote, U+201C
- right curly double quote, U+201D

Use straight ASCII quotes (`"`) if quotation marks are needed.

Avoid AIrish phrasing that turns every post into the same abstract contrast. Rewrite lines like these into specific, source-grounded claims:

```text
"The scary part of AI creators is not the images, it is the memory layer"
"The best use of Hermes is not asking it what should I buy? that is how you get hallucinated confidence"
"follow these 60 GitHub accounts is the wrong frame"
"but the next version is not just a pretty AI model, it is a folder with state"
"the face is not the product
the folder is"
```

Avoid vague drama pivots. Do not write lines that merely label something as scary, important, wild, or overlooked. Name the concrete failure, mechanism, or cost instead.

```text
Bad: That is the scary part.
Good: It keeps sending emails after the prompt breaks.

Bad: The important part is not the agent, it is the runtime.
Good: A closed laptop, stuck retry loop, or unmonitored API key can break the workflow before the model does.
```

Avoid unclear shorthand that hides the actual failure behind abstract nouns. Replace phrases like `routing drifts`, `context drifts`, and `quality drifts` with the concrete behavior the reader would observe.

```text
Bad: routing drifts
Good: requests start hitting the fallback model instead of the intended model

Bad: context drifts
Good: the answer starts citing old requirements after the user changed the spec

Bad: quality drifts
Good: the replies get longer, vaguer, and stop naming the exact command or file
```

Avoid overusing abstract contrast templates, especially `X is the easy part / Y is the hard part`. This pattern makes posts feel interchangeable. Use it only if the source itself makes that exact contrast and the next line names a specific mechanism. Prefer direct cause-and-effect, checklist, or failure-path phrasing.

```text
Bad: The demo is the easy part. The hard part is making it run in production.
Good: A demo agent needs a prompt. A production agent needs hosting, live status, retries, budget limits, and approval gates.

Bad: The agents are the easy part.
Good: The first prompt can work in 10 minutes. The 30-day setup needs logs, spend caps, OAuth permissions, and a human approval step before customer-facing actions.
```

Avoid fake-opponent contrast lines like `The good pattern is not X. It is Y.`, `The trick is not X. It is Y.`, or `The move is not X. It is Y.` These often argue against a strawman, use abstract nouns, and delay the useful mechanism. Use them only when X is a real claim from the source and Y names a concrete mechanism in the same sentence. Prefer starting with the mechanism directly.

```text
Bad: The good pattern is not "install 12 extensions." It is using the built-ins.
Good: Claude Code already has memory, rewind, worktrees, budget caps, print mode, and file mentions. Learn those before adding anything else.

Bad: The trick is not better prompts. It is better structure.
Good: Give Opus 4.7 the audit scope, output table, length cap, source rules, and definition of done.

Bad: The move is not more folders. It is a feedback loop.
Good: Keep one markdown source, generate HTML views from it, and delete the views when they go stale.
```

Avoid polished missing-piece contrasts like `X was not missing Y. It was missing Z.` This structure often sounds neat but generic, especially when `Z` is an abstract noun like context, structure, or intelligence. Replace it with the specific setup change or observed before/after behavior.

```text
Bad: Claude was not missing intelligence. It was missing my working context.
Good: Once the Project had my role, goals, constraints, and writing samples, I stopped spending the first 10 minutes correcting the same assumptions.

Bad: The model was not missing skill. It was missing structure.
Good: The answer improved after I gave it the audit scope, output table, length cap, and definition of done.
```
Avoid default crowd-contrast hooks like `Most people use...`, `Most people think...`, or `Most people are doing...`. They are allowed only when followed by a highly specific, source-grounded behavior that could not fit any other post. Prefer hooks that start with a number, concrete artifact, timestamp, command, failed outcome, or specific setup.

```text
Bad: Most people use Claude like a chat window.
Good: I stopped opening Claude 12 times a day.

Bad: Most people build Obsidian vaults that never talk back.
Good: My Obsidian vault sends me a briefing at 6am.

Bad: Most people think voice cloning is about examples.
Good: 20 favorite posts made my Claude sound like a parody of me.
```

Avoid bad/better examples where the better version starts by repeating the bad prompt or bad line. The contrast should make the missing mechanism obvious immediately. If the bad example is a vague prompt, the better example should start with the precise action, scope, or output format.

```text
Bad:
Stop writing: "Review this contract."
Write: "Review this contract. Flag risks per clause."

Good:
Bad: "Review this contract."
Better: "Audit this contract for payment, liability, renewal, and termination risk. Return a table with clause, severity 1-5, why it matters, and suggested rewrite."

Bad:
Stop writing: "Help me with this email."
Write: "Help me with this email. Make it under 90 words."

Good:
Bad: "Help me with this email."
Better: "Write a send-ready email under 90 words. Goal: book a meeting by Friday. Tone: confident, casual, specific. End with one clear time-based ask."
```

Avoid vague or cute punchlines such as `better vibe`, `more magic`, `smarter energy`, or similar phrasing unless the source is literally about tone or brand feel. End with the actual missing part: scope, format, examples, approval gate, runtime, retrieval path, source of truth, or definition of done.

```text
Bad: Claude did not need a better vibe.
Good: Opus 4.7 was not missing context. My prompt was missing the job spec.

Bad: The setup needed more magic.
Good: The setup needed a source folder, a scheduled run, an output path, and a review step.
```

Avoid coy scare quotes. Do not put ordinary words in quotes to imply irony, sarcasm, or half-failure. Replace the quoted word with the exact behavior.

```text
Bad: found the agent had been "working" for 3 days
Good: found the agent looping through retries for 3 days

Bad: the agent was still "thinking"
Good: the agent was stuck on the same step for 3 hours
```

## Style Rules

- Write in English unless the user asks otherwise.
- Use lowercase casual phrasing when it fits the user's examples.
- Keep paragraphs short.
- Use exact product names and platform names.
- Preserve useful terms from the source, but rewrite weak phrasing.
- Do not over-polish into corporate language.
- Do not invent revenue, user counts, deadlines, salaries, benchmark results, or policy details.
- If a claim is uncertain, soften it or attribute it.
- If the source is a long guide, compress it into the 5-10 points someone would save.
- If the source is about AI tools, agents, coding, apps, or monetization, emphasize the operational setup and hidden failure mode.

## Quality Bar

Before finalizing, compare each post against `references/post-patterns.md` if the post feels soft, generic, or too summary-like.

Rewrite if:

- it could fit any article
- it has no numbers or concrete nouns
- it says system without naming the parts
- it gives advice but no execution path
- it sounds like a LinkedIn recap
- it uses hype instead of mechanism
- it uses any prohibited term, phrase, or symbol from the Output Hygiene section

## Output Shape

Use this default structure:

```text
TLDR format
[copy-paste post block]

Opinion format
[copy-paste post block]

Vibe format
[copy-paste post block]

Sources checked
[only if sources were checked or corrections were made]
```
