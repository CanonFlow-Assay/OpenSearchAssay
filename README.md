# OpenSearchAssay

An offline, deterministic evidence auditor for opensearch **3.9.0**, with a companion engineering skill and native engine qualification cases. Apache-2.0.

## Current scope

The initial catalogue implements **11 versioned profile rules**. It audits supplied normalized settings and declared behavior evidence, with explicit Pass, Fail, Inconclusive and ToolFailure outcomes. It does not discover a production deployment or parse arbitrary SQL. Read the [contract](CONTRACT.md) before treating a receipt as evidence.

[Best-practice guidance](docs/best-practices.md) covers modelling, security, concurrency, resource budgets, recovery and operational decisions. The [research ledger](docs/research.md) records official, Reddit, Medium, Substack and specialist sources and distinguishes implemented checks from contextual recommendations. The release baseline was reviewed on 2026-11-16 against the [official release source](https://opensearch.org/downloads/).

## Run locally

Requires Python 3.12; the auditor has no third-party runtime dependencies.

```sh
PYTHONPATH=src python3 -m opensearch_assay doctor
PYTHONPATH=src python3 -m opensearch_assay catalog
PYTHONPATH=src python3 -m opensearch_assay explain OS001
PYTHONPATH=src python3 -m opensearch_assay scan examples/snapshot.json --policy examples/policy.json
PYTHONPATH=src python3 -m opensearch_assay verify examples/snapshot.json --policy examples/policy.json
```

The example policy deliberately declares no application behavior tests, so its clean snapshot is **Inconclusive**, exit 2. Configure actual required commands and their input files according to the contract; no test is fabricated merely to obtain Pass. `assess` preserves the raw verification receipt inside an additive envelope. `--out PATH` writes a receipt to an existing parent directory.

## Validate and package

```sh
python3 -m unittest discover -s tests -v
python3 eng/package.py
python3 artifacts/opensearch_assay.pyz doctor
python3 eng/qualify.py
```

The archive is independently executable without installing a package. Tests exercise rule mutations, missing/malformed evidence, command failures and bounds, input drift, output aliasing, deterministic receipts and a fresh archive consumer.

For real engine cases use the [native qualification instructions](docs/native.md). Results and current limits are in [qualification](docs/qualification.md). The [companion skill](skills/opensearch-engineering/SKILL.md) is synchronized with CanonFlowFoundation/skills.

## Evidence boundary

A supplied setting is a declaration until its collection is independently established. Runtime TLS, privilege inheritance, recovery, performance and other contextual claims require their own tests. Preserve failed or missing evidence. No live database access, schema mutation, automatic correction or network request occurs inside the audit engine.

See [LICENSE](LICENSE), [NOTICE](NOTICE) and [contributing](CONTRIBUTING.md).
