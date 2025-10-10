# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateWorkItemState(Tool):
    """Updates the state of a work item (e.g., 'open', 'closed')."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("id")
        new_state = kwargs.get("new_state")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == item_id:
                item["state"] = new_state
                return json.dumps({"status": "success", "message": f"State of work item '{item_id}' updated to '{new_state}'."})
        return json.dumps({"error": f"Work item with ID '{item_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_work_item_state",
                "description": "Updates the state of a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "new_state": {"type": "string"}
                    },
                    "required": ["id", "new_state"],
                },
            },
        }
