from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class FindResources(Tool):
    """Identify resources using search criteria such as name keywords, criticality, or owner ID."""

    @staticmethod
    def invoke(data: dict[str, Any], name_keyword: str = None, criticality: str = None, owner_id: str = None) -> str:
        try:
            resources = data.get("resources", [])
        except:
            resources = []

        matching_resources = []
        for resource in resources:
            if (
                name_keyword
                and name_keyword.lower() not in resource.get("name", "").lower()
            ):
                continue
            if (
                criticality
                and criticality.upper() != resource.get("criticality", "").upper()
            ):
                continue
            if owner_id and owner_id != resource.get("owner_id"):
                continue
            matching_resources.append(resource)
        payload = matching_resources
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindResources",
                "description": "Searches for resources based on a combination of criteria. Returns a list of matching resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_keyword": {
                            "type": "string",
                            "description": "A keyword to search for within the resource name.",
                        },
                        "criticality": {
                            "type": "string",
                            "description": "The criticality level to filter by.",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "The user ID of the resource owner to filter by.",
                        },
                    },
                    "required": [],
                },
            },
        }
