from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RemoveChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None) -> str:
        items = data.get("checklist_items", [])
        data["checklist_items"] = [i for i in items if i.get("item_id") != item_id]
        payload = {"removed_item_id": item_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveChecklistItem",
                "description": "Remove a checklist item by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"item_id": {"type": "string"}},
                    "required": ["item_id"],
                },
            },
        }
