from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddOrderFulfillment(Tool):
    """Insert a fulfillment entry containing tracking IDs for designated item IDs."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        tracking_ids: list[str],
        item_ids: list[str]
    ) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                    "status": "success",
                    "order_id": order_id,
                    "fulfillments": order["fulfillments"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
        pass
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                        "status": "success",
                        "order_id": order_id,
                        "fulfillments": order["fulfillments"],
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOrderFulfillment",
                "description": "Add fulfillment with tracking IDs and covered item IDs to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["order_id", "tracking_ids", "item_ids"],
                },
            },
        }
