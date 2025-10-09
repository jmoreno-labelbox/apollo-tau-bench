from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateDevice(Tool):
    """Introduce a brand new device into the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str,
        type: str,
        location: str,
        state_params: list[str],
        state: dict[str, Any],
        name: str = None,
        vendor: str = None,
        model: str = None,
        firmware_version: str = None,
        scheduled_updates: list = None) -> str:
        pass
        devices: list[dict[str, Any]] = data.get("devices", [])
        if any(d.get("id") == id for d in devices):
            payload = {"error": "Duplicate device id"}
            out = json.dumps(payload, indent=2)
            return out
        device_obj: dict[str, Any] = {
            "id": id,
            "type": type,
            "name": name,
            "location": location,
            "state_params": state_params,
            "state": state,
            "scheduled_updates": scheduled_updates or [],
        }
        devices.append(device_obj)
        payload = {"success": True, "device_id": id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", [])
        if any(d.get("id") == id for d in devices):
            payload = {"error": "Duplicate device id"}
            out = json.dumps(payload, indent=2)
            return out
        device_obj: dict[str, Any] = {
            "id": id,
            "type": type,
            "name": name,
            "location": location,
            "state_params": state_params,
            "state": state,
            **extra_fields,
            "scheduled_updates": [],
        }
        devices.append(device_obj)
        payload = {"success": True, "device_id": id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDevice",
                "description": "Add a completely new device to devices.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Unique id."},
                        "type": {"type": "string", "description": "Device type."},
                        "name": {
                            "type": "string",
                            "description": "Human‑readable name.",
                        },
                        "location": {
                            "type": "string",
                            "description": "Room name/location.",
                        },
                        "vendor": {"type": "string", "description": "Vendor name."},
                        "model": {"type": "string", "description": "Model name."},
                        "firmware_version": {
                            "type": "string",
                            "description": "Firmware version.",
                        },
                        "state_params": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "state": {
                            "type": "object",
                            "description": "Key/value pairs of state to set.",
                        },
                    },
                    "required": ["id", "type", "location", "state_params", "state"],
                    "additionalProperties": True,
                },
            },
        }
