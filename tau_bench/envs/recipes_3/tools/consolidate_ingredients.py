from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConsolidateIngredients(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids: list[int]) -> str:
        ri = _get_table(data, "recipe_ingredients")
        agg: dict[tuple[int, str], float] = {}
        for rid in recipe_ids or []:
            for row in ri:
                if row["recipe_id"] != rid:
                    continue
                key = (row["ingredient_id"], row["unit"])
                qty = float(row["quantity"] or 0)
                agg[key] = agg.get(key, 0.0) + qty
        items = [
            {"ingredient_id": ing, "quantity": qty, "unit": unit}
            for (ing, unit), qty in agg.items()
        ]
        payload = {"items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "consolidateIngredients",
                "description": "Aggregates recipe_ingredients for provided recipe_ids by ingredient_id and unit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}}
                    },
                    "required": ["recipe_ids"],
                },
            },
        }
