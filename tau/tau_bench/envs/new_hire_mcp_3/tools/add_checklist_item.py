from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item: dict = None) -> str:
        new_item = item or {}
        items = data.get("checklist_items", {}).values()
        data["checklist_items"][new_item["checklist_item_id"]] = new_item
        data["checklist_items"] = items
        payload = {"added_item": new_item}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addChecklistItem",
                "description": "Add a new checklist item.",
                "parameters": {
                    "type": "object",
                    "properties": {"item": {"type": "object"}},
                    "required": ["item"],
                },
            },
        }
