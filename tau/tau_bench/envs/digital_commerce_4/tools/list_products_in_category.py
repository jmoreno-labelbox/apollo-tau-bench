# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListProductsInCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category_id: Any) -> str:
        category_id = _as_id(category_id)
        products = list(data.get("products", {}).values())
        rows = [p for p in products if _as_id(p.get("category_id")) == category_id]
        return json.dumps({"products": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_products_in_category",
                "description": "List products belonging to a category_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"category_id": {"type": "string"}},
                    "required": ["category_id"],
                },
            },
        }
