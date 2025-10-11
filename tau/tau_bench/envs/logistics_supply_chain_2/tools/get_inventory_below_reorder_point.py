# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryBelowReorderPoint(Tool):
    """Tool to retrieve inventory items that are below reorder point."""

    @staticmethod
    def invoke(data: Dict[str, Any], list_of_ids = None) -> str:
        inventories = list(data.get("inventory", {}).values())
        list_of_inventories = list_of_ids
        low_stock = [item['inventory_id'] for item in inventories if item["quantity_available"] < item["reorder_point"]]
        if list_of_inventories:
            low_stock = [ls for ls in low_stock if ls in list_of_inventories]
        return json.dumps(low_stock, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_below_reorder_point",
                "description": "Retrieve inventory items where available quantity is below reorder point.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        }
                    }
                }
            }
        }
