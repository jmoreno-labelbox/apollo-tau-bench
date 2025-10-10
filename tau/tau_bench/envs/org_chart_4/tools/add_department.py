# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_department(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department: dict) -> str:
        departments = data.setdefault("departments", [])
        departments.append(department)
        return json.dumps(
            {"success": True, "department_id": department.get("department_id")},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_department",
                "description": "Add a new department record. The department object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "object",
                            "description": "Department record to add",
                        }
                    },
                    "required": ["department"],
                    "additionalProperties": False,
                },
            },
        }
