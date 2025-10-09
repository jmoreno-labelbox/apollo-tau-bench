from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateDeviceState(Tool):
    """Replace one or more changeable state fields for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        update: dict[str, Any]
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                dev.setdefault("state", {}).update(update)
                dev["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "device_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        #attempt to check sensors if devices are not found
        sensors: list[dict[str, Any]] = data.get("sensors", [])
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                sensor.setdefault("state", {}).update(update)
                sensor["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "sensor_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                dev.setdefault("state", {}).update(update)
                dev["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "device_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        #attempt to check sensors if devices are not found
        sensors: list[dict[str, Any]] = data.get("sensors", [])
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                sensor.setdefault("state", {}).update(update)
                sensor["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "sensor_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDeviceState",
                "description": "Overwrite one or more mutable state fields for a device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Target device/sensor id.",
                        },
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
