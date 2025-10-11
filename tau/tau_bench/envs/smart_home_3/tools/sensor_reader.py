# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SensorReader(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], location, sensor_id, state_param, threshold, type) -> str:
        sensors = list(data.get('sensors', {}).values())
        sensor_type = type

        result = [s for s in sensors if (not sensor_id or s['id'] == sensor_id) and
                 (not sensor_type or s['type'] == sensor_type) and
                 (not location or s['location'] == location)]

        if state_param:
            if threshold:
                result = [s for s in result if (s['state'].get(state_param)) and ((threshold.get('operator') == 'gt' and s['state'].get(state_param) > threshold.get('value')) or (threshold.get('operator') == 'lt' and s['state'].get(state_param) < threshold.get('value')))]
            else:
                result = [{**s, 'filtered_state': {state_param: s['state'].get(state_param)}} for s in result]

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sensor_reader",
                "description": "Read sensor data (read-only access)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {"type": "string", "description": "Sensor ID"},
                        "type": {"type": "string", "description": "Filter by sensor type"},
                        "location": {"type": "string", "description": "Filter by location"},
                        "state_param": {"type": "string", "description": "Get specific state parameter only"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
