# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealPlanForWeekTool(Tool):
    """
    A tool to retrieve the full details of a meal plan, including all its entries.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plan_for_week",
                "description": (
                    "Retrieves a full meal plan and its daily entries by its unique ID. "
                    "The entries are enriched with recipe titles for clarity."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique identifier for the meal plan to retrieve."
                        }
                    },
                    "required": ["meal_plan_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full meal plan.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'meal_plan_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated meal plan object.
        """
        # 1. Verify Input Values
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        meal_plan_id = kwargs["meal_plan_id"]

        # 2. Data Acquisition: Locate the primary meal plan object
        meal_plan_record = next(
            (p for p in data.get("meal_plans", []) if p.get("meal_plan_id") == meal_plan_id),
            None
        )

        if not meal_plan_record:
            return _build_error_response("NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id})

        # 3. Data Enrichment (Hydration): Retrieve and enhance plan records.
        plan_entries = [
            e for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id
        ]

        enriched_entries = []
        all_recipes = list(data.get("recipes", {}).values())
        for entry in plan_entries:
            recipe_info = next(
                (r for r in all_recipes if r.get("recipe_id") == entry.get("recipe_id")),
                None
            )
            enriched_entry = entry.copy()
            enriched_entry["recipe_title"] = recipe_info.get("recipe_title") if recipe_info else "Unknown Recipe"
            enriched_entries.append(enriched_entry)

        # Organize entries chronologically for better clarity.
        enriched_entries.sort(key=lambda x: x.get("plan_date", ""))

        # 4. Construct the final response object.
        detailed_plan = meal_plan_record.copy()
        detailed_plan["entries"] = enriched_entries

        # 5. Provide the uniform success response.
        return _build_success_response(detailed_plan)
