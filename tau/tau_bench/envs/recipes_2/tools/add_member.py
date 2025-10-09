from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddMember(Tool):
    """Inserts a new member into a household."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, full_name: str = None, birthdate: str = None, is_child: bool = None) -> str:
        members = data.get("members", {}).values()
        new_id = max([m.get("member_id", 0) for m in members.values()]) + 1 if members else 301
        new_member = {
            "member_id": new_id,
            "household_id": household_id,
            "full_name": full_name,
            "birthdate": birthdate,
            "is_child": is_child,
            "activity_level": "medium",
            "dietary_notes": "",
            "allergies_json": ["none"],
            "target_calories": 1400,
            "target_protein": 35,
        }
        data["members"].append(new_member)
        payload = new_member
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addMember",
                "description": "Adds a new member to a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                        "birthdate": {
                            "type": "string",
                            "description": "YYYY-MM-DD format.",
                        },
                        "is_child": {"type": "boolean"},
                    },
                    "required": ["household_id", "full_name", "birthdate", "is_child"],
                },
            },
        }
