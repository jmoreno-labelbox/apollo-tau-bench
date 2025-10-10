# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListDevices(Tool):
    """Return an array of all devices with optional type/location filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], type: Optional[str] = None, location: Optional[str] = None) -> str:
        devices = list(data.get("devices", {}).values())
        if type:
            devices = [d for d in devices if d["type"] == type]
        if location:
            devices = [d for d in devices if d["location"].lower() == location.lower()]
        return json.dumps({"devices": devices}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_devices",
                "description": "List all devices, optionally filtering by type or location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string", "description": "Device type filter (e.g. 'light', 'curtain')."},
                        "location": {"type": "string", "description": "Location/room name filter."},
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
