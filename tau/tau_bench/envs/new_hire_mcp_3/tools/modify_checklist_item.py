from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifyChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, item_id: str = None) -> str:
        updates = updates or {}
        items = data.get("checklist_items", [])
        for i in items:
            if i.get("item_id") == item_id:
                i.update(updates)
                i["updated_at"] = _fixed_now_iso()
        payload = {"updated_item_id": item_id, "updates": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateChecklistItem",
                "description": "Update a checklist task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["item_id", "updates"],
                },
            },
        }
