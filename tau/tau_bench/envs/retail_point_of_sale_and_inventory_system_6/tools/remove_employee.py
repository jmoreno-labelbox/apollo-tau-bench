from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class remove_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        employees = data.get("employees", [])

        if employee_id is None:
            payload = {"error": "employee_id must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for employee in employees:
            if employee["employee_id"] == employee_id:
                del employee
                payload = {"success": f"Removed employee: {employee_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "No employee found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveEmployee",
                "description": "Removes an employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to remove",
                        },
                    },
                },
            },
        }
