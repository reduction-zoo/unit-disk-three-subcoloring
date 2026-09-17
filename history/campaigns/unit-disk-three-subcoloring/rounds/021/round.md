# Round 021 — extend the four-way junction

## Plan

The user added 20 rounds, extending the total allocation to 40. Continue from
the successful reversed-port junction without repeating preparation.
Hypothesis: repeating state 4 along each of its four arms preserves clean
colorings for arbitrary arm lengths. Check actual junctions with two and three
copies per arm (273 and 409 vertices). Derive a coordinate separation bound
between different arms beyond their first copies. If their distance exceeds
two, no P3 can mix those remote cells with another arm; combine this bound
with the previously checked junction and straight-wire triples to prove the
all-length extension. Scope: two full canonical witness checks and exact
projection bounds; no new solver query or timeout. If the bound fails, retain
only finite evidence and identify the next local interaction to check.

Experience: use round 018's periodic local-to-global argument and round 020's
asymmetric-port repair. The shared proposals remain pending under the campaign
write scope. Do not infer arbitrary attachment from clean ports alone.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/021/probe.py`.
[Output](output.jsonl): both 273- and 409-vertex junction extensions have valid
clean canonical witnesses. The normalized lateral bound is M=169/394, and
(1-M)^2|D|^2=2025/394>4. No solver queries or source/recovery calls; no rerun.

For a point beyond the first copy on one arm, its projection along that arm
is at least |D|. A point on an orthogonal arm has projection at most M|D|;
on the opposite arm it is nonpositive. Hence their distance exceeds two.
No P3 can include a remote-arm point and a point from another arm: adjacent
vertices are at distance at most one and the endpoints of a P3 at most two.
All remaining P3s lie in the initial junction or one straight arm, already
covered by the saved junction and periodic triple checks. This proves clean
extension for arbitrary arm lengths, conditional on the base finite lemma.

Experience extraction: update the pending composition entry with the stronger
distance-two separation needed to exclude mixed P3s, rather than merely excluding
cross edges at distance one. Two finite witnesses corroborate the geometric
bound; no independent review is implied. Shared entry remains pending.

## Next action

Attach an inequality gadget between two outward straight wires. Verify two
copies on each side and derive a separation bound before claiming arbitrary
extension. This connects the equality infrastructure to the actual source
constraint; branching alone would only produce trivially satisfiable instances.
