from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSensorState(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], sensor_id: str) -> str:
        for sen in data.get("sensors", []):
            if sen["id"] == sensor_id:
                payload = {"state": sen["state"]}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Sensor not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSensorState",
                "description": "Read current state values for a sensor (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {
                            "type": "string",
                            "description": "Sensor identifier.",
                        }
                    },
                    "required": ["sensor_id"],
                    "additionalProperties": False,
                },
            },
        }
