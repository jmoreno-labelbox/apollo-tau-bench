# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddSensorToDatabase(Tool):
    """Add a new device."""
    @staticmethod
    def invoke(data: Dict[str, Any], sensor: Optional[Dict[str, Any]] = None) -> str:
        if not sensor:
            return json.dumps({"error": "'sensor' parameter is required"}, indent=2)
        sensors_list = data.get('sensors', [])
        if any(d["id"] == sensor.get("id") for d in sensors_list):
            return json.dumps({"error": "Sensor with this id already exists"}, indent=2)
        sensors_list.append(sensor)
        return json.dumps({"success": "Sensor added", "sensor": sensor, "sensors": sensors_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_sensor_to_database",
                "description": "Add a new sensor. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "object",
                            "description": "The full sensor object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["sensor"],
                    "additionalProperties": False
                }
            }
        }
