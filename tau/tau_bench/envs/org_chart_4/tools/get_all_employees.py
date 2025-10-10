# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_all_employees(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], department_id: str = None, level_id: str = None
    ) -> str:
        employees = list(data.get("employees", {}).values())
        filtered = [
            e
            for e in employees
            if (not department_id or e.get("department_id") == department_id)
            and (not level_id or e.get("level_id") == level_id)
        ]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_employees",
                "description": "Return a list of all employees, optionally filtered by department_id and/or level_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Department ID to filter employees",
                        },
                        "level_id": {
                            "type": "string",
                            "description": "Job level ID to filter employees",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
