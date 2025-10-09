from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifySensorState(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sensor_id: str, update: dict[str, Any]) -> str:
        sensors = data.get("sensors", [])
        _, sensor = _find(sensors, sensor_id)
        if not sensor:
            payload = {"error": f"sensor '{sensor_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        allowed = set(sensor.get("state_params", []))
        if any(k not in allowed for k in update):
            payload = {"error": "one or more params not allowed for this sensor"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        sensor_state = sensor.get("state", {})
        sensor_state.update(update)
        sensor_state["last_updated"] = _now_iso()
        payload = {"success": "state updated", "state": sensor_state}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifySensorState",
                "description": "Update the live state of a sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {
                            "type": "string",
                            "description": "Target sensor id",
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["sensor_id", "update"],
                    "additionalProperties": False,
                },
            },
        }
