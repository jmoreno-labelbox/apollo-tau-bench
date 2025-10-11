# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateResourceOwner(Tool):
    """ Updates the 'owner_id' field for a specific resource in the database. """

    @staticmethod
    def invoke(data: Dict[str, Any], new_owner_id, resource_id) -> str:
        resource_id_to_update = resource_id

        try:
            resources = data.get('resources', [])
        except (KeyError, json.JSONDecodeError):
            resources = []

        resource_to_update = None
        for resource in resources:
            if resource.get("resource_id") == resource_id_to_update:
                resource["owner_id"] = new_owner_id
                resource_to_update = resource
                break

        if not resource_to_update:
            return json.dumps({"error": f"Resource with ID '{resource_id_to_update}' not found."})

        data['resources'] = resources
        return json.dumps({
            "message": "Resource owner updated successfully.",
            "resource_details": resource_to_update
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_resource_owner",
                "description": "Updates the owner of a specific resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource whose owner needs to be updated."
                        },
                        "new_owner_id": {
                            "type": "string",
                            "description": "The user ID of the new owner for the resource."
                        }
                    },
                    "required": ["resource_id", "new_owner_id"]
                }
            }
        }
