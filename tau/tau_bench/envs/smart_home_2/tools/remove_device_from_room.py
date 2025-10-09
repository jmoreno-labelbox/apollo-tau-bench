from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RemoveDeviceFromRoom(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str) -> str:
        _, room = _find(data.get("rooms", []), room_id)
        if not room:
            payload = {"error": f"room '{room_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        if device_id not in room.get("devices", []):
            payload = {"error": f"device '{device_id}' not in room"}
            out = json.dumps(payload, indent=2)
            return out
        room["devices"].remove(device_id)
        payload = {"success": f"device '{device_id}' removed from room '{room_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeDeviceFromRoom",
                "description": "Detach a device from a room without deleting the device itself.",
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
