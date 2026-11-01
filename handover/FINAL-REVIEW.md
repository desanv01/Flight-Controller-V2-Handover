# Final coverage and newcomer review

Reviewed **2 November 2026** against the available FC engineering records, all eleven original parameter exports, prior private recording analyses, the nine-session evidence catalog and the pinned public V2 design. The review checks whether the handover preserves the outgoing FC work and the final drone bench state, and whether an incoming reader can locate the next procedure.

**The available FC work and final-test outcomes are covered.** The review corrected the public/private inventory wording, added a beginner route and private-transfer checklist, and made several interface/control details explicit. Missing physical acceptance, original photos and departmental deliverables remain named gaps; they have not been replaced with guessed results.

## Coverage of the FC work

| Work or decision | Where the incoming team finds it | State preserved |
|---|---|---|
| Architecture, FC2 versus V2, FC versus Pi/receiver/ESC roles | [Foundations](../docs/01-foundations.md), [hardware](../docs/02-hardware-identification.md) | A custom STM32H743 FC, not a generic Pixhawk; FC1 fault remains separate |
| MCU resources, clock, sensors, pinout, schematic/PCB and manufacturing variants | [Wiring](../docs/03-wiring-and-power.md), [public design source](../references/README.md) | Full 481-file reference, coherent variant boundaries and 8 MHz HSE-bypass target |
| POWER1, Nano-Fit cable, external regulation and SWD | [Wiring/power](../docs/03-wiring-and-power.md), [recovery](../docs/12-firmware-and-recovery.md) | FC USB is data-only; J12 is regulated input; J3 reference is not power input |
| Original programming/build identity and public rebuild | [Firmware identities](../firmware/README.md), [recovery/build](../docs/12-firmware-and-recovery.md) | Distinct binary hashes, pinned upstream, local unreserved ID and correct boot/application addresses; original files require private transfer |
| Mission Planner startup, backup, messages and current-state interpretation | [Beginner route](BEGINNER-WALKTHROUGH.md), [Mission Planner](../docs/04-mission-planner.md) | Fresh telemetry and saved live read-back required; old screens/counters are not flight proof |
| Dual-IMU/barometer checks, accelerometer calibration and attitude fixes | [Sensors](../docs/05-sensors-and-orientation.md), [issue register](OPEN-ISSUES.md) | Calibration success and later consistency warnings both retained; no false fault closure |
| Receiver identification, CRSF/420000 correction and FC serial options | [Receiver](../docs/06-receiver.md) | CYCLONE marking versus BETAFPV installed target; firmware 3.5.6; J7/SERIAL2; `RC_OPTIONS=8224`, baud parameter distinction |
| Full radio history and corrected endpoints | [Snapshot catalog/comparisons](../config/README.md), [controls](../docs/07-controls-and-calibration.md) | Eleven originals, 945-entry final state, corrected low-throttle calibration and historical bad captures distinguished |
| Momentary shoulder control and final stick-control arrangement | [Controls](../docs/07-controls-and-calibration.md), [chronology](CHRONOLOGY.md) | Final `RC6_OPTION=0`, `ARMING_RUDDER=2`, CH1–CH4 auxiliary options zero; old 154/153 instructions superseded |
| DShot300 and FC-to-ESC integration | [ESC/motors](../docs/08-esc-and-motors.md) | Reported OPENESC_30_F421; signal-only J6, common TIM1 group, output permutation and no PWM endpoint calibration |
| Physical rotation, arm transitions, calibration recovery and reported flip | [Evidence catalog](../evidence/README.md), [status](../CURRENT-STATUS.md), [issues](OPEN-ISSUES.md) | Recorded rotation and reported working controls preserved; no claim that all four directions, synchronized throttle response or flight were accepted |
| Missing GPS/compass and battery monitoring | [Navigation/monitoring](../docs/11-gps-and-compass.md) | No installed module; bench-only estimator profile; J4/SERIAL6; battery monitor disabled; no qualified return-home |
| Pi BEC fault and camera/HAT/SATEL discussions | [Pi system](../docs/09-pi-camera-lidar.md) | USB-C boot confirmation, physical pins 4/14, shared BEC capacity, unresolved loaded voltage and exact SATEL variant |
| Planned FC-to-Pi interface | [MAVLink](../docs/10-fc-pi-mavlink.md) | USB-first telemetry option, conditional J11/SERIAL7 UART, disabled saved port and no accepted companion control |
| Responsibilities, original assets and safe continuation | [Ownership](OWNERSHIP.md), [custody](CUSTODY.md), [acceptance](ACCEPTANCE.md), [gates](../docs/14-continuation-plan.md) | Incoming named assignments and physical sign-off still required |

## Check of the final bench state

The [original final export](../config/historical-fc2-snapshots/FC2_stick_control_working_2026-10-21.param) remains unchanged at SHA256 `0a2d585fbae65b96a086eed1f243a6e54256b0ca37b165a8d4b3d08ad1ad9ee3`. The numerical verifier checks its full analysis/comparisons and critical settings. In particular, the handover preserves:

- Receiver SERIAL2/CRSF and ELRS bitmask rather than a guessed FC UART baud change.
- The final stick-arming arrangement rather than momentary RC6 arming.
- Quad X / Stabilize bench mode, DShot300, no ESC endpoint calibration and output order **Motor2 / Motor3 / Motor4 / Motor1**.
- Both IMUs configured; compass/yaw bench settings, disabled battery monitor and disabled companion UART identified as limitations.
- Radio-loss settings and counters recorded without claiming accepted return-home or actual flight.

The final-test evidence distinguishes original footage, earlier automated scans, selected manual reviews and contributor reports. The additional two overview reviews remain sparse. This final documentation audit does not claim a new every-frame video review or a new hardware test.

## Newcomer route checked

The [beginner walkthrough](BEGINNER-WALKTHROUGH.md) now gives a continuous path from GitHub ZIP download and Mission Planner installation through Device Manager, connection, HUD/messages, first parameter backup, a non-writing numerical comparison, session evidence and safe shutdown. It then routes the reader to FC, receiver, isolated control and gated propulsion procedures in order.

The steps were checked as a documentation walkthrough and the software helpers were exercised locally and through CI. No incoming team member has been observed completing a usability trial, and no hardware was connected for this review. A new reader can prepare the files/software and understand the sequence; powered electrical/propulsion work still needs the competent lead specified in the procedures.

## Items that remain to be received or measured

- Original deployed-build files and actual as-built/vendor records are **privately retained**, not missing from the selection by accident. Receive them using [custody](CUSTODY.md); the public neutral rebuild is not an identical replacement.
- Five original photos were unavailable at their former locations; recover or replace them with current photographs.
- Exact ESC firmware/configuration, assembled voltage/capacitor approval, motor identifiers and the four physical motor checks still need the responsible team.
- Post-impact inspection, repeated sensor acceptance, battery sensing and failsafe closure remain open.
- Final transmitter exports, complete Pi OS/application/driver assets, loaded BEC diagnosis and combined perception/telemetry acceptance remain unestablished.

These gaps are the work queue in [H01–H18](OPEN-ISSUES.md), not completed tasks hidden by a successful repository check. The public/private boundary, unmodified snapshots and pinned design must be preserved in future updates.
