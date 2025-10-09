from tau_bench.envs.tool import Tool
import json
from typing import Any

class NormalizeIssue(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_key: str) -> str:
        work_items = _get_table(data, "work_items")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        raw = item.get("raw") or {}
        normalized = {
            "ticket_key": ticket_key,
            "title": raw.get("title") or item.get("title"),
            "description": raw.get("description") or item.get("description"),
            "severity": raw.get("severity") or "Medium",
            "module": raw.get("module"),
        }
        item["normalized"] = normalized
        payload = normalized
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NormalizeIssue",
                "description": "Derives a normalized subset of issue fields deterministically from stored payload.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_key": {"type": "string"}},
                    "required": ["ticket_key"],
                },
            },
        }
