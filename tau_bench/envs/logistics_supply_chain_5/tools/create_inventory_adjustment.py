from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str = None, warehouse_id: str = None, adjustment_quantity: int = None, reason: str = None,
    variance_percentage: Any = None,
    unit_cost: Any = None,
    ) -> str:
        inventory = data.get("inventory", [])

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({"error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"})

        adjustment_id = f"ADJ-{warehouse_id}"

        # Revise inventory counts
        old_quantity = inventory_item.get("quantity_on_hand", 0)
        new_quantity = old_quantity + adjustment_quantity
        inventory_item["quantity_on_hand"] = new_quantity
        inventory_item["quantity_available"] = inventory_item.get("quantity_available", 0) + adjustment_quantity
        inventory_item["last_counted_date"] = get_current_year_month_day()

        # Generate a record for adjustments
        adjustment_record = {
            "adjustment_id": adjustment_id,
            "sku": sku,
            "warehouse_id": warehouse_id,
            "adjustment_quantity": adjustment_quantity,
            "old_quantity": old_quantity,
            "new_quantity": new_quantity,
            "reason": reason,
            "adjustment_date": get_current_timestamp(),
            "adjusted_by": "SYSTEM"
        }

        if "inventory_adjustments" not in data:
            data["inventory_adjustments"] = []
        data["inventory_adjustments"].append(adjustment_record)

        # Compute the overall adjustment value
        product_master = data.get("inventory", [])
        product = next((p for p in product_master if p.get("sku") == sku), None)
        unit_price = product.get("unit_cost", 0) if product else 0

        total_adjustment_value = abs(adjustment_quantity) * unit_price

        return json.dumps({
            "adjustment_id": adjustment_id,
            "old_quantity": old_quantity,
            "new_quantity": new_quantity,
            "adjustment_amount": adjustment_quantity,
            "total_adjustment_value": total_adjustment_value
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryAdjustment",
                "description": "Create inventory adjustment record and update quantities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "adjustment_quantity": {"type": "integer", "description": "Quantity adjustment (positive or negative)"},
                        "reason": {"type": "string", "description": "Reason for adjustment"}
                    },
                    "required": ["sku", "warehouse_id", "adjustment_quantity", "reason"]
                }
            }
        }
