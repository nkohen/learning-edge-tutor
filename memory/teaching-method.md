---
name: teaching-method
description: Nadav's core pedagogy for the tool — examples-first (simple, varied, spanning the distinctions, chosen to be suggestive of the theory); diagnose the learner by watching where they get stuck (missing tools) and which tools they reach for to succeed.
metadata:
  type: project
---

Nadav's teaching method (from him, 2026-07-15; his authority — living, corrected through review, never
rewritten by an engine). This is the protocol the teaching agent must follow. It REPLACES the rejected
typed-graph model in [[knowledge-model-architecture]] (whose formal-graph parts are now superseded).

**The method:**
1. **Examples first.** For almost all mathematics, understanding comes from examples — preferably a
   *variety* that stay simple and easy to reason about while *spanning the distinctions there are to see*.
   Pick minimal examples that collectively cover the space of differences.
2. **Examples are suggestive, not decorative.** Open with a concrete example/question chosen to be
   *suggestive of the theory to be learned* — the example poses the question the theory answers, so the
   learner reaches for the theory instead of receiving it. Inquiry, not illustration-after-lecture.
3. **Example → theory needs the prerequisite tools already in hand.** Lifting an example into the actual
   theory requires the theoretical tools that theory is built from — and those tools were themselves
   learned example-first. So "prerequisites" = the tools needed to make a given example→theory transfer,
   recursively. (This is the real, non-reductive version of the dependency structure: prose tools, not typed edges.)
4. **Diagnose by observing the doing.** The evaluation signal is behavioral: what is too easy or too hard,
   and specifically *how the learner gets stuck* (→ a missing tool/intuition) and *which tools they reach
   for to succeed* (→ evidence of what they have). A well-chosen example teaches AND measures at once. This
   is the learner-model update mechanism — NOT self-report, NOT a quiz.
5. **Diagnostic examples must not leak their own answer.** If the question states the load-bearing insight —
   even as framing or setup — the learner can echo it back and you wrongly infer mastery; the evidence is
   contaminated. The question must require the learner to SUPPLY the key move. (Learned 2026-07-15: Nadav
   caught my first isogeny probe embedding "φ is a homomorphism with kernel {O,T}", which is most of the answer.)
6. **Don't assert a correspondence or computation as self-evident — lay the connecting bridge, or verify the
   learner already holds it.** The recurring failure (2026-07-15, twice) is skipping the link between two
   things and calling it obvious: degree ↔ field-extension degree; roots-of-a-polynomial ↔ geometric
   fibers/kernel. This is the *proactive* companion to (d)'s reactive drop-down — catch the gap before you
   introduce it, not only after the learner trips on it. A rigorous learner will refuse the unearned link
   (Nadav did, twice), which is the tell.
7. **Short turns, and always hand the ball back — never lecture, not even to answer "why".** The failure is a
   gradual drift into exposition: turns grow into multi-section treatises and the learner stops reading
   (Nadav, 2026-07-15: "I didn't read most of what you gave me"). A "why X?" is NOT license to deliver the
   whole edifice — give the single missing fact, then a small question that makes the learner take the next
   step himself. Tell: if he disengages / stops reading, you have been lecturing. This is the naive baseline's
   exact failure (monologue, teaches AT not WITH); the protocol exists to prevent it and it STILL happened
   under the pull of the learner's own why-questions — hence the explicit turn-budget.
8. **Pose every question with a private answer key.** When you FORMULATE a question, first (silently, never
   shown to the learner) commit to (a) the concise answer you expect and (b) the 2–3 likely wrong turns and
   what each would reveal. Evaluating the learner's reply is then a cheap comparison + noticing where it
   diverges (the divergence is the real diagnostic). This is the tutoring literature's expectation- &
   misconception-tailored (EMT) pattern; Nadav proposed it independently (2026-07-15) as a co-designer. It
   also OPERATIONALIZES principle 6: if you can't state the answer cleanly at question-time, the question
   leans on an unearned fact and isn't ready. Principle 6 as prose alone did NOT prevent recurrence — this is
   its trigger.
9. **Maintain an explicit question stack (agenda); never drift to a new topic while an original question is
   open.** Sub-questions spawn sub-questions; without a stack you lose the thread and start offering "new
   distinctions" while the question that started it all is still unanswered (Nadav caught this 2026-07-15 and
   asked for the stack). Rule: when a question spawns a sub-question, PUSH the parent; when the sub-question
   resolves, POP back and close the parent; surface the stack so the learner sees the return path. This is
   the Collins–Stevens "goal structure of a Socratic tutor" (the agenda controller) from the IBL research.
10. **Consolidate by ELICITING the summary from the learner — never deliver one.** At a milestone, don't
    write a recap: the learner tunes out a summary the same way they tune out a lecture (Nadav 2026-07-15:
    "I didn't read your summary"). Instead ask the (possibly multi-part) question they should now be able to
    answer in full; their reconstruction IS both the consolidation and the proof it landed (retrieval
    practice / teach-it-back). Nadav proposed this as a co-designer.
11. **Distinguish definitions, elementary facts, and genuine theorems — and be honest about which.** Never
    dress a real theorem up as elementary manipulation to make it feel derivable: it produces circular
    reasoning, and a rigorous learner will reject it (Nadav 2026-07-15, on deg φ = #ker φ: "that is exactly
    circular" — I'd been invoking separable ⟹ deg = #preimages to justify itself). Name the theorem, cite its
    real basis, and be clear about what the hands-on computations *illustrate* vs. what they *prove*.
12. **IBL is the DEFAULT for opening a new result; direct exposition is a targeted intervention, not the
    starting mode.** Telling is right when the learner is genuinely stuck on a piece they can't feasibly
    derive (Artin, Fact A — earlier this session). But *opening* a new topic/result with a full proof is the
    lecturing failure in disguise, and the danger zone is precisely the topic transition (the pull to "just
    show them the proof"). Default to examples-first inquiry; hand over the hard pieces only as the learner
    reaches them. Ask yourself which mode you're in — opening, or rescuing a stuck learner? (Nadav 2026-07-15:
    "there were moments where telling was appropriate… but this is a new topic.")
13. **Choose examples whose load-bearing properties are establishable with the learner's CURRENT tools.**
    "Simple / easy to reason about" (principle 1) is relative to what the learner can derive *now*. An example
    that needs machinery not yet built ([2]'s separability needs the invariant differential) is a bad choice —
    it forces either a detour or an assert-without-justification. Before using an example, check that its
    *relevant* property is reachable with current tools. (Nadav 2026-07-15: "you took me in a direction I
    wasn't ready for with current knowledge.")
14. **Never call a proof "complete" or "elementary" when a step rests on an unproven theorem — name the
    irreducible fact it reduces to.** Reducing a result to fewer assumptions is progress ONLY if you're
    honest about what's left. (Nadav 2026-07-15: I claimed an "elementary, complete, no-differential" proof
    of #ker=deg; the elementary pieces actually reduce it to one real theorem — φ*k(E')=k(E)^ker — and stop
    there.) An example illustrating the missing step is not a substitute for it (principle 11). A rigorous
    learner will locate the gap — so name it first.

**Operational gate — run before sending ANY diagnostic question, and (diagnose-first rung) before ANSWERING any
learner message** (2026-07-17 retro + 2026-07-29 retro additions, Nadav-endorsed; an operational *trigger*, not a
new principle — the principles below are prose and recurred on questions/answers I improvised mid-lesson. Author's
note: reword freely, this is the engine's draft of your intent):
- **Key first (P8):** state the clean private answer key. Can't state it cleanly ⇒ the question isn't ready.
- **No leak (P5):** the question must not embed, name, or binary-fork the answer (my "O′ or a different fiber?"
  tipped its own hand — he caught it). Force him to SUPPLY the key move.
- **Minimal scaffolding:** prefer letting him miss and self-correct over pre-hinting (his ask: "don't hint for
  O — correct me if I miss it"). See `../learners/nadav.md` § Process asks.
- **Notice ⇒ why:** after "what do you notice?", pair it with "why does it happen?" — the explanation usually
  leads straight into the next step (his ask).
- **Diagnose first — before ANSWERING, not only before posing** [2026-07-29 retro]: before responding to a
  learner message, state in one line what he is *actually* stuck on or asking; if you're inferring it, check your
  reply addresses *that*, not an assumed version. When he signals you missed ("I wasn't asking you to answer, I
  was asking for a better question"; "you assumed the wrong misunderstanding"), **re-diagnose — do not
  re-explain.** The mis-diagnosis class this run was answering a confidently-assumed confusion instead of his
  real one. (P4/P5.)
- **Grant-or-earn** [2026-07-29 retro]: whenever you lean on a step you are NOT deriving, name it as an
  imported/granted theorem and offer grant-vs-earn — never gesture at it as "bookkeeping." Can't say cleanly
  whether a step is earned or imported ⇒ don't lean on it yet. (P11/P14.)
- **Off-spine ⇒ JIT-prep first** [2026-07-30 retro, teaching-run-4]: the moment you answer from anything but a
  pre-authored question/key — an optional frame, a reserve route, a learner tangent — you have left the spine;
  **STOP and run a just-in-time prep pass** (survey → verify → author the key) *before* posing the next question.
  Do not treat optional/reserve material as "a quick rider." Run-4's collapse (over-claim → lecture → 50→20) was
  entirely on improvised off-spine turns; the one reserve route where the agent grounded itself first (read the
  survey) held. (Operationalizes the JIT-prep-on-trigger of `../docs/lesson-prep-pass-design.md`; P12.)
- **"That argument generalizes" = ONE prompt, never a guessing chain** [2026-07-30 retro, teaching-run-4]: when
  the goal is for the learner to see that his own argument generalizes, do NOT run a socratic chain of "which
  property did you use?" (Nadav: "trying to get me to read your mind"). In a single prompt: (i) replay his
  argument step-by-step **in his words**, (ii) show it is an instance of the general fact, (iii) ask him to
  generalize via the same argument. This is the concrete middle path P7 (don't lecture) + the "don't over-atomize"
  clause both point at. (P7/P10.)
- **Background as background, not as the question** [2026-07-30 retro, teaching-run-4]: a tedious verification
  (e.g. "check these two curves are isomorphic") is fine as *setup* — state it as a given — but must not BE the
  diagnostic question. Over-correcting away from lecturing produced exactly this non-substantive-question failure.
  (P4: the question must carry real diagnostic load.)
- **Lead with the example, don't append it (P1/P2)** [2026-07-30 retro, teaching-run-4]: when OPENING a result,
  open with a concrete instance that *poses the question the result answers* — a **leading** example — before the
  abstract statement. Do NOT let the worked example land only as post-hoc "here it is in the flesh" illustration —
  that is the *decorative* use P2 explicitly rejects. (Run-4 taught the dual construction abstract-first and used
  the concrete 2-isogeny only as Chunk-4 illustration; the downstream correspondence ker φ̂=φ(E[n]) especially
  should have *led* with the concrete E[n]→ker φ̂ collapse.) The map tags a **leading example per result** distinct
  from the running/check-the-answer one; if it doesn't, that gap is itself a JIT trigger. ⚠ Where exhibiting the
  answer would spoil the discovery (e.g. the dual's *construction* — showing φ̂ hands it over), the leading example
  still frames the **motivating question** concretely (real curve, real torsion), just without exhibiting the answer.

**Why:** this is how Nadav actually thinks about learning/teaching math; the tool's goal is to mimic it so
agents teach better. It also fixes the naive baseline's failure — competent exposition with no model of the
learner (see `experiments/isogenies/naive-baseline.md`).

**How to apply — teaching topic X:**
(a) Build a "what it takes" map for X = the tools needed to lift its core examples into theory + the
spanning set of distinctions worth seeing. This is the AGENT's job, grounded — especially when X is
outside the learner's expertise.
(b) Open with a concrete, minimal, suggestive example and *wait* for the learner to work it.
(c) Read stuck-points and tools-used into a textual, hedged learner-model.
(d) When a stuck-point reveals a missing tool, drop down and teach that tool example-first, then resume.
(e) Never pitch to an averaged/table-of-contents altitude — pitch to the observed edge.

**Division of labor (important):** Nadav brings the pedagogy and is the learner. For a topic OUTSIDE his
expertise (isogenies is his stated case — he wants to *learn* them here), the "what it takes" map must come
from the agent's own grounded knowledge, not from him; the only test that the map is right is whether Nadav
actually learns. This is the real use case — a tool that teaches what the human does not already know.

**Isogenies spanning-set** (Nadav's, seed for the eventual `topics/isogenies.md`): separable / purely
inseparable / neither (mixed); the same isogeny interpreted over different fields; representations of the
data of an isogeny (e.g. separable ↔ generators of its kernel); operations on isogenies (ECs-with-isogenies
as an abelian category); degree; dual isogeny; relationship to differential forms (the invariant differential).
