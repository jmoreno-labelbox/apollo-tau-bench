# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindResources(Tool):
    """ Find resources based on search criteria like name keywords, criticality, or owner ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_keyword = kwargs.get("name_keyword")
        criticality = kwargs.get("criticality")
        owner_id = kwargs.get("owner_id")  # The ESSENTIAL new parameter

        try:
            resources = data.get('resources', [])
        except:
            resources = []

        matching_resources = []
        for resource in resources:
            if name_keyword and name_keyword.lower() not in resource.get("name", "").lower():
                continue
            if criticality and criticality.upper() != resource.get("criticality", "").upper():
                continue
            # This is the new, required logic
            if owner_id and owner_id != resource.get("owner_id"):
                continue
            matching_resources.append(resource)

        return json.dumps(matching_resources)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_resources",
                "description": "Searches for resources based on a combination of criteria. Returns a list of matching resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_keyword": {"type": "string", "description": "A keyword to search for within the resource name."},
                        "criticality": {"type": "string", "description": "The criticality level to filter by."},
                        "owner_id": {"type": "string", "description": "The user ID of the resource owner to filter by."} # The new parameter info
                    },
                    "required": []
                }
            }
        }
