# Public provenance and integrity

This directory describes only the sanitized public edition. The private package has its own larger inventory, raw-evidence hashes and workstation copy records; those are excluded here.

## Check a downloaded copy

Install Python 3.10 or newer. Download the ZIP or clone with `git clone -c core.autocrlf=false -c core.eol=lf https://github.com/desanv01/Flight-Controller-V2-Handover.git` to preserve distributed line endings. Open a terminal in this repository and run:

```sh
python tools/verify_handover.py
```

The default command reads files, prints a compact JSON result and exits nonzero on a failure. It requires no third-party packages, network, GitHub authentication or connected hardware. It does not alter firmware, parameters or the reports. Git metadata and Python cache directories are outside its payload scope.

The checks cover exact distributed SHA256 hashes; unexpected/missing payload files; all eleven parameter parsers and their published comparisons; the critical final bench values; 481 source blobs at the pinned V2 commit; included firmware/APJ identity; authored Markdown local targets; and common credential/private-path patterns plus excluded asset types. The retained V2 history is not rewritten to repair historical source-local links. External URLs and section anchors are not automatically checked.

## Records

- [Validation result and limits](VALIDATION.md).
- [Machine-readable validation](validation-results.json).
- [Exact distributed file hashes](package-sha256.csv).
- [Pinned V2 blob inventory](v2-source-tree.json).
- [Public selection and protection record](publication-provenance.json).

The manifest excludes itself and its two generated validation reports to avoid circular hashes. A matching manifest detects accidental changes relative to this release; it is not a digital signature or independent guarantee against someone replacing both files and manifest. Obtain the repository from the intended owner and record the Git commit for stronger provenance.

After intentional reviewed changes, maintainers may run `python tools/verify_handover.py --refresh`, then the default command again. Refresh regenerates only the manifest and validation reports. It does not normalize or rewrite parameter exports/reference files and does not replace a publication review.
