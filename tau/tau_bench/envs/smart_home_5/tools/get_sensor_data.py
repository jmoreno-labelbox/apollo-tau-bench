from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSensorData(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sensor_ids: list[str] | None = None) -> str:
        sensors = data.get("sensors", {}).values()
        if sensor_ids:
            result = [s for s in sensors.values() if s.get("id") in sensor_ids]
        else:
            result = sensors
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSensorData",
                "description": "Get data from one or more sensors. Sensor state is read-only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of sensor IDs to retrieve data from. If empty, returns data for all sensors.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }
