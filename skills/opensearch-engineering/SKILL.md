---
name: opensearch-engineering
description: "Design, implement or review OpenSearch mappings, retrieval, bulk ingestion, security and recovery using the actual self-hosted or managed-service contract."
---

# OpenSearch engineering

Identify self-hosted OpenSearch, AWS OpenSearch Service or Serverless, the actual engine/plugin version, client and deployment ownership. The researched self-hosted baseline is 3.9.0 as of 2026-11-16. Verify managed-service capabilities separately and preserve existing project choices. Elasticsearch guidance is not automatically an OpenSearch contract.

Design mappings/analyzers from exact, full-text, filter, aggregation and language requirements. Control dynamic-field growth and evaluate relevance with held-out information needs. Keep tenant/access/time filters across candidate generation, reranking, snippets and caches; routing is not authorization.

Bound bulk bytes, items, in-flight work and retries. Inspect every item even when HTTP succeeds. Preserve stable IDs/routing and retry only the appropriate failed actions; classify mapping errors, throttling and ambiguous timeouts separately. Test acknowledgment versus search visibility and retain failure-identification fields in filtered responses.

Choose shards, replicas, refresh, merge and vector settings from measured workload, failure domains and recovery objectives. Avoid copying an article's shard count or refresh interval into a blocking policy. Reconcile a rebuilt index before an authorized alias cutover and account for writers still targeting the old index.

Use deployment-owned PKI, verified hostnames, least privilege and actual DLS/FLS/cross-tenant tests. Exercise snapshots/restoration and upgrade/rollback constraints. Cluster health and replicas do not establish backup recovery or search quality.

Read [engineering decisions](references/best-practices.md) and [source decisions](references/sources.json). OpenSearchAssay checks a strict self-hosted HA/TLS/bulk snapshot profile. Its result is bounded to supplied evidence and configured tests; certificate validity, effective permissions, production performance and managed-service equivalence require additional evidence.
