# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSensorByIdOrFilter(Tool):
    """Retrieve sensor(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], sensor: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        sensor_list = data.get('sensors', [])
        if sensor:
            result = [d for d in sensor_list if d.get("id") == sensor]
        elif filters:
            result = [d for d in sensor_list if all(d.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'devices' (id) or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sensor_by_id_or_filter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "string",
                            "description": "Sensor id to retrieve (optional if using filters)"
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
