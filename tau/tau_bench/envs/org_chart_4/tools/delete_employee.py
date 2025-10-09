from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class delete_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", {}).values()
        for i, e in enumerate(employees):
            if e["employee_id"] == employee_id:
                del employees[i]
                payload = {"success": True, "employee_id": employee_id}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteEmployee",
                "description": "Delete the employee record for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to delete",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
