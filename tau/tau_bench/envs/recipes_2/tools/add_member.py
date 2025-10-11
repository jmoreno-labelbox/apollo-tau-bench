# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddMember(Tool):
    """Adds a new member to a household."""
    @staticmethod
    def invoke(data: Dict[str, Any], birthdate, full_name, household_id, is_child) -> str:
        members = list(data.get("members", {}).values())
        new_id = max([m.get("member_id", 0) for m in members]) + 1 if members else 301
        new_member = {
            "member_id": new_id, "household_id": household_id, "full_name": full_name,
            "birthdate": birthdate, "is_child": is_child, "activity_level": "medium",
            "dietary_notes": "", "allergies_json": ["none"], "target_calories": 1400, "target_protein": 35
        }
        data["members"].append(new_member)
        return json.dumps(new_member)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_member",
                "description": "Adds a new member to a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                        "birthdate": {"type": "string", "description": "YYYY-MM-DD format."},
                        "is_child": {"type": "boolean"},
                    },
                    "required": ["household_id", "full_name", "birthdate", "is_child"],
                },
            },
        }
