from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, item_id: str = None, new_stock: int = None, adjustment: int = None) -> str:
        if not supplier_id or not item_id:
            payload = {"error": "supplier_id and item_id are required"}
            out = json.dumps(payload)
            return out

        if new_stock is None and adjustment is None:
            payload = {"error": "Either new_stock or adjustment is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]
        supplier = next((s for s in suppliers.values() if s["supplier_id"] == supplier_id), None)

        if not supplier:
            payload = {"error": "Supplier not found"}
            out = json.dumps(payload)
            return out

        current_stock = supplier["item_stock"].get(item_id)

        if isinstance(current_stock, str) and current_stock == "discontinued":
            payload = {"error": f"Cannot update stock for item with status: {current_stock}"}
            out = json.dumps(payload)
            return out

        if new_stock is not None:
            supplier["item_stock"][item_id] = new_stock
            updated_stock = new_stock
        else:
            if not isinstance(current_stock, int):
                # Manage situations where stock is non-numeric, such as None or absent
                current_stock = 0
            updated_stock = max(0, current_stock + adjustment)
            supplier["item_stock"][item_id] = updated_stock

        payload = {
            "success": True,
            "supplier_id": supplier_id,
            "item_id": item_id,
            "previous_stock": current_stock,
            "updated_stock": updated_stock,
            "updated_at": get_current_timestamp(),
        }
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateInventory",
                "description": "Update inventory stock levels for a specific item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID managing the inventory",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Item ID to update stock for",
                        },
                        "new_stock": {
                            "type": "integer",
                            "description": "Set to this exact stock level",
                        },
                        "adjustment": {
                            "type": "integer",
                            "description": "Adjust current stock by this amount (positive or negative)",
                        },
                    },
                    "required": ["supplier_id", "item_id"],
                },
            },
        }
