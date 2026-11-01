# Continue the handover

Use a branch and a focused pull request for an incoming change. Preserve the original parameter exports and the pinned reference snapshot. Put new physical results in a dated session record with article ID, operator, firmware/configuration hashes, power/harness state, procedure, observations and reviewer.

## Before changing hardware or configuration

Read the relevant guide and open issue. Save a fresh parameter export and identify the received assembly. Record the reason, old/new setting, rollback and test limits. A successful parameter write, arm request or build is not a physical acceptance result.

After a test, update the issue register and current status only to the extent supported by the evidence. Use **recorded**, **reported**, **planned** and **unresolved** consistently. A proposed instruction is not a completed test. Keep failed attempts and private original logs with the custodian.

## Before adding files publicly

Review disclosure authority and license scope. Exclude credentials, personal/site data, raw desktop recordings, private paths, supplier correspondence and unreviewed departmental assets. Copy only the selected files into a clean candidate; an ignore file cannot remove data already committed to Git history.

Do not change `references/v2-design/` silently. A newer design reference requires a reviewed source revision, matching blob inventory, provenance update and explicit compatibility review. Keep supplier variants coherent and distinguish historical source from the actual assembled article.

## Validate a change

Run this read-only command first:

```sh
python tools/verify_handover.py
```

After reviewing intentional file changes and the publication scope, regenerate the integrity manifest/report and verify again:

```sh
python tools/verify_handover.py --refresh
python tools/verify_handover.py
```

`--refresh` updates only generated inventory outputs; it does not grant publication permission or execute hardware steps. Inspect the Git diff before committing. Do not use a regenerated hash to hide an unexplained change to historical evidence. CI runs the read-only checks on pushes and pull requests.

Keep sensitive evidence in approved private custody and link a sanitized result summary. Do not turn this public repository into a raw project-folder dump.
