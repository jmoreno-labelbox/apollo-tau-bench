from tau_bench.envs.tool import Tool
import json
from typing import Any

class RemoveDeviceFromRoom(Tool):
    """Remove a device from a designated room."""

    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str) -> str:
        rooms_doc: list[dict[str, Any]] = data.get("rooms", [])
        for room in rooms_doc:
            if room["id"] == room_id:
                room_devices = room.get("devices", [])
                if device_id not in room_devices:
                    payload = {"error": "Device not present in room"}
                    out = json.dumps(payload, indent=2)
                    return out
                room["devices"] = [d for d in room_devices if d != device_id]
                payload = {"success": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Room not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeDeviceFromRoom",
                "description": "Detach a device from a specific room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "Room identifier.",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }
