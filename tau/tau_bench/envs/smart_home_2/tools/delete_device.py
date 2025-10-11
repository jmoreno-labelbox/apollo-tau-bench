# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find






def _load(entity: str, data: Dict[str, Any]):
    """Return a *mutable copy* of a top-level collection list."""
    return [*data.get(entity, [])]

def _find(collection: List[Dict[str, Any]], entity_id: str):
    for idx, item in enumerate(collection):
        if item.get("id") == entity_id or item.get("reminder_id") == entity_id \
           or item.get("list_id") == entity_id or item.get("member_id") == entity_id:
            return idx, item
    return None, None

class DeleteDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices = _load("devices", data)
        idx, _ = _find(devices, device_id)
        if idx is None:
            return json.dumps({"error": f"device '{device_id}' not found"}, indent=2)
        removed = devices.pop(idx)
        # remove from rooms
        for room in data.get("rooms", []):
            if device_id in room.get("devices", []):
                room["devices"].remove(device_id)
        return json.dumps({"success": "device deleted", "device": removed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_device",
                "description": "Remove a device from the home. If present in any room, it will be detached as well.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "ID of device to delete"}
                    },
                    "required": ["device_id"],
                    "additionalProperties": False
                }
            }
        }