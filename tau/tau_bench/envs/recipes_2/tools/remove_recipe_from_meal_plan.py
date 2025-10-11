# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveRecipeFromMealPlan(Tool):
    """Removes a recipe from a meal plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], entry_id) -> str:
        entries = data.get("meal_plan_entries", [])
        entry_to_remove = next((e for e in entries if e.get("entry_id") == entry_id), None)
        if entry_to_remove:
            data["meal_plan_entries"] = [e for e in entries if e.get("entry_id") != entry_id]
            return json.dumps({"status": "success", "message": f"Entry {entry_id} removed."})
        return json.dumps({"error": f"Meal plan entry {entry_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_recipe_from_meal_plan",
                "description": "Removes a recipe from a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {"entry_id": {"type": "integer"}},
                    "required": ["entry_id"],
                },
            },
        }
