# Recorded state at handover

Prepared **1 November 2026**. The latest identified FC2 configuration is `FC2_stick_control_working_2026-10-21.param`, not a live read-back from the aircraft today. The outgoing contributor stated that the project was left at the same bench-development level. Incoming staff must check that the received hardware still matches.

## Demonstrated and outstanding work

| Area | Recorded result | Remaining boundary |
|---|---|---|
| FC2 | Programming, boot, Mission Planner communication and live attitude | Not a complete electrical, thermal or flight qualification |
| Sensors | Two IMUs identified; successful accelerometer calibration and plausible barometer data recorded | Later gyro/accel inconsistency history remains relevant; installed-axis and repeated-start checks need closure |
| Receiver | ELRS link and CRSF inputs reach the FC; corrected endpoints saved | Complete physical directions and controlled loss/recovery acceptance must be signed off |
| Arm control | Software ARMED transitions recorded; final stick arm/disarm reported working | Shoulder-button instructions are superseded |
| Propulsion | Physical footage and user reports establish motor rotation | All four positions/directions, safe stopping, supply rating and loaded performance not accepted |
| GPS and compass | No external module reported installed; no fitted GNSS or magnetometer in released assembly | No GPS navigation, geographic return-home or absolute-heading qualification |
| Pi system | Bare Pi boots from USB-C according to the user | Battery/BEC boot fails or returns to red; no measured diagnosis supplied |
| Companion integration | Camera, LiDAR and AI HAT+ identified/discussed | Complete sensor acquisition, power and FC communication not established |
| Flight | None verified | No takeoff authorization or flight configuration supplied |

## Last saved FC2 settings

These values describe a **historical bench profile**, not a change list to apply blindly. The exact file is in [configuration snapshots](config/README.md).

| Function | Values |
|---|---|
| Frame | `FRAME_CLASS=1`, `FRAME_TYPE=1` — Quad X |
| RC UART | `SERIAL2_PROTOCOL=23`, `SERIAL2_OPTIONS=0` |
| CRSF and ELRS | `RC_PROTOCOLS=512`, `RC_OPTIONS=8224`, `RSSI_TYPE=3` |
| RC baud parameter | `SERIAL2_BAUD=57` saved; serial-RC handling controls effective baud |
| Inputs | `RCMAP_ROLL=1`, `RCMAP_PITCH=2`, `RCMAP_THROTTLE=3`, `RCMAP_YAW=4` |
| Final arm arrangement | `RC6_OPTION=0`, `ARMING_RUDDER=2` |
| Checks | `ARMING_SKIPCHK=0` |
| Mode | `INITIAL_MODE=0`; all six `FLTMODE` slots `0` — Stabilize; mode channel 5 |
| Motor protocol | `MOT_PWM_TYPE=5` — DShot300; `ESC_CALIBRATION=0` |
| Outputs 1 through 4 | `SERVO1_FUNCTION=34`, `SERVO2_FUNCTION=35`, `SERVO3_FUNCTION=36`, `SERVO4_FUNCTION=33` |
| ESC options | `SERVO_DSHOT_ESC=1`, `SERVO_BLH_AUTO=1`, `SERVO_BLH_BDMASK=0` |
| Attitude | `AHRS_ORIENTATION=0`; nonzero saved roll/pitch trims |
| IMUs | Both enabled; `EK3_IMU_MASK=3`; IDs 3408178 and 3670298 |
| Compass and yaw | `COMPASS_ENABLE=0`; all three `COMPASS_USE` values `0`; `EK3_SRC1_YAW=0` |
| Battery | `BATT_MONITOR=0` |
| Radio failsafe | `FS_THR_ENABLE=1`, `FS_THR_VALUE=975`, `RC_FS_TIMEOUT=1`, `FS_OPTIONS=16` |
| Logging | `LOG_BACKEND_TYPE=4`, `LOG_DISARMED=0` |
| Companion port | `SERIAL7` is the J11 UART; its working connection is not accepted |
| External GPS port | J4 maps to `SERIAL6`; saved `SERIAL6_PROTOCOL=-1` |

The radio endpoints are roll **993/1500/2010**, pitch **988/1500/2003**, throttle **991/998/2008**, yaw **993/1500/2008** in minimum/trim/maximum order. These belong to this transmitter/receiver calibration, not another installation.

## Interpretation that must survive transfer

- RC6 was a momentary shoulder control. Releasing it requested disarm under the earlier switch setup. The final setup deliberately leaves it unused.
- Output number, ArduPilot motor number and Motor Test letter are different labels. Preserve the permutation until physical tests establish its correctness.
- `BATT_MONITOR=0` explains zero battery telemetry; it does not mean the battery is empty, and it gives no qualified flight-pack protection.
- Stored IMU IDs/calibration do not prove current sensor health. Counters such as `STAT_FLTCNT=6` and `STAT_FLTTIME=11` do not prove actual flight.
- No-compass bench settings do not create a heading reference or GPS return-home capability.
- The original SALFCGAMUDA build and public FCV2 rebuild are different files. See [firmware](docs/12-firmware-and-recovery.md).

## Evidence confidence labels

**Recorded:** visible result or saved file. **Reported:** outgoing contributor's account, not independently measured here. **Planned:** a procedure not established as completed. **Unresolved:** a fault or acceptance gap. Each new test should retain these distinctions in the [acceptance record](handover/ACCEPTANCE.md).
