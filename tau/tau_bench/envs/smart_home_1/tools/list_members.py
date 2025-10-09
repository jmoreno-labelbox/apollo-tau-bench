from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListMembers(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], members: list = None) -> str:
        payload = members if members is not None else data.get("members", [])
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListMembers",
                "description": "Return all member profiles.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
