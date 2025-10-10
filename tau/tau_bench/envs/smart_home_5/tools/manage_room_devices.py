# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageRoomDevices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str, action: str) -> str:
        rooms = data.get('rooms', [])
        room_found = False
        for room in rooms:
            if room.get('id') == room_id:
                room_found = True
                if action == 'add':
                    if device_id not in room.get('devices', []):
                        room.setdefault('devices', []).append(device_id)
                        return json.dumps({"success": f"Device '{device_id}' added to room '{room_id}'."}, indent=2)
                    else:
                        return json.dumps({"error": f"Device '{device_id}' already in room '{room_id}'."}, indent=2)
                elif action == 'remove':
                    if device_id in room.get('devices', []):
                        room['devices'].remove(device_id)
                        return json.dumps({"success": f"Device '{device_id}' removed from room '{room_id}'."}, indent=2)
                    else:
                        return json.dumps({"error": f"Device '{device_id}' not found in room '{room_id}'."}, indent=2)
                else:
                    return json.dumps({"error": "Invalid action. Use 'add' or 'remove'."}, indent=2)

        if not room_found:
            return json.dumps({"error": f"Room with ID '{room_id}' not found."}, indent=2)
        return json.dumps({"error": "An unexpected error occurred."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_room_devices",
                "description": "Add or remove a device from a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "The ID of the room to modify."
                        },
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to add or remove."
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform."
                        }
                    },
                    "required": ["room_id", "device_id", "action"],
                    "additionalProperties": False
                }
            }
        }
