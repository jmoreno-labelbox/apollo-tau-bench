from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRoomInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_ids: list[str] | None = None) -> str:
        rooms = data.get("rooms", [])
        if room_ids:
            result = [r for r in rooms if r.get("id") in room_ids]
        else:
            result = rooms
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoomInfo",
                "description": "Get information about one or more rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of room IDs to retrieve. If empty, all rooms will be returned.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }
