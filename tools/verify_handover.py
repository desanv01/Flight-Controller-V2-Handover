#!/usr/bin/env python3
"""Offline, read-only by default. No hardware, network or Git commands are run."""
from __future__ import annotations

import argparse
import base64
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]
GENERATED = {
    'inventory/package-sha256.csv',
    'inventory/validation-results.json',
    'inventory/VALIDATION.md',
}
LATEST = 'FC2_stick_control_working_2026-10-21.param'
LATEST_SHA = '0a2d585fbae65b96a086eed1f243a6e54256b0ca37b165a8d4b3d08ad1ad9ee3'
SOURCE_COMMIT = '56c91e283b9ce56b6e43480734feb60e2f078760'
FAILURES: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def payload() -> list[Path]:
    return sorted((p for p in ROOT.rglob('*') if p.is_file() and not any(
        part in {'.git', '__pycache__'} for part in p.relative_to(ROOT).parts)), key=rel)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding='utf-8-sig'))


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def require(ok: bool, message: str) -> None:
    if not ok:
        FAILURES.append(message)


def parse_params(path: Path) -> dict[str, str]:
    values = {}
    for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith(('#', ';')):
            continue
        parts = re.split(r'[,\s]+', line)
        try:
            if len(parts) != 2 or not re.fullmatch(r'[A-Z][A-Z0-9_]*', parts[0]):
                raise ValueError('invalid format')
            name, value = parts
            if not Decimal(value).is_finite():
                raise ValueError('non-finite value')
            require(name not in values, f'Duplicate parameter: {path.name}:{number}')
            values[name] = value
        except (InvalidOperation, ValueError):
            FAILURES.append(f'Malformed parameter: {path.name}:{number}')
    return values


def check_parameters() -> dict:
    files = sorted((ROOT / 'config/historical-fc2-snapshots').glob('*.param'))
    require(len(files) == 11, 'Expected eleven original parameter exports')
    snapshots = {p.name: parse_params(p) for p in files}
    catalog = {row['file']: row for row in read_csv('config/snapshot-catalog.csv')}
    require(set(catalog) == set(snapshots), 'Snapshot catalog file set differs')
    for path in files:
        row = catalog.get(path.name, {})
        require(row.get('sha256') == sha(path.read_bytes()), f'Original snapshot hash: {path.name}')
        require(row.get('parameters') == str(len(snapshots[path.name])), f'Parameter count: {path.name}')
        require(row.get('bytes') == str(path.stat().st_size), f'Snapshot size: {path.name}')
        require(not row.get('duplicates') and not row.get('malformed_lines'), f'Catalog parser errors: {path.name}')
    latest = snapshots.get(LATEST, {})
    require(len(latest) == 945, 'Latest export must contain 945 unique entries')
    require(sha((ROOT / 'config/historical-fc2-snapshots' / LATEST).read_bytes()) == LATEST_SHA,
            'Historical final export has been changed')
    expected = {
        'FRAME_CLASS': 1, 'FRAME_TYPE': 1,
        'SERIAL2_PROTOCOL': 23, 'SERIAL2_OPTIONS': 0, 'SERIAL2_BAUD': 57,
        'RC_PROTOCOLS': 512, 'RC_OPTIONS': 8224, 'RSSI_TYPE': 3,
        'RCMAP_ROLL': 1, 'RCMAP_PITCH': 2, 'RCMAP_THROTTLE': 3, 'RCMAP_YAW': 4,
        'RC6_OPTION': 0, 'ARMING_RUDDER': 2, 'ARMING_SKIPCHK': 0,
        'RC1_OPTION': 0, 'RC2_OPTION': 0, 'RC3_OPTION': 0, 'RC4_OPTION': 0,
        'RC3_DZ': 30, 'DISARM_DELAY': 10, 'RC_SPEED': 490, 'SERVO_BLH_POLES': 14,
        'MOT_PWM_TYPE': 5, 'ESC_CALIBRATION': 0,
        'SERVO1_FUNCTION': 34, 'SERVO2_FUNCTION': 35, 'SERVO3_FUNCTION': 36, 'SERVO4_FUNCTION': 33,
        'SERVO_DSHOT_ESC': 1, 'SERVO_BLH_AUTO': 1, 'SERVO_BLH_BDMASK': 0,
        'COMPASS_ENABLE': 0, 'COMPASS_USE': 0, 'COMPASS_USE2': 0, 'COMPASS_USE3': 0,
        'EK3_SRC1_YAW': 0, 'BATT_MONITOR': 0, 'EK3_IMU_MASK': 3,
        'SERIAL6_PROTOCOL': -1, 'SERIAL7_PROTOCOL': -1,
        'INITIAL_MODE': 0, 'FLTMODE_CH': 5,
    }
    expected.update({f'FLTMODE{i}': 0 for i in range(1, 7)})
    for name, value in expected.items():
        require(name in latest and Decimal(latest[name]) == Decimal(value), f'Final bench value differs: {name}')
    analysis = load_json('config/parameter-analysis.json')
    require(analysis['latest_values'] == latest, 'Published final-value analysis differs from original')
    require(analysis['latest_sha256'] == LATEST_SHA, 'Analysis final hash differs')

    history = read_csv('config/parameter-history-all.csv')
    observed_history = {(r['snapshot'], r['parameter'], r['value']) for r in history}
    expected_history = {(name, key, value) for name, vals in snapshots.items() for key, value in vals.items()}
    require(observed_history == expected_history and len(history) == len(expected_history),
            'Full parameter history has missing/extra/duplicate rows')
    diff = read_csv('config/parameter-diff-to-final.csv')
    expected_diff = set()
    for name, vals in snapshots.items():
        if name == LATEST:
            continue
        for key in set(vals) | set(latest):
            a, b = vals.get(key), latest.get(key)
            if a is None or b is None or Decimal(a) != Decimal(b):
                expected_diff.add((name, key, a or '', b or ''))
    actual_diff = {(r['earlier_file'], r['parameter'], r['earlier_value'], r['final_value']) for r in diff}
    require(actual_diff == expected_diff and len(diff) == len(expected_diff), 'Numerical comparison differs')
    nonzero_locations = []
    for name, vals in snapshots.items():
        for key, value in vals.items():
            if re.search(r'(?:^|_)(?:LAT|LON)(?:_|$)', key) and Decimal(value) != 0:
                nonzero_locations.append(f'{name}:{key}')
    require(not nonzero_locations, 'Nonzero coordinate parameters need private review')
    return {'snapshots': len(files), 'latest_entries': len(latest),
            'history_rows': len(history), 'difference_rows': len(diff),
            'critical_bench_values_checked': len(expected), 'nonzero_coordinates': len(nonzero_locations)}


def check_source() -> dict:
    source = load_json('inventory/v2-source-tree.json')
    require(source['commit'] == SOURCE_COMMIT, 'Pinned reference revision differs')
    rows = source['blobs']
    require(len(rows) == 481, 'Expected 481 public reference blobs')
    expected_paths = {row['path'] for row in rows}
    source_root = ROOT / 'references/v2-design'
    actual_paths = {p.relative_to(source_root).as_posix() for p in source_root.rglob('*') if p.is_file()}
    require(expected_paths == actual_paths, 'Reference snapshot missing/extra files')
    normalized = []
    for row in rows:
        path = source_root / row['path']
        if not path.is_file():
            FAILURES.append(f'Missing source blob: {row["path"]}')
            continue
        data = path.read_bytes()
        def git_blob(blob):
            return hashlib.sha1(b'blob ' + str(len(blob)).encode() + b'\0' + blob).hexdigest()
        if git_blob(data) != row['sha']:
            if git_blob(data.replace(b'\r\n', b'\n')) == row['sha']:
                normalized.append(row['path'])
            else:
                FAILURES.append(f'Pinned source mismatch: {row["path"]}')
    return {'blobs': len(rows), 'commit': source['commit'],
            'line_ending_only_matches': len(normalized), 'line_ending_paths': normalized}


def check_firmware() -> dict:
    records = load_json('firmware/artifact-identities.json')
    count = 0
    for record in records:
        if 'path' not in record:
            require(record.get('distribution', '').startswith('excluded'), 'Private artifact distribution ambiguous')
            continue
        path = ROOT / record['path']
        data = path.read_bytes()
        require(sha(data) == record['sha256'] and len(data) == record['bytes'], f'Firmware identity: {rel(path)}')
        count += 1
        if path.suffix == '.apj':
            image = json.loads(data)
            decoded = zlib.decompress(base64.b64decode(image['image']))
            require(decoded == path.with_suffix('.bin').read_bytes(), 'Included APJ payload differs from BIN')
            require(image['board_id'] == 1241, 'Included APJ local board ID differs')
            require(sha(decoded) == record['decoded_sha256'], 'APJ decoded hash differs')
    require(count == 3, 'Expected three included neutral firmware identities')
    return {'included_identity_files': count, 'apj_equals_bin': True,
            'device_flash_read_back': False, 'private_original_binaries_included': False}


def check_links(files: list[Path]) -> dict:
    checked = 0
    targets = 0
    for path in files:
        if path.suffix.lower() != '.md' or 'v2-design' in path.relative_to(ROOT).parts or rel(path) in GENERATED:
            continue
        checked += 1
        text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8-sig'), flags=re.S)
        for url in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)', text):
            url = url.strip('<>')
            if re.match(r'^(?:https?:|mailto:|#)', url):
                continue
            target = unquote(url.split('#', 1)[0])
            if target:
                targets += 1
                resolved = (path.parent / target).resolve()
                require(resolved.is_relative_to(ROOT) and (resolved.exists() or rel(resolved) in GENERATED),
                        f'Broken/escaping link: {rel(path)} -> {target}')
    return {'authored_documents': checked, 'local_targets': targets,
            'scope': 'Target existence only; external URLs/anchors and preserved historical source links excluded'}


def check_privacy(files: list[Path]) -> dict:
    patterns = {
        'private workstation path': re.compile(rb'(?i)(?:[a-z]:[/\\]Users[/\\]|[/]Users[/][^/\s]+[/]|[/]home[/][^/\s]+[/])'),
        'GitHub token': re.compile(rb'(?:gh[pousr]_[a-zA-Z0-9]{30,}|github_pat_[a-zA-Z0-9_]{30,})'),
        'private key': re.compile(rb'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),
        'AWS access key': re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    }
    forbidden_suffixes = {'.mp4', '.mov', '.avi', '.mkv', '.pem', '.key'}
    scanned_bytes, zip_members = 0, 0
    def scan(data: bytes, name: str):
        nonlocal scanned_bytes
        scanned_bytes += len(data)
        for label, pattern in patterns.items():
            require(not pattern.search(data), f'Privacy review required ({label}): {name}')
    for path in files:
        relative = rel(path)
        # Generated outputs are checked via their deterministic comparison; avoid findings reflecting themselves.
        if relative in GENERATED:
            continue
        require(path.suffix.lower() not in forbidden_suffixes, f'Excluded file type: {relative}')
        require(not any(part in {'local-only', 'private', 'original-evt1', 'original-pcbway', 'original-jlc-final'}
                        for part in path.relative_to(ROOT).parts), f'Excluded private directory: {relative}')
        data = path.read_bytes()
        scan(data, relative)
        if path.suffix.lower() == '.zip':
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                for item in archive.infolist():
                    if item.is_dir():
                        continue
                    zip_members += 1
                    require('..' not in Path(item.filename).parts, f'Unsafe archive name: {relative}')
                    scan(archive.read(item), relative + ':' + item.filename)
    return {'files_scanned': len(files) - sum(rel(p) in GENERATED for p in files),
            'bytes_scanned_including_zip_contents': scanned_bytes, 'zip_members_scanned': zip_members,
            'scope': 'Common path/key patterns and excluded file classes; not exhaustive secret detection',
            'intentional_public_default': 'The ExpressLRS default AP password is public vendor information, not a private credential'}


def manifest_rows(files: list[Path]) -> list[dict]:
    return [{'path': rel(p), 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())}
            for p in files if rel(p) not in GENERATED]


def report(files: list[Path], rows: list[dict]) -> dict:
    results = {'edition_date': '2026-11-01', 'payload_files': len(files),
               'manifest_files': len(rows), 'manifest_bytes': sum(r['bytes'] for r in rows),
               'manifest_exclusions': sorted(GENERATED)}
    for label, function in [('parameters', check_parameters), ('public_reference', check_source),
                            ('firmware', check_firmware), ('links', lambda: check_links(files)),
                            ('privacy', lambda: check_privacy(files))]:
        try:
            results[label] = function()
        except (OSError, ValueError, KeyError, zipfile.BadZipFile, zlib.error) as error:
            FAILURES.append(f'{label}: {type(error).__name__}: {error}')
    results['failures'] = FAILURES.copy()
    results['result'] = 'FAIL' if FAILURES else 'PASS'
    return results


def write_outputs(rows: list[dict], result: dict) -> None:
    with (ROOT / 'inventory/package-sha256.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['path', 'bytes', 'sha256'], lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    (ROOT / 'inventory/validation-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8', newline='\n')
    (ROOT / 'inventory/VALIDATION.md').write_text(render_report(result), encoding='utf-8', newline='\n')


def render_report(result: dict) -> str:
    lines = [
        '# Public edition validation', '', f'**Result: {result["result"]}** · edition prepared 1 November 2026.', '',
        f'- {result["manifest_files"]} payload files hashed, {result["manifest_bytes"]:,} bytes; generated outputs below excluded.',
        '- Eleven parameter exports parsed; complete history/diff and final 945-entry bench snapshot checked.',
        '- All 481 public V2 blobs compared with the pinned commit; only documented CRLF/LF equivalence permitted.',
        '- Included neutral firmware hashes checked; APJ decoded payload compared with accompanying BIN.',
        '- Authored relative link targets checked; common private-path/key patterns and forbidden asset types scanned.', '',
        '## Reproduce', '', '```sh', 'python tools/verify_handover.py', '```', '',
        'The default command is offline and read-only. Python 3.10+ and its standard library are sufficient.', '',
        '## Scope and limits', '',
        'Excluded from their own hash manifest to avoid circularity:', '',
        *['- `' + path + '`' for path in sorted(GENERATED)], '',
        'These reports are regenerated deterministically and compared during read-only verification. Git metadata and Python caches are outside the payload. '
        'The exact distributed bytes are hashed even where the pinned source comparison permits line-ending equivalence. '
        'External URLs, section anchors and historical source-local links inside the preserved V2 snapshot are not automatically checked. '
        'Pattern scanning is not exhaustive secret detection; raw test media and original private engineering packages were excluded by selection.', '',
        'This is documentation/file validation, not a new hardware test, digital signature, flight approval or closure of an engineering fault. '
        'The local original V2 checkout and remote main revision were checked separately during publication; the portable verifier does not access either.', '',
        'See [machine-readable results](validation-results.json), [manifest](package-sha256.csv) and [public scope](../handover/PUBLICATION-REVIEW.md).', '',
    ]
    if result['failures']:
        lines.extend(['## Failures', '', *['- ' + failure for failure in result['failures']], ''])
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Regenerate only the manifest and validation reports after review')
    args = parser.parse_args()
    files = payload()
    rows = manifest_rows(files)
    # Include future generated paths in counts on the initial refresh.
    if args.refresh:
        for name in GENERATED:
            path = ROOT / name
            if path not in files:
                files.append(path)
        files.sort(key=rel)
    result = report(files, rows)
    if args.refresh:
        write_outputs(rows, result)
    else:
        try:
            saved = read_csv('inventory/package-sha256.csv')
            normalized = [{'path': r['path'], 'bytes': str(r['bytes']), 'sha256': r['sha256']} for r in rows]
            require(saved == normalized, 'Payload differs from published hash manifest; review changes before refresh')
            require(load_json('inventory/validation-results.json') == result, 'Validation JSON differs from recomputed result')
            require((ROOT / 'inventory/VALIDATION.md').read_text(encoding='utf-8') == render_report(result),
                    'Human-readable validation report differs from recomputed result')
        except (OSError, ValueError, KeyError) as error:
            FAILURES.append(f'Generated report unavailable: {error}')
    print(json.dumps({'result': 'FAIL' if FAILURES else 'PASS', 'payload_files': len(files),
                      'manifest_files': len(rows), 'manifest_bytes': result['manifest_bytes'],
                      'parameters': result.get('parameters'), 'source_blobs': result.get('public_reference', {}).get('blobs'),
                      'authored_documents': result.get('links', {}).get('authored_documents'),
                      'failures': FAILURES}, indent=2))
    return 1 if FAILURES else 0


if __name__ == '__main__':
    sys.exit(main())
