# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStores(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return _json({"stores": data.get("stores", [])})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_stores",
                "description": "List stores.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
