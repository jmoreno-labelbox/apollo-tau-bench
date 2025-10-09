from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class update_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, updates: dict[str, Any]) -> str:
        employees = data.get("employees", {}).values()
        changes = updates

        updated = False
        for e in employees.values():
            if e["employee_id"] == employee_id:
                e.update(changes)
                updated = True
                break

        if not updated:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        data["employees"] = employees
        payload = {"success": f"employee {employee_id} updated"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployee",
                "description": "Patch one or more fields on an existing employee record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "updates": {
                            "type": "object",
                            "description": "Dictionary of field:value pairs to update",
                        },
                    },
                    "required": ["employee_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
