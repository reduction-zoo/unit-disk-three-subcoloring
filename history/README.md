# Retained exploration history

The [campaign state](campaigns/unit-disk-three-subcoloring/state.md) indexes the original rounds.
The [question](campaigns/unit-disk-three-subcoloring/question.md), [rounds](campaigns/unit-disk-three-subcoloring/rounds/),
[reviews](campaigns/unit-disk-three-subcoloring/reviews/) and [working evidence](campaigns/unit-disk-three-subcoloring/work/)
are preserved at their original relative paths under `history/`.

The initial local import contained 403 campaign files and 16 explicitly referenced
supporting files. The original campaign files were checked byte-for-byte against
the source. Build caches, virtual environments, bytecode and OS metadata are
excluded. Referenced external URLs and unavailable historical files are not
promised local artifacts; no missing material was invented. A linked board index
may describe other campaigns that are outside this archive.

Live paper and algorithm files are copies of the final campaign artifacts.
Live Markdown links were relocated to the archived or current artifacts.
Packaging path repairs: algorithm/algorithm.py, algorithm/check.py, algorithm/verify.py.
The original versions remain in the snapshot. These repairs do not alter the
mathematical construction. Earlier commands assume their original campaign
working directory. Replays should use the live entry points in the root README.

Additional local imports required by cited historical scripts:

- `history/campaigns/depth-three-unit-two-interval/work/split_oracle.py`

## Regenerating expanded targets

Expanded target JSON files from round 056 and the final prepared and additional
verification suites are excluded from Git. Existing local copies remain available.
Their source instances, generators, witnesses and verification logs are retained;
earlier round fixtures and counterexamples remain tracked.

From the repository root, rebuild the final suite outputs with:

```sh
uv sync --locked
uv run --locked python algorithm/check.py --candidate algorithm/algorithm.py --evidence evidence/prepared-replay
uv run --locked python algorithm/verify.py --candidate algorithm/algorithm.py --evidence evidence/additional-replay
```

Use a fresh evidence directory for each run. To reproduce the round 056 targets
at their historical paths, run:

```sh
uv run --locked python history/campaigns/unit-disk-three-subcoloring/rounds/056/probe.py
```

These commands expand large graphs and run their finite checks; the retained
logs record the earlier executions. Target files are deterministic construction
outputs, not irreplaceable observations.
