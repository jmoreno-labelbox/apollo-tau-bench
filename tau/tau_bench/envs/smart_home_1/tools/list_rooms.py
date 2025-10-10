# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRooms(Tool):
    """Return all rooms and their current device lists."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:  # no extra args
        return json.dumps(data.get("rooms", []), indent=2)

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
