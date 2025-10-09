from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetDeviceByIdOrFilter(Tool):
    """Fetch device(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any], devices: str = "", filters: dict[str, Any] | None = None
    ) -> str:
        device_list = data.get("devices", [])
        if devices:
            result = [d for d in device_list if d.get("id") == devices]
        elif filters:
            result = [
                d for d in device_list if all(d.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'devices' (id) or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeviceByIdOrFilter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "devices": {
                            "type": "string",
                            "description": "Device id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
