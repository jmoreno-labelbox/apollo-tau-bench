# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateResourceOwner(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        new_owner_id = kwargs.get("new_owner_id")
        for res in data.get('resources', []):
            if res.get('resource_id') == resource_id:
                res['owner_id'] = new_owner_id
                return json.dumps(res)
        return json.dumps({"error": "Resource not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_resource_owner",
                        "description": "Updates the owner of a resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "resource_id": {"type": "string"},
                                        "new_owner_id": {"type": "string"}
                                },
                                "required": ["resource_id", "new_owner_id"]
                        }
                }
        }
