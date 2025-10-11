# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertMember(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], id: str, profile: Dict[str, Any]) -> str:
        members = list(data.get("members", {}).values())
        for m in members:
            if m["id"] == id:
                m.update(profile)
                return json.dumps({"success": "updated"}, indent=2)
        profile["id"] = id
        members.append(profile)
        return json.dumps({"success": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_member",
                "description": "Create or update a household member profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Member identifier."},
                        "profile": {"type": "object", "description": "Key/value pairs of member profile."},
                    },
                    "required": ["id", "profile"],
                    "additionalProperties": False,
                },
            },
        }
