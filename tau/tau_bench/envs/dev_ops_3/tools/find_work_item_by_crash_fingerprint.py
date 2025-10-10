# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_work_item_by_crash_fingerprint(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], fingerprint: str) -> str:
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("metadata") and fingerprint in item["metadata"].get("crash_fingerprint", ""):
                return json.dumps(item, indent=2)
        return json.dumps({"error": f"Work item with crash fingerprint '{fingerprint}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "find_work_item_by_crash_fingerprint", "description": "Finds a work item by its associated crash fingerprint.", "parameters": { "type": "object", "properties": { "fingerprint": { "type": "string" } }, "required": ["fingerprint"] } } }
