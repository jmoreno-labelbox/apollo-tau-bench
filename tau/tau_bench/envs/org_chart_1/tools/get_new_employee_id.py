from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_new_employee_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        employees = data.get("employees", [])
        used_ids = [e["employee_id"] for e in employees]
        for i in range(10000, 100000):
            if f"E{i:05d}" not in used_ids:
                payload = f"E{i:05d}"
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "no unused employee ID found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNewEmployeeId",
                "description": "Return an employee ID that is not currently in use.",
                "parameters": {},
            },
        }
