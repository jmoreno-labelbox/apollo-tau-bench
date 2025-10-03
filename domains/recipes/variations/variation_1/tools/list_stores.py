from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListStores(Tool):
    """Retrieve all stores."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        return _json_dump(data.get("stores", []))
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStores",
                "description": "List available stores.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
