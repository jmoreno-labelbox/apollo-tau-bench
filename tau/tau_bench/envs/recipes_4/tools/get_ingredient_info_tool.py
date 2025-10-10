# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetIngredientInfoTool(Tool):
    """
    A tool to retrieve the full data record for a single ingredient.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_ingredient_info",
                "description": "Retrieves the full data record for a single ingredient by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique identifier for the ingredient to retrieve."
                        },
                    },
                    "required": ["ingredient_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to find and return a specific ingredient's data.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects a required
                      'ingredient_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the ingredient object. On failure,
            it contains a structured error object.
        """
        # 1. Validate Inputs
        param_definitions = {
            "ingredient_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        ingredient_id = kwargs["ingredient_id"]

        # 2. Data Retrieval
        ingredient_record = next(
            (i for i in list(data.get("ingredients", {}).values()) if i.get("ingredient_id") == ingredient_id),
            None
        )

        # 3. Handle not found cases
        if not ingredient_record:
            return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id})

        # 4. Return a standardized success response
        return _build_success_response(ingredient_record)
