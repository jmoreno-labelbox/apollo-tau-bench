from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="USER_001",
        instruction=(
            "You are a Risk Manager conducting performance triage for 2025-08-13. Identify all ad sets with a ROAS below 1.5. "
            "For any identified ad set, apply a 20% budget reduction. Furthermore, for any of those ad sets that also have a ROAS below 1.0, you must ensure their bid strategy is set to 'lowest_cost'. Log all actions taken."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a Finance Manager. The total daily budget for the 'Global Summer Sale' campaign as of 2025-08-13 is below its $2500 cap. "
            "You must calculate the exact remaining budget headroom and reinvest this entire amount into the campaign's top-performing ad set for that day, as measured by ROAS, to maximize returns. "
            "Ensure the new budget adheres to rounding policies and the change is logged with the standard reason."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Global Summer Sale"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 880.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 880.0, "reason": "plan_2025-08-13"})
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
            "You are a manager for the 'Toys' and 'Home' categories. Consolidate marketing efforts by creating a new 'Sales' campaign named exactly 'Home_And_Toys_Holiday_Push'. "
            "Move ad sets 106 and 107 into this new campaign by creating new ad sets with identical settings (name, category, budget, bid) under the new campaign ID. "
            "Finally, pause the entire original campaign ('Holiday Season Early Bird') to complete the migration."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="create_campaign", kwargs={"name": "Home_And_Toys_Holiday_Push", "objective": "Sales"}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Holiday - Home Goods", "category": "Home", "daily_budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Holiday - Toys", "category": "Toys", "daily_budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "106"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "107"}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Cozy Home Candles", "creative_type": "image"}),
            Action(name="create_ad", kwargs={"adset_id": "114", "name": "LEGO Space Shuttle", "creative_type": "video"}),
            Action(name="update_campaign_status", kwargs={"campaign_id": "5", "status": "paused"})
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
            "You are a Performance Analyst. On 2025-08-13, ad set 101 had a strong ROAS but its spend was close to its budget. "
            "To test for scalability, you must apply a 25% budget increase while also increasing its cost_cap bid by $8 to maintain competitiveness. "
            "Verify the new bid does not exceed the maximum allowed bid policy. Log both changes."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1150.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 40.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1150.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 40.0, "reason": "plan_2025-08-13"})
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
            "You are a Market Analyst. Your goal is to reward the category with the highest user engagement. For 2025-08-13, find the product category with the highest number of 'active_users'. "
            "Then, as a reward for this high engagement, apply a 10% budget increase to all currently active ad sets within that winning category. Log all changes."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Home", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Mobile", "date": "2025-08-13"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Mobile"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 1100.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 1100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"})
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
            "You are a Senior Strategist. Our 'Global Summer Sale' campaign requires a full portfolio optimization for its US-based ad sets (101 and 102) based on 2025-08-13 performance. "
            "You must apply our standard practices to reward their success across budget and bids. For creative, you must align their active ads with the daily plan. Ensure a complete audit trail is created for all changes."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
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
            "You are the manager for the 'Back to School Deals' campaign. Review the performance of its active ad set for 2025-08-13 and apply the 'Budget Optimization Protocol'. "
            "Apply appropriate budget optimizations based on performance data, ensuring compliance with rounding policies and logging requirements."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Back to School Deals"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "6"}),
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"})
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
            "You are an efficiency analyst. Ad set 'Brand - Video Ads' (ID 103) has been flagged for high spend with zero revenue on 2025-08-13. "
            "Investigate its performance and apply the 'Budget Optimization Protocol' specifically to ad set 103 to optimize its budget based on performance data. "
            "Do not adjust other underperforming ad sets - focus only on ad set 103. "
            "Log the action with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"})
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
            "You are the performance manager for women's apparel. The 'Fall Fashion - Women' ad set (ID 104) requires a budget review for 2025-08-13. "
            "Use the budget optimization practice specifically for ad set 104 only. "
            "Do not adjust other underperforming ad sets that may be found - focus exclusively on ad set 104. "
            "Apply appropriate budget optimizations based on performance data, ensuring compliance with rounding policies and logging requirements."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"})
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
            "You are the social media advertising operations manager. "
            "Review App Install ad sets 110 and 111 for performance on 2025-08-13. "
            "If their ROAS is below the 1.5 threshold, apply the 'Budget Optimization Protocol' "
            "and 'Bid Strategy Optimization Protocol' in accordance with policy, "
            "ensuring adjustments and compliance logging are completed under reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "110", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a portfolio manager. Review ad set 104 ('Fall Fashion - Women') and ad set 111 ('App Installs - iOS') for their performance on 2025-08-13. "
            "Apply the 'Bid Strategy Optimization Protocol' to both: for the high performer (ROAS > 2.5, cost_cap), increase the bid by $5; for the low performer (ROAS < 1.0), switch the strategy to 'lowest_cost'. "
            "Log all changes under reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a risk manager. Ad set 'App Installs - iOS' (ID 111) is performing poorly with a ROAS below 1.0 on 2025-08-13. "
            "Follow the bid strategy optimization practice to mitigate losses by switching it to the 'lowest_cost' strategy. "
            "Confirm this is a valid strategy according to policy and ensure the change is correctly logged with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a growth strategist. Ad set 'Electronics - US' (ID 101) has demonstrated excellent performance on 2025-08-13 with a ROAS well above 2.5. "
            "To capitalize on this success following best-practice bid optimization, increase its cost cap bid by $5. "
            "Ensure the new bid remains below the maximum allowed amount and record the adjustment with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"})
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
            "You are the campaign manager for the 'Fall Collection Launch'. Review the performance of all ad sets in this campaign for 2025-08-13. "
            "Apply the 'Bid Strategy Optimization Protocol' only to eligible ad sets (ROAS > 2.5 and cost_cap strategy). "
            "Increase the bid amount by $5 for any qualifying ad set and log the change with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
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
            "You are a performance optimization specialist. Conduct a system-wide review of 'cost_cap' ad sets for 2025-08-13. Specifically, analyze ad sets 106 and 108. "
            "For each one that exceeds a ROAS of 2.5, apply the 'Bid Strategy Optimization Protocol' to increase its bid by $5. "
            "Ensure you check against the maximum bid policy and log all successful changes using reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
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
            "You are the head of the Apparel advertising division. "
            "Conduct a bid strategy review for all ad sets in the 'Apparel' category based on 2025-08-13 performance. "
            "Follow the bid strategy optimization practice, increasing bids by $5 for any eligible top-performing 'cost_cap' ad sets. Log all required changes with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adsets_by_category", kwargs={"category": "Apparel"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
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
            "You are the specialist for the 'Back to School' season. Ad set 108 ('Back to School - Laptops') is a key driver for the 'Back to School Deals' campaign. "
            "For its performance on 2025-08-13, apply the 'Bid Strategy Optimization Protocol' to increase its bid by $5 if eligible. "
            "You must first verify its current strategy is 'cost_cap' and that the new bid will not exceed the max bid policy. Log the change with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Back to School Deals"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "6"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
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
            "You are the manager overseeing early holiday promotions. Ad set 106 ('Holiday - Home Goods') from the 'Holiday Season Early Bird' campaign shows strong potential. "
            "Analyze its performance for 2025-08-13 and optimize its bid strategy based on performance data. "
            "Apply appropriate adjustments and ensure all changes are logged with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"})
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
            "You are the manager for the 'Global Summer Sale' campaign. "
            "Review your two US-based ad sets (101 and 102) for 2025-08-13 performance. "
            "We got an information that any ad set with ROAS > 2.5 and a cost_cap strategy should increase the bid by $5. "
            "Apply appropriate bid strategy optimizations based on performance data and ensure all changes are logged with reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Global Summer Sale"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"})
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
            "You are a senior analyst conducting a cross-category performance audit. "
            "Analyze ad set 108 ('Back to School - Laptops') and 111 ('App Installs - iOS') for their performance on 2025-08-13. "
            "Follow the Bid Strategy Optimization practice to both: increase the bid by $5 for the top performer if it's on cost_cap, and switch the underperformer to 'lowest_cost' if its ROAS is below 1.0. "
            "Log all actions using reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are the 'Back to School' campaign manager. The new 'Student Laptop Video Ad' (ID 1112) has been approved for launch. "
            "Following standard creative rotation practice, activate this new video in ad set 108 and pause the currently running image ad (1111). "
            "The rationale for the change must be 'New creative launch'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Back to School Deals"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "6"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "creative_rotation_window_days"}),
            Action(name="get_last_successful_run", kwargs={"run_type": "creative_rotation"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1112", "ad_id_to_pause": "1111"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "108", "old_ad_id": "1111", "new_ad_id": "1112", "rationale": "New creative launch"})
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
            "You are the operations manager. Conduct a performance review of all ad sets within the 'Fall Collection Launch' campaign for 2025-08-13. "
            "Follow the Budget Optimization practice to adjust ad set budgets based on performance data, considering both underperforming and top-performing ad sets. "
            "Ensure all changes are logged appropriately with reason 'plan_2025-08-13' and comply with budget rounding policies."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"})
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
            "You are the manager for US apparel. It is time to execute the creative strategy from the 2025-08-13 plan for ad set 102 ('Apparel - US'). "
            "Following standard creative rotation practice, to activate the planned creative type. Log the action with a rationale that references the governing plan."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "creative_rotation_window_days"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "Aligning with plan_2025-08-13 creative strategy"})
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
            "You are a Senior Analyst performing a full-stack optimization on ad set 104 for 2025-08-13. The goal is to first align it with the daily plan and then add a performance bonus. "
            "Apply its budget and bid from 'plan_2025-08-13'. Since its ROAS is exceptionally high, then apply an additional 15% performance budget increase on top of the planned budget, logging this second change with the reason 'performance_bonus'. "
            "Finally, verify its creative is aligned with the plan and log this check with the rationale 'plan_alignment_verified'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 860.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 750.0, "new_budget": 860.0, "reason": "performance_bonus"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1106", "rationale": "plan_alignment_verified"})
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
            "You are the US Market manager responsible for daily operations. It's time for the creative update for ad sets 101 and 102. "
            "For each ad set, follow the standard creative rotation practice, to align their active creatives with the specifications in the `plan_2025-08-13`. "
            "Ensure both rotations are logged with 'plan_2025-08-13' as the rationale."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
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
            "You are a Campaign Restructuring Specialist. Your task is to consolidate our 'Back to School' efforts. "
            "Create a new 'Sales' campaign named 'Q3_Education_Push'. Then, create a new ad set within this campaign by cloning all settings (name, category, budget, bid strategy, and bid amount) from the existing 'Back to School - Laptops' ad set (ID 108). "
            "You must also migrate its ads by creating new ads with the same names and creative types in the new ad set. Finally, to complete the migration, you must pause the entire original 'Back to School Deals' campaign."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="create_campaign", kwargs={"name": "Q3_Education_Push", "objective": "Sales"}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Back to School - Laptops", "category": "Electronics", "daily_budget": 780.0, "bid_strategy": "cost_cap", "bid_amount": 42.0}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Student Laptop Deals", "creative_type": "image"}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Student Laptop Video Ad", "creative_type": "video"}),
            Action(name="update_campaign_status", kwargs={"campaign_id": "6", "status": "paused"})
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
            "You are a Creative Performance Analyst. The daily plan for 'plan_2025-08-13' suggests an 'image' creative for ad set 104. "
            "However, you must override this based on the 'video_cpa_advantage_pct' policy. "
            "Follow the standard creative rotation practice to activate the video creative (ad 1107). The rationale must be 'Policy-driven video prioritization'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "creative_rotation_window_days"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_last_successful_run", kwargs={"run_type": "creative_rotation"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1107", "ad_id_to_pause": "1106"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1107", "rationale": "Policy-driven video prioritization"})
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
            "You are an Ad Operations Specialist. Your task is to execute the planned creative rotation for ad set 102 as per 'plan_2025-08-13'. "
            "Before executing, you must list all ads within that ad set to confirm you are activating the correct, non-archived ad ('Summer T-Shirt Carousel'). "
            "Then, follow the standard creative rotation practice and log it with 'Plan compliance: activating carousel creative' for the record."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "Plan compliance: activating carousel creative"})
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
            "You are the Automation Orchestrator for the 'Global Summer Sale' campaign. Follow the plan execution practice for ad set 101 ('Electronics - US') based on 'plan_2025-08-13'. You must verify the plan, apply both budget and bid strategy changes, and log each action."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_campaign_by_name", kwargs={"name": "Global Summer Sale"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"})
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
            "You are the daily operations lead. The plan for ad set 102 ('Apparel - US') requires only a budget adjustment. "
            "Follow plan execution best practice for ad set 102 based on 'plan_2025-08-13'. "
            "You must apply the budget change and log it. Additionally, you must verify and log the bid strategy status, even though no change is required, to maintain complete audit compliance."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are the manager for the 'Fall Collection Launch' campaign. Your task is to apply the 'plan_2025-08-13' to ad set 104."
            "Implement the plan execution practice by applying all specified budget and bid amount changes and logging them with the correct reason."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"})
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
            "You are the manager for the new 'Fall Collection Launch' campaign. Apply the daily plan 'plan_2025-08-13' to the 'Fall Fashion - Men' ad set (105). Since this is a new and closely monitored ad set"
            "Execute the plan execution practice and confirm that the current budget and bid strategy match the plan, logging both actions as 'no change' for the record."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a senior ad ops specialist responsible for high-budget campaigns. Before executing the plan execution best practice for ad set 111 based on 'plan_2025-08-13', "
            "you must first confirm its parent campaign ('Mobile App Installs Campaign') is active. If the campaign is active, proceed to apply and log all planned changes, even if they are 'no-ops'."
            "You must update the adset budget and bid strategy even for no-op changes to maintain complete audit compliance."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 1000.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5, "new_bid": 2.5, "reason": "plan_2025-08-13"})
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
            "You are a compliance specialist. Your job is to apply the plan 'plan_2025-08-13' for ad set 108 ('Back to School - Laptops'), ensuring the new bid does not violate the 'max_bid_amount' policy. Execute the 'Plan Execution Protocol' by checking the policy, then applying and logging the budget and strategy changes."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 45.0, "reason": "plan_2025-08-13"})
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
            "As the System Reliability Engineer, your goal is to ensure platform stability and optimal performance for 2025-08-13. "
            "Investigate the recent automation run history for any failures that might indicate systemic issues. "
            "Concurrently, conduct a system-wide performance audit. For any ad sets failing to meet the 1.5 ROAS minimum, "
            "apply the budget and bidding optimization practice to restore them to profitability. "
            "Ensure all corrective actions are fully logged under the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_automation_run_history", kwargs={"status": "failed"}),
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "As a Senior Performance Analyst, you are conducting a cross-campaign audit for 2025-08-13, focusing on a mix of high and low-performing ad sets: 101, 104, and 111. "
            "Your objective is to apply comprehensive optimizations based on each ad set's performance tier. "
            "Implement the standard best practices for both budget and bid strategy adjustments to capitalize on successes and mitigate losses. "
            "Ensure every change is meticulously logged with the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "As the Creative Manager for the 'Fall Collection Launch' campaign, it's time to leverage the campaign's strong momentum. "
            "Your goal is to introduce a new video creative to further boost performance. After confirming the parent campaign is operational, "
            "launch a new ad named 'Fall Dress Collection Video v2' within ad set 104. Then, implement the standard creative rotation process to make the new video live, "
            "pausing the existing image ad (ID 1106). Justify this strategic shift in the logs with the rationale: 'Capitalizing on high performance with new video creative'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_creative_types"}),
            Action(name="create_ad", kwargs={"adset_id": "104", "name": "Fall Dress Collection Video v2", "creative_type": "video"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1106"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1119", "rationale": "Capitalizing on high performance with new video creative"})
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
            "You are the lead for US Electronics, and your priority is to deploy the full strategic plan ('plan_2025-08-13') for the 'Electronics - US' ad set (101). "
            "You must follow the complete plan execution practice, ensuring all specified budget, bid, and creative changes are implemented and audited correctly. Also use plan_2025-08-13 as the rationale for creative rotation."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"})
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
            "You are the manager of the 'Fall Collection Launch' campaign. The campaign's initial performance is strong, and your task is to capitalize on this success. "
            "Apply our standard performance reward practices to both the Men's (105) and Women's (104) ad sets based on their 2025-08-13 results. "
            "This includes increasing budgets for these top performers by 15% and, for any using a cost_cap strategy, increasing their bid by $5. "
            "Ensure all adjustments are logged and adhere to rounding policies."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
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
            "You are the manager for the 'Mobile App Installs' campaign, which is showing poor efficiency on 2025-08-13 (ad sets 110 & 111). "
            "Follow the standard corrective measures for underperforming assets to both ad sets. "
            "This involves reducing their budgets by 20% and switching any with a 'cost_cap' strategy to 'lowest_cost' to mitigate further losses. "
            "Log all changes meticulously."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are the manager for the 'Holiday Season Early Bird' campaign, which needs a performance boost. "
            "Your task is to identify the single best-performing ad set within this campaign that uses a 'cost_cap' strategy. "
            "Once you have identified it, you must apply our standard reward protocols for both budget (a 15% increase) and bid (a $5 increase) based on its 2025-08-13 performance, ensuring the new bid does not violate the max bid policy."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"})
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
            "You are a Senior Performance Analyst conducting a graduated optimization across a portfolio of ad sets for 2025-08-13. "
            "For the exceptional performer (ad set 102, ROAS > 12), apply a 20% budget increase. "
            "For the strong performer (ad set 101, ROAS > 8), apply a 15% budget increase. "
            "For the critical underperformer (ad set 111, ROAS < 1), reduce its budget by 20% and switch its strategy to 'lowest_cost'. "
            "Log all actions taken."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 710.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 710.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a senior portfolio manager responsible for key seasonal pushes. You need to optimize two top-performing ad sets from different campaigns: 'Back to School - Laptops' (108) and 'Holiday - Home Goods' (106). "
            "For both, you are to apply our standard reward protocol based on their 2025-08-13 performance: increase their budgets by 15% and their cost_cap bids by $5, ensuring all changes are logged."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"})
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
            "You are responsible for system health. Run a system-wide check for any underperforming ad sets on 2025-08-13 using the established 1.5 ROAS threshold. "
            "For all identified ad sets, execute the budget optimization practice to reduce their budgets by 20%. "
            "Ensure you respect all rounding and logging rules, using the reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"})
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
            "You are a compliance analyst performing a spot check on the 'Fall Fashion - Men' ad set (105). "
            "First, you must verify its current budget and bid strategy are aligned with 'plan_2025-08-13', logging these verifications using the standard reason code. "
            "Once compliance is confirmed, you are to evaluate its 2025-08-13 performance and apply the standard budget optimization protocol if it qualifies as a top performer, again using the standard reason code for the change."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"})
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
            "You are a risk manager investigating the 'Q3 Brand Awareness Push' campaign. The ad set (103) within this campaign reported zero revenue on 2025-08-13. "
            "While a zero ROAS is expected for an 'Awareness' objective, you must still follow the complete Budget Optimization practice to ensure cost efficiency. "
            "Execute the practice specifically for ad set 103 only (do not process other underperforming ad sets) and ensure any resulting budget changes are logged with the standard reason code."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "2"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"})
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
            "You are the Portfolio Manager for all Sales-objective campaigns. Your task is to conduct a comprehensive performance review for ad set 101 ('Electronics - US') and ad set 108 ('Back to School - Laptops') for 2025-08-13. "
            "Because both are top performers, you must apply our standard practices for rewarding success to both their budgets and bid strategies. "
            "Ensure all budget increases (15%) and bid increases ($5 for cost_cap) are compliant with rounding and max bid policies, and log every action using reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
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
            "You are the System Reliability Engineer. Your primary task is to investigate the recent failed automation run. "
            "After identifying the failed run, proceed with a system-wide health check for 2025-08-13. "
            "For any ad sets performing below our 1.5 ROAS minimum, take the standard corrective actions to their budgets and bid strategies to improve cost-efficiency. "
            "Log all adjustments made."
        ),
        actions=[
            Action(name="get_automation_run_history", kwargs={"status": "failed", "limit": 1}),
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are the Head of Automation. Your task is to apply the full daily strategy for the 'Fall Collection Launch' campaign as specified in 'plan_2025-08-13'. "
            "For every ad set in the campaign (104 and 105), you must apply the planned budget and bid strategy. "
            "To ensure a complete audit trail, you must log every single potential change for both ad sets, even if the values are not changing (a 'no-op' change)."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a Creative Director launching a new A/B test. Your task is to set up a new campaign named 'Q4 Gaming Push' with an 'Awareness' objective. "
            "Within this campaign, create one ad set named 'Gaming Mouse Promo' for the 'Electronics' category with an initial budget of $1200. "
            "Then, create two new ad creatives in this ad set: one image named 'Gaming Mouse Static v1' and one video named 'Gaming Mouse Action v1'. "
            "Finally, follow our standard practice to activate the video ad and pause the image ad to begin the test, logging the rotation with rationale 'Initial A/B test launch'."
        ),
        actions=[
            Action(name="create_campaign", kwargs={"name": "Q4 Gaming Push", "objective": "Awareness"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "default_bid_strategy"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Gaming Mouse Promo", "category": "Electronics", "daily_budget": 1200.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Gaming Mouse Static v1", "creative_type": "image"}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Gaming Mouse Action v1", "creative_type": "video"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1120", "ad_id_to_pause": "1119"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "113", "old_ad_id": "1119", "new_ad_id": "1120", "rationale": "Initial A/B test launch"})
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
            "You are a Senior Analyst performing a full-stack optimization on ad set 101 for 2025-08-13. The goal is to first align it with the daily plan and then add a performance bonus. "
            "Apply its budget and bid from 'plan_2025-08-13'. Since its ROAS is strong, then apply an additional 15% performance budget increase on top of the planned budget, logging this second change with the reason 'performance_bonus'. "
            "Finally, execute the creative rotation specified in the plan."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1090.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 950.0, "new_budget": 1090.0, "reason": "performance_bonus"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"})
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
            "You are the manager responsible for the 'Global Summer Sale' campaign. Today, you must execute the full daily strategy for ad sets 101, 102, and 112 as defined in 'plan_2025-08-13'. "
            "This involves applying all specified changes to budgets, bids, and active creatives to ensure complete plan alignment for all three ad sets. Ensure every action is logged."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 700.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
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
            "You are a Performance Analyst tasked with a deep dive into the 'Electronics' category for 2025-08-13. "
            "Your analysis must correlate ad performance with sales data. First, retrieve the weekly sales figures for Electronics. "
            "Then, for all active 'Electronics' ad sets (101, 108, 112), calculate their ROAS. "
            "Based on this data, apply our standard budget adjustments to increase the budget of the top ROAS performer by 15% and decrease the budget of the lowest ROAS performer by 20%."
        ),
        actions=[
            Action(name="get_weekly_sales_by_category", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Electronics"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 810.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 740.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 810.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 740.0, "reason": "plan_2025-08-13"})
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
            "You are the new mobile app campaign manager. Ad sets 110 and 111 are underperforming with ROAS below 1.5 on 2025-08-13. "
            "Implement the 'Budget Optimization Protocol' specifically for ad sets 110 and 111 only. "
            "Do not adjust other underperforming ad sets that may be found - focus exclusively on ad sets 110 and 111. "
            "Ensure compliance with minimum budget allocation policies and proper logging of all changes."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"})
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
            "You are a Compliance Officer. You must verify that the planned bid increase for ad set 108 in 'plan_2025-08-13' is valid. "
            "First, ensure the planned bid is compliant with our max bid policy and that its parent campaign ('Back to School Deals') is active. "
            "If these pre-checks pass, proceed to apply all planned budget and strategy changes for that ad set. "
            "Log all actions, including a specific rationale 'Compliance check passed' for the final strategy change log."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="get_campaign_by_name", kwargs={"name": "Back to School Deals"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 45.0, "reason": "Compliance check passed"})
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
            "You are the manager for all EU marketing. A price drop for the 'Laptop Pro' (product_id 2) was enacted on 2025-08-14. "
            "In response, your task is to boost the 'Electronics - EU' ad set (112) based on its 2025-08-13 performance. "
            "First, confirm the price change. Then, calculate the ad set's current ROAS. "
            "Finally, apply our standard budget increase of 15% for top performers and, since its strategy is 'lowest_cost', log a 'no-op' strategy change to confirm your review. "
            "Log all actions."
        ),
        actions=[
            Action(name="get_product_price_on_date", kwargs={"product_id": "2", "date": "2025-08-13"}),
            Action(name="get_product_price_on_date", kwargs={"product_id": "2", "date": "2025-08-14"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 810.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 810.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are the lead for seasonal promotions. Your task is to ensure the 'Holiday Season Early Bird' campaign is fully aligned with the daily strategy for '2025-08-13'. You must apply all planned budget and bid strategy adjustments to every ad set within this campaign. For creative alignment, you must verify that the active creative type matches the plan and log this verification for each ad set using the exact rationale string 'plan_alignment_verified'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "106"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "106", "old_ad_id": "1109", "new_ad_id": "1109", "rationale": "plan_alignment_verified"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "107", "old_ad_id": "1110", "new_ad_id": "1110", "rationale": "plan_alignment_verified"})
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
            "You are a growth strategist focused on the US market. Ad set 102 ('Apparel - US') has shown exceptional performance on 2025-08-13. To capitalize on this, apply a 15% budget increase. Concurrently, you must ensure its active creative matches the type specified in the 'plan_2025-08-13' to unlock further growth. Ensure all actions are logged."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "Aligning with plan_2025-08-13 creative strategy"})
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
            "You are a Bidding Specialist. Conduct a system-wide review of ad sets 101, 104, and 108, all of which use a 'cost_cap' bid strategy. For every one of these ad sets that exceeded our top-performance ROAS threshold of 2.5 on 2025-08-13, you must apply our standard bid increase practice to press their advantage. Ensure all changes respect the maximum bid policy and are logged."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
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
            "You are a Performance Analyst investigating an anomaly. Ad set 103, which belongs to the 'Q3 Brand Awareness Push' campaign, showed significant spend with zero revenue on 2025-08-13. First, confirm this campaign's objective. Regardless of the objective, apply our standard 20% budget reduction for underperforming assets. Finally, verify its active creative aligns with the daily plan, logging the check with the exact rationale 'verification:plan_sync_ok'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "103"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "103", "old_ad_id": "1105", "new_ad_id": "1105", "rationale": "verification:plan_sync_ok"})
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
            "You are the campaign lead for seasonal promotions. The 'Holiday Season Early Bird' campaign is critical. Analyze the performance of its constituent ad sets for 2025-08-13. "
            "Review performance data and optimize budgets based on ROAS performance, ensuring proper logging and compliance with established policies. "
            "Follow all logging and rounding procedures using 'plan_2025-08-13' as the reason. "
            "For budget increases, round up to the nearest $10 increment to ensure adequate funding for high-performing ad sets."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 460.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 460.0, "reason": "plan_2025-08-13"})
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
            "You are a Senior Portfolio Manager. Your task is to conduct a cross-campaign optimization for 2025-08-13. You need to address both a top-performing asset, ad set 106, and an underperforming one, ad set 111. Apply our standard practice to reward the former's success and mitigate the latter's losses across both their budgets and bid strategies. Log all adjustments."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 580.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 23.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 580.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 23.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a Performance Analyst. Our sales report for the week starting 2025-08-07 shows strong performance in the 'Apparel' category. To build on this momentum, you must review all ad sets in this category. For every ad set that achieved a ROAS greater than 10.0 on 2025-08-13, apply our standard 15% budget increase for top performers. Ensure all changes are logged."
        ),
        actions=[
            Action(name="get_weekly_sales_by_category", kwargs={"category": "Apparel", "start_date": "2025-08-07"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Apparel"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"})
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
            "You are a performance analyst. Ad set 'Apparel - US' (ID 102) has been flagged for a performance review on 2025-08-13. "
            "Execute the 'Budget Optimization Protocol' to optimize its budget based on performance data. "
            "Before applying the change, verify and use the 'budget_rounding_unit' policy. Ensure the change is logged correctly under reason 'plan_2025-08-13'."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"})
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
            "You are a senior strategist reviewing sequential optimizations. The daily plan for 2025-08-13 for ad set 101 continues an aggressive growth strategy. First, you must confirm that its performance on the 13th justifies this continued investment by checking its ROAS. If it remains a top performer, proceed with the full plan execution, applying all specified adjustments to its budget, bid, and active creative to maintain momentum."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"})
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
            "You are a Risk Manager responding to a performance crisis. Ad set 111 is performing critically below threshold on 2025-08-13. You must immediately enact our capital preservation practice: take exactly $500 from its budget and switch it to the 'lowest_cost' strategy. Then, reallocate those saved funds to a proven top performer, ad set 104, to maximize portfolio returns. Ensure all resulting changes are correctly logged."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 500.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 1240.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 1240.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a Portfolio Manager responsible for budget efficiency. Your analysis of 2025-08-13 data has identified an opportunity to reallocate funds. You must move exactly $300 from the budget of the lowest-performing 'Apparel' ad set and transfer it to the top-performing 'Electronics' ad set. Log both resulting budget changes."
        ),
        actions=[
            Action(name="get_adsets_by_category", kwargs={"category": "Apparel"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Electronics"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 450.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 1000.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 450.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 1000.0, "reason": "plan_2025-08-13"})
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
            "You are a Creative Analyst. Our policy prioritizes video creatives due to their performance advantage. For ad set 108, you must ensure the active creative aligns with this policy, overriding the daily plan for 2025-08-13 if it specifies a different creative type. You must log this action with the exact rationale string 'policy_override:video_cpa_advantage'."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1112", "ad_id_to_pause": "1111"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "108", "old_ad_id": "1111", "new_ad_id": "1112", "rationale": "policy_override:video_cpa_advantage"})
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
            "You are a Campaign Specialist launching the 'Q4 Home Goods' initiative. Your task is to create a new 'Sales' campaign with that exact name. Within it, create two new ad sets: one named 'Home_Decor_Q4' for the 'Home' category with a $450 budget, and another named 'Office_Supplies_Q4' for the 'Office' category with a $250 budget. For each new ad set, you must create and activate one new image ad with the name format '[AdSetName]_Image_1'. Log the entire setup."
        ),
        actions=[
            Action(name="create_campaign", kwargs={"name": "Q4 Home Goods", "objective": "Sales"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "default_bid_strategy"}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Home_Decor_Q4", "category": "Home", "daily_budget": 450.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Office_Supplies_Q4", "category": "Office", "daily_budget": 250.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Home_Decor_Q4_Image_1", "creative_type": "image"}),
            Action(name="create_ad", kwargs={"adset_id": "114", "name": "Office_Supplies_Q4_Image_1", "creative_type": "image"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1119", "status": "active"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1120", "status": "active"})
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
            "You are a Risk Manager conducting performance triage for 2025-08-13. Identify all ad sets with a ROAS below 1.5. For any identified ad set, apply a 20% budget reduction. Furthermore, for any of those ad sets with a ROAS below 1.0, you must also ensure their bid strategy is set to 'lowest_cost'. Log all actions taken."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 940.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a Performance Analyst reviewing weekly trends for ad set 101. Compare its total spend for the most recent week (2025-08-07 to 2025-08-13) against the prior week (2025-07-31 to 2025-08-06). After calculating its ROAS for 2025-08-13, if you find that spend has increased week-over-week AND the ROAS is below 11.0, you must apply a 20% budget reduction as a corrective measure and log the change."
        ),
        actions=[
            Action(name="get_adset_spend_for_date_range", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range", kwargs={"adset_id": "101", "start_date": "2025-07-31", "end_date": "2025-08-06"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 740.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 740.0, "reason": "plan_2025-08-13"})
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
            "You are a Compliance Officer. Your task is to perform a lookback verification on ad set 102. You must confirm that its current budget and bid strategy match the allocations specified in the previous day's plan, 'plan_2025-08-12'. Log the outcome of this verification for both budget and strategy, using the exact rationale string 'compliance_lookback_ok' for each log entry."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-12"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "102"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 590.0, "reason": "compliance_lookback_ok"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "compliance_lookback_ok"})
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
            "You are the Campaign Manager for 'Global Summer Sale'. The paused video ad within the 'Electronics - US' ad set needs to be reactivated. To support this, first adjust the ad set's budget to $950. Then, find the paused ad within that ad set and change its status to 'active'. Log the budget change with the reason 'reactivation_budget_adjustment'."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Global Summer Sale"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "reason": "reactivation_budget_adjustment"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1102", "status": "active"})
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
            "You are a Senior Analyst performing a full-stack optimization on ad set 104 for 2025-08-13. The goal is to first align it with the daily plan and then add a performance bonus. Apply its budget and bid from 'plan_2025-08-13'. Since its ROAS is exceptionally high, then apply an additional 15% performance budget increase on top of the planned budget, logging this second change with the reason 'performance_bonus'. Finally, verify its creative is aligned with the plan and log this check with the rationale 'plan_alignment_verified'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 860.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 750.0, "new_budget": 860.0, "reason": "performance_bonus"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1106", "rationale": "plan_alignment_verified"})
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
            "You are a Data Scientist. You hypothesize that high user engagement predicts sales. Check viewership for the 'Toys' category on 2025-08-13. If sessions exceeded 5,000 and the associated ad set 107 has a ROAS above 10.0, confirm your hypothesis by applying a 20% budget increase to capitalize on the demand. Log any budget changes with the exact reason 'data_driven_increase'."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 480.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 480.0, "reason": "data_driven_increase"})
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
            "You are a Finance Manager. The total daily budget for the 'Global Summer Sale' campaign must not exceed $2250. Review the performance of its ad sets (101, 102, 112) on 2025-08-13. Increase the budget of the top performer by 15%, but then decrease the budget of the lowest performer by an amount sufficient to bring the campaign's total budget back down to the $2250 cap. Log all changes."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Global Summer Sale"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 870.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 870.0, "reason": "plan_2025-08-13"})
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
            "You are a Portfolio Optimizer. To maximize ROI, you must reallocate funds based on 2025-08-13 performance. Decrease the budget of all ad sets with a ROAS below 1.0 by exactly $200 each. Then, pool this total amount and add it to the single highest-performing ad set on that day. Log all resulting budget changes."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.0, "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 980.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 1190.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 980.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 1190.0, "reason": "plan_2025-08-13"})
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
            "You are a Campaign Architect. Launch a new 'Lead Generation' campaign named exactly 'Webinar_Signups_Fall_2025'. Create an ad set within it named 'Tech_Webinar_Promo' targeting the 'Electronics' category. You must configure this new ad set using the system's default policies for 'default_bid_strategy' and 'min_budget_allocation'. Then, create and activate a single video ad named 'Webinar_Invite_Video'."
        ),
        actions=[
            Action(name="create_campaign", kwargs={"name": "Webinar_Signups_Fall_2025", "objective": "Lead Generation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "default_bid_strategy"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Tech_Webinar_Promo", "category": "Electronics", "daily_budget": 100.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="create_ad", kwargs={"adset_id": "113", "name": "Webinar_Invite_Video", "creative_type": "video"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1119", "status": "active"})
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
            "You are a Market Analyst. Your goal is to reward the category with the best momentum. First, identify the product category with the highest weekly revenue for the week starting 2025-08-07. Then, find the single highest-performing ad set (by ROAS on 2025-08-13) within that winning category. Apply our standard 15% budget increase to this ad set to amplify its success. Log the change."
        ),
        actions=[
            Action(name="get_weekly_sales_by_category", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="get_weekly_sales_by_category", kwargs={"category": "Apparel", "start_date": "2025-08-07"}),
            Action(name="get_weekly_sales_by_category", kwargs={"category": "Home", "start_date": "2025-08-07"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Electronics"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 810.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 810.0, "reason": "plan_2025-08-13"})
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
            "You are the 'Back to School' campaign manager. You must ensure ad set 108 is perfectly aligned with 'plan_2025-08-13' across all dimensions: budget, bid, and creative. Apply all necessary changes and create a complete audit trail by logging each action taken."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 45.0, "reason": "plan_2025-08-13"})
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
            "You are a Crisis Manager. System monitoring has detected that the 'Mobile App Installs Campaign' is in a performance crisis on 2025-08-13, with both of its ad sets performing critically below a 1.0 ROAS. You must immediately enact our capital preservation measures: pause all of their active ads to halt all spending. Also, as a cost-control measure, ensure ad set 111's strategy is switched to 'lowest_cost' and log the change."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "110"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1114", "status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1115", "status": "paused"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "111", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "reason": "plan_2025-08-13"})
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
            "You are a System Reliability Engineer. The 'plan_freeze' automation failed on 2025-08-12. As a corrective measure, you must now manually apply the strategic changes from 'plan_2025-08-12' for ad sets 101 and 104. This includes applying all specified budget, bid, and creative changes and logging every action taken."
        ),
        actions=[
            Action(name="get_automation_run_history", kwargs={"status": "failed", "limit": 1}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-12"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "101"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 920.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 920.0, "reason": "plan_2025-08-12"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 32.0, "reason": "plan_2025-08-12"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 740.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "reason": "plan_2025-08-12"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "reason": "plan_2025-08-12"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1107", "ad_id_to_pause": "1106"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1107", "rationale": "plan_2025-08-12"})
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
            "You are a Market Response Specialist. We have detected a significant price drop on 'Laptop Pro' (product_id 2) between 2025-08-13 and 2025-08-14. To capitalize on this, you must boost all active ad sets in the 'Electronics' category that are currently using a 'cost_cap' strategy. For each eligible ad set, apply a 15% budget increase and a $5 bid increase. Log all changes."
        ),
        actions=[
            Action(name="get_product_price_on_date", kwargs={"product_id": "2", "date": "2025-08-13"}),
            Action(name="get_product_price_on_date", kwargs={"product_id": "2", "date": "2025-08-14"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Electronics"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 900.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 47.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 900.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 47.0, "reason": "plan_2025-08-13"})
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
            "You are a System Reliability Engineer responding to a past automation failure. The 'plan_freeze' process failed on 2025-08-12. You must now manually apply the strategic directives from 'plan_2025-08-12' for ad sets 101 and 104. "
            "This involves applying all specified budget, bid, and creative changes from that plan. "
            "Ensure you log every action taken with the reason 'manual_override_plan_2025-08-12' to document the corrective action."
        ),
        actions=[
            Action(name="get_automation_run_history", kwargs={"status": "failed", "limit": 1}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-12"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "101"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 920.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 740.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1107", "ad_id_to_pause": "1106"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 920.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 32.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "reason": "manual_override_plan_2025-08-12"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "104", "old_ad_id": "1106", "new_ad_id": "1107", "rationale": "manual_override_plan_2025-08-12"})
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
            "You are a manager for the 'Fall Collection Launch' campaign. Based on 2025-08-13 performance, apply a graduated response. For ad set 105, which is a strong performer, apply a 15% budget increase. For ad set 104, which is an exceptional performer (ROAS > 11.0), apply a full-stack reward: a 15% budget increase AND a $5 bid increase. Log all actions."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
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
            "You are a Senior Performance Analyst. Your task is to apply the 'plan_2025-08-13' to ad set 102. However, you must adhere to our 'do no harm' policy for top performers. Before applying the planned creative rotation, you must first assess the ad set's performance on that day. If its ROAS exceeds 12.0, you must override the plan and maintain the current active creative to avoid disrupting its success. Apply all other planned changes (budget, bids) regardless. Log every action, using the exact rationale 'performance_override_hold_creative' for the creative decision."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1103", "rationale": "performance_override_hold_creative"})
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
            "You are an Analyst. Our policy is to test bid elasticity on top-performing ad sets. For the 'Apparel' category, find the single ad set with the highest ROAS on 2025-08-13. If it uses a 'cost_cap' strategy, apply an aggressive $10 bid increase. If it uses 'lowest_cost', apply a 15% budget increase instead. Before making any changes, you must verify that the price of the 'Summer T-Shirt' (product_id 3) was stable between 2025-08-13 and 2025-08-14. Log the action taken."
        ),
        actions=[
            Action(name="get_product_price_on_date", kwargs={"product_id": "3", "date": "2025-08-13"}),
            Action(name="get_product_price_on_date", kwargs={"product_id": "3", "date": "2025-08-14"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Apparel"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"})
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
            "You are a Portfolio Manager balancing spend across campaigns. The 'Q3 Brand Awareness Push' campaign (ad set 103) is over budget with zero revenue. You must reduce its budget by a significant 40%. Take these saved funds and re-invest them evenly across the two ad sets in the high-performing 'Fall Collection Launch' campaign (104, 105). Log all three budget changes."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 710.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 980.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 990.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 710.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 980.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 990.0, "reason": "plan_2025-08-13"})
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
            "You are a Senior Strategist. Our 'Global Summer Sale' campaign requires a full portfolio optimization for its US-based ad sets (101 and 102) based on 2025-08-13 performance. You must apply our standard practices to reward their success across budget, bids, and creative alignment with the daily plan. Ensure a complete audit trail is created for all changes."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 37.0}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1102", "ad_id_to_pause": "1101"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 37.0, "reason": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1102", "rationale": "plan_2025-08-13"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104", "rationale": "plan_2025-08-13"})
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
            "You are a Creative Specialist. The 'Apparel - US' ad set (102) is a top performer based on its 2025-08-13 performance. You need to launch an A/B test. First, verify that 'image' is a valid creative type according to our policy. If it is, create a new image ad within the ad set named exactly 'Fall_TShirt_Image_v2'. Then, to begin the test, activate this new ad and pause the currently active ad. Log this rotation with the exact rationale 'ab_test_launch:new_image'."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_creative_types"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="create_ad", kwargs={"adset_id": "102", "name": "Fall_TShirt_Image_v2", "creative_type": "image"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119", "rationale": "ab_test_launch:new_image"})
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
            "You are a Finance Manager. The total daily budget for the 'Global Summer Sale' campaign as of 2025-08-13 is below its $2500 cap. You must calculate the exact remaining budget headroom and reinvest this entire amount into the campaign's top-performing ad set for that day, as measured by ROAS, to maximize returns. Ensure the new budget adheres to rounding policies and the change is logged with the standard reason."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Global Summer Sale"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 880.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 880.0, "reason": "plan_2025-08-13"})
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
            "You are a manager for the 'Toys' and 'Home' categories. Consolidate marketing efforts by creating a new 'Sales' campaign named exactly 'Home_And_Toys_Holiday_Push'. Move ad sets 106 and 107 into this new campaign by creating new ad sets with identical settings (name, category, budget, bid) under the new campaign ID. Finally, pause the entire original campaign ('Holiday Season Early Bird') to complete the migration."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="create_campaign", kwargs={"name": "Home_And_Toys_Holiday_Push", "objective": "Sales"}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Holiday - Home Goods", "category": "Home", "daily_budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}),
            Action(name="create_adset", kwargs={"campaign_id": "11", "name": "Holiday - Toys", "category": "Toys", "daily_budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="update_campaign_status", kwargs={"campaign_id": "5", "status": "paused"})
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
            "You are a Performance Analyst. On 2025-08-13, ad set 101 had a strong ROAS but its spend was close to its budget. To test for scalability, you must apply a 25% budget increase while also increasing its cost_cap bid by $8 to maintain competitiveness. Verify the new bid does not exceed the maximum allowed bid policy. Log both changes."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 1150.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 40.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1150.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 40.0, "reason": "plan_2025-08-13"})
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
            "You are a Market Analyst. Your goal is to reward the category with the highest user engagement. For 2025-08-13, find the product category with the highest number of 'active_users'. Then, as a reward for this high engagement, apply a 10% budget increase to all currently active ad sets within that winning category. Log all changes."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Home", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Mobile", "date": "2025-08-13"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Mobile"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 1100.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 1100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1100.0, "reason": "plan_2025-08-13"})
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
            "You are a Creative Manager. The 'plan_2025-08-13' specifies a video creative for ad set 101. However, after reviewing the daily insights, you've noticed the cost per purchase is higher than desired. As a corrective measure, you must override the plan and revert to the image creative to test if it's more cost-effective. Log this override with the exact rationale 'override:high_cpa_test'."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1101", "ad_id_to_pause": "1102"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1102", "new_ad_id": "1101", "rationale": "override:high_cpa_test"})
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
            "You are a Portfolio Manager balancing spend across campaigns. The 'Q3 Brand Awareness Push' campaign (ad set 103) has zero revenue. Reduce its budget by 40%. Take the saved funds, rounded down to the nearest $10, and re-invest this amount in the budget of ad set 104 in the 'Fall Collection Launch' campaign. Log both budget changes."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 710.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 1210.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 710.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 1210.0, "reason": "plan_2025-08-13"})
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
            "You are a Portfolio Manager responsible for budget efficiency. Your analysis of 2025-08-13 data has identified a significant performance gap. You must reallocate funds from the underperforming 'Mobile App Installs Campaign' to the high-performing 'Fall Collection Launch' campaign. "
            "Follow our standard practice by reducing the budget of each ad set in the mobile campaign by 20%. Then, pool the total amount saved and reinvest it evenly across all active ad sets in the fall campaign. "
            "Ensure all budget adjustments adhere to rounding policies and are meticulously logged."
        ),
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),
            Action(name="get_campaign_by_name", kwargs={"name": "Fall Collection Launch"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 800.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 940.0}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 950.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 940.0, "reason": "plan_2025-08-13"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 950.0, "reason": "plan_2025-08-13"})
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
            "You are a Senior Ad Ops Specialist. Your task is to apply the full 'plan_2025-08-13' to ad set 102. However, you must follow our 'do no harm' policy for top performers. "
            "Before applying the planned creative rotation, first assess the ad set's performance on that day. If its ROAS exceeds 12.0, you must override the plan and maintain the current active creative to avoid disrupting its success. "
            "Apply all other planned changes (budget, bids) regardless, and log every action, using the exact rationale 'performance_override_hold_creative' for the creative decision if the override is triggered."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "bid_amount": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "reason": "plan_2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1103", "rationale": "performance_override_hold_creative"})
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
            "You are a Creative Strategist responding to market trends. User engagement for the 'Electronics' category surged on 2025-08-13. To capitalize on this, you must launch a new A/B test in the category's top-performing ad set from that day. "
            "Identify the top performer by ROAS. Then, create a new video creative named 'Top_Performer_Video_Test' within that ad set. "
            "Finally, implement our standard creative rotation practice to activate the new video and pause the existing active ad named 'EU Laptop Deals' (ID 1116), logging the action with the rationale 'ab_test_response_to_engagement_surge'."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_adsets_by_category", kwargs={"category": "Electronics"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "112"}),
            Action(name="create_ad", kwargs={"adset_id": "112", "name": "Top_Performer_Video_Test", "creative_type": "video"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1116"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "112", "old_ad_id": "1116", "new_ad_id": "1119", "rationale": "ab_test_response_to_engagement_surge"})
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
            "You are a Compliance Officer performing a two-part audit on ad set 104. First, you must conduct a lookback verification, confirming its current settings match the 'plan_2025-08-12'. Then, apply our standard reward practice based on its strong 2025-08-13 performance by increasing its budget by 15% and its bid by $5. Ensure every action, including the initial verification checks, is logged using the standard reason code for today's operations."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-12"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-12", "adset_id": "104"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "reason": "plan_2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 850.0}),
            Action(name="update_adset_bid_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 25.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 850.0, "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 25.0, "reason": "plan_2025-08-13"})
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

