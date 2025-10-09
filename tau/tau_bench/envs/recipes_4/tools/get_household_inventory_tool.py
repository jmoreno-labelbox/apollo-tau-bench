from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetHouseholdInventoryTool(Tool):
    """
    A tool to retrieve all inventory items for a specific household.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdInventory",
                "description": "Retrieves a list of all inventory items for a given household, enriched with ingredient names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household.",
                        }
                    },
                    "required": ["household_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> dict[str, Any]:
        """
        Executes the logic to find and return a household's inventory.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household to retrieve inventory for.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of enriched inventory items.
        """
        #1. Validate Inputs
        param_definitions = {"household_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"household_id": household_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check: Ensure the household exists
        if not any(
            h.get("household_id") == household_id for h in data.get("households", {}).values()
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )

        #3. Data Retrieval and Enrichment (Hydration)
        inventory_items = [
            i
            for i in data.get("inventory_items", {}).values()
            if i.get("household_id") == household_id
        ]

        enriched_items = []
        all_ingredients_meta = data.get("ingredients", {}).values()
        for item in inventory_items:
            ingredient_meta = next(
                (
                    i
                    for i in all_ingredients_meta.values() if i.get("ingredient_id") == item.get("ingredient_id")
                ),
                None,
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = (
                ingredient_meta.get("ingredient_name")
                if ingredient_meta
                else "Unknown Ingredient"
            )
            enriched_items.append(enriched_item)

        #4. Sort results alphabetically for consistency
        enriched_items.sort(key=lambda x: x.get("ingredient_name", ""))

        #5. Return the standardized success response
        return _build_success_response(enriched_items)
