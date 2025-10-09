from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class update_work_item(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str, updates: dict[str, Any]) -> str:
        pass
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == work_item_id:
                item.update(updates)
                data["work_items"] = work_items
                payload = {"success": f"Work item '{work_item_id}' was updated."}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Work item '{work_item_id}' not found."}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWorkItem",
                "description": "Updates one or more fields of an existing work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields to update.",
                        },
                    },
                    "required": ["work_item_id", "updates"],
                },
            },
        }
