# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserAddress(Tool):
    """Update a user's address to the provided fields."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        user_id = kwargs.get('user_id')
        address = kwargs.get('address')
        if not user_id or not isinstance(address, dict):
            return json.dumps({"error":"user_id and address (object) are required"}, indent=2)
        user = _find_user(data, user_id)
        if not user:
            return json.dumps({"error":f"user_id {user_id} not found"}, indent=2)
        user['address'] = address
        return json.dumps({"success": True, "user_id": user_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_user_address","description":"Replace a user's address with the provided object.","parameters":{"type":"object","properties":{"user_id":{"type":"string"},"address":{"type":"object"}},"required":["user_id","address"]}}}
