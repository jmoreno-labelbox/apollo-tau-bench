# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_name = kwargs.get("name")
        department_id = kwargs.get("department_id", f"conflict_{uuid.uuid4().hex[:8]}")
        head_id = kwargs.get("head_id")

        if not all([department_name, head_id]):
            return json.dumps({"error": "department_name and head_id are required parameters"})

        departments = list(data.get("departments", {}).values())

        new_department = {
            "department_id": department_id,
            "department_name": department_name,
            "head_id": head_id,
            "total_capacity_hours": 800,
            "allocated_hours": 680,
            "available_hours": 120,
            "employee_count": 20,
            "avg_utilization": 85
        }

        departments.append(new_department)

        return json.dumps(
            {
                "success": True,
                "department_id": department_id,
                "name": department_name,
                "head_id": head_id,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_department",
                "description": "Create a new department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Department name"},
                        "department_id": {
                            "type": "string",
                            "description": "ID for the department",
                        },
                        "head_id": {
                            "type": "string",
                            "description": "Employee ID for the department head",
                        },
                    },
                    "required": ["name", "head_id"],
                },
            },
        }
