# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department, user_id) -> str:
        new_department = department
        for user in list(data.get('users', {}).values()):
            if user.get('user_id') == user_id:
                user['department'] = new_department
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_department",
                        "description": "Updates the department for a specific user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "department": {"type": "string"}
                                },
                                "required": ["user_id", "department"]
                        }
                }
        }
