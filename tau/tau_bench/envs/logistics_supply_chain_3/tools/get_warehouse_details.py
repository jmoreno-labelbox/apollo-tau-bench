# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWarehouseDetails(Tool):
    """Retrieves the full details for a warehouse by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id) -> str:
        warehouses = list(data.get("warehouses", {}).values())
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                return json.dumps(warehouse)
        return json.dumps({"error": "Warehouse not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_details",
                "description": "Retrieves the full record for a warehouse by its exact ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse (e.g., 'WH-01').",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
