# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAllEmployees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employees = list(data.get("employees", {}).values())
        return json.dumps({"employees": employees, "count": len(employees)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_employees",
                "description": "List all employees.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }
