from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateItemOption(Tool):
    """Modify a specific option key for a particular item in an order."""

    @staticmethod
    def invoke(data, order_id=None, item_id=None, option_key=None, option_value=None) -> str:
        if not order_id or not item_id or option_key is None or option_value is None:
            payload = {"error": "order_id, item_id, option_key, option_value are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        it = next((i for i in o.get("items", []) if i.get("item_id") == item_id), None)
        if not it:
            payload = {"error": f"item_id {item_id} not in order {order_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        opts = it.setdefault("options", {})
        opts[option_key] = option_value
        payload = {
                "success": True,
                "order_id": order_id,
                "item_id": item_id,
                "option_key": option_key,
                "option_value": option_value,
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
                "name": "updateItemOption",
                "description": "Update a single option on an order item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "option_key": {"type": "string"},
                        "option_value": {},
                    },
                    "required": ["order_id", "item_id", "option_key", "option_value"],
                },
            },
        }
