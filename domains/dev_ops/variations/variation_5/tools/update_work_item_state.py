from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateWorkItemState(Tool):
    """Modifies the status of a work item (e.g., 'open', 'closed')."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        item_id: str = None,
        new_state: str = None
    ) -> str:
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == item_id:
                item["state"] = new_state
                payload = {
                    "status": "success",
                    "message": f"State of work item '{item_id}' updated to '{new_state}'.",
                }
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
                "name": "UpdateWorkItemState",
                "description": "Updates the state of a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "new_state": {"type": "string"},
                    },
                    "required": ["id", "new_state"],
                },
            },
        }
