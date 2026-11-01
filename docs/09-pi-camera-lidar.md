# Raspberry Pi camera LiDAR and AI HAT handover

The recorded compute hardware is **Raspberry Pi 5 8 GB**, **AI HAT+**, **IMX708 camera** and one intact **VL53L5CX-SATEL**. Older CM5 and custom-camera/custom-LiDAR proposals are not the confirmed hardware for this bench setup. No complete OS/application image or accepted combined-system data set has been identified here.

## Current fault and what is established

The outgoing contributor confirmed that the bare Pi boots from the USB-C reference supply. With BEC power, the reported pattern was red, briefly green after pressing the button, then red again; the HAT LED also changed. The last stated header feed was BEC OUT to **physical pin 4**, GND to **physical pin 14**, not BCM GPIO4/GPIO14. Simultaneous BEC and USB-C powering was explicitly denied.

These are valid 5 V/GND rails, but cable/contact current capability, actual loaded voltage and the current assembled harness were not measured in the supplied results. A red Pi 5 LED can indicate standby; it is not a measurement of insufficient current or proof of a dead board. The HAT LED colour alone is not a diagnosis.

## Power diagnosis in a controlled sequence

1. Disconnect all power and isolate FC/ESC branches. Remove the HAT, its PCIe ribbon, camera ribbon and **all** LiDAR wires. Leave Pi, known OS microSD, cooler and display.
2. Keep the BEC output physically disconnected. Repeat the known-good official USB-C supply boot, recording the display and storage used. Give the button one brief press if needed; do not hold it through startup.
3. Shut down and remove USB-C. Check battery/BEC input polarity and selected 5.2 V output with the Pi disconnected.
4. Have the electrical lead inspect a current-rated, protected, short, strain-relieved power harness and header/stacking contact path. Ordinary thin Dupont jumpers must not be assumed suitable for a 5 A power path. Do not require both 5 V pins merely to make a bare Pi boot; qualify the actual contact arrangement.
5. Connect only with power off. Measure at BEC output and at the Pi input during the attempt using preattached insulated test leads. Record unloaded/startup/steady values and any resets; a DMM can miss brief dips.
6. If BEC output falls, investigate input wiring, overload, shorts, regulation/protection and heat. If BEC stays stable but Pi input falls, investigate wires/connectors/stacking header. If Pi input is stable yet boot fails, inspect HDMI diagnostics, boot media and board/firmware state.
7. Once bare-Pi BEC boot is repeatable, add one peripheral at a time with complete power-off between changes. Repeat voltage, temperature and reset observations for each step.
8. Qualify the final expected processing workload and thermal arrangement, not just an idle desktop. Record headroom; Pi, HAT, camera, sensor and other loads share the regulator's total rating.

Do not increase to 8/12 V, power from two sources, or set software current overrides to conceal an unqualified supply. A GPIO feed has no USB-PD negotiation. The recommended 5 A supply capacity is not a constant 5 A Pi load. USB current-limit configuration cannot repair cable drop or a short. [Raspberry Pi power reference](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html).

## Camera commissioning after power passes

Use the correct **15-to-22-pin camera cable** between the IMX708 unit and a Pi 5 CAM/DISP connector. The camera is not wired to the GPIO power/I2C harness in this setup. Verify contact orientation for the actual cable/socket; do not infer it from the blue stiffener colour alone. Open and latch the connectors only while all power is removed.

On the known installed OS, the Pi lead can collect:

```sh
cat /etc/os-release
uname -a
command -v rpicam-hello
rpicam-hello --list-cameras
```

These are diagnostic commands, not confirmation that the program is installed. If available, make a short preview/capture using the installed supported camera stack and verify a real image, autofocus behaviour, orientation and timestamps. Keep original captures local until privacy approval. Do not enable the deprecated legacy camera stack for IMX708. See [official camera software](https://www.raspberrypi.com/documentation/accessories/camera-software.html).

## AI HAT commissioning

Record whether the actual HAT+ is the 13 or 26 TOPS variant, the PCIe ribbon orientation, standoffs/cooler clearance and power path. **AI HAT+ is not AI HAT+ 2.** Use the manufacturer's instructions matching that exact product and OS; preserve kernel, Hailo driver/runtime, firmware and model/HEF versions together. First prove device enumeration, then an official sample workload, then the intended camera model. No successful inference benchmark is asserted in this handover. [Official AI HAT guide](https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html).

## LiDAR wiring is a separate acceptance gate

The historical harness was for an intact ST PCB4109A SATEL, not the snapped-off sensor section. ST documents at least variant **00B with onboard LDO** and **01B with externally supplied AVDD**. The exact received variant and bridges must be photographed and checked before energizing its power/control pins. An intact-looking board alone does not settle all supply details.

Known Pi-side signal positions, **only after that electrical review**, are physical pin **3 = GPIO2/SDA**, **5 = GPIO3/SCL**, **1/17 = 3.3 V** and a verified ground. These are not a complete SATEL power harness. The historical conditional resistor network and full J1 map are retained in the private engineering archive. They are not an accepted harness. Obtain that record through the project custodian if needed; the incoming sensor lead must still verify the actual SATEL variant and produce the signed wiring table below.

The incoming sensor lead must produce a revised, signed table of exact SATEL connector pin, net, permitted voltage, pull network, Pi physical pin and viewing direction. Never put 5 V on Pi I2C/GPIO or IOVDD. Verify against the [ST schematic](https://www.st.com/resource/en/schematic_pack/vl53l5cx-satel-schematics.pdf); use the correct variant. Until this is done, **keep the LiDAR harness disconnected**.

After approved wiring and power, enable the intended I2C interface and use a bus scan only as a connection clue. The sensor's usual address is 0x29 in 7-bit notation; this alone does not prove ranging. A working Pi 5 driver/platform layer must load firmware and report timestamped distances, valid-target/status fields, frame rate and errors. Do not invent an unverified pip package or assume an older Pi platform example is a completed Pi 5 port.

Validate known targets, invalid/no-target cases, lens obstruction, disconnection, stale frames and CPU load. Invalid or all-zero data must not mean “clear space.” Start with one sensor; multiple same-address units require a reviewed addressing/power-control scheme. No multi-sensor solution or obstacle-avoidance acceptance exists yet.

## Files the Pi lead must supply

Record OS image/version and storage backup; application repository/commit and dependency lock; service/autostart definitions; actual GPIO/UART/I2C configuration; HAT software/model versions; camera and LiDAR test outputs; power measurements; timestamp conventions; and procedures for stop, restart and failure recovery. Do not put Wi-Fi credentials, SSH keys or a raw private SD image in a public repository.

Next link: [FC to Pi telemetry](10-fc-pi-mavlink.md). Keep perception and navigation commands disabled until their safety contract is reviewed.
