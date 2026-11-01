# Bench acceptance records

These forms are **blank for the incoming team**. No hardware test is marked passed by document preparation. Complete a separate record for each physical article and configuration. A competent reviewer must sign the relevant gate before progressing.

## Session header

| Field | Enter actual result |
|---|---|
| Session ID / date / local time / timezone | Not recorded yet |
| Operator / observer / reviewer | Assign names |
| Article IDs / board revisions / frame nose | Inspect and record |
| FC firmware banner / artifact relation | Record, do not infer byte identity |
| Before parameter filename and SHA256 | Save live read-back |
| Wiring revision / disconnected branches | Photograph and describe |
| Source supply / voltage / protection | Identify and approve |
| Instruments / calibration status | Record |
| Propeller count physically removed | Must be all four for this package's bench procedures |
| Procedure and entry/stop criteria | Reference numbered guide and approval |

## FC only measurements

| Check | Measured or observed result | Evidence | Pass / fail / hold |
|---|---|---|---|
| Unpowered harness polarity/continuity and no unintended shorts | Pending | Pending | HOLD |
| POWER1 voltage at pads before/startup/steady load | Pending | Pending | HOLD |
| FC supply current and rail measurements | Pending | Pending | HOLD |
| Temperatures at comparable elapsed times | Pending | Pending | HOLD |
| No unexpected reset/disconnect | Pending | Pending | HOLD |
| Both IMUs and barometer identified/live | Pending | Pending | HOLD |
| Level, nose-up and right-bank axis response | Pending | Pending | HOLD |
| Calibration persistence across deliberate starts | Pending | Pending | HOLD |
| Fresh inconsistency warnings investigated | Pending | Pending | HOLD |
| Downloaded diagnostic log with both IMUs | Pending | Pending | HOLD |

## Receiver and control checks with propulsion isolated

| Check | Actual result / endpoints / state | Evidence | Result |
|---|---|---|---|
| Physical CH1 roll direction/full span | Pending | Pending | HOLD |
| Physical CH2 pitch direction/full span | Pending | Pending | HOLD |
| Physical CH3 throttle low/full span/mechanics | Pending | Pending | HOLD |
| Physical CH4 yaw direction/full span | Pending | Pending | HOLD |
| RC6 unused, stick arm then disarm | Pending | Pending | HOLD |
| Cold-start link recovery | Pending | Pending | HOLD |
| Deliberate radio-loss detection and recovery | Pending | Pending | HOLD |
| Reviewed armed/idle software failsafe with ESC isolated | Pending | Pending | HOLD |

## Propulsion checks after all power and safety gates close

| Motor Test | Expected position / rotation / output | Actual physical motor / direction / startup / stop | Evidence / result |
|---|---|---|---|
| A | M1 front right / CCW / output 4 | Pending | HOLD |
| B | M4 rear right / CW / output 3 | Pending | HOLD |
| C | M2 rear left / CCW / output 1 | Pending | HOLD |
| D | M3 front left / CW / output 2 | Pending | HOLD |

Record approved supply voltage, command and duration, current/temperature, any twitch/stall/reset and post-test inspection. Add the short controller-throttle response and safe stop record only after all four mapping checks pass. No full-throttle unloaded test is prescribed.

## Pi and integration checks

| Check | Actual measurements / software identity | Evidence / result |
|---|---|---|
| Bare Pi on reference USB-C | Repeat and record | HOLD |
| BEC output and Pi input throughout startup | Pending | HOLD |
| Each peripheral added power-off between changes | Pending | HOLD |
| Camera real capture and HAT workload | Pending | HOLD |
| SATEL variant/wiring approved, valid timestamped ranging | Pending | HOLD |
| Full processing load/thermal/power margin | Pending | HOLD |
| FC telemetry and independent restart/loss behaviour | Pending | HOLD |

## Close the session

Save the after export/hash, raw logs, screenshots/recording intervals, deviations, faults and rollback performed. Confirm power isolated and equipment stored safely. Record reviewer decision **pass / fail / hold**, specific limits and the next authorized gate. Flight readiness requires a separate plan and approval; this form is not a flight certificate.
