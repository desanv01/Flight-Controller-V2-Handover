# Firmware distribution and identity

The recorded FC2 banner is **SALFCGAMUDA / ArduCopter 4.7.1**. The bundled public neutral rebuild is **FCV2 / ArduCopter 4.7.1**. They share a pinned upstream revision and local numeric board ID but have **different binary hashes**. No flash read-back establishes which exact bytes are currently deployed.

Only the already-public neutral rebuild is distributed here:

- [Public firmware, target definitions and source/build instructions](../references/v2-design/firmware/README.md).
- [Public build manifest](../references/v2-design/firmware/build/manifest.json).
- [Artifact hashes and APJ/BIN identity records](artifact-identities.json). Original private artifact entries are identity records only, not downloadable files.
- [Detailed identity and recovery guide](../docs/12-firmware-and-recovery.md).

The original EVT1 binaries, board overlay, patches, manifest and logs remain in the private project archive. Obtain them as a coherent set through the custodian if recovery of the original build is required. Do not rebrand the neutral image as the tested original or flash it merely to match the public repository name.

The local board ID **1241 is not upstream-reserved**. A matching numeric ID alone does not establish hardware compatibility. The application BIN belongs after the reserved bootloader region, not at the bootloader start address. Read the recovery guide before any programming operation.

The public verifier decodes the included APJ and compares it with the accompanying BIN. This checks packaged file consistency, not device flash, runtime safety or flight acceptance. Historical HAL/Betaflight/iNAV experiments in the source reference are not accepted replacement targets. No firmware is written by this repository's verification tool or CI.
