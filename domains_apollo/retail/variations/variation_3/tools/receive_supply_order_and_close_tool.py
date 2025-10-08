from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class ReceiveSupplyOrderAndCloseTool(Tool):
    """
    Designate a supply order as 'received' and finalize it with a terminal timestamp.

    Behavior:
    - Confirms the supply order exists.
    - Changes status to 'received' and records 'received_at' with UTC ISO (if not already present).
    - Adds an event {type: "received", message: <optional note>, timestamp: UTC ISO} to events.
    - Updates inventory of received items.
    - Changes status to 'closed' and records 'closed_at' with UTC ISO.

    Input (kwargs):
        supply_order_id (str, required)
        note (str, optional)

    Output:
        JSON string with {"supply_order_id","status","received_at","closed_at","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, note: str = None) -> str:
        so_id = supply_order_id

        if not so_id:
            payload = {"error": "supply_order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        supply_orders = data.get("supply_orders", [])
        products = data.get("products", [])

        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #1. Change status to 'received' and include received_at timestamp
        so["status"] = "received"
        if not so.get("received_at"):
            so["received_at"] = _now_iso()

        #Add 'received' event
        event = {
            "type": "received",
            "message": (note or "supply order received"),
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)

        #2. Adjust product inventory for every item in the supply order
        for so_item in so.get("items", []):
            product_id = so_item.get("product_id")
            quantity = so_item.get("quantity", 0)

            product = next(
                (p for p in products if p.get("product_id") == product_id), None
            )
            if product:
                product["quantity"] = product.get("quantity", 0) + quantity
                product["reserved_quantity"] = (
                    product.get("reserved_quantity", 0) + quantity
                )

        #3. Change final status to 'closed' and include closed_at timestamp
        so["status"] = "closed"
        so["closed_at"] = _now_iso()
        payload = {
                "supply_order_id": so_id,
                "status": so["status"],
                "received_at": so["received_at"],
                "closed_at": so["closed_at"],
                "events_len": len(so.get("events", [])),
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
                "name": "ReceiveSupplyOrderAndClose",
                "description": "Set a supply order to 'received' and 'closed', update product stock, and append events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["supply_order_id"],
                },
            },
        }
