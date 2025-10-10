# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdjustInventory(Tool):
    """Tool to adjust the quantity of a product in a warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, sku: str, quantity_change: int, reason: str) -> str:
        """Execute the tool with given parameters."""
        inventory = list(data.get("inventory", {}).values())
        for item in inventory:
            if item.get("warehouse_id") == warehouse_id and item.get("sku") == sku:
                original_qty = item["quantity_on_hand"]
                item["quantity_on_hand"] += quantity_change
                item["quantity_available"] += quantity_change

                if item["quantity_on_hand"] < 0:
                    item["quantity_on_hand"] = 0
                if item["quantity_available"] < 0:
                    item["quantity_available"] = 0

                return json.dumps({
                    "inventory_id": item["inventory_id"],
                    "sku": sku,
                    "warehouse_id": warehouse_id,
                    "original_quantity": original_qty,
                    "new_quantity": item["quantity_on_hand"],
                    "reason": reason
                }, indent=2)
        return json.dumps({"error": f"Inventory item not found for SKU {sku} in warehouse {warehouse_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "adjust_inventory",
                "description": "Manually adjusts the inventory quantity for a product in a specific warehouse (e.g., for cycle counts, damage).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "The ID of the warehouse."},
                        "sku": {"type": "string", "description": "The SKU of the product to adjust."},
                        "quantity_change": {"type": "integer", "description": "The amount to change the quantity by (can be positive or negative)."},
                        "reason": {"type": "string", "description": "The reason for the adjustment (e.g., 'Damaged Goods', 'Cycle Count Adjustment')."}
                    },
                    "required": ["warehouse_id", "sku", "quantity_change", "reason"],
                },
            },
        }
