from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class list_department_headcount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None) -> str:
        headcount = len(
            [
                e
                for e in data.get("employees", {}).values()
                if e.get("department_id") == department_id
                and e.get("status") == "Active"
            ]
        )
        payload = {"department_id": department_id, "active_headcount": headcount}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListDepartmentHeadcount",
                "description": "Return current headcount of active employees for a department.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                },
            },
        }
