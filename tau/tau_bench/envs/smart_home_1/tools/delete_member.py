# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteMember(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], member_id: str) -> str:
        members = list(data.get("members", {}).values())
        new_members = [m for m in members if m["id"] != member_id]
        if len(new_members) == len(members):
            return json.dumps({"error": "Member not found"}, indent=2)
        data["members"] = new_members
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_member",
                "description": "Remove a member entry.",
                "parameters": {
                    "type": "object",
                    "properties": {"member_id": {"type": "string", "description": "Member identifier."}},
                    "required": ["member_id"],
                    "additionalProperties": False,
                },
            },
        }
