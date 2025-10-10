# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_device: Dict[str, Any]) -> str:
        devices = list(data.get('devices', {}).values())
        if 'id' not in new_device:
            return json.dumps({"error": "New device must have an 'id'."}, indent=2)

        if any(d.get('id') == new_device['id'] for d in devices):
            return json.dumps({"error": f"Device with ID '{new_device['id']}' already exists."}, indent=2)

        devices.append(new_device)
        return json.dumps({"success": f"Device '{new_device.get('name', new_device['id'])}' added."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device",
                "description": "Add a new device to the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_device": {
                            "type": "object",
                            "description": "A dictionary representing the new device.",
                            "properties": {
                                "id": {"type": "string"},
                                "type": {"type": "string"},
                                "name": {"type": "string"},
                                "location": {"type": "string"}
                            },
                            "required": ["id", "type", "name"],
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_device"],
                    "additionalProperties": False
                }
            }
        }
