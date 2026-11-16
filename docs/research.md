# Research and admission decisions

Reviewed 2026-11-16 for opensearch 3.9.0. Community articles identify hypotheses, incidents and test cases. Exact product semantics come from primary documentation and executed native fixtures. No article, popularity score or benchmark ratio automatically admits a blocking rule.

| Source | Kind | Decision |
|---|---|---|
| [OS-SEC](https://docs.opensearch.org/3.9/security/configuration/best-practices/) | primary | TLS, least privilege and replacing demo PKI; do not infer certificate validity from filenames. |
| [OS-TLS](https://docs.opensearch.org/3.9/security/configuration/tls/) | primary | TLS and hostname-verification configuration; a snapshot is not a handshake test. |
| [OS-INDEX](https://docs.opensearch.org/3.9/install-and-configure/configuring-opensearch/index-settings/) | primary | Explicit topology/mapping limits; sizing remains contextual. |
| [OS-BULK](https://docs.opensearch.org/3.9/api-reference/document-apis/bulk/) | primary | Inspect per-item failures, byte bounds, retry and visibility semantics. |
| [OS-TUNE](https://docs.opensearch.org/3.9/tuning-your-cluster/) | primary | Measure indexing/search/recovery before tuning. |
| [OS-REDDIT](https://www.reddit.com/r/aws/comments/1axkjgd/) | community | Distinguish AWS-managed/serverless service limits from self-hosted OpenSearch controls. |
| [OS-MEDIUM](https://medium.com/motive-eng/optimizing-opensearch-for-high-velocity-writes-processing-85-million-updates-a-day-ac736484f3d3) | community | Write-amplification and refresh/merge tuning motivate experiments; five shards, 30s refresh and merge values are not universal rules. |
| [OS-SHARDS](https://dejanualex.medium.com/opensearch-do-some-stats-on-your-indices-ac9bb5670444) | community | Shard pressure is real; reducing replicas or applying a fixed GB target requires availability/recovery context. |
| [OS-INCIDENT](https://itnext.io/opensearch-outage-lessons-learnt-and-measures-implemented-a9730e1b275f) | community | Public preview only of a 2023 incident account; no paywalled root cause or mitigation details are claimed or admitted. |
| [OS-RELEVANCE](https://opensearch.org/blog/measuring-and-improving-search-quality-metrics/) | primary | Separate relevance evaluation from cluster health and ingestion success. |
| [OS-INDEXING](https://docs.opensearch.org/3.9/tuning-your-cluster/performance-tuning/indexing-speed/) | primary | Experiment with byte size, refresh and concurrency; preserve fields needed to identify/retry failed items. |

The complete conceptual checklist is in [best practices](best-practices.md). Only the finite catalogue is implemented as executable profile checks. Missing inputs remain untested; contextual recovery, performance, migrations and security behavior require declared external tests. These sources are linked and synthesized in original wording rather than copied in full.

Substack searches yielded no sufficiently relevant general operational reference to admit; OpenSearch maintainer material, a first-hand Medium engineering article and an ITNEXT incident account supplement the official documentation. No Substack authority is fabricated.

Demo-certificate setting semantics are also checked against the [OpenSearch maintainer Helm documentation](https://github.com/opensearch-project/helm-charts). This does not validate certificate chains.
