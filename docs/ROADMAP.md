# V2 Roadmap

## Milestone 1 — Curriculum foundation
- [x] Define a 12-module curriculum baseline.
- [x] Establish stable topic IDs and priority levels.
- [x] Define a reusable knowledge lesson template.
- [x] Audit and map the existing 41 V1 topic cards to syllabus IDs. See [V1 migration map](V1-MIGRATION-MAP.md).
- [ ] Identify missing P0 topics and duplicate/overlapping entries.

**Acceptance:** every existing topic maps to one syllabus entry; each syllabus topic has an owner status (planned/draft/reviewed).

## Milestone 2 — Knowledge-first website
- [ ] Build module and topic navigation from structured curriculum data.
- [ ] Add topic detail pages with objectives, explanation, mechanism, interview outline, misconceptions, and self-check.
- [ ] Preserve search, filtering, mastery, review marking, and existing browser progress where feasible.
- [ ] Add visible content status so planned topics are not mistaken for completed lessons.

**Acceptance:** a learner can navigate from module → topic → full lesson → questions → progress.

## Milestone 3 — Core lesson corpus
- [ ] Complete P0 lessons for Java language and collections.
- [ ] Complete P0 lessons for concurrency and JVM.
- [ ] Complete P0 lessons for Spring and MySQL.
- [ ] Add Redis, Kafka, distributed systems, and system design P0 lessons.
- [ ] Add financial technology and payment architecture case studies.

**Acceptance:** P0 topics have mechanism-level explanations, interview-ready outlines, common follow-ups, boundary conditions, and at least one applied exercise.

## Milestone 4 — Practice and review
- [ ] Add structured question data and answer rubrics.
- [ ] Record answer correctness and confidence separately.
- [ ] Build wrong-answer and low-confidence review queues.
- [ ] Add spaced review scheduling with transparent rules.

**Acceptance:** review recommendations are explainable and driven by actual performance.

## Milestone 5 — AI assistant
- [ ] Define server-side model gateway and secret handling.
- [ ] Implement retrieval over reviewed knowledge files.
- [ ] Add explain / follow-up / mock interview / code analysis / targeted drill modes.
- [ ] Add source attribution and safeguards for version-sensitive claims.

**Acceptance:** no API secret exists in static client assets; AI answers distinguish retrieved curriculum from external research.

## Non-goals for the first V2 iteration
- No public storage of personal learning records.
- No client-side model API key.
- No claim that all syllabus topics already have complete lessons.
- No premature vector database or complex microservice architecture.
