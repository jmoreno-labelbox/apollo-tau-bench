# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id


class CreateOrderFromList(Tool):
    """Create an order shell for a list+store with scheduled slot; returns order_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        store_id = kwargs.get("store_id")
        list_id = kwargs.get("list_id")
        slot_start = kwargs.get("scheduled_slot_start_ts")
        slot_end = kwargs.get("scheduled_slot_end_ts")
        if household_id is None or store_id is None or list_id is None or not slot_start or not slot_end:
            return _json_dump({"error": "household_id, store_id, list_id, scheduled_slot_start_ts, scheduled_slot_end_ts are required"})
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
            "scheduled_slot_start_ts": str(slot_start),
            "scheduled_slot_end_ts": str(slot_end),
        }
        tbl.append(row)
        return _json_dump({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_order_from_list",
            "description":"Create a new order shell for a grocery list and store.",
            "parameters":{"type":"object","properties":{
                "household_id":{"type":"integer"},
                "store_id":{"type":"integer"},
                "list_id":{"type":"integer"},
                "scheduled_slot_start_ts":{"type":"string"},
                "scheduled_slot_end_ts":{"type":"string"}
            },"required":["household_id","store_id","list_id","scheduled_slot_start_ts","scheduled_slot_end_ts"]}
        }}
