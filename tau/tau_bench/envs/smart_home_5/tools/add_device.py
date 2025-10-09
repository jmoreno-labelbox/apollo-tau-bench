from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_device_id: str = None, new_device_name: str = None,
    new_device: Any = None,
    ) -> str:
        devices = data.get("devices", {}).values()
        if not new_device_id:
            payload = {"error": "New device must have an 'id'."}
            out = json.dumps(payload, indent=2)
            return out

        if any(d.get("id") == new_device_id for d in devices.values()):
            payload = {"error": f"Device with ID '{new_device_id}' already exists."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_device = {"id": new_device_id, "name": new_device_name}
        data["devices"][device_id] = new_device
        payload = {"success": f"Device '{new_device_name or new_device_id}' added."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDevice",
                "description": "Add a new device to the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_device": {
                            "type": "object",
                            "description": "A dictionary representing the new device.",
                            "properties": {
                                "id": {"type": "string"},
                                "type": {"type": "string"},
                                "name": {"type": "string"},
                                "location": {"type": "string"},
                            },
                            "required": ["id", "type", "name"],
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_device"],
                    "additionalProperties": False,
                },
            },
        }
