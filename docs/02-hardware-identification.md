# Identify the received hardware

Match the physical test article before using any wiring or firmware. The public design reference contains multiple vendor snapshots and historical experiments; a filename or 3D render is not an as-built inspection.

## Flight controller

The working test article was called **FC2**. Its recorded firmware banner identified **SALFCGAMUDA**, ArduCopter **4.7.1**, source short ID **dbe79216**. The public hardware is a six-layer STM32H743VIT6 adaptation with two IMUs and a barometer.

| Feature | Identify on the received FC |
|---|---|
| MCU | STM32H743VIT6 or approved supply-form equivalent; photograph actual markings |
| Primary IMU | ICM-42688-P, SPI6 |
| Secondary IMU | BMI270, SPI3 |
| Barometer | BMP388, I2C2 |
| Storage | W25Q128-class flash; this target uses dataflash logging, not an assumed microSD slot |
| Input power | J12 POWER1, black two-position Nano-Fit on the projecting tab |
| Debug | J3 white four-position SWD connector; not POWER1 |
| ESC connector | J6 eight-position JST-SH; only ground and four motor signals used |
| Receiver | J7 four-position connector |
| Companion | J11 signal-only UART connector |
| External GNSS | J4 six-position UART and I2C connector |
| Body and mounting | About 40.5 mm square body, 30.5 mm M3 mounting; tab extends overall envelope |

The released assembly does not fit a GPS receiver or compass. Some older schematics show a magnetometer symbol; inspect the released PCB/BOM and real populated board, not a historical symbol. Connector labels do not mean sensors are present.

## Photographs needed at intake

1. Both FC faces square-on and in focus, including silkscreen revision.
2. J12 and its mating cable, cavity numbers and solder joints.
3. Both ends of J6 and J7 harnesses, without disconnecting a powered system.
4. Installed FC top and the marked aircraft nose in the same view.
5. ESC faces, MCU/board markings, main capacitor voltage rating and power input.
6. Motor labels, mounting screws, shafts and phase leads.
7. BEC faces, selection bridges, input/output labels and wiring.
8. Pi, HAT model label, stacking header, PCIe ribbon, camera and both LiDAR faces.

Record any substitutions. Until the source-to-board match is established, the bundled manufacturing packages are engineering references, not proof of the delivered assembly variant.

## Other recorded equipment

| Item | Recorded identity | Still to identify |
|---|---|---|
| Frame | iFlight Chimera7 Pro V2 family | Exact delivered frame/revision and installation geometry |
| Transmitter | RadioMaster T8L | Current handset/RF firmware exports, throttle mechanical arrangement |
| Receiver | CYCLONE ELRS 2.4G NANO marking | Exact hardware manufacturer/target suitability independently |
| Receiver firmware | BETAFPV 2.4GHz Nano RX, ELRS 3.5.6, ee188b, ISM2G4 | Fresh read-back if modified after the recorded session |
| ESC | Custom four-channel board, target reported OPENESC_30_F421, DShot300 | Firmware version/commit/config export and assembled voltage/current rating |
| Motors | Four installed brushless motors | Exact model, KV, pole count, current and propeller compatibility |
| Battery | 6S standard LiPo, 10,000 mAh, 22.2 V nominal, 25.2 V full | Label/C-rating, cell condition, ownership and charging equipment |
| BEC | Matek BEC12S-PRO | Count of physical units, current bridge selection and measured loaded output |
| Bench source | Mean Well LRS-35-12 recorded, 12 V nominal, 3 A | Actual nameplate and protected installation |
| Companion | Raspberry Pi 5 8 GB recorded | Board revision, OS image and storage ownership |
| Accelerator | AI HAT+ | Exact TOPS variant and Hailo software versions |
| Camera | IMX708 / Camera Module 3-type unit | Exact product/lens and ribbon correctness |
| LiDAR | Intact ST VL53L5CX-SATEL, PCB4109A recorded | Regulator variant/bridges and actual connector wiring |

Use [equipment](../handover/EQUIPMENT.md) to assign asset IDs. Quarantine FC1: its earlier INS/heating problem is not resolved by FC2 working.
