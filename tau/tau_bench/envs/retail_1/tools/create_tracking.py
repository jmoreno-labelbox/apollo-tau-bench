from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTracking(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        item_ids: list[str],
        courier_id: str,
        delivery_option: str,
    ) -> str:
        pass
        orders = data["orders"]
        order = [row for row in orders.values() if row["order_id"] == order_id]

        couriers = data["couriers"]
        #Verify if the delivery carrier is present
        courier_id_list = [row["courier_id"] for row in couriers]
        if courier_id not in courier_id_list:
            payload = {
                    "error": "Delivery carrier not found. It must be the id of a courier from the couriers database."
                }
            out = json.dumps(
                payload)
            return out

        if len(order) > 1:
            payload = {"error": "Multiple orders found"}
            out = json.dumps(payload)
            return out
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        tracking_id = f"TRK{len(data['tracking']) + 1:07d}"

        #Insert into the order database
        fulfillment = {"tracking_id": [tracking_id], "item_ids": item_ids}
        order.setdefault("fulfillments", []).append(fulfillment)

        #Insert into the tracking database
        tracking_dict = {}
        tracking_dict["tracking_id"] = [tracking_id]
        tracking_dict["item_ids"] = item_ids
        tracking_dict["order_id"] = order_id
        tracking_dict["address"] = order.get("address", {}).values()
        tracking_dict["delivery_carrier"] = courier_id
        tracking_dict["delivery_option"] = delivery_option
        tracking_dict["tracking_history"] = {"received": "2025-01-30T10:26:19.115651"}
        data["tracking"][tracking_id] = tracking_dict

        courier = [row for row in couriers.values() if row["courier_id"] == courier_id]
        courier[0]["tracking_ids"].append(tracking_id)
        payload = tracking_dict
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTracking",
                "description": "Create a new tracking entry for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to create tracking for.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs associated with the tracking.",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "The delivery carrier for the tracking.",
                        },
                        "delivery_option": {
                            "type": "string",
                            "description": "Delivery options for the tracking.",
                        },
                    },
                    "required": ["order_id", "item_ids"],
                },
            },
        }
