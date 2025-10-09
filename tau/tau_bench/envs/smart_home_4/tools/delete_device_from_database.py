from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteDeviceFromDatabase(Tool):
    """Delete a device using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], device_id: str = "") -> str:
        if not device_id:
            payload = {"error": "'device_id' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        device_list = data.get("devices", [])
        new_list = [d for d in device_list if d["id"] != device_id]
        if len(new_list) == len(device_list):
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": "Device deleted", "device_id": device_id, "devices": new_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteDeviceFromDatabase",
                "description": "Remove a device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to delete.",
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }
