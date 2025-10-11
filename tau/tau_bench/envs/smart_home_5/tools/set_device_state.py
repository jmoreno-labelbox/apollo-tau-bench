# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _now_iso




def _now_iso() -> str:
    # return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"

class SetDeviceState(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, update: Dict[str, Any]) -> str:
        devices = list(data.get('devices', {}).values())
        device_found = False
        for device in devices:
            if device.get('id') == device_id:
                device_found = True
                device['state'].update(update)
                device['state']['last_updated'] = _now_iso()
                break

        if not device_found:
            # check sensors if devices are unavailable
            sensors = data.get('sensors', [])
            sensor_found = False
            for sensor in sensors:
                if sensor.get('id') == device_id:
                    sensor['state'].update(update)
                    sensor['state']['last_updated'] = _now_iso()
                    sensor_found = True
                    break
            if not sensor_found:
                return json.dumps({"error": f"Device/sensor with ID '{device_id}' not found."}, indent=2)

        return json.dumps({"success": f"State for device/sensor '{device_id}' updated."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_device_state",
                "description": "Set the state of a specific device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device/sensor to update."
                        },
                        "update": {
                            "type": "object",
                            "description": "A dictionary of state parameters to update (e.g., {\"power\": \"on\", \"brightness\": 80}).",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False
                }
            }
        }