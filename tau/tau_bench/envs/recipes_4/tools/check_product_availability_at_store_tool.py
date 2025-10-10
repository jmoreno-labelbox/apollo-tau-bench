# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckProductAvailabilityAtStoreTool(Tool):
    """
    A tool to check product availability for a grocery list at a specific store.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "check_product_availability_at_store",
                "description": (
                    "Checks the stock status for each item on a grocery list at a specific store. "
                    "Returns a list of items that are low in stock or out of stock."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to check."
                        },
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store to check against."
                        }
                    },
                    "required": ["list_id", "store_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], list_id, store_id) -> Dict[str, Any]:
        """
        Executes the logic to check store inventory against a grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'list_id' and 'store_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of items with potential stock issues.
        """
        # 1. Verify Input Data
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "store_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Preconditions Verification
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})
        if not any(s.get("store_id") == store_id for s in data.get("stores", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Store", "entity_id": store_id})

        # 3. Fundamental Logic
        list_items = [item for item in data.get("grocery_list_items", []) if item.get("list_id") == list_id]
        all_store_products = data.get("store_products", [])
        all_ingredients_meta = list(data.get("ingredients", {}).values())

        problem_items = []
        for item in list_items:
            ingredient_id = item["ingredient_id"]

            # Retrieve all items in the store containing this ingredient.
            candidate_products = [
                p for p in all_store_products
                if p.get("store_id") == store_id and p.get("ingredient_id") == ingredient_id
            ]

            # Identify the optimal product that is either in stock or has low availability and is the least expensive.
            in_stock_products = [p for p in candidate_products if p.get("stock_status_enum") in ("in_stock", "low")]

            best_product = None
            if in_stock_products:
                best_product = min(in_stock_products, key=lambda p: p.get("price_cents", float('inf')))

            status = ""
            if not best_product:
                status = "out_of_stock"
            elif best_product.get("stock_status_enum") == "low":
                status = "low_stock"

            if status:
                ingredient_meta = next((i for i in all_ingredients_meta if i["ingredient_id"] == ingredient_id), {})
                problem_items.append({
                    "ingredient_id": ingredient_id,
                    "ingredient_name": ingredient_meta.get("ingredient_name", "Unknown"),
                    "status": status
                })

        # 4. Reply
        return _build_success_response(problem_items)
