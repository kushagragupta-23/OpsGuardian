# Runbook: OOMKilled
Evidence required: pod status reason OOMKilled or exit code 137 plus memory usage near the configured limit.
Mitigation: rollback a memory regression, fix unbounded allocation/cache growth, or raise memory only after capacity review. A restart is temporary mitigation, not root-cause resolution.
