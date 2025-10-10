# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSensorState(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], sensor_id: str) -> str:
        for sen in data.get("sensors", []):
            if sen["id"] == sensor_id:
                return json.dumps({"state": sen["state"]}, indent=2)
        return json.dumps({"error": "Sensor not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sensor_state",
                "description": "Read current state values for a sensor (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {"sensor_id": {"type": "string", "description": "Sensor identifier."}},
                    "required": ["sensor_id"],
                    "additionalProperties": False,
                },
            },
        }
