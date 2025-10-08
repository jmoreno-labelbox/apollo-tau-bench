from tau_bench.envs.tool import Tool
import json
from typing import Any

class LinkTrackingToOrder(Tool):
    """Create a fulfillment record that associates tracking_id and item_ids with an order (idempotent by exact tuple)."""

    @staticmethod
    def invoke(data, order_id: str = None, tracking_id: str = None, item_ids: list = None) -> str:
        if item_ids is None:
            item_ids = []
        if not order_id or not tracking_id or not item_ids:
            payload = {"error": "order_id, tracking_id, item_ids are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        fl = _ensure_list(o, "fulfillments")
        payload = {"tracking_id": [tracking_id], "item_ids": item_ids}
        if payload not in fl:
            fl.append(payload)
        payload = {
                "success": True,
                "order_id": order_id,
                "tracking_id": tracking_id,
                "item_ids": item_ids,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "linkTrackingToOrder",
                "description": "Append a fulfillment mapping (tracking_id, item_ids) to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["order_id", "tracking_id", "item_ids"],
                },
            },
        }
