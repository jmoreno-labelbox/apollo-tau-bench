# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id








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

class ComputeAndSetMemberTargets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], member_id) -> str:
        if member_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            members = [m for m in data.get("members", []) if m.get("household_id") == household_id]
            if not members:
                return _json_dump({"error": "no members available"})
            adults = [m for m in members if not m.get("is_child")]
            member_id = adults[0]["member_id"] if adults else members[0]["member_id"]
        m = next((x for x in data.get("members", []) if x.get("member_id") == member_id), None)
        if not m:
            return _json_dump({"error": f"member_id {member_id} not found"})
        if m.get("is_child"):
            calories, protein = 1200, 30
        else:
            calories, protein = 2200, 110
        level = (m.get("activity_level") or "medium").lower()
        bump = {"low": 0.0, "medium": 0.05, "high": 0.10}.get(level, 0.05)
        protein = int(round(protein * (1.0 + bump), 0))
        m["target_calories"] = calories
        m["target_protein"] = protein
        return _json_dump(m)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"compute_and_set_member_targets","description":"Compute and set targets for a member; defaults to first adult member.","parameters":{"type":"object","properties":{"member_id":{"type":"integer"}},"required":[]}}}