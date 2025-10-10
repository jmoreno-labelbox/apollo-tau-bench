# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoomInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_ids: Optional[List[str]] = None) -> str:
        rooms = data.get('rooms', [])
        if room_ids:
            result = [r for r in rooms if r.get('id') in room_ids]
        else:
            result = rooms
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_room_info",
                "description": "Get information about one or more rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of room IDs to retrieve. If empty, all rooms will be returned."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
