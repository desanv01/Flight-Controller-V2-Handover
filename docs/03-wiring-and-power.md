# Wiring and power boundaries

All pin numbers below are **schematic/footprint pad numbers**, not an unspecified left-to-right photograph view. Mating-face and wire-entry views are mirrored. Verify molded cavity markings, PCB pad numbering and end-to-end continuity with all power disconnected.

The [copied public connector tables](../references/v2-design/docs/connector-pinouts.md), [MCU resource map](../references/v2-design/docs/pin-mapping.md) and the matched physical article must agree. Do not apply V1, generic Pixhawk or older reference-board wiring.

## FC power and debug

| Connector | Pin | Function | Boundary |
|---|---:|---|---|
| J12 POWER1 | 1 | Regulated +5 V rail input | Design basis 5.2 V nominal, never VBAT |
| J12 POWER1 | 2 | GND | Supply return |
| J3 SWD | 1 | 3.3 V target reference | Programmer voltage sense, not BEC input |
| J3 SWD | 2 | SWDIO | Debug data |
| J3 SWD | 3 | SWCLK | Debug clock |
| J3 SWD | 4 | GND | Debug reference |

The FC input design requirement is 4.9–5.5 V at its pads under load, with 3 A continuous and 4 A/100 ms transient **design targets**. These are not measured FC current draws, and not the Pi's permitted supply range. The FC's USB VBUS is not its main supply. Connect independent regulated POWER1 for USB communication.

The recorded J12 header is Molex **105311-1202**. The documented mating housing is **105307-1202**, terminals **105300-2200**, TPA **105325-1002**. The short harness concept uses 22 AWG copper, about 100 mm with a 150 mm EVT1 maximum target and strain relief. Recheck the exact contact/crimp tool and assembly; part names do not certify workmanship. See the [harness reference](../references/v2-design/fabrication/pcbway/harness/POWER1_Harness_Drawing_and_Instructions.md).

## Receiver J7

| J7 pin | FC function | Receiver pad |
|---:|---|---|
| 1 | Regulated +5 V | Supply, only when its verified rating permits this rail |
| 2 | FC RX, PD9 / USART3 | Receiver TX |
| 3 | FC TX, PD8 / USART3 | Receiver RX |
| 4 | GND | GND |

This is **SERIAL2**, not the Pi port. The original receiver cable used unconventional colours; colour-based assumptions are unsafe. Preserve a qualified harness rather than swapping TX/RX again without diagnosis.

## ESC J6

| J6 pin | Net | Cable treatment |
|---:|---|---|
| 1 | NC | Empty |
| 2 | GND | ESC signal ground |
| 3 | NC | Empty |
| 4 | NC | Empty |
| 5 | M1 output / PE14 | ESC signal input for FC output 1 |
| 6 | M2 output / PE13 | ESC signal input for FC output 2 |
| 7 | M3 output / PE11 | ESC signal input for FC output 3 |
| 8 | M4 output / PE9 | ESC signal input for FC output 4 |

This is a **five-wire signal-only interface**. No battery, 5 V or current-sense wire belongs in its unused cavities. J6 M1/M2/M3/M4 net names identify electrical outputs; the latest `SERVOx_FUNCTION` permutation assigns them different logical motor numbers. See [motor mapping](08-esc-and-motors.md).

## Companion and external navigation

| Connector | Pins | MCU / ArduPilot mapping |
|---|---|---|
| J11 companion | 1 NC; 2 FC RX; 3 FC TX; 4 GND | PB15 RX / PB14 TX, USART1, **SERIAL7** |
| J4 external GNSS | 1 GND; 2 FC TX; 3 FC RX; 4 SDA; 5 SCL; 6 regulated +5 V | UART8 **SERIAL6**, PE1 TX / PE0 RX; I2C4 PB7 SDA / PB6 SCL |

J11 cannot power the Pi. UART signals are nominal 3.3 V logic, not RS232 levels. The source mapping is verified from the copied netlist and target; hardware wiring and successful runtime data exchange still need tests. Leave unneeded VTX, DJI and CAN connectors unused rather than treating them as spare safe power outputs.

## BEC and battery

The Matek BEC12S-PRO accepts **9–55 V DC**, selects **5.2 V default / 8 V / 12 V**, supports up to **5 A continuous**, **9 A peak**, and has **no reverse-input protection**. The 6S pack is within its input range, but this says nothing about the downstream ESC rating. Manufacturer reference: [Matek BEC12S-PRO](https://www.mateksys.com/?portfolio=bec12s-pro).

Verify selection and actual output before connecting a load. Neither increasing the setting to 8/12 V nor buying a larger battery is a remedy for a Pi boot problem. A 5 A output is shared by every device on that BEC and depends on the real power path and thermal conditions. Do not assume there are two BECs merely because the architecture needs separately qualified branches.

## Safe harness qualification

1. Disconnect battery, USB, bench source and programmer; check that LEDs extinguish.
2. Identify connector numbers from exact source and physical keying. Draw both ends with a specified viewing direction.
3. Continuity-check each conductor; record actual origin and destination pin, not just colour.
4. Check adjacent cavities and supply-to-ground for accidental shorts. Capacitor charging can change resistance readings; do not invent a universal populated-board pass resistance.
5. Inspect solder/crimp joints, exposed strands, insulation, strain relief and clearance from carbon fibre.
6. With the load disconnected, verify source voltage and polarity at the intended mating pins.
7. Have the electrical lead approve the harness and protection. Connect only while power is off.
8. Measure at the load under startup and intended operation, recording instruments and conditions. Check temperatures and resets as well as voltage.

The original safety and power drawings are retained locally as historical illustrations. Their representative component shapes, unspecified views or depicted protection boards are not physical wiring authority.
