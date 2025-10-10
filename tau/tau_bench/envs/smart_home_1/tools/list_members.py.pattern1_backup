# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListMembers(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps(data.get("members", []), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_members",
                "description": "Return all member profiles.",
                "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False},
            },
        }
