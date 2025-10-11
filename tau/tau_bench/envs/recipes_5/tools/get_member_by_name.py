# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class GetMemberByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], full_name, household_id) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        members = [m for m in data.get("members", []) if m.get("household_id") == household_id]
        m = None
        if full_name:
            m = next((x for x in members if x.get("full_name") == full_name), None)
        if m is None and members:
            adults = [x for x in members if not x.get("is_child")]
            m = adults[0] if adults else members[0]
        if not m:
            return _json_dump({"error": "no member found"})
        return _json_dump(m)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_member_by_name","description":"Find a member by name; defaults to the first adult in the default household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"full_name":{"type":"string"}},"required":[]}}}
