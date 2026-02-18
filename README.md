# URF Manuscript README — Template v1.0

This README serves as a **cover page and binding review contract** for a manuscript published under the **Unified Rigidity Framework (URF)**.

It defines identity, scope, verification, and the rules for public review.

---

## Manuscript Identity

**Title:** Boundary-Decoupled Relational Observables, Gauge Fixing, Boundary Jets, and Sharp BMS Decoupling in Classical General Relativity  
**Manuscript ID:** URF-P-0002  
**Author:** Inacio F. Vasquez (Independent Researcher)  
**Status:** FROZEN  
**Version Tag:** urf-p-0002-v1  
**DOI:** 10.5281/zenodo.18684473

---

## Canonical Artifacts

This repository is the **canonical source** for this manuscript.

Required contents:
- `URF-P-0002.tex`
- `URF-P-0002.pdf`
- `README.md`
- `STATUS.md`
- `CITATION.cff`

---

## Verification

**SHA256 (PDF):**

d25d79feac7417c4e449dbdfe4417931c90552bea501e4155c175ff73abcc38c

The PDF was compiled twice with `pdflatex` prior to hashing.

---

## Scope of Review

Review is strictly limited to:
- Mathematical correctness
- Logical coherence
- Adequacy of definitions
- Dependency clarity
- Correct labeling of conditional vs. unconditional results

### Out of Scope
- Empirical benchmarking
- Detector or information-theoretic models
- Performance comparisons
- Sociological or speculative claims

---

## Review Process

All public review occurs via the **URF Open Review Ledger**.

**Review issue:**  
(to be created in `urf-open-review-ledger`)

Feedback **must** be classified as one of:
- `ERROR`
- `MISSING ASSUMPTION`
- `CLARIFICATION`
- `NON-BLOCKING SUGGESTION`

Unclassified feedback is ignored.

---

## Claims Policy

- Conditional results are explicitly labeled.
- No claim extends beyond stated assumptions.
- No empirical or model-dependent claims are made unless explicitly stated.

---

## Citation

Please cite using the DOI once assigned or via `CITATION.cff`.

---

## License

Released under the license specified in this repository unless otherwise noted.

---

## Notes

This README is part of the **URF reproducible publication pipeline**.  
It is intentionally minimal and reviewer-facing.
