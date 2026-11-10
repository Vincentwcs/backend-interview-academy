# Question Bank

Question files are organized by module and topic ID.

Recommended JSON shape:

```json
{
  "topic_id": "JAVA-004",
  "version": 1,
  "questions": [
    {
      "id": "JAVA-004-Q001",
      "type": "single_choice",
      "difficulty": "intermediate",
      "prompt": "Question text",
      "options": [{"id": "A", "text": "..."}, {"id": "B", "text": "..."}],
      "answer": ["B"],
      "explanation": "Reasoning and relevant boundaries",
      "follow_ups": ["..."],
      "tags": ["generics", "type-erasure"],
      "source": []
    }
  ]
}
```

Keep answer keys and explanations in the data source, but reveal them only after the learner submits an answer. Record learner responses separately from this public repository.
