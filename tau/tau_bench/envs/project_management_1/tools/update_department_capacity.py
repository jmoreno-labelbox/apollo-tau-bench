from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateDepartmentCapacity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, employee_id: str = None, hours_allocated: int = None, cross_department_project: bool = None) -> str:
        if not all([department, employee_id, hours_allocated is not None]):
            payload = {"error": "department, employee_id, and hours_allocated are required"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", [])

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
                payload = {"success": True, "department": dept}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Department '{department}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDepartmentCapacity",
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
