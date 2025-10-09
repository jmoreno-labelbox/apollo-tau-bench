from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetResourceByName(Tool):
    """Locate a resource by its user-friendly name."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_name: str = None) -> str:
        resource_name_to_find = resource_name
        try:
            all_resources = data.get("resources", {}).values()
        except:
            all_resources = []

        for resource in all_resources:
            if resource.get("name") == resource_name_to_find:
                payload = resource
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource with name '{resource_name_to_find}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceByName",
                "description": "Retrieves the full details of a resource by searching for its exact name (e.g., 'Sales Reporting Dashboard').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "The unique, human-readable name of the resource.",
                        }
                    },
                    "required": ["resource_name"],
                },
            },
        }
