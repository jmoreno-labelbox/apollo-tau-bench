# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
        devices: List[Dict[str, Any]] = list(data.get("devices", {}).values())
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
