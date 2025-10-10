# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_work_item_details(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], work_item_id: str) -> str:
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get('id') == work_item_id:
                return json.dumps(item, indent=2)
        return json.dumps({"error": f"Work item '{work_item_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "get_work_item_details", "description": "Retrieves the full details for a given work item.", "parameters": { "type": "object", "properties": { "work_item_id": { "type": "string" } }, "required": ["work_item_id"] } } }
