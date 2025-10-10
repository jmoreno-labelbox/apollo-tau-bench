# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddDeviceToRoom(Tool):
    """Associate an existing device with a room."""

    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        rooms_doc: List[Dict[str, Any]] = list(data.get("rooms", {}).values())
        target_room = next(
            (room for room in rooms_doc if room["id"] == room_id),
            None,
        )
        if not target_room:
            return json.dumps({"error": "Room not found"}, indent=2)
        if device_id in target_room.get("devices", []):
            return json.dumps({"error": "Device already assigned"}, indent=2)
        target_room.setdefault("devices", []).append(device_id)
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device_to_room",
                "description": "Associate an existing device with a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room identifier."},
                        "device_id": {"type": "string", "description": "Device identifier."},
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }
