# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReturnIds(Tool):
    """Tool to return list of ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], list_of_ids = []) -> str:
        return json.dumps(list_of_ids, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "return_ids",
                "description": "Return List of Ids",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": []
                }
            }
        }
