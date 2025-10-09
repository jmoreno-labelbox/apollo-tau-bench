from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class update_employee_job_level(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, new_level: str = None) -> str:
        employee = find_employee(data.get("employees", {}).values(), employee_id)
        if not employee:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employee["level_id"] = new_level
        payload = {"success": f"Job level for {employee_id} updated to {new_level}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeeJobLevel",
                "description": "Change an employee's job level ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_level": {"type": "string"},
                    },
                    "required": ["employee_id", "new_level"],
                },
            },
        }
