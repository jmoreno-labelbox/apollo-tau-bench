from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertMember(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member: dict[str, Any]) -> str:
        if not member:
            payload = {"error": "member object required"}
            out = json.dumps(payload, indent=2)
            return out
        members = _load("members", data)
        idx, _ = _find(members, member["id"])
        if idx is not None:
            members[idx].update(member)
            msg = "updated"
        else:
            members.append(member)
            msg = "added"
            data["members"] = members
        payload = {"success": f"member {msg}", "member": member}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertMember",
                "description": "Create or update a household member record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member": {
                            "type": "object",
                            "description": "Full or partial member object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["member"],
                    "additionalProperties": False,
                },
            },
        }
