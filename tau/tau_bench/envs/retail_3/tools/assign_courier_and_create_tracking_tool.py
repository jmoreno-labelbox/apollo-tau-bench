from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignCourierAndCreateTrackingTool(Tool):
    """
    Assign a courier to an order and generate a tracking entry in tracking.json.

    Behavior:
    - Retrieves the order (orders.json) and the user's country (users.json) to select a courier from couriers.json.
    - Chooses the first available tracking_id from the selected courier's tracking_ids.
    - Creates a new entry in tracking.json:
        {
          "tracking_id": [ "<id>" ],
          "order_id": "...",
          "courier_name": "...",
          "status_history": [{ "status": "label_created", "timestamp": "UTC ISO" }]
        }
    - Additionally, adds a fulfillment snippet to the order in orders.json:
        {
          "status": "label_created",
          "tracking_id": "<id>",
          "courier": "<courier_name>",
          "timestamp": "UTC ISO"
        }

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        users = data.get("users", [])
        user = next(
            (u for u in users if u.get("user_id") == order.get("user_id")), None
        )
        if not user:
            payload = {"error": f"user '{order.get('user_id')}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        country = ((user.get("address") or {}).get("country")) or "USA"
        couriers = data.get("couriers", [])
        courier = next(
            (c for c in couriers if country in (c.get("coverage_area") or [])),
            couriers[0] if couriers else None,
        )
        if not courier:
            payload = {"error": f"No courier covers '{country}'"}
            out = json.dumps(payload, indent=2)
            return out

        used = {
            tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])
        }
        tid = next(
            (tid for tid in courier.get("tracking_ids", []) if tid not in used), None
        )
        if not tid:
            payload = {
                    "error": f"No available tracking_id for courier '{courier.get('name')}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        data.setdefault("tracking", []).append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier.get("name"),
                "status_history": [
                    {"status": "label_created", "timestamp": _now_iso()}
                ],
            }
        )

        order.setdefault("fulfillments", []).append(
            {
                "status": "label_created",
                "tracking_id": tid,
                "courier": courier.get("name"),
                "timestamp": _now_iso(),
            }
        )
        payload = {
                "order_id": order_id,
                "tracking_id": tid,
                "courier_name": courier.get("name"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignCourierAndCreateTracking",
                "description": "Assign a courier based on user's country and create a new tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Target order_id in orders.json.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
