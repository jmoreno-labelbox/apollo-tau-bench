from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignCourierToOrder(Tool):
    """
    Insert a courier tracking ID into the fulfillments of an order.
    Predictable: necessitates specific tracking_ids and item_ids.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        courier_id: str,
        tracking_ids: list[str],
        item_ids: list[str]
    ) -> str:
        # Check if the courier is present and possesses all tracking_ids
        couriers = data.get("couriers", [])
        courier = None
        for c in couriers:
            if c.get("courier_id") == courier_id:
                courier = c
                break
        if courier is None:
            payload = {"error": "Courier not found", "courier_id": courier_id}
            out = json.dumps(payload)
            return out

        for t in tracking_ids:
            if t not in courier.get("tracking_ids", []):
                payload = {
                    "error": "Tracking ID not owned by courier",
                    "courier_id": courier_id,
                    "tracking_id": t,
                }
                out = json.dumps(payload)
                return out

        # Revise order fulfillments
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                    "status": "success",
                    "order_id": order_id,
                    "courier_id": courier_id,
                    "fulfillments": fulfillments,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
        pass
        #Check if the courier is present and possesses all tracking_ids
        couriers = data.get("couriers", [])
        courier = None
        for c in couriers:
            if c.get("courier_id") == courier_id:
                courier = c
                break
        if courier is None:
            payload = {"error": "Courier not found", "courier_id": courier_id}
            out = json.dumps(payload)
            return out

        for t in tracking_ids:
            if t not in courier.get("tracking_ids", []):
                payload = {
                        "error": "Tracking ID not owned by courier",
                        "courier_id": courier_id,
                        "tracking_id": t,
                    }
                out = json.dumps(
                    payload)
                return out

        #Revise order fulfillments
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                        "status": "success",
                        "order_id": order_id,
                        "courier_id": courier_id,
                        "fulfillments": fulfillments,
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
                "name": "AssignCourierToOrder",
                "description": "Assign courier tracking to an order by adding a fulfillment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["order_id", "courier_id", "tracking_ids", "item_ids"],
                },
            },
        }
