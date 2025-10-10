# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateEmployeeUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        allocations = data.get("allocations", [])
        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        total_hours = sum(
            alloc.get("hours_per_week", 0) for alloc in employee_allocations
        )
        utilization_percentage = (total_hours / 40) * 100

        return json.dumps(
            {
                "employee_id": employee_id,
                "total_hours": total_hours,
                "utilization_percentage": round(utilization_percentage, 1),
                "allocations_count": len(employee_allocations),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_employee_utilization",
                "description": "Calculate the utilization percentage for an employee",
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
