from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_all_employees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], department_id: str = None, level_id: str = None
    ) -> str:
        employees = data.get("employees", {}).values()
        filtered = [
            e
            for e in employees.values() if (not department_id or e.get("department_id") == department_id)
            and (not level_id or e.get("level_id") == level_id)
        ]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllEmployees",
                "description": "Return a list of all employees, optionally filtered by department_id and/or level_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Department ID to filter employees",
                        },
                        "level_id": {
                            "type": "string",
                            "description": "Job level ID to filter employees",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
