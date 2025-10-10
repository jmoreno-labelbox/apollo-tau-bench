# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        products = list(data.get("products", {}).values())
        match = next((p for p in products if p.get("name") == name), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_name",
                "description": "Return a product by exact display name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
