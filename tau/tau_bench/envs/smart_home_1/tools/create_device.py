# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDevice(Tool):
    """Add a completely new device to the system."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        id: str,
        type: str,
        location: str,
        state_params: List[str],
        state: Dict[str, Any],
        name: str = None,
        **extra_fields: Any,
    ) -> str:
        devices: List[Dict[str, Any]] = list(data.get("devices", {}).values())
        if any(d.get("id") == id for d in devices):
            return json.dumps({"error": "Duplicate device id"}, indent=2)
        device_obj: Dict[str, Any] = {
            "id": id,
            "type": type,
            "name": name,
            "location": location,
            "state_params": state_params,
            "state": state,
            **extra_fields,
            "scheduled_updates": [],
        }
        devices.append(device_obj)
        return json.dumps({"success": True, "device_id": id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_device",
                "description": "Add a completely new device to devices.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Unique id."},
                        "type": {"type": "string", "description": "Device type."},
                        "name": {"type": "string", "description": "Human‑readable name."},
                        "location": {"type": "string", "description": "Room name/location."},
                        "vendor": {"type": "string", "description": "Vendor name."},
                        "model": {"type": "string", "description": "Model name."},
                        "firmware_version": {"type": "string", "description": "Firmware version."},
                        "state_params": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "state": {"type": "object", "description": "Key/value pairs of state to set."},
                    },
                    "required": ["id", "type", "location", "state_params", "state"],
                    "additionalProperties": True,
                },
            },
        }
