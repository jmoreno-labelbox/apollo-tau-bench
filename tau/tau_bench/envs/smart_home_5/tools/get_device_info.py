# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDeviceInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_ids: Optional[List[str]] = None) -> str:
        devices = list(data.get('devices', {}).values())
        if device_ids:
            result = [d for d in devices if d.get('id') in device_ids]
        else:
            result = devices
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device_info",
                "description": "Get information about one or more devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of device IDs to retrieve. If empty, all devices will be returned."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
