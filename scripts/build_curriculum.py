#!/usr/bin/env python3
"""Compile the authoritative Markdown syllabus into a browser-friendly JSON index."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "syllabus.md"
OUTPUT = ROOT / "data" / "curriculum.json"

MODULE_RE = re.compile(r"^### (M\d{2}) — (.+)$")
TOPIC_RE = re.compile(r"^\|\s*([A-Z]+-\d{3})\s*\|\s*(.*?)\s*\|\s*(P[0-2])\s*\|\s*(.*?)\s*\|$")

def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing syllabus: {SOURCE}")
    modules = []
    current = None
    for raw in SOURCE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        module_match = MODULE_RE.match(line)
        if module_match:
            current = {
                "id": module_match.group(1),
                "title": module_match.group(2).strip(),
                "outcome": "",
                "topics": [],
            }
            modules.append(current)
            continue
        if current and line.startswith("**Outcome:**"):
            current["outcome"] = line.replace("**Outcome:**", "", 1).strip()
            continue
        topic_match = TOPIC_RE.match(line)
        if topic_match and current:
            topic_id, title, priority, scope = topic_match.groups()
            current["topics"].append({
                "id": topic_id,
                "title": title.strip(),
                "priority": priority,
                "scope": scope.strip(),
                "status": "outline",
            })

    topic_count = sum(len(m["topics"]) for m in modules)
    if len(modules) != 12:
        raise SystemExit(f"Expected 12 modules, parsed {len(modules)}")
    if topic_count < 100:
        raise SystemExit(f"Expected at least 100 topics, parsed {topic_count}")
    all_ids = [t["id"] for m in modules for t in m["topics"]]
    if len(all_ids) != len(set(all_ids)):
        raise SystemExit("Duplicate topic IDs found in syllabus")

    payload = {
        "schema_version": 1,
        "source": "syllabus.md",
        "module_count": len(modules),
        "topic_count": topic_count,
        "modules": modules,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)}: {len(modules)} modules, {topic_count} topics")

if __name__ == "__main__":
    main()
