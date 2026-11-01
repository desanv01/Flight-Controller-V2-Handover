# ESC and motor commissioning

The ESC team reported target **OPENESC_30_F421** and **DShot300** support. The FC is configured for DShot300 and recorded tests show actual rotation. That is not yet approval of the assembled ESC for full-charge 6S, proof of its firmware version, or acceptance of all four motor positions and directions.

## Preserve these boundaries

- The FC sends four nominal 3.3 V logic command signals; the ESC supplies motor phase power.
- Receiver input is separate from motor output. Do not use RC passthrough to make individual sticks drive motors.
- J6 carries ground and four signals only. Its unused cavities are not battery/5 V/current-sense inputs.
- DShot does not need conventional high-throttle/low-throttle endpoint calibration. Leave `ESC_CALIBRATION=0` for this arrangement.
- `SERVO_DSHOT_ESC=1` selects command behaviour, not proof that AM32/BLHeli32 or a specific firmware is installed.
- `SERVO_BLH_AUTO=1` is present in the latest file. It is not permission to run passthrough flashing. Bidirectional DShot remains disabled (`SERVO_BLH_BDMASK=0`).
- Outputs 1–4 share **TIM1** in the custom target. Review protocol/timer/DMA changes as an output-group change with the ESC team, not as four unrelated adjustments. `RC_SPEED=490` is not the DShot bit rate or ELRS packet rate. The saved `SERVO_BLH_POLES=14` is an unverified motor-pole assumption, not a measured motor identity.

## Electrical output versus logical motor

The latest saved assignments differ from the compiled initial defaults. For normal Quad X geometry, viewed from above:

| FC output | J6 pin / MCU | Saved function | Expected logical motor position | Expected rotation |
|---:|---|---|---|---|
| 1 | 5 / PE14 | 34 = Motor2 | Rear left | CCW |
| 2 | 6 / PE13 | 35 = Motor3 | Front left | CW |
| 3 | 7 / PE11 | 36 = Motor4 | Rear right | CW |
| 4 | 8 / PE9 | 33 = Motor1 | Front right | CCW |

These positions are what the **current logical assignment requires**, not observations of the harness. The incoming team must mark the real nose and establish actual connections. Do not replace the values with 33/34/35/36 just because that is a common default.

| Mission Planner Motor Test | Logical motor | Required position / rotation | Electrical output under saved mapping |
|---|---|---|---:|
| A | 1 | Front right / CCW | 4 |
| B | 4 | Rear right / CW | 3 |
| C | 2 | Rear left / CCW | 1 |
| D | 3 | Front left / CW | 2 |

## Gates before any powered motor test

The technical lead must sign off all of the following in the [acceptance sheet](../handover/ACCEPTANCE.md):

1. Every propeller physically removed; no loose items near bells/shafts.
2. Post-flip inspection passed, including frame, screws, bearings, phase leads, solder joints and FC mounting.
3. Correct FC top/nose and attitude directions verified; no fresh blocking INS/gyro/accel warnings.
4. ESC team has identified board revision, installed firmware version/configuration and accepted input signalling.
5. Supply, capacitor, wiring and protection approved for the **actual test voltage**, including 25.2 V if using a full 6S pack. An unconfirmed rating is a hold.
6. J6 continuity/common ground and output permutation reviewed.
7. Source disconnect accessible without crossing rotating parts; observer and stop conditions agreed.
8. Transmitter inputs, low throttle and propulsion-isolated arm/disarm already checked.

The historical recordings do not close these gates. Do not reconnect the battery merely because the FC can arm.

## Identify motors with the FC disarmed

Once all gates are closed:

1. Secure the propeller-free aircraft. Open **SETUP → Optional Hardware → Motor Test** and confirm the frame is Quad X.
2. Choose a short test, for example **2 seconds**, and a low starting command, for example **5%**. These are starting test settings, not guaranteed startup values or measured thrust.
3. Energize the approved ESC branch. Test **A only**, observe from clear of the motor, then wait for it to stop.
4. Record which physical motor moved and its rotation using a safe visual method. Do not touch a bell, use loose tape or fit a propeller to determine direction.
5. Repeat B, C and D separately. Do not use Test All for identification.
6. If startup is uncertain, use only agreed small short increments; stop for twitching, stall, heat, resets or abnormal sound. Do not jump to high command.
7. Disconnect power before changing wiring, phase connections or ESC configuration. Preserve before/after settings.

Motor Test is a separate command path. Do not assume stick disarming cancels it. Use short durations and a physical disconnect plan.

## Brief controller throttle response test

Only after the identity/direction test and previous gates pass:

1. Keep all props off, aircraft secured and Pi branch off. Set Stabilize, transmitter on, throttle fully low, other axes centred.
2. Start the approved supplies and allow stationary initialization. Confirm no fresh blocking warnings.
3. Arm using the verified down-right stick gesture, then centre yaw while keeping throttle down.
4. Raise only throttle **slightly and briefly**. Record CH3 input, output commands and physical motor response together if practical.
5. Lower throttle fully, disarm, verify all motors stop, then electrically isolate propulsion.
6. Stop and diagnose if inputs rise but outputs do not, outputs rise but motors do not, or the FC repeatedly disarms. Do not solve an unexplained response by increasing to full throttle.

`MOT_SPIN_ARM=0.1`, `MOT_SPIN_MIN=0.15` and `MOT_SPOOL_TIME=0.5` are saved settings. They are not 10% RPM, 15% thrust or a certified delay. Stabilization can produce unequal unloaded motor outputs; prolonged or full-throttle no-prop running is not a tuning method.

## ESC team deliverables still required

Supply the board schematic/revision and pinout; exact MCU and firmware version/commit; full ESC configuration export; supported command/telemetry features; voltage/current/protection/capacitor approval; motor model/KV/poles; and measured input/output acceptance. A target name alone is insufficient. Keep bidirectional DShot, RPM filtering, passthrough updates and protocol changes as later separately reviewed work.

References: [ArduPilot DShot](https://ardupilot.org/copter/docs/common-dshot-escs.html), [motor order diagrams](https://ardupilot.org/copter/docs/connect-escs-and-motors.html), [motor range](https://ardupilot.org/copter/docs/set-motor-range.html). The custom J6 signal-only contract overrides generic wiring pictures that include power pins.
