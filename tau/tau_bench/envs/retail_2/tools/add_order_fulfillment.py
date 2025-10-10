# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddOrderFulfillment(Tool):
    """Add a fulfillment record with tracking IDs for specific item IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, tracking_ids: List[str], item_ids: List[str]) -> str:
        orders = list(data.get("orders", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({
                    "tracking_id": tracking_ids,
                    "item_ids": item_ids
                })
                order["fulfillments"] = fulfillments
                return json.dumps({"status": "success", "order_id": order_id, "fulfillments": order["fulfillments"]})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_order_fulfillment",
                "description": "Add fulfillment with tracking IDs and covered item IDs to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["order_id", "tracking_ids", "item_ids"]
                }
            }
        }
