# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: int) -> str:
        order = _require(data, "orders", "order_id", int(order_id))
        items = [i for i in data.get("order_items", []) if int(i.get("order_id")) == int(order_id)]
        return json.dumps({"order": order, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get order header and items.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "integer"}},
                    "required": ["order_id"],
                },
            },
        }
