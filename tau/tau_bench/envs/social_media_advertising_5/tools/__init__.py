# Copyright owned by Sierra.

from .get_plan_for_date import GetPlanForDate
from .get_adset_allocation_from_plan import GetAdsetAllocationFromPlan
from .get_policy_parameter import GetPolicyParameter
from .list_canonical_bid_strategies import ListCanonicalBidStrategies
from .list_canonical_creative_types import ListCanonicalCreativeTypes
from .validate_allocations_against_policy import ValidateAllocationsAgainstPolicy
from .get_campaign_by_name import GetCampaignByName
from .create_campaign import CreateCampaign
from .update_campaign_status import UpdateCampaignStatus
from .get_adsets_by_campaign_id import GetAdsetsByCampaignID
from .get_adset_details_by_id import GetAdsetDetailsByID
from .create_adset import CreateAdset
from .update_adset_budget import UpdateAdsetBudget
from .update_adset_bid_strategy import UpdateAdsetBidStrategy
from .get_ads_by_adset_id import GetAdsByAdsetID
from .create_ad import CreateAd
from .update_ad_status import UpdateAdStatus
from .rotate_ad_creative import RotateAdCreative
from .get_daily_insights_for_adset import GetDailyInsightsForAdset
from .calculate_adset_roas_for_day import CalculateAdsetRoasForDay
from .compute_ctr_for_adset_day import ComputeCtrForAdsetDay
from .get_adset_spend_for_date_range import GetAdsetSpendForDateRange
from .get_weekly_sales_by_category import GetWeeklySalesByCategory
from .get_viewership_for_category import GetViewershipForCategory
from .get_product_price_on_date import GetProductPriceOnDate
from .find_underperforming_adsets import FindUnderperformingAdsets
from .create_automation_run import CreateAutomationRun
from .get_automation_run_history import GetAutomationRunHistory
from .update_automation_run_end import UpdateAutomationRunEnd
from .get_last_successful_run import GetLastSuccessfulRun
from .log_budget_change import LogBudgetChange
from .log_strategy_change import LogStrategyChange
from .log_creative_rotation import LogCreativeRotation
from .get_product_by_name import GetProductByName
from .get_adsets_by_category import GetAdsetsByCategory
from .create_plan import CreatePlan

ALL_TOOLS = [
    GetPlanForDate,
    GetAdsetAllocationFromPlan,
    GetPolicyParameter,
    ListCanonicalBidStrategies,
    ListCanonicalCreativeTypes,
    ValidateAllocationsAgainstPolicy,
    GetCampaignByName,
    CreateCampaign,
    UpdateCampaignStatus,
    GetAdsetsByCampaignID,
    GetAdsetDetailsByID,
    CreateAdset,
    UpdateAdsetBudget,
    UpdateAdsetBidStrategy,
    GetAdsByAdsetID,
    CreateAd,
    UpdateAdStatus,
    RotateAdCreative,
    GetDailyInsightsForAdset,
    CalculateAdsetRoasForDay,
    ComputeCtrForAdsetDay,
    GetAdsetSpendForDateRange,
    GetWeeklySalesByCategory,
    GetViewershipForCategory,
    GetProductPriceOnDate,
    FindUnderperformingAdsets,
    CreateAutomationRun,
    GetAutomationRunHistory,
    UpdateAutomationRunEnd,
    GetLastSuccessfulRun,
    LogBudgetChange,
    LogStrategyChange,
    LogCreativeRotation,
    GetProductByName,
    GetAdsetsByCategory,
    CreatePlan,
]
