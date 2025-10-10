# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMembersByHouseholdId(Tool):
    """Retrieves all members for a given household ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> str:
        members = list(data.get("members", {}).values())
        household_members = [member for member in members if member.get("household_id") == household_id]
        return json.dumps(household_members)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_members_by_household_id",
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
