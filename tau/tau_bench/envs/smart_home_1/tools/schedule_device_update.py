from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ScheduleDeviceUpdate(Tool):
    """Insert or substitute a forthcoming scheduled update for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        timestamp: str,
        update: dict[str, Any],
        replace: bool = False,
        rrule: str | None = None
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices:
            if dev.get("id") == device_id:
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched.values() if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                sched.sort(key=lambda x: x["timestamp"])  # maintain chronological order
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices:
            if dev.get("id") == device_id:
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched.values() if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                sched.sort(key=lambda x: x["timestamp"])  #maintain chronological order
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
                "name": "ScheduleDeviceUpdate",
                "description": "Add or replace a future scheduled update for a device.",
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
