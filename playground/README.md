# OpenSearchAssay playground

The wrapper evaluates a checked-in OpenSearch 3.9.0 settings and index snapshot. The configured input is a JSON file.

Run the source commands from the repository root with Python 3.
[Native fixture setup](../docs/native.md)

```sh
python3 playground/run.py
```

The v2 receipt preserves command arguments, exits, and raw logs for
readiness, catalogue explanations, source tests, the showcase verification,
and the provisional scan control. The scan control expects
`Inconclusive` with exit `2`. The wrapper propagates a failed or
incomplete showcase and refuses a contradictory receipt and process exit.

For the native receipt alone, run each command independently.

```sh
PYTHONPATH=src python3 -m opensearch_assay scan examples/snapshot.json --policy examples/policy.json
PYTHONPATH=src python3 -m opensearch_assay verify examples/snapshot.json --policy examples/policy.json
```

The example policy has an empty `requiredCommands` list. Both commands report `Inconclusive` with exit `2` for this fixture. The native fixture uses its own policy and records the limits of its isolated cluster.
