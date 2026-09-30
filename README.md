# Crosswalk Lookup

**Status: Verified — author sign-off complete 2026-09-16 (see `docs/VERIFY_CHECKLIST.md`). Released on Zenodo: [10.5281/zenodo.22785152](https://doi.org/10.5281/zenodo.22785152).**
**Version:** 0.1.0 (2026-09-16)
**Category:** Software and interactive resources

A lightweight web tool that displays one TSA Pipeline-2021-02 performance-based
cybersecurity outcome alongside its mapped controls from five major frameworks —
NIST SP 800-82, NIST SP 800-53, IEC 62443, CIS Controls v8, and NIST CSF 2.0 — so
operators, auditors, and researchers get an instant, unified view of compliance
options for CIP / CIRP / CAP documentation.

**Purpose:** the author frames this project as three things at once —

- a **research crosswalk**: an original, citable mapping between a federal directive and
  five independently governed control frameworks, with sourcing and limitations documented
  to research standards
- a **publication artifact**: a versioned, DOI-able output (via GitHub + Zenodo, once
  verified) with its own citation record, authorship, and license
- a **compliance-prep aid**: a practical lookup an operator, auditor, or researcher can use
  directly when assembling CIP/CIRP/CAP documentation

These three roles aren't in tension, but they do pull in different directions — the
compliance-prep use case wants maximal coverage and confidence, the research/publication use
case wants every judgment call disclosed rather than smoothed over. `docs/LIMITATIONS.md`
and the `author-mapped` flags in `crosswalk.csv` exist to keep the third role's honesty from
being sanded down by the first two.

## What it covers

Six TSA Pipeline-2021-02 performance-based outcome groups, drawn from TSA's own public
press materials and the NIST CSF v2.0 / CPG–TSA crosswalk filed in regulations.gov docket
TSA-2022-0001:

1. Network Segmentation
2. Access Control
3. Continuous Monitoring
4. Patch Management
5. Governance & Risk Management
6. Assessment & Incident Response

For each, `data/processed/crosswalk.csv` gives the mapped control IDs, a short description,
and a source citation in five frameworks (30 rows total). See `docs/CODEBOOK.md` for column
definitions.

## How to run

This is a static site with no build step and no server-side code.

1. Open `site/index.html` in a browser — the crosswalk data is embedded inline as JSON, so
   no fetch/CORS setup is needed.
2. To regenerate `site/index.html` from `data/processed/crosswalk.csv` after editing the
   data, run `python3 code/02_build_site.py` from the repository root.

## Sources and licenses

| Source | License / access |
|---|---|
| TSA Security Directive Pipeline-2021-02F and press materials | US government work, public domain |
| NIST SP 800-82 Rev. 3, NIST SP 800-53 Rev. 5 | US government work, public domain |
| NIST CSF v2.0 / CPG–TSA crosswalk (regulations.gov docket TSA-2022-0001-0041) | Public rulemaking record |
| Open Security Architecture, "TSA Pipeline SD — Control Mappings" | CC BY-SA 4.0, attribution required |
| IEC 62443-3-3, IEC 62443-2-3 | Proprietary ISA/IEC standard — control IDs and functional summaries only, no verbatim text reproduced |
| CIS Controls v8 | CC BY-NC-ND 4.0 — safeguard IDs + original paraphrase only, no verbatim text reproduced |

Full citations with URLs and access dates are in `data/raw/PROVENANCE.txt`.

## Limitations

See `docs/LIMITATIONS.md` — in particular, the IEC 62443 and CIS Controls v8 mappings are
the author's domain-knowledge judgment calls, not pulled from one ready-made authoritative
crosswalk (`source_type = author-mapped` in `crosswalk.csv`). Every control ID and title in
those cells has been independently re-confirmed against a secondary source (see
`docs/qa_report.txt`), and the author has separately confirmed the outcome-to-control
assignments and the primary SD PDF wording by hand (2026-09-16).

## License

Code: MIT (`LICENSE`). Crosswalk dataset and documentation: CC BY 4.0, **except** the
CIS Controls v8 and IEC 62443 cells in `crosswalk.csv`, which remain governed by their
own source licenses noted above and are not sublicensed under CC BY.

## Citation

See `CITATION.cff`.

## Authors

See `AUTHORS.json`. Corresponding author: Friday Ogochukwu Ikwuogu (ORCID
0009-0009-2222-1318), Independent Researcher, Odessa, Texas, USA. Co-authors: David
Mike-Ewewie and Osorachukwu Maurice Ayozie, University of Texas Permian Basin — matching
the co-author list on the related "TSA Pipeline Policy-to-Control Crosswalk" project,
since both share the same underlying dataset.

## Maintainer

Friday Ogochukwu Ikwuogu — fo.ikwuogu@gmail.com

## AI assistance

**AI assistance:** AI coding tools (Claude, Anthropic) were used for code scaffolding, test fixtures, and documentation drafting. The problem definition, methodology, classification rules, mappings, and analytic decisions are the author's own.
