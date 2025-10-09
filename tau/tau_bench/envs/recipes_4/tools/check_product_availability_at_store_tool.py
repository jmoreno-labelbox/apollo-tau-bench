from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckProductAvailabilityAtStoreTool(Tool):
    """
    A tool to check product availability for a grocery list at a specific store.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CheckProductAvailabilityAtStore",
                "description": (
                    "Checks the stock status for each item on a grocery list at a specific store. "
                    "Returns a list of items that are low in stock or out of stock."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to check.",
                        },
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store to check against.",
                        },
                    },
                    "required": ["list_id", "store_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int, store_id: int) -> dict[str, Any]:
        """
        Executes the logic to check store inventory against a grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            list_id: The ID of the grocery list to check.
            store_id: The ID of the store to check against.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of items with potential stock issues.
        """
        #1. Validate Inputs
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "store_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs({"list_id": list_id, "store_id": store_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id}
            )
        if not any(s.get("store_id") == store_id for s in data.get("stores", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Store", "entity_id": store_id}
            )

        #3. Core Logic
        list_items = [
            item
            for item in data.get("grocery_list_items", [])
            if item.get("list_id") == list_id
        ]
        all_store_products = data.get("store_products", [])
        all_ingredients_meta = data.get("ingredients", [])

        problem_items = []
        for item in list_items:
            ingredient_id = item["ingredient_id"]

            #Find all products at the store for this ingredient
            candidate_products = [
                p
                for p in all_store_products
                if p.get("store_id") == store_id
                and p.get("ingredient_id") == ingredient_id
            ]

            #Find the best available product (in stock or low, and cheapest)
            in_stock_products = [
                p
                for p in candidate_products
                if p.get("stock_status_enum") in ("in_stock", "low")
            ]

            best_product = None
            if in_stock_products:
                best_product = min(
                    in_stock_products, key=lambda p: p.get("price_cents", float("inf"))
                )

            status = ""
            if not best_product:
                status = "out_of_stock"
            elif best_product.get("stock_status_enum") == "low":
                status = "low_stock"

            if status:
                ingredient_meta = next(
                    (
                        i
                        for i in all_ingredients_meta
                        if i["ingredient_id"] == ingredient_id
                    ),
                    {},
                )
                problem_items.append(
                    {
                        "ingredient_id": ingredient_id,
                        "ingredient_name": ingredient_meta.get(
                            "ingredient_name", "Unknown"
                        ),
                        "status": status,
                    }
                )

        #4. Response
        return _build_success_response(problem_items)
