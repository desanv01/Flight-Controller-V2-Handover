# Source ownership and license boundaries

This repository combines handover documentation, device-specific configuration records and a preserved public engineering reference. **No blanket license is asserted over the entire compilation.** New handover prose and original configuration records have no additional open-source license grant in this release; public availability alone does not relicense them. Obtain the owner's permission for uses requiring a grant beyond applicable law. This does not restrict rights already granted by licenses attached to the included upstream materials.

## Public hardware reference

The copied V2 hardware retains its [CERN-OHL-S-2.0 license](references/v2-design/LICENSE) and [third-party notices](references/v2-design/THIRD_PARTY_NOTICES.md). Preserve upstream hardware authorship and the distinction between upstream design, Desan Vasu's adaptation/integration work, and external fabrication. The source lineage and original contributor credits remain in the copied notices.

Project-local KiCad libraries include KiCad-derived symbols, footprints and models under the [KiCad library license and exception](https://www.kicad.org/libraries/license/). Manufacturer-derived geometry and data retain applicable notices. The hardware license must not be interpreted as a new blanket license for every library or model.

## Firmware and software

ArduPilot source and firmware are governed by GPL-3.0 and their corresponding-source obligations. ChibiOS, STM32 code and other dependencies retain their respective notices. The neutral build's [manifest](references/v2-design/firmware/build/manifest.json), [build instructions](references/v2-design/firmware/README.md), target inputs and pinned upstream source identify how it was produced. The source tree and build dependencies must be obtained as described; this handover is not a complete compiler/container image.

Firmware binary availability is not permission to ignore the applicable license or substitute a mismatched image on the physical FC. The original deployed-image identity is not proven byte-for-byte and the private original build is excluded; see [firmware identity](firmware/README.md).

Existing engineering scripts retain any source headers and their applicable upstream terms. No new blanket software license is invented for unlicensed historical scripts or new verification code in this compilation.

## Documentation and attribution

Manufacturer documents are referenced by official links unless already present in the reviewed public design snapshot. Do not add third-party manuals, media, models or datasets merely because a URL is available. Preserve notices and verify redistribution rights for later additions.

The handover records Desan Vasu's FC work and integration interfaces. ESC/Pi departmental work is identified as reported or outstanding where appropriate. It does not claim authorship of all subsystems, physical testing by upstream authors, or certification/endorsement by GAMUDA. Private recordings and original non-public engineering packages remain excluded under the [release scope](handover/PUBLICATION-REVIEW.md).
