# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDeviceState(Tool):
    """Overwrite one or more mutable state fields for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        update: Dict[str, Any],
    ) -> str:
        devices: List[Dict[str, Any]] = list(data.get("devices", {}).values())
        for dev in devices:
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                dev.setdefault("state", {}).update(update)
                dev["state"]["last_updated"] = _now_iso()
                return json.dumps(
                    {"success": True, "device_id": device_id},
                    indent=2,
                )
        # attempt sensors if devices are absent
        sensors: List[Dict[str, Any]] = list(data.get("sensors", {}).values())
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                sensor.setdefault("state", {}).update(update)
                sensor["state"]["last_updated"] = _now_iso()
                return json.dumps(
                    {"success": True, "sensor_id": device_id},
                    indent=2,
                )
        return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_device_state",
                "description": "Overwrite one or more mutable state fields for a device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device/sensor id."},
                        "update": {
                            "type": "object",
                            "description": "Key/value pairs of state to set.",
                        },
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False,
                },
            },
        }
