# Backend Interview Academy — Syllabus

> Version: 2.0-draft  
> Status: Curriculum baseline  
> This file is the single source of truth for curriculum scope, module IDs, topic IDs, priority, and learning objectives. Detailed lessons live under `knowledge/`; questions live under `questions/`. Do not silently change topic IDs after progress data has been recorded.

## Learning outcomes

A learner should be able to:
1. Explain core mechanisms accurately, not merely recite definitions.
2. Read code and reason about compilation, runtime behavior, concurrency, and failure modes.
3. Design reliable backend services and explain trade-offs.
4. Diagnose production-style problems using evidence and a structured method.
5. Present concise, layered interview answers and handle follow-up questions.
6. Translate domain complexity into clear data, consistency, and architecture models.

## Priority and depth

- **P0 — Core:** expected in most experienced Java backend interviews; requires mechanism-level understanding and interview-ready expression.
- **P1 — Important:** frequently tested or differentiating; requires practical application and common edge cases.
- **P2 — Advanced / differentiating:** role-dependent depth; understand design trade-offs and know where to investigate further.

Depth labels:
- **D1 Concept:** define, purpose, and boundaries.
- **D2 Mechanism:** internal implementation, execution path, invariants.
- **D3 Application:** code, troubleshooting, design trade-offs, and interview expression.

## Curriculum map

### M01 — Java language and core foundations
**Outcome:** reason about Java type semantics, object behavior, APIs, and language/runtime boundaries.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| JAVA-001 | Object model and OOP | P0 | Encapsulation, inheritance, polymorphism, composition vs inheritance, equals/hashCode/toString contracts |
| JAVA-002 | Types, wrappers and boxing | P0 | Primitive/reference types, boxing cache, null, numeric conversion, overflow |
| JAVA-003 | String and immutability | P0 | String pool, immutability, StringBuilder/StringBuffer, concatenation |
| JAVA-004 | Generics and type erasure | P0 | Generic classes/methods, bounds, wildcards, PECS, invariance, bridge methods, reifiable types |
| JAVA-005 | Exceptions | P1 | Checked/unchecked, propagation, custom exceptions, try-with-resources, suppression |
| JAVA-006 | Reflection and annotations | P1 | Reflection API, runtime metadata, annotation processing concepts, dynamic invocation |
| JAVA-007 | Class loading basics | P0 | Loading/linking/initialization, initialization triggers, parent delegation, class identity |
| JAVA-008 | Java 8+ language features | P1 | Lambda, functional interfaces, streams, Optional, method references, default methods |
| JAVA-009 | I/O and serialization | P1 | Byte/character streams, NIO concepts, serialization risks and alternatives |
| JAVA-010 | Common API contracts | P0 | Comparable/Comparator, equals/hashCode, clone, immutability, defensive copying |

### M02 — Collections and data structures
**Outcome:** select collections based on ordering, complexity, concurrency, and memory behavior.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| COLL-001 | Collection framework hierarchy | P0 | Collection/Map, List/Set/Queue, interface vs implementation |
| COLL-002 | ArrayList and LinkedList | P0 | Storage, complexity, resizing, traversal, realistic trade-offs |
| COLL-003 | HashMap | P0 | Hash spread, buckets, collision, treeification, resize, null handling |
| COLL-004 | ConcurrentHashMap | P0 | Concurrent access, CAS, synchronized bins, resize cooperation, consistency |
| COLL-005 | HashSet, TreeSet and Map views | P1 | Uniqueness, ordering, backing map, comparator consistency |
| COLL-006 | TreeMap and sorted structures | P1 | Red-black tree concepts, range queries, comparator |
| COLL-007 | Queue, Deque and PriorityQueue | P1 | FIFO/LIFO, heap, blocking queue distinctions |
| COLL-008 | Iterator and fail-fast | P0 | Iterator contract, modCount, ConcurrentModificationException, safe removal |
| COLL-009 | Complexity and data structure selection | P0 | Big-O, amortized analysis, heap, stack, queue, hash table, tree |

### M03 — Concurrency and thread safety
**Outcome:** explain Java Memory Model guarantees, coordinate concurrent work, and diagnose races/deadlocks.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| CONC-001 | Thread lifecycle and creation | P0 | Thread/Runnable/Callable, Future, lifecycle, interruption |
| CONC-002 | Java Memory Model | P0 | Main memory, working memory model, visibility, atomicity, ordering |
| CONC-003 | volatile and happens-before | P0 | Visibility, ordering, limits of volatile, happens-before rules |
| CONC-004 | synchronized and monitor | P0 | Monitor semantics, reentrancy, lock release/acquire, wait/notify |
| CONC-005 | Lock and AQS | P1 | ReentrantLock, Condition, AQS queue, fairness, interruptible lock |
| CONC-006 | CAS and atomic classes | P1 | Compare-and-set, ABA, AtomicStampedReference, contention |
| CONC-007 | Thread pools | P0 | Core/max size, queue, rejection policies, lifecycle, sizing, task isolation |
| CONC-008 | CompletableFuture | P1 | Composition, exception paths, executor selection, blocking hazards |
| CONC-009 | Concurrent collections | P1 | ConcurrentHashMap, blocking queues, copy-on-write, weak consistency |
| CONC-010 | Deadlock and concurrency defects | P0 | Deadlock conditions, lock ordering, starvation, livelock, race conditions |
| CONC-011 | Lock optimization | P1 | Biased/stack/lightweight lock historical context, inflation, contention, JIT interaction |
| CONC-012 | Parallel streams and ForkJoinPool | P2 | Work stealing, common pool, blocking task risks |

### M04 — JVM and performance
**Outcome:** connect runtime memory, class loading, garbage collection, JIT, and observability to production behavior.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| JVM-001 | Runtime data areas | P0 | Heap, stacks, PC register, native method stack, method area/metaspace |
| JVM-002 | Object allocation and layout | P1 | Object headers, alignment, references, allocation path |
| JVM-003 | Garbage collection roots | P0 | GC roots, reachability, reference types, finalization caveats |
| JVM-004 | Garbage collectors | P0 | Serial, Parallel, CMS historical context, G1, ZGC, Shenandoah concepts |
| JVM-005 | GC tuning and diagnosis | P1 | Heap sizing, pause goals, GC logs, allocation rate, promotion, OOM analysis |
| JVM-006 | Class loading mechanism | P0 | Loading, verification, preparation, resolution, initialization, loaders |
| JVM-007 | Bytecode and execution engine | P1 | Class file, interpreter, JIT compilation, tiered compilation |
| JVM-008 | JIT and runtime optimization | P1 | Inlining, devirtualization, escape analysis, scalar replacement, lock elimination |
| JVM-009 | JVM troubleshooting tools | P1 | jcmd, jstack, jmap, jstat, JFR, heap dump, thread dump |
| JVM-010 | Common memory and thread failures | P0 | OOM variants, StackOverflowError, native memory, thread exhaustion |

### M05 — Spring and Spring Boot
**Outcome:** explain container lifecycle, proxy-based AOP, transaction semantics, request flow, and auto-configuration.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| SPR-001 | IoC and dependency injection | P0 | Bean definitions, creation, dependency resolution, scopes |
| SPR-002 | Bean lifecycle and extension points | P0 | Instantiation, populate properties, aware callbacks, post-processors, init/destroy |
| SPR-003 | AOP and proxies | P0 | JDK/CGLIB proxies, join points, advice, self-invocation, proxy boundaries |
| SPR-004 | Spring transactions | P0 | Proxy interception, propagation, isolation, rollback rules, self-invocation |
| SPR-005 | Spring MVC request lifecycle | P1 | DispatcherServlet, HandlerMapping, adapters, converters, exception handling |
| SPR-006 | Auto-configuration | P1 | Conditions, configuration classes, imports, properties, ordering |
| SPR-007 | Spring Boot startup | P1 | ApplicationContext refresh, runners, lifecycle events |
| SPR-008 | Configuration and profiles | P1 | Property sources, precedence, binding, externalized configuration |
| SPR-009 | Events and extension mechanisms | P2 | Application events, listeners, factories, post-processors |
| SPR-010 | Validation and exception handling | P1 | Validation pipeline, binding errors, global handlers |
| SPR-011 | Spring Security fundamentals | P2 | Filter chain, authentication, authorization, security context |
| SPR-012 | Spring integration testing | P1 | Test slices, context caching, mocks, transaction test behavior |

### M06 — Relational databases and MySQL/InnoDB
**Outcome:** understand storage/index structures, transaction isolation, locking, logging, and query performance.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| DB-001 | Relational model and SQL execution | P0 | Logical query processing, joins, aggregation, execution plan |
| DB-002 | B+Tree indexes | P0 | Page structure, fanout, height, clustered/secondary indexes |
| DB-003 | Index design and usage | P0 | Composite indexes, leftmost prefix, covering index, ICP, selectivity |
| DB-004 | InnoDB storage architecture | P1 | Tablespaces, pages, buffer pool, change buffer, adaptive hash concepts |
| DB-005 | Transactions and ACID | P0 | Atomicity, consistency, isolation, durability |
| DB-006 | Isolation levels and anomalies | P0 | RU/RC/RR/Serializable, dirty/non-repeatable/phantom reads |
| DB-007 | MVCC and Read View | P0 | Undo versions, transaction IDs, visibility rules, RC vs RR |
| DB-008 | Undo, redo and binlog | P0 | Roles, write-ahead logging, commit path, crash recovery, two-phase commit |
| DB-009 | Locks and lock granularity | P0 | Record/gap/next-key/insert-intention locks, intention locks |
| DB-010 | Locking reads and deadlocks | P0 | FOR UPDATE, index access paths, lock order, deadlock detection |
| DB-011 | SQL optimization | P0 | EXPLAIN, cardinality, join algorithms, filesort, temporary tables |
| DB-012 | Schema and index engineering | P1 | Data types, normalization, denormalization, online DDL |
| DB-013 | Replication and high availability | P1 | Binlog replication, GTID, semi-sync concepts, failover |
| DB-014 | Connection pools and database capacity | P1 | Pool sizing, queueing, timeout, saturation, transaction duration |
| DB-015 | Distributed database concepts | P2 | Sharding, routing, global IDs, distributed transactions, consistency trade-offs |

### M07 — Redis and caching
**Outcome:** design caches with explicit consistency, availability, and failure strategies.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| REDIS-001 | Redis data structures | P0 | String, Hash, List, Set, ZSet, Stream, encoding concepts |
| REDIS-002 | Persistence | P1 | RDB, AOF, rewrite, fsync policies, recovery |
| REDIS-003 | Single-threaded event loop | P1 | Command execution, I/O multiplexing, blocking operations |
| REDIS-004 | Expiration and eviction | P0 | Expiration strategies, maxmemory policies, lazy deletion |
| REDIS-005 | Cache consistency | P0 | Cache-aside, invalidation, delayed double delete caveats, outbox/event approaches |
| REDIS-006 | Cache penetration, breakdown and avalanche | P0 | Bloom filters, null caching, mutex, logical expiry, jitter |
| REDIS-007 | Distributed locks | P1 | SET NX PX, ownership token, release safety, lease expiry, fencing token |
| REDIS-008 | Replication and Sentinel | P1 | Replication, failover, split-brain and data loss windows |
| REDIS-009 | Cluster and sharding | P1 | Hash slots, resharding, multi-key constraints |
| REDIS-010 | Redis performance and operations | P1 | Big keys, hot keys, latency, slowlog, memory analysis |

### M08 — Messaging and Kafka
**Outcome:** design reliable asynchronous processing and explain delivery, ordering, replay, and idempotency.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| MQ-001 | Messaging fundamentals | P0 | Producer, broker, consumer, queue/topic, async decoupling |
| MQ-002 | Kafka architecture | P0 | Topic, partition, replica, leader/follower, ISR |
| MQ-003 | Producer reliability | P0 | Acks, retries, idempotent producer, batching, ordering |
| MQ-004 | Consumer groups and offsets | P0 | Assignment, rebalance, commit modes, offset semantics |
| MQ-005 | Delivery semantics | P0 | At-most-once, at-least-once, effectively-once boundaries |
| MQ-006 | Message ordering | P1 | Partition key, per-partition ordering, sequence control |
| MQ-007 | Duplicate prevention and idempotency | P0 | Business keys, deduplication store, state transitions, idempotent effects |
| MQ-008 | Retry and dead-letter handling | P1 | Retry topics, backoff, poison messages, replay |
| MQ-009 | Message loss and backlog diagnosis | P1 | Producer/broker/consumer failure points, lag, throughput |
| MQ-010 | Transactional messaging patterns | P1 | Outbox, local transaction + event, Kafka transactions boundaries |

### M09 — Distributed systems and service architecture
**Outcome:** design dependable services under partial failure, concurrency, and scale.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| DIST-001 | Network and HTTP fundamentals | P0 | TCP lifecycle, HTTP, TLS concepts, timeout layers |
| DIST-002 | RPC and service communication | P1 | REST, gRPC concepts, serialization, connection management |
| DIST-003 | Idempotency and deduplication | P0 | Request identity, state machine, storage constraints, replay safety |
| DIST-004 | Distributed transactions | P1 | 2PC, TCC, Saga, local transaction, compensation |
| DIST-005 | Consistency models | P1 | Strong/eventual consistency, read-your-writes, ordering |
| DIST-006 | Distributed locks and coordination | P1 | Lease, fencing, consensus service concepts, failure windows |
| DIST-007 | Resilience patterns | P0 | Timeout, retry, circuit breaker, bulkhead, rate limit |
| DIST-008 | Load balancing and service discovery | P1 | Client/server-side balancing, health checks, discovery |
| DIST-009 | Observability | P0 | Logs, metrics, traces, correlation IDs, SLI/SLO |
| DIST-010 | Reliability engineering | P1 | Availability, graceful degradation, recovery, capacity, error budgets |
| DIST-011 | Data consistency and reconciliation | P0 | State reconciliation, compensation, periodic checks, exception queues |
| DIST-012 | Security fundamentals | P1 | Authentication, authorization, secrets, encryption, audit, least privilege |

### M10 — System design and backend engineering
**Outcome:** turn requirements into a scalable, operable, and explainable design.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| ARCH-001 | Requirements and workload modeling | P0 | Functional/non-functional requirements, QPS, throughput, latency, storage |
| ARCH-002 | API and domain modeling | P0 | Contracts, state transitions, validation, domain boundaries |
| ARCH-003 | High-concurrency design | P0 | Queues, partitioning, contention, backpressure, resource isolation |
| ARCH-004 | High availability and disaster recovery | P0 | Redundancy, failover, RTO/RPO, backup and restore |
| ARCH-005 | Data architecture | P1 | Ownership, read/write paths, CQRS concepts, schema evolution |
| ARCH-006 | Capacity and performance engineering | P1 | Load testing, bottleneck analysis, Little's Law, saturation |
| ARCH-007 | Deployment and release safety | P1 | Rolling, blue-green, canary, rollback, compatibility |
| ARCH-008 | Production troubleshooting | P0 | Incident framing, evidence, hypothesis, mitigation, root cause |
| ARCH-009 | Technical decision-making | P1 | Trade-off analysis, ADR, build vs buy, operational cost |
| ARCH-010 | Architecture communication | P0 | Context/container/component views, sequence diagrams, risk explanation |

### M11 — Coding, algorithms, and engineering quality
**Outcome:** solve practical coding tasks and produce maintainable, testable services.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| CODE-001 | Complexity analysis | P0 | Time/space complexity, worst/average/amortized |
| CODE-002 | Arrays, strings and hash tables | P0 | Two pointers, sliding window, prefix sums, frequency maps |
| CODE-003 | Linked lists, stacks and queues | P1 | Pointer manipulation, monotonic stack/queue |
| CODE-004 | Trees, heaps and graphs | P1 | Traversal, BST, heap, BFS/DFS, shortest path concepts |
| CODE-005 | Sorting and searching | P0 | Binary search boundaries, sorting complexity |
| CODE-006 | Dynamic programming and greedy | P2 | State definition, transitions, proof intuition |
| CODE-007 | Clean code and SOLID | P0 | SRP, OCP, LSP, ISP, DIP, cohesion/coupling |
| CODE-008 | Design patterns | P1 | Strategy, factory, template, chain of responsibility, observer, decorator |
| CODE-009 | Testing strategy | P0 | Unit/integration/contract tests, test doubles, boundary cases |
| CODE-010 | Build and delivery | P1 | Maven/Gradle, dependency management, CI, artifact lifecycle |

### M12 — Financial technology, clearing, and payment architecture
**Outcome:** articulate payment-domain workflows and derive technical designs from financial correctness requirements.

| Topic ID | Topic | Priority | Learning scope |
|---|---|---:|---|
| FIN-001 | Payment lifecycle and state model | P0 | Initiation, validation, routing, clearing, settlement, notification |
| FIN-002 | Clearing vs settlement | P0 | Roles, obligations, net/gross settlement, timing |
| FIN-003 | CIPS and cross-border RMB payment concepts | P1 | Participants, message flow, business roles, operational boundaries |
| FIN-004 | Domestic/foreign-currency clearing concepts | P1 | Currency paths, FXPS context, routing and clearing responsibilities |
| FIN-005 | SWIFT messaging | P1 | FIN, MT concepts, FINplus, ISO 20022 message families and mapping |
| FIN-006 | ISO 20022 data model | P1 | Message structure, parties, agents, identifiers, validation |
| FIN-007 | Inquiry/response and exception handling | P0 | Correlation, timeout, duplicate response, unmatched flow, manual repair |
| FIN-008 | Ledger and accounting consistency | P0 | Shadow ledger, posting, internal transfer, accounting invariants |
| FIN-009 | Reconciliation and closed-loop control | P0 | Internal/external reconciliation, break management, evidence |
| FIN-010 | Payment idempotency and duplicate control | P0 | End-to-end keys, channel retries, state transitions, exactly-once limits |
| FIN-011 | High-volume payment processing | P1 | Partitioning, batching, ordering, backpressure, throughput |
| FIN-012 | Payment platform architecture case study | P0 | Inbound/outbound flows, adapters, orchestration, ledger, callbacks, observability |
| FIN-013 | Risk, compliance and auditability | P1 | Screening integration concepts, audit trail, traceability, data protection |
| FIN-014 | Failure recovery and operational controls | P0 | Replay, compensation, suspense queues, manual intervention, recovery drills |

## Topic content contract

Every topic should have:
- Stable topic ID and title.
- Prerequisites and related topics.
- Explicit learning objectives and priority.
- Core explanation and mechanism.
- Example or execution flow where useful.
- Common misconceptions and boundary conditions.
- Interview outline, common questions, and follow-ups.
- Practical scenario or diagnostic exercise.
- Self-check questions and answer rationale.
- References with source/version/date where applicable.

See [knowledge/TEMPLATE.md](knowledge/TEMPLATE.md).

## Learning workflow

1. **Map:** choose a module or topic from this syllabus.
2. **Learn:** read the topic lesson and inspect mechanisms/examples.
3. **Recall:** answer questions before viewing the reference answer.
4. **Explain:** produce a 1-minute and 3-minute interview answer.
5. **Apply:** solve a code, diagnosis, or design scenario.
6. **Assess:** record correctness, confidence, and evidence.
7. **Review:** schedule review based on demonstrated mastery, not only elapsed time.

## Personalization boundary

The curriculum may include generic payment and clearing architecture concepts. Do not publish employer-specific system names, internal topology, credentials, production code, real transaction data, private incident details, or personal compensation and identity information.
