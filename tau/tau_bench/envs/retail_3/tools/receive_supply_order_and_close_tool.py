# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReceiveSupplyOrderAndCloseTool(Tool):
    """
    Mark a supply order as 'received' and close it with a terminal timestamp.

    Behavior:
    - Validates the supply order exists.
    - Sets status to 'received' and stamps 'received_at' with UTC ISO (if not present).
    - Appends an event {type: "received", message: <optional note>, timestamp: UTC ISO} to events.
    - Updates stock of received items.
    - Sets status to 'closed' and stamps 'closed_at' with UTC ISO.

    Input (kwargs):
        supply_order_id (str, required)
        note (str, optional)

    Output:
        JSON string with {"supply_order_id","status","received_at","closed_at","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_id = kwargs.get("supply_order_id")
        note = kwargs.get("note")

        if not so_id:
            return json.dumps({"error": "supply_order_id is required"}, indent=2)

        supply_orders = data.get("supply_orders", [])
        products = list(data.get("products", {}).values())

        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        # 1. Update status to 'received' and add received_at timestamp
        so["status"] = "received"
        if not so.get("received_at"):
            so["received_at"] = _now_iso()

        # Append 'received' event
        event = {
            "type": "received",
            "message": (note or "supply order received"),
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)

        # 2. Update product stock for each item in the supply order
        for so_item in so.get("items", []):
            product_id = so_item.get("product_id")
            quantity = so_item.get("quantity", 0)

            product = next((p for p in products if p.get("product_id") == product_id), None)
            if product:
                product["quantity"] = product.get("quantity", 0) + quantity
                product["reserved_quantity"] = product.get("reserved_quantity", 0) + quantity

        # 3. Set final status to 'closed' and add closed_at timestamp
        so["status"] = "closed"
        so["closed_at"] = _now_iso()

        return json.dumps(
            {
                "supply_order_id": so_id,
                "status": so["status"],
                "received_at": so["received_at"],
                "closed_at": so["closed_at"],
                "events_len": len(so.get("events", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "receive_supply_order_and_close",
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
