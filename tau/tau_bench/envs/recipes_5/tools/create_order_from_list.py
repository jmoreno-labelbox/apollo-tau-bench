# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id














def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    return max(int(r.get(key, default)) for r in records)

def _latest_list_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    gl = _latest_list_for_household(data, household_id)
    return int(gl["list_id"]) if gl else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_store_id(data: Dict[str, Any]) -> Optional[int]:
    stores = data.get("stores", [])
    if not stores:
        return None
    return int(sorted(stores, key=lambda s: int(s.get("store_id", 10**9)))[0]["store_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class CreateOrderFromList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id, list_id, scheduled_slot_end_ts, scheduled_slot_start_ts, store_id) -> str:
        slot_start = scheduled_slot_start_ts
        slot_end = scheduled_slot_end_ts
        if store_id is None:
            store_id = _default_store_id(data)
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        if list_id is None:
            list_id = _latest_list_id(data, household_id)
        if not slot_start:
            slot_start = "2025-01-02T18:00:00Z"
        if not slot_end:
            slot_end = "2025-01-02T20:00:00Z"
        if household_id is None or store_id is None or list_id is None:
            return _json_dump({"error": "unable to infer household, store, or list"})
        orders = list(data.get("orders", {}).values())
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
            "scheduled_slot_start_ts": str(slot_start),
            "scheduled_slot_end_ts": str(slot_end),
        }
        orders.append(row)
        return _json_dump({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_order_from_list","description":"Create a new order shell; infers household, store, list, and slot if omitted.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"store_id":{"type":"integer"},"list_id":{"type":"integer"},"scheduled_slot_start_ts":{"type":"string"},"scheduled_slot_end_ts":{"type":"string"}},"required":[]}}}