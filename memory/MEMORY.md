# Memory Index — learning-edge (tutor)

Loaded at session start. One line per topic file. Learner state is NOT here. It lives in
`learners/<name>.md` and `lessons/<name>/`.

- [Teaching method](teaching-method.md) — **how to teach, non-negotiable:** examples first (simple, varied, suggestive), diagnose by watching where the learner gets stuck and which tools they reach for, plus the per-question gate. Written by the author from his own runs (on isogenies — the method is topic-general). Read "Nadav" as "the learner".
- [Lesson-prep pass](../docs/lesson-prep-pass-design.md) — **how to prepare a lesson:** survey many routes → verify (claim-auditor → red-team) → probe the learner (= find the edge) → select route → assemble the map → teach, with a just-in-time prep trip-wire. `/lesson` runs it.
- [Territory maps](../territories/) — one file per learning goal: what there is to learn toward it and how it depends on what. `sqisign.md` ships; `/setup` builds others. A map, not a syllabus. The edge comes from the learner's state.
