from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMemberInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member_ids: list[str] | None = None) -> str:
        members = data.get("members", [])
        if member_ids:
            result = [m for m in members if m.get("id") in member_ids]
        else:
            result = members
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getMemberInfo",
                "description": "Get information about one or more household members.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of member IDs to retrieve. If empty, all members will be returned.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }
