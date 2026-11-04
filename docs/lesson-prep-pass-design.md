# Lesson-prep pass — design (v2)

**Provenance.** Designed with Nadav (2026-07-17 design session), validated by **teaching-run-2**, refined
2026-07-18 with the reachability-probe / learning-edge mechanism (v1), and revised 2026-07-20 after
**teaching-run-3** with the verified-results ledger, JIT-prep-on-trigger, the depth-probe fix, and the
anti-lecture discipline (v2 — all Nadav-endorsed; see `../memory/teaching-run-3-findings.md`). Living doc
under Nadav's authority (like `../memory/teaching-method.md`) — corrected through review, never rewritten by
an engine. Non-spoiler: this is the abstract design, safe for the learner to read. Legend: ★ key idea · ⚠ trap / caution.

## Why it exists
Before teaching a specific target (a concept or a proof), the agent **prepares** — task-scoped foresight, not
a global model of the field — then teaches *from* the plan instead of improvising turn-by-turn. Motivation,
earned not asserted:
- **Run-1 (no prep):** improvised teaching → a multi-hour circular goose-chase and abstract examples the
  learner couldn't grip.
- **Scaffolding/path errors are the ONE class the learner cannot catch** — catching them needs the very
  knowledge being learned. So "the learner corrects the agent" is not a safety net for the errors that matter.
  The agent must walk in with verified foresight.
- **Run-2 (from prep):** the learner *discovered* the target proof in ~8 turns, no goose-chase — validated.
- **Run-3 (from prep, again):** discovery validated a *second* time — but the toolkit *underneath* the
  discovery needed a from-scratch rebuild the probe under-read, and the agent lectured + mis-diagnosed on
  every improvised turn. Lesson: pre-authoring holds exactly where it exists; the fix is a sharper depth-probe
  + JIT-prep for the unforeseeable rebuild + a verified-results ledger to cache both — not more blanket upfront breadth.
This is a **rich** textual model, NOT the rejected reductive typed-graph. Richer model, not none.

## The pipeline
1. **Survey routes (not one).** The `researcher` surveys *many* routes to the target. Each is a **route-record**:
   ingredients · facts-taken-as-given · reachability-vs-learner · circularity/soundness verdict · sources.
   ★ Breadth is deliberate: an over-prepared spread of routes is how the plan stays honest when the learner
   surprises it mid-lesson (you can follow a route you did not pre-pick).
2. **Verify before it's a map.** The survey is a *bundle of claims*, and a wrong map is worse than none. Gate
   each load-bearing route through the project's pipeline: **claim-auditor** (compute-free — does the write-up
   follow from its cited evidence at honest scope?) → **red-team** (falsifier — is it actually true /
   non-circular? runs a concrete computation). Only survivors become map material. ⚠ The gate catches the
   scaffolding errors the learner can't.
3. **Author the probe kit.** For the **large** candidate tools that *discriminate between the surviving
   routes*, pre-author a reachability probe (see "Reachability probe" below). Pre-authored, off the live clock
   — because the run-2 evidence is that questioning discipline holds at prep-time and lapses under live pressure.
   ⚠ **Probe the sublayer the discovery RIDES ON, not just discovery-adjacent tools** (run-3: the probe tested
   pullback + 1-dimensionality, which he held, but not the order/div/uniformizer layer underneath — the
   rustiest — and the learner model over-credited a *named* background he did not actually have). Verify the
   ACTUAL mental model; never trust a named background.
4. **Probe → find the learning edge.** Run the probe (cheap, task-scoped, *before* the lesson commits) to
   resolve which large tools the learner actually holds. ★ This probing **is** locating the learning edge —
   the frontier is not a separate module; it falls out of route-survey + probe.
5. **Select the route at the learning edge.** Pick the route through the **fewest genuinely-missing tools** —
   ⚠ *except* when one short, motivated new-tool detour beats a long tool-avoiding slog (the **cost tradeoff**,
   still a judgment call — see Soft spots). A missing-but-worth-it tool becomes a **sub-target**: recurse a
   sub-prep for it (the MathILy "make it a separate curricular goal" move). Recursion bottoms out at tools the
   probe shows the learner holds.
6. **Assemble the map** for the chosen route (heavy authoring happens only here, after selection):
   - narrative in **chunks** with key ideas ★ and traps ⚠ marked;
   - **named traps** (e.g. "counting the kernel fiber is circular — name it, don't prove it");
   - **complete worked-example objects** — full data (the *entire* isogeny incl. the Y-map, the target curve,
     every definition), never just the load-bearing fragment; the learner checks his reasoning against the
     whole object;
   - ⚠ **tag a LEADING example per result, distinct from the running/illustration one (teaching-run-4,
     2026-07-30, Nadav-endorsed).** A *leading* example is concrete, spoiler-free, and **poses the question the
     result answers** (P1/P2 — examples-first, suggestive); a *running* example checks the answer after the fact.
     Run-4 had complete objects but slotted them all as running/illustration (the concrete 2-isogeny appeared only
     as Chunk-4 "in the flesh"), so the construction was taught abstract-first — the decorative use P2 rejects.
     For EACH result, the map's question tree must open with its leading example. ⚠ Where exhibiting the answer
     would spoil the discovery (the dual's *construction* — showing φ̂ hands it over), the leading example still
     frames the **motivating question** concretely (real curve, real torsion) without exhibiting the answer; for
     downstream results with no spoiler risk (e.g. ker φ̂=φ(E[n])) it leads with the full concrete instance.
     ★ **Pick-up constraint:** this discipline reaches the teacher only because it lives in `teaching-method.md`
     (loaded every run) AND is tagged in the map (run from directly) — NOT design-doc-only. Same lesson as the
     JIT trip-wire: a discipline the kickoff doesn't load does not fire (that's why the dual's JIT never triggered).
   - a **pre-authored question tree** — opener *and* the anticipated mid-lesson branch-points, each carrying a
     private answer key + a "what-not-to-reveal" note;
   - the **probe kit** and the **reserve routes** (for honesty-under-surprise);
   - a **disambiguated fact-ledger** — names that collide breed the confusion the map exists to prevent
     (run-2's sharpest audit catch was two similarly-named facts making an elementary step look circular);
   - a **verified-results ledger seed** — the load-bearing lemmas this route depends on, each verified upfront
     and written as *given* so the live lesson (and any JIT sub-prep) references them instead of re-deriving
     (see "JIT prep, the verified-results ledger, and the non-double-charge rule" below).
7. **Teach from the map.** IBL per `teaching-method.md`'s 14 principles + the **per-question gate**
   (key-first · no-leak · minimal-scaffolding · notice⇒why). **Translate map notation into the learner's own
   before speaking** (run-2: private "u/v" leaked; he uses α/β). Run-3 disciplines for the **improvised turns**
   where every rating crash clustered:
   - ⚠ **Diagnose the ACTUAL stuck-point before responding at all** — do not pattern-match to an assumed
     misunderstanding (run-3: answered "why can't poles appear" when he flagged an *unearned fact in the
     question*; ran past his `x²` probe). Read his message for the real confusion first (teaching-method 4/5).
   - ⚠ **When a question rests on an unearned fact, RE-POSE a better question — do NOT answer it.** ("I wasn't
     asking you to answer, I was asking you to come up with a better question.")
   - ⚠ **Do not lecture, even on "why."** Give the single missing fact, then hand the ball back
     (teaching-method 7) — BUT ★ **don't over-atomize:** bundle as many sub-questions as cohere into one move
     (1–3), no more; a lone tiny question where a small bundle would let him see the connection whole is its own failure.
   - **Reload his prior work in HIS words** when you reference something he built but hasn't used lately.
   - **Never dress an imported/granted theorem as elementary** — name the import, offer grant-vs-earn (teaching-method 11/14).
   - **Log friction** whenever the map is wrong, insufficient, or misleading — a bad map surviving into a live
     lesson is the exact failure this project fears, so that friction is the primary signal for whether the prep worked.

## JIT prep, the verified-results ledger, and the non-double-charge rule (run-3, Nadav-endorsed 2026-07-20)
IBL is responsive, so some needs (run-3's from-scratch toolkit rebuild) cannot be pre-authored. Resolved design:
- ★ **JIT prep is a necessary component** — not optional. When a depth-probe or a live wall surfaces an
  unforeseen missing sublayer, prep it just-in-time (survey → verify → teach), on trigger, mid-lesson.
- ⚠ **The trigger must be MECHANICAL, and the protocol must be LOADED (teaching-run-4, 2026-07-30, Nadav-endorsed).**
  Run-4 proved "on trigger" was too soft: JIT *fired* where the agent happened to ground itself (it read the route
  survey before the Pic⁰ reserve route — which held, despite being the heaviest route) and *did not fire* on an
  improvised optional-frame detour (fact B — which collapsed 50→20, reproducing the runs 2–3 improvised-turn
  failure). Same session, both outcomes: **grounded held, improvised collapsed.** Two fixes:
  1. **Mechanical trip-wire:** *"I have left the pre-authored spine's question tree"* **is** the JIT trigger —
     the moment you answer from anything but a pre-authored question/key (an optional (B)/(D) frame, a reserve
     route, a learner tangent), STOP and run the JIT pass (survey → verify → author key → resume) **before**
     posing the next question. Do not treat optional/reserve material as "a quick rider." (This subsumes the
     weaker "author the optional/reserve question-trees to spine standard" — do that too where foreseeable, but
     the trip-wire is the safety net for the unforeseeable.)
  2. **Load it in the kickoff.** The teaching-agent kickoff must carry this JIT trip-wire as a first-class live
     instruction — in run-4 it lived only here and in the memory index, so the agent had awareness but not a live
     "STOP and prep" reflex. Prep authors: put the trip-wire in the kickoff, not only in this design doc.
- **Upfront breadth is still allowed** — the two coexist; adding *foreseeable* breadth to the offline prep
  still earns its keep.
- ⚠ **Non-double-charge rule.** Each prep item lives in exactly ONE place: upfront if foreseeable (cheap, done
  once), JIT if only surfaced live (live = expensive). Breadth that would be incurred in *both* must clear a
  **higher justification bar**. Do not pre-author what will be re-prepped live anyway.
- ★ **Verified-results ledger** — the mechanism that realizes all three. A running per-session store of
  established lemmas: verify once, write it down as *given*, reference thereafter, **never re-derive**. It is
  simultaneously (a) the **caching fix** for the agent's redundant per-turn re-verification — infra
  prompt-caching makes re-*reading* cheap but does NOT cache re-*derivation*; (b) **consolidation** for the
  learner (the "what's settled" half of the question stack); and (c) the **enforcement** of the
  non-double-charge rule across the upfront/JIT boundary — upfront prep writes verified results in, JIT
  *references* them. The sealed map already was a static version of this cache for the discovery phase; the
  foundation phase had no ledger → live re-derivation every turn → the latency Nadav flagged.

## Answer keys are a distinct artifact class (Nadav, 2026-07-31)

**The evidence.** Three consecutive prep gates were killed by the same thing: an **un-computed
datum sitting in an answer key**. Route claims get a falsifier script; answer keys get authored
from recall and skip it. Two instances: a key asserting a general fact that is false at exactly
the parameters the branch uses — which **would have graded a correct learner wrong** — and a
worked example built on a curve that does not exist over the field stated. Twice the correct data
was already written down elsewhere in the same directory.

**The rule.** An answer key is not prose in a map; it is an artifact with its own verification
obligation, and it never ships unverified. Two routes, by what kind of answer it is:

- **Computable keys — COMPUTE them.** Any key whose content is a number, a curve, a group order,
  a count, a worked example: it comes out of the falsifier script, not out of memory.
  Nadav: *"the more we can do from scripts the better."*
- **Non-computable keys — GATE them.** Most keys are *informal proof arguments*, not numbers, and
  no script checks those. Nadav: *"many answers will not be numeric but rather will be informal
  proof arguments so we also need a mechanism to trigger the relevant gates before we commit to
  claims, as usual."* So a key carrying an argument goes through the project's standing gate —
  **claim-auditor → red-team** — before it is committed to the map. Same machinery as every other
  claim; the change is that keys stop being exempt from it.

**Mechanically:** the map's answer-key section carries, per key, either the script + line that
produced it, or its gate verdict. A key with neither is not ready to pose a question from.

## Reachability probe (the learning-edge finder)
Resolve "does the learner hold tool X?" cheapest-first; only fire this ladder for **large** facts (small
motivated tools are cheaper to just teach than to carefully probe for — which kills most of the cost and risk):
1. **Check the evidence** — transcripts / the knowledge model. Grows richer per student over time; a *new*
   student simply has less here and leans on the lower rungs.
2. **Just ask** — "do you know X?" Cheap, and often enough.
3. **Hypothetical probe** — only when the ask is inconclusive: a setup built from tools he *definitely* holds
   plus the one being probed, **no confounding unknowns**, and see whether he **offers the tool himself**.
   Must not leak that X is load-bearing (that would spoil the discovery the lesson is for) — hence pre-authored
   as an isolate-and-don't-leak question (`teaching-method.md` principle 5).

⚠ **Depth, not just breadth (run-3).** Run the ladder on the layer the target discovery *depends on*, not only
the tools adjacent to it. A rung-2 "just ask" that returns "I know it, rusty" is NOT sufficient for a
load-bearing sublayer — escalate to rung 3, and probe the *actual* mental model (does he read `dx` as a form or
a function?). A mis-calibrated background is exactly what forces an improvised live rebuild — the run-3 weak link.

## What the prep produces (artifact shape)
A **teaching map** object for the target: goal · standing hypotheses · learner entry-state · the chosen route
as chunked narrative (key ideas + traps) · complete worked-example objects · pre-authored question tree · probe
kit · reserve routes · fact-ledger · **verified-results ledger seed** · corrections/audit-trail. Worked
instance (sealed spoiler): `../experiments/isogenies/prep-sealed/kerdeg-teaching-map.md`.

## Evidence & provenance
- **Baseline:** `../experiments/isogenies/naive-baseline.md` (no model) and run-1 (`../memory/teaching-run-1-findings.md`, the goose-chase).
- **First from-prep run:** `../memory/teaching-run-2-findings.md` — crux solved ~8 turns; the map earned its
  keep exactly where used; residual failures clustered on *improvised* (not pre-authored) questions → drove the
  pre-author-deeper + probe-kit refinements here.
- **Second from-prep run:** `../memory/teaching-run-3-findings.md` — discovery validated again; replicated and
  pinned the "failures cluster on improvised turns" finding one layer down (the toolkit-calibration sublayer)
  → drove the v2 additions: depth-probe, JIT prep, verified-results ledger, anti-lecture discipline.
- **Third from-prep run (first v2 test):** `../memory/teaching-run-4-findings.md` (the dual isogeny) — discovery
  spine validated a third time; verified-results ledger worked; depth-probe half-worked (right the fact was
  rusty, wrong that the *build vehicle* — division polynomials — was held). **Headline:** the v2 JIT-prep-on-
  trigger safeguard *existed but did not fire* on the off-spine detour, reproducing the runs 2–3 collapse → drove
  the **mechanical JIT trip-wire** + **load-it-in-the-kickoff** fixes above, and the **"that argument
  generalizes" one-prompt move** (see `../memory/teaching-method.md`).
- **Eval rubric & run-1 instance:** `../experiments/isogenies/prep-pass-run.md`.

## Soft spots (not yet resolved — do not pretend they are)
- **The cost tradeoff** (pipeline step 5): how to weigh "longer/more-complex route" against "just learn one new
  tool." Currently a per-case judgment call; not operationalized. (v2 partly structures the *upfront-vs-JIT*
  axis via the non-double-charge rule, but the route-length-vs-new-tool tradeoff itself is still a judgment call.)
- **Recursion termination & depth** (step 5): sub-prep for a missing tool is itself a prep pass; needs a stop
  rule beyond "bottoms out at held tools."
- **Generalization past the expert learner.** Run-2's learner *built* the flagged-missing tool himself; a
  learner who can't forces heavier reliance on the recursion. Validated for an expert; the non-expert case
  (the tool's real target — non-experts → SQISign) is still open.

## Relationship to the planned pipeline
This is the prep for the **teach** stage. The reachability probe (steps 3–4) is a **task-scoped instance of the
`interview` stage** — scoped to *this* target's surviving routes rather than the whole field.
