#!/usr/bin/env python3
"""Compare saved numeric exports without connecting to or changing an FC."""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ROOT / 'config/historical-fc2-snapshots/FC2_stick_control_working_2026-10-21.param'
FIELDS = ['parameter', 'status', 'baseline_value', 'current_value', 'review_group']


def parse_text(text: str) -> dict[str, str]:
    values = {}
    for number, line in enumerate(text.lstrip('\ufeff').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith(('#', ';')):
            continue
        parts = re.split(r'[,\s]+', line)
        if len(parts) != 2 or not re.fullmatch(r'[A-Z][A-Z0-9_]*', parts[0]):
            raise ValueError(f'Invalid parameter format at line {number}')
        name, value = parts
        try:
            if not Decimal(value).is_finite():
                raise InvalidOperation
        except InvalidOperation as error:
            raise ValueError(f'Non-finite or nonnumeric value at line {number}') from error
        if name in values:
            raise ValueError(f'Duplicate parameter {name} at line {number}')
        values[name] = value
    if not values:
        raise ValueError('The export has no numeric parameter entries')
    return values


def review_group(name: str) -> str:
    if name.startswith('STAT_'):
        return 'runtime counter; not flight evidence'
    if name.startswith('INS_GYR') or name == 'BARO1_GND_PRESS':
        return 'sensor startup/calibration; interpret with live data'
    if name.startswith(('INS_ACC', 'AHRS_TRIM')) or re.fullmatch(r'RC\d+_(?:MIN|MAX|TRIM|REVERSED|DZ)', name):
        return 'device-specific calibration; do not copy blindly'
    return 'configuration; explain before changing'


def compare(baseline: dict[str, str], current: dict[str, str]) -> list[dict[str, str]]:
    rows = []
    for name in sorted(set(baseline) | set(current)):
        old, new = baseline.get(name), current.get(name)
        if old is not None and new is not None and Decimal(old) == Decimal(new):
            continue
        rows.append({'parameter': name,
                     'status': 'added' if old is None else 'missing' if new is None else 'changed',
                     'baseline_value': old or '', 'current_value': new or '', 'review_group': review_group(name)})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, default=DEFAULT_BASELINE,
                        help='Reference export; defaults to the historical final FC2 bench file')
    parser.add_argument('--current', type=Path, required=True, help='Fresh saved export to inspect')
    parser.add_argument('--output', type=Path, help='New CSV outside this repository; otherwise print CSV to stdout')
    args = parser.parse_args()
    try:
        baseline = parse_text(args.baseline.read_text(encoding='utf-8-sig'))
        current = parse_text(args.current.read_text(encoding='utf-8-sig'))
        rows = compare(baseline, current)
        if args.output:
            output = args.output.resolve()
            if output.is_relative_to(ROOT) or output in {args.baseline.resolve(), args.current.resolve()}:
                raise ValueError('Output must be a new file outside the repository and distinct from both inputs')
            with output.open('x', encoding='utf-8', newline='') as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator='\n')
                writer.writeheader()
                writer.writerows(rows)
            print(f'{len(rows)} numeric differences; {len(baseline)} baseline and {len(current)} current entries. CSV created. No settings applied.')
        else:
            writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f'Comparison stopped: {error}\nNo settings were applied.\n')


if __name__ == '__main__':
    sys.exit(main())
