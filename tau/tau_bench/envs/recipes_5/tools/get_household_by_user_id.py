# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _household_for_user, _first_user_id








def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

class GetHouseholdByUserId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        if user_id is None:
            user_id = _first_user_id(data)
        hh = _household_for_user(data, user_id)
        if not hh:
            return _json_dump({"error": "no households available"})
        return _json_dump(hh)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_household_by_user_id","description":"Get household for user_id; defaults to the first household if unspecified.","parameters":{"type":"object","properties":{"user_id":{"type":"integer"}},"required":[]}}}