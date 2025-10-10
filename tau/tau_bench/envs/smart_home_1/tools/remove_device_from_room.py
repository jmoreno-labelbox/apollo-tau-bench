# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveDeviceFromRoom(Tool):
    """Detach a device from a specific room."""

    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        rooms_doc: List[Dict[str, Any]] = list(data.get("rooms", {}).values())
        for room in rooms_doc:
            if room["id"] == room_id:
                room_devices = room.get("devices", [])
                if device_id not in room_devices:
                    return json.dumps({"error": "Device not present in room"}, indent=2)
                room["devices"] = [d for d in room_devices if d != device_id]
                return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Room not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_device_from_room",
                "description": "Detach a device from a specific room.",
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
