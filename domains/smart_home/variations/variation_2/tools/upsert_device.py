from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], device: dict[str, Any]) -> str:
        if not device or not isinstance(device, dict):
            payload = {"error": "device object required"}
            out = json.dumps(payload, indent=2)
            return out
        devices = _load("devices", data)
        idx, _old = _find(devices, device["id"])
        if idx is not None:
            devices[idx].update(device)
            action = "updated"
        else:
            devices.append(device)
            action = "added"
            data["devices"] = devices
        payload = {"success": f"device {action}", "device": device}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertDevice",
                "description": "Create a new device or update an existing one (metadata only; state changes use modify_device_state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "UpsertScene": {
                            "type": "object",
                            "description": "Full or partial device object following the schema in devices.json.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False,
                },
            },
        }
