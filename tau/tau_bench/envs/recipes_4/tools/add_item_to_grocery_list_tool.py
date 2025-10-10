# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddItemToGroceryListTool(Tool):
    """
    A tool to add a single item to an existing grocery list.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_grocery_list",
                "description": (
                    "Adds a single ingredient to a grocery list. If the ingredient already "
                    "exists on the list, its quantity is updated. Otherwise, a new item is created."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to modify."
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to add."
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient to add."
                        },
                        "unit": {
                            "type": "string",
                            "description": "The unit of measurement for the quantity."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["list_id", "ingredient_id", "quantity", "unit"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], ingredient_id, list_id, quantity, unit, user_id) -> Dict[str, Any]:
        """
        Executes the logic to add or update a grocery list item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the final state of the grocery list item.
        """
        # 1. Verify Input Data
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "unit": {"type": str, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Validation of Preconditions
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})
        ingredient_meta = next((i for i in list(data.get("ingredients", {}).values()) if i.get("ingredient_id") == ingredient_id), None)
        if not ingredient_meta:
            return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id})

        # 3. Logic: Locate current item or set up for creation
        gli_table = data.setdefault("grocery_list_items", [])
        existing_item = next(
            (item for item in gli_table if item.get("list_id") == list_id and item.get("ingredient_id") == ingredient_id),
            None
        )

        list_record = next(g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id)
        household_id = list_record.get("household_id")

        if existing_item:
            # Modify current item
            action = "update"
            # To simplify, we assume compatible units and directly sum the quantities.
            # An enhanced normalizer could manage unit conversions.
            existing_item["quantity"] += quantity
            final_record = existing_item
            entity_id = existing_item["item_id"]
        else:
            # Generate a new item.
            action = "create"
            max_id = max((i.get("item_id", 0) for i in gli_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_list_items"])
            new_item_id = max_id + 1

            new_record = {
                "item_id": new_item_id,
                "list_id": list_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "unit": unit,
                "grocery_section": ingredient_meta.get("grocery_section", "Misc"),
                "pantry_staple_flag": ingredient_meta.get("pantry_staple_flag", False),
                "overlap_last_month_flag": False # Indeterminate at this point.
            }
            gli_table.append(new_record)
            final_record = new_record
            entity_id = new_item_id

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="grocery_list_items",
            entity_id=entity_id,
            action_enum=action,
            payload_json={"ingredient_id": ingredient_id, "quantity_added": quantity, "unit": unit}
        )

        # 5. Reply
        return _build_success_response(final_record)
