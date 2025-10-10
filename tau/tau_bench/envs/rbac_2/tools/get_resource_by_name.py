# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetResourceByName(Tool):
    """Find a resource using its human-readable name."""

    @staticmethod
    def invoke(data: Dict[str, Any], resource_name) -> str:
        try:
            all_resources = data.get('resources', [])
        except (KeyError, json.JSONDecodeError):
            all_resources = []

        for resource in all_resources:
            if resource.get("name") == resource_name:
                return json.dumps(resource)

        # 5. If all resources are checked and no match is found, return an error message.
        return json.dumps({"error": f"Resource with name '{resource_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_by_name",
                "description": "Retrieves the full details of a resource by searching for its exact name (e.g., 'sales-reporting-dashboard').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "The unique, human-readable name of the resource."
                        }
                    },
                    "required": ["resource_name"]
                }
            }
        }
