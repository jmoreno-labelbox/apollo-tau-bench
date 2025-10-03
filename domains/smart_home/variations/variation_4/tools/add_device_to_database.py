from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddDeviceToDatabase(Tool):
    """Introduce a new device."""

    @staticmethod
    def invoke(data: dict[str, Any], device: dict[str, Any] | None = None,
    new_device: Any = None,
    ) -> str:
        if not device:
            payload = {"error": "'device' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        device_list = data.get("devices", [])
        if any(d["id"] == device.get("id") for d in device_list):
            payload = {"error": "Device with this id already exists"}
            out = json.dumps(payload, indent=2)
            return out
        device_list.append(device)
        payload = {"success": "Device added", "device": device, "devices": device_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDeviceToDatabase",
                "description": "Add a new device. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device": {
                            "type": "object",
                            "description": "The full device object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False,
                },
            },
        }
