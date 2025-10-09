from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetResourceDetailsById(Tool):
    """Obtain the complete details of a specific resource by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        try:
            resources = data.get("resources", [])
        except:
            resources = []

        for resource in resources:
            if resource.get("resource_id") == resource_id:
                payload = resource
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource with ID '{resource_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceDetailsById",
                "description": "Retrieves the full details of a specific resource (e.g., its criticality) using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to retrieve (e.g., 'RES-025').",
                        }
                    },
                    "required": ["resource_id"],
                },
            },
        }
