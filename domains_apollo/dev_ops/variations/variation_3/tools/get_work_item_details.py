from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_work_item_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str) -> str:
        pass
        work_items = data.get("work_items", [])
        for item in work_items:
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
