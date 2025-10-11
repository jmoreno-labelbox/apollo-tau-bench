# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListWarehousesByCapability(Tool):
    """A tool to find all warehouses that hold a specific certification."""
    @staticmethod
    def invoke(data: Dict[str, Any], certification) -> str:
        if not certification:
            return json.dumps({"error": "certification is a required argument."}, indent=2)
        warehouses = list(data.get('warehouses', {}).values())
        matching_warehouses = [wh for wh in warehouses if certification in wh.get('certifications', [])]
        return json.dumps(matching_warehouses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_warehouses_by_capability", "description": "Finds all warehouses that hold a specific certification.", "parameters": {"type": "object", "properties": {"certification": {"type": "string", "description": "The certification to filter warehouses by (e.g., 'FDA Registered')."}}, "required": ["certification"]}}}
