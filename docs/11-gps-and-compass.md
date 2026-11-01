# GPS compass and battery monitoring continuation

The released assembly has IMUs and a barometer, but no fitted GNSS receiver or magnetometer. The outgoing contributor reported no external GPS/compass module. A connector labelled GPS is an interface for external hardware, not a sensor.

## Can the aircraft operate without them

Some manually piloted non-position modes can operate without GPS and a compass when the firmware, estimator, available sensors and checks support the arrangement. That does **not** make this prototype ready to fly. Stabilize does not supply position hold or a geographic return-home function. This project's planned higher-level navigation/perception features need an explicitly qualified navigation solution; object detection and range measurements alone do not replace it.

The current no-compass settings were used for a **propeller-free bench profile**: `COMPASS_ENABLE=0`, `COMPASS_USE/USE2/USE3=0`, `EK3_SRC1_YAW=0`. Do not convert them into a flight recommendation or turn off all pre-arm checks. The target permits a no-compass arrangement, but no absolute-heading/navigation qualification was completed.

## Select hardware before configuration

The incoming navigation lead should select a documented UART GNSS plus supported I2C compass, or deliberately review another supported architecture. Record exact model/revision, supply range, signal levels, connector pinout, firmware support, intended mounting and interference separation. A six-pin plug is not a cable-compatibility guarantee. No purchase or selected replacement module is implied by this handover.

## J4 is SERIAL6 in this custom target

| J4 pad | Function | External device connection |
|---:|---|---|
| 1 | GND | GND |
| 2 | FC UART8 TX / PE1 | GNSS RX |
| 3 | FC UART8 RX / PE0 | GNSS TX |
| 4 | I2C4 SDA / PB7 | Compass SDA |
| 5 | I2C4 SCL / PB6 | Compass SCL |
| 6 | Regulated +5 V rail | Module supply only if its exact rating permits |

Verify pad/cavity numbers and viewing direction with power off. The 5.2 V rail and 3.3 V signal compatibility both matter. Do not assume a generic “GPS uses SERIAL3” tutorial applies.

## Planned commissioning sequence

1. Preserve the current profile and verify supply, continuity and common ground with propulsion disconnected.
2. Approve the exact module and adapter harness. Locate it away from battery/ESC currents, magnets and steel.
3. Configure its actual UART and protocol according to the selected device. A conventional approved u-blox UART arrangement would start with `SERIAL6_PROTOCOL=5`, `SERIAL6_OPTIONS=0`, automatic first GPS detection/configuration and no second GPS. These are **conditional future changes**, not settings to apply while no module exists.
4. Review unused GPS assignments on other serial ports without disturbing SERIAL2. Keep a before/after diff and read-back.
5. Fully power-cycle FC/module and establish detected GPS and a real compass device entry before calibrating. Do not invent device IDs.
6. Test GPS outdoors with a suitable antenna sky view. Record detection, fix, satellites, HDOP, plausible position and time to acquisition across starts. “No GPS” differs from a detected GPS with no fix.
7. Configure the intended estimator yaw source and compass use for the selected hardware, then perform standard compass calibration away from metal, magnets and powered current loops. Do not blindly copy the old bench's disabled-compass settings.
8. Restart and confirm detection, calibration persistence, heading response and receiver operation. Test in the final mounted layout; motor-current interference remains a later controlled acceptance item.

A GPS-only module will not automatically provide a compass. If only one half works, troubleshoot its UART or I2C path separately. Relaxing calibration fitness cannot repair absent hardware.

## Battery monitoring is also unfinished

`BATT_MONITOR=0` means the FC has no qualified flight-pack voltage/current source. The HUD's zero is not a pack-voltage measurement. The regulated FC rail is not a proxy for battery state, and J6 does not provide battery/current sensing. Do not connect 6S to an ADC or guess ADC parameter pins.

Select a reviewed supported sensing path: an approved power module, qualified ESC telemetry if truly supported, or a designed measurement interface with protection and calibration. Check the actual CAN/UART connector and supply contract; this custom board is not a standard Pixhawk power connector. Compare measurements against instruments across relevant loads, then define/test low and critical actions appropriate to the aircraft and available navigation. Record sensor identity, scale factors and evidence before enabling flight protection claims.

References: [GPS installation](https://ardupilot.org/copter/docs/common-installing-3dr-ublox-gps-compass-module.html), [compass setup](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html), [compass calibration](https://ardupilot.org/copter/docs/common-compass-calibration-in-mission-planner.html), [battery monitoring](https://ardupilot.org/copter/docs/common-power-module-configuration-in-mission-planner.html).
