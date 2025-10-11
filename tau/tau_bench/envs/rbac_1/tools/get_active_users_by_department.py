# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetActiveUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department) -> str:
        active_users = [
                user['user_id'] for user in list(data.get('users', {}).values())
                if user.get('department') == department and user.get('status') == 'ACTIVE'
        ]
        return json.dumps({"users": active_users})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_active_users_by_department",
                        "description": "Retrieves a list of active users for a specific department.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "department": {
                                                "type": "string",
                                                "description": "The department to filter by."
                                        }
                                },
                                "required": ["department"]
                        }
                }
        }
