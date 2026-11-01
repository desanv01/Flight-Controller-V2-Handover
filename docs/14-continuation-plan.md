# Continue development through explicit acceptance gates

The next milestone is a reproducible safe bench baseline, not autonomous flight. Every gate needs a named incoming owner, measured/recorded results and acceptance in [the test form](../handover/ACCEPTANCE.md). A proposed step is not marked complete because a guide contains it.

## Gate 0 Intake and source control

Label FC2/FC1, inventory all equipment, photograph wiring/top/nose, recover missing originals where possible, preserve the 21 October snapshot, this public release and the separately held private evidence package. Read the original/public firmware distinction. Record each incoming change in a separate reviewed commit. Exit: custody sheet, exact received assembly, source provenance and safe isolated bench.

## Gate 1 FC only

Verify POWER1/no backfeed, startup/current/rail/temperature behaviour, firmware identity, both IMUs/barometer, calibration persistence, installed attitude axes, repeated startup and diagnostic logging. Investigate fresh inconsistency warnings; do not mask them. Exit: signed FC-only acceptance and saved logs/parameters.

## Gate 2 Receiver and pilot controls

Verify the qualified J7 harness, RF/CRSF identity, main input directions/ranges, fully low throttle, final stick-arming arrangement, cold-start link and deliberate loss/recovery detection with ESC isolated. Review actual momentary/latching controls and throttle mechanics. Exit: physical-controls recording, fresh export and loss/recovery record.

## Gate 3 Propulsion interface

Obtain ESC team's exact firmware/configuration and assembled electrical ratings. Review main power/capacitor/ground/J6 mapping and post-flip condition. With props off and approved supply, establish A/B/C/D positions/rotation, clean short startup and stopping; then brief collective-throttle response. Exit: all four observed mappings, electrical/thermal observations, current profile and controlled stop evidence. No props-on testing at a desk.

## Gate 4 Power monitoring and failsafe design

Select and qualify actual battery sensing, low/critical actions, RC-loss behaviour, recovery/pilot takeover and effects of available navigation. The stored RTL-oriented radio failsafe is not proof of usable return-home without a position solution. First test relevant software actions with propulsion isolated. Exit: reviewed failure-mode matrix, calibrated battery evidence and tested ground responses; airborne claims remain separate.

## Gate 5 Navigation decision

Decide whether the next controlled demonstrator is manually piloted or navigation-capable. Qualify external GNSS/compass or a properly supported alternative as required. Define estimator sources, mounting, interference and acceptable performance. No-GPS manual possibility is not a shortcut around unresolved propulsion or sensor gates. Exit: documented architecture and accepted sensors appropriate to intended modes.

## Gate 6 Pi and perception

Resolve bare-Pi BEC boot, qualify the full power path and workload, then camera, HAT and LiDAR separately and together. Preserve OS/application/dependency versions and data-quality/failure tests. Exit: repeatable startup and workload records, valid timestamped sensor/inference outputs, no adverse effect on FC supply/control.

## Gate 7 Companion telemetry then data integration

Prove telemetry first using USB or verified J11/SERIAL7. Test independent restarts and dropouts. Define proximity/navigation message contract, invalid/stale handling and pilot authority before enabling any control effect. Exit: reviewed data contract, measured timing and loss behaviour; no hidden dependency of stabilization on Pi health.

## Gate 8 Separate supervised flight readiness review

An experienced multirotor lead must review mounting, CG/weight/thrust margin, motor/propeller compatibility, all axes/directions, power rating, battery sensing, failsafes, estimator/modes, logs/vibration, tuning prerequisites, pilot skills, site and applicable permissions. Prepare a separate limited first-flight/test plan with abort criteria and responsibilities. This package does not supply a ready-to-load flight profile or certify flight.

## Suggested first work allocation

The FC lead closes Gates 0–2 and coordinates interfaces. The ESC lead supplies ratings/firmware and joins Gate 3. The electrical lead resolves power/monitoring. The Pi lead can prepare software records and a USB-C baseline in parallel with non-propulsion work, but cannot sign off the FC or ESC. Assign navigation and flight-test leads explicitly instead of assuming the outgoing contributor owns them indefinitely.

Use the [ownership matrix](../handover/OWNERSHIP.md) and [open issues](../handover/OPEN-ISSUES.md) as the work queue. Preserve functioning configurations until a change has a specific reason, test and rollback.
