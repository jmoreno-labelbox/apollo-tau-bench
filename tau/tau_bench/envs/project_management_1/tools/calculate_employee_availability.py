from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CalculateEmployeeAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

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
        payload = {
                "employee_id": employee_id,
                "total_allocated_hours": total_allocated,
                "available_hours": available_hours,
                "availability_percentage": round((available_hours / 40) * 100, 1),
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
                "name": "CalculateEmployeeAvailability",
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
