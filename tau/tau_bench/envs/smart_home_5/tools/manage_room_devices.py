from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ManageRoomDevices(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str, action: str) -> str:
        rooms = data.get("rooms", [])
        room_found = False
        for room in rooms:
            if room.get("id") == room_id:
                room_found = True
                if action == "add":
                    if device_id not in room.get("devices", []):
                        room.setdefault("devices", []).append(device_id)
                        payload = {
                            "success": f"Device '{device_id}' added to room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    else:
                        payload = {
                            "error": f"Device '{device_id}' already in room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                elif action == "remove":
                    if device_id in room.get("devices", []):
                        room["devices"].remove(device_id)
                        payload = {
                            "success": f"Device '{device_id}' removed from room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    else:
                        payload = {
                            "error": f"Device '{device_id}' not found in room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                else:
                    payload = {"error": "Invalid action. Use 'add' or 'remove'."}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out

        if not room_found:
            payload = {"error": f"Room with ID '{room_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": "An unexpected error occurred."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageRoomDevices",
                "description": "Add or remove a device from a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "The ID of the room to modify.",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to add or remove.",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform.",
                        },
                    },
                    "required": ["room_id", "device_id", "action"],
                    "additionalProperties": False,
                },
            },
        }
