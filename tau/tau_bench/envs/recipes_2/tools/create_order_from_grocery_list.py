# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrderFromGroceryList(Tool):
    """Creates a new order from a grocery list."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        store_id = kwargs.get("store_id")
        list_id = kwargs.get("list_id")
        subtotal_cents = kwargs.get("subtotal_cents")
        total_cents = kwargs.get("total_cents")
        
        orders = list(data.get("orders", {}).values())
        # Automatically create the subsequent order_id.
        new_id = max([order.get("order_id", 0) for order in orders]) + 1 if orders else 10001

        new_order = {
            "order_id": new_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": "placed",
            "subtotal_cents": subtotal_cents,
            "total_cents": total_cents,
            "placed_ts": "2025-08-21T09:00:00Z",
            "scheduled_slot_start_ts": "2025-08-22T18:00:00Z",
            "scheduled_slot_end_ts": "2025-08-22T20:00:00Z"
        }
        data["orders"].append(new_order)
        return json.dumps(new_order)
        
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order_from_grocery_list",
                "description": "Creates a new order from a grocery list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "subtotal_cents": {"type": "integer"},
                        "total_cents": {"type": "integer"},
                    },
                    "required": ["household_id", "store_id", "list_id", "subtotal_cents", "total_cents"],
                },
            },
        }
