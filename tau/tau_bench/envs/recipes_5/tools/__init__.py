# Copyright Sierra


# Helper functions
def _household_for_user(data, user_id):
    """Get household for a user."""
    users = list(data.get('users', {}).values())
    for user in users:
        if user.get('user_id') == user_id:
            return user.get('household_id')
    return None

def _first_user_id(data):
    """Get first user ID."""
    users = list(data.get('users', {}).values())
    if users:
        return users[0].get('user_id')
    return None




# Helper function
import json

def _json_dump(obj):
    """Dump object to JSON string."""
    return json.dumps(obj, indent=2)

from .get_user_by_email import GetUserByEmail
from .get_household_by_user_id import GetHouseholdByUserId
from .list_household_members import ListHouseholdMembers
from .get_member_by_name import GetMemberByName
from .compute_and_set_member_targets import ComputeAndSetMemberTargets
from .list_recent_meal_history import ListRecentMealHistory
from .build_recipe_filters import BuildRecipeFilters
from .list_recipes_by_filters import ListRecipesByFilters
from .exclude_recent_recipes import ExcludeRecentRecipes
from .apply_cuisine_limit import ApplyCuisineLimit
from .rank_recipes_for_targets import RankRecipesForTargets
from .generate_child_modifications import GenerateChildModifications
from .create_meal_plan import CreateMealPlan
from .bulk_add_meal_plan_entries import BulkAddMealPlanEntries
from .update_meal_plan_entry_notes import UpdateMealPlanEntryNotes
from .create_grocery_list_from_meal_plan import CreateGroceryListFromMealPlan
from .categorize_grocery_list_sections import CategorizeGroceryListSections
from .flag_pantry_staples_on_list import FlagPantryStaplesOnList
from .flag_overlap_last_month_on_list import FlagOverlapLastMonthOnList
from .list_inventory_by_household import ListInventoryByHousehold
from .check_store_inventory_for_list import CheckStoreInventoryForList
from .find_substitute_products import FindSubstituteProducts
from .update_grocery_list_with_substitutes import UpdateGroceryListWithSubstitutes
from .create_order_from_list import CreateOrderFromList
from .add_order_items_from_list import AddOrderItemsFromList
from .update_order_status import UpdateOrderStatus
from .log_audit_event import LogAuditEvent
from .generate_recipe_packet import GenerateRecipePacket
from .get_meal_plan_details import GetMealPlanDetails
from .get_grocery_list_details import GetGroceryListDetails

ALL_TOOLS = [
    GetUserByEmail,
    GetHouseholdByUserId,
    ListHouseholdMembers,
    GetMemberByName,
    ComputeAndSetMemberTargets,
    ListRecentMealHistory,
    BuildRecipeFilters,
    ListRecipesByFilters,
    ExcludeRecentRecipes,
    ApplyCuisineLimit,
    RankRecipesForTargets,
    GenerateChildModifications,
    CreateMealPlan,
    BulkAddMealPlanEntries,
    UpdateMealPlanEntryNotes,
    CreateGroceryListFromMealPlan,
    CategorizeGroceryListSections,
    FlagPantryStaplesOnList,
    FlagOverlapLastMonthOnList,
    ListInventoryByHousehold,
    CheckStoreInventoryForList,
    FindSubstituteProducts,
    UpdateGroceryListWithSubstitutes,
    CreateOrderFromList,
    AddOrderItemsFromList,
    UpdateOrderStatus,
    LogAuditEvent,
    GenerateRecipePacket,
    GetMealPlanDetails,
    GetGroceryListDetails,
]