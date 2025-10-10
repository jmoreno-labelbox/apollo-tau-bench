# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplyOrderTerms(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str, new_unit_cost: float = None, payment_terms: str = None, delivery_deadline: str = None) -> str:
        """
        Update supply order terms and conditions

        Writes to: supply_orders.json (updates existing supply order terms)
        Data Sources: supply_orders.json (supply_order_id, unit_cost, quantity)
        """
        if new_unit_cost is not None and new_unit_cost < 0:
            return json.dumps({"error": "Unit cost cannot be negative", "status": "failed"})

        # Find the supply order to update
        supply_orders = data.get("supply_orders", [])
        supply_order_to_update = None
        order_index = None

        for i, order in enumerate(supply_orders):
            if order.get("supply_order_id") == supply_order_id:
                supply_order_to_update = order
                order_index = i
                break

        if not supply_order_to_update:
            return json.dumps({"error": f"Supply order {supply_order_id} not found", "status": "failed"})

        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        current_status = supply_order_to_update.get("status")
        if current_status == "fulfilled":
            return json.dumps({
                "error": f"Cannot modify terms for fulfilled supply order {supply_order_id}",
                "status": "failed"
            })

        # WRITE OPERATION: Update supply order terms
        updates_applied = []
        old_unit_cost = supply_order_to_update.get("unit_cost", 0)
        quantity = supply_order_to_update.get("quantity", 0)

        if new_unit_cost is not None:
            supply_order_to_update["unit_cost"] = new_unit_cost
            supply_order_to_update["total_cost"] = round(new_unit_cost * quantity, 2)
            updates_applied.append("unit_cost")
            updates_applied.append("total_cost")

        if payment_terms:
            supply_order_to_update["payment_terms"] = payment_terms
            updates_applied.append("payment_terms")

        if delivery_deadline:
            supply_order_to_update["delivery_deadline"] = delivery_deadline
            updates_applied.append("delivery_deadline")

        supply_order_to_update["terms_updated"] = datetime.now().isoformat()

        # Update the supply order in the data structure
        data["supply_orders"][order_index] = supply_order_to_update

        result = {
            "status": "success",
            "supply_order_id": supply_order_id,
            "supplier_id": supply_order_to_update.get("supplier_id"),
            "item_id": supply_order_to_update.get("item_id"),
            "product_id": supply_order_to_update.get("product_id"),
            "updates_applied": updates_applied,
            "cost_changes": {
                "previous_unit_cost": old_unit_cost,
                "new_unit_cost": supply_order_to_update.get("unit_cost"),
                "new_total_cost": supply_order_to_update.get("total_cost")
            } if new_unit_cost is not None else None,
            "terms_updated": supply_order_to_update["terms_updated"]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_supply_order_terms",
                "description": "Update supply order terms and conditions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string", "description": "Supply order identifier (e.g., '#SO9359')"},
                        "new_unit_cost": {"type": "number", "description": "New unit cost"},
                        "payment_terms": {"type": "string", "description": "Payment terms (e.g., 'NET30', 'COD')"},
                        "delivery_deadline": {"type": "string", "description": "Delivery deadline (ISO format)"}
                    },
                    "required": ["supply_order_id"]
                }
            }
        }
