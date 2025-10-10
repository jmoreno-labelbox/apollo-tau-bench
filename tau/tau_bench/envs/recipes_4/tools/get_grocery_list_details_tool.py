# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGroceryListDetailsTool(Tool):
    """
    A tool to retrieve the full details of a grocery list, including its items.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_details",
                "description": "Retrieves a grocery list and all its items, enriched with ingredient names, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique identifier for the grocery list to retrieve."
                        }
                    },
                    "required": ["list_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], list_id) -> Dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'list_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed grocery list object.
        """
        # 1. Verify Input Data
        param_definitions = {
            "list_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Data Acquisition: Locate the primary grocery list object.
        list_record = next(
            (g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id),
            None
        )

        if not list_record:
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})

        # 3. Data Enrichment (Hydration): Retrieve and augment list elements.
        list_items = [
            item for item in data.get("grocery_list_items", []) if item.get("list_id") == list_id
        ]

        enriched_items = []
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        for item in list_items:
            ingredient_meta = next(
                (i for i in all_ingredients_meta if i.get("ingredient_id") == item.get("ingredient_id")),
                None
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = ingredient_meta.get("ingredient_name") if ingredient_meta else "Unknown Ingredient"
            enriched_items.append(enriched_item)

        # Arrange items according to grocery categories for better organization.
        enriched_items.sort(key=lambda x: (x.get("grocery_section", ""), x.get("ingredient_name", "")))

        # 4. Construct the ultimate response object.
        detailed_list = list_record.copy()
        detailed_list["items"] = enriched_items

        # 5. Provide the standardized success reply
        return _build_success_response(detailed_list)
