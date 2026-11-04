---
allowed-tools: Bash, Read, Write, Edit
description: First-run setup — check the install, explain where data goes, then a knowledge interview that writes your learner profile. Usage: /setup
---

Walk the learner through first-time setup. Keep each turn short and hand the ball back. This is
the learner's first contact with the tutor, so it should feel like the tutor, not a form.

## 1. Install check (do it, then report in a few lines)

Run these checks yourself and fix what you can. Ask the learner only for what needs them.

- `git --version`, and that this directory is a git clone (`git rev-parse --show-toplevel`).
- `python3 --version` (≥ 3.8; every hook is stdlib-only, so no packages are needed).
- Hooks work. Run `python3 .claude/hooks/friction_log.py --dry-run "setup check"` and
  `python3 .claude/hooks/memory_index.py </dev/null | head -3`. Both must exit 0.
- `observe/` exists and is writable.

If something is missing, tell the learner exactly how to install it for their OS, one step at a
time, and re-check. Do not proceed to the interview with broken hooks. The logs are the data this
test release exists to collect.

Then say, in two sentences: everything stays on their machine (logs in `observe/`, transcripts in
Claude Code's own store), and nothing is sent unless they run `/share-data` and send it themselves.

## 2. Who they are

Ask for a short handle for their profile (lowercase, used as a filename). Then ask about their
background, what they want from the tutor, and how they like to work. Keep it to one or two
turns.

## 3. Knowledge interview — locate the edge, don't quiz

Goal: a first, hedged picture of what they hold along `memory/sqisign-prerequisite-chain.md` §A
(the trunk), and whether any of §B is already familiar. Read `memory/teaching-method.md` and the
"Reachability probe" section of `docs/lesson-prep-pass-design.md` first.

- **Cheapest first.** Ask ("have you worked with X? what do you remember of why it holds?") before
  probing. Only escalate to a hypothetical probe (a small setup built from what they surely hold,
  where they must *supply* the tool) for large, load-bearing items where the answer is unclear.
- **Never leak the answer in a probe**, and never accept "I know it" as mastery of a load-bearing
  layer. Record it as **(claimed)** until something observed backs it.
- **Breadth, not depth.** This is a coarse map, roughly 15 to 30 minutes. Each lesson's own prep
  pass probes deeply for its target. Stop when you can name a plausible edge.
- Watch *how* they answer. Where they get stuck reveals a missing tool. What they reach for
  reveals what they hold. Note both.

## 4. Write the profile

Copy `learners/TEMPLATE.md` to `learners/<handle>.md` and fill it: grades by how acquired, the
evidence for each, and process asks they voiced. Create `lessons/<handle>/stack.md`, an empty
question stack with a one-line goal. Tell them, in their terms, where you think their edge is (one
or two sentences, hedged), and ask whether it matches their sense of it. Correct the profile if
not.

Finish with: "Type `/lesson` when you're ready." Do not start a lesson inside `/setup`.
