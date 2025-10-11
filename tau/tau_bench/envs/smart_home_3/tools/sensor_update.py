# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SensorUpdate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], location, sensor_id, state_param, type) -> str:
        sensors = list(data.get('sensors', {}).values())
        sensor_type = type
        if not state_param:
            return json.dumps({"error": "New state ins obligatory"},indent=2)
        result = [s for s in sensors if (not sensor_id or s['id'] == sensor_id) and
                 (not sensor_type or s['type'] == sensor_type) and
                 (not location or s['location'] == location)]
        if len(result) == 0:
            return json.dumps({"error": "No device fund"}, indent=2)
        for s in result:
            for key in state_param:
                if not s['state'][key]:
                    return json.dumps({"error": "State not found in sensors filtered"}, indent=2)
                s['state'][key] = state_param[key]

        return json.dumps({"success": f"Sensors updated {result}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sensor_update",
                "description": "Update sensor state",
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
