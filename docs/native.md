# Native qualification

These scripts create only disposable local fixtures. PostgreSQL/OpenSearch use pinned official container digests, no published ports, a private no-network container, bounded CPU/memory and cleanup of their own named container/volume. They do not stop or alter existing containers. Native startup can take longer than the audit command runner's 30-second deadline, so the separate qualification coordinator allows 240 seconds per trusted test process.

Requires an already running Docker daemon and the pinned Linux image. No daemon or host configuration is changed.

```sh
docker pull opensearchproject/opensearch:3.9.0@sha256:3bf4fe26aeb9f7b03c0ebcb1302bb24e855ee6b89fd926d26a71a83ef6f7e076
python3 eng/qualify.py --native
```

The fixture intentionally disables production security controls inside its isolated test environment. The native API/SQL tests can Pass while its strict production snapshot correctly remains Fail. This distinction is retained in qualification evidence.

Outputs are retained under ignored artifacts/. The coordinator binds native result/snapshot identities and assesses the exported evidence through the independent zipapp. Its acceptance command checks the retained native result and snapshot integrity; it does not pretend to rerun the original engine after it has been cleaned up.
