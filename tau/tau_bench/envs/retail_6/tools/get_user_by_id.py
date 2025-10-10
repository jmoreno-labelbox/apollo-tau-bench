# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserById(Tool):
    """Get a user by user_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        if not user_id:
            return json.dumps({"error": "user_id is required"}, indent=2)
        user = _find_user(data, user_id)
        return json.dumps(user or {"error": f"user_id {user_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_user_by_id","description":"Return the user object by user_id.","parameters":{"type":"object","properties":{"user_id":{"type":"string"}},"required":["user_id"]}}}
