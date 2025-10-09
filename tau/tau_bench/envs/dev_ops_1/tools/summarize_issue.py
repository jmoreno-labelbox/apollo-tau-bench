from tau_bench.envs.tool import Tool
import json
from typing import Any

class SummarizeIssue(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_key: str) -> str:
        work_items = _get_table(data, "work_items")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        norm = item.get("normalized") or {}
        desc = (norm.get("description") or "")[:140]
        summary = f"{norm.get('title') or 'Issue'} :: {desc}"
        item["summary_text"] = summary
        payload = {"summary_text": summary}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeIssue",
                "description": "Creates a deterministic short summary from normalized fields.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_key": {"type": "string"}},
                    "required": ["ticket_key"],
                },
            },
        }
