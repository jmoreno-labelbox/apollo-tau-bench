from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateDeviceInDatabase(Tool):
    """Modify any attribute of a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any], device_id: str = "", updates: dict[str, Any] | None = None
    ) -> str:
        if not device_id or not updates:
            payload = {"error": "'device_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        device_list = data.get("devices", [])
        found = False
        for d in device_list:
            if d["id"] == device_id:
                for k, v in updates.items():
                    if k in d:
                        d[k] = v
                    elif k in d.get("state", {}):
                        d["state"][k] = v
                    else:
                        d[k] = v
                found = True
                break
        if not found:
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Device updated",
                "device_id": device_id,
                "updates": updates,
                "devices": device_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDeviceInDatabase",
                "description": "Update any field of a device by id. Updates can be for top-level or nested fields (e.g., state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update. For nested fields like state, use the field name directly.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["device_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
