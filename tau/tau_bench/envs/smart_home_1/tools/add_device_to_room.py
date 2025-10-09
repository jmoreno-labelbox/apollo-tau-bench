from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddDeviceToRoom(Tool):
    """Link an existing device to a room."""

    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str,
    new_device: Any = None,
    ) -> str:
        rooms_doc: list[dict[str, Any]] = data.get("rooms", [])
        target_room = next(
            (room for room in rooms_doc if room["id"] == room_id),
            None,
        )
        if not target_room:
            payload = {"error": "Room not found"}
            out = json.dumps(payload, indent=2)
            return out
        if device_id in target_room.get("devices", []):
            payload = {"error": "Device already assigned"}
            out = json.dumps(payload, indent=2)
            return out
        target_room.setdefault("devices", []).append(device_id)
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDeviceToRoom",
                "description": "Associate an existing device with a room.",
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
