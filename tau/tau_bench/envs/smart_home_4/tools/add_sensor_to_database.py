from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddSensorToDatabase(Tool):
    """Introduce a new device."""

    @staticmethod
    def invoke(data: dict[str, Any], sensor: dict[str, Any] | None = None) -> str:
        if not sensor:
            payload = {"error": "'sensor' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        sensors_list = data.get("sensors", [])
        if any(d["id"] == sensor.get("id") for d in sensors_list):
            payload = {"error": "Sensor with this id already exists"}
            out = json.dumps(payload, indent=2)
            return out
        sensors_list.append(sensor)
        payload = {"success": "Sensor added", "sensor": sensor, "sensors": sensors_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSensorToDatabase",
                "description": "Add a new sensor. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "object",
                            "description": "The full sensor object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["sensor"],
                    "additionalProperties": False,
                },
            },
        }
