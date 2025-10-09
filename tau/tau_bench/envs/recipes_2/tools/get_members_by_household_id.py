from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMembersByHouseholdId(Tool):
    """Fetches all members associated with a specific household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        members = data.get("members", {}).values()
        household_members = [
            member for member in members.values() if member.get("household_id") == household_id
        ]
        payload = household_members
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMembersByHouseholdId",
                "description": "Retrieves all members for a given household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        }
                    },
                    "required": ["household_id"],
                },
            },
        }
