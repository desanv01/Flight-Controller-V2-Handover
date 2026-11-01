# Pinned public engineering reference

`v2-design/` preserves the **481 tracked files** of [Flight-Controller-V2 at commit 56c91e283b9ce56b6e43480734feb60e2f078760](https://github.com/desanv01/Flight-Controller-V2/tree/56c91e283b9ce56b6e43480734feb60e2f078760). No nested Git history is bundled. The original repository was not modified to make this handover.

The snapshot includes editable KiCad source/libraries/models, connector and MCU maps, drawings, separate manufacturing variants, historical engineering records, neutral FCV2 firmware, target inputs and build/provenance records. Its original README is [here](v2-design/README.md). All source licensing and attribution remain in place.

Do not combine one manufacturing variant's source with another variant's BOM, placement or Gerbers. Supplier/as-built identity must be established at intake. The private original EVT1/vendor packages are not included; request those separately from the project custodian if the received assembly cannot be reconciled with the public references.

The root status and numbered handover guides govern current continuation. Archived development notes inside the snapshot may include obsolete assumptions, historical workflow restrictions and source-local links. A clean configured EDA report is not physical qualification. The public FCV2 firmware is a different binary from the original recorded SALFCGAMUDA build.

## Official references

These sources were consulted in preparing the consolidated handover on 1 November 2026. Current online documentation can change; use the recorded version and target for parameter interpretation.

- [ArduPilot 4.7.1 pinned source](https://github.com/ArduPilot/ardupilot/tree/dbe792162d06cab66c3475fd5556bf7a120f119e).
- [CRSF and ELRS](https://ardupilot.org/copter/docs/common-tbs-rc.html), [DShot](https://ardupilot.org/copter/docs/common-dshot-escs.html), [motor order](https://ardupilot.org/copter/docs/connect-escs-and-motors.html), [radio failsafe](https://ardupilot.org/copter/docs/radio-failsafe.html).
- [ExpressLRS Web UI](https://www.expresslrs.org/quick-start/webui/); use the 3.x section for the recorded receiver.
- [Matek BEC12S-PRO](https://www.mateksys.com/?portfolio=bec12s-pro).
- [Raspberry Pi hardware and power](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html), [UART configuration](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-uarts), [camera software](https://www.raspberrypi.com/documentation/accessories/camera-software.html), [AI HAT+](https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html).
- [ST VL53L5CX-SATEL schematic variants](https://www.st.com/resource/en/schematic_pack/vl53l5cx-satel-schematics.pdf).

See [notices](../THIRD_PARTY_NOTICES.md) for license boundaries and [source provenance](../inventory/README.md) for portable validation.
