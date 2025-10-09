from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class DuplicateOrderTool(Tool):
    """
    Create a duplicate of an existing order as a new one for the same user.

    Behavior:
    - Confirms the source order exists.
    - Copies user_id, address, items; resets fulfillments to [] and payment_history to [].
    - Changes status to "pending" and generates a new order_id and timestamp.
    - Adds the new order to orders.json.

    Input (kwargs):
        source_order_id (str, required)

    Output:
        JSON string with {"source_order_id","new_order_id","items_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], source_order_id: str = None) -> str:
        src_id = source_order_id
        if not src_id:
            payload = {"error": "source_order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        src = next((o for o in orders if o.get("order_id") == src_id), None)
        if not src:
            payload = {"error": f"source_order_id '{src_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        new_order = {
            "order_id": _gen_order_id(),
            "user_id": src.get("user_id"),
            "address": src.get("address"),
            "items": list(src.get("items", [])),
            "fulfillments": [],
            "status": "pending",
            "payment_history": [],
            "timestamp": _now_iso(),
        }
        orders.append(new_order)
        payload = {
                "source_order_id": src_id,
                "new_order_id": new_order["order_id"],
                "items_count": len(new_order.get("items", [])),
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
                "name": "duplicateOrder",
                "description": "Duplicate an existing order (same user/address/items) with a fresh id, pending status, and no payments/fulfillments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_order_id": {"type": "string"},
                    },
                    "required": ["source_order_id"],
                },
            },
        }
