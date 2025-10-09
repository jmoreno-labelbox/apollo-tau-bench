from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_work_item_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str) -> str:
        pass
        work_items = data.get("work_items", {}).values()
        for item in work_items.values():
            if item.get("id") == work_item_id:
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Work item '{work_item_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getWorkItemDetails",
                "description": "Retrieves the full details for a given work item.",
                "parameters": {
                    "type": "object",
                    "properties": {"work_item_id": {"type": "string"}},
                    "required": ["work_item_id"],
                },
            },
        }
