from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSensorByIdOrFilter(Tool):
    """Fetch sensor(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any], sensor: str = "", filters: dict[str, Any] | None = None
    ) -> str:
        sensor_list = data.get("sensors", {}).values()
        if sensor:
            result = [d for d in sensor_list.values() if d.get("id") == sensor]
        elif filters:
            result = [
                d for d in sensor_list.values() if all(d.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'devices' (id) or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSensorByIdOrFilter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "string",
                            "description": "Sensor id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
