# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHouseholdInventoryTool(Tool):
    """
    A tool to retrieve all inventory items for a specific household.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_household_inventory",
                "description": "Retrieves a list of all inventory items for a given household, enriched with ingredient names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household."
                        }
                    },
                    "required": ["household_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> Dict[str, Any]:
        """
        Executes the logic to find and return a household's inventory.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'household_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of enriched inventory items.
        """
        # 1. Verify Input Data
        param_definitions = {
            "household_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Pre-condition Validation: Verify the existence of the household.
        if not any(h.get("household_id") == household_id for h in data.get("households", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 3. Data Acquisition and Enhancement (Hydration)
        inventory_items = [i for i in data.get("inventory_items", []) if i.get("household_id") == household_id]

        enriched_items = []
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        for item in inventory_items:
            ingredient_meta = next(
                (i for i in all_ingredients_meta if i.get("ingredient_id") == item.get("ingredient_id")),
                None
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = ingredient_meta.get("ingredient_name") if ingredient_meta else "Unknown Ingredient"
            enriched_items.append(enriched_item)

        # 4. Organize results in alphabetical order for uniformity.
        enriched_items.sort(key=lambda x: x.get("ingredient_name", ""))

        # 5. Provide the standardized success response.
        return _build_success_response(enriched_items)
