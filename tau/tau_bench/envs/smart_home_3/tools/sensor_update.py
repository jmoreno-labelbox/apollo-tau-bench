from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SensorUpdate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sensor_id: str = None, sensor_type: str = None, location: str = None, state_param: dict[str, Any] = None, type: Any = None) -> str:
        sensors = data.get("sensors", [])
        if not state_param:
            payload = {"error": "New state ins obligatory"}
            out = json.dumps(payload, indent=2)
            return out
        result = [
            s
            for s in sensors
            if (not sensor_id or s["id"] == sensor_id)
            and (not sensor_type or s["type"] == sensor_type)
            and (not location or s["location"] == location)
        ]
        if len(result) == 0:
            payload = {"error": "No device fund"}
            out = json.dumps(payload, indent=2)
            return out
        for s in result:
            for key in state_param:
                if not s["state"][key]:
                    payload = {"error": "State not found in sensors filtered"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                s["state"][key] = state_param[key]
        payload = {"success": f"Sensors updated {result}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sensorUpdate",
                "description": "Update sensor state",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {"type": "string", "description": "Sensor ID"},
                        "type": {
                            "type": "string",
                            "description": "Filter by sensor type",
                        },
                        "location": {
                            "type": "string",
                            "description": "Filter by location",
                        },
                        "state_param": {
                            "type": "string",
                            "description": "Get specific state parameter only",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
