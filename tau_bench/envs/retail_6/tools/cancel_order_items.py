from tau_bench.envs.tool import Tool
import json
from typing import Any

class CancelOrderItems(Tool):
    """Designate certain items in an order as cancelled with a reason_code (adds 'cancelled': True)."""

    @staticmethod
    def invoke(data, order_id: str = None, item_ids: list = None, reason_code: str = None) -> str:
        if item_ids is None:
            item_ids = []
        if not order_id or not item_ids or not reason_code:
            payload = {"error": "order_id, item_ids, reason_code are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        updated = []
        for item in o.get("items", []):
            if item.get("item_id") in item_ids:
                item["cancelled"] = True
                item["cancellation_reason"] = reason_code
                updated.append(item["item_id"])
        payload = {
                "success": True,
                "order_id": order_id,
                "cancelled_item_ids": updated,
                "reason_code": reason_code,
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
                "name": "cancelOrderItems",
                "description": "Mark given item_ids in an order as cancelled with a reason_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "reason_code": {"type": "string"},
                    },
                    "required": ["order_id", "item_ids", "reason_code"],
                },
            },
        }
