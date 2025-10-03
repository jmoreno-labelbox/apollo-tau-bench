import json
from datetime import datetime, timedelta
from typing import Any

from domains.dto import Tool


#Meal Planning Tools
class CreateMealPlan(Tool):
    """Establishes a new meal plan for a family."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, week_start_date: str = None, created_by_user_id: int = None) -> str:
        meal_plans = data.get("meal_plans", [])
        # Automatically create the subsequent meal_plan_id
        new_id = (
            max([plan.get("meal_plan_id", 0) for plan in meal_plans]) + 1
            if meal_plans
            else 6001
        )

        new_plan = {
            "meal_plan_id": new_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "2025-08-20T11:00:00Z",  # Employing a constant timestamp for uniformity
        }
        data["meal_plans"].append(new_plan)
        payload = new_plan
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Creates a new meal plan for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {
                            "type": "string",
                            "description": "Start date of the week in YYYY-MM-DD format.",
                        },
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "created_by_user_id",
                    ],
                },
            },
        }


class AddRecipeToMealPlan(Tool):
    """Incorporates a recipe entry into a current meal plan."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        plan_date: str,
        recipe_id: int,
        meal_type: str = "Dinner",
        servings_adult: int = 2,
        servings_child: int = 1,
        notes: str = ""
    ) -> str:
        entries = data.get("meal_plan_entries", [])
        # Automatically create the next entry_id
        new_id = (
            max([entry.get("entry_id", 0) for entry in entries]) + 1
            if entries
            else 6101
        )

        new_entry = {
            "entry_id": new_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes,
        }
        data["meal_plan_entries"].append(new_entry)
        payload = new_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRecipeToMealPlan",
                "description": "Adds a recipe entry to an existing meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "plan_date": {
                            "type": "string",
                            "description": "Date for the meal in YYYY-MM-DD format.",
                        },
                        "recipe_id": {"type": "integer"},
                        "notes": {
                            "type": "string",
                            "description": "Optional notes for the meal entry.",
                        },
                    },
                    "required": ["meal_plan_id", "plan_date", "recipe_id"],
                },
            },
        }


#Grocery Planning Tools
class CreateGroceryListFromMealPlan(Tool):
    """Creates a shopping list based on a meal plan."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, meal_plan_id: int = None, user_id: int = None) -> str:
        lists = data.get("grocery_lists", [])
        # Automatically create the next list_id
        new_id = max([l.get("list_id", 0) for l in lists]) + 1 if lists else 8001

        new_list = {
            "list_id": new_id,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id,
            "created_at": "2025-08-20T12:00:00Z",  # Utilizing a stable timestamp for consistency
            "status_enum": "initialized",
        }
        data["grocery_lists"].append(new_list)
        payload = new_list
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateGroceryListFromMealPlan",
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
    """Inserts a new item into a grocery list."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, ingredient_id: int = None, quantity: float = None, unit: str = None) -> str:
        items = data.get("grocery_list_items", [])
        # Automatically create the next item_id
        new_id = max([item.get("item_id", 0) for item in items]) + 1 if items else 8101

        ingredients = data.get("ingredients", [])
        ingredient_info = next(
            (ing for ing in ingredients if ing["ingredient_id"] == ingredient_id), None
        )
        if not ingredient_info:
            payload = {"error": f"Ingredient {ingredient_id} not found."}
            out = json.dumps(payload)
            return out

        new_item = {
            "item_id": new_id,
            "list_id": list_id,
            "ingredient_id": ingredient_id,
            "quantity": quantity,
            "unit": unit,
            "grocery_section": ingredient_info.get("grocery_section"),
            "pantry_staple_flag": ingredient_info.get("pantry_staple_flag"),
            "overlap_last_month_flag": False,
        }
        data["grocery_list_items"].append(new_item)
        payload = new_item
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddItemToGroceryList",
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


#Ordering Tools
class CreateOrderFromGroceryList(Tool):
    """Forms a new order based on a grocery list."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        store_id: int = None,
        list_id: int = None,
        subtotal_cents: int = None,
        total_cents: int = None
    ) -> str:
        orders = data.get("orders", [])
        # Automatically create the next order_id
        new_id = (
            max([order.get("order_id", 0) for order in orders]) + 1 if orders else 10001
        )

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
            "scheduled_slot_end_ts": "2025-08-22T20:00:00Z",
        }
        data["orders"].append(new_order)
        payload = new_order
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateOrderFromGroceryList",
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
                    "required": [
                        "household_id",
                        "store_id",
                        "list_id",
                        "subtotal_cents",
                        "total_cents",
                    ],
                },
            },
        }


#Audit Logging Tool
class AddAuditLog(Tool):
    """Inserts a new record into the audit logs."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int, user_id: int, entity_type: str, entity_id: int, action_enum: str, payload_json: dict = {}) -> str:
        logs = data.get("audit_logs", [])
        # Automatically create the next audit_id
        new_id = max([log.get("audit_id", 0) for log in logs]) + 1 if logs else 12001

        new_log = {
            "audit_id": new_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "2025-08-25T11:00:05Z",  # Applying a fixed timestamp for reliability
        }
        data["audit_logs"].append(new_log)
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddAuditLog",
                "description": "Adds a new entry to the audit logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {
                            "type": "string",
                            "description": "The type of entity being logged (e.g., meal_plans, orders).",
                        },
                        "entity_id": {"type": "integer"},
                        "action_enum": {
                            "type": "string",
                            "description": "The action performed (e.g., create, update, delete).",
                        },
                        "payload_json": {
                            "type": "object",
                            "description": "JSON object with details about the action.",
                        },
                    },
                    "required": [
                        "household_id",
                        "user_id",
                        "entity_type",
                        "entity_id",
                        "action_enum",
                    ],
                },
            },
        }


#User and Family Tools
class GetUserByEmail(Tool):
    """Fetches a user's information using their email address."""

    @staticmethod
    def invoke(data: dict[str, Any], email: str = None) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("email") == email:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with email '{email}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUserByEmail",
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
    """Obtains household details for a specified user ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        households = data.get("households", [])
        for household in households:
            if household.get("primary_user_id") == user_id:
                payload = household
                out = json.dumps(payload)
                return out
        payload = {"error": f"Household for user ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdByUserId",
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
    """Fetches all members associated with a specific household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        members = data.get("members", [])
        household_members = [
            member for member in members if member.get("household_id") == household_id
        ]
        payload = household_members
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMembersByHouseholdId",
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
    """Looks for households whose names include the given text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out
        households = data.get("households", [])
        matching_households = [
            household
            for household in households
            if name_query.lower() in household.get("household_name", "").lower()
        ]
        payload = matching_households
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchHouseholdsByName",
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


#Recipe and Component Tools
class SearchRecipes(Tool):
    """Looks for recipes according to different parameters."""

    @staticmethod
    def invoke(data: dict[str, Any], cuisine: str = None, meal_type: str = None, is_peanut_free: bool = None) -> str:
        recipes = data.get("recipes", [])
        results = []
        for recipe in recipes:
            match = True
            if cuisine and recipe.get("cuisine") != cuisine:
                match = False
            if meal_type and recipe.get("meal_type") != meal_type:
                match = False
            if (
                is_peanut_free is not None
                and recipe.get("is_peanut_free") != is_peanut_free
            ):
                match = False
            if match:
                results.append(recipe)
        payload = results
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchRecipes",
                "description": "Searches for recipes based on various criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {
                            "type": "string",
                            "description": "The cuisine of the recipe (e.g., Italian, Mexican).",
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The type of meal (e.g., Dinner, Lunch).",
                        },
                        "is_peanut_free": {
                            "type": "boolean",
                            "description": "Filter for peanut-free recipes.",
                        },
                    },
                },
            },
        }


class GetRecipeDetails(Tool):
    """Fetches complete information for a particular recipe ID."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        recipes = data.get("recipes", [])
        for recipe in recipes:
            if recipe.get("recipe_id") == recipe_id:
                payload = recipe
                out = json.dumps(payload)
                return out
        payload = {"error": f"Recipe with ID '{recipe_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getRecipeDetails",
                "description": "Retrieves the full details for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe.",
                        }
                    },
                    "required": ["recipe_id"],
                },
            },
        }


class GetRecipeIngredients(Tool):
    """Obtains all components for a certain recipe ID."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        recipe_ingredients = data.get("recipe_ingredients", [])
        ingredients = [
            ri for ri in recipe_ingredients if ri.get("recipe_id") == recipe_id
        ]
        payload = ingredients
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeIngredients",
                "description": "Retrieves all ingredients for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe.",
                        }
                    },
                    "required": ["recipe_id"],
                },
            },
        }


class SearchRecipesByTitleSubstring(Tool):
    """Looks for recipes whose titles include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], title_substring: str = None) -> str:
        if not title_substring:
            payload = {"error": "title_substring parameter is required."}
            out = json.dumps(payload)
            return out
        recipes = data.get("recipes", [])
        matching_recipes = [
            recipe
            for recipe in recipes
            if title_substring.lower() in recipe.get("recipe_title", "").lower()
        ]
        payload = matching_recipes
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchRecipesByTitleSubstring",
                "description": "Searches for recipes with titles containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title_substring": {
                            "type": "string",
                            "description": "The text to search for in recipe titles.",
                        }
                    },
                    "required": ["title_substring"],
                },
            },
        }


#Stock and Meal Record Tools
class GetInventoryForHousehold(Tool):
    """Fetches all stock items for a specific household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        inventory = data.get("inventory_items", [])
        household_inventory = [
            item for item in inventory if item.get("household_id") == household_id
        ]
        payload = household_inventory
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getInventoryForHousehold",
                "description": "Retrieves all inventory items for a given household ID.",
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


class GetMealHistoryForHousehold(Tool):
    """Obtains the meal records for a specific household ID over a defined number of previous days."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str, days_ago: int = 14) -> str:
        meal_history = data.get("meal_history", [])
        current_date = datetime.strptime("2025-08-20", "%Y-%m-%d")
        start_date = current_date - timedelta(days=days_ago)
        history = [
            h
            for h in meal_history
            if h.get("household_id") == household_id
            and datetime.strptime(h.get("plan_date"), "%Y-%m-%d") >= start_date
        ]
        payload = history
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistoryForHousehold",
                "description": "Retrieves the meal history for a given household ID for a specified number of past days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "days_ago": {
                            "type": "integer",
                            "description": "Number of past days to retrieve history for. Defaults to 14.",
                        },
                    },
                    "required": ["household_id"],
                },
            },
        }


#Meal Planning Tools


class GetMealPlansByHouseholdId(Tool):
    """Fetches all meal plans associated with a particular household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            payload = {"error": "household_id parameter is required."}
            out = json.dumps(payload)
            return out
        meal_plans = data.get("meal_plans", [])
        matching_plans = [
            plan for plan in meal_plans if plan.get("household_id") == household_id
        ]
        payload = matching_plans
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlansByHouseholdId",
                "description": "Retrieves all meal plans for a specific household ID.",
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


class SearchMealPlanEntries(Tool):
    """Looks for meal plan entries in a specific plan and date range that have a substring in their notes."""

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: str = None, start_date: str = None, end_date: str = None, notes_substring: str = None) -> str:
        if not all([meal_plan_id, start_date, end_date, notes_substring]):
            payload = {
                    "error": "meal_plan_id, start_date, end_date, and notes_substring are required parameters."
                }
            out = json.dumps(
                payload)
            return out
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
        payload = matching_entries
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchMealPlanEntries",
                "description": "Searches for meal plan entries within a specific plan and date range that contain a substring in their notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID of the meal plan to search within.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the search range (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the search range (YYYY-MM-DD).",
                        },
                        "notes_substring": {
                            "type": "string",
                            "description": "The text to search for within the entry notes.",
                        },
                    },
                    "required": [
                        "meal_plan_id",
                        "start_date",
                        "end_date",
                        "notes_substring",
                    ],
                },
            },
        }


class GetMealPlanEntriesByRecipeId(Tool):
    """Fetches all meal plan entries that incorporate a particular recipe ID."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        if recipe_id is None:
            payload = {"error": "recipe_id parameter is required."}
            out = json.dumps(payload)
            return out
        meal_plan_entries = data.get("meal_plan_entries", [])
        matching_entries = [
            entry for entry in meal_plan_entries if entry.get("recipe_id") == recipe_id
        ]
        payload = matching_entries
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanEntriesByRecipeId",
                "description": "Retrieves all meal plan entries that use a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe to find in meal plans.",
                        }
                    },
                    "required": ["recipe_id"],
                },
            },
        }


#Grocery Planning Tools


#Modify/Delete Tools
class UpdateInventoryItemQuantity(Tool):
    """Modifies the amount of an item in the household stock."""

    @staticmethod
    def invoke(data: dict[str, Any], inv_item_id: str = None, new_quantity: int = None) -> str:
        inventory = data.get("inventory_items", [])
        for item in inventory:
            if item.get("inv_item_id") == inv_item_id:
                item["quantity"] = new_quantity
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"error": f"Inventory item {inv_item_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryItemQuantity",
                "description": "Updates the quantity of an item in the household inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {"type": "integer"},
                        "new_quantity": {"type": "number"},
                    },
                    "required": ["inv_item_id", "new_quantity"],
                },
            },
        }


class RemoveRecipeFromMealPlan(Tool):
    """Deletes a recipe from a meal plan."""

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: str = None) -> str:
        entries = data.get("meal_plan_entries", [])
        entry_to_remove = next(
            (e for e in entries if e.get("entry_id") == entry_id), None
        )
        if entry_to_remove:
            data["meal_plan_entries"] = [
                e for e in entries if e.get("entry_id") != entry_id
            ]
            payload = {"status": "success", "message": f"Entry {entry_id} removed."}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Meal plan entry {entry_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveRecipeFromMealPlan",
                "description": "Removes a recipe from a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {"entry_id": {"type": "integer"}},
                    "required": ["entry_id"],
                },
            },
        }


class SearchUsersByName(Tool):
    """Looks for users whose full names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out

        users = data.get("users", [])

        matching_users = [
            user
            for user in users
            if name_query.lower() in user.get("full_name", "").lower()
        ]
        payload = matching_users
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchUsersByName",
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
    """Looks for ingredients whose names contain the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out

        ingredients = data.get("ingredients", [])

        matching_ingredients = [
            ingredient
            for ingredient in ingredients
            if name_query.lower() in ingredient.get("ingredient_name", "").lower()
        ]
        payload = matching_ingredients
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchIngredientsByName",
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
    """Fetches all stock items for a specific household ID and a particular ingredient ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None, ingredient_id: str = None) -> str:
        if household_id is None or ingredient_id is None:
            payload = {"error": "household_id and ingredient_id parameters are required."}
            out = json.dumps(payload)
            return out

        inventory = data.get("inventory_items", [])

        household_ingredient_inventory = [
            item
            for item in inventory
            if item.get("household_id") == household_id
            and item.get("ingredient_id") == ingredient_id
        ]
        payload = household_ingredient_inventory
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryForHouseholdAndIngredientId",
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
                        },
                    },
                    "required": ["household_id", "ingredient_id"],
                },
            },
        }


class SearchStoresByName(Tool):
    """Looks for stores whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out

        stores = data.get("stores", [])

        matching_stores = [
            store
            for store in stores
            if name_query.lower() in store.get("store_name", "").lower()
        ]
        payload = matching_stores
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchStoresByName",
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
    """Inserts a new record into the meal history."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, recipe_id: int = None, plan_date: str = None, was_prepared: bool = None, rating_int: int = None) -> str:
        history = data.get("meal_history", [])
        new_id = max([h.get("history_id", 0) for h in history]) + 1 if history else 6201

        new_entry = {
            "history_id": new_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int,
        }
        data["meal_history"].append(new_entry)
        payload = new_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddMealHistory",
                "description": "Adds a new entry to the meal history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "recipe_id": {"type": "integer"},
                        "plan_date": {
                            "type": "string",
                            "description": "Date the meal was planned for in YYYY-MM-DD format.",
                        },
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {
                            "type": "integer",
                            "description": "Rating from 1 to 5; can be null.",
                        },
                    },
                    "required": [
                        "household_id",
                        "recipe_id",
                        "plan_date",
                        "was_prepared",
                    ],
                },
            },
        }


class UpdateMealPlanEntryNotes(Tool):
    """Modifies the notes for a particular meal plan entry."""

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: str = None, new_notes: str = None) -> str:
        entries = data.get("meal_plan_entries", [])
        for entry in entries:
            if entry.get("entry_id") == entry_id:
                entry["notes"] = new_notes
                payload = entry
                out = json.dumps(payload)
                return out
        payload = {"error": f"Meal plan entry with ID '{entry_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealPlanEntryNotes",
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
    """Incorporates a new user."""

    @staticmethod
    def invoke(data: dict[str, Any], email: str = None, full_name: str = None) -> str:
        users = data.get("users", [])
        if any(user.get("email") == email for user in users):
            payload = {"error": f"User with email '{email}' already exists."}
            out = json.dumps(payload)
            return out
        new_id = max([u.get("user_id", 0) for u in users]) + 1 if users else 101
        new_user = {
            "user_id": new_id,
            "email": email,
            "full_name": full_name,
            "created_at": "2025-08-22T10:00:00Z",
        }
        data["users"].append(new_user)
        payload = new_user
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addUser",
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
    """Incorporates a new household."""

    @staticmethod
    def invoke(data: dict[str, Any], household_name: str = None, timezone: str = None, primary_user_id: int = None) -> str:
        households = data.get("households", [])
        new_id = (
            max([h.get("household_id", 0) for h in households]) + 1
            if households
            else 201
        )
        new_household = {
            "household_id": new_id,
            "household_name": household_name,
            "timezone": timezone,
            "primary_user_id": primary_user_id,
        }
        data["households"].append(new_household)
        payload = new_household
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addHousehold",
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
    """Inserts a new member into a household."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, full_name: str = None, birthdate: str = None, is_child: bool = None) -> str:
        members = data.get("members", [])
        new_id = max([m.get("member_id", 0) for m in members]) + 1 if members else 301
        new_member = {
            "member_id": new_id,
            "household_id": household_id,
            "full_name": full_name,
            "birthdate": birthdate,
            "is_child": is_child,
            "activity_level": "medium",
            "dietary_notes": "",
            "allergies_json": ["none"],
            "target_calories": 1400,
            "target_protein": 35,
        }
        data["members"].append(new_member)
        payload = new_member
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addMember",
                "description": "Adds a new member to a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                        "birthdate": {
                            "type": "string",
                            "description": "YYYY-MM-DD format.",
                        },
                        "is_child": {"type": "boolean"},
                    },
                    "required": ["household_id", "full_name", "birthdate", "is_child"],
                },
            },
        }


class GetGroceryListsByHouseholdId(Tool):
    """Fetches all shopping lists for a particular household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            payload = {"error": "household_id parameter is required."}
            out = json.dumps(payload)
            return out

        grocery_lists = data.get("grocery_lists", [])

        matching_lists = [
            glist
            for glist in grocery_lists
            if glist.get("household_id") == household_id
        ]
        payload = matching_lists
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListsByHouseholdId",
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
    """Obtains meal records for a specific household on a particular date."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None, plan_date: str = None) -> str:
        if household_id is None or plan_date is None:
            payload = {"error": "household_id and plan_date parameters are required."}
            out = json.dumps(payload)
            return out

        meal_history = data.get("meal_history", [])

        matching_history = [
            entry
            for entry in meal_history
            if entry.get("household_id") == household_id
            and entry.get("plan_date") == plan_date
        ]
        payload = matching_history
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistoryByHouseholdAndDate",
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
                        },
                    },
                    "required": ["household_id", "plan_date"],
                },
            },
        }


class RemoveItemFromGroceryList(Tool):
    """Deletes an item from a grocery list using its item ID."""

    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None) -> str:
        if item_id is None:
            payload = {"error": "item_id parameter is required."}
            out = json.dumps(payload)
            return out

        items = data.get("grocery_list_items", [])
        original_count = len(items)
        # Exclude the item that has the corresponding ID
        data["grocery_list_items"] = [
            item for item in items if item.get("item_id") != item_id
        ]

        if len(data["grocery_list_items"]) < original_count:
            payload = {
                "status": "success",
                "message": f"Item {item_id} removed from grocery list.",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Item with ID '{item_id}' not found on any grocery list."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveItemFromGroceryList",
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
    """Modifies a record in the meal history, including its preparation status or rating."""

    @staticmethod
    def invoke(data: dict[str, Any], history_id: str = None, was_prepared: bool = None, rating_int: int = None) -> str:
        if history_id is None:
            payload = {"error": "history_id parameter is required."}
            out = json.dumps(payload)
            return out

        history = data.get("meal_history", [])
        for entry in history:
            if entry.get("history_id") == history_id:
                if was_prepared is not None:
                    entry["was_prepared"] = was_prepared
                if rating_int is not None:
                    entry["rating_int"] = rating_int
                payload = entry
                out = json.dumps(payload)
                return out
        payload = {"error": f"Meal history entry with ID '{history_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealHistory",
                "description": "Updates an entry in the meal history, such as its preparation status or rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "history_id": {"type": "integer"},
                        "was_prepared": {
                            "type": "boolean",
                            "description": "Set to true if the meal was prepared.",
                        },
                        "rating_int": {
                            "type": "integer",
                            "description": "Rating from 1 to 5, can be null.",
                        },
                    },
                    "required": ["history_id"],
                },
            },
        }


class GetGroceryListItemsByListIdAndIngredientId(Tool):
    """Fetches items from a specific grocery list that correspond to a particular ingredient ID."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = None, ingredient_id: str = None) -> str:
        if list_id is None or ingredient_id is None:
            payload = {"error": "list_id and ingredient_id parameters are required."}
            out = json.dumps(payload)
            return out

        grocery_list_items = data.get("grocery_list_items", [])

        matching_items = [
            item
            for item in grocery_list_items
            if item.get("list_id") == list_id
            and item.get("ingredient_id") == ingredient_id
        ]
        payload = matching_items
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListItemsByListIdAndIngredientId",
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
                        },
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
