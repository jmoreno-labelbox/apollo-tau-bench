# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, warehouse_id: str) -> str:
        inventory = list(data.get("inventory", {}).values())

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({
                "error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"
            })

        return json.dumps(inventory_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_details",
                "description": "Get detailed inventory information for a specific SKU and warehouse",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["sku", "warehouse_id"]
                }
            }
        }
