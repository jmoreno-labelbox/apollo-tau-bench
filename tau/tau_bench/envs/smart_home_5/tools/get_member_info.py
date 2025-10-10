# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMemberInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], member_ids: Optional[List[str]] = None) -> str:
        members = data.get('members', [])
        if member_ids:
            result = [m for m in members if m.get('id') in member_ids]
        else:
            result = members
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_member_info",
                "description": "Get information about one or more household members.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of member IDs to retrieve. If empty, all members will be returned."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
