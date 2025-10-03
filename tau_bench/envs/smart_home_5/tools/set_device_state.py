from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetDeviceState(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], device_id: str, state_update: dict[str, Any]
    ) -> str:
        devices = data.get("devices", [])
        device_found = False
        for device in devices:
            if device.get("id") == device_id:
                device_found = True
                device["state"].update(state_update)
                device["state"]["last_updated"] = _now_iso()
                break

        if not device_found:
            # attempt to use sensors if devices are not available
            sensors = data.get("sensors", [])
            sensor_found = False
            for sensor in sensors:
                if sensor.get("id") == device_id:
                    sensor["state"].update(state_update)
                    sensor["state"]["last_updated"] = _now_iso()
                    sensor_found = True
                    break
            if not sensor_found:
                payload = {"error": f"Device/sensor with ID '{device_id}' not found."}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"success": f"State for device/sensor '{device_id}' updated."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetDeviceState",
                "description": "Set the state of a specific device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device/sensor to update.",
                        },
                        "state_update": {
                            "type": "object",
                            "description": 'A dictionary of state parameters to update (e.g., {"power": "on", "brightness": 80}).',
                            "additionalProperties": True,
                        },
                    },
                    "required": ["device_id", "state_update"],
                    "additionalProperties": False,
                },
            },
        }
