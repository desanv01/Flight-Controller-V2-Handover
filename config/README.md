# FC2 configuration snapshots

This folder preserves **eleven original parameter exports** and generated comparisons. The latest identified bench snapshot is [FC2_stick_control_working_2026-10-21.param](historical-fc2-snapshots/FC2_stick_control_working_2026-10-21.param). It has 945 unique parameter entries. It is not a live read-back from the hardware at transfer and not a flight-ready or universal restore file.

## Snapshot roles

| Filename | Role |
|---|---|
| `fc2 new updated working params 16.10.param` | Earlier FC2 baseline before the completed calibration described in the review |
| `FC2_after_accel_calibration_2026-10-16.param` | Saved accelerometer-calibration state |
| `FC2_before_ELRS_parameter_changes_2026-10-16.param` | Pre-receiver-configuration backup |
| `FC2_before_receiver_setup_2026-10-16.param` | Earlier receiver setup baseline |
| `FC2_after_receiver_config_2026-10-16.param` | Receiver parameters saved; filename date is not necessarily session date |
| `FC2_after_receiver_calibration_2026-10-16.param` | Earlier receiver endpoint capture; not the final low-throttle correction |
| `FC2_receiver_rechecked_2026-10-19.param` | Later receiver recheck |
| `FC2_before_orientation_fix_2026-10-21.param` | Intermediate state with RC6 option 154 and throttle trim 1826 |
| `FC2_after_flip_before_changes_2026-10-21.param` | Intermediate state with narrow roll range and high throttle trim |
| `FC2_radio_corrected_2026-10-21.param` | Corrected main-axis endpoints, RC6 still assigned 153 |
| `FC2_stick_control_working_2026-10-21.param` | Final identified stick-control bench state, RC6 disabled |

This is a role summary, not proof of every file's creation order. Several filenames retain 16 October even though later review identified a 19 October session. The private copy manifest preserves filesystem modification times as metadata, not unquestionable event timestamps. Public provenance uses relative paths and content hashes instead of workstation metadata.

## Machine-readable comparisons

- [Snapshot counts and hashes](snapshot-catalog.csv).
- [Every parameter in every snapshot](parameter-history-all.csv).
- [Every earlier snapshot compared numerically with the final one](parameter-diff-to-final.csv).
- [Final values and analysis metadata](parameter-analysis.json).

Comparisons use numeric equality, so equivalent decimal/scientific notation is not reported as a configuration change. Added/removed parameter names are retained. All input lines, duplicate names and malformed values are checked. The compiled files are never normalized or rewritten.

Changes are grouped as configuration, device-specific calibration, sensor startup/calibration data and counters. Startup gyro offsets, pressure and operating counters can vary without an intentional configuration change. Their differences alone do not prove a fault or flight. Use live data and logs to interpret them.

## Safe use

1. Save a new complete live export from the correctly identified FC before any write.
2. Compare it with the relevant historical snapshot; explain all intentional differences.
3. Review individual required settings rather than loading the full dump by default.
4. Never import another board's sensor IDs, offsets/scales, level trims or radio calibration blindly.
5. A replacement board needs its own calibration and physical mapping tests.
6. Keep device-specific snapshots separate from reusable configuration instructions. No automatic parameter-application script is supplied.

The final profile has no compass, battery monitoring or enabled J11 companion UART and preserves a non-default output permutation. Read [current status](../CURRENT-STATUS.md) before interpreting a filename containing “working.”
