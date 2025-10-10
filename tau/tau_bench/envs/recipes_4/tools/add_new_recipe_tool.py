# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewRecipeTool(Tool):
    """
    A tool to add a new recipe to the dataset.
    """

    # Defines the set of expected fields for the main recipe data.
    EXPECTED_RECIPE_FIELDS = {
        "recipe_title", "meal_type", "cuisine", "servings_default",
        "prep_minutes", "cook_minutes", "is_peanut_free",
        "calories_per_serving", "protein_g_per_serving", "instructions_json",
        "notes"
    }

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "add_new_recipe",
                "description": (
                    "Adds a new recipe to the dataset. Requires recipe metadata and a "
                    "list of its ingredients with quantities and units."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_data": {
                            "type": "object",
                            "description": "A dictionary with the new recipe's main data."
                        },
                        "ingredients_list": {
                            "type": "array",
                            "description": "A list of ingredient objects, each with ingredient_id, quantity, and unit."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["recipe_data", "ingredients_list", "user_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to create a new recipe and its ingredient links.

        This method performs deep validation on the provided recipe data and
        ingredient list, creates records in both the 'recipes' and
        'recipe_ingredients' tables, logs the event, and returns the new recipe.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'recipe_data',
                      'ingredients_list', and 'user_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created recipe object.
        """
        # 1. Standard Validation
        param_definitions = {
            "recipe_data": {"type": dict, "required": True},
            "ingredients_list": {"type": list, "required": True},
            "user_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        recipe_data = kwargs["recipe_data"]
        ingredients_list = kwargs["ingredients_list"]
        user_id = kwargs["user_id"]

        # 2. Deep Validation
        if not AddNewRecipeTool.EXPECTED_RECIPE_FIELDS.issubset(recipe_data.keys()):
            return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "recipe_data", "expected_type": "object with all required recipe fields"})
        if not ingredients_list:
             return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "ingredients_list", "expected_type": "non-empty list"})

        all_ingredient_ids = {i["ingredient_id"] for i in list(data.get("ingredients", {}).values())}
        for item in ingredients_list:
            if not isinstance(item, dict) or not all(k in item for k in ["ingredient_id", "quantity", "unit"]):
                return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "ingredients_list", "expected_type": "list of valid ingredient objects"})
            if item["ingredient_id"] not in all_ingredient_ids:
                return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": item["ingredient_id"]})

        # 3. Create Recipe Record
        recipes_table = data.setdefault("recipes", [])
        max_recipe_id = max((r.get("recipe_id", 0) for r in recipes_table), default=400)
        new_recipe_id = max_recipe_id + 1

        new_recipe_record = {"recipe_id": new_recipe_id}
        new_recipe_record.update({key: recipe_data.get(key) for key in AddNewRecipeTool.EXPECTED_RECIPE_FIELDS})
        recipes_table.append(new_recipe_record)

        # 4. Create Recipe-Ingredient Links
        ri_table = data.setdefault("recipe_ingredients", [])
        max_ri_id = max((ri.get("ri_id", 0) for ri in ri_table), default=5000)

        for ingredient in ingredients_list:
            max_ri_id += 1
            new_ri_record = {
                "ri_id": max_ri_id,
                "recipe_id": new_recipe_id,
                "ingredient_id": ingredient["ingredient_id"],
                "quantity": ingredient["quantity"],
                "unit": ingredient["unit"]
            }
            ri_table.append(new_ri_record)

        # 5. Auditing
        user_household = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        household_id = user_household.get("household_id") if user_household else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="recipes",
            entity_id=new_recipe_id,
            action_enum="create",
            payload_json={"recipe_data": recipe_data, "ingredients_list": ingredients_list}
        )

        # 6. Response
        return _build_success_response(new_recipe_record)
