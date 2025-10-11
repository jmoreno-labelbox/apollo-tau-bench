# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryBySkuWarehouse(Tool):
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
                "name": "get_inventory_by_sku_warehouse",
                "description": "Retrieve inventory details for specific SKU in a warehouse",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU identifier"
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse identifier"
                        }
                    },
                    "required": ["sku", "warehouse_id"]
                }
            }
        }
