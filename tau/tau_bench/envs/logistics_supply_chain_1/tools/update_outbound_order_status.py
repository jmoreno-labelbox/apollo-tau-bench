from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateOutboundOrderStatus(Tool):
    """Modifies the status of a current outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_status: str = None) -> str:
        if not all([order_id, new_status]):
            payload = {"error": "order_id and new_status are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        order = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out

        if new_status == "Cancelled":
            for item in order.get("line_items", []):
                for inv_record in data.get("inventory", {}).values():
                    if inv_record.get("sku") == item.get("sku") and inv_record.get(
                        "warehouse_id"
                    ) == order.get("warehouse_id"):
                        inv_record["quantity_available"] += item.get("quantity", 0)
                        inv_record["quantity_allocated"] -= item.get("quantity", 0)
                        break

        order["status"] = new_status
        return_related_statuses = [
            "Returned",
            "Partially Returned",
            "Cancelled - Damaged Stock",  #Or other statuses that involve return/cancellation affecting returns
            "Processing Return",
            "Incorrect Item Returned",
            "Cancelled - Force Majeure",
            "On Hold - Fraud Investigation",  #Depending on the fraud/return policy
            "Cancelled - Expired Stock",
            "Cancelled",  #If a generic cancellation also involves a return
        ]
        if new_status in return_related_statuses:
            order["return_status"] = new_status
        else:
            order["return_status"] = "None"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrderStatus",
                "description": "Updates the status of an existing outbound order (e.g., to 'Partially Returned').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the order.",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
