from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListRooms(Tool):
    """Provide all rooms along with their current lists of devices."""

    @staticmethod
    def invoke(data: dict[str, Any], rooms: list = None) -> str:
        payload = rooms if rooms is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRooms",
                "description": "Return all rooms and their current device lists.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
