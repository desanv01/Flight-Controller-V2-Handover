# Establish a telemetry only FC to Pi connection

The companion link was planned, not accepted as working. First qualify Pi power and the FC separately. Keep props removed, ESC power isolated and the laptop disconnected from any FC USB port needed by the Pi. The first milestone is reliable **telemetry reception**, not arming or offboard control.

## Prefer USB for the first diagnostic link

1. Start the Pi from its known-good independent supply and FC2 from qualified POWER1. The FC still needs regulated power because its USB is data-only.
2. Check that the cable does not create an unintended alternate power path. Use a known USB data connection from Pi USB-A to FC USB-C; do not connect two hosts to the same FC USB port.
3. On the Pi, inspect actual device paths:

   ```sh
   ls -l /dev/serial/by-id/
   ```

4. Record the matching stable device path and permissions. Do not assume `/dev/ttyACM0` will always be this FC.
5. Use the Pi team's reviewed MAVLink client/environment to receive a heartbeat and log identity/attitude/status. Only one process should own the port; use a reviewed router if multiple consumers are needed.
6. Confirm reported vehicle/autopilot identity and fresh timestamps. Check continuous telemetry through deliberate cable reconnect and independent restarts, without motor power.
7. Confirm companion restart/loss does not reset the FC or change arming state. Save logs, port configuration, software versions and power observations.

No application or virtual environment is invented as already installed. The source team must supply its code and dependency record, or the incoming team must create and verify a new minimal telemetry client under change control.

## UART alternative after the electrical review

The matching netlist and `SERIAL_ORDER` establish J11 as **USART1 / SERIAL7**, not SERIAL2:

| FC J11 pad | FC signal | Pi destination if its GPIO14/15 UART route is deliberately configured |
|---:|---|---|
| 1 | NC | Leave empty |
| 2 | PB15 / FC RX | Pi TX, physical 8 / BCM14 |
| 3 | PB14 / FC TX | Pi RX, physical 10 / BCM15 |
| 4 | GND | Verified Pi ground |

This table is source-derived and conditional on a verified Pi UART route and mating orientation. It is not proof of an installed harness. Use 3.3 V TTL signals, not RS232 or a 5 V USB-serial adapter. No power wire connects the two regulators.

The final FC2 snapshot has `SERIAL7_PROTOCOL=-1`, `SERIAL7_BAUD=57`, `SERIAL7_OPTIONS=0`: **the planned UART is not enabled** in that saved configuration.

For a future approved UART test, after backup and harness qualification, the intended starting FC configuration is MAVLink2 on SERIAL7 (`SERIAL7_PROTOCOL=2`, `SERIAL7_BAUD=115`, `SERIAL7_OPTIONS=0`). Read back after restart. These are **planned changes**, not part of the preserved baseline. Keep receiver SERIAL2 unchanged. USART1 is configured NODMA, so do not begin with an arbitrarily high generic baud.

On Pi 5, do not assume `/dev/serial0` routes to the 40-pin GPIO UART: it may identify the separate debug interface. Identify the installed OS overlays and actual pins, remove any login console from the intended UART through a reviewed configuration, restart, and document the resolved device. Refer to [official UART configuration](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-uarts), not a Pi 3 recipe.

## Data contract before command authority

The FC owns attitude stabilization, motor waveform generation, arming and failsafe. Define message IDs, rates, frame conventions, units, timestamps, staleness timeouts and invalid-data handling before sending perception/proximity data. Camera boxes or an 8×8 range frame are not automatically a supported navigation input.

Before any autonomy, separately review position/yaw sources, flight modes, pilot takeover, RC loss, companion loss, malformed/stale inputs and command permissions. No script in this package requests arming, takeoff, parameter writes or actuator commands. [ArduPilot companion-computer reference](https://ardupilot.org/dev/docs/companion-computers.html).
