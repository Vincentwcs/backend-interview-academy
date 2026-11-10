# V2 Architecture and Delivery Plan

## Product direction

Backend Interview Academy is a knowledge-first learning system:
- The syllabus is the authoritative curriculum map.
- Topic lessons are maintained as independent, reviewable source files.
- Questions and answer rubrics are separate from explanatory lessons.
- The website is a generated presentation layer, not the source of truth.
- AI is an optional learning and practice engine grounded in curated content.
- Progress is learner data and must remain separate from public curriculum content.

## Repository layout target

```
backend-interview-academy/
├── index.html
├── syllabus.md
├── knowledge/
│   ├── TEMPLATE.md
│   └── <module>/<topic-id>.md
├── questions/
│   ├── README.md
│   └── <module>/<topic-id>.json
├── interview-guide/
│   ├── README.md
│   └── role-maps/
├── docs/
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
├── assets/
└── .github/workflows/deploy.yml
```

## Data ownership

| Data | Source of truth | Public? |
|---|---|---|
| Module and topic IDs, names, priority, objectives | `syllabus.md` | Yes |
| Detailed explanations | `knowledge/**/*.md` | Yes, after review |
| Question stems, choices, answer rubrics | `questions/**/*` | Yes, but answers should be separated in UI |
| Interview outlines and role maps | `interview-guide/**/*` | Yes |
| Learner progress, confidence, mistakes | Browser storage initially; private backend later | No |
| API credentials and model provider secrets | Server-side secret store only | No |

## Front-end evolution

### V2.0 — knowledge-first static site
- Keep GitHub Pages and the current no-build deployment.
- Add a syllabus-driven information architecture.
- Separate curriculum data from presentation.
- Add module overview, topic detail, interview outline, question practice, and progress views.
- Preserve current progress behavior where feasible; avoid breaking existing localStorage keys without migration.

### V2.1 — structured practice
- Add question metadata: type, difficulty, topic IDs, answer rubric, explanation, and source.
- Add confidence tracking and wrong-answer review.
- Keep answer keys out of the initial question prompt view.

### V3 — AI learning assistant
- Add a backend/serverless API proxy; never expose provider API keys in browser JavaScript.
- Retrieve relevant reviewed topic content before model generation (RAG).
- Support explain, ask-follow-up, mock-interview, code-review, and weak-area-drill modes.
- Distinguish curated knowledge from external web research; cite sources for changing/version-specific claims.
- Store user learning data privately and only with explicit user understanding/consent.

## Content quality controls

- Stable IDs must match syllabus entries.
- P0 content receives mechanism-level review and at least one practical scenario.
- Version-sensitive claims must state applicable Java/framework/database version.
- Prefer official documentation, specifications, source code, and reproducible examples.
- Avoid presenting model-generated content as reviewed fact.
- Genericize all payment examples; do not publish employer-confidential information.

## Delivery sequence

1. Publish curriculum baseline and topic template.
2. Audit the current 41 topics against the syllabus and map legacy IDs.
3. Build the syllabus-driven navigation and topic detail view.
4. Deepen P0 topics in Java, concurrency, JVM, Spring, and MySQL.
5. Add question bank and interview answer outlines.
6. Add local progress migration and review queue.
7. Design secure AI API and retrieval layer only after the knowledge corpus is stable.
