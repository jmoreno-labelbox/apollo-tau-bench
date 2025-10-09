from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveRecipeFromMealPlan(Tool):
    """Deletes a recipe from a meal plan."""

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: str = None) -> str:
        entries = data.get("meal_plan_entries", {}).values()
        entry_to_remove = next(
            (e for e in entries.values() if e.get("entry_id") == entry_id), None
        )
        if entry_to_remove:
            data["meal_plan_entries"] = [
                e for e in entries.values() if e.get("entry_id") != entry_id
            ]
            payload = {"status": "success", "message": f"Entry {entry_id} removed."}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Meal plan entry {entry_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveRecipeFromMealPlan",
                "description": "Removes a recipe from a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {"entry_id": {"type": "integer"}},
                    "required": ["entry_id"],
                },
            },
        }
