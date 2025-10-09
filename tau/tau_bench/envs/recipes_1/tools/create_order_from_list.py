from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateOrderFromList(Tool):
    """Generate an order shell for a list and store with a scheduled slot; returns order_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        store_id: int = None,
        list_id: int = None,
        scheduled_slot_start_ts: str = None,
        scheduled_slot_end_ts: str = None,
    ) -> str:
        if (
            household_id is None
            or store_id is None
            or list_id is None
            or not scheduled_slot_start_ts
            or not scheduled_slot_end_ts
        ):
            return _json_dump(
                {
                    "error": "household_id, store_id, list_id, scheduled_slot_start_ts, scheduled_slot_end_ts are required"
                }
            )
        tbl = data.setdefault("orders", [])
        next_id = _max_id(tbl, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(list_id),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00Z",
            "scheduled_slot_start_ts": str(scheduled_slot_start_ts),
            "scheduled_slot_end_ts": str(scheduled_slot_end_ts),
        }
        tbl.append(row)
        return _json_dump({"order_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrderFromList",
                "description": "Create a new order shell for a grocery list and store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "scheduled_slot_start_ts": {"type": "string"},
                        "scheduled_slot_end_ts": {"type": "string"},
                    },
                    "required": [
                        "household_id",
                        "store_id",
                        "list_id",
                        "scheduled_slot_start_ts",
                        "scheduled_slot_end_ts",
                    ],
                },
            },
        }
