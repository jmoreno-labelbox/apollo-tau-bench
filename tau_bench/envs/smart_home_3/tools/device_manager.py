from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeviceManager(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        device_id: str = None,
        type: str = None,
        location: str = None,
        state_updates: dict = {},
        updates: dict = None,
        schedule_updates: dict = None,
        device_data: dict = {}) -> str:
        devices = data.get("devices", [])

        if action == "get":
            result = [
                d
                for d in devices
                if (not device_id or d["id"] == device_id)
                and (not type or d["type"] == type)
                and (not location or d["location"] == location)
            ]
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "update_state":
            if not device_id:
                payload = {"error": "device_id required for state update"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            # Use updates if provided, otherwise fall back to state_updates
            actual_updates = updates if updates is not None else state_updates
            for device in devices:
                if device["id"] == device_id:
                    device["state"].update(actual_updates)
                    device["state"]["last_updated"] = _now_iso()
                    payload = {"success": f"Updated {device_id} state"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        elif action == "add_schedule":
            if not device_id or not schedule_updates:
                payload = {"error": "device_id and schedule_updates required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            for device in devices:
                if device["id"] == device_id:
                    device["scheduled_updates"].append(schedule_updates)
                    payload = {"success": f"Added schedule to {device_id}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        elif action == "create":
            if not device_data:
                payload = {"error": "device_data required for creation"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            devices.append(device_data)
            payload = {"success": f"Created device {device_data.get('id')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        elif action == "delete":
            if not device_id:
                payload = {"error": "device_id required for deletion"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            devices[:] = [d for d in devices if d["id"] != device_id]
            payload = {"success": f"Deleted device {device_id}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeviceManager",
                "description": "Comprehensive device management - CRUD, state updates, scheduling",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "get",
                                "update_state",
                                "add_schedule",
                                "create",
                                "delete",
                            ],
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device ID for operations",
                        },
                        "type": {
                            "type": "string",
                            "description": "Filter by device type",
                        },
                        "location": {
                            "type": "string",
                            "description": "Filter by location",
                        },
                        "state_updates": {
                            "type": "object",
                            "description": "State parameters to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Alias for state_updates",
                        },
                        "schedule_updates": {
                            "type": "object",
                            "description": "Schedule data to add (Dict with fields timestamp (String), update (Dict), rrule (String))",
                        },
                        "device_data": {
                            "type": "object",
                            "description": "Full device data for creation",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
