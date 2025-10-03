from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], device_id: str, rooms: list[dict[str, Any]] = None) -> str:
        devices = _load("devices", data)
        idx, _ = _find(devices, device_id)
        if idx is None:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        removed = devices.pop(idx)
        # remove from rooms
        for room in (rooms or []):
            if device_id in room.get("devices", []):
                room["devices"].remove(device_id)
        payload = {"success": "device deleted", "device": removed}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteDevice",
                "description": "Remove a device from the home. If present in any room, it will be detached as well.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "ID of device to delete",
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
