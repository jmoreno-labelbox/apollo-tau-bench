# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteDeviceFromDatabase(Tool):
    """Remove a device by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str = "") -> str:
        if not device_id:
            return json.dumps({"error": "'device_id' parameter is required"}, indent=2)
        device_list = list(data.get('devices', {}).values())
        new_list = [d for d in device_list if d["id"] != device_id]
        if len(new_list) == len(device_list):
            return json.dumps({"error": "Device not found"}, indent=2)
        return json.dumps({"success": "Device deleted", "device_id": device_id, "devices": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_device_from_database",
                "description": "Remove a device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to delete."
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False
                }
            }
        }
