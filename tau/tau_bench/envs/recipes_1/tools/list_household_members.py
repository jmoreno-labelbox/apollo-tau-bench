from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListHouseholdMembers(Tool):
    """Enumerate all members of a household."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        rows = [
            m
            for m in data.get("members", {}).values()
            if int(m.get("household_id")) == int(household_id)
        ]
        return _json_dump(rows)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListHouseholdMembers",
                "description": "List all members belonging to a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
