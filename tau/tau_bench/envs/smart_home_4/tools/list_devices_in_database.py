from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListDevicesInDatabase(Tool):
    """Display all devices, with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] | None = None) -> str:
        device_list = data.get("devices", [])
        if filters:
            result = [
                d for d in device_list if all(d.get(k) == v for k, v in filters.items())
            ]
        else:
            result = device_list
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listDevicesInDatabase",
                "description": "List all devices, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional)",
                            "additionalProperties": True,
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
