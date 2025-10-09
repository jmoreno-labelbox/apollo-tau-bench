from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_department(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str) -> str:
        departments = data.get("departments", {}).values()
        for d in departments.values():
            if d["department_id"] == department_id:
                payload = d
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"department_id {department_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDepartment",
                "description": "Return the department record for the given department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Unique ID of the department to fetch",
                        }
                    },
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }
