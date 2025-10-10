# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWorkItemAssignee(Tool):
    """Retrieves the assignee for a work item."""
    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        item_id = id
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == item_id:
                return json.dumps({"assignee_id": item.get("assignee_id")})
        return json.dumps({"error": f"Work item with ID '{item_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_work_item_assignee",
                "description": "Retrieves the assignee for a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
