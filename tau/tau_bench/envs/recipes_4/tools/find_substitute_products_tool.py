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

class FindSubstituteProductsTool(Tool):
    """
    A tool to find available in-stock substitutes for out-of-stock items.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindSubstituteProducts",
                "description": (
                    "For a given list of out-of-stock or low-stock ingredients at a specific store, "
                    "suggests available in-stock products as substitutes based on a predefined knowledge base."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store where the check is being performed.",
                        },
                        "problem_items": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "The list of items with stock issues, from the 'check_product_availability_at_store' tool.",
                        },
                    },
                    "required": ["store_id", "problem_items"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], store_id: int, problem_items: list) -> dict[str, Any]:
        """
        Executes the logic to find viable, in-stock substitute products.

        Args:
            data: The main in-memory dictionary containing all datasets.
            store_id: The ID of the store.
            problem_items: A list of problem items.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of substitution suggestions.
        """
        #1. Validate Inputs
        param_definitions = {
            "store_id": {"type": int, "required": True},
            "problem_items": {"type": list, "required": True},
        }
        validation_error = _validate_inputs({"store_id": store_id, "problem_items": problem_items}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check
        if not any(s.get("store_id") == store_id for s in data.get("stores", {}).values()):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Store", "entity_id": store_id}
            )

        #3. Core Logic
        suggestions = []
        all_store_products = data.get("store_products", {}).values()

        for item in problem_items:
            original_ingredient_id = item.get("ingredient_id")

            #Find substitution rules for the problematic ingredient
            substitute_options = INGREDIENT_SUBSTITUTE_MAP.get(
                original_ingredient_id, []
            )

            for sub_ingredient_id in substitute_options:
                #Find all products for the substitute ingredient at the store
                candidate_products = [
                    p
                    for p in all_store_products.values() if p.get("store_id") == store_id
                    and p.get("ingredient_id") == sub_ingredient_id
                ]

                #Find the best available option (in stock and cheapest)
                in_stock_products = [
                    p
                    for p in candidate_products
                    if p.get("stock_status_enum") in ("in_stock", "low")
                ]

                if in_stock_products:
                    best_sub_product = min(
                        in_stock_products,
                        key=lambda p: p.get("price_cents", float("inf")),
                    )

                    suggestions.append(
                        {
                            "original_ingredient_id": original_ingredient_id,
                            "substitute_ingredient_id": sub_ingredient_id,
                            "substitute_product_id": best_sub_product["product_id"],
                            "substitute_product_name": best_sub_product.get(
                                "product_name"
                            ),
                            "price_cents": best_sub_product.get("price_cents"),
                        }
                    )
                    #Found a valid substitute, stop searching for this item
                    break

        #4. Response
        return _build_success_response(suggestions)
