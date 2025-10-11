# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _now_iso() -> str:
    # return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return "deterministic placeholder for current time"

class ScheduleDeviceUpdate(Tool):
    """Add or replace a future scheduled update for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        timestamp: str,
        update: Dict[str, Any],
        replace: bool = False,
        rrule: Optional[str] = None,
    ) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                sched: List[Dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append({"timestamp": timestamp, "update": update, "rrule": rrule})
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                sched.sort(key=lambda x: x["timestamp"])  # keep chronologically ordered
                return json.dumps({"success": True, "scheduled_updates": sched}, indent=2)
        return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_device_update",
                "description": "Add or replace a future scheduled update for a device.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Device identifier."},
                        "timestamp": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp in device local tz.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Partial state to apply at timestamp.",
                        },
                        "replace": {
                            "type": "boolean",
                            "description": "If true, replace any existing entry with same timestamp or whose recurrence rule causes a conflict.",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Recurrence rule for the scheduled update [FREQ=DAILY, FREQ=WEEKLY, FREQ=MONTHLY, FREQ=YEARLY]; \
                                will repeat at the same time of day as the timestamp.",
                        },
                    },
                    "required": ["device_id", "timestamp", "update"],
                    "additionalProperties": False,
                },
            },
        }

class UpdateDeviceStateTimer(Tool):
    """Overwrite one or more mutable state fields for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        timestamp_end: str,
        update: Dict[str, Any],
        rrule: Optional[str] = None
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
                ScheduleDeviceUpdate.invoke(data, device_id, timestamp_end, {"power": "off"}, None, rrule)
                return json.dumps(
                    {"success": True, "device_id": device_id},
                    indent=2,
                )
        # attempt sensors if devices are unavailable
        sensors: List[Dict[str, Any]] = list(data.get("sensors", {}).values())
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                sensor.setdefault("state", {}).update(update)
                sensor["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(data, device_id, timestamp_end, {"power": "off"}, None, rrule)
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
                "name": "update_device_state_timer",
                "description": "Overwrite one or more mutable state fields for a device/sensor, then turn off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device/sensor id."},
                        "timestamp_end": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp to turn off the device in device local tz.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Key/value pairs of state to set.",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Recurrence rule for the scheduled update [FREQ=DAILY, FREQ=WEEKLY, FREQ=MONTHLY, FREQ=YEARLY]; \
                                will repeat at the same time of day as the timestamp.",
                        },
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False,
                },
            },
        }