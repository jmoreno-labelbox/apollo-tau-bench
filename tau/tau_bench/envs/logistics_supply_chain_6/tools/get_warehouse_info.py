# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWarehouseInfo(Tool):
    """Tool to get information about a warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        """Execute the tool with given parameters."""
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                return json.dumps(warehouse, indent=2)
        return json.dumps({"error": f"Warehouse with ID {warehouse_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_info",
                "description": "Retrieves detailed information about a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "The ID of the warehouse."}
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
