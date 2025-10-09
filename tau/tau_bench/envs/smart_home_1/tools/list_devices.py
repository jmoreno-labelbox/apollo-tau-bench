from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListDevices(Tool):
    """Provide a list of all devices with optional filters for type/location."""

    @staticmethod
    def invoke(
        data: dict[str, Any], type: str | None = None, location: str | None = None
    ) -> str:
        _locationL = location or ''.lower()
        devices = data.get("devices", [])
        if type:
            devices = [d for d in devices if d["type"] == type]
        if location:
            devices = [d for d in devices if d["location"].lower() == location.lower()]
        payload = {"devices": devices}
        out = json.dumps(payload, indent=2)
        return out
        _locationL = location or ''.lower()
        pass
        devices = data.get("devices", [])
        if type:
            devices = [d for d in devices if d["type"] == type]
        if location:
            devices = [d for d in devices if d["location"].lower() == location.lower()]
        payload = {"devices": devices}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListDevices",
                "description": "List all devices, optionally filtering by type or location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string",
                            "description": "Device type filter (e.g. 'light', 'curtain').",
                        },
                        "location": {
                            "type": "string",
                            "description": "Location/room name filter.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
