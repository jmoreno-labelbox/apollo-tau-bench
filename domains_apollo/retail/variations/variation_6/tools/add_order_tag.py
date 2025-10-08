from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddOrderTag(Tool):
    """Include a tag string to an order (idempotent)."""

    @staticmethod
    def invoke(data, order_id=None, tag=None) -> str:
        if not order_id or tag is None:
            payload = {"error": "order_id and tag are required"}
            out = json.dumps(payload, indent=2)
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        tags = o.setdefault("order_tags", [])
        if tag not in tags:
            tags.append(tag)
        payload = {"success": True, "order_id": order_id, "tag": tag}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "addOrderTag",
                "description": "Append a tag to order.order_tags if not present.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tag": {"type": "string"},
                    },
                    "required": ["order_id", "tag"],
                },
            },
        }
