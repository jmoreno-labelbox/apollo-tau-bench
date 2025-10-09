from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWorkItemAssignee(Tool):
    """Fetches the assignee for a work item."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        item_id: str = None
    ) -> str:
        work_items = data.get("work_items", {}).values()
        for item in work_items:
            if item.get("id") == item_id:
                payload = {"assignee_id": item.get("assignee_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Work item with ID '{item_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWorkItemAssignee",
                "description": "Retrieves the assignee for a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
