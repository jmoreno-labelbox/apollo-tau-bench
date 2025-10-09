from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteDevice(Tool):
    """Eliminate a device from inventory and all associated rooms."""

    @staticmethod
    def invoke(data: dict[str, Any], device_id: str) -> str:
        devices = data.get("devices", [])
        rooms = data.get("rooms", {})
        original_len = len(devices)
        devices[:] = [d for d in devices if d.get("id") != device_id]
        if len(devices) == original_len:
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        
        # Update the data with the modified devices list
        data["devices"] = devices
        
        # Detach from any room associations
        for room in rooms.get("rooms", []):
            room_devices = room.get("devices", [])
            if device_id in room_devices:
                room["devices"] = [d for d in room_devices if d != device_id]
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteDevice",
                "description": "Remove a device from inventory and all rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
