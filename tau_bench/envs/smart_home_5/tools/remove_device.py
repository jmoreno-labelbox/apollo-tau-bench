from tau_bench.envs.tool import Tool
import json
from typing import Any

class RemoveDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], devices: list = None, rooms: list = None, device_id: str = None, new_device: Any = None) -> str:
        devices = devices if devices is not None else data.get("devices", [])
        initial_len = len(devices)
        devices[:] = [d for d in devices if d.get("id") != device_id]

        if len(devices) == initial_len:
            payload = {"error": f"Device with ID '{device_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Additionally, eliminate from rooms
        rooms = rooms if rooms is not None else data.get("rooms", [])
        for room in rooms:
            if device_id in room.get("devices", []):
                room["devices"].remove(device_id)
        payload = {"success": f"Device '{device_id}' removed."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveDevice",
                "description": "Remove a device from the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to remove.",
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
