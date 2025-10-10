# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryInWarehouse(Tool):
    """Tool to get inventory for a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, sku: Optional[str] = None) -> str:
        """Execute the tool with given parameters."""
        inventory = list(data.get("inventory", {}).values())
        results = []
        for item in inventory:
            if item.get("warehouse_id") == warehouse_id:
                if not sku or item.get("sku") == sku:
                    results.append(item)
        if not results:
            return json.dumps({"error": f"No inventory found for warehouse {warehouse_id}"}, indent=2)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_in_warehouse",
                "description": "Retrieves all inventory items or a specific SKU's inventory from a single warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to check.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "Optional: The SKU of a specific product to check.",
                        },
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
