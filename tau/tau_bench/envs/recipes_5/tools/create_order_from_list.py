from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateOrderFromList(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        store_id: int = None,
        list_id: int = None,
        scheduled_slot_start_ts: str = None,
        scheduled_slot_end_ts: str = None
    ) -> str:
        if store_id is None:
            store_id = _default_store_id(data)
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        if list_id is None:
            list_id = _latest_list_id(data, household_id)
        if not scheduled_slot_start_ts:
            scheduled_slot_start_ts = "2025-01-02T18:00:00Z"
        if not scheduled_slot_end_ts:
            scheduled_slot_end_ts = "2025-01-02T20:00:00Z"
        if household_id is None or store_id is None or list_id is None:
            return _json_dump({"error": "unable to infer household, store, or list"})
        orders = data.get("orders", {}).values()
        next_id = _max_id(orders, "order_id", 10000) + 1
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
        data["orders"][order_id] = row
        return _json_dump({"order_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrderFromList",
                "description": "Create a new order shell; infers household, store, list, and slot if omitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "scheduled_slot_start_ts": {"type": "string"},
                        "scheduled_slot_end_ts": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
