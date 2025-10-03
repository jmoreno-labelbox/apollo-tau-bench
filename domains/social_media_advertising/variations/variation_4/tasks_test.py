from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="USER_001",
        instruction=(
            "Acting as a Risk Manager, your task is to conduct performance triage for 2025-08-13. Locate all ad sets having a ROAS under 1.5. Once identified, apply a 20% budget cut to each ad set. Additionally, for any of those ad sets with a ROAS under 1.0, make sure their bid strategy is configured to 'lowest_cost'. Ensure that all actions are logged."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"underperforming_adsets_found": "3"',
            '"budget_changes_logged": "3"',
            '"strategy_changes_logged": "1"',
            '"total_optimizations_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction=(
            "As a Finance Manager, recognize that on 2025-08-13, the 'Global Summer Sale' campaign’s total daily budget remains under its $2500 limit. Calculate the precise budget headroom still available and fully redirect this portion into the highest performing ad set for that day, based on ROAS, to enhance returns. Confirm that the new budget respects rounding guidelines and document the modification with the standard reason."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Global Summer Sale"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "1"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 880.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 880.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"budget_headroom": "290.0"',
            '"top_performer_id": "102"',
            '"reinvestment_complete": "true"',
            '"new_budget_for_102": "880.0"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction=(
            "As a manager for the 'Toys' and 'Home' categories, handle the consolidation of marketing efforts by establishing a new 'Sales' campaign called 'Home_And_Toys_Holiday_Push'. Transition ad sets 106 and 107 into this newly created campaign by setting up new ad sets with the same settings (name, category, budget, bid) under the new campaign ID. Conclude the migration by pausing the entire original campaign ('Holiday Season Early Bird')."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="CreateCampaign", kwargs={"name": "Home_And_Toys_Holiday_Push", "objective": "Sales"}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Holiday - Home Goods", "category": "Home", "daily_budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Holiday - Toys", "category": "Toys", "daily_budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "106"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "107"}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Cozy Home Candles", "creative_type": "image"}),
            Action(name="CreateAd", kwargs={"adset_id": "114", "name": "MEGA Space Shuttle", "creative_type": "video"}),
            Action(name="UpdateCampaignStatus", kwargs={"campaign_id": "5", "status": "paused"})
        ],
        outputs=[
            '"new_campaign_id": "11"',
            '"new_adsets_created": "2"',
            '"ads_migrated": "2"',
            '"original_campaign_paused": "true"',
            '"consolidation_complete": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_004",
        instruction=(
            "Acting as a Performance Analyst, analyze ad set 101 on 2025-08-13, which achieved a high ROAS but was close to its budget limit. To explore scalability, coordinate a 25% budget increase alongside an $8 increment to the cost_cap bid to sustain competitiveness. Ensure the revised bid complies with the maximum bid policy. Record both modifications."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1150.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 40.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1150.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 40.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"roas": "10.0"',
            '"new_budget": "1150.0"',
            '"new_bid": "40.0"',
            '"max_bid_check_passed": "true"',
            '"changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction=(
            "As a Market Analyst, your mission is to reward the category with the highest user engagement. On 2025-08-13, identify the product category that has recorded the maximum 'active_users'. Following this identification, grant a 10% budget enhancement to all existing ad sets within this top-performing category to acknowledge the high engagement. Document all the modifications."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Home", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Mobile", "date": "2025-08-13"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Mobile"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 1100.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 1100.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"winning_category": "Mobile"',
            '"adsets_rewarded": "2"',
            '"budget_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_006",
        instruction=(
            "As a Senior Strategist, you are tasked with conducting a full portfolio optimization for the 'Global Summer Sale' campaign focusing on the CA-based ad sets (101 and 102), reflecting on the performance of 2025-08-13. Implement our standard procedures to reward their accomplishments in terms of budget and bids. For creative aspects, align their active ads with the scheduled daily plan. Generate a comprehensive audit trail for all updates."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"adsets_optimized": "2"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "1"',
            '"creative_changes_logged": "2"',
            '"total_logs": "5"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_007",
        instruction=(
            "As the manager for the 'Back to School Deals' campaign, examine the active ad set's performance for 2025-08-13 and implement the 'Budget Optimization Protocol'. Appropriately optimize the budget according to performance data, ensuring adherence to rounding policies and logging requirements."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Back to School Deals"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "6"}),
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "6"',
            '"active_adset_id": "108"',
            '"adset_108_roas": "11.28"',
            '"old_budget": "780.0"',
            '"new_budget": "900.0"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction=(
            "As an efficiency analyst, note that ad set 'Brand - Video Ads' (ID 103) has been identified for excessive spending without revenue on 2025-08-13. Assess its performance and implement the 'Budget Optimization Protocol' exclusively for ad set 103 to tailor its budget according to the performance data. Avoid adjusting other underperforming ad sets - concentrate solely on ad set 103. Document the action with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_103_roas": "0.0"',
            '"old_budget": "1180.0"',
            '"new_budget": "940.0"',
            '"budget_reduction_pct": "20"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_009",
        instruction=(
            "As the performance manager for women's apparel, handle the budget examination for the 'Fall Fashion - Women' ad set (ID 104) scheduled for 2025-08-13. Coordinate the budget optimization process specifically targeting ad set 104 without altering any other underperforming ad sets that might be identified. Focus solely on ad set 104, applying suitable budget enhancements based on performance data, while adhering to rounding policies and documenting requirements."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_104_roas": "11.22"',
            '"old_budget": "740.0"',
            '"new_budget": "850.0"',
            '"budget_increase_pct": "15"',
            '"status": "completed"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_010",
        instruction=(
            "In your role as the social media advertising operations manager, examine the performance of App Install ad sets 110 and 111 on 2025-08-13. Should their ROAS fall below the 1.5 benchmark, implement the 'Budget Optimization Protocol' and 'Bid Strategy Optimization Protocol' in line with policy, making sure that adjustments and compliance logging are performed under the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "110", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_110_roas": "0.5"',
            '"adset_111_roas": "0.55"',
            '"budget_reduction_pct": "20"',
            '"strategy_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction=(
            "As a portfolio manager, assess ad set 104 ('Fall Fashion - Women') and ad set 111 ('App Installs - iOS') concerning their performance on 2025-08-13. Implement the 'Bid Strategy Optimization Protocol' for both: if either demonstrates high performance (ROAS > 2.5, cost_cap), increase the bid by $5; if any performs poorly (ROAS < 1.0), change the strategy to 'lowest_cost'. Record all modifications with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_104_roas": "11.22"',
            '"adset_111_roas": "0.55"',
            '"adset_104_action": "bid_increase"',
            '"adset_111_action": "strategy_switch"',
            '"changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction=(
            "As a risk manager, recognize that ad set 'App Installs - iOS' (ID 111) is underperforming with a ROAS below 1.0 on 2025-08-13. Apply the bid strategy optimization method to minimize losses by switching it to the 'lowest_cost' strategy. Verify that this adjustment aligns with policy and ensure the adjustment is accurately logged with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_111_roas": "0.55"',
            '"roas_threshold_met": "true"',
            '"old_strategy": "cost_cap"',
            '"new_strategy": "lowest_cost"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction=(
            "As a growth strategist, tackle the 'Electronics - CA' ad set (ID 101) which performed impressively on 2025-08-13 with a ROAS well exceeding 2.5. To leverage this success using optimal bid adjustments, raise the cost cap bid by $5. Make certain the new bid stays under the maximum permitted limit and document the adjustment with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_101_roas": "10.0"',
            '"old_bid": "32.0"',
            '"new_bid": "37.0"',
            '"max_bid_policy": "50"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction=(
            "As the campaign manager for the 'Fall Collection Launch', analyze the performance of every ad set in this campaign for 2025-08-13. Apply the 'Bid Strategy Optimization Protocol' solely to ad sets that meet the criteria (ROAS > 2.5 and cost_cap strategy). Enhance the bid by $5 for each qualifying ad set and record the modification with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"eligible_adsets_found": "1"',
            '"adset_104_roas": "11.22"',
            '"adset_105_eligible": "false"',
            '"adset_104_new_bid": "25.0"',
            '"changes_logged": "1"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction=(
            "You are a performance optimization specialist. Handle a comprehensive assessment of 'cost_cap' ad sets for 2025-08-13. In particular, evaluate ad sets 106 and 108. For any set that surpasses a ROAS of 2.5, implement the 'Bid Strategy Optimization Protocol' by raising its bid by $5. Verify compliance with the maximum bid policy and document all successful modifications using the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_106_roas": "12.0"',
            '"adset_108_roas": "11.28"',
            '"adset_106_new_bid": "23.0"',
            '"adset_108_new_bid": "47.0"',
            '"total_adsets_updated": "2"'
        ]
    ),
        Task(
        annotator="0",
        user_id="USER_016",
        instruction=(
            "You are the head of the Apparel advertising division. Coordinate a bid strategy evaluation for all ad sets within the 'Apparel' category based on the performance of 2025-08-13. Adhere to the bid strategy optimization practice, increasing bids by $5 for any qualifying top-performing 'cost_cap' ad sets. Record all necessary changes with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetsByCategory", kwargs={"category": "Apparel"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"category_adsets_found": "3"',
            '"eligible_adset_count": "1"',
            '"updated_adset_id": "104"',
            '"adset_104_new_bid": "25.0"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction=(
            "As the specialist for the 'Back to School' season, handle ad set 108 ('Back to School - Laptops') which is crucial for the 'Back to School Deals' campaign. On 2025-08-13, employ the 'Bid Strategy Optimization Protocol' to boost its bid by $5 if it qualifies. Begin by confirming its current strategy is 'cost_cap' and ascertain that the new bid stays within the maximum bid policy. Document the modification with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Back to School Deals"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "6"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_108_roas": "11.28"',
            '"eligibility_confirmed": "true"',
            '"old_bid": "42.0"',
            '"new_bid": "47.0"',
            '"max_bid_policy": "50"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction=(
            "As the manager in charge of early holiday promotions, coordinate ad set 106 ('Holiday - Home Goods') from the 'Holiday Season Early Bird' campaign that demonstrates strong potential. Evaluate its performance on 2025-08-13 and refine its bid strategy based on the performance data. Implement the necessary adjustments, ensuring all modifications are documented with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_106_roas": "12.0"',
            '"adset_106_eligible": "true"',
            '"old_bid": "18.0"',
            '"new_bid": "23.0"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_019",
        instruction=(
            "As the manager for the 'Global Summer Sale' campaign, assess your two CA-based ad sets (101 and 102) for their performance on 2025-08-13. It has been reported that any ad set with a ROAS greater than 2.5 and a cost_cap strategy should have its bid increased by $5. Implement suitable bid strategy enhancements based on the performance data and ensure all modifications are documented with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Global Summer Sale"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "1"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_101_roas": "10.0"',
            '"adset_102_roas": "13.22"',
            '"adset_101_eligible": "true"',
            '"adset_102_eligible": "false"',
            '"updated_adset_id": "101"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction=(
            "As a senior analyst tasked with a cross-category performance audit, evaluate the performance of ad set 108 ('Back to School - Laptops') and 111 ('App Installs - iOS') on 2025-08-13. Adhere to the Bid Strategy Optimization practice by increasing the bid by $5 for the leading performer if it is on cost_cap, and altering the strategy to 'lowest_cost' for the underachiever with a ROAS below 1.0. Ensure all activities are logged using the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_108_roas": "11.28"',
            '"adset_111_roas": "0.55"',
            '"adset_108_action": "bid_increase"',
            '"adset_111_action": "strategy_switch"',
            '"total_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction=(
            "As the manager of the 'Back to School' campaign, handle the activation of the newly approved 'Student Laptop Video Ad' (ID 1112) within ad set 108, following standard creative rotation procedures. Also, ensure the existing image ad (1111) is paused. Document the change reason as 'New creative launch'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Back to School Deals"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "6"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "108"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "creative_rotation_window_days"}),
            Action(name="GetLastSuccessfulRun", kwargs={"run_type": "creative_rotation"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1112", "ad_id_to_pause": "1111"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "108", "old_ad_id": "1111", "new_ad_id": "1112", "rationale": "New creative launch"})
        ],
        outputs=[
            '"campaign_id": "6"',
            '"adset_id": "108"',
            '"ad_to_activate": "1112"',
            '"ad_to_pause": "1111"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_022",
        instruction=(
            "In your role as the operations manager, coordinate a performance assessment of all ad sets in the 'Fall Collection Launch' campaign scheduled for 2025-08-13. Utilize Budget Optimization strategies to modify the budgets of ad sets based on their performance, addressing both underperforming and excel-performing ad sets. Be sure to log all modifications correctly with the reason 'plan_2025-08-13' and adhere to budget rounding protocols."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "3"',
            '"adset_104_roas": "11.22"',
            '"adset_105_roas": "11.08"',
            '"adset_104_new_budget": "850.0"',
            '"adset_105_new_budget": "860.0"',
            '"budget_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction=(
            "As the manager for CA apparel, it is your responsibility to handle the creative strategy outlined in the 2025-08-13 plan for ad set 102 ('Apparel - CA'). Following standard practice of creative rotation, ensure the planned creative type is activated. Document the action including a rationale that cites the governing plan."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "creative_rotation_window_days"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "Aligning with plan_2025-08-13 creative strategy"})
        ],
        outputs=[
            '"plan_creative_type": "carousel"',
            '"current_active_ad_type": "image"',
            '"ad_to_activate": "1104"',
            '"ad_to_pause": "1103"',
            '"status": "completed"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction=(
            "As a Senior Analyst, coordinate a comprehensive optimization of ad set 104 for 2025-08-13. Start by aligning it with the daily plan and incorporate a performance bonus. Apply its budget and bid from 'plan_2025-08-13'. Given its exceptionally high ROAS, proceed to apply an additional 15% performance budget increase to the planned budget, documenting this adjustment with the reason 'performance_bonus'. Conclude by verifying the creative's alignment with the plan and recording this check with the rationale 'plan_alignment_verified'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 860.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 750.0, "new_budget": 860.0, "reason": "performance_bonus"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "104"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1106", "rationale": "plan_alignment_verified"})
        ],
        outputs=[
            '"plan_budget_applied": "true"',
            '"performance_bonus_applied": "true"',
            '"final_budget": "860.0"',
            '"creative_alignment_verified": "true"',
            '"total_logs": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction=(
            "You are the CA Market manager overseeing daily operations. It's time to refresh the creative content for ad sets 101 and 102. For each ad set, adhere to the standard creative rotation practice to align their active creatives with the specifications outlined in the `plan_2025-08-13`. Make sure both rotations are documented with 'plan_2025-08-13' as the reason."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_101_planned_creative": "video"',
            '"adset_102_planned_creative": "carousel"',
            '"rotations_executed": "2"',
            '"logs_created": "2"',
            '"status": "completed"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction=(
            "You are a Campaign Restructuring Specialist tasked with consolidating our 'Back to School' efforts. Initiate a new 'Sales' campaign entitled 'Q3_Education_Push'. Subsequently, establish a new ad set within this campaign by replicating all settings (name, category, budget, bid strategy, and bid amount) from the current 'Back to School - Laptops' ad set (ID 108). You must also transfer its ads by generating new ads with identical names and creative types in the new ad set. Finally, to finalize the migration, you must pause the entire original 'Back to School Deals' campaign."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CreateCampaign", kwargs={"name": "Q3_Education_Push", "objective": "Sales"}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Back to School - Laptops", "category": "Electronics", "daily_budget": 780.0, "bid_strategy": "cost_cap", "bid_amount": 42.0}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "108"}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Student Laptop Deals", "creative_type": "image"}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Student Laptop Video Ad", "creative_type": "video"}),
            Action(name="UpdateCampaignStatus", kwargs={"campaign_id": "6", "status": "paused"})
        ],
        outputs=[
            '"original_adset_cloned": "108"',
            '"new_campaign_id": "11"',
            '"new_adset_id": "113"',
            '"ads_migrated": "2"',
            '"original_campaign_paused": "true"',
            '"migration_status": "complete"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_027",
        instruction=(
            "As a Creative Performance Analyst, the daily agenda for 'plan_2025-08-13' proposes an 'image' creative for ad set 104. However, you should supersede this following the 'video_cpa_advantage_pct' policy. Use the customary creative rotation procedure to put the video creative (ad 1107) into action. The justification should be 'Policy-driven video prioritization'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "104"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "creative_rotation_window_days"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="GetLastSuccessfulRun", kwargs={"run_type": "creative_rotation"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1107", "ad_id_to_pause": "1106"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1107", "rationale": "Policy-driven video prioritization"})
        ],
        outputs=[
            '"plan_creative_type": "image"',
            '"policy_override_justification": "video_cpa_advantage_pct"',
            '"creative_rotation_window_days": "7"',
            '"last_rotation_date": "2025-08-14"',
            '"adset_104_performance": "8300.0 revenue, 740.0 spend"',
            '"ad_to_activate": "1107"',
            '"ad_to_pause": "1106"',
            '"rotation_logged": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction=(
            "You are an Ad Operations Specialist. Your responsibility is to coordinate the scheduled creative rotation for ad set 102 according to 'plan_2025-08-13'. Prior to proceeding, ensure to list all ads within that ad set to verify the activation of the correct, non-archived ad ('Summer T-Shirt Carousel'). Then, employ the standard creative rotation procedure and document it as 'Plan compliance: activating carousel creative' for records."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "Plan compliance: activating carousel creative"})
        ],
        outputs=[
            '"plan_creative_type": "carousel"',
            '"total_ads_in_adset": "3"',
            '"archived_ad_ignored": "1118"',
            '"ad_activated": "1104"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction=(
            "You are the Automation Orchestrator for the 'Global Summer Sale' campaign. Manage the plan execution process for ad set 101 ('Electronics - CA') following 'plan_2025-08-13'. Ensure to verify the plan, implement the changes for both budget and bid strategy, and document each step taken."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetCampaignByName", kwargs={"name": "Global Summer Sale"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget_updated": "true"',
            '"bid_strategy_updated": "true"',
            '"changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction=(
            "You are the daily operations lead. The plan for ad set 102 ('Apparel - CA') necessitates only a modification in the budget. Conduct plan execution best practice for ad set 102 according to 'plan_2025-08-13'. Apply the budget alteration and record it. Additionally, confirm and document the bid strategy status, despite no modification being needed, to uphold complete audit compliance."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_id": "102"',
            '"budget_change_required": "true"',
            '"strategy_change_required": "false"',
            '"new_budget": "600.0"',
            '"status": "completed"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction=(
            "Ensure management over the 'Fall Collection Launch' campaign. Your responsibility is to utilize the 'plan_2025-08-13' for ad set 104. Carry out the plan execution practice by incorporating all designated budget and bid amount modifications and documenting them with the appropriate reason."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_id": "104"',
            '"old_budget": "740.0"',
            '"new_budget": "750.0"',
            '"old_bid": "20.0"',
            '"new_bid": "22.0"',
            '"changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_032",
        instruction=(
            "Oversee the new 'Fall Collection Launch' campaign's management. Implement the daily plan 'plan_2025-08-13' for the 'Fall Fashion - Men' ad set (105). As this is a novel and continuously observed ad set, conduct the plan execution practice and verify that the present budget and bid strategy conform to the plan, recording both actions as 'no change' for documentation."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "3"',
            '"adset_id": "105"',
            '"plan_budget": "750.0"',
            '"current_budget": "750.0"',
            '"action": "no_change_required"',
            '"logs_created": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction=(
            "As a senior ad ops specialist in charge of high-budget campaigns, it is your responsibility to first verify that the parent campaign ('Mobile App Installs Campaign') is active before proceeding with the plan execution best practice for ad set 111 as specified in 'plan_2025-08-13'. If the campaign is indeed active, continue to implement and record all planned modifications, including those that are 'no-ops'. It is essential to update the adset budget and bid strategy, even for no-op changes, to ensure comprehensive audit compliance."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "7"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 1000.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5, "new_bid": 2.5, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_status": "active"',
            '"pre_check_passed": "true"',
            '"adset_id": "111"',
            '"budget_change_required": "false"',
            '"strategy_change_required": "false"',
            '"logs_created": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction=(
            "As a compliance specialist, your task involves applying the plan 'plan_2025-08-13' for ad set 108 ('Back to School - Laptops'), making sure the new bid remains within the boundaries of the 'max_bid_amount' policy. Start the 'Plan Execution Protocol' by reviewing the policy, followed by implementing and documenting the budget and strategy modifications."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 45.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_id": "108"',
            '"planned_bid": "45.0"',
            '"max_bid_policy": "50"',
            '"policy_check_passed": "true"',
            '"execution_status": "completed"'
        ]
    ),
     
    Task(
        annotator="0",
        user_id="USER_035",
        instruction=(
            "As the System Reliability Engineer, your responsibility is to guarantee platform stability and optimal performance for 2025-08-13. Examine the recent automation run history for any failures that might suggest systemic problems. Simultaneously, carry out a system-wide performance audit. For any ad sets failing to meet the 1.5 ROAS minimum, utilize the budget and bidding optimization practice to return them to profitability. Ensure all corrective measures are thoroughly logged under the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAutomationRunHistory", kwargs={"status": "failed"}),
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"failed_runs_found": "1"',
            '"underperforming_adsets": "[\\"103\\", \\"110\\", \\"111\\"]"',
            '"budget_adjustments_made": "3"',
            '"strategy_adjustments_made": "1"',
            '"total_changes_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction=(
            "In your role as a Senior Performance Analyst, carry out a cross-campaign audit for 2025-08-13, concentrating on a combination of high and low-performing ad sets: 101, 104, and 111. Your task is to implement comprehensive optimizations based on each ad set's performance tier. Employ the standard best practices for both budget and bid strategy adjustments to maximize successes and reduce losses. Make sure every amendment is accurately logged with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"top_performers_optimized": "2"',
            '"underperformers_optimized": "1"',
            '"budget_changes_logged": "3"',
            '"strategy_changes_logged": "3"',
            '"total_optimizations_logged": "6"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction=(
            "As the Creative Manager for the 'Fall Collection Launch' campaign, it's essential to harness the campaign's strong momentum. Your objective is to introduce a new video creative to further enhance performance. Once you've confirmed the parent campaign is active, proceed to launch a new ad titled 'Fall Dress Collection Video v2' within ad set 104. Next, apply the standard creative rotation process to activate the new video, and pause the existing image ad (ID 1106). Provide justification for this strategic transition in the logs with the explanation: 'Capitalizing on high performance with new video creative'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_creative_types"}),
            Action(name="CreateAd", kwargs={"adset_id": "104", "name": "Fall Dress Collection Video v2", "creative_type": "video"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "104"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1106"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1119", "rationale": "Capitalizing on high performance with new video creative"})
        ],
        outputs=[
            '"campaign_status": "active"',
            '"adset_104_roas": "11.22"',
            '"new_ad_created_id": "1119"',
            '"creative_rotation_status": "success"',
            '"log_status": "success"'
        ]
    ),

    Task(
       annotator="0",
        user_id="USER_038",
        instruction=(
            "As the lead for CA Electronics, your main task is to execute the entire strategic plan ('plan_2025-08-13') for the 'Electronics - CA' ad set (101). You must adhere to the complete plan execution protocol, ensuring all specified budget, bid, and creative adjustments are correctly implemented and audited. Additionally, use plan_2025-08-13 as the justification for creative rotation."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget_updated": "true"',
            '"bid_strategy_updated": "true"',
            '"creative_rotated": "true"',
            '"total_logs_created": "3"'
        ]
    ),
    Task(
       annotator="0",
        user_id="USER_039",
        instruction=(
            "As the manager of the 'Fall Collection Launch' campaign, you are tasked with leveraging its strong initial performance. Utilize our standard reward practices for performance on the Men's (105) and Women's (104) ad sets based on their 2025-08-13 results. This entails increasing budgets for these top performers by 15% and raising their bid by $5 for those utilizing a cost_cap strategy. Ensure that all modifications are documented and comply with rounding policies."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "3"',
            '"adsets_optimized": "2"',
            '"adset_104_roas": "11.22"',
            '"adset_105_roas": "11.08"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "1"'
        ]
    ),
    Task(
       annotator="0",
        user_id="USER_040",
        instruction=(
            "As the manager of the 'Mobile App Installs' campaign, you need to address its inefficiency displayed on 2025-08-13 (ad sets 110 & 111). Implement standard corrective actions for underperforming assets to both ad sets. This requires a 20% reduction in their budgets and changing any with a 'cost_cap' strategy to 'lowest_cost' to prevent additional losses. Log all changes thoroughly."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adsets_underperforming": "2"',
            '"adset_110_roas": "0.5"',
            '"adset_111_roas": "0.55"',
            '"budget_reductions_made": "2"',
            '"strategy_switches_made": "1"',
            '"no_op_strategy_logs": "1"'
        ]
    ),
    Task(
       annotator="0",
        user_id="USER_041",
        instruction=(
            "As the manager overseeing the 'Holiday Season Early Bird' campaign, which requires an enhancement in performance, your responsibility is to pinpoint the single ad set with the best performance utilizing a 'cost_cap' strategy within this campaign. After you determine it, proceed to apply our standard reward protocols concerning its budget (with a 15% increase) and bid (with an increase of $5) based on its 2025-08-13 performance, ensuring the adjusted bid adheres to the max bid policy."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "5"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"eligible_adset_id": "106"',
            '"adset_106_roas": "12.0"',
            '"adset_106_new_budget": "580.0"',
            '"adset_106_new_bid": "23.0"',
            '"max_bid_policy_ok": "true"',
            '"optimizations_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction=(
            "As a Senior Performance Analyst, you are tasked with coordinating a graduated optimization across several ad sets for 2025-08-13. For the ad set with exceptional performance (ad set 102, ROAS > 12), enact a 20% budget increase. For the strong-performing set (ad set 101, ROAS > 8), apply a 15% boost in budget. For the critically underperforming ad set (ad set 111, ROAS < 1), decrease its budget by 20% and change its strategy to 'lowest_cost'. Ensure that all actions are documented."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 710.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 710.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"exceptional_performer_optimized": "102"',
            '"strong_performer_optimized": "101"',
            '"underperformer_optimized": "111"',
            '"budget_changes_logged": "3"',
            '"strategy_changes_logged": "1"'
        ]
    ),    
    Task(
       annotator="0",
        user_id="USER_043",
        instruction=(
            "As a senior portfolio manager in charge of major seasonal initiatives, you must enhance two high-performing ad sets from different campaigns: 'Back to School - Laptops' (108) and 'Holiday - Home Goods' (106). For these, apply our usual reward protocol based on their 2025-08-13 performance: raise their budgets by 15% and increase their cost_cap bids by $5, making sure all modifications are logged."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adsets_optimized": "2"',
            '"adset_108_roas": "11.28"',
            '"adset_106_roas": "12.0"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction=(
            "You are tasked with ensuring the system's health. Conduct a comprehensive check for any underperforming ad sets on 2025-08-13 using the set 1.5 ROAS threshold. For each detected ad set, carry out the budget optimization method to decrease their budgets by 20%. Adhere to all rounding and logging standards, citing the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"underperforming_adsets": "[\\"103\\", \\"110\\", \\"111\\"]"',
            '"adset_103_roas": "0.0"',
            '"adset_103_new_budget": "940.0"',
            '"total_adsets_adjusted": "3"',
            '"budget_changes_logged": "3"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_045",
        instruction=(
            "You are a compliance analyst tasked with conducting a spot check on the 'Fall Fashion - Men' ad set (105). Begin by verifying that its current budget and bid strategy are aligned with 'plan_2025-08-13', documenting these verifications using the standard reason code. After confirming compliance, evaluate its performance on 2025-08-13 and employ the standard budget optimization protocol if it qualifies as a top performer, while once again using the standard reason code for any changes."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"plan_compliance_verified": "true"',
            '"adset_105_roas": "11.08"',
            '"performance_optimization_triggered": "true"',
            '"new_budget": "860.0"',
            '"total_logs_created": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction=(
            "You are a risk manager examining the 'Q3 Brand Awareness Push' campaign. The ad set (103) within this campaign reported zero revenue on 2025-08-13. Although a zero ROAS is expected for an 'Awareness' objective, you must still carry out the complete Budget Optimization practice to ensure cost efficiency. Specifically execute the practice for ad set 103 only (do not process other underperforming ad sets) and ensure any resulting budget changes are recorded with the standard reason code."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "2"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_objective": "Awareness"',
            '"adset_roas": "0.0"',
            '"protocol_followed": "true"',
            '"action_taken": "budget_reduction"',
            '"new_budget": "940.0"'
        ]
    ),
    
    Task(
        annotator="0",
        user_id="USER_047",
        instruction=(
            "As the Portfolio Manager for all Sales-objective campaigns, your role is to carry out a thorough performance assessment for ad set 101 ('Electronics - CA') and ad set 108 ('Back to School - Laptops') on 2025-08-13. Given that both ad sets are top performers, it's necessary to implement our standard methods for rewarding success concerning both their budgets and bid strategies. Make sure all budget increases (15%) and bid increments ($5 for cost_cap) comply with rounding and maximum bid policies, and document every step using the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_101_roas": "10.0"',
            '"adset_108_roas": "11.28"',
            '"adsets_optimized": "2"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "2"',
            '"total_changes_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction=(
            "As the System Reliability Engineer, your main responsibility is to look into the recent failed automation run. Once the failed run is identified, coordinate a system-wide health examination for 2025-08-13. For any ad sets that do not meet our minimum ROAS of 1.5, apply the usual corrective measures to their budgets and bid strategies to enhance cost-efficiency. Record all modifications made."
        ),
        actions=[
            Action(name="GetAutomationRunHistory", kwargs={"status": "failed", "limit": 1}),
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"failed_run_id": "AR-20250812-01"',
            '"underperforming_adsets_found": "3"',
            '"budget_reductions_made": "3"',
            '"strategy_switches_made": "1"',
            '"total_corrective_logs": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction=(
            "As the Head of Automation, your responsibility is to implement the comprehensive daily strategy for the 'Fall Collection Launch' campaign as detailed in 'plan_2025-08-13'. For each ad set in the campaign (104 and 105), ensure the application of the designated budget and bid strategy. In order to maintain a thorough audit trail, it is essential to log each potential modification for both ad sets, even if the values remain unchanged (a 'no-op' change)."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "3"',
            '"adsets_processed": "2"',
            '"budget_updates_applied": "2"',
            '"strategy_updates_applied": "2"',
            '"total_logs_created": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction=(
            "Being a Creative Director launching a new A/B test, your role is to establish a new campaign named 'Q4 Gaming Push' with an 'Awareness' objective. Within this campaign, formulate one ad set named 'Gaming Mouse Promo' for the 'Electronics' category with a starting budget of $1200. Subsequently, generate two new ad creatives in this ad set: one image titled 'Gaming Mouse Static v1' and one video titled 'Gaming Mouse Action v1'. Lastly, adhere to our standard procedure by activating the video ad and pausing the image ad to initiate the test, documenting the rotation with the rationale 'Initial A/B test launch'."
        ),
        actions=[
            Action(name="CreateCampaign", kwargs={"name": "Q4 Gaming Push", "objective": "Awareness"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "default_bid_strategy"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Gaming Mouse Promo", "category": "Electronics", "daily_budget": 1200.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Gaming Mouse Static v1", "creative_type": "image"}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Gaming Mouse Action v1", "creative_type": "video"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1120", "ad_id_to_pause": "1119"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "113", "old_ad_id": "1119", "new_ad_id": "1120", "rationale": "Initial A/B test launch"})
        ],
        outputs=[
            '"new_campaign_id": "11"',
            '"new_adset_id": "113"',
            '"new_ad_ids": "[\\"1119\\", \\"1120\\"]"',
            '"active_ad_for_test": "1120"',
            '"rotation_logged": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction=(
            "As a Senior Analyst, handle a comprehensive optimization on ad set 101 for 2025-08-13. Initially, synchronize it with the daily plan and subsequently include a performance bonus. Apply its budget and bid from 'plan_2025-08-13'. Given its strong ROAS, proceed with a further 15% performance budget increase beyond the planned budget, documenting this additional adjustment with the reason 'performance_bonus'. Lastly, implement the creative rotation indicated in the plan."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1090.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 950.0, "new_budget": 1090.0, "reason": "performance_bonus"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"plan_applied": "true"',
            '"performance_bonus_applied": "true"',
            '"final_budget": "1090.0"',
            '"creative_rotated": "true"',
            '"total_logs": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction=(
            "As the manager overseeing the 'Global Summer Sale' campaign, today you must coordinate the complete daily strategy for ad sets 101, 102, and 112 as detailed in 'plan_2025-08-13'. This entails implementing all specified modifications to budgets, bids, and active creatives to ensure full plan alignment for all three ad sets. Make sure every action is documented."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 700.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"adsets_processed": "3"',
            '"budget_changes_logged": "3"',
            '"strategy_changes_logged": "3"',
            '"creative_rotations_applied": "2"',
            '"total_logs_created": "8"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction=(
            "As a Performance Analyst, your role requires a comprehensive analysis of the 'Electronics' category for 2025-08-13. Establish a link between ad performance and sales data. Start by obtaining the weekly sales statistics for Electronics. Next, for the active 'Electronics' ad sets (101, 108, 112), determine their ROAS. Utilizing this information, execute our standard budget modifications to raise the budget of the highest ROAS performer by 15% and reduce the budget of the lowest ROAS performer by 20%."
        ),
        actions=[
            Action(name="GetWeeklySalesByCategory", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 810.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 740.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 810.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 740.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"weekly_electronics_revenue": "455000"',
            '"top_performer_id": "112"',
            '"lowest_performer_id": "101"',
            '"adset_112_new_budget": "810.0"',
            '"adset_101_new_budget": "740.0"',
            '"optimizations_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_054",
        instruction=(
            "As the newly appointed mobile app campaign manager, address the issue of ad sets 110 and 111, which are underperforming with ROAS below 1.5 as of 2025-08-13. Apply the 'Budget Optimization Protocol' specifically to ad sets 110 and 111 solely. Refrain from altering other underperforming ad sets that might be discovered; concentrate exclusively on ad sets 110 and 111. Ensure adherence to minimum budget allocation guidelines and accurate documentation of all modifications."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_110_roas": "0.5"',
            '"adset_111_roas": "0.55"',
            '"min_budget_policy": "100"',
            '"new_budget_valid": "true"',
            '"total_adsets_updated": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction=(
            "As a Compliance Officer, you are tasked with confirming the validity of the planned bid increase for ad set 108 in 'plan_2025-08-13'. Begin by verifying that the proposed bid adheres to our maximum bid policy and ensure that its parent campaign ('Back to School Deals') is presently active. Provided that these initial checks are cleared, proceed with applying all intended budget and strategy modifications for that ad set. Document every step taken, including a detailed explanation 'Compliance check passed' for the final strategy alteration log."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="GetCampaignByName", kwargs={"name": "Back to School Deals"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 45.0, "reason": "Compliance check passed"})
        ],
        outputs=[
            '"planned_bid": "45.0"',
            '"max_bid_policy": "50"',
            '"campaign_status": "active"',
            '"pre_checks_passed": "true"',
            '"execution_completed": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction=(
            "Being the manager for all UK marketing, you must address the price reduction for the 'Laptop Pro' (product_id 2) that was implemented on 2025-08-14. Your responsibility includes enhancing the 'Electronics - UK' ad set (112) according to its performance on 2025-08-13. Start by confirming the price adjustment. Next, determine the ad set's current ROAS. Conclude by implementing our customary 15% budget increase for top performers, and due to its strategy being 'lowest_cost', record a 'no-op' strategy alteration to validate your review. Make sure to record all steps."
        ),
        actions=[
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "2", "date": "2025-08-13"}),
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "2", "date": "2025-08-14"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 810.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 810.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"price_drop_confirmed": "true"',
            '"old_price": "1599.99"',
            '"new_price": "1499.99"',
            '"adset_112_roas": "12.57"',
            '"new_budget": "810.0"',
            '"logs_created": "2"'
        ]
    ),
    
    Task(
        annotator="0",
        user_id="USER_057",
        instruction=(
            "As the lead for seasonal promotions, handle the 'Holiday Season Early Bird' campaign to align completely with the daily strategy for '2025-08-13'. Implement all planned budget and bid strategy modifications for every ad set within this campaign. For creative alignment, validate that the active creative type corresponds with the plan, and record this verification for each ad set using the exact rationale string 'plan_alignment_verified'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "5"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "106"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "106", "old_ad_id": "1109", "new_ad_id": "1109", "rationale": "plan_alignment_verified"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "107", "old_ad_id": "1110", "new_ad_id": "1110", "rationale": "plan_alignment_verified"})
        ],
        outputs=[
            '"campaign_id": "5"',
            '"adsets_processed": "2"',
            '"budget_logs_created": "2"',
            '"strategy_logs_created": "2"',
            '"creative_logs_created": "2"',
            '"full_alignment_confirmed": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction=(
            "As a growth strategist concentrating on the CA market, coordinate a 15% budget increase for ad set 102 ('Apparel - CA'), which exhibited outstanding performance on 2025-08-13. Simultaneously, confirm its active creative aligns with the type specified in the 'plan_2025-08-13' to stimulate additional growth. Log all actions taken."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "Aligning with plan_2025-08-13 creative strategy"})
        ],
        outputs=[
            '"adset_102_roas": "13.22"',
            '"budget_increased": "true"',
            '"new_budget": "680.0"',
            '"creative_aligned_to_plan": "true"',
            '"total_logs_created": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_059",
        instruction=(
            "You are a Bidding Specialist. Handle a system-wide evaluation of ad sets 101, 104, and 108, each utilizing a 'cost_cap' bid strategy. For any of these ad sets that surpassed our top-performance ROAS threshold of 2.5 on 2025-08-13, apply our standard bid increase practice to capitalize on their performance. Ensure all modifications adhere to the maximum bid policy and are documented."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"eligible_adsets_found": "3"',
            '"bids_increased": "3"',
            '"max_bid_policy_respected": "true"',
            '"strategy_changes_logged": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction=(
            "You are a Performance Analyst tasked with investigating an anomaly. Ad set 103, part of the 'Q3 Brand Awareness Push' campaign, exhibited significant spend but no revenue on 2025-08-13. Begin by confirming the campaign's objective. Regardless of the verified objective, apply our standard 20% budget cut for underperforming assets. Lastly, ensure its current creative matches the daily plan, documenting the check with the exact rationale 'verification:plan_sync_ok'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "103"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "103", "old_ad_id": "1105", "new_ad_id": "1105", "rationale": "verification:plan_sync_ok"})
        ],
        outputs=[
            '"campaign_objective": "Awareness"',
            '"budget_reduction_applied": "true"',
            '"creative_alignment_verified": "true"',
            '"no_op_creative_log_created": "true"',
            '"total_logs": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction=(
            "As the campaign lead for seasonal promotions, the 'Holiday Season Early Bird' campaign is of utmost importance. Examine the performance of its constituent ad sets for 2025-08-13. Assess performance data and adjust budgets based on ROAS performance, ensuring all documentation and compliance with established policies are maintained. Follow all logging and rounding procedures using 'plan_2025-08-13' as the rationale. For budget increases, adjust to the nearest $10 increment to ensure sufficient funds for high-performing ad sets."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "5"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 460.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 460.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "5"',
            '"adset_106_roas": "12.0"',
            '"adset_107_roas": "12.5"',
            '"adset_106_new_budget": "580.0"',
            '"adset_107_new_budget": "460.0"',
            '"total_budget_increase": "140.0"',
            '"budget_rounding_unit": "10"',
            '"status": "completed"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_062",
        instruction=(
            "Being a Senior Portfolio Manager, your role requires a cross-campaign optimization for 2025-08-13. Address both a top-performing asset, ad set 106, and an underperforming one, ad set 111. Utilize our standard practice to enhance the success of the former and reduce the losses of the latter across their budgets and bid strategies. Record all adjustments."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"top_performer_optimized": "106"',
            '"underperformer_optimized": "111"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "2"',
            '"total_adjustments_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction=(
            "As a Performance Analyst, our sales report for the week commencing 2025-08-07 highlights robust results in the 'Apparel' category. To capitalize on this trend, it's essential to review every ad set in this category. For each ad set with a ROAS exceeding 10.0 on 2025-08-13, implement our routine 15% budget boost for top achievers. Make sure all modifications are recorded."
        ),
        actions=[
            Action(name="GetWeeklySalesByCategory", kwargs={"category": "Apparel", "start_date": "2025-08-07"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Apparel"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"weekly_apparel_revenue": "120000"',
            '"eligible_adsets_found": "3"',
            '"budgets_increased": "3"',
            '"budget_changes_logged": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction=(
            "As a performance analyst, ad set 'Apparel - CA' (ID 102) requires a performance assessment on 2025-08-13. Handle the 'Budget Optimization Protocol' to adjust its budget based on performance metrics. Prior to applying any modifications, confirm and adhere to the 'budget_rounding_unit' policy. Ensure the adjustment is logged correctly with the rationale 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_102_roas": "13.22"',
            '"old_budget": "590.0"',
            '"new_budget": "680.0"',
            '"budget_rounding_unit": "10"',
            '"log_status": "success"'
        ]
    ),        
    Task(
        annotator="0",
        user_id="USER_065",
        instruction=(
            "As a senior strategist, you are tasked with examining sequential optimizations. For ad set 101, the plan on 2025-08-13 continues the aggressive growth approach. Initially, verify that its performance on the 13th supports this ongoing investment by checking its ROAS. If it maintains its top performance, continue with the complete plan, implementing all defined changes to its budget, bid, and active creative to sustain momentum."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"performance_check_passed": "true"',
            '"adset_101_roas": "10.0"',
            '"plan_execution_status": "completed"',
            '"total_changes_logged": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction=(
            "As a Risk Manager, you need to address a performance crisis. On 2025-08-13, ad set 111 is significantly underperforming the threshold. Implement our capital preservation policy by removing exactly $500 from its budget and shifting to the 'lowest_cost' strategy. Then, redirect those saved funds to a reliable top performer, ad set 104, to enhance portfolio returns. Confirm that all resulting modifications are accurately recorded."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 500.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 1240.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 1240.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"reallocation_complete": "true"',
            '"adset_111_new_budget": "500.0"',
            '"adset_104_new_budget": "1240.0"',
            '"adset_111_strategy_switched": "true"',
            '"total_logs_created": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction=(
            "As a Portfolio Manager in charge of budget efficiency, your review of the data from 2025-08-13 indicates a chance to redistribute funds. You are to transfer exactly $300 from the budget of the 'Apparel' ad set that is underperforming, and allocate it to the 'Electronics' ad set that is excelling. Document both budget adjustments."
        ),
        actions=[
            Action(name="GetAdsetsByCategory", kwargs={"category": "Apparel"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 450.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 1000.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 450.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 1000.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"source_adset_id": "105"',
            '"destination_adset_id": "112"',
            '"amount_reallocated": "300.0"',
            '"budget_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction=(
            "In your role as a Creative Analyst, adhere to our policy that favors video creatives due to their superior performance. For ad set 108, ensure that the currently active creative complies with this policy, even if the daily agenda for 2025-08-13 suggests using another type of creative. Record this action with the specific rationale string 'policy_override:video_cpa_advantage'."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "108"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1112", "ad_id_to_pause": "1111"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "108", "old_ad_id": "1111", "new_ad_id": "1112", "rationale": "policy_override:video_cpa_advantage"})
        ],
        outputs=[
            '"plan_creative_type": "image"',
            '"policy_value": "10"',
            '"override_executed": "true"',
            '"activated_ad_id": "1112"',
            '"rotation_logged": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction=(
            "As a Campaign Specialist, you are overseeing the launch of the 'Q4 Home Goods' initiative. Your obligation is to initiate a new 'Sales' campaign under that exact title. Inside it, establish two new ad sets: first, label one as 'Home_Decor_Q4' within the 'Home' category, allocating a $450 budget; second, designate the other as 'Office_Supplies_Q4' in the 'Office' category with a $250 budget. For each ad set that you create, ensure to create and activate an image ad titled in the format '[AdSetName]_Image_1'. Ensure the complete setup is logged."
        ),
        actions=[
            Action(name="CreateCampaign", kwargs={"name": "Q4 Home Goods", "objective": "Sales"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "default_bid_strategy"}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Home_Decor_Q4", "category": "Home", "daily_budget": 450.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Office_Supplies_Q4", "category": "Office", "daily_budget": 250.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Home_Decor_Q4_Image_1", "creative_type": "image"}),
            Action(name="CreateAd", kwargs={"adset_id": "114", "name": "Office_Supplies_Q4_Image_1", "creative_type": "image"}),
            Action(name="UpdateAdStatus", kwargs={"ad_id": "1119", "status": "active"}),
            Action(name="UpdateAdStatus", kwargs={"ad_id": "1120", "status": "active"})
        ],
        outputs=[
            '"new_campaign_id": "11"',
            '"adsets_created": "2"',
            '"ads_created": "2"',
            '"ads_activated": "2"',
            '"setup_status": "complete"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction=(
            "Your role as a Risk Manager involves executing a performance triage for 2025-08-13. Locate any ad sets displaying a ROAS lower than 1.5. For the ad sets identified, implement a 20% cut in budget. Additionally, if any of those ad sets show a ROAS under 1.0, confirm their bid strategy is adjusted to 'lowest_cost'. Document every action performed."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"underperforming_adsets_found": "3"',
            '"budget_changes_logged": "3"',
            '"strategy_changes_logged": "1"',
            '"total_optimizations_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction=(
            "As a Performance Analyst, you are tasked with examining weekly trends for ad set 101. Contrast its overall spend for the latest week (2025-08-07 to 2025-08-13) with the preceding week (2025-07-31 to 2025-08-06). Upon determining its ROAS for 2025-08-13, if there's an increase in spend week-over-week AND the ROAS is less than 11.0, you need to implement a 20% budget reduction as a remedial action and record the adjustment."
        ),
        actions=[
            Action(name="GetAdsetSpendForDateRange", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange", kwargs={"adset_id": "101", "start_date": "2025-07-31", "end_date": "2025-08-06"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 740.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 740.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"recent_week_spend": "6140.0"',
            '"prior_week_spend": "0.0"',
            '"roas_for_2025_08_13": "10.0"',
            '"conditions_met_for_action": "true"',
            '"action_taken": "budget_reduction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction=(
            "As a Compliance Officer, your responsibility is to conduct a lookback verification on ad set 102. Ensure that its current budget and bid strategy align with the allocations defined in the prior day's plan, 'plan_2025-08-12'. Document the results of this verification for both budget and strategy, applying the exact rationale string 'compliance_lookback_ok' for each log entry."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-12"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "102"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 590.0, "reason": "compliance_lookback_ok"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "compliance_lookback_ok"})
        ],
        outputs=[
            '"current_budget": "590.0"',
            '"plan_budget": "590.0"',
            '"budget_match": "true"',
            '"strategy_match": "true"',
            '"logs_created": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction=(
            "As the Campaign Manager for 'Global Summer Sale', you need to reactivate the paused video ad in the 'Electronics - CA' ad set. Start by adjusting the budget of the ad set to $950. Subsequently, locate the paused ad within the set and update its status to 'active'. Document the budget modification citing the reason 'reactivation_budget_adjustment'."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Global Summer Sale"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "1"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "reactivation_budget_adjustment"}),
            Action(name="UpdateAdStatus", kwargs={"ad_id": "1102", "status": "active"})
        ],
        outputs=[
            '"adset_budget_updated": "true"',
            '"ad_to_activate": "1102"',
            '"ad_status_updated": "true"',
            '"reactivation_complete": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction=(
            "In your role as a Senior Analyst, coordinate a full-stack optimization for ad set 104 scheduled for 2025-08-13. Initially, ensure it aligns with the daily plan and subsequently add a performance bonus. Utilize the budget and bid from 'plan_2025-08-13'. Given that its ROAS is notably high, apply an extra 15% performance budget increase beyond the planned budget, and log this secondary adjustment with the reason 'performance_bonus'. Lastly, confirm that its creative aligns with the plan and record this verification with the justification 'plan_alignment_verified'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 860.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 750.0, "new_budget": 860.0, "reason": "performance_bonus"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "104"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1106", "rationale": "plan_alignment_verified"})
        ],
        outputs=[
            '"plan_budget_applied": "true"',
            '"performance_bonus_applied": "true"',
            '"final_budget": "860.0"',
            '"creative_alignment_verified": "true"',
            '"total_logs": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction=(
            "As a Data Scientist, you theorize that increased user engagement is a predictor of sales. Examine the viewership numbers for the 'Toys' category on 2025-08-13. Should sessions surpass 5,000 and the related ad set 107 display a ROAS greater than 10.0, validate your theory by boosting the budget by 20% to leverage the demand. Record any budget adjustments with the specific reason 'data_driven_increase'."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 480.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 480.0, "reason": "data_driven_increase"})
        ],
        outputs=[
            '"user_sessions": "6000"',
            '"roas": "12.5"',
            '"hypothesis_confirmed": "true"',
            '"budget_increased": "true"',
            '"budget_change_logged": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction=(
            "Serving as a Finance Manager, ensure that the 'Global Summer Sale' campaign's total daily budget does not surpass $2250. Evaluate the performance of its ad sets (101, 102, 112) on 2025-08-13. Raise the budget of the highest-performing ad set by 15%, and then reduce the budget of the least successful to keep the total campaign budget within the $2250 limit. Document every adjustment made."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Global Summer Sale"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "1"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 870.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 870.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"top_performer": "102"',
            '"lowest_performer": "101"',
            '"budget_increase": "90.0"',
            '"budget_decrease": "50.0"',
            '"final_campaign_budget": "2250.0"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_077",
        instruction=(
            "You are a Portfolio Optimizer. To maximize ROI, handle the reallocation of funds based on 2025-08-13 performance. Reduce the budget of each ad set with a ROAS below 1.0 by exactly $200. Subsequently, compile this entire amount and allocate it to the highest-performing ad set on that day. Record all resulting budget adjustments."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.0, "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 980.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 1190.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 980.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 1190.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"underperformers_identified": "3"',
            '"top_performer_identified": "102"',
            '"funds_reallocated": "600.0"',
            '"budget_changes_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction=(
            "You are a Campaign Architect. Initiate a new 'Lead Generation' campaign named exactly 'Webinar_Signups_Fall_2025'. Set up an ad set within it called 'Tech_Webinar_Promo' targeting the 'Electronics' category. Coordinate this new ad set using the system's default policies for 'default_bid_strategy' and 'min_budget_allocation'. Afterward, develop and activate a single video ad named 'Webinar_Invite_Video'."
        ),
        actions=[
            Action(name="CreateCampaign", kwargs={"name": "Webinar_Signups_Fall_2025", "objective": "Lead Generation"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "default_bid_strategy"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Tech_Webinar_Promo", "category": "Electronics", "daily_budget": 100.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="CreateAd", kwargs={"adset_id": "113", "name": "Webinar_Invite_Video", "creative_type": "video"}),
            Action(name="UpdateAdStatus", kwargs={"ad_id": "1119", "status": "active"})
        ],
        outputs=[
            '"new_campaign_id": "11"',
            '"new_adset_id": "113"',
            '"default_budget_used": "100.0"',
            '"default_strategy_used": "lowest_cost"',
            '"ad_activated": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction=(
            "As a Market Analyst, your objective is to reward the category demonstrating the strongest growth. Begin by determining the product category that achieved the highest weekly revenue for the week commencing 2025-08-07. Next, locate the top-performing ad set (based on ROAS on 2025-08-13) within that leading category. Implement our standard 15% budget increase for this ad set to enhance its success. Document the modification."
        ),
        actions=[
            Action(name="GetWeeklySalesByCategory", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="GetWeeklySalesByCategory", kwargs={"category": "Apparel", "start_date": "2025-08-07"}),
            Action(name="GetWeeklySalesByCategory", kwargs={"category": "Home", "start_date": "2025-08-07"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 810.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 810.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"winning_category": "Electronics"',
            '"top_adset_in_category": "112"',
            '"adset_112_roas": "12.57"',
            '"budget_increase_applied": "true"',
            '"log_status": "success"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction=(
            "Serving as the 'Back to School' campaign manager, you need to ensure that ad set 108 aligns perfectly with 'plan_2025-08-13' in all aspects: budget, bid, and creative. Execute all necessary adjustments and maintain a complete audit trail by documenting each action executed."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 45.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"budget_aligned": "true"',
            '"strategy_aligned": "true"',
            '"creative_already_aligned": "true"',
            '"total_logs_created": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction=(
            "As a Crisis Manager, it's been noted by system monitoring that on 2025-08-13, the 'Mobile App Installs Campaign' has hit a performance crisis, with its ad sets showing a critically low ROAS below 1.0. You are required to promptly implement our capital preservation procedures: pause every active ad to stop all expenditures. Furthermore, as a measure to control costs, make sure to adjust ad set 111's strategy to 'lowest_cost' and record the modification."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "7"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "110"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdStatus", kwargs={"ad_id": "1114", "status": "paused"}),
            Action(name="UpdateAdStatus", kwargs={"ad_id": "1115", "status": "paused"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"crisis_conditions_verified": "true"',
            '"ads_paused": "2"',
            '"strategy_switched": "1"',
            '"capital_preservation_complete": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_082",
        instruction=(
            "As a System Reliability Engineer, the 'plan_freeze' automation did not succeed on 2025-08-12. To correct this, you must now manually implement the strategic updates from 'plan_2025-08-12' for ad sets 101 and 104. This entails processing all specified alterations in budget, bid, and creative, and documenting every step taken."
        ),
        actions=[
            Action(name="GetAutomationRunHistory", kwargs={"status": "failed", "limit": 1}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-12"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "101"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 920.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 920.0, "reason": "plan_2025-08-12"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 32.0, "reason": "plan_2025-08-12"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 740.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "reason": "plan_2025-08-12"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "reason": "plan_2025-08-12"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1107", "ad_id_to_pause": "1106"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1107", "rationale": "plan_2025-08-12"})
        ],
        outputs=[
            '"failed_run_confirmed": "true"',
            '"adsets_processed": "2"',
            '"budget_logs": "2"',
            '"strategy_logs": "2"',
            '"creative_logs": "1"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_083",
        instruction=(
            "As a Market Response Specialist, a considerable price reduction on 'Laptop Pro' (product_id 2) has been identified between 2025-08-13 and 2025-08-14. To take advantage of this situation, you need to enhance all functioning ad sets within the 'Electronics' category that currently implement a 'cost_cap' approach. Increase the budget by 15% and the bid by $5 for each qualifying ad set. Record all alterations."
        ),
        actions=[
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "2", "date": "2025-08-13"}),
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "2", "date": "2025-08-14"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Electronics"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"price_drop_confirmed": "true"',
            '"eligible_adsets_found": "2"',
            '"budget_increases_logged": "2"',
            '"bid_increases_logged": "2"',
            '"total_actions_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction=(
            "As a System Reliability Engineer addressing a previous automation error, you are required to manually implement the strategic guidelines from 'plan_2025-08-12' because the 'plan_freeze' process did not succeed on 2025-08-12. This task involves implementing all designated budget, bid, and creative adjustments from the plan for ad sets 101 and 104. Make sure to log each step with the justification 'manual_override_plan_2025-08-12' as evidence of the corrective procedure."
        ),
        actions=[
            Action(name="GetAutomationRunHistory", kwargs={"status": "failed", "limit": 1}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-12"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "101"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 920.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 740.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1107", "ad_id_to_pause": "1106"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 920.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 32.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1107", "rationale": "manual_override_plan_2025-08-12"})
        ],
        outputs=[
            '"failed_run_id": "AR-20250812-01"',
            '"corrective_action_status": "completed"',
            '"adsets_processed": "2"',
            '"budget_logs": "2"',
            '"strategy_logs": "2"',
            '"creative_logs": "1"'
        ]
    ),     
    Task(
        annotator="0",
        user_id="USER_085",
        instruction=(
            "As a manager for the 'Fall Collection Launch' campaign, assess the 2025-08-13 results and implement a graduated response accordingly. For ad set 105, which shows strong performance, execute a 15% budget increase. For ad set 104, which performs exceptionally well (ROAS > 11.0), execute a comprehensive reward: a 15% budget increase AND a $5 bid increase. Record all actions."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"adset_105_optimized": "true"',
            '"adset_104_optimized": "true"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "1"',
            '"total_optimizations": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction=(
            "In your role as a Senior Performance Analyst, your assignment is to implement the 'plan_2025-08-13' on ad set 102. Ensure compliance with our 'do no harm' policy regarding top performers. Prior to enacting the planned creative rotation, you must evaluate the ad set's performance on the specified day. If its ROAS is higher than 12.0, override the plan and retain the current active creative to prevent hindering its success. Execute all other planned changes (budget, bids) without exception. Document each action and use the rationale 'performance_override_hold_creative' specifically for the creative decision."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1103", "rationale": "performance_override_hold_creative"})
        ],
        outputs=[
            '"roas_check": "13.22"',
            '"override_triggered": "true"',
            '"budget_change_applied": "true"',
            '"strategy_change_verified": "true"',
            '"creative_rotation_skipped": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_087",
        instruction=(
            "As an Analyst, handle bid elasticity testing for top-performing ad sets. For the 'Apparel' category, identify the ad set with the highest ROAS as of 2025-08-13. If it operates under a 'cost_cap' strategy, execute an aggressive $10 bid increase. Conversely, if it uses a 'lowest_cost' strategy, coordinate a 15% budget increase. Prior to any modifications, confirm the stability of the 'Summer T-Shirt' (product_id 3) price between 2025-08-13 and 2025-08-14. Record the action executed."
        ),
        actions=[
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "3", "date": "2025-08-13"}),
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "3", "date": "2025-08-14"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Apparel"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"price_stable": "true"',
            '"top_apparel_adset": "102"',
            '"adset_strategy": "lowest_cost"',
            '"action_taken": "budget_increase"',
            '"change_logged": "true"'
        ]
    ),    
    Task(
        annotator="0",
        user_id="USER_088",
        instruction=(
            "As a Portfolio Manager, coordinate the balancing of expenses across campaigns. The 'Q3 Brand Awareness Push' campaign (ad set 103) is exceeding its budget without yielding revenue. Therefore, you are required to decrease its budget by a substantial 40%. Distribute the reclaimed funds equally across the two ad sets within the successful 'Fall Collection Launch' campaign (104, 105). Document all three budget adjustments."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 710.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 980.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 990.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 710.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 980.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 990.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"funds_sourced_amount": "470.0"',
            '"funds_per_recipient": "235.0"',
            '"adset_104_new_budget": "980.0"',
            '"adset_105_new_budget": "990.0"',
            '"reallocation_logged": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction=(
            "As a Senior Strategist, it is imperative to manage a full portfolio optimization for the 'Global Summer Sale' campaign pertaining to its CA-based ad sets (101 and 102), using the results from 2025-08-13. Implement our standard procedures to enhance their achievements in budget, bids, and creative alignment with the daily plan. Guarantee the creation of a thorough audit trail for all modifications made."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
        ],
        outputs=[
            '"adsets_optimized": "2"',
            '"budget_changes_logged": "2"',
            '"strategy_changes_logged": "1"',
            '"creative_changes_logged": "2"',
            '"total_logs": "5"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_090",
        instruction=(
            "In your role as a Creative Specialist, acknowledge that the 'Apparel - CA' ad set (102) is excelling due to its 2025-08-13 performance. Proceed to initiate an A/B test. Initially, confirm that 'image' is a permissible creative type following our guidelines. If confirmed, construct a new image ad within the ad set, titled precisely 'Fall_TShirt_Image_v2'. Next, to commence the test, activate this new advertisement and suspend the one presently active. Record this change with the detailed justification 'ab_test_launch:new_image'."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_creative_types"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="CreateAd", kwargs={"adset_id": "102", "name": "Fall_TShirt_Image_v2", "creative_type": "image"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119", "rationale": "ab_test_launch:new_image"})
        ],
        outputs=[
            '"performance_check_passed": "true"',
            '"policy_check_passed": "true"',
            '"new_ad_created_id": "1119"',
            '"old_ad_paused_id": "1103"',
            '"ab_test_launched": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction=(
            "As a Finance Manager, assess the total daily budget for the 'Global Summer Sale' campaign on 2025-08-13 and confirm it is below its $2500 limit. Calculate the precise amount of unused budget and reinvest this sum completely into the campaign's highest-performing ad set of that day, determined by ROAS, to optimize returns. Ensure compliance with rounding policies and document the budget adjustment using the standard reason."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Global Summer Sale"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "1"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 880.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 880.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"budget_headroom": "290.0"',
            '"top_performer_id": "102"',
            '"reinvestment_complete": "true"',
            '"new_budget_for_102": "880.0"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction=(
            "Oversee marketing for the 'Toys' and 'Home' categories by creating a new 'Sales' campaign called 'Home_And_Toys_Holiday_Push'. Transfer ad sets 106 and 107 into this new campaign by establishing new ad sets with the same settings (name, category, budget, bid) within the new campaign ID. Once this transfer is complete, suspend the entire original campaign ('Holiday Season Early Bird') to finalize the migration."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="CreateCampaign", kwargs={"name": "Home_And_Toys_Holiday_Push", "objective": "Sales"}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Holiday - Home Goods", "category": "Home", "daily_budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}),
            Action(name="CreateAdset", kwargs={"campaign_id": "11", "name": "Holiday - Toys", "category": "Toys", "daily_budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="UpdateCampaignStatus", kwargs={"campaign_id": "5", "status": "paused"})
        ],
        outputs=[
            '"new_campaign_id": "11"',
            '"new_adsets_created": "2"',
            '"original_campaign_paused": "true"',
            '"consolidation_complete": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction=(
            "As a Performance Analyst, on 2025-08-13, ad set 101 showed a strong ROAS, however, the spend was nearing its budget. To test scalability, it's essential to implement a 25% budget increase and raise its cost_cap bid by $8 to ensure competitiveness. Confirm that the new bid complies with the maximum allowed bid policy. Document both modifications."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 1150.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 40.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1150.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 40.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"roas": "10.0"',
            '"new_budget": "1150.0"',
            '"new_bid": "40.0"',
            '"max_bid_check_passed": "true"',
            '"changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction=(
            "Acting as a Market Analyst, your objective is to reward the category with the highest user engagement. For the date 2025-08-13, identify the product category with the peak 'active_users' count. Subsequently, as a reward for this elevated engagement, increase the budget by 10% for all currently active ad sets under that winning category. Record all changes."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Home", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Mobile", "date": "2025-08-13"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Mobile"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 1100.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 1100.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"winning_category": "Mobile"',
            '"adsets_rewarded": "2"',
            '"budget_changes_logged": "2"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction=(
            "As a Creative Manager, observe the 'plan_2025-08-13' which outlines a video creative for ad set 101. Nonetheless, upon examining the daily insights, it's apparent that the cost per purchase exceeds expectations. To address this, you must amend the plan and switch back to the image creative to evaluate if it yields better cost-efficiency. Document this modification with the precise reason 'override:high_cpa_test'."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1101", "ad_id_to_pause": "1102"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1102", "new_ad_id": "1101", "rationale": "override:high_cpa_test"})
        ],
        outputs=[
            '"cost_per_purchase": "10.0"',
            '"planned_creative": "video"',
            '"override_action_taken": "true"',
            '"new_active_ad": "1101"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction=(
            "As a Portfolio Manager tasked with adjusting expenditure among campaigns, note that the 'Q3 Brand Awareness Push' campaign (ad set 103) has not generated any revenue. Decrease its budget by 40%. Allocate the saved amount, rounding down to the nearest $10, into the budget of ad set 104 under the 'Fall Collection Launch' campaign. Record both budget adjustments."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 710.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 1210.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 710.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 1210.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"funds_sourced_amount": "470.0"',
            '"adset_103_new_budget": "710.0"',
            '"adset_104_new_budget": "1210.0"',
            '"reallocation_logged": "true"'
        ]
    ),
     Task(
        annotator="0",
        user_id="USER_097",
        instruction=(
            "As a Portfolio Manager, you oversee budget efficiency. Upon reviewing the data from 2025-08-13, you've discovered a notable performance gap. It's essential to shift funds from the lagging 'Mobile App Installs Campaign' to the thriving 'Fall Collection Launch' campaign. According to our standard procedure, decrease the budget of each ad set in the mobile campaign by 20%. Subsequently, compile the total savings and distribute it equally across all active ad sets in the fall campaign. Ensure that all budget modifications comply with rounding policies and are accurately recorded."
        ),
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "7"}),
            Action(name="GetCampaignByName", kwargs={"name": "Fall Collection Launch"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "3"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 940.0}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 950.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 950.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"source_campaign_id": "7"',
            '"destination_campaign_id": "3"',
            '"total_funds_reallocated": "400.0"',
            '"funds_per_recipient_adset": "200.0"',
            '"budget_changes_logged": "4"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction=(
            "As a Senior Ad Ops Specialist, you're tasked with executing the complete 'plan_2025-08-13' on ad set 102. Nevertheless, adhere to our 'do no harm' policy for top performers. Prior to implementing the planned creative rotation, evaluate the ad set's performance for that date. Should its ROAS be greater than 12.0, you need to bypass the plan and preserve the currently active creative to maintain its success. Implement all other planned changes (budget, bids) without exception, and document every step, specifying the reason 'performance_override_hold_creative' for the creative decision if an override occurs."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1103", "rationale": "performance_override_hold_creative"})
        ],
        outputs=[
            '"roas_check": "13.22"',
            '"override_triggered": "true"',
            '"budget_change_applied": "true"',
            '"strategy_change_verified": "true"',
            '"creative_rotation_skipped": "true"',
            '"total_logs_created": "3"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction=(
            "As a Creative Strategist responding to market trends, user engagement for the 'Electronics' category increased significantly on 2025-08-13. To take advantage of this opportunity, handle the launch of a new A/B test in the top-performing ad set for that day in the category. Determine the top performer by ROAS. Next, coordinate the creation of a new video creative named 'Top_Performer_Video_Test' within that ad set. Finally, apply our standard creative rotation practice to activate the new video and pause the current active ad named 'UK Laptop Deals' (ID 1116), recording the action with the justification 'ab_test_response_to_engagement_surge'."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetAdsetsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "112"}),
            Action(name="CreateAd", kwargs={"adset_id": "112", "name": "Top_Performer_Video_Test", "creative_type": "video"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1116"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "112", "old_ad_id": "1116", "new_ad_id": "1119", "rationale": "ab_test_response_to_engagement_surge"})
        ],
        outputs=[
            '"engagement_surge_confirmed": "true"',
            '"top_performing_adset_id": "112"',
            '"new_ad_created_id": "1119"',
            '"ad_paused_for_test_id": "1116"',
            '"ab_test_launched": "true"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction=(
            "As a Compliance Officer tasked with conducting a two-part audit on ad set 104, first carry out a lookback verification to ensure its current settings align with the 'plan_2025-08-12'. Afterwards, implement our standard reward procedure based on its strong performance on 2025-08-13 by increasing its budget by 15% and its bid by $5. Make sure that all actions, including the initial verification checks, are documented with the standard reason code for today's operations."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-12"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "104"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "reason": "plan_2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="UpdateAdsetBidStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="LogStrategyChange", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
        ],
        outputs=[
            '"lookback_compliance_verified": "true"',
            '"optimization_triggered": "true"',
            '"adset_104_roas": "11.22"',
            '"new_budget_applied": "850.0"',
            '"new_bid_applied": "25.0"',
            '"total_logs_created": "4"'
        ]
    ),  
]

