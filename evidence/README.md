# Evidence catalog and confidence limits

This public catalog summarizes privately retained source evidence. **The clips, extracted frames and desktop screenshots are not distributed here.** They include private context and, in one physical clip, an unsafe historical test with propellers fitted. The current procedures require every propeller removed for bench work.

The preparation combined earlier automated frame scans, selected visual reviews, parameter files and the outgoing contributor's reports. It did **not** newly inspect every frame of every recording. Automated image classification is not a MAVLink log; software output values are not measured RPM.

## Private recording register

The IDs below let the custodian locate the originals without publishing desktop paths or raw media. Durations are approximate unless stated from container metadata.

| ID / session | Length | Established content | Limit |
|---|---:|---|---|
| E01 · 16 October early FC | 12m32.67s | Programming/startup workflow, original target banner and early calibration/RC/compass warnings | Six sparse overview frames; not complete programming verification |
| E02 · 16 October calibration | 20m40s | Sensor/calibration work; explicit accelerometer success identified near 15m50s in prior review | Physical installed-axis and long-term sensor acceptance remain open |
| E03 · 19 October receiver | 25m48s | Receiver inputs/calibration; final prompt captured throttle above minimum | Superseded by later corrected endpoints |
| E04 · 21 October early screen | 4m43s | Software ARMED intervals and later gyro warning | Prior automated scan decoded 5,235 frames with selected review; not complete IMU closure |
| E05 · 21 October physical rotation | 18s | Actual motor/propeller rotation | Prior scan decoded 1,047 frames; two props fitted; not an approved test or complete motor map |
| E06 · 21 October post-incident screen | 23.25s | DISARMED and throttle-too-high context | Prior scan 471 frames; reported flip itself not recorded |
| E07 · 21 October calibration correction | 4m24s | Intermediate narrow roll range and high throttle trim | Prior scan 3,035 frames; later corrected, not final baseline |
| E08 · 21 October short arm test | 39s | Four ARMED intervals, low throttle/output telemetry | Prior label comparison 778 frames; screen-only, no synchronized physical throttle response |
| E09 · 21 October afternoon controls | 50m50.29s | Final stick-control discussion, Mission Planner and contributor's working-controls report | Eight sparse overview frames; not a Pi power repair or complete propulsion test |

[Additional sparse-review details](OVERVIEW-REVIEW.md) identify sampling limits for E01 and E09. The private package retains original hashes, file-to-ID correspondence and prior analyses. Ask the project custodian for private access rather than treating this catalog as independent downloadable evidence.

## What supports each claim

| Claim | Supporting record | Not established |
|---|---|---|
| Last intended configuration | [Latest original export](../config/historical-fc2-snapshots/FC2_stick_control_working_2026-10-21.param) | Live hardware state at transfer |
| Accelerometer calibration saved | Exports and private success/startup screens | Installed axes or repeated-start sensor consistency |
| Receiver data reaches FC | Calibration/status sessions and saved RC settings | Full physical direction mapping, range or airborne failsafe acceptance |
| Arm requests accepted | Private HUD transitions | Flight clearance or motor-output electrical integrity |
| Motor rotation | E05 and contributor report | All four positions/directions, variable-throttle response, thrust or power rating |
| Final stick arm/disarm works | Contributor report, final RC6/rudder settings and E09 context | New independent measured acceptance |
| Bare Pi boots from USB-C | Contributor confirmation | BEC output quality or full peripheral operation |

Five referenced original photographs were missing from their former locations during private compilation. Recover them or take new versioned photographs. A chat reference does not recover missing image bytes. The existing public V2 PCB renders are design illustrations, not proof of this aircraft's wiring or flight.

## Record new tests

Before a session, record article ID, operator, time/timezone, firmware/configuration hashes, wiring/power state and procedure. Keep physical movements and live telemetry in one synchronized view where relevant. Save original logs/clips privately, identify exact useful intervals and retain failures as well as successes. Publish only a separately reviewed sanitized result summary, then update the [acceptance form](../handover/ACCEPTANCE.md) and [issue register](../handover/OPEN-ISSUES.md).
