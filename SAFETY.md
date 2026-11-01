# Safe bench work and stopping conditions

This is an unfinished engineering prototype with a high-energy battery, custom electronics and exposed rotating machinery. Documentation does not certify the assembled article. Work must be supervised by a competent electronics/multirotor engineer.

## Nonnegotiable boundaries

1. **Remove all four propellers before any configuration, calibration, arm/disarm or motor bench test.** A restrained aircraft with propellers is not an acceptable substitute. Historical footage with fitted props is incident evidence, not a demonstration to repeat.
2. Physically disconnect propulsion power for software, radio and sensor checks. DISARMED, a low throttle value and a USB disconnect are not electrical isolation.
3. A standard 6S LiPo is **25.2 V fully charged**, not merely 22.2 V. The exact custom ESC, capacitor, connectors and wiring must be approved for the actual voltage and transients before use. Earlier rotation does not prove that approval.
4. Never connect raw battery voltage to FC POWER1, receiver power, Pi 5 V, 3.3 V, UART or I2C pins.
5. Use separate qualified branches for FC and Pi. Common signal ground does not authorize joining two regulators' positive outputs. Do not simultaneously power the Pi through its header and a USB-C supply.
6. FC USB is data/debug only. ST-Link VTref senses the target voltage; it is not permission to power the board through its 3.3 V debug pin.
7. Keep electronics and joints insulated from conductive carbon fibre and metal. Secure loose boards, motor leads, receiver and battery. Provide strain relief and a clear accessible propulsion disconnect.
8. Do not work on accessible mains terminals. An appropriately qualified person must enclose, earth and protect a mains supply. Hot glue is not mains insulation or a substitute for a proper enclosure.
9. Never force-arm, disable safety checks or suppress a sensor to make a warning disappear. `ARMING_SKIPCHK=0` is retained in the final snapshot.
10. Do not hot-plug camera/PCIe ribbons, sensor wires or regulator outputs. Disconnect **all** power first, including USB and debug leads that may provide alternate paths.

## LiPo and measurement precautions

Inspect the pack for swelling, impact damage, damaged insulation, heat or suspect cells; follow its manufacturer's handling and charging instructions. Capacity is not a discharge-current rating. The 10 Ah pack's C-rating has not been verified. Use suitably rated connectors, conductors, fusing and disconnects selected for the actual branch and inrush by the electrical lead. Do not solder or modify the pack itself.

For voltage checks, attach insulated leads at accessible test points with power off. Use DC-voltage mode and correct meter sockets. **Never connect an ammeter directly across the battery or BEC output.** Do not crowd loose probe tips between live header pins. If measurements cannot be made safely, stop and prepare a proper breakout. A multimeter can miss startup transients; a steady no-load voltage is not qualification.

## Stop immediately for

- Unexpected motor motion, incorrect motor identity or failure to stop.
- Smoke, smell, rapidly increasing temperature or abnormal current.
- Power cycling, collapsing rails, repeated USB disconnects or receiver resets.
- Fresh INS initialization, gyro/accelerometer inconsistency or attitude-axis errors.
- Unverified connector orientation, supply rating, polarity, battery condition or exposed conductors.
- A crash, flip or impact. Disconnect power and inspect before any retest.

Stop by making the test safe and electrically isolating propulsion without reaching through rotating parts. A delayed stick-disarm gesture is **not an instantaneous emergency stop**, and it must not be assumed to cancel Mission Planner's separate Motor Test command.

## Before flight is considered

Resolve the [open issues](handover/OPEN-ISSUES.md), complete the [acceptance gates](handover/ACCEPTANCE.md), select appropriate navigation and battery/failsafe arrangements, and obtain a separate reviewed first-flight plan with trained personnel and applicable site/regulatory approval. No bench checklist in this package authorizes flight.
