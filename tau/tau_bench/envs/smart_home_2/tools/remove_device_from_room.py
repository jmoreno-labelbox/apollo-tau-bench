# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find


class RemoveDeviceFromRoom(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        _, room = _find(data.get("rooms", []), room_id)
        if not room:
            return json.dumps({"error": f"room '{room_id}' not found"}, indent=2)
        if device_id not in room.get("devices", []):
            return json.dumps({"error": f"device '{device_id}' not in room"}, indent=2)
        room["devices"].remove(device_id)
        return json.dumps({"success": f"device '{device_id}' removed from room '{room_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_device_from_room",
                "description": "Detach a device from a room without deleting the device itself.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room id"},
                        "device_id": {"type": "string", "description": "Device id"}
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False
                }
            }
        }
