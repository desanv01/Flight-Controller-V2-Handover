# Receiver and ExpressLRS handover

The established path is **RadioMaster T8L → ELRS radio → CYCLONE-labelled receiver → CRSF UART → FC2 SERIAL2**. The receiver does not directly drive the four ESC motor inputs.

## Preserve the working identity

| Item | Recorded value |
|---|---|
| Receiver PCB marking | CYCLONE ELRS 2.4G NANO |
| Installed target banner | BETAFPV 2.4GHz Nano RX |
| ExpressLRS version | 3.5.6 |
| Commit / domain | ee188b / ISM2G4 |
| Firmware platform | Unified_ESP8285_2400_RX |
| Receiver output selected during setup | Ordinary CRSF, UART baud 420000 |
| FC port | J7, USART3, SERIAL2 |

The banner identifies the installed firmware configuration, not independently the receiver's manufacturer. Do not flash a target chosen only from appearance. The exact current transmitter RF version/configuration export has not been preserved in this package as a verified final artifact; obtain it before any reflash/rebind operation.

## Inspect the receiver Web UI only when needed

First isolate propulsion, keep the T8L off and power the receiver from its verified FC supply. The recorded Wi-Fi auto-on interval was about 30 seconds. If it starts an ExpressLRS RX access point, connect despite the no-Internet warning; the default password is `expresslrs` and AP address is `http://10.0.0.1`. A configured home network can change access behaviour.

Record the banner and current Model/Options pages. In the recorded 3.x UI, persistent binding storage, ordinary CRSF and 420000 baud were the intended receiver setup; AirPort and Model Match were not used for initial setup. Do not reset, upload firmware, replace binding information or change home Wi-Fi just to inspect identity. A blank binding-phrase entry is normal and does not show that binding data is absent. “Bound” indicates saved binding information, not a live RF connection while in Wi-Fi mode.

If the preserved configuration already works, leave it unchanged. If inspection reveals a difference, save evidence and agree on a specific change before editing. Firmware flashing or rebinding is separate work requiring the correct target and both sides' versions.

## Verify FC settings without disturbing calibration

The historical final file contains:

```ini
SERIAL2_PROTOCOL = 23
SERIAL2_OPTIONS  = 0
RC_PROTOCOLS     = 512
RC_OPTIONS       = 8224
RSSI_TYPE        = 3
SERIAL2_BAUD     = 57
```

`8224` retains the existing bit 5 throttle-idle arming requirement and bit 13 ELRS 420 kbaud selection. If another reviewed installation has additional appropriate bits, preserve them rather than blindly replacing the bitmask. Do not change the FC baud parameter to 420000: ArduPilot manages serial-RC baud behaviour. Confirm the actual values after a full FC/receiver power cycle.

The [J7 harness](03-wiring-and-power.md) uses crossed signal directions and common ground. Receiver TX goes to FC RX. Do not troubleshoot missing stick data by changing the Pi's SERIAL7 port or the ESC output protocol.

## Link acceptance with no propulsion power

1. Turn the transmitter on with throttle fully low. Start FC/receiver together and allow initialization without movement.
2. Connect Mission Planner and confirm fresh changes on all four intended axes. Follow [calibration](07-controls-and-calibration.md) for physical mapping and endpoints.
3. Record receiver/link indicators and current messages; a blue LED by itself is not full control acceptance.
4. Keeping the aircraft disarmed and ESC power isolated, switch off the transmitter and wait. Record radio-loss indication or log evidence; frozen channel bars alone are ambiguous.
5. Restore the transmitter with throttle low. Confirm fresh input changes return and inspect mode/arming state rather than assuming automatic recovery.
6. Perform a deliberate full FC/receiver power cycle and verify automatic link recovery, calibration persistence and low-throttle input again.

This preliminary test checks loss detection/recovery. The selected **armed** failsafe action still needs separate approval and a propulsion-isolated test; it is not proven by a disarmed screen. No GPS means the stored RTL preference does not establish geographic return home.

References: [ArduPilot CRSF/ELRS](https://ardupilot.org/copter/docs/common-tbs-rc.html), [ExpressLRS Web UI, use the 3.x section](https://www.expresslrs.org/quick-start/webui/), [radio failsafe](https://ardupilot.org/copter/docs/radio-failsafe.html).
