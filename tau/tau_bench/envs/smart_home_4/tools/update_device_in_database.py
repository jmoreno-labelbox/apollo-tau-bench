# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDeviceInDatabase(Tool):
    """Update any field of a device."""
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not device_id or not updates:
            return json.dumps({"error": "'device_id' and 'updates' parameters are required"}, indent=2)
        device_list = list(data.get('devices', {}).values())
        found = False
        for d in device_list:
            if d["id"] == device_id:
                for k, v in updates.items():
                    if k in d:
                        d[k] = v
                    elif k in d.get("state", {}):
                        d["state"][k] = v
                    else:
                        d[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Device not found"}, indent=2)
        return json.dumps({"success": "Device updated", "device_id": device_id, "updates": updates, "devices": device_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_device_in_database",
                "description": "Update any field of a device by id. Updates can be for top-level or nested fields (e.g., state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update. For nested fields like state, use the field name directly.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device_id", "updates"],
                    "additionalProperties": False
                }
            }
        }
