# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddChecklistItemForCandidate(Tool):
    """Create or upsert a checklist item for a candidate."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, completed_on, due_date, item_id, title, status = "pending") -> str:
        item = {
            "item_id": item_id,
            "candidate_id": candidate_id,
            "title": title,
            "due_date": due_date,
            "status": status,
            "completed_on": completed_on,
        }
        if not item["item_id"] or not item["candidate_id"]:
            return json.dumps({"error": "missing_required_fields"}, indent=2)
        data.setdefault("checklist_items", [])
        # insert or update using item_id
        for i, it in enumerate(data["checklist_items"]):
            if it.get("item_id") == item["item_id"]:
                updated = dict(it)
                updated.update({k: v for k, v in item.items() if v is not None})
                data["checklist_items"][i] = updated
                return json.dumps(updated, indent=2)
        data["checklist_items"].append(item)
        return json.dumps(item, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_checklist_item_for_candidate",
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
                    "required": ["item_id", "candidate_id"]
                }
            }
        }
