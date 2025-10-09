from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListAllEmployees(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employees: list = None) -> str:
        employees = employees if employees is not None else data.get("employees", [])
        payload = {"employees": employees, "count": len(employees)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllEmployees",
                "description": "List all employees.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
