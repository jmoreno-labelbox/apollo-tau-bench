# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_name) -> str:
        n = product_name
        for p in list(data.get("dim_product", {}).values()):
            if p.get("name") == n:
                return json.dumps(p)
        return json.dumps({"error": f"product {n} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_product_by_name", "description": "Looks up a product by name.",
                             "parameters": {"type": "object", "properties": {"product_name": {"type": "string"}},
                                            "required": ["product_name"]}}}
