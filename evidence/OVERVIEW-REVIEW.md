# Scope of two additional sparse recording reviews

On 1 November 2026, two previously unclassified recordings were sampled to identify their subject. Fourteen extracted overview frames and container metadata remain in private custody. This was **sparse classification, not a full-timeline or every-frame inspection**. No new passed motor, programming or flight test is inferred.

## E01 · 16 October initial FC session

Container duration **752.666667 seconds**, 1920×1080. Samples at **0, 150, 300, 450, 600 and 740 seconds**.

| Sample | Observation | Limit |
|---:|---|---|
| 0s | Programmer and FC programming discussion | Sample did not establish a completed write |
| 150s | Desktop and transition instructions | Instructions are not measured results |
| 300s | Mission Planner custom-firmware workflow, board type 1241 | No byte-for-byte flash read-back |
| 450s | ArduCopter 4.7.1 / SALFCGAMUDA, DISARMED, startup warnings, inverted-looking attitude | Actual physical orientation not shown |
| 600s | Similar early telemetry/messages | Does not close thermal/sensor qualification |
| 740s | DISARMED with early warnings and contributor describing initial results | Not the later calibrated receiver profile |

This supports early programming/startup classification. E02 and the corresponding parameter exports record later calibration separately.

## E09 · 21 October afternoon controls

Container duration **3050.291667 seconds**, 1920×1080. Samples at **0, 300, 600, 900, 1200, 1800, 2400 and 3000 seconds**.

| Samples | Observation | Limit |
|---|---|---|
| 0–1200s, sparse | DISARMED Mission Planner and corrected-radio/control discussion | Intervening intervals not inspected |
| 1800s | Momentary RC6/immediate-disarm discussion | Not a physical button timing measurement |
| 2400s | Contributor reports working stick arm/disarm; CH3 near 998 and outputs near 1000 while DISARMED | Reported result, not independent physical throttle/motor acceptance |
| 3000s | Future motor/failsafe guidance; ground station shows CONNECT | Cached values are not live telemetry and guidance is not an executed test |

The recording is about FC/receiver controls, not a demonstrated Pi power repair. All four motor positions/directions, synchronized physical throttle response and failsafe acceptance remain unestablished. Review relevant continuous intervals privately before making stronger claims.
