# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_department(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_id: str) -> str:
        departments = list(data.get("departments", {}).values())
        for d in departments:
            if d["department_id"] == department_id:
                return json.dumps(d, indent=2)
        return json.dumps(
            {"error": f"department_id {department_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department",
                "description": "Return the department record for the given department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Unique ID of the department to fetch",
                        }
                    },
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }
