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

class UseItemFromInventoryTool(Tool):
    """
    A tool to decrease the quantity of an item in a household's inventory.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UseItemFromInventory",
                "description": (
                    "Decreases the quantity of a specific ingredient in a household's inventory. "
                    "If the used quantity is greater than or equal to the available quantity, the item is removed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to use.",
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient that was used.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "ingredient_id", "quantity"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        ingredient_id: int,
        quantity: float,
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to consume an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household.
            ingredient_id: The ID of the ingredient.
            quantity: The quantity to be used.
            user_id: The ID of the user (optional).

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the updated item or a removal confirmation.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "user_id": user_id,
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        inventory_table = data.get("inventory_items", [])

        #2. Find the item in inventory
        item_to_use = next(
            (
                item
                for item in inventory_table
                if item.get("household_id") == household_id
                and item.get("ingredient_id") == ingredient_id
            ),
            None,
        )

        if not item_to_use:
            return _build_error_response(
                "NOT_FOUND",
                {
                    "entity": "Inventory Item",
                    "entity_id": f"for ingredient {ingredient_id}",
                },
            )

        #3. Logic: Decrement quantity or remove item
        current_quantity = item_to_use.get("quantity", 0)
        item_id = item_to_use.get("inv_item_id")

        payload = {"ingredient_id": ingredient_id, "quantity_used": quantity}

        if quantity >= current_quantity:
            #Item is fully consumed
            action = "delete"
            #Log a copy of the item before it's deleted
            _log_audit_event(
                data=data,
                household_id=household_id,
                user_id=user_id,
                entity_type="inventory_items",
                entity_id=item_id,
                action_enum=action,
                payload_json=payload,
            )
            #Rebuild the list without the removed item
            data["inventory_items"] = [
                item for item in inventory_table if item.get("inv_item_id") != item_id
            ]
            response_data = {"status": "item_removed", "removed_item": item_to_use}
        else:
            #Item is partially consumed
            action = "update"
            item_to_use["quantity"] -= quantity
            _log_audit_event(
                data=data,
                household_id=household_id,
                user_id=user_id,
                entity_type="inventory_items",
                entity_id=item_id,
                action_enum=action,
                payload_json=payload,
            )
            response_data = item_to_use

        #4. Response
        return _build_success_response(response_data)
