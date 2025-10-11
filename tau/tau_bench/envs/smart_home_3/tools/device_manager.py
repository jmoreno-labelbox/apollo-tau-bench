# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    # return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"

class DeviceManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id, location, schedule_updates, type, action = 'get', device_data = {}, state_updates = {}) -> str:
        devices = list(data.get('devices', {}).values())
        device_type = type

        if action == 'get':
            result = [d for d in devices if (not device_id or d['id'] == device_id) and
                     (not device_type or d['type'] == device_type) and
                     (not location or d['location'] == location)]
            return json.dumps(result, indent=2)
        elif action == 'update_state':
            if not device_id:
                return json.dumps({"error": "device_id required for state update"}, indent=2)
            for device in devices:
                if device['id'] == device_id:
                    device['state'].update(state_updates)
                    device['state']['last_updated'] = _now_iso()
                    return json.dumps({"success": f"Updated {device_id} state"}, indent=2)
            return json.dumps({"error": "Device not found"}, indent=2)
        elif action == 'add_schedule':
            if not device_id or not schedule_updates:
                return json.dumps({"error": "device_id and schedule_updates required"}, indent=2)
            for device in devices:
                if device['id'] == device_id:
                    device['scheduled_updates'].append(schedule_updates)
                    return json.dumps({"success": f"Added schedule to {device_id}"}, indent=2)
        elif action == 'create':
            if not device_data:
                return json.dumps({"error": "device_data required for creation"}, indent=2)
            devices.append(device_data)
            return json.dumps({"success": f"Created device {device_data.get('id')}"}, indent=2)
        elif action == 'delete':
            if not device_id:
                return json.dumps({"error": "device_id required for deletion"}, indent=2)
            devices[:] = [d for d in devices if d['id'] != device_id]
            return json.dumps({"success": f"Deleted device {device_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "device_manager",
                "description": "Comprehensive device management - CRUD, state updates, scheduling",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "update_state", "add_schedule", "create", "delete"]},
                        "device_id": {"type": "string", "description": "Device ID for operations"},
                        "type": {"type": "string", "description": "Filter by device type"},
                        "location": {"type": "string", "description": "Filter by location"},
                        "state_updates": {"type": "object", "description": "State parameters to update"},
                        "schedule_updates": {"type": "object", "description": "Schedule data to add (Dict with fields timestamp (String), update (Dict), rrule (String))"},
                        "device_data": {"type": "object", "description": "Full device data for creation"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }