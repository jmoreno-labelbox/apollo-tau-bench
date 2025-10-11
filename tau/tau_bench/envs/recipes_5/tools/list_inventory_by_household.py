# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class ListInventoryByHousehold(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [i for i in data.get("inventory_items", []) if i.get("household_id") == household_id]
        return _json_dump({"household_id": household_id, "inventory_items": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_inventory_by_household","description":"Get inventory items for a household; defaults to primary household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"}},"required":[]}}}