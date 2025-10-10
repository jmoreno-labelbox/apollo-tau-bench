# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWarehouseByID(Tool):
    """Tool to retrieve a warehouse’s full details using its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                return json.dumps(warehouse, indent=2)
        return json.dumps({"error": f"Warehouse ID '{warehouse_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_by_id",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-14')"
                        }
                    },
                    "required": ["warehouse_id"]
                }
            }
        }
