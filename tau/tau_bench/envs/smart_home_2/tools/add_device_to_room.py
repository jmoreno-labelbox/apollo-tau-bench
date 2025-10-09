from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddDeviceToRoom(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str,
    new_device: Any = None,
    ) -> str:
        rooms = data.get("rooms", {}).values()
        _, room = _find(rooms, room_id)
        if not room:
            payload = {"error": f"room '{room_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        # check if the device is present
        if not _find(data.get("devices", {}).values(), device_id)[1]:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        if device_id in room.get("devices", []):
            payload = {"warning": "device already in room"}
            out = json.dumps(payload, indent=2)
            return out
        room.setdefault("devices", []).append(device_id)
        payload = {"success": f"device '{device_id}' added to room '{room_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDeviceToRoom",
                "description": "Associate an existing device with a room (physical placement).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room id"},
                        "device_id": {"type": "string", "description": "Device id"},
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }
