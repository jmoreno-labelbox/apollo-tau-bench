from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateInventoryItem(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        store_id: str,
        quantity_change: int,
        current_time: str
    ) -> str:
        db = data.get("inventory", [])
        filtered_db = _filter_db(db, {"sku": sku, "store_id": store_id})
        if len(filtered_db) == 1:
            row = filtered_db[0]
            row["quantity"] = row.get("quantity", 0) + quantity_change
            row["updated_at"] = current_time
            payload = {"result": row}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Inventory item {sku} in store {store_id} not found"}
            out = json.dumps(payload)
            return out
        pass
        db = data.get("inventory", [])
        filtered_db = _filter_db(db, {"sku": sku, "store_id": store_id})
        if len(filtered_db) == 1:
            row = filtered_db[0]
            row["quantity"] = row.get("quantity", 0) + quantity_change
            row["updated_at"] = current_time
            payload = {"result": row}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Inventory item {sku} in store {store_id} not found"}
            out = json.dumps(
                payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryItem",
                "description": "Update the quantity and updated_at time of an inventory item by inventory_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The inventory item's id to update.",
                        },
                        "quantity_change": {
                            "type": \"integer\",
                            "description": "The amount to change the quantity by (can be negative).",
                        },
                        "current_time": {
                            "type": "string",
                            "description": "Timestamp for updated_at.",
                        },
                    },
                    "required": ["inventory_id", "quantity_change", "current_time"],
                },
            },
        }
