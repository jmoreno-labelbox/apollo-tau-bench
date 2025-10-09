from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SensorReader(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sensor_id: str = None,
        sensor_type: str = None,
        location: str = None,
        state_param: str = None,
        threshold: dict[str, Any] = None
,
    type: Any = None,
    ) -> str:
        sensors = data.get("sensors", [])

        result = [
            s
            for s in sensors
            if (not sensor_id or s["id"] == sensor_id)
            and (not sensor_type or s["type"] == sensor_type)
            and (not location or s["location"] == location)
        ]

        if state_param:
            if threshold:
                result = [
                    s
                    for s in result
                    if (s["state"].get(state_param))
                    and (
                        (
                            threshold.get("operator") == "gt"
                            and s["state"].get(state_param) > threshold.get("value")
                        )
                        or (
                            threshold.get("operator") == "lt"
                            and s["state"].get(state_param) < threshold.get("value")
                        )
                    )
                ]
            else:
                result = [
                    {**s, "filtered_state": {state_param: s["state"].get(state_param)}}
                    for s in result
                ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SensorReader",
                "description": "Read sensor data (read-only access)",
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
