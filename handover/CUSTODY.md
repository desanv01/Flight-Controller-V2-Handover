# Physical and digital custody transfer

Use this form when the incoming team receives the project. It does not assert that a physical transfer or hardware inspection occurred during compilation.

## People and scope

- Outgoing contributor: Desan Vasu, FC and interfaces documented in this package.
- Incoming accountable lead: **to be assigned**.
- Transfer date, local time and site: **to be recorded**.
- Technical reviewer / observer: **to be assigned**.
- This sanitized public release: authorized by the outgoing repository owner on 1 November 2026. Additional departmental/private disclosures require their own review.

## Physical receipt

List each asset from [equipment](EQUIPMENT.md), quantity, model/revision/serial where appropriate, condition, accessories, photographs, new custodian and storage location. Separate FC1 with its unresolved fault from FC2. Record battery condition and safe storage/charging responsibility. Confirm props removed and the received power/harness configuration before reassembly.

## Digital receipt

1. Preserve an unchanged copy of this package and its [hash manifest](../inventory/package-sha256.csv).
2. Acknowledge that the last identified saved configuration is from 21 October, not a fresh physical read-back.
3. Acknowledge the original SALFCGAMUDA versus public FCV2 artifact distinction and the local unreserved board ID.
4. Receive licenses/source provenance, parameter exports and the issue register from this repository. Arrange separate private receipt of original recordings and excluded project artifacts; they are not included here. Do not move private evidence into this public repository.
5. Transfer Pi OS/code, transmitter exports and any credentials through an approved private channel. This package contains no asserted complete accepted Pi application image.
6. Record missing items/photos/logs and the person responsible for recovering each.
7. Have the incoming lead demonstrate locating the correct guide, latest snapshot, wiring table and stopping conditions before energizing hardware.

## Private digital material to request

The public repository and the private evidence package are separate deliveries. The incoming custodian should record receipt or a named recovery owner for each item below. Do not assume a GitHub ZIP includes them.

| Material | Required identification or contents | Why it matters |
|---|---|---|
| Original EVT1 firmware set | Original APJ, application BIN, matching bootloader, manifest, board overlay, patches and build logs; compare identities in the [firmware guide](../docs/12-firmware-and-recovery.md) | Recovery of the original build without substituting the neutral public image |
| Original manufacturing/vendor variants | Matched source, BOM, placement, Gerbers and assembly records, with actual supplier/revision | Establish which set produced the received board |
| Private test evidence | Nine originals identified by E01–E09 in the [catalog](../evidence/README.md), hashes, extracted-frame/analysis records and available telemetry logs | Revisit exact events without upgrading a reported/sampled result to acceptance |
| Original photographs | Recover the five missing originals or take dated replacements showing the current article, harnesses and nose | Close as-built wiring and post-impact inspection gaps |
| Radio assets | Actual T8L handset/RF versions, configuration export and binding custody | Preserve the working transmitter/receiver pair |
| Pi assets | Actual OS/storage backup, application repository/commit, dependencies, service definitions, HAT model/runtime and sensor driver/configuration | Resume software work from its actual state rather than an invented complete image |

Keep credentials and private hardware/account identifiers in the approved private transfer channel. The full local compilation is a separate retained archive; cleaning temporary publication checkouts must not delete it. Missing physical or digital items remain open under the [issue register](OPEN-ISSUES.md).

## Acceptance of custody, not flight approval

Outgoing acknowledgement: name / date / signature **pending**.

Incoming receipt acknowledgement: name / date / signature **pending**.

Technical limitations accepted and issue owners assigned: name / date / signature **pending**.

Custody acceptance confirms receipt and understanding of limitations. It does not accept the aircraft for flight or close unresolved engineering issues.
