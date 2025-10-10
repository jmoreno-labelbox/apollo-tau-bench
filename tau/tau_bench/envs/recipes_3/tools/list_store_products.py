# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStoreProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], store_id: int, ingredient_id: Optional[int] = None) -> str:
        rows = [
            p for p in data.get("store_products", []) if int(p.get("store_id")) == int(store_id)
        ]
        if ingredient_id is not None:
            rows = [p for p in rows if int(p.get("ingredient_id")) == int(ingredient_id)]
        return json({"products": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_store_products",
                "description": "List products for a store (optionally filtered by ingredient).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                    },
                    "required": ["store_id"],
                },
            },
        }
