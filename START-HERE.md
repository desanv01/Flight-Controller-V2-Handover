# First day with the FC2 drone prototype

The purpose of the first session is to identify the hardware, preserve its state and establish safe telemetry. **Do not try to make the motors spin on your first connection.** Read [safety](SAFETY.md) before handling the battery or power supplies.

## Before touching the hardware

1. Nominate an incoming technical lead and a second observer. A beginner can inspect documentation and telemetry; live power and propulsion work needs someone competent with LiPo batteries, electronics and multirotors.
2. Read [current status](CURRENT-STATUS.md), [equipment](handover/EQUIPMENT.md) and [open issues](handover/OPEN-ISSUES.md).
3. Disconnect the flight battery, USB and external supplies. Confirm all LEDs extinguish. Remove **every propeller** and store them away from the test area.
4. Separate and label the healthy-test article **FC2** and any earlier **FC1** with the reported INS/heating fault. Do not exchange them without a new qualification record.
5. Photograph the received arrangement before unplugging harnesses. Record frame nose, FC top, mounting, all connectors, regulator settings and capacitor markings. Do not infer wire functions from colour.
6. Complete the [custody form](handover/CUSTODY.md). Missing equipment or an unknown connector is a hold, not a reason to guess.

## Prepare the workstation

1. Keep this handover folder intact. Use relative links and do not rename evidence files independently of the index.
2. Preserve its original copy before editing procedures. Run the read-only validation command in [inventory](inventory/README.md) if Python is available.
3. Obtain Mission Planner from its official source. The recorded ground station is **1.3.83**, while the FC runs **ArduCopter 4.7.1**. They are different programs and version numbers.
4. Do not install generic H743 firmware. Do not load a parameter dump. Do not update the receiver merely because a newer version exists.
5. Create a dated session folder outside the archived snapshots for new photos, a parameter export, startup messages and measured values. Record actual tool versions.

## Establish a non-propulsion connection

Only after a competent person has verified the supply and harness:

1. Electrically disconnect ESC propulsion power and keep the Pi branch disconnected. Software DISARMED is not isolation.
2. Secure FC2 on insulated supports in its intended orientation. Prevent loose wires or carbon fibre from touching the underside.
3. Verify regulated POWER1 voltage and polarity **before** connecting the FC. POWER1 is not a battery input. See [power](docs/03-wiring-and-power.md).
4. Power FC2 from the approved regulated branch and keep it stationary during startup.
5. Connect the FC USB data cable. This FC's USB does **not** provide its main power.
6. Follow [Mission Planner connection](docs/04-mission-planner.md). Identify the actual COM port, not a remembered COM6 assignment.
7. Export all live parameters before any change. Save startup messages and the displayed firmware identity.
8. Compare the fresh export with the historical 21 October snapshot. Differences must be understood before declaring that the handed-over state is reproduced.
9. Check for fresh sensor, power and radio warnings. Do not arm to see whether a warning goes away.
10. Disconnect Mission Planner, remove USB and turn off regulated power. Record the session result and unresolved items.

## What success means on day one

- Correct physical board and harnesses identified.
- No propellers fitted; propulsion and companion power isolated.
- Safe regulated supply independently checked.
- Fresh firmware identification, parameter backup and startup messages saved.
- No unexpected heating or resets during the limited observation.
- Issues assigned to an owner rather than worked around.

This completes intake, not flight approval. Continue through the gated [plan](docs/14-continuation-plan.md).
