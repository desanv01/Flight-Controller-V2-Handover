# Open issue and acceptance register

Status at compilation on **1 November 2026**. Role names below are proposed incoming owners, not named personnel assignments. A “working” filename, an old success message or a later arm transition does not close a different issue. Add actual owners and dates during takeover.

| ID | Priority | Issue and recorded state | Closure evidence required | Incoming owner |
|---|---|---|---|---|
| H01 | Stop before hardware testing | Received assembly/custody and exact supplier/revision are not newly inspected | Asset list, both-face photos, revision/substitution reconciliation, signed intake | Technical lead |
| H02 | Stop before propulsion | ESC target OPENESC_30_F421 and DShot300 reported; exact firmware/version and assembled 25.2 V/transient/capacitor rating not accepted | ESC schematic/revision, configuration export, ratings/protection review and test-supply approval | ESC and electrical leads |
| H03 | Stop before propulsion | Non-default output permutation saved; all four actual motor positions/directions not accepted | Marked nose, harness continuity, separate A/B/C/D observations and before/after config | FC and ESC leads |
| H04 | Stop before propulsion | Gyro/accel inconsistency and orientation history; calibration later succeeded | Repeated stationary startups, physically verified axes, both IMU logs/health, cause/disposition of fresh warnings | FC lead |
| H05 | Stop before propulsion | Reported unintended flip; physical footage earlier had props fitted | Post-impact mechanical/electrical inspection and correction; supervised no-prop procedure | Mechanical/test lead |
| H06 | Stop before flight | Battery monitor disabled; no qualified battery protection | Selected sensing hardware, wiring review, instrument calibration, low/critical action tests | Electrical and FC leads |
| H07 | Stop before flight | RC-loss/recovery and appropriate final action not completely accepted | Propulsion-isolated loss/recovery logs, reviewed no-GPS/available-navigation action, pilot recovery procedure | FC/radio lead |
| H08 | Required before repeating powered manual test | RC6 momentary and disabled in final profile; throttle mechanics/directions need incoming verification | Physical CH1–CH4 sweep, low throttle, stick arm/disarm recording, mechanical throttle decision | Radio/test lead |
| H09 | Required before Pi integration | Pi boots on USB-C; BEC attempt fails; no loaded voltage result | Bare-Pi BEC startup measurements, harness/contact review, progressive load and thermal tests | Pi and electrical leads |
| H10 | Stop before energizing LiDAR harness | Actual SATEL supply variant/bridges and complete wiring not signed off | Clear board photos, exact variant schematic match, signed pin/voltage/pull-network table | Sensor/electrical leads |
| H11 | Required for perception | Camera/HAT/LiDAR combined operation and software baseline unaccepted | OS/app/dependency records, valid timestamped sensor/inference outputs, workload/failure tests | Pi lead |
| H12 | Planned link, not a fault in the receiver | J11 is SERIAL7, disabled in latest snapshot; companion exchange not accepted | Approved independent power, correct UART or USB route, heartbeat/logs and reconnect/loss tests | FC and Pi leads |
| H13 | Required for navigation-capable modes | No GNSS/compass installed and no alternative localization qualified | Architecture decision, compatible sensor installation, detection/calibration/performance evidence | Navigation lead |
| H14 | Documentation recovery | Five referenced original photo paths missing; exact as-built wiring images incomplete | Recover originals or take new versioned photos; preserve provenance | Documentation/technical lead |
| H15 | Scoped publication completed for this release | User authorized a separate sanitized public handover; raw evidence and original private engineering packages remain excluded | Preserve the [release scope](PUBLICATION-REVIEW.md); review any additional disclosure separately | Project owner |
| H16 | Quarantine | Earlier FC1 INS/heating fault | Clearly separated labelled board; repair/qualification record before reuse | Hardware lead |
| H17 | Detailed evidence review remains | Afternoon recording sparsely sampled: final-control discussion/Mission Planner, not a Pi test; no complete motor/throttle acceptance established | Review relevant continuous intervals and privacy before stronger claims; retain sparse-review limits | Documentation/FC lead |
| H18 | Reproduction limitation | Original deployed-image identity not proven byte-for-byte; public rebuild differs; board ID local | Preserve matching artifacts/source, exact live banner, approved recovery selection and own post-flash acceptance | Firmware lead |

## How to close an issue

1. Assign an accountable person and define a bounded test and pass/stop criteria.
2. Record exact article/firmware/parameters, power/harness state, date and instruments.
3. Perform only the approved isolated/gated procedure. Save raw results and failed attempts.
4. Link the evidence and state whether the result is measured, visually recorded or reported.
5. Have a competent reviewer accept the result and note residual limits. Do not mark a future instruction as a completed test.
6. Update [current status](../CURRENT-STATUS.md) through a dated change record. Keep the original snapshots immutable.

Documentation validation does not close hardware acceptance issues. H15 records this release's limited publication scope; H01–H14 and H16–H18 remain open until their required evidence is accepted.
