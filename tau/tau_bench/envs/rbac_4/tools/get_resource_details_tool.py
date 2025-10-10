# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetResourceDetailsTool(Tool):
    """Retrieve details for a given resource."""

    @staticmethod
    def invoke(data: Dict[str, Any], resource_id) -> str:
        rid = resource_id
        for res in data.get("resources", []):
            if res["resource_id"] == rid:
                return json.dumps(res, indent=2)
        return json.dumps({"error": f"Resource {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_details",
                "description": "Get full details of a resource from resource_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"}
                    },
                    "required": ["resource_id"]
                }
            }
        }
