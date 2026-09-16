# Codebook — `data/processed/crosswalk.csv`

30 rows: 6 TSA outcomes × 5 frameworks, one row per outcome/framework cell.

| Column | Type | Definition |
|---|---|---|
| `tsa_outcome_id` | string | Short ID for the TSA outcome (`TSA-1`…`TSA-6`). Stable key for joins. |
| `tsa_outcome_name` | string | The outcome's public name, as TSA names it (Network Segmentation, Access Control, Continuous Monitoring, Patch Management, Governance & Risk Management, Assessment & Incident Response). |
| `tsa_outcome_summary` | string | One-sentence paraphrase of what TSA's SD Pipeline-2021-02F requires for this outcome, drawn from TSA's own public press materials. |
| `framework` | string | One of: `NIST SP 800-82 Rev. 3`, `NIST SP 800-53 Rev. 5`, `IEC 62443`, `CIS Controls v8`, `NIST CSF 2.0`. |
| `control_ids` | string | Comma-separated control/section identifiers in that framework that map to the outcome. |
| `description` | string | Short description of what those controls require, in the author's own words (never verbatim standard text for IEC 62443 or CIS Controls v8). |
| `source_type` | string | `primary` (TSA or NIST material read directly), `derived` (a third-party crosswalk, cited, e.g. Open Security Architecture), or `author-mapped` (the author's own domain-knowledge mapping, not sourced from a single ready-made crosswalk — flagged for verification). |
| `source_citation` | string | Citation for the row, matching an entry in `data/raw/PROVENANCE.txt`. `author-mapped` rows carry a bracketed note on what's been independently confirmed (IDs/titles) versus what remains the author's own judgment (the outcome-to-control assignment). |

## Known-value spot checks

Confirmed by the author by hand, 2026-09-16 (originally flagged during the build for
verification):

1. `TSA-1` × `NIST SP 800-53 Rev. 5` → `SC-7, SC-7(21), AC-4` — **open**, check against TSA SD Pipeline-2021-02F Section A/B and NIST SP 800-53 Rev. 5 directly (this row's IDs are sourced from Open Security Architecture, a third party, not confirmed against the primary SD text itself).
2. `TSA-2` × `NIST CSF 2.0` → CPG 2.H (phishing-resistant MFA) — **open**, check against the regulations.gov docket TSA-2022-0001-0041 PDF, page covering Access Control (this row is sourced directly from that primary docket document, so lower risk, but not independently spot-checked page-by-page).
3. `TSA-3` × `IEC 62443` → `SR 6.1, SR 6.2` — **ID/title confirmed 2026-09-16** against TeepTrak's IEC 62443-3-3 requirements guide ("Audit log accessibility", "Continuous monitoring" — exact match). Outcome-to-SR assignment (that these are the right requirements for *Continuous Monitoring*) is still the author's judgment call, not independently confirmed.
4. `TSA-4` × `IEC 62443` → `IEC TR 62443-2-3` — **confirmed 2026-09-16** this is the correct dedicated patch-management document, and its correct designation is "IEC TR 62443-2-3" (a Technical Report, not a full standard — corrected from the v0.1 citation). Whether to cite it alongside or instead of a specific SR within 62443-3-3 is still the author's call.
5. `TSA-4` × `CIS Controls v8` → Safeguards 7.1–7.7 — **confirmed 2026-09-16** direct from cisecurity.org's own CIS Controls Navigator v8 page: all seven IDs and titles (7.1 "Establish and Maintain a Vulnerability Management Process" through 7.7 "Remediate Detected Vulnerabilities") match exactly, and are v8-specific (not v7 numbering).
