# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindProductByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        name = name
        match = next((p for p in list(data.get("products", {}).values()) if p.get("name") == name), {})
        return json.dumps(match, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_product_by_name",
                "description": "Returns product by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
