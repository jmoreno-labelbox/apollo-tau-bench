from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetOrderShippingAddress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, address: Any) -> str:
        order_id = _as_id(order_id)
        if not order_id or address is None:
            return _err("order_id and address are required.")
        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["shipping_address_used"] = address
        payload = {"order_id": order_id, "shipping_address_used": address}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetOrderShippingAddress",
                "description": "Attach a shipping address to an order (explicit object).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["order_id", "address"],
                },
            },
        }
