from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, new_status: str = None) -> str:
        if not supply_order_id or not new_status:
            payload = {"error": "supply_order_id and new_status are required"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        order = next(
            (o for o in supply_orders.values() if o["supply_order_id"] == supply_order_id), None
        )

        if not order:
            payload = {"error": "Supply order not found"}
            out = json.dumps(payload)
            return out

        old_status = order["status"]
        order["status"] = new_status

        # Update inventory if the order is finalized
        if new_status == "completed":
            suppliers = data["suppliers"]
            supplier = next(
                (s for s in suppliers.values() if s["supplier_id"] == order["supplier_id"]), None
            )

            if supplier and order["item_id"] in supplier["item_stock"]:
                current_stock = supplier["item_stock"][order["item_id"]]
                if isinstance(current_stock, int):
                    supplier["item_stock"][order["item_id"]] = (
                        current_stock + order["quantity"]
                    )
        payload = {
            "success": True,
            "supply_order_id": supply_order_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": get_current_timestamp(),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSupplyOrderStatus",
                "description": "Update the status of a supply order. Automatically updates inventory when marked as completed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the supply order",
                        },
                    },
                    "required": ["supply_order_id", "new_status"],
                },
            },
        }
