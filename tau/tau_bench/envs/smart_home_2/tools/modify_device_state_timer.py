# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find, _now_iso
from .modify_device_state import ModifyDeviceState


class ModifyDeviceStateTimer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, schedule_end: str, update: Dict[str, Any], schedule_at: Optional[str] = None,  rrule: Optional[str] = None, timestamp: Optional[str] = None) -> str:

        devices = list(data.get("devices", {}).values())
        idx, device = _find(devices, device_id)
        if not schedule_end:
            return json.dumps({"error": f"end time is required"}, indent=2)
        if not device:
            return json.dumps({"error": f"device '{device_id}' not found"}, indent=2)
        allowed = set(device.get("state_params", []))
        if any(k not in allowed for k in update):
            return json.dumps({"error": "one or more params not allowed for this device"}, indent=2)

        if schedule_at:
            device.setdefault("scheduled_updates", []).append({
                "timestamp": schedule_at,
                "update": update,
                **({"rrule": rrule} if rrule else {})
            })
            ModifyDeviceState.invoke(data, device_id, {"power": "off"}, schedule_end, rrule, timestamp)
            return json.dumps({"success": "scheduled", "scheduled_update": device["scheduled_updates"][-1]}, indent=2)
        else:
            device_state = device.get("state", {})
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            ModifyDeviceState.invoke(data, device_id, {"power": "off"}, schedule_end, rrule, timestamp)
            return json.dumps({"success": "state updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_device_state_timer",
                "description": "Update the live state of a device, or schedule a future state change, then schedule the device to power off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device id"},
                        "schedule_end": {
                            "type": "string",
                            "description": "ISO8601 timestamp for when to apply the power off"
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp for when to apply the update"
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Optional recurrence rule (RFC5545) if schedule_at is provided"
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Override the 'last_updated' timestamp when updating immediately"
                        }
                    },
                    "required": ["device_id", "update", "schedule_end"],
                    "additionalProperties": False
                }
            }
        }
