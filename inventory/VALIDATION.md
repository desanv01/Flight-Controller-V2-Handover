# Public edition validation

**Result: PASS** · edition prepared 1 November 2026.

- 537 payload files hashed, 137,861,267 bytes; generated outputs below excluded.
- Eleven parameter exports parsed; complete history/diff and final 945-entry bench snapshot checked.
- All 481 public V2 blobs compared with the pinned commit; only documented CRLF/LF equivalence permitted.
- Included neutral firmware hashes checked; APJ decoded payload compared with accompanying BIN.
- Authored relative link targets checked; common private-path/key patterns and forbidden asset types scanned.

## Reproduce

```sh
python tools/verify_handover.py
```

The default command is offline and read-only. Python 3.10+ and its standard library are sufficient.

## Scope and limits

Excluded from their own hash manifest to avoid circularity:

- `inventory/VALIDATION.md`
- `inventory/package-sha256.csv`
- `inventory/validation-results.json`

These reports are regenerated deterministically and compared during read-only verification. Git metadata and Python caches are outside the payload. The exact distributed bytes are hashed even where the pinned source comparison permits line-ending equivalence. External URLs, section anchors and historical source-local links inside the preserved V2 snapshot are not automatically checked. Pattern scanning is not exhaustive secret detection; raw test media and original private engineering packages were excluded by selection.

This is documentation/file validation, not a new hardware test, digital signature, flight approval or closure of an engineering fault. The local original V2 checkout and remote main revision were checked separately during publication; the portable verifier does not access either.

See [machine-readable results](validation-results.json), [manifest](package-sha256.csv) and [public scope](../handover/PUBLICATION-REVIEW.md).
