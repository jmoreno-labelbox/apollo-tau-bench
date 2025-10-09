from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateOrderFromGroceryList(Tool):
    """Forms a new order based on a grocery list."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        store_id: int = None,
        list_id: int = None,
        subtotal_cents: int = None,
        total_cents: int = None
    ) -> str:
        orders = data.get("orders", [])
        # Automatically create the next order_id
        new_id = (
            max([order.get("order_id", 0) for order in orders]) + 1 if orders else 10001
        )

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
            "scheduled_slot_end_ts": "2025-08-22T20:00:00Z",
        }
        data["orders"].append(new_order)
        payload = new_order
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrderFromGroceryList",
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
                    "required": [
                        "household_id",
                        "store_id",
                        "list_id",
                        "subtotal_cents",
                        "total_cents",
                    ],
                },
            },
        }
