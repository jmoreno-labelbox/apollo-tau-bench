from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ManageRoomInDatabase(Tool):
    """Consolidated CRUD for rooms: retrieve and modify device assignments/settings, but cannot add or remove rooms."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        room_id: str = "",
        device_id: str = "",
        device_settings: dict[str, Any] | None = None,
        filters: dict[str, Any] | None = None
    ) -> str:
        rooms = data.get("rooms", {}).values()
        if action == "get":
            if room_id:
                result = [r for r in rooms.values() if r.get("id") == room_id]
            elif filters:
                result = [
                    r for r in rooms.values() if all(r.get(k) == v for k, v in filters.items())
                ]
            else:
                result = rooms
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "AddDeviceToDatabase":
            if not room_id or not device_id:
                payload = {"error": "'room_id' and 'device_id' are required for add_device"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id not in r["devices"]:
                        r["devices"].append(device_id)
                    found = True
                    break
            if not found:
                payload = {"error": "Room not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Device added to room",
                    "room_id": room_id,
                    "device_id": device_id,
                    "rooms": rooms,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "remove_device":
            if not room_id or not device_id:
                payload = {
                        "error": "'room_id' and 'device_id' are required for remove_device"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        r["devices"].remove(device_id)
                    found = True
                    break
            if not found:
                payload = {"error": "Room not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Device removed from room",
                    "room_id": room_id,
                    "device_id": device_id,
                    "rooms": rooms,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "update_device_settings":
            if not room_id or not device_id or not device_settings:
                payload = {
                        "error": "'room_id', 'device_id', and 'device_settings' are required for update_device_settings"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        # This serves as a placeholder; real device configurations for each room will require a schema
                        if "device_settings" not in r:
                            r["device_settings"] = {}
                        r["device_settings"][device_id] = device_settings
                        found = True
                        break
            if not found:
                payload = {"error": "Room or device not found in room"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            payload = {
                    "success": "Device settings updated in room",
                    "room_id": room_id,
                    "device_id": device_id,
                    "device_settings": device_settings,
                    "rooms": rooms,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": f"Unknown action: {action}"}
            out = json.dumps(payload, indent=2)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageRoomInDatabase",
                "description": "Get room info, add/remove device to/from room, or update device-specific settings in a room. Cannot add/remove rooms themselves.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add_device, remove_device, update_device_settings",
                        },
                        "room_id": {
                            "type": "string",
                            "description": "Room id to operate on (required for all actions except get with filters)",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device id to add/remove/update in the room (required for add_device, remove_device, update_device_settings)",
                        },
                        "device_settings": {
                            "type": "object",
                            "description": "Settings to update for the device in the room (required for update_device_settings)",
                            "additionalProperties": True,
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter rooms (optional for get)",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
