# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDepartmentCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department) -> str:
        if not department:
            return json.dumps({"error": "department is required"})

        employees = list(data.get("employees", {}).values())
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

        return json.dumps(
            {
                "department": department,
                "total_employees": len(dept_employees),
                "total_capacity": total_capacity,
                "total_allocated": total_allocated,
                "available_capacity": available_capacity,
                "utilization_percentage": round(utilization_percentage, 1),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_capacity",
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
