# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRooms(Tool):
    """Return all rooms and their current device lists."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:  # no additional parameters
        return json.dumps(list(data.get("rooms", {}).values()), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_rooms",
                "description": "Return all rooms and their current device lists.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
