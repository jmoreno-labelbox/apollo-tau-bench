# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListDevicesInDatabase(Tool):
    """List all devices, with optional filters."""
    @staticmethod
    def invoke(data: Dict[str, Any], filters: Optional[Dict[str, Any]] = None) -> str:
        device_list = list(data.get('devices', {}).values())
        if filters:
            result = [d for d in device_list if all(d.get(k) == v for k, v in filters.items())]
        else:
            result = device_list
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_devices_in_database",
                "description": "List all devices, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
