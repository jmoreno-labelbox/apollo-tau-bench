# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageRoomInDatabase(Tool):
    """Unified CRUD for rooms: get, update device assignments/settings, but not add/remove rooms."""
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        action: str = "get",
        room_id: str = "",
        device_id: str = "",
        device_settings: Optional[Dict[str, Any]] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> str:
        rooms = data.get('rooms', [])
        if action == "get":
            if room_id:
                result = [r for r in rooms if r.get("id") == room_id]
            elif filters:
                result = [r for r in rooms if all(r.get(k) == v for k, v in filters.items())]
            else:
                result = rooms
            return json.dumps(result, indent=2)
        elif action == "add_device_to_database":
            if not room_id or not device_id:
                return json.dumps({"error": "'room_id' and 'device_id' are required for add_device"}, indent=2)
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id not in r["devices"]:
                        r["devices"].append(device_id)
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Room not found"}, indent=2)
            return json.dumps({"success": "Device added to room", "room_id": room_id, "device_id": device_id, "rooms": rooms}, indent=2)
        elif action == "remove_device":
            if not room_id or not device_id:
                return json.dumps({"error": "'room_id' and 'device_id' are required for remove_device"}, indent=2)
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        r["devices"].remove(device_id)
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Room not found"}, indent=2)
            return json.dumps({"success": "Device removed from room", "room_id": room_id, "device_id": device_id, "rooms": rooms}, indent=2)
        elif action == "update_device_settings":
            if not room_id or not device_id or not device_settings:
                return json.dumps({"error": "'room_id', 'device_id', and 'device_settings' are required for update_device_settings"}, indent=2)
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        # This is a placeholder; actual device settings per room would need a schema
                        if "device_settings" not in r:
                            r["device_settings"] = {}
                        r["device_settings"][device_id] = device_settings
                        found = True
                        break
            if not found:
                return json.dumps({"error": "Room or device not found in room"}, indent=2)
            return json.dumps({"success": "Device settings updated in room", "room_id": room_id, "device_id": device_id, "device_settings": device_settings, "rooms": rooms}, indent=2)
        else:
            return json.dumps({"error": f"Unknown action: {action}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_room_in_database",
                "description": "Get room info, add/remove device to/from room, or update device-specific settings in a room. Cannot add/remove rooms themselves.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add_device, remove_device, update_device_settings"
                        },
                        "room_id": {
                            "type": "string",
                            "description": "Room id to operate on (required for all actions except get with filters)"
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device id to add/remove/update in the room (required for add_device, remove_device, update_device_settings)"
                        },
                        "device_settings": {
                            "type": "object",
                            "description": "Settings to update for the device in the room (required for update_device_settings)",
                            "additionalProperties": True
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter rooms (optional for get)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
