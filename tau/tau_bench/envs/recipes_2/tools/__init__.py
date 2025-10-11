# Copyright Sierra

from .create_meal_plan import CreateMealPlan
from .add_recipe_to_meal_plan import AddRecipeToMealPlan
from .create_grocery_list_from_meal_plan import CreateGroceryListFromMealPlan
from .add_item_to_grocery_list import AddItemToGroceryList
from .create_order_from_grocery_list import CreateOrderFromGroceryList
from .add_audit_log import AddAuditLog
from .get_user_by_email import GetUserByEmail
from .get_household_by_user_id import GetHouseholdByUserId
from .get_members_by_household_id import GetMembersByHouseholdId
from .search_households_by_name import SearchHouseholdsByName
from .search_recipes import SearchRecipes
from .get_recipe_details import GetRecipeDetails
from .get_recipe_ingredients import GetRecipeIngredients
from .search_recipes_by_title_substring import SearchRecipesByTitleSubstring
from .get_inventory_for_household import GetInventoryForHousehold
from .get_meal_history_for_household import GetMealHistoryForHousehold
from .get_meal_plans_by_household_id import GetMealPlansByHouseholdId
from .search_meal_plan_entries import SearchMealPlanEntries
from .get_meal_plan_entries_by_recipe_id import GetMealPlanEntriesByRecipeId
from .update_inventory_item_quantity import UpdateInventoryItemQuantity
from .remove_recipe_from_meal_plan import RemoveRecipeFromMealPlan
from .search_users_by_name import SearchUsersByName
from .search_ingredients_by_name import SearchIngredientsByName
from .get_inventory_for_household_and_ingredient_id import GetInventoryForHouseholdAndIngredientId
from .search_stores_by_name import SearchStoresByName
from .add_meal_history import AddMealHistory
from .update_meal_plan_entry_notes import UpdateMealPlanEntryNotes
from .add_user import AddUser
from .add_household import AddHousehold
from .add_member import AddMember
from .get_grocery_lists_by_household_id import GetGroceryListsByHouseholdId
from .get_meal_history_by_household_and_date import GetMealHistoryByHouseholdAndDate
from .remove_item_from_grocery_list import RemoveItemFromGroceryList
from .update_meal_history import UpdateMealHistory
from .get_grocery_list_items_by_list_id_and_ingredient_id import GetGroceryListItemsByListIdAndIngredientId

ALL_TOOLS = [
    CreateMealPlan,
    AddRecipeToMealPlan,
    CreateGroceryListFromMealPlan,
    AddItemToGroceryList,
    CreateOrderFromGroceryList,
    AddAuditLog,
    GetUserByEmail,
    GetHouseholdByUserId,
    GetMembersByHouseholdId,
    SearchHouseholdsByName,
    SearchRecipes,
    GetRecipeDetails,
    GetRecipeIngredients,
    SearchRecipesByTitleSubstring,
    GetInventoryForHousehold,
    GetMealHistoryForHousehold,
    GetMealPlansByHouseholdId,
    SearchMealPlanEntries,
    GetMealPlanEntriesByRecipeId,
    UpdateInventoryItemQuantity,
    RemoveRecipeFromMealPlan,
    SearchUsersByName,
    SearchIngredientsByName,
    GetInventoryForHouseholdAndIngredientId,
    SearchStoresByName,
    AddMealHistory,
    UpdateMealPlanEntryNotes,
    AddUser,
    AddHousehold,
    AddMember,
    GetGroceryListsByHouseholdId,
    GetMealHistoryByHouseholdAndDate,
    RemoveItemFromGroceryList,
    UpdateMealHistory,
    GetGroceryListItemsByListIdAndIngredientId,
]
