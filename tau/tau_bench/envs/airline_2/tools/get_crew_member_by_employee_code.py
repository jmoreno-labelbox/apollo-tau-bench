from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCrewMemberByEmployeeCode(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_code: str) -> str:
        for c in data.get("crew_members", []):
            if c.get("employee_code") == employee_code:
                return _j(c)
        return _j({})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewMemberByEmployeeCode",
                "description": "Return one crew member by employee_code.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_code": {"type": "string"}},
                    "required": ["employee_code"],
                },
            },
        }
