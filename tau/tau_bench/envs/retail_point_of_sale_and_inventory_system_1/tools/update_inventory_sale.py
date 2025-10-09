from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateInventorySale(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, quantity_sold: int = None, last_stock_count_date: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["quantity"] = item.get("quantity", 0) - quantity_sold
                item["reserved_quantity"] = max(
                    0, item.get("reserved_quantity", 0) - quantity_sold
                )
                item["last_stock_count"] = last_stock_count_date
                updated_item = item
                break
        payload = {"updated_inventory_item": updated_item}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventorySale",
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
                    "required": [
                        "inventory_id",
                        "quantity_sold",
                        "last_stock_count_date",
                    ],
                },
            },
        }
