from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any

class AddItemToInventoryTool(Tool):
    """
    A tool to add an item to a household's inventory or update its quantity.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddItemToInventory",
                "description": (
                    "Adds an item to a household's inventory. If the ingredient already exists, "
                    "it updates the quantity. Otherwise, it creates a new inventory entry."
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
                            "description": "The unique ID of the ingredient to add.",
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient to add.",
                        },
                        "unit": {
                            "type": "string",
                            "description": "The unit of measurement for the quantity.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "ingredient_id", "quantity", "unit"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        ingredient_id: int,
        quantity: float,
        unit: str,
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to add or update an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household.
            ingredient_id: The ID of the ingredient.
            quantity: The quantity of the ingredient.
            unit: The unit of measurement for the quantity.
            user_id: The ID of the user (optional).

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the final state of the inventory item.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "unit": {"type": str, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "unit": unit,
                "user_id": user_id,
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(
            h.get("household_id") == household_id for h in data.get("households", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )
        if not any(
            i.get("ingredient_id") == ingredient_id for i in data.get("ingredients", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id}
            )

        #3. Logic: Find existing item or prepare for creation
        inventory_table = data.setdefault("inventory_items", [])
        existing_item = next(
            (
                item
                for item in inventory_table
                if item.get("household_id") == household_id
                and item.get("ingredient_id") == ingredient_id
            ),
            None,
        )

        context = {"ingredients": data.get("ingredients", [])}

        if existing_item:
            action = "update"
            normalized_addition = _normalize_domain_data(
                "unit_measurement",
                {"ingredient_id": ingredient_id, "quantity": quantity, "unit": unit},
                context,
            )

            normalized_existing = _normalize_domain_data(
                "unit_measurement", existing_item, context
            )

            #Now that both are in the standard unit, we can safely add them
            new_total_quantity = (
                normalized_existing["quantity"] + normalized_addition["quantity"]
            )

            existing_item["quantity"] = round(new_total_quantity, 2)
            existing_item["unit"] = normalized_existing[
                "unit"
            ]  #Store in the standard unit

            final_record = existing_item
            entity_id = existing_item["inv_item_id"]
        else:
            #Create new item (normalize the input for consistency)
            action = "create"
            normalized_input = _normalize_domain_data(
                "unit_measurement",
                {"ingredient_id": ingredient_id, "quantity": quantity, "unit": unit},
                context,
            )

            max_id = max(
                (i.get("inv_item_id", 0) for i in inventory_table), default=7000
            )
            new_item_id = max_id + 1

            new_record = {
                "inv_item_id": new_item_id,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": normalized_input["quantity"],
                "unit": normalized_input["unit"],
                "location_enum": "pantry",  #Default location
                "best_by_date": None,
            }
            inventory_table.append(new_record)
            final_record = new_record
            entity_id = new_item_id

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="inventory_items",
            entity_id=entity_id,
            action_enum=action,
            payload_json={
                "ingredient_id": ingredient_id,
                "quantity_added": quantity,
                "unit": unit,
            },
        )

        #5. Response
        return _build_success_response(final_record)
