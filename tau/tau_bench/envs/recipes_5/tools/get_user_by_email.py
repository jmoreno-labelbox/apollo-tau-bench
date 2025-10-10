# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class GetUserByEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        user_id = kwargs.get("user_id")
        user = None
        if email:
            user = next((u for u in list(data.get("users", {}).values()) if u.get("email") == email), None)
        if user is None and user_id is not None:
            user = next((u for u in list(data.get("users", {}).values()) if u.get("user_id") == user_id), None)
        if user is None:
            fid = _first_user_id(data)
            user = next((u for u in list(data.get("users", {}).values()) if u.get("user_id") == fid), None)
        if not user:
            return _json_dump({"error": "no users available"})
        return _json_dump(user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function":{"name":"get_user_by_email","description":"Retrieve a user by email or user_id; defaults to the first user.","parameters":{"type":"object","properties":{"email":{"type":"string"},"user_id":{"type":"integer"}},"required":[]}}}
