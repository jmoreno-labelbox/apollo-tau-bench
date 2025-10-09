from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetRecipeIngredients(Tool):
    """Obtains all components for a certain recipe ID."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        recipe_ingredients = data.get("recipe_ingredients", [])
        ingredients = [
            ri for ri in recipe_ingredients if ri.get("recipe_id") == recipe_id
        ]
        payload = ingredients
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeIngredients",
                "description": "Retrieves all ingredients for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe.",
                        }
                    },
                    "required": ["recipe_id"],
                },
            },
        }
