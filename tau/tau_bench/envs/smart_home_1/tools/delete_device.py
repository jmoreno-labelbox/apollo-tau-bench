# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteDevice(Tool):
    """Remove a device from inventory and all rooms."""

    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices: List[Dict[str, Any]] = list(data.get("devices", {}).values())
        original_len = len(devices)
        devices[:] = [d for d in devices if d.get("id") != device_id]
        if len(devices) == original_len:
            return json.dumps({"error": "Device not found"}, indent=2)
        # Eliminate from all room mappings.
        rooms_doc: Dict[str, Any] = data.get("rooms", {})
        for room in rooms_doc.get("rooms", []):
            room_devices = room.get("devices", [])
            if device_id in room_devices:
                room["devices"] = [d for d in room_devices if d != device_id]
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_device",
                "description": "Remove a device from inventory and all rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Device identifier."},
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
