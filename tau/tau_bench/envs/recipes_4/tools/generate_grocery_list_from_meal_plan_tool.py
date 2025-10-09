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

class GenerateGroceryListFromMealPlanTool(Tool):
    """
    A tool to create an optimized grocery list from a meal plan and inventory.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GenerateGroceryListFromMealPlan",
                "description": (
                    "Creates a new grocery list by calculating ingredients needed for a meal plan, "
                    "subtracting items already in the household's inventory."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan.",
                        },
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household the plan belongs to.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the list, for auditing.",
                        },
                    },
                    "required": ["meal_plan_id", "household_id", "user_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int, household_id: int, user_id: int) -> dict[str, Any]:
        """
        Executes the logic to generate an optimized grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            meal_plan_id: The ID of the meal plan.
            household_id: The ID of the household.
            user_id: The ID of the user.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the ID of the new list and its item IDs.
        """
        pass
        #1. Validate Inputs
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True},
            "household_id": {"type": int, "required": True},
            "user_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs({"meal_plan_id": meal_plan_id, "household_id": household_id, "user_id": user_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        meal_plan = next(
            (
                p
                for p in data.get("meal_plans", {}).values()
                if p.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )
        if not meal_plan:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id}
            )
        if meal_plan.get("household_id") != household_id:
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Generate List",
                    "entity": "MealPlan does not belong to the specified household.",
                },
            )

        #3. Core Logic: Calculate Net Needs
        all_ingredients_meta = data.get("ingredients", {}).values()
        context = {"ingredients": all_ingredients_meta}

        #3a. Aggregate all required ingredients for the plan, normalizing units
        plan_entries = [
            e
            for e in data.get("meal_plan_entries", {}).values()
            if e.get("meal_plan_id") == meal_plan_id
        ]
        recipe_ids = {e["recipe_id"] for e in plan_entries}
        required_ingredients_list = [
            ri
            for ri in data.get("recipe_ingredients", {}).values()
            if ri["recipe_id"] in recipe_ids
        ]

        required_totals = collections.defaultdict(float)
        for req in required_ingredients_list:
            normalized_req = _normalize_domain_data("unit_measurement", req, context)
            required_totals[normalized_req["ingredient_id"]] += normalized_req[
                "quantity"
            ]

        #3b. Get available inventory, normalizing units
        inventory_items = [
            i
            for i in data.get("inventory_items", {}).values()
            if i.get("household_id") == household_id
        ]
        available_totals = collections.defaultdict(float)
        for item in inventory_items:
            normalized_item = _normalize_domain_data("unit_measurement", item, context)
            available_totals[normalized_item["ingredient_id"]] += normalized_item[
                "quantity"
            ]

        #3c. Calculate what needs to be bought
        net_needed_items = []
        for ingredient_id, required_qty in required_totals.items():
            needed_qty = required_qty - available_totals.get(ingredient_id, 0)
            if needed_qty > 0:
                ingredient_meta = next(
                    (
                        i
                        for i in all_ingredients_meta.values() if i["ingredient_id"] == ingredient_id
                    ),
                    {},
                )
                net_needed_items.append(
                    {
                        "ingredient_id": ingredient_id,
                        "quantity": round(needed_qty, 2),
                        "unit": ingredient_meta.get("default_unit", "units"),
                        "grocery_section": ingredient_meta.get(
                            "grocery_section", "Misc"
                        ),
                        "pantry_staple_flag": ingredient_meta.get(
                            "pantry_staple_flag", False
                        ),
                    }
                )

        #4. Create Grocery List and Items
        gl_table = data.setdefault("grocery_lists", [])
        max_list_id = max(
            (g.get("list_id", 0) for g in gl_table.values()),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_lists"],
        )
        new_list_id = max_list_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        new_list_record = {
            "list_id": new_list_id,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id,
            "created_at": timestamp,
            "status_enum": "initialized",
        }
        gl_table.append(new_list_record)

        gli_table = data.setdefault("grocery_list_items", [])
        max_item_id = max(
            (i.get("item_id", 0) for i in gli_table.values()),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_list_items"],
        )
        created_item_ids = []

        for item in net_needed_items:
            max_item_id += 1
            new_item_record = {
                "item_id": max_item_id,
                "list_id": new_list_id,
                "overlap_last_month_flag": False,
                **item,
            }
            gli_table.append(new_item_record)
            created_item_ids.append(max_item_id)

        #5. Auditing
        _log_audit_event(
            data,
            household_id=household_id,
            user_id=user_id,
            entity_type="grocery_lists",
            entity_id=new_list_id,
            action_enum="create",
            payload_json={"source_meal_plan_id": meal_plan_id},
        )

        #6. Response
        return _build_success_response(
            {
                "list_id": new_list_id,
                "items_added_count": len(created_item_ids),
                "created_item_ids": created_item_ids,
            }
        )
