from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetDepartmentCapacity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None) -> str:
        if not department:
            payload = {"error": "department is required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", [])
        allocations = data.get("allocations", [])

        dept_employees = [
            emp for emp in employees if emp.get("department") == department
        ]

        total_capacity = len(dept_employees) * 40
        total_allocated = 0

        for employee in dept_employees:
            emp_allocations = [
                alloc
                for alloc in allocations
                if alloc.get("employee_id") == employee.get("employee_id")
                and alloc.get("status") == "active"
            ]
            total_allocated += sum(
                alloc.get("hours_per_week", 0) for alloc in emp_allocations
            )

        available_capacity = total_capacity - total_allocated
        utilization_percentage = (
            (total_allocated / total_capacity * 100) if total_capacity > 0 else 0
        )
        payload = {
                "department": department,
                "total_employees": len(dept_employees),
                "total_capacity": total_capacity,
                "total_allocated": total_allocated,
                "available_capacity": available_capacity,
                "utilization_percentage": round(utilization_percentage, 1),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDepartmentCapacity",
                "description": "Get current capacity information for a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        }
                    },
                    "required": ["department"],
                },
            },
        }
