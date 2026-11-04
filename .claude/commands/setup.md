---
allowed-tools: Bash, Read, Write, Edit, Agent, Glob, Grep
description: First-run setup — check the install, explain where data goes, choose a learning goal (building its territory map if needed), then a knowledge interview that writes your learner profile. Usage: /setup
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
time, and re-check. Do not proceed with broken hooks. The logs are the data this test release
exists to collect.

Then say, in two sentences: everything stays on their machine (logs in `observe/`, transcripts in
Claude Code's own store), and nothing is sent unless they run `/share-data` and send it themselves.

## 2. Who they are, and what they want to learn

Ask for a short handle for their profile (lowercase, used as a filename). Then ask what they want
to understand, in their own words, along with their background and how they like to work. The goal
is theirs. Do not suggest one, and do not steer toward a topic a shipped map happens to cover.

If the goal is vague ("learn some number theory"), help them sharpen it into something you could
recognize them having reached: a result, a construction, a paper they want to read.

## 3. The territory map for that goal

List `territories/`. If a map there serves **this** goal (not just a nearby topic), use it and say
so in one line. Otherwise build one. Tell the learner it takes a while, and that they can keep
chatting about their background meanwhile.

- Launch the `researcher` agent to write `territories/<slug>.md`: what there is to learn on the
  way to the goal and how each piece bears on the others. Label each dependency **formal**
  (cannot state the next thing without it) or **informal** (motivation, intuition, analogy). Keep
  informal *concepts* too. Note where several routes exist, and give sources. Follow the shape of
  `territories/sqisign.md`: foundations first, then branches, then what is out of scope. It must
  hold **no proofs or answer keys**. Those belong to lesson prep. Head it with a status line:
  "DRAFT — built for <handle>'s goal on <date>".
- Run `claim-auditor` on it, then `red-team` on the load-bearing dependency claims. Fold the
  verdicts in under `## Audit` and `## Adversarial ledger`, and mark the status "gated once".
- If the goal is far beyond what one map can honestly cover, say so and agree on a nearer goal.

## 4. Knowledge interview — locate the edge, don't quiz

Goal: a first, hedged picture of what they hold among the map's foundations, and whether any of
the later material is already familiar. Read `memory/teaching-method.md` and the "Reachability
probe" section of `docs/lesson-prep-pass-design.md` first.

- **Cheapest first.** Ask ("have you worked with X? what do you remember of why it holds?") before
  probing. Only escalate to a hypothetical probe (a small setup built from what they surely hold,
  where they must *supply* the tool) for large, load-bearing items where the answer is unclear.
- **Never leak the answer in a probe**, and never accept "I know it" as mastery of a load-bearing
  layer. Record it as **(claimed)** until something observed backs it.
- **Breadth, not depth.** This is a coarse map, roughly 15 to 30 minutes. Each lesson's own prep
  pass probes deeply for its target. Stop when you can name a plausible edge.
- Watch *how* they answer. Where they get stuck reveals a missing tool. What they reach for
  reveals what they hold. Note both.

## 5. Write the profile

Copy `learners/TEMPLATE.md` to `learners/<handle>.md` and fill it: the goal and its map, grades by
how acquired, the evidence for each, and process asks they voiced. Create
`lessons/<handle>/stack.md`, an empty question stack headed by their goal. Tell them, in their
terms, where you think their edge is (one or two sentences, hedged), and ask whether it matches
their sense of it. Correct the profile if not.

Finish with: "Type `/lesson` when you're ready." Do not start a lesson inside `/setup`.
