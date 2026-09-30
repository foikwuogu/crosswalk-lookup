# Build spec — Crosswalk Lookup

```
PROJECT:        Crosswalk Lookup (archetypes: open dataset + interactive public resource)
QUESTION:       For a given TSA Pipeline-2021-02 performance-based cybersecurity outcome,
                which controls in NIST SP 800-82, NIST SP 800-53, IEC 62443, CIS Controls v8,
                and NIST CSF 2.0 map to it?
SOURCES:
  - TSA Security Directive Pipeline-2021-02F and predecessor press materials — tsa.gov —
    accessed 2026-09-14 — US government work, public domain (17 U.S.C. §105)
  - TSA public press release, 2022-07-21, "TSA revises and reissues cybersecurity
    requirements for pipeline owners and operators" — tsa.gov — public domain
  - NIST CSF v2.0 / CPG / TSA requirements crosswalk, docket TSA-2022-0001-0041,
    attachment_1.pdf — downloads.regulations.gov — accessed 2026-09-14 — public docket
    record, US government rulemaking material
  - NIST SP 800-53 Rev. 5 (Security and Privacy Controls) — csrc.nist.gov — public domain
  - NIST SP 800-82 Rev. 3 (Guide to OT Security) — csrc.nist.gov — public domain
  - Open Security Architecture, "TSA Pipeline SD — Control Mappings" —
    opensecurityarchitecture.org — accessed 2026-09-14 — CC BY-SA 4.0, attribution required
  - IEC 62443-3-3 (System security requirements) and IEC 62443-2-3 (Patch management in
    the IACS environment) — ISA/IEC, paid standard — control IDs and functional summaries
    only, no verbatim requirement text reproduced (standard purchase required for full text)
  - CIS Controls v8 — cisecurity.org — CC BY-NC-ND 4.0 — safeguard IDs + original
    paraphrase only, no verbatim safeguard text reproduced, attributed and linked to the
    free CIS download
UNIT:           one TSA performance-based outcome (row) × one framework (column) = one
                crosswalk cell (control ID(s) + short description + source)
MEASURES:       n/a (qualitative mapping, not a computed statistic) — each cell is an
                analytic judgment call the author must verify, not a measured quantity
OUTPUTS:
  - data/processed/crosswalk.csv — the mapping table
  - docs/CODEBOOK.md — column definitions
  - site/index.html — the lookup tool (reads crosswalk.csv)
  - docs/qa_report.txt, docs/LIMITATIONS.md, docs/VERIFY_CHECKLIST.md, docs/NEXT_STEPS.md
  - README.md, LICENSE, CITATION.cff, AUTHORS.json
VENUES:         Artifact preview (verified state, 2026-09-16); GitHub repo + Pages and
                Zenodo DOI once GITHUB_TOKEN / ZENODO_TOKEN are supplied — author
                verification (Step 5) is complete, this is now a token-only blocker
VERIFY POINTS:  all resolved — see docs/VERIFY_CHECKLIST.md (signed 2026-09-16)
  - Every IEC 62443 SR/CR ID and every CIS Controls v8 safeguard ID assigned to each TSA
    outcome — IDs/titles independently re-confirmed against secondary sources; the
    outcome-to-control assignment itself confirmed by the author's own spot-check, 2026-09-16
  - Whether "Governance & Risk Management" and "Assessment & Incident Response" (present in
    the regulations.gov CSF/CPG crosswalk) should be added as additional rows beyond the
    four core outcomes — resolved 2026-09-16: added, now six outcomes (TSA-1..TSA-6)
  - The NIST SP 800-53 control IDs pulled from Open Security Architecture (CC BY-SA 4.0) —
    spot-checked by the author against the primary SD text, 2026-09-16
LICENSE:        Code: MIT. Crosswalk dataset and docs: CC BY 4.0 (with the CIS Controls v8
                and IEC 62443 cells specifically excluded from that CC BY grant, since they
                paraphrase third-party copyrighted material under their own terms — see
                LIMITATIONS.md)
ASSUMPTIONS:
  - Scope is six outcome groups drawn from TSA's own public materials and the
    regulations.gov CSF/CPG–TSA crosswalk (Network Segmentation, Access Control, Continuous
    Monitoring, Patch Management, Governance & Risk Management, Assessment & Incident
    Response) — expanded from the original four core outcomes by author decision, 2026-09-16
  - Fifth framework is NIST CSF 2.0 — confirmed by author
  - CIS Controls v8 handled as ID + original paraphrase + attribution, not verbatim text —
    confirmed by author
  - This is the public front-end for the same underlying dataset as the author's separate
    "TSA Pipeline Policy-to-Control Crosswalk" project — confirmed by author; built fresh
    here since that project's files are not available at build time. Authorship: as of
    2026-09-16, this project's AUTHORS.json matches that project's co-author list (David
    Mike-Ewewie, Osorachukwu Maurice Ayozie), at the author's explicit request for
    consistency — supersedes the 2026-09-14 version of this file, which used Abidemi
    Orimogunje as co-author for this project specifically.
```
