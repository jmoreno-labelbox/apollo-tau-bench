# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PerformInventoryAdjustment(Tool):
    """
    Performs a full inventory adjustment for a product at a specific warehouse.
    It updates quantity on hand, available quantity, last counted date, and adds an audit note.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], current_date, new_physical_count, sku, warehouse_id, reason_note = "") -> str:
        inventory_items = list(data.get("inventory", {}).values())

        if not all(
            [
                sku,
                warehouse_id,
                new_physical_count is not None,
                current_date,
            ]
        ):
            return json.dumps({"error": "One or more required arguments are missing."})

        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_on_hand = item.get("quantity_on_hand", 0)
                discrepancy = new_physical_count - original_on_hand

                # Revise fundamental values.
                item["quantity_on_hand"] = new_physical_count
                item["quantity_available"] = max(
                    0, new_physical_count - item.get("quantity_allocated", 0)
                )
                item["last_counted_date"] = current_date

                # Add a comprehensive record for audit purposes.
                if reason_note:
                    adjustment_log = f"Adjustment on {current_date}: Count changed from {original_on_hand} to {new_physical_count} (Discrepancy: {discrepancy}). Reason: {reason_note}."
                    if item.get("notes"):
                        item["notes"] = f"{item['notes']} | {adjustment_log}"
                    else:
                        item["notes"] = adjustment_log

                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": item.get("inventory_id"),
                        "new_on_hand_quantity": item["quantity_on_hand"],
                        "new_available_quantity": item["quantity_available"],
                    }
                )
        return json.dumps({"error": "Inventory record not found to adjust"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "perform_inventory_adjustment",
                "description": "Updates inventory quantities based on a physical count, adjusts available stock, updates the count date, and logs the reason.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to adjust.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse where the adjustment is occurring.",
                        },
                        "new_physical_count": {
                            "type": "integer",
                            "description": "The new, correct physical quantity on hand.",
                        },
                        "current_date": {
                            "type": "string",
                            "description": "The date of the adjustment in YYYY-MM-DD format.",
                        },
                        "reason_note": {
                            "type": "string",
                            "description": "Optional. A reason for the adjustment, which will be logged in the inventory record.",
                        },
                    },
                    "required": [
                        "sku",
                        "warehouse_id",
                        "new_physical_count",
                        "current_date",
                    ],
                },
            },
        }
