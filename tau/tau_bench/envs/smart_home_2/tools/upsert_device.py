# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device: Dict[str, Any]) -> str:
        if not device or not isinstance(device, dict):
            return json.dumps({"error": "device object required"}, indent=2)
        devices = _load("devices", data)
        idx, _old = _find(devices, device["id"])
        if idx is not None:
            devices[idx].update(device)
            action = "updated"
        else:
            devices.append(device)
            action = "added"
            data["devices"] = devices
        return json.dumps({"success": f"device {action}", "device": device}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_device",
                "description": "Create a new device or update an existing one (metadata only; state changes use modify_device_state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "upsert_scene": {
                            "type": "object",
                            "description": "Full or partial device object following the schema in devices.json.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False
                }
            }
        }
