from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpsertMember(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], id: str, profile: dict[str, Any]) -> str:
        members = data.get("members", {}).values()
        for m in members.values():
            if m["id"] == id:
                m.update(profile)
                payload = {"success": "updated"}
                out = json.dumps(payload, indent=2)
                return out
        profile["id"] = id
        data["members"][profile["member_id"]] = profile
        payload = {"success": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertMember",
                "description": "Create or update a household member profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Member identifier."},
                        "profile": {
                            "type": "object",
                            "description": "Key/value pairs of member profile.",
                        },
                    },
                    "required": ["id", "profile"],
                    "additionalProperties": False,
                },
            },
        }
