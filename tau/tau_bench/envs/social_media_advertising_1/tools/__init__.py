# Copyright Sierra

from .get_campaigns import GetCampaigns
from .get_name_for_campaign import GetNameForCampaign
from .get_objective_for_campaign import GetObjectiveForCampaign
from .get_status_for_campaign import GetStatusForCampaign
from .update_campaign_status import UpdateCampaignStatus
from .get_ad_sets import GetAdSets
from .get_name_for_ad_set import GetNameForAdSet
from .get_campaign_id_for_ad_set import GetCampaignIdForAdSet
from .get_daily_budget_for_ad_set import GetDailyBudgetForAdSet
from .update_daily_budget_for_ad_set import UpdateDailyBudgetForAdSet
from .get_ads import GetAds
from .get_name_for_ad import GetNameForAd
from .get_creative_type_for_ad import GetCreativeTypeForAd
from .get_status_for_ad import GetStatusForAd
from .update_ad_status import UpdateAdStatus
from .get_products import GetProducts
from .get_name_for_product import GetNameForProduct
from .get_plans import GetPlans
from .get_date_for_plan import GetDateForPlan
from .get_automation_runs import GetAutomationRuns
from .get_run_type_for_automation_run import GetRunTypeForAutomationRun
from .get_budget_changes import GetBudgetChanges
from .get_ad_set_id_for_budget_change import GetAdSetIdForBudgetChange
from .search_campaigns_by_objective import SearchCampaignsByObjective
from .search_campaigns_by_status import SearchCampaignsByStatus
from .search_ad_sets_by_category import SearchAdSetsByCategory
from .search_ad_sets_by_status import SearchAdSetsByStatus
from .search_ads_by_creative_type import SearchAdsByCreativeType
from .search_ads_by_status import SearchAdsByStatus
from .search_products_by_category import SearchProductsByCategory
from .search_automation_runs_by_type import SearchAutomationRunsByType
from .search_automation_runs_by_status import SearchAutomationRunsByStatus
from .search_budget_changes_by_ad_set import SearchBudgetChangesByAdSet
from .delete_campaign import DeleteCampaign
from .add_campaign import AddCampaign
from .delete_ad_set import DeleteAdSet
from .add_ad_set import AddAdSet
from .delete_ad import DeleteAd
from .add_ad import AddAd
from .delete_product import DeleteProduct
from .add_product import AddProduct
from .search_ad_sets_by_campaign_id import SearchAdSetsByCampaignId
from .calculate_roas import CalculateROAS
from .calculate_cpa import CalculateCPA
from .compare_value import CompareValue
from .increase_value_with_percent import IncreaseValueWithPercent
from .log_budget_change import LogBudgetChange
from .log_strategy_change import LogStrategyChange
from .add_automation_run import AddAutomationRun
from .update_bid_strategy_for_ad_set import UpdateBidStrategyForAdSet
from .update_ad_set_status import UpdateAdSetStatus
from .create_plan_allocation import CreatePlanAllocation
from .get_policy_param import GetPolicyParam
from .update_policy_param import UpdatePolicyParam
from .check_no_purchases import CheckNoPurchases
from .calculate_percentage_change import CalculatePercentageChange
from .calculate_spend_variance import CalculateSpendVariance
from .calculate_campaign_roas_for_period import CalculateCampaignROASForPeriod
from .calculate_roas_for_ad_set_for_period import CalculateROASForAdSetForPeriod
from .calculate_cpa_for_ad_set_for_period import CalculateCPAForAdSetForPeriod
from .calculate_roas_for_ad_set_for_day import CalculateROASForAdSetForDay
from .calculate_cpa_for_ad_set_for_day import CalculateCPAForAdSetForDay
from .search_ad_sets_by_name import SearchAdSetsByName
from .search_campaigns_by_name import SearchCampaignsByName
from .get_current_timestamp import GetCurrentTimestamp
from .delete_automation_run import DeleteAutomationRun
from .add_plan import AddPlan
from .get_status_for_ad_set import GetStatusForAdSet
from .decrease_value_with_percent import DecreaseValueWithPercent
from .round_number_to_unit import RoundNumberToUnit
from .search_ads_by_name import SearchAdsByName
from .search_ads_by_ad_set import SearchAdsByAdSet
from .get_bid_strategy_for_ad_set import GetBidStrategyForAdSet
from .get_bid_amount_for_ad_set import GetBidAmountForAdSet
from .get_allocations_for_plan import GetAllocationsForPlan
from .get_category_for_product import GetCategoryForProduct
from .search_products_by_name import SearchProductsByName
from .search_ad_sets_by_bid_strategy import SearchAdSetsByBidStrategy
from .get_bid_strategy_for_ad_set import GetBidStrategyForAdSet
from .get_viewership_for_date_and_category import GetViewershipForDateAndCategory
from .get_total_viewership_for_category_in_period import GetTotalViewershipForCategoryInPeriod
from .get_average_viewership_for_category_in_period import GetAverageViewershipForCategoryInPeriod
from .get_sales_for_category_in_period import GetSalesForCategoryInPeriod
from .get_average_daily_sales_for_category_in_period import GetAverageDailySalesForCategoryInPeriod

ALL_TOOLS = [
    GetCampaigns,
    GetNameForCampaign,
    GetObjectiveForCampaign,
    GetStatusForCampaign,
    UpdateCampaignStatus,
    GetAdSets,
    GetNameForAdSet,
    GetCampaignIdForAdSet,
    GetDailyBudgetForAdSet,
    UpdateDailyBudgetForAdSet,
    GetAds,
    GetNameForAd,
    GetCreativeTypeForAd,
    GetStatusForAd,
    UpdateAdStatus,
    GetProducts,
    GetNameForProduct,
    GetPlans,
    GetDateForPlan,
    GetAutomationRuns,
    GetRunTypeForAutomationRun,
    GetBudgetChanges,
    GetAdSetIdForBudgetChange,
    SearchCampaignsByObjective,
    SearchCampaignsByStatus,
    SearchAdSetsByCategory,
    SearchAdSetsByStatus,
    SearchAdsByCreativeType,
    SearchAdsByStatus,
    SearchProductsByCategory,
    SearchAutomationRunsByType,
    SearchAutomationRunsByStatus,
    SearchBudgetChangesByAdSet,
    DeleteCampaign,
    AddCampaign,
    DeleteAdSet,
    AddAdSet,
    DeleteAd,
    AddAd,
    DeleteProduct,
    AddProduct,
    SearchAdSetsByCampaignId,
    CalculateROAS,
    CalculateCPA,
    CompareValue,
    IncreaseValueWithPercent,
    LogBudgetChange,
    LogStrategyChange,
    AddAutomationRun,
    UpdateBidStrategyForAdSet,
    UpdateAdSetStatus,
    CreatePlanAllocation,
    GetPolicyParam,
    UpdatePolicyParam,
    CheckNoPurchases,
    CalculatePercentageChange,
    CalculateSpendVariance,
    CalculateCampaignROASForPeriod,
    CalculateROASForAdSetForPeriod,
    CalculateCPAForAdSetForPeriod,
    CalculateROASForAdSetForDay,
    CalculateCPAForAdSetForDay,
    SearchAdSetsByName,
    SearchCampaignsByName,
    GetCurrentTimestamp,
    DeleteAutomationRun,
    AddPlan,
    GetStatusForAdSet,
    DecreaseValueWithPercent,
    RoundNumberToUnit,
    SearchAdsByName,
    SearchAdsByAdSet,
    GetBidStrategyForAdSet,
    GetBidAmountForAdSet,
    GetAllocationsForPlan,
    GetCategoryForProduct,
    SearchProductsByName,
    SearchAdSetsByBidStrategy,
    GetBidStrategyForAdSet,
    GetViewershipForDateAndCategory,
    GetTotalViewershipForCategoryInPeriod,
    GetAverageViewershipForCategoryInPeriod,
    GetSalesForCategoryInPeriod,
    GetAverageDailySalesForCategoryInPeriod,
]
