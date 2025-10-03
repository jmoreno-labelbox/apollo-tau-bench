from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetDeviceInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], device_ids: list[str] | None = None) -> str:
        devices = data.get("devices", [])
        if device_ids:
            result = [d for d in devices if d.get("id") in device_ids]
        else:
            result = devices
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeviceInfo",
                "description": "Get information about one or more devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of device IDs to retrieve. If empty, all devices will be returned.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }
