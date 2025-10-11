# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find






def _find(collection: List[Dict[str, Any]], entity_id: str):
    for idx, item in enumerate(collection):
        if item.get("id") == entity_id or item.get("reminder_id") == entity_id \
           or item.get("list_id") == entity_id or item.get("member_id") == entity_id:
            return idx, item
    return None, None

class ModifyDeviceState(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, update: Dict[str, Any], schedule_at: Optional[str] = None, rrule: Optional[str] = None, timestamp: Optional[str] = None) -> str:

        devices = data.get("devices", [])
        idx, device = _find(devices, device_id)
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
            return json.dumps({"success": "scheduled", "scheduled_update": device["scheduled_updates"][-1]}, indent=2)
        else:
            device_state = device.get("state", {})
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            return json.dumps({"success": "state updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_device_state",
                "description": "Update the live state of a device, or schedule a future state change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device id"},
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
                    "required": ["device_id", "update"],
                    "additionalProperties": False
                }
            }
        }

class RunScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        _, scene = _find(list(data.get("scenes", {}).values()), scene_id)
        if not scene:
            return json.dumps({"error": f"scene '{scene_id}' not found"}, indent=2)
        results = []
        for act in scene.get("actions", []):
            res = ModifyDeviceState.invoke(data, device_id=act["device_id"], update=act["update"])
            results.append(json.loads(res))
        return json.dumps({"success": f"scene '{scene_id}' executed", "results": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_scene",
                "description": "Execute the actions of a scene immediately.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene id to run"}
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }