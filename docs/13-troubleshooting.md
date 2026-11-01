# Troubleshoot without destroying the baseline

Start by isolating propulsion, saving the current configuration and reading the newest timestamped messages. Change one understood cause at a time. Do not reflash, reset or disable checks as a general diagnostic shortcut.

| Symptom | First checks | Do not do |
|---|---|---|
| FC absent from USB | External POWER1, correct data cable, actual COM port, connector, driver, boot state | Assume FC USB powers it or flash another H743 target |
| Mission Planner screen static | Connection button/state, fresh telemetry timestamps, cable/power | Treat cached disconnected values as live health |
| Zero battery voltage | Saved `BATT_MONITOR=0`, whether a real monitor exists | Connect 6S to a guessed ADC or use FC rail as battery voltage |
| Compass unhealthy / empty table | No onboard compass, external hardware presence and intended estimator profile | Repeated calibration or fabricated device IDs |
| GPS No GPS | No module installed; if installed, actual J4/SERIAL6 power/UART | Assign generic SERIAL3 without tracing this board |
| Arm Leaning | Actual installed FC top/nose, numeric attitude, six-face calibration and sensor consistency | Rotate parameters at random with powered motors |
| Gyros/accels inconsistent | Stationary startup, both IMUs, supply/heat, sensor rotations, logs | Disable the second IMU or increase thresholds just to arm |
| Arm throttle too high | Actual CH3 low position, physical stick mapping, newest message | Change ESC protocol to solve a high RC input |
| Roll max/min warnings | Live full-axis travel; intermediate file had 1468–1534 | Type fake endpoints to clear validation |
| RC6 no longer arms | Final `RC6_OPTION=0` intentionally leaves it unused | Restore old momentary arm mapping unintentionally |
| Motors stop when shoulder released | Earlier momentary RC6 state returned low | Remap flight channels to motor passthrough |
| Armed but fixed-looking low speed | CH3 at minimum, armed idle, persistent arming state | Assume a missing speed-enable setting or raise to full throttle |
| CH3 rises but outputs do not | Mode, arm/spool state, calibration/dead zone, messages | Randomly replace motor functions/PIDs |
| Output commands change, motor does not | ESC input/protocol/supply, ground, harness, team firmware | Blindly update ESC firmware or perform PWM endpoint calibration |
| Wrong motor responds | Marked nose, Motor Test letter versus logical motor versus electrical output | Reset permutation to defaults without physical mapping |
| Pi red / green then red | Bare Pi USB-C baseline, BEC and Pi startup voltage, wiring/peripheral isolation, HDMI | Diagnose current from LED alone or select 8/12 V |
| Camera absent | Power-off ribbon/socket/contact check and supported camera stack | Hot-plug, GPIO-power the ribbon camera or use legacy stack |
| LiDAR not ranging | Exact SATEL variant/bridges/levels, I2C, driver and validity | Treat address detection or zero distances as accepted ranging |
| Pi UART no FC heartbeat | J11/SERIAL7, crossed TX/RX, 3.3 V levels, actual Pi UART device route | Disturb working receiver SERIAL2 or assume serial0 means pins 8/10 |

## Save a useful fault report

Record physical article and firmware, exact newest message/time, wiring state, supply voltage **at the load**, temperature/time since power-on, steps to reproduce, before/after parameters and relevant log/video intervals. Distinguish a user's report from visible evidence and an inferred cause from a confirmed repair.

For a post-impact issue, inspect frame/mounts/shafts/wiring first. If power resets or heating occur, stop repeated restarts. A successful later arm attempt is not a full fault closure. Use the [open-issue register](../handover/OPEN-ISSUES.md) and attach acceptance evidence when closing an item.
