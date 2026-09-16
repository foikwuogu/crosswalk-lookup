# Next steps (post-v0.1)

- Have the author do a final domain-judgment check on the outcome-to-control *assignment*
  in the 12 `author-mapped` cells (IEC 62443 and CIS Controls v8 columns, all 6 outcomes).
  Every ID/title in those cells has been independently re-confirmed as of 2026-09-16 — what's
  left is confirming these are the *right* controls, not whether the IDs exist.
- The Governance & Risk Management outcome's CIS Controls v8 mapping (Safeguards 14.1, 14.9)
  is flagged as a weaker fit than the project's other CIS mappings — CIS Controls v8 predates
  NIST CSF 2.0's Govern function and has no direct governance/accountable-executive
  equivalent. Worth a second look before publishing, or noting explicitly as a known gap.
- Confirm with the author whether this project and "TSA Pipeline Policy-to-Control
  Crosswalk" should share one AUTHORS.json, or stay two separate author lists on two
  related projects.
- Re-fetch and directly quote-check the four outcome summaries against
  `tsa-security-directive-pipeline-2021-02f-and-memo-508c.pdf` once reachable.
- Add a search/filter box and a "copy citation for this cell" button to the lookup UI.
- Consider an export-to-CSV / export-to-PDF button for auditors building CIP/CIRP/CAP
  documentation packages directly from the tool.
- After verification: publish the repository to GitHub (`scripts/publish_github.py`
  equivalent) and deposit a Zenodo release for a DOI.
