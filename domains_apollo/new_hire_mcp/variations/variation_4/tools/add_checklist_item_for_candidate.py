from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class AddChecklistItemForCandidate(Tool):
    """Establish or insert a checklist item for a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, candidate_id: str = None, title: str = None, due_date: str = None, status: str = "pending", completed_on: str = None) -> str:
        item = {
            "item_id": item_id,
            "candidate_id": candidate_id,
            "title": title,
            "due_date": due_date,
            "status": status,
            "completed_on": completed_on,
        }
        if not item["item_id"] or not item["candidate_id"]:
            payload = {"error": "missing_required_fields"}
            out = json.dumps(payload, indent=2)
            return out
        data.setdefault("checklist_items", [])
        #insert or update using item_id
        for i, it in enumerate(data["checklist_items"]):
            if it.get("item_id") == item["item_id"]:
                updated = dict(it)
                updated.update({k: v for k, v in item.items() if v is not None})
                data["checklist_items"][i] = updated
                payload = updated
                out = json.dumps(payload, indent=2)
                return out
        data["checklist_items"].append(item)
        payload = item
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addChecklistItemForCandidate",
                "description": "Create or upsert a checklist item for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                        "title": {"type": "string"},
                        "due_date": {"type": "string"},
                        "status": {"type": "string"},
                        "completed_on": {"type": "string"},
                    },
                    "required": ["item_id", "candidate_id"],
                },
            },
        }
