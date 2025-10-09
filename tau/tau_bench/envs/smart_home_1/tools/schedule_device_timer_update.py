from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ScheduleDeviceTimerUpdate(Tool):
    """Insert or substitute a forthcoming scheduled update for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        timestamp: str,
        timestamp_end: str,
        update: dict[str, Any],
        replace: bool = False,
        rrule: str | None = None
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                if timestamp_end is None:
                    payload = {"error": "End time is needed"}
                    out = json.dumps(payload, indent=2)
                    return out

                # Configure Device as required
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, replace, rrule
                )
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                if timestamp_end == None:
                    payload = {"error": "End time is needed"}
                    out = json.dumps(payload, indent=2)
                    return out

                #Configure Device as required
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, replace, rrule
                )
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(
                    payload, indent=2
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
                "name": "ScheduleDeviceUpdateTimer",
                "description": "Add or replace a future scheduled update for a device that only bee on for a time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp in device local tz.",
                        },
                        "timestamp_end": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp to turn off the device in device local tz.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Partial state to apply at timestamp.",
                        },
                        "replace": {
                            "type": "boolean",
                            "description": "If true, replace any existing entry at that timestamp.",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Recurrence rule for the scheduled update [FREQ=DAILY, FREQ=WEEKLY, FREQ=MONTHLY, FREQ=YEARLY]; \
                                will repeat at the same time of day as the timestamp.",
                        },
                    },
                    "required": ["device_id", "timestamp", "timestamp_end", "update"],
                    "additionalProperties": False,
                },
            },
        }
