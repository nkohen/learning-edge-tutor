---
allowed-tools: Bash, Read, Write, Edit, Agent, Glob, Grep
description: Pick a target at your learning edge, prepare it, and teach it by inquiry (resumes an unfinished lesson). Usage: /lesson [optional topic]
---

Run one lesson for the learner. Topic hint, if any: $ARGUMENTS

## 0. Load

- The learner: `learners/*.md` other than `TEMPLATE.md`. If there are none, say to run `/setup`
  and stop. If there are several, ask which one.
- `lessons/<name>/stack.md` (their question stack) and any `lessons/<name>/*/log.md` with status
  `in-progress`. If one exists, offer to **resume** it and skip to step 4 (re-read its map first).
- `memory/teaching-method.md` and `docs/lesson-prep-pass-design.md`, in full. They are the
  protocol for everything below.
- The learner's territory map, named in their profile's § Goal (`territories/<slug>.md`). If the
  profile names none, or the learner now wants a different goal, build or choose one as in
  `/setup` step 3 before going on.

## 1. Choose the target at the edge

From the learner's graded state, never from the map's order, propose **1–3 candidate targets**
whose formal inputs they hold or are one short, motivated detour away. Give one line each on what
it is and what it would cost them (what is missing on the way). If they named a topic, include it
and say honestly how far from their edge it is. Let them pick, or propose their own. A target
several rungs above their edge is the failure to avoid: say so and offer the nearest stepping
stone instead.

Create `lessons/<name>/<slug>/` with `log.md` (target, date, status `in-progress`, chosen-because).

## 2. Prepare (the lesson-prep pass, steps 1–3)

Tell the learner in one or two lines: prep takes a while, it is the tutor's private foresight, and
they should not open `lessons/<name>/<slug>/prep/` or expand the prep tool output.

Run the pipeline from `docs/lesson-prep-pass-design.md`, writing everything under `prep/`:

1. **Survey routes.** Launch the `researcher` agent to survey *many* routes to the target, as
   route-records (ingredients, facts taken as given, reachability for *this* learner (give it the
   profile path), circularity verdict, sources). Give it the absolute path of
   `prep/route-survey.md`. It writes the survey there and replies with the path only.
2. **Verify.** Run `claim-auditor` (read-only) on `prep/route-survey.md`, then append its findings
   to that file under `## Audit` and fix what it flags. Then run `red-team` on each load-bearing
   route. Tell it to write its falsifier as a small, stdlib-only Python script in `prep/` and run it
   with `python3` (there is no special guarded runner here, so keep limits small). Append each
   ledger line it returns under `## Adversarial ledger` in the survey. Only surviving routes become
   map material.
3. **Author the probe kit** for the large tools that discriminate between the surviving routes,
   probing the layer the discovery *rides on*, not only the adjacent tools.

Tell every subagent its reply must be **paths and verdicts, never mathematical content**. Subagent
replies and file reads show up as collapsed tool output. Never restate prep content in your own
text.

## 3. Probe, select, assemble (steps 4–6)

- Run the probe kit **live** (cheapest-first ladder; no probe may leak that its tool is
  load-bearing). This is finding the edge for this target. Update the learner profile with what you
  observe.
- Select the route through the fewest genuinely missing tools, unless one short, motivated new
  tool beats a long slog. A missing tool worth having becomes a sub-target with its own sub-prep.
- Assemble `prep/teaching-map.md` per the design doc: chunked narrative with key ideas and traps,
  a **leading example per result**, complete worked-example objects, the pre-authored question
  tree with a private answer key per question, reserve routes, a fact-ledger, and a
  verified-results ledger. ⚠ **Answer keys are computed (from a script) or gated
  (claim-auditor → red-team), never written from recall.** A key with neither is not ready.

## 4. Teach from the map

IBL per `memory/teaching-method.md`, with its per-question gate before every question and every
answer. Translate map notation into the learner's own before speaking. Keep the question stack in
`lessons/<name>/stack.md` current (push on a sub-question, pop on resolve).

⚠ **JIT trip-wire (live instruction, not background):** the moment you would answer from anything
other than a pre-authored question or key (a learner tangent, a reserve route, an optional frame),
you have left the spine. **STOP**, run a just-in-time prep for that point (survey → verify → author
the key, into `prep/jit-<topic>.md`), and only then pose the next question.

At the start, offer once: "If you're willing, rate any of my turns 0–100 as we go. It's the most
useful feedback this test can get." Record ratings in `log.md`.

Log `/friction` yourself whenever the map proves wrong, insufficient or misleading, or the
learner has to correct you.

## 5. Close (also when stopping mid-lesson)

- `log.md`: status (`done` / `in-progress`), what they discovered and how, where it broke, ratings.
- `learners/<name>.md`: update grades **by how acquired** (self-derived / rebuilt / granted /
  fact-held-why-not / absent), misconceptions, process asks, a lesson-history line.
- Suggest `/retro` if they gave feedback, and mention `/share-data`.
