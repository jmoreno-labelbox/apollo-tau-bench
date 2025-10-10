import json
# Copyright owned by Sierra.

from .get_user_by_full_name import GetUserByFullName
from .get_household_by_primary_user import GetHouseholdByPrimaryUser
from .get_household_by_id import GetHouseholdById
from .list_household_members import ListHouseholdMembers
from .compute_household_servings import ComputeHouseholdServings
from .build_recipe_filters import BuildRecipeFilters
from .list_recipes_by_filters import ListRecipesByFilters
from .list_recent_meal_history import ListRecentMealHistory
from .apply_cuisine_cap import ApplyCuisineCap
from .minimize_new_ingredients import MinimizeNewIngredients
from .rank_recipes_for_targets import RankRecipesForTargets
from .generate_child_modifications import GenerateChildModifications
from .create_meal_plan import CreateMealPlan
from .bulk_add_meal_plan_entries import BulkAddMealPlanEntries
from .update_meal_plan_entry_notes import UpdateMealPlanEntryNotes
from .get_meal_plan_by_household_and_week import GetMealPlanByHouseholdAndWeek
from .add_meal_plan_entries_by_keys import AddMealPlanEntriesByKeys
from .update_meal_plan_entry_notes_by_keys import UpdateMealPlanEntryNotesByKeys
from .create_empty_grocery_list import CreateEmptyGroceryList
from .create_grocery_list_for_plan_by_keys import CreateGroceryListForPlanByKeys
from .get_grocery_list_by_plan_keys import GetGroceryListByPlanKeys
from .get_grocery_list_details_by_plan_keys import GetGroceryListDetailsByPlanKeys
from .upsert_grocery_list_items_from_recipes import UpsertGroceryListItemsFromRecipes
from .categorize_grocery_list_sections import CategorizeGroceryListSections
from .flag_pantry_staples_on_list import FlagPantryStaplesOnList
from .flag_overlap_last_month_on_list import FlagOverlapLastMonthOnList
from .get_grocery_list_by_source_plan import GetGroceryListBySourcePlan
from .get_grocery_list_details import GetGroceryListDetails
from .upsert_grocery_list_items_for_plan_by_keys import UpsertGroceryListItemsForPlanByKeys
from .categorize_grocery_list_sections_by_plan_keys import CategorizeGroceryListSectionsByPlanKeys
from .flag_pantry_staples_on_list_by_plan_keys import FlagPantryStaplesOnListByPlanKeys
from .flag_overlap_last_month_on_list_by_plan_keys import FlagOverlapLastMonthOnListByPlanKeys
from .list_stores import ListStores
from .get_preferred_store_id import GetPreferredStoreId
from .get_aggregator_store_id import GetAggregatorStoreId
from .get_household_staple_ingredient_id import GetHouseholdStapleIngredientId
from .list_store_products import ListStoreProducts
from .check_store_inventory_for_list import CheckStoreInventoryForList
from .propose_substitute_products import ProposeSubstituteProducts
from .update_grocery_list_with_substitutes import UpdateGroceryListWithSubstitutes
from .create_order_from_list import CreateOrderFromList
from .create_order_for_plan_list_by_keys import CreateOrderForPlanListByKeys
from .add_order_items_for_plan_by_keys import AddOrderItemsForPlanByKeys
from .update_order_status_by_plan_keys import UpdateOrderStatusByPlanKeys
from .get_order_details_by_plan_keys import GetOrderDetailsByPlanKeys
from .add_order_items_from_list import AddOrderItemsFromList
from .update_order_status import UpdateOrderStatus
from .get_orders_for_household import GetOrdersForHousehold
from .get_order_details import GetOrderDetails
from .append_meal_history import AppendMealHistory
from .update_inventory_quantity import UpdateInventoryQuantity
from .log_inventory_consume_by_keys import LogInventoryConsumeByKeys
from .log_meal_plan_create_by_keys import LogMealPlanCreateByKeys
from .log_grocery_list_create_by_keys import LogGroceryListCreateByKeys
from .log_meal_history_create_by_keys import LogMealHistoryCreateByKeys
from .log_order_placed_by_plan_keys import LogOrderPlacedByPlanKeys
from .log_order_delivered_by_plan_keys import LogOrderDeliveredByPlanKeys
from .log_validate_substitutions_by_plan_keys import LogValidateSubstitutionsByPlanKeys
from .check_store_inventory_for_plan_by_keys import CheckStoreInventoryForPlanByKeys
from .update_grocery_list_with_substitutes_by_plan_keys import UpdateGroceryListWithSubstitutesByPlanKeys
from .log_audit_event import LogAuditEvent
from .get_recipe_details import GetRecipeDetails
from .list_recipe_ingredients import ListRecipeIngredients
from .search_ingredients_by_name import SearchIngredientsByName
from .search_recipes_by_title_substring import SearchRecipesByTitleSubstring
from .get_inventory_for_household_and_ingredient_id import GetInventoryForHouseholdAndIngredientId
from .get_meal_history_for_household import GetMealHistoryForHousehold

ALL_TOOLS = [
    GetUserByFullName,
    GetHouseholdByPrimaryUser,
    GetHouseholdById,
    ListHouseholdMembers,
    ComputeHouseholdServings,
    BuildRecipeFilters,
    ListRecipesByFilters,
    ListRecentMealHistory,
    ApplyCuisineCap,
    MinimizeNewIngredients,
    RankRecipesForTargets,
    GenerateChildModifications,
    CreateMealPlan,
    BulkAddMealPlanEntries,
    UpdateMealPlanEntryNotes,
    GetMealPlanByHouseholdAndWeek,
    AddMealPlanEntriesByKeys,
    UpdateMealPlanEntryNotesByKeys,
    CreateEmptyGroceryList,
    CreateGroceryListForPlanByKeys,
    GetGroceryListByPlanKeys,
    GetGroceryListDetailsByPlanKeys,
    UpsertGroceryListItemsFromRecipes,
    CategorizeGroceryListSections,
    FlagPantryStaplesOnList,
    FlagOverlapLastMonthOnList,
    GetGroceryListBySourcePlan,
    GetGroceryListDetails,
    UpsertGroceryListItemsForPlanByKeys,
    CategorizeGroceryListSectionsByPlanKeys,
    FlagPantryStaplesOnListByPlanKeys,
    FlagOverlapLastMonthOnListByPlanKeys,
    ListStores,
    GetPreferredStoreId,
    GetAggregatorStoreId,
    GetHouseholdStapleIngredientId,
    ListStoreProducts,
    CheckStoreInventoryForList,
    ProposeSubstituteProducts,
    UpdateGroceryListWithSubstitutes,
    CreateOrderFromList,
    CreateOrderForPlanListByKeys,
    AddOrderItemsForPlanByKeys,
    UpdateOrderStatusByPlanKeys,
    GetOrderDetailsByPlanKeys,
    AddOrderItemsFromList,
    UpdateOrderStatus,
    GetOrdersForHousehold,
    GetOrderDetails,
    AppendMealHistory,
    UpdateInventoryQuantity,
    LogInventoryConsumeByKeys,
    LogMealPlanCreateByKeys,
    LogGroceryListCreateByKeys,
    LogMealHistoryCreateByKeys,
    LogOrderPlacedByPlanKeys,
    LogOrderDeliveredByPlanKeys,
    LogValidateSubstitutionsByPlanKeys,
    CheckStoreInventoryForPlanByKeys,
    UpdateGroceryListWithSubstitutesByPlanKeys,
    LogAuditEvent,
    GetRecipeDetails,
    ListRecipeIngredients,
    SearchIngredientsByName,
    SearchRecipesByTitleSubstring,
    GetInventoryForHouseholdAndIngredientId,
    GetMealHistoryForHousehold,
]
