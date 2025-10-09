from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class update_employee_status(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, new_status: str = None) -> str:
        employee = find_employee(data.get("employees", {}).values(), employee_id)
        if not employee:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employee["status"] = new_status
        if new_status.lower() == "terminated":
            employee["termination_date"] = "2025-06-24"  # Utilizing our typical "today"
        payload = {"success": f"Employee {employee_id} status updated to {new_status}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeeStatus",
                "description": "Update an employee's current status (e.g., 'Active', 'On Leave', 'Terminated').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["employee_id", "new_status"],
                },
            },
        }
