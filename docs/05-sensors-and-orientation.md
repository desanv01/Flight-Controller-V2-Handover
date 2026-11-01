# Sensor calibration and installed orientation

FC2 has two dissimilar IMUs and a BMP388 barometer. Earlier records demonstrate useful live data and successful calibration, but later sessions also show inconsistency warnings. **A moving horizon and saved IDs are not sufficient to close sensor acceptance.**

## Recorded baseline

| Parameter | Recorded device or role |
|---|---|
| `INS_ACC_ID` and `INS_GYR_ID` = 3408178 | ICM42688P |
| `INS_ACC2_ID` and `INS_GYR2_ID` = 3670298 | BMI270 |
| `INS_ENABLE_MASK=127` | Probe mask in saved profile |
| `INS_USE=1`, `INS_USE2=1` | Both sensors enabled |
| `EK3_IMU_MASK=3` | Both EKF IMU instances configured |
| `AHRS_ORIENTATION=0` | Saved default board orientation, not proof of installed axes |

The latest file includes saved accelerometer scales/offsets and roll/pitch trims. Do not manually type sensor IDs, copy them to a new board or delete the calibration to make a warning disappear. Calibration temperatures are stored calibration metadata, not current live temperature measurements.

## Repeatable verification before recalibration

1. Isolate propulsion and Pi power; remove all props. Secure FC2 with no underside short and slack cables.
2. Establish the actual aircraft nose and intended FC top from physical mounting, not from the screen orientation you prefer.
3. Start from power off and let the FC initialize motionless. Record fresh startup messages and both sensor IDs/health.
4. Observe at comparable elapsed times and temperatures. Stop for abnormal heating, repeated resets or new inconsistency warnings while stationary.
5. With the aircraft physically level and disarmed, record numeric roll and pitch plus a photograph of the physical attitude.
6. Raise the marked nose: pitch should increase in the nose-up sense. Return level.
7. Lower the aircraft's right side: roll should increase in the right-bank sense. Return level.
8. Repeat slowly, recording the physical board and display together. Verify both sensors remain plausible and continuous where telemetry/logging exposes them.
9. Repeat deliberate cold/warm starts and record conditions. Disconnected screens and old warnings are not current measurements.

If the horizon is inverted with the intended top up, first investigate mounting, sensor axis definitions and firmware identity. Do not use trial-and-error orientation changes with powered motors or compensate with extreme level trims. Both firmware IMU rotations start at `ROTATION_NONE`; confirm that assumption against the assembled sensor axes.

## Six-face calibration when justified

Recalibrate a new/repaired board, a genuinely invalid calibration, or after an approved orientation change—not simply because time passed.

1. Export the current settings. Isolate propulsion, leave the FC alone on a stable nonconductive support, and preserve the working receiver configuration.
2. Open **SETUP → Mandatory Hardware → Accel Calibration** in the installed Mission Planner version.
3. Follow its exact prompts for level and each requested face. Place the **whole FC** in each orientation and hold it still before acknowledging.
4. Support the PCB without bending it or pressing components. Avoid cable torque and accidental motion during each sample.
5. Require an explicit success result; save the screen and subsequent read-back. A completed progress bar without success is not acceptance.
6. If the firmware/UI offers a separate level calibration, perform it only with verified mounting/orientation and a truly level reference. It does not fix a wrongly rotated sensor.
7. Fully restart stationary and verify persistence, directions and both IMUs again. Export the result with a new name.

## Diagnostic logging

The saved backend is `LOG_BACKEND_TYPE=4` and `LOG_DISARMED=0`. For an approved short sensor investigation, a competent operator may record the old setting, temporarily enable disarmed logging, restart stationary, record a short still/controlled-tilt/still sequence, then restore `LOG_DISARMED=0` and close the session. Download the newest DataFlash log through Mission Planner without erasing it.

Inspect IMU instances, accelerometer/gyro health/error counters, temperatures, attitude, barometer and messages. The goal is continuity and consistent motion, not identical samples from different sensors. Do not substitute a screen recording for a time-series log. Limited onboard flash can fill; do not leave diagnostic logging enabled indefinitely.

## Unresolved warnings

`Arm: Leaning`, `Accels inconsistent`, `Gyros inconsistent` and the earlier FC1 INS/heating fault are different observations. The later corrected attitude and accepted arming do not by themselves prove every cause has been resolved. Log fresh warnings against time, physical state, supply and firmware. Do not raise inconsistency thresholds, disable one IMU or skip checks solely to pass arming.

References: [accelerometer calibration](https://ardupilot.org/copter/docs/common-accelerometer-calibration.html), [pre-arm checks](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html), [DataFlash logging](https://ardupilot.org/copter/docs/common-downloading-and-analyzing-data-logs-in-mission-planner.html).
