from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class CloseCompletedChecklistItems(Tool):
    @staticmethod
    def invoke(db: dict[str, Any], candidate_id: str, due_date_lte: str = None) -> str:
        items = db.get("checklist_items", [])
        updated = 0
        for it in items:
            if it.get("candidate_id") != candidate_id:
                continue
            if it.get("status") != "Completed":
                continue
            if it.get("completed_ts"):
                continue
            if due_date_lte and it.get("due_date") and it["due_date"] > due_date_lte:
                continue
            it["completed_ts"] = _fixed_ts(None)
            updated += 1
        payload = {"updated": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CloseCompletedChecklistItems",
                "description": "Backfill completed_ts for completed checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "due_date_lte": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }
