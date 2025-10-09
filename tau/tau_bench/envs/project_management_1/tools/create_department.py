from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, department_id: str = None, head_id: str = None) -> str:
        department_name = name
        department_id = department_id or f"conflict_{uuid.uuid4().hex[:8]}"
        head_id = head_id

        if not all([department_name, head_id]):
            payload = {"error": "department_name and head_id are required parameters"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", {}).values()

        new_department = {
            "department_id": department_id,
            "department_name": department_name,
            "head_id": head_id,
            "total_capacity_hours": 800,
            "allocated_hours": 680,
            "available_hours": 120,
            "employee_count": 20,
            "avg_utilization": 85,
        }

        data["departments"][department_id] = new_department
        payload = {
            "success": True,
            "department_id": department_id,
            "name": department_name,
            "head_id": head_id,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDepartment",
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
