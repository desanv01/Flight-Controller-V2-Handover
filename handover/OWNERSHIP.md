# Responsibilities and subsystem handoffs

This handover covers Desan Vasu's FC adaptation/bring-up, receiver and Mission Planner work, and the final integration interfaces he handled. It preserves original upstream authorship and external fabrication. It does not assign authorship or completion of all ESC, Pi or sensor work to one person.

Incoming owners are **roles awaiting named assignment**, not presumed existing personnel. An engineer may fill several roles only if competent for each responsibility.

| Role | Accountable scope | Required handoff or acceptance |
|---|---|---|
| Project/technical lead | Overall state, architecture, change approval, risk and test coordination | Named owners, custody, gate acceptance, bounded test plans |
| FC/firmware lead | Board identity, power interface, firmware, sensors, outputs, estimator, parameter management | Fresh read-back, sensor logs/orientation, known build selection and recovery plan |
| Receiver/control lead | RF identity, binding custody, physical axes, calibration, arming controls and RC-loss detection | Transmitter/RX config record, joint stick/display recording, recovery evidence |
| ESC lead | ESC hardware/firmware, supported DShot commands, motor phase drive, electrical ratings | Exact board/version/export, voltage/current/capacitor/protection approval, motor mapping |
| Electrical/power lead | Battery, distribution, regulators, protection, harnesses, measurements and monitoring | Signed wiring tables, startup/load/thermal evidence, battery-sensing qualification |
| Pi/software lead | OS/storage, camera, HAT, LiDAR driver, application/service lifecycle and logs | Reproducible software/configuration and sensor/power acceptance |
| Navigation lead | GNSS/compass or alternative localization, estimator sources, mode limitations | Architecture decision and navigation-specific acceptance |
| Mechanical/flight-test lead | Mounting, damage, mass/CG, motor/prop pairing, site/pilot/flight readiness | Inspection and separate supervised test plan |
| Documentation/release owner | Provenance, immutable evidence, redaction, licensing and public allowlist | Reviewed publication candidate, not a raw local-folder upload |

## FC to ESC contract

FC lead supplies J6 output/ground contract, current permutation and DShot configuration. ESC lead supplies accepted logic/command behaviour, exact firmware/configuration and power-stage limits. They jointly sign actual A/B/C/D motor positions/rotation and stopping behaviour. FC parameter values alone cannot accept ESC ratings or motor thrust.

## FC to receiver contract

FC lead owns SERIAL2/CRSF interpretation; radio lead owns transmitted axis/switch behaviour and binding. Both confirm full-axis directions, low throttle, final stick-arming setup and loss/recovery. Do not infer a transmitter button's momentary/latching behaviour from its shape.

## FC to Pi contract

FC owns stabilization, outputs, arming and failsafe. Pi owns perception/application data. Electrical lead signs independent power and signal levels. Begin with telemetry. Before accepting control-affecting data, jointly define units, frames, timestamps, rates, staleness, invalid-data rules, loss behaviour and pilot takeover. A Pi crash must not defeat FC control.

## Outgoing contributor information still helpful

Confirm that the final saved profile still describes the physical article left behind; identify the last successful physical throttle test and any available logs; help recover photos and actual component labels; and identify departmental code/configuration owners. These confirmations should add evidence, not backdate unperformed tests or turn reported results into measured acceptance.
