from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteMember(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], member_id: str) -> str:
        members = data.get("members", [])
        new_members = [m for m in members if m["id"] != member_id]
        if len(new_members) == len(members):
            payload = {"error": "Member not found"}
            out = json.dumps(payload, indent=2)
            return out
        data["members"] = new_members
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteMember",
                "description": "Remove a member entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "string",
                            "description": "Member identifier.",
                        }
                    },
                    "required": ["member_id"],
                    "additionalProperties": False,
                },
            },
        }
