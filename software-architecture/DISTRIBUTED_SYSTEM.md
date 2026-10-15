# Fundamentals of Distributed Systems

## Properties of a Reliable Application
- Idempotency
  - Use alternet/unique key that is usually generated on the client-side
  - CQRS
- Immutability
  - Make all data immutable
  - Realiable audit log
  - Do not destroy data
  - Preserve metadata
  - Promote eventual consistency
- Location Independence
- Versioning

## Fallacies of Distributed Computing
- The network is reliable
- Latency is zero
- Bandwidth is infinite
- The network is secure
- Topology doesn't change
- There is one administrator
- Transport cost is zero
- The network is homogeneous

## Immutability Patterns
- Snapshots
- Tombstones
