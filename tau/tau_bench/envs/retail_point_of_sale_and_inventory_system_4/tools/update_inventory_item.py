# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryItem(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, store_id: str, quantity_change: int, current_time: str) -> str:
        db = list(data.get("inventory", {}).values())
        filtered_db = _filter_db(db, {"sku":sku, "store_id":store_id})
        if len(filtered_db) == 1:
            row = filtered_db[0]
            row["quantity"] = row.get("quantity", 0) + quantity_change
            row["updated_at"] = current_time
            return json.dumps({"result": row})
        else:
            return json.dumps({"error": f"Inventory item {sku} in store {store_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_item",
                "description": "Update the quantity and updated_at time of an inventory item by inventory_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The inventory item's id to update."},
                        "quantity_change": {"type": "int", "description": "The amount to change the quantity by (can be negative)."},
                        "current_time": {"type": "string", "description": "Timestamp for updated_at."}
                    },
                    "required": ["inventory_id", "quantity_change", "current_time"]
                }
            }
        }
