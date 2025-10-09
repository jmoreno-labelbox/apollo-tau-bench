from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AdjustInventory(Tool):
    """Utility for modifying the amount of a product within a warehouse."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        warehouse_id: str,
        sku: str,
        quantity_change: int,
        reason: str
    ) -> str:
        """Run the tool using the specified parameters."""
        inventory = data.get("inventory", {}).values()
        for item in inventory.values():
            if item.get("warehouse_id") == warehouse_id and item.get("sku") == sku:
                original_qty = item["quantity_on_hand"]
                item["quantity_on_hand"] += quantity_change
                item["quantity_available"] += quantity_change

                if item["quantity_on_hand"] < 0:
                    item["quantity_on_hand"] = 0
                if item["quantity_available"] < 0:
                    item["quantity_available"] = 0
                payload = {
                    "inventory_id": item["inventory_id"],
                    "sku": sku,
                    "warehouse_id": warehouse_id,
                    "original_quantity": original_qty,
                    "new_quantity": item["quantity_on_hand"],
                    "reason": reason,
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {
            "error": f"Inventory item not found for SKU {sku} in warehouse {warehouse_id}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        """Run the tool using the specified parameters."""
        pass
        inventory = data.get("inventory", {}).values()
        for item in inventory.values():
            if item.get("warehouse_id") == warehouse_id and item.get("sku") == sku:
                original_qty = item["quantity_on_hand"]
                item["quantity_on_hand"] += quantity_change
                item["quantity_available"] += quantity_change

                if item["quantity_on_hand"] < 0:
                    item["quantity_on_hand"] = 0
                if item["quantity_available"] < 0:
                    item["quantity_available"] = 0
                payload = {
                        "inventory_id": item["inventory_id"],
                        "sku": sku,
                        "warehouse_id": warehouse_id,
                        "original_quantity": original_qty,
                        "new_quantity": item["quantity_on_hand"],
                        "reason": reason,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {
                "error": f"Inventory item not found for SKU {sku} in warehouse {warehouse_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AdjustInventory",
                "description": "Manually adjusts the inventory quantity for a product in a specific warehouse (e.g., for cycle counts, damage).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to adjust.",
                        },
                        "quantity_change": {
                            "type": "integer",
                            "description": "The amount to change the quantity by (can be positive or negative).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the adjustment (e.g., 'Damaged Goods', 'Cycle Count Adjustment').",
                        },
                    },
                    "required": ["warehouse_id", "sku", "quantity_change", "reason"],
                },
            },
        }
