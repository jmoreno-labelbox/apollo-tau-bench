from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RoomManager(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = "get", room_id: str = None, device_id: str = None, floor: str = None) -> str:
        rooms = data.get("rooms", [])

        if action == "get":
            result = [
                r
                for r in rooms
                if (not room_id or r["id"] == room_id)
                and (not floor or r["floor"] == floor)
            ]
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "add_device":
            if not room_id or not device_id:
                payload = {"error": "room_id and device_id required"}
                out = json.dumps(payload, indent=2)
                return out
            for room in rooms:
                if room["id"] == room_id:
                    if device_id not in room["devices"]:
                        room["devices"].append(device_id)
                    payload = {"success": f"Added {device_id} to {room_id}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        elif action == "remove_device":
            if not room_id or not device_id:
                payload = {"error": "room_id and device_id required"}
                out = json.dumps(payload, indent=2)
                return out
            for room in rooms:
                if room["id"] == room_id:
                    if device_id in room["devices"]:
                        room["devices"].remove(device_id)
                    payload = {"success": f"Removed {device_id} from {room_id}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RoomManager",
                "description": "Manage rooms and device assignments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["get", "add_device", "remove_device"],
                        },
                        "room_id": {"type": "string", "description": "Room ID"},
                        "device_id": {
                            "type": "string",
                            "description": "Device ID to add/remove",
                        },
                        "floor": {
                            "type": "integer",
                            "description": "Filter by floor number",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
