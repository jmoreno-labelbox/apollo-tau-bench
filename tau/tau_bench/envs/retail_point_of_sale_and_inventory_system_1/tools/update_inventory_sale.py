# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventorySale(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        quantity_sold = kwargs.get('quantity_sold')
        last_stock_count_date = kwargs.get('last_stock_count_date')
        inventory_items = list(data.get("inventory", {}).values())
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["quantity"] = item.get("quantity", 0) - quantity_sold
                item["reserved_quantity"] = max(0, item.get("reserved_quantity", 0) - quantity_sold)
                item["last_stock_count"] = last_stock_count_date
                updated_item = item
                break
        return json.dumps({"updated_inventory_item": updated_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_sale",
                "description": "Updates inventory quantities and last stock count date after a sale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "quantity_sold": {
                            "type": "integer",
                            "description": "The number of units sold.",
                        },
                        "last_stock_count_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The date of the last stock count (YYYY-MM-DD).",
                        },
                    },
                    "required": ["inventory_id", "quantity_sold", "last_stock_count_date"],
                },
            },
        }
