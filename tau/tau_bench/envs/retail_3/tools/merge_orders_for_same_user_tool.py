# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergeOrdersForSameUserTool(Tool):
    """
    Merge items from a source order into a target order when both belong to the same user.

    Behavior:
    - Validates both orders exist and belong to the same user_id.
    - Appends all items from source into target's 'items'.
    - Optionally moves payment_history too (flag include_payments).
    - Sets source order status to "cancelled" after merge.
    - Does not merge fulfillments; logistics remain bound to the original order_id.

    Input (kwargs):
        target_order_id (str, required)
        source_order_id (str, required)
        include_payments (bool, optional, default=False)

    Output:
        JSON string with {"target_order_id","source_order_id","moved_items","target_items_len","source_status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_id = kwargs.get("target_order_id")
        source_id = kwargs.get("source_order_id")
        include_payments = bool(kwargs.get("include_payments", False))

        if not target_id or not source_id or target_id == source_id:
            return json.dumps(
                {"error": "target_order_id and source_order_id must be provided and different"},
                indent=2,
            )

        orders = list(data.get("orders", {}).values())
        target = next((o for o in orders if o.get("order_id") == target_id), None)
        source = next((o for o in orders if o.get("order_id") == source_id), None)
        if not target or not source:
            return json.dumps({"error": "target or source order not found"}, indent=2)

        if target.get("user_id") != source.get("user_id"):
            return json.dumps({"error": "orders belong to different users"}, indent=2)

        moved_items = len(source.get("items", []))
        (target.setdefault("items", [])).extend(source.get("items", []))

        if include_payments and source.get("payment_history"):
            (target.setdefault("payment_history", [])).extend(source.get("payment_history", []))

        source["status"] = "cancelled"

        return json.dumps(
            {
                "target_order_id": target_id,
                "source_order_id": source_id,
                "moved_items": moved_items,
                "target_items_len": len(target.get("items", [])),
                "source_status": source.get("status"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_orders_for_same_user",
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
