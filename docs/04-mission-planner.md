# Connect Mission Planner and preserve the FC state

Mission Planner is the ground station on the laptop. ArduCopter is the firmware on FC2. The recorded versions were Mission Planner **1.3.83** and ArduCopter **4.7.1**, custom SALFCGAMUDA target. A different COM port or ground-station version on the incoming workstation is possible; record it rather than forcing an old port assignment.

## Connect without propulsion

1. Complete [intake](../START-HERE.md). Remove every propeller and physically isolate ESC power. Leave the Pi branch off.
2. Power FC2 using its verified regulated POWER1 branch. Keep the board still during initialization.
3. Connect a known USB data cable to the FC. Do not connect the transmitter's USB and assume that is the FC port.
4. In Windows Device Manager, identify the FC's COM port by device appearance. If enumeration fails, investigate external power, cable, driver and connector before erasing firmware.
5. Open Mission Planner. Select that COM port and **115200** for the recorded USB connection workflow; this does not configure the receiver UART's 420 kbaud behaviour.
6. Select **Connect** and wait for the full parameter download. Do not start calibration while the download is incomplete.
7. Save the displayed firmware/board identity and startup Messages. A screenshot with the firmware banner helps distinguish the application, board and ground station.
8. Confirm live attitude/status updates while disarmed. A retained screen after disconnect is not live telemetry.

## Save all parameters before changes

1. Open **CONFIG → Full Parameter List** or **Full Parameter Tree**.
2. Clear filters, refresh/read all parameters if needed and wait for completion.
3. Choose **Save to File**, not Load from File.
4. Name the new export with date, test article and purpose, for example `FC2_incoming_readback_YYYY-MM-DD.param`.
5. Confirm a populated file was created. Record its SHA256 and keep it immutable; copy it before experimenting.
6. Compare with [historical snapshots](../config/README.md). Classify differences as calibration, runtime counters/startup values, intentional configuration or unexplained change.

Do not restore another board's calibration, use the legacy upstream `configs.param`, or load all 945 entries merely to set one receiver option.

## Pages used in this project

| Page | Purpose | What it does not prove |
|---|---|---|
| DATA / HUD | Live attitude, mode and arming state | Correct physical axes or healthy hardware by itself |
| DATA / Messages | Timestamped startup/errors/arm rejection | A persistent old message is not necessarily a fresh fault |
| DATA / Status | Live channel inputs and output commands | Output values are not measured RPM or electrical waveforms |
| SETUP / Radio Calibration | Input values, ranges and calibration | Switch assignment or physical stick direction from a still image |
| SETUP / Flight Modes | Mode-slot assignments | Readiness of those modes for the installed sensors |
| SETUP / Servo Output | Electrical output function assignments | Physical motor order/direction |
| SETUP / Optional Hardware / Motor Test | Explicit motor test requests | Normal RC arming behaviour; treat it as a separate source of motion |

On the DATA HUD, **Stabilize** is the flight mode. **DISARMED** is the arming state. Both can appear together. “Ready to Arm” does not override a rejection from a subsequent arm request.

## Make an approved individual change

Record old value, new value, reason, source, operator and expected result in [acceptance](../handover/ACCEPTANCE.md). Search the exact parameter, edit it, choose **Write Params**, wait for acknowledgment, then read it back. Restart only as required with propulsion isolated. For receiver communication problems after a software reboot, use a deliberate full FC/receiver power cycle and recheck rather than swapping wires randomly.

Never use “install firmware,” “reset defaults,” “load parameters,” force-arm or broad arming-check changes as routine connection troubleshooting. A successful write is not a passed physical test.

## End the session

Save results and a post-change export, disconnect Mission Planner, remove USB and switch off the regulated branch. Confirm hardware is off before harness work. Keep original telemetry logs if available; this compilation did not establish a corresponding complete MAVLink/DataFlash log set for the final motor sessions.

Official reference: [Mission Planner](https://ardupilot.org/planner/). Interface locations can vary; verify the installed version before following an old screenshot.
