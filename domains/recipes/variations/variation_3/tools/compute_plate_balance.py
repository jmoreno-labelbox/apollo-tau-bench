from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputePlateBalance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> str:
        pass
        # Deterministic macro categorization using ingredient grocery_section as a reference
        ri = _get_table(data, "recipe_ingredients")
        ingredients = _get_table(data, "ingredients")
        section_map = {
            i["ingredient_id"]: i["grocery_section"] for i in ingredients
        }
        rows = [r for r in ri if r["recipe_id"] == recipe_id]
        counts = {"veggies": 0, "protein": 0, "carb": 0, "fats": 0}
        for r in rows:
            sec = section_map.get(r["ingredient_id"]) or ""
            if sec in ("Produce", "Cereal & Breakfast"):
                counts["veggies"] += 1
            elif sec in ("Meat", "Seafood", "Refrigerated", "Deli"):
                counts["protein"] += 1
            elif sec in ("Pasta & Grains", "Bakery", "Canned Goods"):
                counts["carb"] += 1
            elif sec in ("Oils & Vinegars", "Spreads", "Health Foods"):
                counts["fats"] += 1
        payload = {"plate": counts}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computePlateBalance",
                "description": "Returns a coarse macro balance proxy for a recipe.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
