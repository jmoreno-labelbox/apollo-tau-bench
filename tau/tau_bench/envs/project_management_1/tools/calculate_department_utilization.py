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

class CalculateDepartmentUtilization(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None) -> str:
        if not department:
            payload = {"error": "department is required"}
            out = json.dumps(payload)
            return out

        result = GetDepartmentCapacity.invoke(data, department=department)
        dept_data = json.loads(result)
        payload = {
                "department": department,
                "dept_utilization": dept_data.get("utilization_percentage", 0),
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
                "name": "CalculateDepartmentUtilization",
                "description": "Calculate overall department utilization",
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
