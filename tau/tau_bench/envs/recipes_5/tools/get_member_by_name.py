from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMemberByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None, full_name: str = None) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        members = [
            m for m in data.get("members", {}).values() if m.get("household_id") == household_id
        ]
        m = None
        if full_name:
            m = next((x for x in members if x.get("full_name") == full_name), None)
        if m is None and members:
            adults = [x for x in members.values() if not x.get("is_child")]
            m = adults[0] if adults else members[0]
        if not m:
            return _json_dump({"error": "no member found"})
        return _json_dump(m)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getMemberByName",
                "description": "Find a member by name; defaults to the first adult in the default household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
