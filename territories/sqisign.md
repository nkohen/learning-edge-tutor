# Territory map — SQIsign (variant-aware)

*A territory map: what there is to learn on the way to a goal, and how it depends on what. Not a
syllabus and not a learner record. Which node to teach next comes from the learner's graded state
in `learners/<name>.md`, never from the order here. This map ships with the tutor: it was drafted
from the literature, used in the author's own teaching runs, and gated once (claim-auditor → red-team).*

**Goal this map serves:** understanding SQIsign. For a different goal, `/setup` builds a new map.
That map may borrow overlapping nodes from this one, but this file is not reorganized around
another goal.

**Scope** (the author's choice, 2026-07-30). The variants use materially different mathematics:

- **Priority: SQIsign2D-West** (Basso–Dartois–De Feo–Leroux–Maino–Pope–Robert–Wesolowski, 2024),
  the basis of the NIST round-2 submission. This is the terminal target.
- **Also in scope, lower priority:** mathematics relevant to other SQIsign variants (original
  SQIsign, SQIsignHD, the dim-4/dim-8 line) and adjacent oriented-curve constructions. In scope for
  breadth, not what the teaching order optimizes for.

Edges are **formal** (cannot state the next concept without it) or **informal** (motivation or
intuition that makes it learnable but isn't logically required).

> **Status.** The trunk (§A) is corroborated by several teaching runs. The 2D branch (§B) was
> drafted from the literature and gated once (claim-auditor → red-team), which corrected it in
> the places marked ⚠. It is still a *hypothesis about the dependency structure*. A lesson's own
> prep pass re-surveys and re-verifies its target and does not inherit trust from this file.

---

## A. Shared trunk — variant-independent (formal, all of it)

- **Elliptic curves over finite fields** — group law, torsion E[n] ≅ (Z/n)² (char ∤ n).
- **Isogenies** — degree, kernel, separability, #ker φ = deg φ for separable φ.
- **The dual isogeny φ̂** — φ̂φ = [deg φ], ker φ̂ = φ(E[n]), φ̂̂ = φ.
  - More central in 2D-West than in original SQIsign: Kani's lemma (§B) is a 2×2 matrix of
    isogenies and their duals.
- **The Weil pairing** — bilinearity, non-degeneracy, and the **adjoint identity**
  e_n(φP, Q) = e_n(P, φ̂Q). (formal → Kani, → torsion-image isogeny representation)
- **Supersingular curves over F_p²; ℓ-isogeny graphs** — Ramanujan expansion, vertices as j-invariants.
  - informal edge from *random walks / expander mixing* → why these graphs are cryptographically hard.
- **Quaternion algebras & maximal orders** — B_{p,∞}, orders, ideals, reduced norm as a quadratic
  form on a rank-4 lattice. Finding elements of prescribed norm (Cornacchia, LLL).
- **Deuring correspondence** — supersingular curves ↔ maximal orders. Isogenies from E₀ ↔ left
  O₀-ideals, ideal norm ↔ degree, **conjugate ideal ↔ dual isogeny** (𝔞𝔞̄ = (N𝔞) ⟷ φ̂φ = [deg φ]).
  The hinge of every variant.
  - Should have MANY incoming informal edges. It is the concept most learners need analogies for.

## B. SQIsign2D-West branch — PRIORITY (formal unless noted)

The organizing problem: **how do you represent and evaluate an isogeny of large, arbitrary
(non-smooth) degree?** Original SQIsign answers "force the degree to be powersmooth" (→ KLPT, §C).
2D-West answers "embed it in a 2-dimensional isogeny of degree 2^e" (→ Kani). That single
substitution is the whole delta.

- **B0 · Dual algebra on Hom and on products** — composition **bilinear** over Hom. The dual as an
  **anti**-involution: `(φψ)^ = ψ̂φ̂`, `φ̂̂ = φ`, `[m]^ = [m]`. `φ̂φ = φφ̂ = [deg φ]`,
  `deg Φ̂ = deg Φ`, `deg[d] = d^{2g}`. `Hom(A×B, C×D)` ≅ 2×2 matrices with composition = matrix
  multiplication, and the adjoint matrix `M̂ = (φ̂_{ji})`. (formal → Kani's identity) ⚠ Dual
  *additivity* `(φ+ψ)^ = φ̂+ψ̂` is not consumed by the Kani computation.
- **B1 · The isogeny representation problem** — the *motivating question* "what does it mean to
  **have** an isogeny you can evaluate?" (**informal** → the rest of the branch), and *efficient
  representation* as a precise object (SQIsign2D-West Def. 1) (**formal** → the protocol).
- **B2 · Isotropy at g = 1** — `H ⊆ E[N]` isotropic ⟺ `#H | N`. Maximal ⟺ `#H = N` ⟺ kernel of a
  degree-N isogeny. ⚠ The **cyclic** ones are the kernels of *cyclic* N-isogenies, and at
  non-squarefree N they are **not all of them** (E[2] ⊂ E[4] is maximal isotropic and non-cyclic).
  This is the g=1 shadow of "an N-isogeny is not an (N,N)-isogeny". (formal → dim-2 isotropy)
- **B3 · Weil pairing package** — bilinear, non-degenerate, Galois-equivariant, alternating
  (⚠ alternating is what makes a *cyclic* subgroup isotropic; the maximality bound runs on
  `H ⊆ H^⊥` + perfectness, so pin which definition of "isotropic" is in use). The adjoint identity
  and its corollary `e_n(φP,φQ) = e_n(P,Q)^{deg φ}`. The product pairing on A×B.
- **B4 · The (d₁,d₂)-isogeny diamond**, with `gcd(d₁,d₂) = 1` (load-bearing) **and the sign
  normalized**. ⚠ Each far leg is fixed by its kernel only up to ±1. The wrong gluing gives
  `φ₂′φ₁ = −φ₁′φ₂`, and then `Φ̂Φ = [d]·Id` fails outright.
- **B5 · Kani's identity** `Φ̂Φ = [d₁+d₂]·Id` — reachable from B0 + B4 alone. **Kani's lemma** (that
  Φ is a d-isogeny of PPAS) additionally needs the B6 import. Kernel
  `Ker Φ = {(φ̂₁P, φ₂′P) : P ∈ E₁[d]}`, of order d². **The keystone.**
- **B6 · Polarizations & PPAS** — polarization λ: A → Â. Principal = isomorphism, and for E it is
  the `P ↦ (P)−(O)` map to Pic⁰(E). The definitional import "`Φ̂Φ = [N]` ⟺ N-isogeny of PPAV".
  **Kani Prop. 1.1** (maximal isotropic ⟺ the quotient is principally polarized), a named black
  box, never smuggled. PPAS = product of elliptic curves or Jac(genus-2 curve). The Rosati
  involution. ⚠ An `N`-isogeny has degree N², not N.
- **B7 · Computing (2,2)-isogenies** — the (2^e,2^e)-chain and the **gluing / generic /
  splitting** trichotomy (the chain generically passes *through* genus-2 Jacobians even when both
  ends are products). Level-2 theta coordinates ("the x-coordinate, one dimension up") or
  Richelot. (formal → verification)
- **B8 · Ideal-to-isogeny without KLPT** — Deuring hinge + norm-equation solving (Cornacchia,
  `GeneralizedRepresentInteger`, LLL) + Kani applied twice + a (2^e,2^e)-chain. **Quaternions are
  NOT removed, only KLPT is.**
- **B9 · The protocol** — Σ-protocol for `EndRing`, Fiat–Shamir **with hints**, soundness w.r.t.
  `OneEnd`. EUF-CMA ⟸ q-unif-hint-OneEnd ≡ q-unif-hint-EndRing. (target)

## C. Original-SQIsign-only — DEPRIORITIZED

- **KLPT / SigningKLPT** — quaternion ideal → equivalent ideal of powersmooth norm. The piece
  2D-West removes.
- **Powersmooth torsion constraints** — the T | p²−1 gymnastics of the original parameter selection.

## D. Adjacent variants — breadth, not the teaching order

- **SQIsignHD** — the same representation problem answered in **dimension 4** (Zarhin's trick).
  The natural second stop after 2D-West.
- **Other 2D variants** (2D-East, Prague-line) — same Kani core, different engineering.
- **Oriented curves & the class-group action** (CSIDH, OSIDH, SCALLOP) — **a different family.**
  A commutative class-group action needs an *orientation*. SQIsign works with *unoriented*
  supersingular curves, where End(E) is a non-commutative maximal order. So the class-group action
  is **not a formal** on-ramp to SQIsign. It remains a legitimate **informal** (motivational) edge
  toward Deuring. The formal on-ramp is the Deuring correspondence itself.

## Sources

**Priority (2D-West):** Basso et al., *SQIsign2D-West: The Fast, the Small, and the Safer* (2024).
Dartois–Maino–Pope–Robert, *An algorithmic approach to (2,2)-isogenies in the theta model*. The
NIST round-2 SQIsign specification. Robert's higher-dimensional-isogeny / Kani-embedding line.

**Trunk:** Silverman, *The Arithmetic of Elliptic Curves* (III, and the Weil pairing in III.8).
Voight, *Quaternion Algebras*. Leroux's thesis and the algorithmic Deuring literature.

**Breadth:** De Feo–Kohel–Leroux–Petit–Wesolowski, original SQIsign (2020).
Dartois–Leroux–Robert–Wesolowski, SQIsignHD.

## Notes for the tutor

- Several nodes are **informal concepts** ("why supersingular, not ordinary", "what it means to
  *have* an isogeny"). Model them; do not drop them.
- A learner coming from elsewhere may hold none of the trunk, or hold parts of the 2D branch
  through another route (abelian varieties, theta functions, lattices). Locate them by interview
  and probe, never by assumption.
