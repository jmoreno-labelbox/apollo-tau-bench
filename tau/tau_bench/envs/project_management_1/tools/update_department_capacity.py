# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDepartmentCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        employee_id = kwargs.get("employee_id")
        hours_allocated = kwargs.get("hours_allocated")
        cross_department_project = kwargs.get("cross_department_project")

        if not all([department, employee_id, hours_allocated is not None]):
            return json.dumps(
                {"error": "department, employee_id, and hours_allocated are required"}
            )

        departments = list(data.get("departments", {}).values())

        for dept in departments:
            if dept.get("department_name") == department:
                if "capacity_changes" not in dept:
                    dept["capacity_changes"] = []

                change_entry = {
                    "employee_id": employee_id,
                    "hours_allocated": hours_allocated,
                    "cross_department_project": cross_department_project,
                    "timestamp": datetime.now().isoformat(),
                }

                dept["capacity_changes"].append(change_entry)

                return json.dumps({"success": True, "department": dept})

        return json.dumps({"error": f"Department '{department}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_department_capacity",
                "description": "Update department capacity when allocations change",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        },
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "hours_allocated": {
                            "type": "number",
                            "description": "Hours allocated",
                        },
                        "cross_department_project": {
                            "type": "string",
                            "description": "Cross-department project ID",
                        },
                    },
                    "required": ["department", "employee_id", "hours_allocated"],
                },
            },
        }
