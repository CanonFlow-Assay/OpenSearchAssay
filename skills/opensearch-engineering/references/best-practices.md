# OpenSearch engineering decisions

Baseline reviewed on 2026-11-16: self-hosted OpenSearch 3.9.0. AWS OpenSearch Service and Serverless expose different versions, controls and operational responsibilities. Check that service's actual contract rather than sending self-hosted YAML settings to a managed endpoint. Elasticsearch and other products called OpenSearch are not interchangeable authorities for 3.9 behavior.

## Mapping and search meaning

Design mappings/analyzers from information needs. Use keyword for exact/filter/sort/aggregation semantics and analyzed text for the intended full-text behavior. Preserve source identifiers, language and timestamp semantics. Strict mappings can enforce a known schema; dynamic mappings can also be valid with a deliberate field budget and validation. Avoid uncontrolled dynamic fields and enabling fielddata on arbitrary text merely to fix an aggregation error.

Evaluate lexical/hybrid/vector ranking on held-out needs and relevance judgments. A healthy cluster and successful ingest do not establish search quality. Keep access/tenant/time filters through candidate generation, reranking, snippets and caches. A routing key is not an authorization boundary.

## Bulk ingestion and consistency

Use deterministic document IDs where retry semantics require them and preserve the same custom routing on index/get/update/delete. Bound bytes, items, in-flight requests and retries. Start with a measured request-size/concurrency experiment rather than importing one article's values.

HTTP 200 can contain failed bulk items. Inspect every action result and retain enough identity to retry the failed subset. Retry classified transient failures with bounded backoff; mapping/validation failures need repair or a reject path. A timeout after submission is ambiguous, and create/index/update operations have different replay semantics. Do not strip response fields required for failure identification merely to save bandwidth.

Indexing acknowledgment and search visibility are distinct. Choose refresh=false/wait_for/explicit refresh from the consistency contract and test it. A disabled refresh interval can affect wait_for behavior; retain a request deadline. Stable IDs do not by themselves guarantee exactly-once business effects.

Use versioned indexes and an authorized atomic alias change when a rebuild needs cutover. Reconcile counts, identifiers, routing, mappings and representative queries first. An alias switch does not stop producers writing to an old concrete index; account for that write path and rollback retention.

## Topology, memory and operations

Choose primary shards, replicas, node roles and failure domains from data growth, query fan-out, ingest, recovery time and availability requirements. The strict HA snapshot profile requires positive replicas; a disposable single-node or rebuild target is a different scope. Fixed five-shard, GB-per-shard, refresh or merge-policy recipes are starting experiments, not universal gates.

Monitor tail search/index latency, rejections, JVM GC/heap, native/off-heap vector memory, merges, shard skew, disk watermarks, cluster-state pressure and recovery. Raising a shard limit or reducing replicas can hide pressure while reducing resilience. Coordinate settings with the service/operator, and restore temporary load settings deliberately.

Snapshots need repository permissions, retention and an actual restore exercise. Replicas do not replace independent backups. Test rolling upgrade compatibility and index/plugin formats before relying on downgrade or rollback. The native fixture is not HA or snapshot/restore qualification.

## Security boundaries

Use deployment-owned PKI, verify hostnames and test REST/transport TLS. Demo certificates and disabled security do not satisfy the strict self-hosted production profile. A setting or certificate filename does not prove a valid trust chain, safe key handling or a successful handshake.

Test least-privilege roles, DLS/FLS/masking and combined role behavior through actual requests. Inspect unauthorized and cross-tenant cases; a role definition alone does not establish the effective permissions. Keep credentials out of logs and use the existing secret/signing mechanism, including managed-service IAM where applicable.

The initial Assay checks 11 declared settings/collections in a strict self-hosted HA/TLS/bulk profile. It does not independently discover a cluster or prove PKI, DLS/FLS, performance, relevance or recovery. Native tests deliberately use a private security-disabled single-node fixture and retain its expected production-profile Fail alongside successful API semantics. See sources.json for community/specialist claims and their disposition.
