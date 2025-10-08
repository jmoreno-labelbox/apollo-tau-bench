from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class UpdateResourceOwner(Tool):
    """Modifies the 'owner_id' field for a specific resource in the database."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, new_owner_id: str = None) -> str:
        resource_id_to_update = resource_id
        new_owner_id = new_owner_id

        try:
            resources = data.get("resources", [])
        except (KeyError, json.JSONDecodeError):
            resources = []

        resource_to_update = None
        for resource in resources:
            if resource.get("resource_id") == resource_id_to_update:
                resource["owner_id"] = new_owner_id
                resource_to_update = resource
                break

        if not resource_to_update:
            payload = {"error": f"Resource with ID '{resource_id_to_update}' not found."}
            out = json.dumps(
                payload)
            return out

        data["resources"] = resources
        payload = {
                "message": "Resource owner updated successfully.",
                "resource_details": resource_to_update,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateResourceOwner",
                "description": "Updates the owner of a specific resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource whose owner needs to be updated.",
                        },
                        "new_owner_id": {
                            "type": "string",
                            "description": "The user ID of the new owner for the resource.",
                        },
                    },
                    "required": ["resource_id", "new_owner_id"],
                },
            },
        }
