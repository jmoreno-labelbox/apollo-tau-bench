# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrderFromList(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        store_id: int,
        list_id: int,
        scheduled_slot_start_ts: str,
        scheduled_slot_end_ts: str,
    ) -> str:
        tbl = _tbl(data, "orders")
        next_id = _max_id(tbl, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(list_id),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00",
            "scheduled_slot_start_ts": str(scheduled_slot_start_ts),
            "scheduled_slot_end_ts": str(scheduled_slot_end_ts),
        }
        tbl.append(row)
        return _json({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order_from_list",
                "description": "Create an order header for a list and store.",
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
