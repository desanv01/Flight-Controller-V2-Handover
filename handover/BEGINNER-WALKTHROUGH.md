# Begin the FC2 handover from zero

Use this route if you have not previously used GitHub, Mission Planner or this drone. The first session ends with a saved live configuration and a written result. It does not include motor rotation. An incoming engineer competent with multirotors, batteries and electronics must supervise powered hardware work; reading a guide does not supply that competence.

## Understand the five main parts

Read [foundations](../docs/01-foundations.md) first. The **T8L transmitter** sends the pilot's controls to the **receiver**. The receiver passes those inputs to the **FC2 flight controller**, which runs ArduCopter and uses its sensors to calculate motor commands. The **ESC** turns those commands into motor phase power. **Mission Planner** is the laptop application used to inspect/configure the FC. The separate Pi perception system is unfinished and should remain disconnected during the first FC sessions.

The prototype was left at bench development. Start with [current status](../CURRENT-STATUS.md), not the firmware-installation button. **FC2** identifies a physical board; **V2** identifies the published design. FC1's reported heating/INS problem is a separate unresolved fault.

## Download and locate the handover

1. Open the [public repository](https://github.com/desanv01/Flight-Controller-V2-Handover).
2. For a first read, click `START-HERE.md` directly on GitHub. Follow the blue links to the chapters.
3. To keep a complete local copy without installing Git, choose **Code → Download ZIP**. In Windows File Explorer, right-click the downloaded ZIP and choose **Extract All**. Work in the extracted folder, not inside the ZIP viewer.
4. Find `README.md`, `START-HERE.md`, `CURRENT-STATUS.md`, and the `docs`, `config`, `handover`, `references`, `inventory` and `tools` folders. All are part of the delivery.
5. Keep this downloaded copy unchanged. Create a separate dated private session folder for new results; do not save new exports into `config/historical-fc2-snapshots`.
6. Optional integrity check: with Python 3.10+ installed, open PowerShell in the extracted repository folder and run `python tools/verify_handover.py`. If Windows uses the Python launcher, use `py -3 tools/verify_handover.py`. Require `result: PASS`. If Python is unavailable, the incoming lead can install it from [python.org](https://www.python.org/downloads/) or perform the check on another workstation before hardware work.

Git users should use the clone command in the [README](../README.md), which preserves the distributed line endings. The verification command reads files only; it neither connects to the aircraft nor applies settings. An error is a reason to inspect the download or command, not flash the FC.

## Install the laptop ground station

1. Keep the FC and all power sources disconnected while installing software.
2. Open the [official Mission Planner installation page](https://ardupilot.org/planner/docs/mission-planner-installation.html) and follow its Windows installer link. Run the downloaded MSI and its driver setup; use that official source rather than an unrelated driver site.
3. Open Mission Planner and record its actual version. The recorded project used 1.3.83; a newer ground station can have different labels. Do not change the FC firmware just to make the version numbers match.
4. Locate **DATA**, **SETUP** and **CONFIG**. DATA is telemetry/status, SETUP contains calibration/test pages, and CONFIG contains parameters. **Install Firmware is not part of this intake.**

## Prepare one private session folder

In File Explorer, make a folder beside the extracted handover, for example `FC2-intake-YYYY-MM-DD`. Replace the date with the actual session date. Store these files there:

| File | What to record |
|---|---|
| `session-notes.txt` | Operator/observer, article IDs, date/timezone, procedure, supply and disconnected branches, observations and pass/fail/hold decision |
| `FC2_incoming_readback_YYYY-MM-DD.param` | Complete fresh parameter export before any changes |
| `firmware-and-messages.png` | Live firmware identity and newest startup messages |
| `wiring-and-nose` photographs | Received board, orientation, harness ends, regulator setting and any damage |
| `parameter-comparison.csv` | Read-only comparison with the historical baseline, if Python is available |

Use Windows **Win+Shift+S** to capture the relevant application area and save the image. Avoid unrelated private chats, account details or site data. Raw results remain in private custody until separately reviewed for publication.

## Have the lead establish the safe power state

Follow [intake](../START-HERE.md), [safety](../SAFETY.md) and [the connector tables](../docs/03-wiring-and-power.md). Every propeller must be removed. Physically isolate ESC propulsion and Pi power. The lead must identify J12 POWER1, verify regulated supply/polarity and the received wiring, insulate/secure FC2 and inspect for post-impact damage.

Do not learn polarity measurement by experimenting on the connected drone. This FC's USB does not provide its main power, and raw 6S must never enter POWER1. If the correct article, connector, voltage or supply arrangement is uncertain, record **HOLD** and ask the assigned electrical/FC lead to resolve it.

## Connect and identify the FC without motor power

1. With the approved regulated FC supply on, keep the board stationary for startup. Connect a known USB data cable from FC to laptop.
2. Right-click Windows Start and open **Device Manager**. Expand **Ports (COM & LPT)** if present. Identify the device that appears with the FC connection; record its COM number. A missing or warning-marked device needs power/cable/driver diagnosis. COM6 in an old screenshot is not a required assignment.
3. In Mission Planner, select that COM port and the recorded USB connection setting **115200**, then **Connect**. Wait for parameters to finish downloading.
4. Open **DATA**. The blue/ground attitude display is the **HUD**. Confirm it is updating and shows **DISARMED**. The final intended mode is **Stabilize**. The top-right connection button should show **Disconnect** while connected; a disconnected screen can retain old values.
5. Select **Messages** below the HUD and record fresh startup entries and firmware identity. The historical banner is SALFCGAMUDA / ArduCopter 4.7.1. A different banner is an investigation item, not a reason to overwrite it.
6. Do not arm. A zero battery readout is expected when `BATT_MONITOR=0`; it is not a measurement of pack condition. No external GPS/compass was reported installed. Fresh sensor warnings still require the [sensor procedure](../docs/05-sensors-and-orientation.md), not bypassed checks.

## Save and compare before changing anything

1. Open **CONFIG → Full Parameter List** or **Full Parameter Tree**. Clear filters and wait for the full read.
2. Choose **Save to File** and save the fresh `.param` in the private session folder. Do not use **Load from File** or **Write Params** for this backup.
3. The historical reference is `config/historical-fc2-snapshots/FC2_stick_control_working_2026-10-21.param`. It has 945 entries and device-specific calibration. Its filename does not prove today's hardware state.
4. For a numeric comparison, open PowerShell in the handover root. With the example private folder beside that root, replace both date placeholders below, then run:

   ```powershell
   python tools/compare_parameters.py --current "..\FC2-intake-YYYY-MM-DD\FC2_incoming_readback_YYYY-MM-DD.param" --output "..\FC2-intake-YYYY-MM-DD\parameter-comparison.csv"
   ```

5. Open the CSV in a text editor or spreadsheet. It lists added, missing and numerically changed entries. Equal forms such as `1` and `1.0` are not differences. An empty result table means numerical equality, not hardware acceptance.
6. The helper only reads parameter files and creates the explicitly requested new CSV outside the repository. It has no hardware connection and does not apply changes. If the output already exists, choose a new filename. For another baseline, use `--baseline` with its path; `--help` lists options.
7. The FC lead must explain configuration differences. Startup offsets, pressure and counters can change; another device's calibration must not be copied to make the CSV empty. Changed motor functions, receiver settings, arming controls or estimator sources need particular attention.

On Windows, a file hash can be recorded with `Get-FileHash -Algorithm SHA256 -LiteralPath "path-to-the-export.param"`, replacing the example with the real file. Keep the original export unchanged.

## Finish the first session

Save the messages, comparison and notes. Select **Disconnect** in Mission Planner, remove USB, switch off the regulated FC supply and verify the hardware is off. Complete the session header and relevant pending rows in [acceptance](ACCEPTANCE.md), then assign unresolved items from [the issue register](OPEN-ISSUES.md). No motors should have moved in this session.

## Progress to controls and motors in order

| Session or gate | Procedure | Result required before moving on |
|---|---|---|
| FC sensors | [Sensors and orientation](../docs/05-sensors-and-orientation.md) | Both IMUs/barometer, correct physical axes, repeatable startup and warning disposition |
| Receiver link | [Receiver](../docs/06-receiver.md) | Fresh radio inputs, preserved firmware/settings and loss/recovery record with propulsion isolated |
| Pilot controls | [Controls](../docs/07-controls-and-calibration.md) | CH1–CH4 physically verified, low throttle, RC6 unused, stick arm/disarm and software command response with ESC power disconnected |
| Propulsion | [ESC and motors](../docs/08-esc-and-motors.md) | Approved supply/ESC rating and inspection, then separate A/B/C/D position/direction/stop checks and only a brief no-prop throttle response |
| Remaining development | [Continuation gates](../docs/14-continuation-plan.md) | Assigned battery/failsafe, navigation, Pi/perception and telemetry acceptance |

If an arm request is rejected, read the newest timestamped message and stop at that issue. Do not enable old RC6 functions, guess a safety-button setting, force-arm or disable an IMU. The original private evidence and firmware still need the [separate custody transfer](CUSTODY.md). No step in this walkthrough authorizes flight.
