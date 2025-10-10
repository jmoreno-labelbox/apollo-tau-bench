# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDevice(Tool):
    """Fetch a single device record by its id."""

    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices: List[Dict[str, Any]] = list(data.get("devices", {}).values())
        dev = next((d for d in devices if d.get("id") == device_id), None)
        if not dev:
            return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)
        return json.dumps({"device": dev}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device",
                "description": "Fetch the full record for a specific device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "The device identifier."},
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
