# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find


class UpsertMember(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], member: Dict[str, Any]) -> str:
        if not member:
            return json.dumps({"error": "member object required"}, indent=2)
        members = _load("members", data)
        idx, _ = _find(members, member["id"])
        if idx is not None:
            members[idx].update(member)
            msg = "updated"
        else:
            members.append(member)
            msg = "added"
            data["members"] = members
        return json.dumps({"success": f"member {msg}", "member": member}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_member",
                "description": "Create or update a household member record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member": {
                            "type": "object",
                            "description": "Full or partial member object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["member"],
                    "additionalProperties": False
                }
            }
        }
