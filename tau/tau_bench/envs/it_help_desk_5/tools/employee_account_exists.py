from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class EmployeeAccountExists(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str = None, last_name: str = None) -> str:
        if first_name is None or last_name is None:
            payload = {"error": "first_name and last_name are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if (
                employee["first_name"] == first_name
                and employee["last_name"] == last_name
            ):
                payload = {"account_exists": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"account_exists": False}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "employeeAccountExists",
                "description": "Checks whether an employee account exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the employee to search for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the employee to search for.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }
