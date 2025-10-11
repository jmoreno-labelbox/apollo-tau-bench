# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department) -> str:
        department_name = department
        users_in_dept = [
                user for user in list(data.get('users', {}).values())
                if user.get('department') == department_name
        ]
        return json.dumps({"users": users_in_dept})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_users_by_department",
                        "description": "Retrieves all users for a given department by the department's name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "department": {
                                                "type": "string",
                                                "description": "The name of the department to search for (e.g., 'Engineering')."
                                        }
                                },
                                "required": ["department"]
                        }
                }
        }
