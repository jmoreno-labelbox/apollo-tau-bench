import json
from typing import Any, Dict, List, Set
from datetime import datetime, timedelta

from domains.dto import Tool


# Meal Plan Tools
class CreateMealPlan(Tool):
    """Creates a new meal plan for a household."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        week_start_date = kwargs.get("week_start_date")
        created_by_user_id = kwargs.get("created_by_user_id")

        meal_plans = data.get("meal_plans", [])
        # Automatically generate the next meal_plan_id
        new_id = max([plan.get("meal_plan_id", 0) for plan in meal_plans]) + 1 if meal_plans else 6001

        new_plan = {
            "meal_plan_id": new_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "2025-08-20T11:00:00Z" # Using a fixed timestamp for consistency
        }
        data["meal_plans"].append(new_plan)
        return json.dumps(new_plan)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_meal_plan",
                "description": "Creates a new meal plan for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string", "description": "Start date of the week in YYYY-MM-DD format."},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "created_by_user_id"],
                },
            },
        }

class AddRecipeToMealPlan(Tool):
    """Adds a recipe entry to an existing meal plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        plan_date = kwargs.get("plan_date")
        recipe_id = kwargs.get("recipe_id")
        meal_type = kwargs.get("meal_type", "Dinner")
        servings_adult = kwargs.get("servings_adult", 2)
        servings_child = kwargs.get("servings_child", 1)
        notes = kwargs.get("notes", "")

        entries = data.get("meal_plan_entries", [])
        # Automatically generate the next entry_id
        new_id = max([entry.get("entry_id", 0) for entry in entries]) + 1 if entries else 6101

        new_entry = {
            "entry_id": new_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes
        }
        data["meal_plan_entries"].append(new_entry)
        return json.dumps(new_entry)
        
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_recipe_to_meal_plan",
                "description": "Adds a recipe entry to an existing meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "plan_date": {"type": "string", "description": "Date for the meal in YYYY-MM-DD format."},
                        "recipe_id": {"type": "integer"},
                        "notes": {"type": "string", "description": "Optional notes for the meal entry."},
                    },
                    "required": ["meal_plan_id", "plan_date", "recipe_id"],
                },
            },
        }
        
# Grocery List Tools
class CreateGroceryListFromMealPlan(Tool):
    """Generates a grocery list from a meal plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        meal_plan_id = kwargs.get("meal_plan_id")
        user_id = kwargs.get("user_id")

        lists = data.get("grocery_lists", [])
        # Automatically generate the next list_id
        new_id = max([l.get("list_id", 0) for l in lists]) + 1 if lists else 8001

        new_list = {
            "list_id": new_id,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id,
            "created_at": "2025-08-20T12:00:00Z", # Using a fixed timestamp for consistency
            "status_enum": "initialized"
        }
        data["grocery_lists"].append(new_list)
        return json.dumps(new_list)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_grocery_list_from_meal_plan",
                "description": "Generates a grocery list from a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "meal_plan_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                    },
                    "required": ["household_id", "meal_plan_id", "user_id"],
                },
            },
        }

class AddItemToGroceryList(Tool):
    """Adds a new item to a grocery list."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        ingredient_id = kwargs.get("ingredient_id")
        quantity = kwargs.get("quantity")
        unit = kwargs.get("unit")
        
        items = data.get("grocery_list_items", [])
        # Automatically generate the next item_id
        new_id = max([item.get("item_id", 0) for item in items]) + 1 if items else 8101
        
        ingredients = data.get("ingredients", [])
        ingredient_info = next((ing for ing in ingredients if ing["ingredient_id"] == ingredient_id), None)
        if not ingredient_info:
            return json.dumps({"error": f"Ingredient {ingredient_id} not found."})

        new_item = {
            "item_id": new_id,
            "list_id": list_id,
            "ingredient_id": ingredient_id,
            "quantity": quantity,
            "unit": unit,
            "grocery_section": ingredient_info.get("grocery_section"),
            "pantry_staple_flag": ingredient_info.get("pantry_staple_flag"),
            "overlap_last_month_flag": False
        }
        data["grocery_list_items"].append(new_item)
        return json.dumps(new_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_grocery_list",
                "description": "Adds a new item to a grocery list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                        "quantity": {"type": "number"},
                        "unit": {"type": "string"},
                    },
                    "required": ["list_id", "ingredient_id", "quantity", "unit"],
                },
            },
        }

# Order Tools
class CreateOrderFromGroceryList(Tool):
    """Creates a new order from a grocery list."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        store_id = kwargs.get("store_id")
        list_id = kwargs.get("list_id")
        subtotal_cents = kwargs.get("subtotal_cents")
        total_cents = kwargs.get("total_cents")
        
        orders = data.get("orders", [])
        # Automatically generate the next order_id
        new_id = max([order.get("order_id", 0) for order in orders]) + 1 if orders else 10001

        new_order = {
            "order_id": new_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": "placed",
            "subtotal_cents": subtotal_cents,
            "total_cents": total_cents,
            "placed_ts": "2025-08-21T09:00:00Z",
            "scheduled_slot_start_ts": "2025-08-22T18:00:00Z",
            "scheduled_slot_end_ts": "2025-08-22T20:00:00Z"
        }
        data["orders"].append(new_order)
        return json.dumps(new_order)
        
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order_from_grocery_list",
                "description": "Creates a new order from a grocery list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "subtotal_cents": {"type": "integer"},
                        "total_cents": {"type": "integer"},
                    },
                    "required": ["household_id", "store_id", "list_id", "subtotal_cents", "total_cents"],
                },
            },
        }
        
# Audit Log Tool
class AddAuditLog(Tool):
    """Adds a new entry to the audit logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        user_id = kwargs.get("user_id")
        entity_type = kwargs.get("entity_type")
        entity_id = kwargs.get("entity_id")
        action_enum = kwargs.get("action_enum")
        payload_json = kwargs.get("payload_json", {})
        
        logs = data.get("audit_logs", [])
        # Automatically generate the next audit_id
        new_id = max([log.get("audit_id", 0) for log in logs]) + 1 if logs else 12001

        new_log = {
            "audit_id": new_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "2025-08-25T11:00:05Z" # Using a fixed timestamp for consistency
        }
        data["audit_logs"].append(new_log)
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_audit_log",
                "description": "Adds a new entry to the audit logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {"type": "string", "description": "The type of entity being logged (e.g., meal_plans, orders)."},
                        "entity_id": {"type": "integer"},
                        "action_enum": {"type": "string", "description": "The action performed (e.g., create, update, delete)."},
                        "payload_json": {"type": "object", "description": "JSON object with details about the action."},
                    },
                    "required": ["household_id", "user_id", "entity_type", "entity_id", "action_enum"],
                },
            },
        }



# User and Household Tools
class GetUserByEmail(Tool):
    """Retrieves a user's details by their email address."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        users = data.get("users", [])
        for user in users:
            if user.get("email") == email:
                return json.dumps(user)
        return json.dumps({"error": f"User with email '{email}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_email",
                "description": "Retrieves a user's details by their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address of the user to find.",
                        }
                    },
                    "required": ["email"],
                },
            },
        }

class GetHouseholdByUserId(Tool):
    """Retrieves household information for a given user ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        households = data.get("households", [])
        for household in households:
            if household.get("primary_user_id") == user_id:
                return json.dumps(household)
        return json.dumps({"error": f"Household for user ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_by_user_id",
                "description": "Retrieves household information for a given user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "integer",
                            "description": "The unique ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }

class GetMembersByHouseholdId(Tool):
    """Retrieves all members for a given household ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        members = data.get("members", [])
        household_members = [member for member in members if member.get("household_id") == household_id]
        return json.dumps(household_members)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_members_by_household_id",
                "description": "Retrieves all members for a given household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        }
                    },
                    "required": ["household_id"],
                },
            },
        }

class SearchHouseholdsByName(Tool):
    """Searches for households with names containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})
        households = data.get("households", [])
        matching_households = [
            household for household in households 
            if name_query.lower() in household.get("household_name", "").lower()
        ]
        return json.dumps(matching_households)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_households_by_name",
                "description": "Searches for households with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in household names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }

# Recipe and Ingredient Tools
class SearchRecipes(Tool):
    """Searches for recipes based on various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipes = data.get("recipes", [])
        cuisine = kwargs.get("cuisine")
        meal_type = kwargs.get("meal_type")
        is_peanut_free = kwargs.get("is_peanut_free")
        results = []
        for recipe in recipes:
            match = True
            if cuisine and recipe.get("cuisine") != cuisine:
                match = False
            if meal_type and recipe.get("meal_type") != meal_type:
                match = False
            if is_peanut_free is not None and recipe.get("is_peanut_free") != is_peanut_free:
                match = False
            if match:
                results.append(recipe)
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_recipes",
                "description": "Searches for recipes based on various criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {"type": "string", "description": "The cuisine of the recipe (e.g., Italian, Mexican)."},
                        "meal_type": {"type": "string", "description": "The type of meal (e.g., Dinner, Lunch)."},
                        "is_peanut_free": {"type": "boolean", "description": "Filter for peanut-free recipes."},
                    },
                },
            },
        }

class GetRecipeDetails(Tool):
    """Retrieves the full details for a specific recipe ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipe_id = kwargs.get("recipe_id")
        recipes = data.get("recipes", [])
        for recipe in recipes:
            if recipe.get("recipe_id") == recipe_id:
                return json.dumps(recipe)
        return json.dumps({"error": f"Recipe with ID '{recipe_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_details",
                "description": "Retrieves the full details for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer", "description": "The unique ID of the recipe."}},
                    "required": ["recipe_id"],
                },
            },
        }

class GetRecipeIngredients(Tool):
    """Retrieves all ingredients for a specific recipe ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipe_id = kwargs.get("recipe_id")
        recipe_ingredients = data.get("recipe_ingredients", [])
        ingredients = [ri for ri in recipe_ingredients if ri.get("recipe_id") == recipe_id]
        return json.dumps(ingredients)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_ingredients",
                "description": "Retrieves all ingredients for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer", "description": "The unique ID of the recipe."}},
                    "required": ["recipe_id"],
                },
            },
        }
        
class SearchRecipesByTitleSubstring(Tool):
    """Searches for recipes with titles containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title_substring = kwargs.get("title_substring")
        if not title_substring:
            return json.dumps({"error": "title_substring parameter is required."})
        recipes = data.get("recipes", [])
        matching_recipes = [
            recipe for recipe in recipes 
            if title_substring.lower() in recipe.get("recipe_title", "").lower()
        ]
        return json.dumps(matching_recipes)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_recipes_by_title_substring",
                "description": "Searches for recipes with titles containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title_substring": {"type": "string", "description": "The text to search for in recipe titles."}
                    },
                    "required": ["title_substring"],
                },
            },
        }

# Inventory and Meal History Tools
class GetInventoryForHousehold(Tool):
    """Retrieves all inventory items for a given household ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        inventory = data.get("inventory_items", [])
        household_inventory = [item for item in inventory if item.get("household_id") == household_id]
        return json.dumps(household_inventory)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_for_household",
                "description": "Retrieves all inventory items for a given household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer", "description": "The unique ID of the household."}},
                    "required": ["household_id"],
                },
            },
        }

class GetMealHistoryForHousehold(Tool):
    """Retrieves the meal history for a given household ID for a specified number of past days."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        days_ago = kwargs.get("days_ago", 14)
        meal_history = data.get("meal_history", [])
        current_date = datetime.strptime("2025-08-20", "%Y-%m-%d")
        start_date = current_date - timedelta(days=days_ago)
        history = [
            h for h in meal_history 
            if h.get("household_id") == household_id and 
               datetime.strptime(h.get("plan_date"), "%Y-%m-%d") >= start_date
        ]
        return json.dumps(history)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history_for_household",
                "description": "Retrieves the meal history for a given household ID for a specified number of past days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer", "description": "The unique ID of the household."},
                        "days_ago": {"type": "integer", "description": "Number of past days to retrieve history for. Defaults to 14."},
                    },
                    "required": ["household_id"],
                },
            },
        }

# Meal Plan Tools


class GetMealPlansByHouseholdId(Tool):
    """Retrieves all meal plans for a specific household ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            return json.dumps({"error": "household_id parameter is required."})
        meal_plans = data.get("meal_plans", [])
        matching_plans = [plan for plan in meal_plans if plan.get("household_id") == household_id]
        return json.dumps(matching_plans)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plans_by_household_id",
                "description": "Retrieves all meal plans for a specific household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer", "description": "The unique ID of the household."}},
                    "required": ["household_id"],
                },
            },
        }

class SearchMealPlanEntries(Tool):
    """Searches for meal plan entries within a specific plan and date range that contain a substring in their notes."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        notes_substring = kwargs.get("notes_substring")
        if not all([meal_plan_id, start_date, end_date, notes_substring]):
            return json.dumps({"error": "meal_plan_id, start_date, end_date, and notes_substring are required parameters."})
        meal_plan_entries = data.get("meal_plan_entries", [])
        matching_entries = []
        for entry in meal_plan_entries:
            if entry.get("meal_plan_id") != meal_plan_id:
                continue
            plan_date = entry.get("plan_date", "")
            if not (start_date <= plan_date <= end_date):
                continue
            notes = entry.get("notes", "")
            if notes and notes_substring.lower() in notes.lower():
                matching_entries.append(entry)
        return json.dumps(matching_entries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_meal_plan_entries",
                "description": "Searches for meal plan entries within a specific plan and date range that contain a substring in their notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer", "description": "The unique ID of the meal plan to search within."},
                        "start_date": {"type": "string", "description": "The start date of the search range (YYYY-MM-DD)."},
                        "end_date": {"type": "string", "description": "The end date of the search range (YYYY-MM-DD)."},
                        "notes_substring": {"type": "string", "description": "The text to search for within the entry notes."},
                    },
                    "required": ["meal_plan_id", "start_date", "end_date", "notes_substring"],
                },
            },
        }

class GetMealPlanEntriesByRecipeId(Tool):
    """Retrieves all meal plan entries that use a specific recipe ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipe_id = kwargs.get("recipe_id")
        if recipe_id is None:
            return json.dumps({"error": "recipe_id parameter is required."})
        meal_plan_entries = data.get("meal_plan_entries", [])
        matching_entries = [entry for entry in meal_plan_entries if entry.get("recipe_id") == recipe_id]
        return json.dumps(matching_entries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plan_entries_by_recipe_id",
                "description": "Retrieves all meal plan entries that use a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer", "description": "The unique ID of the recipe to find in meal plans."}},
                    "required": ["recipe_id"],
                },
            },
        }

# Grocery List Tools

# Update/Delete Tools
class UpdateInventoryItemQuantity(Tool):
    """Updates the quantity of an item in the household inventory."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inv_item_id = kwargs.get("inv_item_id")
        new_quantity = kwargs.get("new_quantity")
        inventory = data.get("inventory_items", [])
        for item in inventory:
            if item.get("inv_item_id") == inv_item_id:
                item["quantity"] = new_quantity
                return json.dumps(item)
        return json.dumps({"error": f"Inventory item {inv_item_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_item_quantity",
                "description": "Updates the quantity of an item in the household inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {"type": "integer"}, "new_quantity": {"type": "number"},
                    },
                    "required": ["inv_item_id", "new_quantity"],
                },
            },
        }

class RemoveRecipeFromMealPlan(Tool):
    """Removes a recipe from a meal plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry_id = kwargs.get("entry_id")
        entries = data.get("meal_plan_entries", [])
        entry_to_remove = next((e for e in entries if e.get("entry_id") == entry_id), None)
        if entry_to_remove:
            data["meal_plan_entries"] = [e for e in entries if e.get("entry_id") != entry_id]
            return json.dumps({"status": "success", "message": f"Entry {entry_id} removed."})
        return json.dumps({"error": f"Meal plan entry {entry_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_recipe_from_meal_plan",
                "description": "Removes a recipe from a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {"entry_id": {"type": "integer"}},
                    "required": ["entry_id"],
                },
            },
        }

class SearchUsersByName(Tool):
    """Searches for users with full names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})

        users = data.get("users", [])
        
        matching_users = [
            user for user in users 
            if name_query.lower() in user.get("full_name", "").lower()
        ]
        
        return json.dumps(matching_users)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_users_by_name",
                "description": "Searches for users with full names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in user full names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchIngredientsByName(Tool):
    """Searches for ingredients with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})

        ingredients = data.get("ingredients", [])
        
        matching_ingredients = [
            ingredient for ingredient in ingredients 
            if name_query.lower() in ingredient.get("ingredient_name", "").lower()
        ]
        
        return json.dumps(matching_ingredients)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ingredients_by_name",
                "description": "Searches for ingredients with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ingredient names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }

class GetInventoryForHouseholdAndIngredientId(Tool):
    """Retrieves all inventory items for a given household ID and a specific ingredient ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        ingredient_id = kwargs.get("ingredient_id")

        if household_id is None or ingredient_id is None:
            return json.dumps({"error": "household_id and ingredient_id parameters are required."})

        inventory = data.get("inventory_items", [])
        
        household_ingredient_inventory = [
            item for item in inventory 
            if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id
        ]
        
        return json.dumps(household_ingredient_inventory)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_for_household_and_ingredient_id",
                "description": "Retrieves inventory items for a specific household and ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to find in the inventory.",
                        }
                    },
                    "required": ["household_id", "ingredient_id"],
                },
            },
        }

class SearchStoresByName(Tool):
    """Searches for stores with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})

        stores = data.get("stores", [])
        
        matching_stores = [
            store for store in stores 
            if name_query.lower() in store.get("store_name", "").lower()
        ]
        
        return json.dumps(matching_stores)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_stores_by_name",
                "description": "Searches for stores with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in store names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class AddMealHistory(Tool):
    """Adds a new entry to the meal history."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        recipe_id = kwargs.get("recipe_id")
        plan_date = kwargs.get("plan_date")
        was_prepared = kwargs.get("was_prepared")
        rating_int = kwargs.get("rating_int")

        history = data.get("meal_history", [])
        new_id = max([h.get("history_id", 0) for h in history]) + 1 if history else 6201

        new_entry = {
            "history_id": new_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int
        }
        data["meal_history"].append(new_entry)
        return json.dumps(new_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_meal_history",
                "description": "Adds a new entry to the meal history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "recipe_id": {"type": "integer"},
                        "plan_date": {"type": "string", "description": "Date the meal was planned for in YYYY-MM-DD format."},
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {"type": "integer", "description": "Rating from 1 to 5; can be null."},
                    },
                    "required": ["household_id", "recipe_id", "plan_date", "was_prepared"],
                },
            },
        }

class UpdateMealPlanEntryNotes(Tool):
    """Updates the notes for a specific meal plan entry."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry_id = kwargs.get("entry_id")
        new_notes = kwargs.get("new_notes")

        entries = data.get("meal_plan_entries", [])
        for entry in entries:
            if entry.get("entry_id") == entry_id:
                entry["notes"] = new_notes
                return json.dumps(entry)
        return json.dumps({"error": f"Meal plan entry with ID '{entry_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry_notes",
                "description": "Updates the notes for a specific meal plan entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {"type": "integer"},
                        "new_notes": {"type": "string"},
                    },
                    "required": ["entry_id", "new_notes"],
                },
            },
        }

class AddUser(Tool):
    """Adds a new user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        full_name = kwargs.get("full_name")
        users = data.get("users", [])
        if any(user.get("email") == email for user in users):
            return json.dumps({"error": f"User with email '{email}' already exists."})
        new_id = max([u.get("user_id", 0) for u in users]) + 1 if users else 101
        new_user = {
            "user_id": new_id, "email": email, "full_name": full_name,
            "created_at": "2025-08-22T10:00:00Z"
        }
        data["users"].append(new_user)
        return json.dumps(new_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_user",
                "description": "Adds a new user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "full_name": {"type": "string"},
                    },
                    "required": ["email", "full_name"],
                },
            },
        }

class AddHousehold(Tool):
    """Adds a new household."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_name = kwargs.get("household_name")
        timezone = kwargs.get("timezone")
        primary_user_id = kwargs.get("primary_user_id")
        households = data.get("households", [])
        new_id = max([h.get("household_id", 0) for h in households]) + 1 if households else 201
        new_household = {
            "household_id": new_id, "household_name": household_name,
            "timezone": timezone, "primary_user_id": primary_user_id
        }
        data["households"].append(new_household)
        return json.dumps(new_household)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_household",
                "description": "Adds a new household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_name": {"type": "string"},
                        "timezone": {"type": "string"},
                        "primary_user_id": {"type": "integer"},
                    },
                    "required": ["household_name", "timezone", "primary_user_id"],
                },
            },
        }

class AddMember(Tool):
    """Adds a new member to a household."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        full_name = kwargs.get("full_name")
        birthdate = kwargs.get("birthdate")
        is_child = kwargs.get("is_child")
        members = data.get("members", [])
        new_id = max([m.get("member_id", 0) for m in members]) + 1 if members else 301
        new_member = {
            "member_id": new_id, "household_id": household_id, "full_name": full_name,
            "birthdate": birthdate, "is_child": is_child, "activity_level": "medium",
            "dietary_notes": "", "allergies_json": ["none"], "target_calories": 1400, "target_protein": 35
        }
        data["members"].append(new_member)
        return json.dumps(new_member)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_member",
                "description": "Adds a new member to a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                        "birthdate": {"type": "string", "description": "YYYY-MM-DD format."},
                        "is_child": {"type": "boolean"},
                    },
                    "required": ["household_id", "full_name", "birthdate", "is_child"],
                },
            },
        }

class GetGroceryListsByHouseholdId(Tool):
    """Retrieves all grocery lists for a specific household ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            return json.dumps({"error": "household_id parameter is required."})

        grocery_lists = data.get("grocery_lists", [])
        
        matching_lists = [
            glist for glist in grocery_lists 
            if glist.get("household_id") == household_id
        ]
        
        return json.dumps(matching_lists)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_lists_by_household_id",
                "description": "Retrieves all grocery lists for a specific household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        }
                    },
                    "required": ["household_id"],
                },
            },
        }

class GetMealHistoryByHouseholdAndDate(Tool):
    """Retrieves meal history for a specific household on a given date."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        plan_date = kwargs.get("plan_date")

        if household_id is None or plan_date is None:
            return json.dumps({"error": "household_id and plan_date parameters are required."})

        meal_history = data.get("meal_history", [])
        
        matching_history = [
            entry for entry in meal_history 
            if entry.get("household_id") == household_id and entry.get("plan_date") == plan_date
        ]
        
        return json.dumps(matching_history)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history_by_household_and_date",
                "description": "Retrieves meal history for a specific household on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date of the meal plan entry in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["household_id", "plan_date"],
                },
            },
        }


class RemoveItemFromGroceryList(Tool):
    """Removes an item from a grocery list by its item ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("item_id")
        if item_id is None:
            return json.dumps({"error": "item_id parameter is required."})

        items = data.get("grocery_list_items", [])
        original_count = len(items)
        # Filter out the item with the matching ID
        data["grocery_list_items"] = [item for item in items if item.get("item_id") != item_id]

        if len(data["grocery_list_items"]) < original_count:
            return json.dumps({"status": "success", "message": f"Item {item_id} removed from grocery list."})
        else:
            return json.dumps({"error": f"Item with ID '{item_id}' not found on any grocery list."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_item_from_grocery_list",
                "description": "Removes an item from a grocery list by its item ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "integer",
                            "description": "The unique ID of the grocery list item to remove.",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }

class UpdateMealHistory(Tool):
    """Updates an entry in the meal history, such as its preparation status or rating."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        history_id = kwargs.get("history_id")
        was_prepared = kwargs.get("was_prepared")
        rating_int = kwargs.get("rating_int")

        if history_id is None:
            return json.dumps({"error": "history_id parameter is required."})

        history = data.get("meal_history", [])
        for entry in history:
            if entry.get("history_id") == history_id:
                if was_prepared is not None:
                    entry["was_prepared"] = was_prepared
                if rating_int is not None:
                    entry["rating_int"] = rating_int
                return json.dumps(entry)
        
        return json.dumps({"error": f"Meal history entry with ID '{history_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_history",
                "description": "Updates an entry in the meal history, such as its preparation status or rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "history_id": {"type": "integer"},
                        "was_prepared": {"type": "boolean", "description": "Set to true if the meal was prepared."},
                        "rating_int": {"type": "integer", "description": "Rating from 1 to 5, can be null."},
                    },
                    "required": ["history_id"],
                },
            },
        }


class GetGroceryListItemsByListIdAndIngredientId(Tool):
    """Retrieves grocery list items from a specific list that match a given ingredient ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        ingredient_id = kwargs.get("ingredient_id")

        if list_id is None or ingredient_id is None:
            return json.dumps({"error": "list_id and ingredient_id parameters are required."})

        grocery_list_items = data.get("grocery_list_items", [])
        
        matching_items = [
            item for item in grocery_list_items 
            if item.get("list_id") == list_id and item.get("ingredient_id") == ingredient_id
        ]
        
        return json.dumps(matching_items)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_items_by_list_id_and_ingredient_id",
                "description": "Retrieves grocery list items from a specific list that match a given ingredient ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID of the grocery list.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to find on the list.",
                        }
                    },
                    "required": ["list_id", "ingredient_id"],
                },
            },
        }

TOOLS = [
    CreateMealPlan(),
    AddRecipeToMealPlan(),
    CreateGroceryListFromMealPlan(),
    AddItemToGroceryList(),
    CreateOrderFromGroceryList(),
    AddAuditLog(),
    GetUserByEmail(),
    GetHouseholdByUserId(),
    GetMembersByHouseholdId(),
    SearchHouseholdsByName(),
    SearchRecipes(),
    GetRecipeDetails(),
    GetRecipeIngredients(),
    SearchRecipesByTitleSubstring(),
    GetInventoryForHousehold(),
    GetMealHistoryForHousehold(),
    GetMealPlansByHouseholdId(),
    SearchMealPlanEntries(),
    GetMealPlanEntriesByRecipeId(),
    UpdateInventoryItemQuantity(),
    RemoveRecipeFromMealPlan(),
    SearchUsersByName(),
    SearchIngredientsByName(),
    GetInventoryForHouseholdAndIngredientId(),
    SearchStoresByName(),
    AddMealHistory(),
    UpdateMealPlanEntryNotes(),
    AddUser(),
    AddHousehold(),
    AddMember(),
    GetGroceryListsByHouseholdId(),
    GetMealHistoryByHouseholdAndDate(),
    RemoveItemFromGroceryList(),
    UpdateMealHistory(),
    GetGroceryListItemsByListIdAndIngredientId(),
]



