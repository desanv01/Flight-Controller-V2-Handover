# Pilot controls and radio calibration

The final arrangement uses the two joysticks for CH1–CH4 and **stick arming/disarming**. The shoulder control is momentary and deliberately unused (`RC6_OPTION=0`). Do not combine old shoulder-button instructions with this arrangement.

## Mode 2 control reference

These physical directions apply only after the one-axis verification below. Aircraft left/right refers to the aircraft, not the person facing it.

| Action | Intended Mode 2 control, verify physically | Channel |
|---|---|---|
| Roll left/right | Right stick left/right | CH1 |
| Pitch nose down/up | Right stick forward/back | CH2 |
| Increase/decrease collective demand | Left stick up/down | CH3 |
| Yaw nose left/right | Left stick left/right | CH4 |
| Arm request on bench | Left stick fully down-right, held until ARMED | Low CH3 + right CH4 |
| Ground disarm | Left stick fully down-left, held until DISARMED | Low CH3 + left CH4 |

The recorded gesture hold is approximately 3–5 seconds; trust the confirmed arming state, not a count alone. After arming, center **yaw only** while keeping throttle fully low. If the throttle axis springs to centre, releasing it can command substantial throttle. Record its actual mechanical arrangement before propulsion work. Stick disarm is not instantaneous and must not be used as an in-flight gesture.

Stabilize does not hold altitude or position. Roll/pitch/yaw are requests processed by the FC's mixer; there is no CH1-to-motor1 passthrough to enable.

## Verify each physical axis before changing settings

Remove props and disconnect ESC power. In **SETUP → Radio Calibration**, do not start calibration simply to identify a control.

1. Lower the actual throttle stick and confirm CH3 is close to the saved low endpoint.
2. Move only right-stick left/right: only the intended roll input should follow, low to high.
3. Move only right-stick forward/back: verify pitch input and direction against Mission Planner's radio calibration instructions.
4. Move only left-stick down/up: verify CH3 smoothly traverses low to high.
5. Move only left-stick left/right: verify CH4 traverses low to high.
6. Return to centred roll/pitch/yaw and fully low throttle. Record a combined view of sticks and live bars.
7. Check auxiliary controls independently. Do not assign mode selection and arming to the same channel. Channel 5 remains the recorded mode channel.

The final export's minimum/trim/maximum values are:

| Axis | Minimum | Trim | Maximum | Reversed flag |
|---|---:|---:|---:|---:|
| Roll | 993 | 1500 | 2010 | 0 |
| Pitch | 988 | 1500 | 2003 | 0 |
| Throttle | 991 | 998 | 2008 | 0 |
| Yaw | 993 | 1500 | 2008 | 0 |

These are evidence of captured values, not numbers to force into a different transmitter. Reverse a genuinely reversed axis in one reviewed place only, then repeat the physical test.

## Recalibrate only when the live test requires it

1. Save a full backup. Keep propulsion isolated and any auxiliary arming function inactive.
2. Start **Calibrate Radio** and follow the prompts.
3. Move all intended axes through their real full range and exercise the physical switches. Do not stop after only moving throttle.
4. Select Done when the full capture is finished.
5. At the final prompt, centre roll/pitch/yaw and hold throttle **fully down** before acknowledging.
6. Inspect ranges for every control. A roll range near 1468–1534 is invalid as a full-stick capture; this occurred in an intermediate file and was later corrected.
7. Verify low-throttle input, directions and persistence after a complete FC/receiver restart. Export a new snapshot and keep the old one.

Earlier files with throttle trims 1448, 1826 or 1618 are historical. Their trim alone does not prove an equivalent motor-throttle command, but the final calibration prompt was not completed at the required low position.

## Propulsion-isolated arm and disarm check

Proceed only after safe intake, correct orientation, low throttle and no fresh blocking warnings. ESC propulsion must remain **electrically disconnected**.

1. Read back `RC6_OPTION=0`, `ARMING_RUDDER=2`, `ARMING_SKIPCHK=0`, and verify CH1–CH4 mapping.
2. Confirm Stabilize and DISARMED on the HUD. The shoulder button should not arm the FC.
3. Keep right stick centred; hold left stick down-right until ARMED.
4. Return yaw to centre with throttle still down. Confirm it does not immediately disarm from shoulder-button release.
5. Hold down-left until DISARMED. Record the transition.
6. If an arm request is rejected, lower controls and inspect the **newest timestamped** message. Do not bypass it.

The saved `DISARM_DELAY=10` may cause automatic disarming under qualifying landed/idle conditions. Do not disable it just to keep ARMED visible. For a throttle-command check with motors isolated, inspect CH3 input and output command telemetry after a normal arm request, then return throttle low and disarm. These values are not RPM measurements.

Physical motor tests require the additional [propulsion gates](08-esc-and-motors.md). References: [radio calibration](https://ardupilot.org/copter/docs/common-radio-control-calibration.html), [arming](https://ardupilot.org/copter/docs/arming_the_motors.html), [Stabilize](https://ardupilot.org/copter/docs/stabilize-mode.html).
