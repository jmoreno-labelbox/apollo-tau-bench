from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any

class GetMealPlanForWeekTool(Tool):
    """
    A tool to retrieve the full details of a meal plan, including all its entries.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanForWeek",
                "description": (
                    "Retrieves a full meal plan and its daily entries by its unique ID. "
                    "The entries are enriched with recipe titles for clarity."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique identifier for the meal plan to retrieve.",
                        }
                    },
                    "required": ["meal_plan_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int) -> dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full meal plan.

        Args:
            data: The main in-memory dictionary containing all datasets.
            meal_plan_id: The ID of the meal plan to fetch.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated meal plan object.
        """
        #1. Validate Inputs
        param_definitions = {"meal_plan_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"meal_plan_id": meal_plan_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval: Find the base meal plan object
        meal_plan_record = next(
            (
                p
                for p in data.get("meal_plans", [])
                if p.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )

        if not meal_plan_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id}
            )

        #3. Data Enrichment (Hydration): Fetch and enrich plan entries
        plan_entries = [
            e
            for e in data.get("meal_plan_entries", [])
            if e.get("meal_plan_id") == meal_plan_id
        ]

        enriched_entries = []
        all_recipes = data.get("recipes", [])
        for entry in plan_entries:
            recipe_info = next(
                (
                    r
                    for r in all_recipes
                    if r.get("recipe_id") == entry.get("recipe_id")
                ),
                None,
            )
            enriched_entry = entry.copy()
            enriched_entry["recipe_title"] = (
                recipe_info.get("recipe_title") if recipe_info else "Unknown Recipe"
            )
            enriched_entries.append(enriched_entry)

        #Sort entries by date for a logical view
        enriched_entries.sort(key=lambda x: x.get("plan_date", ""))

        #4. Build the final response object
        detailed_plan = meal_plan_record.copy()
        detailed_plan["entries"] = enriched_entries

        #5. Return the standardized success response
        return _build_success_response(detailed_plan)
