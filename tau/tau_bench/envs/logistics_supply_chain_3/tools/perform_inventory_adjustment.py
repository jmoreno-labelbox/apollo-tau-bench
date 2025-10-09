from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class PerformInventoryAdjustment(Tool):
    """
    Conducts a complete inventory adjustment for a product at a designated warehouse.
    It revises the quantity on hand, available quantity, last counted date, and appends an audit note.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        warehouse_id: str,
        new_physical_count: int,
        current_date: str,
        reason_note: str = ""
,
    current_allocated_quantity: Any = None,
    ) -> str:
        inventory_items = data.get("inventory", [])

        if not all(
            [
                sku,
                warehouse_id,
                new_physical_count is not None,
                current_date,
            ]
        ):
            payload = {"error": "One or more required arguments are missing."}
            out = json.dumps(payload)
            return out

        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_on_hand = item.get("quantity_on_hand", 0)
                discrepancy = new_physical_count - original_on_hand

                item["quantity_on_hand"] = new_physical_count
                item["quantity_available"] = max(
                    0, new_physical_count - item.get("quantity_allocated", 0)
                )
                item["last_counted_date"] = current_date

                if reason_note:
                    adjustment_log = f"Adjustment on {current_date}: Count changed from {original_on_hand} to {new_physical_count} (Discrepancy: {discrepancy}). Reason: {reason_note}."
                    if item.get("notes"):
                        item["notes"] = f"{item['notes']} | {adjustment_log}"
                    else:
                        item["notes"] = adjustment_log
                payload = {
                    "status": "success",
                    "inventory_id": item.get("inventory_id"),
                    "new_on_hand_quantity": item["quantity_on_hand"],
                    "new_available_quantity": item["quantity_available"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found to adjust"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PerformInventoryAdjustment",
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
