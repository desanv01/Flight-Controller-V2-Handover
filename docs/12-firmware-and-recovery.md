# Firmware identity build provenance and recovery

**Do not reflash a working FC as the first takeover action.** Read its identity and preserve parameters. Reprogramming is a separately approved repair/reproduction task and can erase the application and calibration.

## Two distinct builds must be distinguished

| Item | Original project EVT1 build | Public neutral rebuild |
|---|---|---|
| Board directory / banner | SALFCGAMUDA | FCV2 |
| Upstream | Copter-4.7.1 | Copter-4.7.1 |
| Source SHA | dbe792162d06cab66c3475fd5556bf7a120f119e | Same pinned upstream SHA |
| Local board ID | 1241, not upstream-reserved | 1241, not upstream-reserved |
| Build record date | 13 September 2026 | 14 October 2026 |
| Relation to tests | Recorded running banner agrees with original target/version | Successful build, not demonstrated as the deployed bench binary |
| Distribution here | Identity and hashes only; original files retained privately | [Public firmware and source inputs](../references/v2-design/firmware/README.md) |

Both sets of local firmware files were rehashed during private compilation; only the already-public neutral rebuild is distributed here. They are different binaries; the shared upstream commit does not imply byte identity. No flash-memory read-back comparison was performed. Do not mix bootloaders and applications across builds just because the numeric board ID matches.

## Artifact identity

| Build / file | Bytes | SHA256 |
|---|---:|---|
| Original arducopter.apj | 1,247,475 | `23003d8c1bb64ac21be54da0a38e12a1b2687273e8f5773e48ff179bebf2d759` |
| Original arducopter.bin | 1,400,648 | `6fb863c9490f6d8771ca4cdc60e4ef7fc75cf77c741fc14ecccb071cae355054` |
| Original SALFCGAMUDA_bl.bin | 18,828 | `e20cc7e59ceb5503762b148c63981b79c15b8ef01f42494a9792c8854efcf8b8` |
| Public arducopter.apj | 1,247,376 | `cb32ec56d200029e046464a39302d651689243f6b6a69d49a4e90cfb4f9ff98d` |
| Public arducopter.bin | 1,400,584 | `c62187cb03442fe1764abc4a585ccedc7912fa0daff56034434b9b1fa0503673` |
| Public FCV2_bl.bin | 18,796 | `5915b12bc9f6ca9a31f835ea87a026e5bf8ad24668ae438ff954d583dc2fb68d` |

APJ is a packaged application image. Its package-format `version` is not the ArduCopter flight-firmware version. BIN is the raw application, not a bootloader. Parameter `.param` files are neither.

## Reproduce in a separate clean build directory

The source record uses `ardupilot/ardupilot-dev-chibios:v0.2.0`, digest `sha256:8bb0f850fb3fe1c170cb12dd577ab64f3708be8a828f9eafd28d73559766e81f`, GNU Arm Embedded 10.2.1 and upstream waf. Network/upstream dependencies and licenses remain necessary; this package is not a complete compiler/container image.

For the public build, inspect [build.sh](../references/v2-design/firmware/build/build.sh) and [manifest](../references/v2-design/firmware/build/manifest.json). Run it only in a new disposable build area under engineering change control: it clones upstream, checks out the pinned SHA, initializes submodules, installs the FCV2 board definition/local ID, builds the bootloader, copies that bootloader to the expected upstream path, then builds Copter. Do not run it inside the preserved repository or assume its local numeric ID is globally accepted.

For the original build, obtain its manifest, matching `board/` files, source patches and full build logs from the private project custodian. Those original assets are excluded from this public repository; their absence must not be bridged by guessing that the public rebuild is identical. The source patch and board overlay are related inputs; choose a reviewed application method in a clean upstream checkout and use a patch applicability check before applying it. Do not apply overlapping board additions twice. The original record notes a packaging CRLF/shebang correction; preserve that detail instead of substituting a legacy binary.

Record the actual image digest, compiler versions, source/submodule SHAs, local patches, commands, logs and output hashes for every rebuild. Successful compilation alone does not accept runtime compatibility.

## Recovery decision

Before any write, the lead must document: why recovery is required, physical board identity, matching source/build, current backups, intended erase/write scope, rollback artifact and post-write acceptance. Remove props, isolate ESC/receiver/Pi as appropriate, use proven regulated POWER1, and never power the FC from ST-Link's reference lead.

### First bootloader installation or an approved damaged-bootloader repair

1. Identify the actual ST-Link adapter pinout. J3 is target 3.3 V reference, SWDIO, SWCLK and ground; adapter numbering varies. Verify from the probe's manual.
2. Power the target independently. Connect STM32CubeProgrammer over SWD conservatively, confirm target voltage, STM32H743 identity and flash layout **before** writing.
3. Preserve readable existing firmware and parameters if valuable/available. Full flash erase is destructive and is not a routine diagnostic step.
4. If an erase/write is explicitly approved, program the **matching bootloader** at `0x08000000`, verify it, save the programming log and reset.
5. Remove debug wiring for normal operation. Keep POWER1 powered for USB enumeration.

### Matching application through the bootloader

Use Mission Planner's custom-firmware workflow and the matching APJ. Save successful completion and the new banner. The targets reserve 128 KiB before the application; raw application address is `0x08020000`, not the bootloader address. Do not write the application BIN at `0x08000000`.

After programming, perform FC-only power/sensor/orientation/receiver acceptance again. A replacement board requires its own calibration; the old complete FC2 dump is not an automatic restore. Initial defaults use sequential Motor1–Motor4, while the final bench profile uses a permutation. Review that difference before any ESC connection.

The earlier guide's suggested progression through PWM/faster/bidirectional DShot is historical, not required now. Preserve the known DShot300 baseline; waveform/telemetry improvements need their own approval. Firmware flashing is not carried out by this package.
