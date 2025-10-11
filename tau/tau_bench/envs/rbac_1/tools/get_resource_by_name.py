# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetResourceByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        for res in data.get('resources', []):
            if res.get('name') == name:
                return json.dumps(res)
        return json.dumps({"error": "Resource not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_resource_by_name",
                        "description": "Retrieves a resource by its name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "name": {"type": "string"}
                                },
                                "required": ["name"]
                        }
                }
        }
