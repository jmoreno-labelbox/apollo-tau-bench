# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RoomManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id, floor, room_id, action = 'get') -> str:
        rooms = list(data.get('rooms', {}).values())

        if action == 'get':
            result = [r for r in rooms if (not room_id or r['id'] == room_id) and
                     (not floor or r['floor'] == floor)]
            return json.dumps(result, indent=2)
        elif action == 'add_device':
            if not room_id or not device_id:
                return json.dumps({"error": "room_id and device_id required"}, indent=2)
            for room in rooms:
                if room['id'] == room_id:
                    if device_id not in room['devices']:
                        room['devices'].append(device_id)
                    return json.dumps({"success": f"Added {device_id} to {room_id}"}, indent=2)
        elif action == 'remove_device':
            if not room_id or not device_id:
                return json.dumps({"error": "room_id and device_id required"}, indent=2)
            for room in rooms:
                if room['id'] == room_id:
                    if device_id in room['devices']:
                        room['devices'].remove(device_id)
                    return json.dumps({"success": f"Removed {device_id} from {room_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "room_manager",
                "description": "Manage rooms and device assignments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "add_device", "remove_device"]},
                        "room_id": {"type": "string", "description": "Room ID"},
                        "device_id": {"type": "string", "description": "Device ID to add/remove"},
                        "floor": {"type": "integer", "description": "Filter by floor number"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
