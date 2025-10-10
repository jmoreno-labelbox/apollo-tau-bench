# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindWarehouseByName(Tool):
    """Finds a warehouse's ID by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_name) -> str:
        warehouses = list(data.get("warehouses", {}).values())
        for warehouse in warehouses:
            if warehouse.get("warehouse_name") == warehouse_name:
                return json.dumps({"warehouse_id": warehouse.get("warehouse_id")})
        return json.dumps({"error": "Warehouse not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_warehouse_by_name",
                "description": "Finds a warehouse's ID by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_name": {
                            "type": "string",
                            "description": "The full name of the warehouse.",
                        }
                    },
                    "required": ["warehouse_name"],
                },
            },
        }
