# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find


class ModifySensorState(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sensor_id: str, update: Dict[str, Any]) -> str:
        sensors = data.get("sensors", [])
        _, sensor = _find(sensors, sensor_id)
        if not sensor:
            return json.dumps({"error": f"sensor '{sensor_id}' not found"}, indent=2)
        allowed = set(sensor.get("state_params", []))
        if any(k not in allowed for k in update):
            return json.dumps({"error": "one or more params not allowed for this sensor"}, indent=2)
        sensor_state = sensor.get("state", {})
        sensor_state.update(update)
        sensor_state["last_updated"] = _now_iso()
        return json.dumps({"success": "state updated", "state": sensor_state}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_sensor_state",
                "description": "Update the live state of a sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {"type": "string", "description": "Target sensor id"},
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["sensor_id", "update"],
                    "additionalProperties": False
                }
            }
        }
