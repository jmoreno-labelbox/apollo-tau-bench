from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetDevice(Tool):
    """Retrieve a specific device record using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], device_id: str) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        dev = next((d for d in devices if d.get("id") == device_id), None)
        if not dev:
            payload = {"error": f"Device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"device": dev}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDevice",
                "description": "Fetch the full record for a specific device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The device identifier.",
                        },
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
