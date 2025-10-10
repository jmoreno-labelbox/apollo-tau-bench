# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSensorData(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sensor_ids: Optional[List[str]] = None) -> str:
        sensors = data.get('sensors', [])
        if sensor_ids:
            result = [s for s in sensors if s.get('id') in sensor_ids]
        else:
            result = sensors
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sensor_data",
                "description": "Get data from one or more sensors. Sensor state is read-only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of sensor IDs to retrieve data from. If empty, returns data for all sensors."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
