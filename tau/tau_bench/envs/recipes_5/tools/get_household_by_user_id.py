# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _household_for_user, _first_user_id


class GetHouseholdByUserId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        if user_id is None:
            user_id = _first_user_id(data)
        hh = _household_for_user(data, user_id)
        if not hh:
            return _json_dump({"error": "no households available"})
        return _json_dump(hh)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_household_by_user_id","description":"Get household for user_id; defaults to the first household if unspecified.","parameters":{"type":"object","properties":{"user_id":{"type":"integer"}},"required":[]}}}
