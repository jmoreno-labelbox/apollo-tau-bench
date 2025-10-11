# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetResourceDetailsById(Tool):
    """ Get the full details of a specific resource using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], resource_id) -> str:
        try:
            resources = data.get('resources', [])
        except:
            resources = []

        for resource in resources:
            if resource.get("resource_id") == resource_id:
                return json.dumps(resource)

        return json.dumps({"error": f"Resource with ID '{resource_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_details_by_id",
                "description": "Retrieves the full details of a specific resource (e.g., its criticality) using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to retrieve (e.g., 'RES-025')."
                        }
                    },
                    "required": ["resource_id"]
                }
            }
        }
