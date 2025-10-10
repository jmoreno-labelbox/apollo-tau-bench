# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _first_user_id


class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [m for m in data.get("members", []) if m.get("household_id") == household_id]
        return _json_dump(rows)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_household_members","description":"List members for a household; household defaults if omitted.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"}},"required":[]}}}
