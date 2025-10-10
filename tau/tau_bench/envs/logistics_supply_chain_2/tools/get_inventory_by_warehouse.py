# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryByWarehouse(Tool):
    """Tool to retrieve inventory items stored in a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        list_of_inventories = kwargs.get("list_of_ids", None)
        inventories = list(data.get("inventory", {}).values())
        filtered = [item['inventory_id'] for item in inventories if item["warehouse_id"] == warehouse_id]
        if list_of_inventories:
            filtered = [f for f in filtered if f in list_of_inventories]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_warehouse",
                "description": "Retrieve inventory items from a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-10')."
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        }
                    },
                    "required": ["warehouse_id"]
                }
            }
        }
