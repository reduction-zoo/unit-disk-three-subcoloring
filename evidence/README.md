# Import checks

Local replay on 2026-09-17. Only the `positive-unit` candidate case was replayed (537,397 vertices; six recoveries). The complete generated suite and additional verifier were not rerun.

| Check | Command | Exit code |
|---|---|---|
| [uv-lock](import-uv-lock.log) | `uv lock` | 0 |
| [uv-sync](import-uv-sync.log) | `uv sync --locked` | 0 |
| [self-test](import-self-test.log) | `uv run --locked python algorithm/check.py --self-test` | 0 |
| [candidate](import-candidate.log) | `uv run --locked python algorithm/check.py --candidate algorithm/algorithm.py --case positive-unit --evidence evidence/positive-unit` | 0 |
| [Paper](import-paper.log) | `typst compile paper/manuscript.typ paper/manuscript.pdf` | 0 |

The retained campaign and supporting files were compared byte-for-byte with the source. Live Markdown links and the documented executable paths were adjusted for this directory layout. Dependencies are recorded in `../uv.lock`.

These checks establish that the listed finite tests and manuscript build run in the new local project. They are not a new general proof, novelty assessment or independent formal certification. Historical review and verification evidence remains under `../history/`; the additional `algorithm/verify.py` suite was retained but not rerun during migration.
