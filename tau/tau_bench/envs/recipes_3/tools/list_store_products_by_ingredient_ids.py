from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListStoreProductsByIngredientIds(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: int, ingredient_ids: list[int]) -> str:
        sp = _get_table(data, "store_products")
        rows = [
            p
            for p in sp
            if p.get("store_id") == store_id
            and p.get("ingredient_id") in (ingredient_ids or [])
        ]
        payload = {"products": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreProductsByIngredientIds",
                "description": "Returns store_products for a store filtered by ingredient_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "ingredient_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                    },
                    "required": ["store_id", "ingredient_ids"],
                },
            },
        }
