# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDeviceByIdOrFilter(Tool):
    """Retrieve device(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], devices: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        device_list = list(data.get('devices', {}).values())
        if devices:
            result = [d for d in device_list if d.get("id") == devices]
        elif filters:
            result = [d for d in device_list if all(d.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'devices' (id) or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device_by_id_or_filter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "devices": {
                            "type": "string",
                            "description": "Device id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
