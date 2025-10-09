from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ReturnIds(Tool):
    """Utility for providing a list of identifiers."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list = None) -> str:
        if list_of_ids is None:
            list_of_ids = []
        payload = list_of_ids
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReturnIds",
                "description": "Return List of Ids",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        }
                    },
                    "required": [],
                },
            },
        }
