from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_department_by_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None) -> str:
        depts = data.get("departments", {}).values()
        for d in depts:
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
                "name": "GetDepartmentById",
                "description": "Fetch department details by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }
