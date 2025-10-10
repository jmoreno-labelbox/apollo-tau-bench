# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices = list(data.get('devices', {}).values())
        initial_len = len(devices)
        devices[:] = [d for d in devices if d.get('id') != device_id]

        if len(devices) == initial_len:
            return json.dumps({"error": f"Device with ID '{device_id}' not found."}, indent=2)

        # Additionally, eliminate from rooms.
        rooms = data.get('rooms', [])
        for room in rooms:
            if device_id in room.get('devices', []):
                room['devices'].remove(device_id)

        return json.dumps({"success": f"Device '{device_id}' removed."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_device",
                "description": "Remove a device from the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to remove."
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False
                }
            }
        }
