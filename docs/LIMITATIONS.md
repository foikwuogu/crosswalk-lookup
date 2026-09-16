# Limitations

1. **Scope is the six outcome groups in the regulations.gov CSF/CPG crosswalk, not
   necessarily the full text of the directive.** SD Pipeline-2021-02F is organized into
   sections (A through H across SD-1/SD-2) that this project groups into six outcomes
   following the regulations.gov docket TSA-2022-0001-0041 crosswalk's own structure:
   Network Segmentation, Access Control, Continuous Monitoring, Patch Management,
   Governance & Risk Management, and Assessment & Incident Response. This is TSA/CISA's own
   grouping, not the author's invention, but it is still a grouping — always cite the
   specific SD section for anything compliance-critical, not just the outcome name.
   Governance & Risk Management's CIS Controls v8 mapping is a weaker fit than the other
   five outcomes' CIS mappings (see item 2).

2. **IEC 62443 and CIS Controls v8 mappings are author-mapped, not sourced from one
   ready-made crosswalk.** The NIST SP 800-53 and NIST CSF 2.0 columns come from citable
   published crosswalks (Open Security Architecture; the regulations.gov docket). No
   equivalent published TSA-to-IEC-62443 or TSA-to-CIS-Controls-v8 crosswalk was found
   during this build's research pass. Those two columns are the author's own domain-mapping
   from the outcome descriptions to the standards' functional requirement structure, and
   every such cell is flagged `source_type = author-mapped` in the dataset (12 of 30 rows,
   across all six outcomes: 2 per outcome, IEC 62443 + CIS Controls v8).
   **Update 2026-09-16:** every control ID and exact title in these 12 cells has since been
   independently re-confirmed against a secondary source (TeepTrak's IEC 62443-3-3
   requirements guide; standards catalogs for IEC 62443-2-1 and 62443-3-2; cisecurity.org's
   own CIS Controls Navigator v8, fetched directly) — zero ID/title mismatches. The
   outcome-to-control assignment itself — that, say, "Network Segmentation" is best
   represented by SR 5.1/5.2 rather than some other combination — has since been confirmed
   by the author's own hand spot-check (2026-09-16); see `docs/VERIFY_CHECKLIST.md`.

3. **IEC 62443 requirement text is not reproduced.** IEC 62443-3-3, IEC TR 62443-2-3,
   IEC 62443-2-1, and IEC 62443-3-2 are paid ISA/IEC standards (62443-2-3 is specifically a
   Technical Report, informative rather than normative). Only requirement/document IDs
   (e.g., `SR 5.1`) and short, original functional summaries appear here — never the
   standard's own requirement wording. Anyone using this tool for compliance work needs a
   licensed copy of the standard for the actual requirement text.

4. **CIS Controls v8 content is paraphrased, not quoted, and is CC BY-NC-ND licensed.**
   CIS's own terms (cisecurity.org/terms-of-use-for-non-member-cis-products, accessed
   2026-09-14) are Creative Commons Attribution-NonCommercial-NoDerivatives 4.0. This
   project reproduces only safeguard IDs plus an original paraphrase, with attribution and a
   link to CIS's free download — not verbatim safeguard text, and this project itself is
   non-commercial. If the project's use ever becomes commercial, or if closer reproduction
   of CIS Controls text is wanted, contact CIS for explicit permission first.

5. **TSA SD Pipeline-2021-02F could not be fetched directly in this build session** (403
   response from tsa.gov, on two separate attempts: 2026-09-14 and 2026-09-16). The six
   outcome names and summaries are corroborated across TSA's own 2022-07-21 press release,
   the regulations.gov docket TSA-2022-0001-0041 crosswalk, and secondary reporting that
   quotes the directive directly. **Update 2026-09-16:** the author has since read the
   primary PDF directly in their own browser and confirmed it matches `crosswalk.csv`.

6. **This project is a research crosswalk, publication artifact, and compliance-prep aid,
   not an official standard mapping or compliance certification artifact.** It is intended
   to support planning, documentation drafting, and comparison work for CIP/CIRP/CAP
   preparation; it is not TSA, NIST, IEC, or CIS endorsement or a substitute for an
   operator's own compliance review with counsel and control owners.

   "OT compliance alignment," mentioned in the project's subject line, is treated as a
   descriptive theme, not a sixth framework — there is no separate "OT compliance
   alignment" standard being mapped. Flag if this reading is wrong.

7. **No claim of TSA, NIST, ISA, IEC, or CIS endorsement.** This is an independent
   researcher's crosswalk for reference and documentation support, not an official or
   government-published mapping, and is not intended to replace any operator's own
   compliance review with counsel or with TSA/CISA directly.
