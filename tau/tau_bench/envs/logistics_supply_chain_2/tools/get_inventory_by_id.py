# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryById(Tool):
    """Tool to retrieve inventory item by inventory ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get("inventory_id")
        inventories = list(data.get("inventory", {}).values())
        for item in inventories:
            if item["inventory_id"] == inventory_id:
                return json.dumps(item, indent=2)
        return json.dumps({"error": f"Inventory with ID {inventory_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_id",
                "description": "Retrieve inventory item details using inventory ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Inventory ID (e.g., 'INV-0008')."
                        }
                    },
                    "required": ["inventory_id"]
                }
            }
        }
