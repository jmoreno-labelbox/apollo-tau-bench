# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_work_item(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], work_item_id: str, updates: Dict[str, Any]) -> str:
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get('id') == work_item_id:
                item.update(updates)
                data["work_items"] = work_items
                return json.dumps({"success": f"Work item '{work_item_id}' was updated."}, indent=2)
        return json.dumps({"error": f"Work item '{work_item_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "update_work_item", "description": "Updates one or more fields of an existing work item.", "parameters": { "type": "object", "properties": { "work_item_id": { "type": "string" }, "updates": { "type": "object", "description": "A dictionary of fields to update." } }, "required": ["work_item_id", "updates"] } } }
