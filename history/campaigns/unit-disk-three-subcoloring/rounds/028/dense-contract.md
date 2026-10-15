# Executable contract

Source: JSON object `{"n": nonnegative integer, "clauses": [[a,b,c], ...]}`.
Each literal is a nonzero signed integer of magnitude at most n. Repeated
literals and tautologies are legal. A source witness is a list of n booleans.
Every clause must contain a literal satisfied by that list.

Target: `{"centers": [[[x_numerator,x_denominator],
[y_numerator,y_denominator]], ...]}`. Numerators are integers; denominators
are positive integers. Floats and booleans are not integer encodings. Duplicate
centers are allowed. Edges join distinct indices at squared distance <= 1.
A target witness is a list of integers in {0,1,2}, one per center. Each
monochromatic connected component must be a clique.

`python3 algorithm.py` consumes one source JSON value on stdin and writes one
target JSON value. Malformed sources map to JSON null, a rejected target string.
Well-formed NO sources must produce valid center lists. Diagnostics use stderr;
execution failures have nonzero status. `python3 algorithm.py --extract` consumes
`{"source": ..., "target_solution": ...}` and emits the source witness. Recovery
recomputes any needed metadata from the source and works in a fresh process.
No candidate implementation exists yet.
