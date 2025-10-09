from tau_bench.envs.tool import Tool
import json
from typing import Any

class ModifyDeviceStateTimer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        schedule_end: str,
        update: dict[str, Any],
        schedule_at: str | None = None,
        rrule: str | None = None,
        timestamp: str | None = None,
    ) -> str:
        devices = data.get("devices", [])
        idx, device = _find(devices, device_id)
        if not schedule_end:
            payload = {"error": "end time is required"}
            out = json.dumps(payload, indent=2)
            return out
        if not device:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        allowed = set(device.get("state_params", []))
        if any(k not in allowed for k in update):
            payload = {"error": "one or more params not allowed for this device"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if schedule_at:
            device.setdefault("scheduled_updates", []).append(
                {
                    "timestamp": schedule_at,
                    "update": update,
                    **({"rrule": rrule} if rrule else {}),
                }
            )
            ModifyDeviceState.invoke(
                data, device_id, {"power": "off"}, schedule_end, rrule, timestamp
            )
            payload = {
                    "success": "scheduled",
                    "scheduled_update": device["scheduled_updates"][-1],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            device_state = device.get("state", {})
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            ModifyDeviceState.invoke(
                data, device_id, {"power": "off"}, schedule_end, rrule, timestamp
            )
            payload = {"success": "state updated"}
            out = json.dumps(payload, indent=2)
            return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyDeviceStateTimer",
                "description": "Update the live state of a device, or schedule a future state change, then schedule the device to power off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Target device id",
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "ISO8601 timestamp for when to apply the power off",
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True,
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp for when to apply the update",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Optional recurrence rule (RFC5545) if schedule_at is provided",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Override the 'last_updated' timestamp when updating immediately",
                        },
                    },
                    "required": ["device_id", "update", "schedule_end"],
                    "additionalProperties": False,
                },
            },
        }
