# Equipment and software transfer inventory

The following is the recorded equipment baseline, not a physical count performed during compilation. The receiving team should fill asset IDs, quantity, condition, storage location and custodian during intake. Do not treat a proposed part in an old sourcing list as purchased hardware.

| Item | Recorded identity | Quantity or condition to confirm |
|---|---|---|
| FC2 | Custom STM32H743 Rev A / V2 physical test article | One working-session article; inspect and label |
| FC1 | Earlier FC with INS/heating issue | Presence unknown; quarantine if returned |
| Frame | Chimera7 Pro V2 family | One assembled prototype; exact revision and damage check |
| ESC | Custom four-channel, OPENESC_30_F421 target reported | One assembly; exact firmware, revision and rating required |
| Motors | Four brushless motors installed | Record model/KV/poles/condition at each physical location |
| Propellers | Earlier two red props seen installed | Remove/store separately; exact matched set and condition not accepted |
| Transmitter | RadioMaster T8L | Identify asset, RF/handset firmware, battery and controls |
| Receiver | CYCLONE ELRS 2.4G NANO, installed BETAFPV Nano target 3.5.6 | Label hardware, qualified four-wire cable and binding custody |
| Flight battery | Standard 6S 10 Ah, 22.2 V nominal / 25.2 V full | Record actual label, C-rating, connector, cell condition and charger |
| BEC | Matek BEC12S-PRO | Confirm physical count, assignments and output selection; do not assume dedicated units already exist |
| Bench supply | Mean Well LRS-35-12 recorded, 12 V / 3 A | Nameplate, enclosure/earthing/protection and mains competence review |
| Pi | Raspberry Pi 5 8 GB recorded | Revision, microSD/OS and successful USB-C reference setup |
| AI board | Raspberry Pi AI HAT+ | 13/26 TOPS variant, PCIe cable, standoffs/cooling |
| Camera | IMX708 / Camera Module 3-type | Model/lens, 15-to-22 camera cable and case/mount |
| Range sensor | ST VL53L5CX-SATEL intact PCB4109A | Exact supply variant/bridges, harness and resistor network |
| FC input harness | J12 Nano-Fit mating set | Cavity markings, continuity, crimp/solder/strain relief |
| ESC harness | Eight-position J6 with five conductors used | Ground + outputs only; no power in unused cavities |
| Debug | STLINK-V3SET recorded | Exact adapter and labelled SWD/VTref cable |
| USB data cables | FC USB-C, Pi/reference power arrangements | Distinguish data-only capability and power supplies |
| Cooling and supports | Pi cooler, FC insulation/mounting | Count/clearance and secure installation |

## Instruments and facilities required

An appropriately rated multimeter and insulated leads, safe low-voltage breakout/test points, current-limited regulated bench source for bring-up, suitable solder/crimp tools, magnification and a protected LiPo work area. Waveform/transient investigations may require an oscilloscope and correct probing. Presence/calibration of these tools is not established by this package.

## Software and data transfer

| Material | Public repository or separate custody | Incoming action |
|---|---|---|
| FC source/manufacturing records | Pinned public V2 is included; original private/vendor packages are held separately | Identify match to received board; request originals if needed |
| Original/public firmware | Neutral FCV2 binaries/source inputs/manifests are included; original SALFCGAMUDA files are private, with identities/hashes published | Obtain original matching files privately if recovery requires them; no automatic flash |
| FC2 parameters | Eleven exports plus complete comparisons | Fresh live read-back before changes |
| Ground-station evidence | Sanitized catalog and summaries are public; recordings/screenshots/reviews remain private | Install official Mission Planner; arrange private evidence transfer |
| MCU programming tool | Instructions and source references | Obtain official STM32CubeProgrammer/drivers; installer not bundled |
| Transmitter/RX exports | Receiver banner/settings recorded; no complete final handset export established | Capture current config privately without reset |
| Pi OS/storage image | Not supplied as an accepted image | Identify and make an authorized private backup; preserve credentials separately |
| Pi application/service code | Not established as a final working deliverable | Obtain from Pi team; record repository/commit/lockfile/services |
| HAT models/drivers | No accepted version set preserved | Record exact compatible versions and model licenses |
| DataFlash/MAVLink logs | No complete final motor-session log set established | Download/preserve available logs during safe intake; do not erase storage |

## Intake record

For each received item enter: asset ID, physical model/revision, serial if appropriate, quantity, condition, accessories, last known configuration, photograph filename, custodian and location. Keep private serial/account identifiers out of future public additions unless there is a reason and approval. Use the [custody checklist](CUSTODY.md) to distinguish public downloads from private files still to be received.
