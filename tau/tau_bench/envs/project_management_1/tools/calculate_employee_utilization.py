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

class CalculateEmployeeUtilization(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", {}).values()
        employee_allocations = [
            alloc
            for alloc in allocations.values() if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        total_hours = sum(
            alloc.get("hours_per_week", 0) for alloc in employee_allocations
        )
        utilization_percentage = (total_hours / 40) * 100
        payload = {
                "employee_id": employee_id,
                "total_hours": total_hours,
                "utilization_percentage": round(utilization_percentage, 1),
                "allocations_count": len(employee_allocations),
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
                "name": "CalculateEmployeeUtilization",
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
