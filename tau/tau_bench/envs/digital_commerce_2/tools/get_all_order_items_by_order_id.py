# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idstr(v):
    return str(v) if isinstance(v, int) else v

class GetAllOrderItemsByOrderId(Tool):
    """Return all order_items rows for a given order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            return json.dumps({"error": "Missing required field: order_id"}, indent=2)
        order_items: List[Dict[str, Any]] = list(data.get("order_items", {}).values())
        items = [item for item in order_items if item.get("order_id") == order_id]
        return json.dumps(items, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_order_items_by_order_id",
                "description": "Return all order items for the specified order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID whose items should be returned.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }