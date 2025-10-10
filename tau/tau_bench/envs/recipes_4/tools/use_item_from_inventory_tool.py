# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UseItemFromInventoryTool(Tool):
    """
    A tool to decrease the quantity of an item in a household's inventory.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "use_item_from_inventory",
                "description": (
                    "Decreases the quantity of a specific ingredient in a household's inventory. "
                    "If the used quantity is greater than or equal to the available quantity, the item is removed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household."
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to use."
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient that was used."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["household_id", "ingredient_id", "quantity"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, ingredient_id, quantity, user_id) -> Dict[str, Any]:
        """
        Executes the logic to consume an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the updated item or a removal confirmation.
        """
        # 1. Verify Input Data
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])
        quantity_used = quantity

        inventory_table = data.get("inventory_items", [])

        # Locate the item in stock.
        item_to_use = next(
            (item for item in inventory_table if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id),
            None
        )

        if not item_to_use:
            return _build_error_response("NOT_FOUND", {"entity": "Inventory Item", "entity_id": f"for ingredient {ingredient_id}"})

        # 3. Functionality: Reduce quantity or eliminate item
        current_quantity = item_to_use.get("quantity", 0)
        item_id = item_to_use.get("inv_item_id")

        payload = {"ingredient_id": ingredient_id, "quantity_used": quantity_used}

        if quantity_used >= current_quantity:
            # Item has been completely utilized.
            action = "delete"
            # Record a duplicate of the item prior to its removal.
            _log_audit_event(
                data=data, household_id=household_id, user_id=user_id, entity_type="inventory_items",
                entity_id=item_id, action_enum=action, payload_json=payload
            )
            # Reconstruct the list excluding the deleted item.
            data["inventory_items"] = [item for item in inventory_table if item.get("inv_item_id") != item_id]
            response_data = {"status": "item_removed", "removed_item": item_to_use}
        else:
            # Item has been partially utilized.
            action = "update"
            item_to_use["quantity"] -= quantity_used
            _log_audit_event(
                data=data, household_id=household_id, user_id=user_id, entity_type="inventory_items",
                entity_id=item_id, action_enum=action, payload_json=payload
            )
            response_data = item_to_use

        # 4. Reply
        return _build_success_response(response_data)
