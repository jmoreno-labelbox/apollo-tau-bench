from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class MergeOrdersForSameUserTool(Tool):
    """
    Combine items from a source order into a target order when both are associated with the same user.

    Behavior:
    - Confirms both orders exist and are linked to the same user_id.
    - Adds all items from the source to the target's 'items'.
    - Optionally transfers payment_history as well (flag include_payments).
    - Changes the source order status to "cancelled" after the merge.
    - Does not merge fulfillments; logistics remain tied to the original order_id.

    Input (kwargs):
        target_order_id (str, required)
        source_order_id (str, required)
        include_payments (bool, optional, default=False)

    Output:
        JSON string with {"target_order_id","source_order_id","moved_items","target_items_len","source_status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], target_order_id: str = None, source_order_id: str = None, include_payments: bool = False) -> str:
        if not target_order_id or not source_order_id or target_order_id == source_order_id:
            payload = {
                    "error": "target_order_id and source_order_id must be provided and different"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        orders = data.get("orders", [])
        target = next((o for o in orders if o.get("order_id") == target_order_id), None)
        source = next((o for o in orders if o.get("order_id") == source_order_id), None)
        if not target or not source:
            payload = {"error": "target or source order not found"}
            out = json.dumps(payload, indent=2)
            return out

        if target.get("user_id") != source.get("user_id"):
            payload = {"error": "orders belong to different users"}
            out = json.dumps(payload, indent=2)
            return out

        moved_items = len(source.get("items", []))
        (target.setdefault("items", [])).extend(source.get("items", []))

        if include_payments and source.get("payment_history"):
            (target.setdefault("payment_history", [])).extend(
                source.get("payment_history", [])
            )

        source["status"] = "cancelled"
        payload = {
                "target_order_id": target_order_id,
                "source_order_id": source_order_id,
                "moved_items": moved_items,
                "target_items_len": len(target.get("items", [])),
                "source_status": source.get("status"),
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
                "name": "MergeOrdersForSameUser",
                "description": "Merge items (and optionally payments) from a source order into a target order for the same user; cancel the source.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_order_id": {"type": "string"},
                        "source_order_id": {"type": "string"},
                        "include_payments": {"type": "boolean", "default": False},
                    },
                    "required": ["target_order_id", "source_order_id"],
                },
            },
        }
