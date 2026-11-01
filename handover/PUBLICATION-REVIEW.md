# Public release scope and exclusions

On **1 November 2026**, the repository owner explicitly authorized creation and publication of the separate public **Flight-Controller-V2-Handover** repository containing sanitized guides and reviewed engineering files. This record supersedes the earlier local-only compilation hold **for this selected edition**. It does not authorize publication of the entire private archive or certify another department's work.

## Included allowlist

- Consolidated root guides, fourteen technical chapters, issue register, ownership, equipment, chronology and blank acceptance/custody forms.
- Eleven original numeric parameter exports, their hashes and complete comparisons. These retain device-specific calibration and sensor identifiers; no home-position coordinates, Wi-Fi credentials or signing keys were found in these exports.
- The 481-file already-public V2 design tree pinned to commit `56c91e283b9ce56b6e43480734feb60e2f078760`, including its original notices and coherent hardware/firmware/manufacturing references.
- Sanitized evidence descriptions, firmware identity hashes, relative-path provenance, an integrity manifest and a portable read-only verifier.

The exact published payload is enumerated in [the hash manifest](../inventory/package-sha256.csv). Validation outputs excluded from that manifest to avoid self-reference are explicitly listed in [validation](../inventory/VALIDATION.md).

## Excluded material

| Exclusion | Reason and custody |
|---|---|
| Nine raw screen/physical recordings and all desktop screenshots | Private desktop/chat context and unsafe historical arrangements; held in the private evidence package |
| Old chat exports, earlier private guides and generated illustrative wiring images | Private context, absolute paths and superseded/conditional instructions |
| Original EVT1, PCBWay and JLC private project packages | Not treated as newly approved public engineering disclosure; public V2 variants remain distinct |
| Original SALFCGAMUDA binaries/source package | Identity/hashes retained, files held privately; public FCV2 rebuild is not a byte-identical substitute |
| Workstation discovery/copy manifests and protected-checkout records | Absolute paths and private source metadata; replaced by relative public provenance |
| Pi OS disk images, account/network credentials, keys, tokens and supplier correspondence | Not required for public takeover instructions; no private image or credentials bundled |

The public reference snapshot contains two existing PCB render PNGs and engineering PDFs from the V2 repository. These are public design documentation, not the excluded raw drone test media. Their inherited authorship and license boundaries remain applicable.

## Checks and remaining limits

The candidate was assembled separately from an explicit allowlist. Automated checks inspect all included files for private workstation-path and credential patterns, parse parameter exports, verify included firmware payload identity, check authored relative links and compare all 481 public reference blobs with the pinned source. The validator reports its exact scope and exceptions; it is not a guarantee that arbitrary future additions are safe to publish.

The reference snapshot is preserved without semantic edits. During preparation, 190 copied Windows text files were restored to their exact pinned Git blob line endings. All 481 distributed reference files then matched the source blobs exactly. The verifier also permits CRLF/LF equivalence for the source comparison, while the release manifest hashes exact distributed bytes. Use the documented clone command or ZIP to avoid checkout line-ending conversion. Historical source-local links or commands within the preserved design archive may require that archive's original context.

The incoming technical lead, subsystem owners and physical custodian still need to complete the blank hardware acceptance forms. No company endorsement, departmental sign-off, flight approval or repair of an open hardware fault is implied by publication. Future private material must undergo a separate disclosure/license review before addition.

See [source notices](../THIRD_PARTY_NOTICES.md), [evidence limits](../evidence/README.md) and [open issues](OPEN-ISSUES.md).
