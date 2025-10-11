# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateEmployeeAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        allocations = data.get("allocations", [])
        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        total_allocated = sum(
            alloc.get("hours_per_week", 0) for alloc in employee_allocations
        )
        available_hours = max(0, 40 - total_allocated)

        return json.dumps(
            {
                "employee_id": employee_id,
                "total_allocated_hours": total_allocated,
                "available_hours": available_hours,
                "availability_percentage": round((available_hours / 40) * 100, 1),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_employee_availability",
                "description": "Calculate available hours for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
