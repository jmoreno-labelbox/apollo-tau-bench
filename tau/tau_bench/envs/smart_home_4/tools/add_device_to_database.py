# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddDeviceToDatabase(Tool):
    """Add a new device."""
    @staticmethod
    def invoke(data: Dict[str, Any], device: Optional[Dict[str, Any]] = None) -> str:
        if not device:
            return json.dumps({"error": "'device' parameter is required"}, indent=2)
        device_list = list(data.get('devices', {}).values())
        if any(d["id"] == device.get("id") for d in device_list):
            return json.dumps({"error": "Device with this id already exists"}, indent=2)
        device_list.append(device)
        return json.dumps({"success": "Device added", "device": device, "devices": device_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device_to_database",
                "description": "Add a new device. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device": {
                            "type": "object",
                            "description": "The full device object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False
                }
            }
        }
