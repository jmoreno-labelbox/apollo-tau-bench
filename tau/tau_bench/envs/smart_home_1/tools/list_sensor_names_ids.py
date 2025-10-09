from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListSensorNamesIds(Tool):

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = [
            {"name": s["name"], "sensor_id": s["id"]}
            for s in data.get("sensors", [])
        ]
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSensorNamesIds",
                "description": "Return all sensors' names and ids (state is read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
