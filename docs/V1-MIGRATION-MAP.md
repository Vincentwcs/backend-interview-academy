# V1 → V2 Topic Migration Map

This map preserves continuity between the original 41 V1 learning cards and the canonical V2 syllabus IDs. V1 cards sometimes combine multiple concepts; one legacy card may therefore map to more than one canonical topic. Existing browser progress uses legacy keys and must be migrated deliberately rather than discarded.

| V1 module | Existing V1 card | V2 canonical topic IDs | Migration note |
|---|---|---|---|
| Java 基础与集合 | Java 内存模型与变量 | JAVA-002, JVM-001 | Split Java variable semantics from JVM runtime storage; do not teach stack/heap as an absolute allocation rule. |
| Java 基础与集合 | 集合框架：List / Set / Map | COLL-001, COLL-002, COLL-005 | Separate framework hierarchy from concrete List and Set implementations. |
| Java 基础与集合 | HashMap 底层原理 | COLL-003 | Keep as a dedicated mechanism-level lesson. |
| Java 基础与集合 | 泛型与类型擦除 | JAVA-004 | Expand invariance, PECS, bounds, bridge methods, and type erasure boundaries. |
| Java 基础与集合 | equals 与 hashCode | JAVA-010 | Include contracts, mutable keys, and hash-based collection behavior. |
| Java 基础与集合 | 反射、注解与动态代理 | JAVA-006, SPR-003 | Split reflection/annotations from Spring proxy/AOP implementation. |
| 并发编程与线程安全 | 线程创建与生命周期 | CONC-001 | Add interruption, Future, and lifecycle distinctions. |
| 并发编程与线程安全 | Java 内存模型与 happens-before | CONC-002, CONC-003 | Separate JMM concepts from volatile and happens-before rules. |
| 并发编程与线程安全 | synchronized 与锁升级 | CONC-004, CONC-011 | Teach monitor semantics separately from version-sensitive lock optimizations. |
| 并发编程与线程安全 | AQS 与 ReentrantLock | CONC-005 | Expand queueing, state, fairness, interruption, and Condition. |
| 并发编程与线程安全 | 线程池与任务拒绝 | CONC-007 | Add sizing, queueing, isolation, and overload control. |
| 并发编程与线程安全 | ConcurrentHashMap | COLL-004, CONC-009 | Cross-link collection implementation and concurrency concepts. |
| JVM 与性能调优 | JVM 运行时数据区 | JVM-001 | Deepen stack frames, method area/metaspace, and thread ownership. |
| JVM 与性能调优 | 对象创建与内存布局 | JVM-002 | Add allocation path, TLAB, headers, and alignment. |
| JVM 与性能调优 | 垃圾回收算法与收集器 | JVM-003, JVM-004 | Separate reachability from collectors and algorithms. |
| JVM 与性能调优 | 类加载机制与双亲委派 | JAVA-007, JVM-006 | Cross-link Java class initialization and JVM loading lifecycle. |
| JVM 与性能调优 | JIT、逃逸分析与标量替换 | JVM-007, JVM-008 | Explain hotspot compilation, escape categories, scalar replacement, and limits. |
| JVM 与性能调优 | 线上故障诊断 | JVM-005, JVM-009, JVM-010 | Split GC tuning, diagnostic tooling, and failure patterns. |
| Spring / Spring Boot | IoC 容器与 Bean 生命周期 | SPR-001, SPR-002 | Dedicated lifecycle timeline and extension-point ordering. |
| Spring / Spring Boot | 自动配置与条件装配 | SPR-006, SPR-007 | Split configuration conditions from application startup sequence. |
| Spring / Spring Boot | AOP 与代理机制 | SPR-003 | Include JDK/CGLIB, proxy boundaries, and self-invocation. |
| Spring / Spring Boot | Spring 事务传播与隔离 | SPR-004 | Include propagation, rollback, isolation, and transaction manager boundaries. |
| Spring / Spring Boot | Spring MVC 请求链路 | SPR-005, SPR-010 | Cross-link request dispatch and validation/exception handling. |
| MySQL / 数据库 | B+ 树索引与索引设计 | DB-002, DB-003 | Separate tree structure from practical index design. |
| MySQL / 数据库 | 事务 ACID 与隔离级别 | DB-005, DB-006 | Explain anomalies and InnoDB implementation boundaries. |
| MySQL / 数据库 | MVCC、Read View 与 Undo Log | DB-007 | Deepen version chain and RC/RR visibility rules. |
| MySQL / 数据库 | Redo Log、Binlog 与两阶段提交 | DB-008 | Include commit timeline and crash recovery. |
| MySQL / 数据库 | 行锁、间隙锁与 Next-Key Lock | DB-009, DB-010 | Split lock types from locking reads, access paths, and deadlocks. |
| MySQL / 数据库 | SQL 调优与执行计划 | DB-001, DB-011 | Split SQL execution concepts from optimization workflow. |
| Redis / Kafka / 分布式系统 | Redis 数据结构与应用边界 | REDIS-001, REDIS-003 | Separate structures from execution model. |
| Redis / Kafka / 分布式系统 | 缓存一致性与穿透击穿雪崩 | REDIS-004, REDIS-005, REDIS-006 | Split expiry/eviction, consistency, and cache failure patterns. |
| Redis / Kafka / 分布式系统 | Kafka 分区、顺序与消费组 | MQ-002, MQ-004, MQ-006 | Separate architecture, consumer groups, and ordering. |
| Redis / Kafka / 分布式系统 | 消息可靠性与重复消费 | MQ-003, MQ-005, MQ-007, MQ-008 | Split producer, delivery semantics, idempotency, and retry/DLQ. |
| Redis / Kafka / 分布式系统 | 分布式事务与最终一致性 | DIST-004, DIST-005, MQ-010 | Cross-link transaction patterns, consistency, and messaging transaction patterns. |
| Redis / Kafka / 分布式系统 | 幂等、去重与状态机 | DIST-003, MQ-007 | Shared concept; retain one canonical lesson with cross-links. |
| 金融清算与架构实战 | 跨境支付端到端链路 | FIN-001, FIN-012 | Split lifecycle and platform architecture case study. |
| 金融清算与架构实战 | CIPS / SWIFT / ISO 20022 | FIN-003, FIN-005, FIN-006 | Separate scheme concepts, SWIFT messaging, and ISO 20022 data model. |
| 金融清算与架构实战 | 清算分账与账务一致性 | FIN-002, FIN-008 | Separate clearing/settlement concepts from ledger/accounting invariants. |
| 金融清算与架构实战 | 高并发下的可靠性设计 | DIST-007, DIST-010, ARCH-003 | Cross-link resilience patterns, reliability engineering, and high-concurrency architecture. |
| 金融清算与架构实战 | 对账体系与差错闭环 | FIN-009, FIN-014, DIST-011 | Split reconciliation, recovery controls, and distributed reconciliation. |
| 金融清算与架构实战 | 架构设计题：跨境支付平台 | ARCH-001, ARCH-002, ARCH-010, FIN-012 | Use as an integrated capstone, not a standalone factual article. |

## Progress migration policy

- Keep V1 localStorage key `baa-progress` readable during the transition.
- Add a one-time mapping from legacy card keys (`module-index`) to canonical topic IDs.
- When one legacy card maps to multiple topics, do not mark all targets mastered automatically. Preserve the legacy completion as a migration hint and ask the learner to confirm the split topics.
- Never upload local progress to the public repository.
