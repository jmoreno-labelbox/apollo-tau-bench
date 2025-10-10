# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveItemFromInventoryTool(Tool):
    """
    A tool to explicitly remove an item from a household's inventory.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "remove_item_from_inventory",
                "description": (
                    "Explicitly removes an entire item from inventory. Useful for scenarios "
                    "like discarding expired food. Identify the item either by its unique 'inv_item_id' "
                    "or by the combination of 'household_id' and 'ingredient_id'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {
                            "type": "integer",
                            "description": "The unique ID of the inventory item to remove."
                        },
                        "household_id": {
                            "type": "integer",
                            "description": "The household ID, used with ingredient_id if inv_item_id is absent."
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The ingredient ID, used with household_id if inv_item_id is absent."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": [],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to find and explicitly remove an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the item that was removed.
        """
        # 1. Validate Input Types
        param_definitions = {
            "inv_item_id": {"type": int, "required": False},
            "household_id": {"type": int, "required": False},
            "ingredient_id": {"type": int, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        inv_item_id = kwargs.get("inv_item_id")
        household_id = kwargs.get("household_id")
        ingredient_id = kwargs.get("ingredient_id")
        user_id = kwargs.get("user_id")

        # 2. Specific Validation: Ensure at least one identification method is provided
        if not inv_item_id and not (household_id and ingredient_id):
            return _build_error_response("REQUIRED_PARAMETER", {"param": "'inv_item_id' or both 'household_id' and 'ingredient_id'"})

        # 3. Find the item to remove
        inventory_table = data.get("inventory_items", [])
        item_to_remove = None
        if inv_item_id:
            item_to_remove = next((item for item in inventory_table if item.get("inv_item_id") == inv_item_id), None)
        else:
            item_to_remove = next((item for item in inventory_table if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id), None)

        if not item_to_remove:
            return _build_error_response("NOT_FOUND", {"entity": "Inventory Item", "entity_id": inv_item_id or f"for ingredient {ingredient_id}"})

        # 4. Auditing (before the data is removed)
        item_id_to_remove = item_to_remove["inv_item_id"]
        _log_audit_event(
            data=data,
            household_id=item_to_remove.get("household_id"),
            user_id=user_id,
            entity_type="inventory_items",
            entity_id=item_id_to_remove,
            action_enum="delete",
            payload_json=item_to_remove # Log the full record being deleted
        )

        # 5. Perform the removal
        data["inventory_items"] = [item for item in inventory_table if item.get("inv_item_id") != item_id_to_remove]

        # 6. Response
        return _build_success_response({
            "status": "success",
            "removed_item": item_to_remove
        })
