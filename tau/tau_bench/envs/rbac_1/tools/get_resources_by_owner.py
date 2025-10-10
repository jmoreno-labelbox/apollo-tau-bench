# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetResourcesByOwner(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner_id = kwargs.get("owner_id")

        owned_resources = [
                resource for resource in data.get('resources', [])
                if resource.get('owner_id') == owner_id
        ]

        return json.dumps({"resources": owned_resources})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_resources_by_owner",
                        "description": "Retrieves a list of all resources owned by a specific user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "owner_id": {
                                                "type": "string",
                                                "description": "The user_id of the resource owner."
                                        }
                                },
                                "required": ["owner_id"]
                        }
                }
        }
