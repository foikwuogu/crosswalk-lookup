# Verification checklist — author sign-off required before publishing

This project does not leave draft status, and nothing gets pushed to GitHub or Zenodo,
until the corresponding author has personally completed this checklist.

## Mechanical (also enforced by `scripts/publish_gate.py` once the repo is pushed)

- [x] No draft stamps remain that shouldn't — **checked 2026-09-16**: the UI's status
      stamp and README status line now read VERIFIED, set only once the sign-off below was
      actually signed
- [x] No open VERIFY-tag placeholders remain in `crosswalk.csv` or the docs without a
      resolution — **checked 2026-09-16**: no unresolved VERIFY tags remain in
      `crosswalk.csv`; the two stray mentions in README.md/CODEBOOK.md describing the old
      tagging convention have been corrected to describe the current, resolved state
- [x] No placeholder-bracket-style markers (an unresolved insert-here marker, etc.) remain
      anywhere — **checked 2026-09-16**: none found
- [x] No secrets or tokens committed anywhere in the repo — **checked 2026-09-16**: none
      found

## Content — the author's own judgment calls

- [x] ~~Re-read the primary SD PDF directly and confirm the outcome names/summaries~~ —
      **confirmed by the author, 2026-09-16**: read directly, matches `crosswalk.csv`
- [x] ~~Spot-check the five known-value checks by hand~~ — **confirmed by the author,
      2026-09-16**, alongside a successful local rebuild (`python3 code/02_build_site.py`
      → "Rebuilt site/index.html: 30 rows, 6 outcomes.", matching this repo exactly) and a
      live local browser check of `site/index.html`
- [x] ~~Check every IEC 62443 SR/CR ID against a licensed copy~~ — **IDs/titles confirmed
      2026-09-16** against an independent secondary source (TeepTrak's IEC 62443-3-3
      requirements guide); zero mismatches, and IEC TR 62443-2-3 corrected from a
      miscited "standard" to its actual Technical Report status. The outcome-to-SR
      assignment itself is confirmed by the author's own spot-check pass, above.
- [x] ~~Check every CIS Controls v8 safeguard number~~ — **confirmed 2026-09-16** by
      fetching cisecurity.org's own CIS Controls Navigator v8 page directly: all 16
      safeguard IDs and titles used in crosswalk.csv match exactly (v8-specific numbering
      confirmed, not v7). The outcome-to-safeguard assignment itself is confirmed by the
      author's own spot-check pass, above.
- [x] ~~Decide whether to add the two additional outcome groups~~ — **resolved 2026-09-16:
      added now.** Governance & Risk Management and Assessment & Incident Response are in
      `crosswalk.csv` as TSA-5/TSA-6 (30 rows total, 6 outcomes × 5 frameworks). Note:
      TSA-5's CIS Controls v8 mapping is flagged as a weaker fit than the others — see
      `docs/NEXT_STEPS.md`
- [x] ~~Confirm the AUTHORS.json author/co-author list against the related project~~ —
      **resolved 2026-09-16: matched.** AUTHORS.json, CITATION.cff, README.md, LICENSE, and
      the site footer now list David Mike-Ewewie and Osorachukwu Maurice Ayozie as
      co-authors, same as "TSA Pipeline Policy-to-Control Crosswalk" (supersedes the
      2026-09-14 Abidemi Orimogunje co-author block for this project)
- [x] ~~Confirm the CIS Controls v8 non-commercial / no-derivatives handling is
      acceptable~~ — **confirmed 2026-09-16** (ID + paraphrase + attribution approach
      chosen explicitly, then reconfirmed alongside the license split below)
- [x] ~~Read `docs/LIMITATIONS.md` end to end and confirm it is still accurate and
      complete~~ — **confirmed by the author, 2026-09-16**: read end to end and returned
      with an edit (item 6 now leads with the project's three-part framing — research
      crosswalk / publication artifact / compliance-prep aid — before the "OT compliance
      alignment" note). Item 5 also corrected in the same pass: it still said "four outcome
      names" from before the scope expansion; now reads "six" and notes the author's direct
      PDF read.
- [x] ~~Confirm the license split~~ — **confirmed 2026-09-16**: MIT code / CC BY 4.0 data,
      with the CIS Controls v8 and IEC 62443 cells excepted, kept as-is

## Sign-off

- [x] I have completed every item above and the project is ready to move to GitHub/Zenodo.

Signed: Friday Ogochukwu Ikwuogu  Date: 2026-09-16

**Verification complete.** This project has left draft status. Publishing to GitHub and
Zenodo is now blocked only on `GITHUB_TOKEN` / `ZENODO_TOKEN` being supplied, not on any
further author review.
