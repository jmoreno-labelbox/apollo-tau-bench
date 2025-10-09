from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class create_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee: dict[str, Any]) -> str:
        new_emp = employee
        if not new_emp:
            payload = {"error": "employee payload required"}
            out = json.dumps(payload, indent=2)
            return out

        employees = data.get("employees", {}).values()
        if any(e["employee_id"] == new_emp["employee_id"] for e in employees.values()):
            payload = {"error": "employee_id already exists"}
            out = json.dumps(payload, indent=2)
            return out

        data["employees"][employee_id] = new_emp
        data["employees"] = employees
        payload = {"success": f'employee {new_emp["employee_id"]} created'}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateEmployee",
                "description": "Insert a completely new employee record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee": {
                            "type": "object",
                            "description": "Full employee JSON object conforming to employees.json schema",
                        }
                    },
                    "required": ["employee"],
                    "additionalProperties": False,
                },
            },
        }
