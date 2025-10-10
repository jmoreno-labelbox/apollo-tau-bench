# Copyright owned by Sierra



# Utility function
def _require(data, key, error_msg=None):
    """Require a key to exist in data."""
    if key not in data or data[key] is None:
        raise ValueError(error_msg or f"Required key '{key}' not found or is None")
    return data[key]


# Utility function
def _max_id(items, id_key='id', prefix=''):
    """Get max ID from items."""
    if not items:
        return 0
    max_id = 0
    for item in items:
        item_id = str(item.get(id_key, ''))
        if prefix:
            item_id = item_id.replace(prefix, '')
        try:
            num = int(item_id)
            max_id = max(max_id, num)
        except (ValueError, AttributeError):
            pass
    return max_id

from .get_user_by_id import GetUserById
from .get_household_by_id import GetHouseholdById
from .list_household_members import ListHouseholdMembers
from .get_member_targets import GetMemberTargets
from .list_inventory_by_household import ListInventoryByHousehold
from .list_recent_meal_history import ListRecentMealHistory
from .get_recipe_by_id import GetRecipeById
from .list_recipe_ingredients import ListRecipeIngredients
from .build_recipe_filters import BuildRecipeFilters
from .list_recipes_by_filters import ListRecipesByFilters
from .exclude_recipe_ids import ExcludeRecipeIds
from .apply_cuisine_cap import ApplyCuisineCap
from .minimize_new_ingredients import MinimizeNewIngredients
from .rank_recipes_for_targets import RankRecipesForTargets
from .generate_child_modifications import GenerateChildModifications
from .create_meal_plan import CreateMealPlan
from .bulk_add_meal_plan_entries import BulkAddMealPlanEntries
from .update_meal_plan_entry_notes import UpdateMealPlanEntryNotes
from .create_empty_grocery_list import CreateEmptyGroceryList
from .upsert_grocery_list_items_from_recipes import UpsertGroceryListItemsFromRecipes
from .categorize_grocery_list_sections import CategorizeGroceryListSections
from .flag_pantry_staples_on_list import FlagPantryStaplesOnList
from .flag_overlap_last_month_on_list import FlagOverlapLastMonthOnList
from .set_grocery_list_status import SetGroceryListStatus
from .check_store_inventory_for_list import CheckStoreInventoryForList
from .propose_substitute_products import ProposeSubstituteProducts
from .update_grocery_list_with_substitutes import UpdateGroceryListWithSubstitutes
from .create_order_from_list import CreateOrderFromList
from .add_order_items_from_list import AddOrderItemsFromList
from .update_order_status import UpdateOrderStatus
from .log_audit_event import LogAuditEvent
from .get_meal_plan_details import GetMealPlanDetails
from .get_grocery_list_details import GetGroceryListDetails
from .list_stores import ListStores
from .list_store_products import ListStoreProducts

ALL_TOOLS = [
    GetUserById,
    GetHouseholdById,
    ListHouseholdMembers,
    GetMemberTargets,
    ListInventoryByHousehold,
    ListRecentMealHistory,
    GetRecipeById,
    ListRecipeIngredients,
    BuildRecipeFilters,
    ListRecipesByFilters,
    ExcludeRecipeIds,
    ApplyCuisineCap,
    MinimizeNewIngredients,
    RankRecipesForTargets,
    GenerateChildModifications,
    CreateMealPlan,
    BulkAddMealPlanEntries,
    UpdateMealPlanEntryNotes,
    CreateEmptyGroceryList,
    UpsertGroceryListItemsFromRecipes,
    CategorizeGroceryListSections,
    FlagPantryStaplesOnList,
    FlagOverlapLastMonthOnList,
    SetGroceryListStatus,
    CheckStoreInventoryForList,
    ProposeSubstituteProducts,
    UpdateGroceryListWithSubstitutes,
    CreateOrderFromList,
    AddOrderItemsFromList,
    UpdateOrderStatus,
    LogAuditEvent,
    GetMealPlanDetails,
    GetGroceryListDetails,
    ListStores,
    ListStoreProducts,
]
