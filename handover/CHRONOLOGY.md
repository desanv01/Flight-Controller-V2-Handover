# Development and commissioning chronology

Dates below describe technical records and reported sessions, not employment dates. A filename date, filesystem modification time, source publication date and test event date may differ.

| Period | Event | Handover interpretation |
|---|---|---|
| 26 August to September 2026 | Research, interface selection, MCU resources, schematic/PCB and correction stages | Historical engineering rationale retained in the V2 archive, not current assembly instructions |
| September 2026 | External-regulated-power, Nano-Fit and signal-only ESC EVT1 packages; separate vendor variants | Keep source/manufacturing sets coherent; supplier/as-built identity still requires inspection |
| 13 September build record | Original SALFCGAMUDA Copter 4.7.1 bootloader/application and source patches | Original project firmware associated with the later reported banner |
| 5–6 October | Bring-up, power, programming and Pi integration guides/illustrations | Earlier plans include assumptions and conditional wiring; consolidated handover supersedes conflicting instructions |
| 14 October | Public neutral FCV2 engineering publication/rebuild and source checks | Compilation/EDA evidence, not physical qualification |
| 17 October | Latest identified public README change | Pinned remote commit 56c91e2; original local publication checkout stays at its earlier HEAD |
| 16 October sessions | FC2 startup, live sensor evidence, accelerometer success and saved calibration | Useful bench baseline; physical orientation and later consistency still need qualification |
| 16–19 October receiver work | Receiver Web UI identity, CRSF/baud corrections, SERIAL2 options, live inputs and calibration | Some files retain 16 October names despite later session use |
| 19 October | Receiver recheck and FC-to-ESC handoff | Interface/protocol description, not completed motor acceptance |
| 20 October | Drone wiring photos and no-GPS/compass bench setup; arming warnings | Images are not proof of exact harness or voltage ratings |
| 21 October early tests | Corrected attitude/calibration, accepted arming and actual rotation | Physical footage included two fitted props; preserve as unsafe historical evidence |
| 21 October incident | User reported unintended flip during joystick testing | Flip itself not recorded; require post-impact inspection and do not claim its cause established |
| 21 October recovery | Throttle-high/narrow-roll captures corrected; later radio_corrected export | Final calibration differs materially from intermediate files |
| 21 October final control arrangement | RC6 confirmed momentary; disabled, stick arming/disarming retained; user reported working | Final identified snapshot is stick_control_working, not the earlier shoulder-button profile |
| Latest Pi discussion | Bare Pi USB-C boot confirmed; battery/BEC red/no-boot issue unresolved | No measured loaded BEC diagnosis or full peripheral acceptance provided |
| 1 November handover preparation | Outgoing contributor confirmed the left-behind project remains at bench development; local compilation authorized | No new hardware test, repository creation, publishing or V2 source mutation |

## Superseded instructions that must not reappear as current steps

- RC6 option 154 with AirMode, then 153 normal arm/disarm, were intermediate states. Final RC6 is 0; rudder arming/disarming is 2.
- Calibration summaries with roll 1468–1534 or high throttle trim were corrected. Do not restore them.
- Initial firmware defaults assign sequential motors. Final saved outputs are Motor2/Motor3/Motor4/Motor1. Neither establishes the physical wiring without tests.
- Generic GPS SERIAL3 and companion SERIAL2 examples are not this board's mapping. J4 is SERIAL6; J11 is SERIAL7; receiver remains SERIAL2.
- Older MicroClasp/power-path/eFuse depictions and CM5/custom-sensor proposals do not identify the final received hardware.
- Suggested faster/bidirectional DShot progressions are not required to repeat the known ordinary DShot300 baseline.

Raw earlier guides remain in the private engineering archive and are excluded from this public release. Their assertions and old absolute links are history, not current results. The numbered guides here are the consolidated continuation procedures.
