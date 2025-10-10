# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWarehouseDetails(Tool):
    """Retrieves all details for a specific warehouse by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_name) -> str:
        if not warehouse_name:
            return json.dumps({"error": "warehouse_name is required."}, indent=2)
        warehouse = next((w for w in data.get('warehouses', []) if w.get('warehouse_name') == warehouse_name), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse '{warehouse_name}' not found."}, indent=2)
        return json.dumps(warehouse, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_warehouse_details", "description": "Retrieves all details for a specific warehouse by its name.", "parameters": {"type": "object", "properties": {"warehouse_name": {"type": "string"}}, "required": ["warehouse_name"]}}}
