from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="066",
        instruction=(
            "You are a Trend Analyst. Check the 'Electronics' viewership sessions on 2025-08-07 and compare it to 2025-08-10. "
            "If the growth over these 3 days is greater than 10%, it signals strong momentum. "
            "In response, pause the lower-priority 'Electronics - EU' ad set (ID 112) to shift focus to other electronics ad sets, but only if it is currently active. "
            "Also log a 'trend_analysis' automation run with input_ref set to 'electronics_momentum'."

            "Also, the 'App Installs - Android' ad set has an undefined bid amount. "
            "To better control the cost per install, switch its strategy to 'cost_cap' and set a specific bid of $2.0. "
            "Log the strategy change with reason 'Set CPI Target'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-07", "category": "Electronics"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-10", "category": "Electronics"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 13500, "previous_value": 12000}), # Returns 12.5% growth
            Action(name="compare_value", kwargs={"value": 12.5, "threshold": 10, "operator": "greater"}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "112"}), # Returns 'active'
            Action(name="update_adset_status", kwargs={"adset_id": "112", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "trend_analysis",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "electronics_momentum", "errors_json": "{}"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - Android'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "110"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "110", "new_strategy": "cost_cap", "new_bid": 2.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 2.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Set CPI Target"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="067",
        instruction=(
            "You are a Trend Analyst. Check the 'Apparel' viewership sessions on 2025-08-12 and compare it to 2025-08-13. "
            "If the growth over this day is less than 2%, it signals a weak trend. "
            "In response, pre-emptively pause the 'Apparel - US' ad set (ID 102) to conserve budget, but only if it is currently active. "
            "Also log a 'trend_pause' automation run with input_ref set to 'apparel_weak_growth'."

            "Also, the 'App Installs - iOS' ad set is on 'cost_cap', but the team wants to experiment with the platform's algorithm. "
            "Change the strategy to 'lowest_cost' to see if it improves performance. The bid amount should be set to null. "
            "Log the change for the A/B test with reason 'A/B Test: Algorithmic Bid'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-12", "category": "Apparel"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 12000, "previous_value": 11800}), # Returns 1.69% growth
            Action(name="compare_value", kwargs={"value": 1.694915254237288, "threshold": 2, "operator": "less"}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "102"}), # Returns 'active'
            Action(name="update_adset_status", kwargs={"adset_id": "102", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "apparel_weak_growth", "errors_json": "{}"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - iOS'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "111"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "111"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "111", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "A/B Test: Algorithmic Bid"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="068",
        instruction=(
            "You are a Trend Analyst. Check the 'Electronics' viewership sessions on 2025-08-10 and compare it to 2025-08-13. "
            "If the growth over these 3 days is less than 12%, it signals a slowing trend, "
            "and you should pause the 'Back to School - Laptops' ad set to conserve budget. "
            "Also log a 'trend_pause' automation run with input_ref set to 'electronics_slowing'."

            "Also, the 'Fall Fashion - Men' ad set is part of a 'Traffic' campaign, but its 'lowest_cost' strategy is not driving enough volume. "
            "Update its strategy to 'cost_cap' with a generous bid of $28.0 to be more competitive in the auction. "
            "Log the strategy change with reason 'Increase competitiveness'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Back to School - Laptops'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-10", "category": "Electronics"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 15000, "previous_value": 13500}), # Returns 11.11% growth
            Action(name="compare_value", kwargs={"value": 11.11111111111111, "threshold": 12, "operator": "less"}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "108"}), # Returns 'active'
            Action(name="update_adset_status", kwargs={"adset_id": "108", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "electronics_slowing", "errors_json": "{}"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Men'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "105"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "105"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "105", "new_strategy": "cost_cap", "new_bid": 28.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 28.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Increase competitiveness"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="069",
        instruction=(
            "You are a Trend Analyst. Check the 'Electronics' viewership sessions on 2025-08-07 and compare it to 2025-08-13. "
            "If the growth over these 6 days is greater than 30%, the trend is considered exhausted. "
            "In response, pause the 'Electronics - US' ad set to avoid ad fatigue, but only if it is currently active. "
            "Log a 'trend_analysis' automation run with input_ref 'electronics_exhaustion_check'. If no action is taken, log the status as 'skipped'."

            "Also, The 'Brand - Video Ads' ad set is for an 'Awareness' campaign. "
            "Its current 'lowest_cost' strategy is correct, but we need to reset any potentially lingering bid data. "
            "Re-apply the 'lowest_cost' strategy and ensure the bid amount is explicitly null. "
            "Log this as a strategy reset with reason 'Strategy Reset'."

        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - US'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-07", "category": "Electronics"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 15000, "previous_value": 12000}), # Returns 25% growth
            Action(name="compare_value", kwargs={"value": 25, "threshold": 30, "operator": "greater"}), # Returns false, no pause.
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "trend_analysis",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "skipped", 
                    "input_ref": "electronics_exhaustion_check", "errors_json": "{}"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'Brand - Video Ads'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "103"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "103"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "103", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "lowest_cost", "old_bid": None, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strategy Reset"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="074",
        instruction=(
            "You are a Bid Optimizer. The 'Fall Fashion - Men' ad set is being prepared for a new creative test. "
            "As part of the prep, switch its strategy to 'cost_cap' with a bid of $23.0 and then pause the ad set pending the new creatives. "
            "Log the strategy change with reason 'Prep for Creative Test'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Men'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "105"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "105"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "105", "new_strategy": "cost_cap", "new_bid": 23.0}),
            Action(name="update_adset_status", kwargs={"adset_id": "105", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 23.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Prep for Creative Test"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="076",
        instruction=(
            "You are a Bid Optimizer. The bid for 'Electronics - US' ad set needs to be aligned with the latest plan. "
            "Find the bid amount for this ad set in 'plan_2025-08-12' and apply it. "
            "Keep the strategy as 'cost_cap'. Log the reversion with reason 'Realign to Plan 2025-08-12'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - US'}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-12"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "101"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "101"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "101", "new_strategy": "cost_cap", "new_bid": 32.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 32.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Realign to Plan 2025-08-12"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="082",
        instruction=(
            "You are a Bid Optimizer. To prepare for an upcoming A/B test, change the strategy for the 'Brand - Video Ads' ad set to 'bid_cap' with a value of $0.50. "
            "Then, ensure the ad set is active for the test to run. "
            "Log the strategy change with reason 'A/B Test Preparation'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Brand - Video Ads'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "103"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "103"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "103", "new_strategy": "bid_cap", "new_bid": 0.50}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "103"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "bid_cap", "old_bid": None, "new_bid": 0.50, "changed_at": "2025-08-13T01:01:01Z", "reason": "A/B Test Preparation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="085",
        instruction=(
            "You are a Bid Optimizer. The 'Fall Fashion - Women' ad set needs its bid updated based on the 'plan_2025-08-13'. "
            "Find the bid amount for this ad set in the plan and apply it, keeping the strategy as 'cost_cap'. "
            "Log the strategy change with reason 'Plan Alignment'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Women'}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "cost_cap", "new_bid": 22.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Plan Alignment"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="086",
        instruction=(
            "You are a Bid Optimizer. The bid strategy for 'Apparel - US' ad set is being reset. "
            "Change its strategy to 'cost_cap' but set the bid amount to $0 to effectively pause bidding without pausing the ad set. "
            "Log this as a strategy change with reason 'bidding_pause'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Apparel - US'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "102"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "102"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "102", "new_strategy": "cost_cap", "new_bid": 0.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 0.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "bidding_pause"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="002",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold of 1.5 to all active ad sets. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below 1.5, "
            "and for ad sets with ROAS above 13, increase their budget by 10%. "
            "Add logging for any budget change with reason 'ROAS update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 649.0}),

            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 649.0, 'old_budget': 590.0, 
                        'reason': 'ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="003",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold of 1.5 to all active ad sets. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below 1.5, "
            "and for ad sets with ROAS above 13, increase their budget by 10%. "
            "For ad sets with 'App Installs - Android' and 'App Installs - iOS' names apply a special rule: "
            "if CPA is below $6, increase budget by 15%."
            "Add logging for any budget change with reason 'ROAS update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 649.0}),


            
            Action(name="search_adsets_by_name", kwargs={"name_query": "App Installs"}),

            Action(name="get_name_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "111"}),


            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1150.0}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1150.0}),


            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 649.0, 'old_budget': 590.0, 
                        'reason': 'ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "110", "new_budget": 1150.0, 'old_budget': 1000.0, 
                        'reason': 'ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "111", "new_budget": 1150.0, 'old_budget': 1000.0, 
                        'reason': 'ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="004",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold of 1.5 to all active ad sets. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below 1.5, "
            "and for ad sets with ROAS above 13, increase their budget by 10%. "
            "For ad sets from campaign 'Mobile App Installs Campaign' apply a special rule: "
            "if CPA is below $16, increase budget by 15%."
            "Add logging for any budget change with reason 'ROAS/CPA update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 649.0}),

            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Mobile App Installs Campaign"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1150.0}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1150.0}),

            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 649.0, 'old_budget': 590.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "110", "new_budget": 1150.0, 'old_budget': 1000.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "111", "new_budget": 1150.0, 'old_budget': 1000.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="005",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for ad sets with ROAS above 13, increase their budget by 10%. "
            "For ad sets from campaign 'Mobile App Installs Campaign' apply a special rule (this rule takes precedence): "
            "if CPA is below $7, increase budget by 15%."
            "Add logging for any budget change with reason 'ROAS/CPA update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 649.0}),

            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Mobile App Installs Campaign"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1150.0}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1150.0}),

            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 649.0, 'old_budget': 590.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "110", "new_budget": 1150.0, 'old_budget': 1000.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "111", "new_budget": 1150.0, 'old_budget': 1000.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="006",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for ad sets with ROAS above 12, increase their budget by 20%. "
            "For ad sets from campaign 'Fall Collection Launch' apply a special rule (this rule takes precedence): "
            "if CPA is above $9, increase budget by 15%."
            "Add logging for any budget change with reason 'ROAS/CPA update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),

            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 862.5}),

            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 708.0, 'old_budget': 590.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "105", "new_budget": 862.5, 'old_budget': 750.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "107", "new_budget": 480.0, 'old_budget': 400.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "112", "new_budget": 840.0, 'old_budget': 700.0, 
                        'reason': 'ROAS/CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="007",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for ad sets with ROAS above 12, increase their budget by 20%. "
            "For ad sets from campaign 'Fall Collection Launch' apply a special rule (this rule takes precedence): "
            "if CPA is below $10, increase budget by 15%."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),

            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 15}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 851.0}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 862.5}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="008",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for ad sets with ROAS above 12, increase their budget by 20%. "
            "For ad sets from campaign 'Fall Collection Launch' apply a special rule (this rule takes precedence): "
            "if CPA is below $9, increase budget by 15%."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),

            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 851.0}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="009",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for ad sets with ROAS above 12, increase their budget by 20%. "
            "For ad sets from campaign 'Holiday Season Early Bird' apply a special rule (this rule takes precedence): "
            "if CPA is below $10, increase budget by 20%."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),

            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Holiday Season Early Bird"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 600.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="010",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Apply the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. "
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for ad sets with ROAS above 11.5, increase their budget by 20%. "
            "For ad sets with 'Holiday' substring in name apply a special rule (this rule takes precedence): "
            "if CPA is below $10, increase budget by 20%."
            "Add logging for any budget change with reason 'CPA/ROAS update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),

            
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday"}),

            Action(name="get_name_for_adset", kwargs={"adset_id": "106"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "107"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 600.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),


            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 708.0, 'old_budget': 590.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "112", "new_budget": 840.0, 'old_budget': 700.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "106", "new_budget": 600.0, 'old_budget': 500.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "107", "new_budget": 480.0, 'old_budget': 400.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="011",
        instruction=(
            "You are a Performance Marketing Analyst."
            "For data from period 2025-08-07 to 2025-08-13, pause any active ad set with ROAS below "
            "the policy value of 'min_roas_threshold_7d', "
            "and for active ad sets with ROAS above 12.5, increase their budget by 20%. "
            "For ad sets with 'Holiday' substring in name apply a special rule (this rule takes precedence): "
            "if CPA is below $20, increase budget by 20%."
            "Add logging for any budget change with reason 'CPA/ROAS update'. "
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),

            
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday"}),

            Action(name="get_name_for_adset", kwargs={"adset_id": "106"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "107"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 600.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),


            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "102", "new_budget": 708.0, 'old_budget': 590.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "112", "new_budget": 840.0, 'old_budget': 700.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "106", "new_budget": 600.0, 'old_budget': 500.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "107", "new_budget": 480.0, 'old_budget': 400.0, 
                        'reason': 'CPA/ROAS update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="012",
        instruction=(
            "You are a Performance Marketing Analyst."
            "For data from period 2025-08-07 to 2025-08-13, pause any ad set with CPA below $10 "
            "and for ad sets with CPA above or equal to $10, increase their budget by 10%. "
            "For ad sets with 'Holiday' substring in name apply a special rule (this rule takes precedence): "
            "if CPA is below $20, increase budget by 20%."
            "Add logging for any budget change with reason 'CPA update'. "
        ),
        actions=[
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="update_adset_status", kwargs={"adset_id": "102", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "104", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "105", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "108", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "111", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "112", "new_status": "paused"}),


            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1012.0}),
            
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday"}),

            Action(name="get_name_for_adset", kwargs={"adset_id": "106"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "107"}),

            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 600.0}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 480.0}),

            Action(name="get_current_timestamp", kwargs={}),

            Action(name="log_budget_change",
                kwargs={"adset_id": "101", "new_budget": 1012.0, 'old_budget': 920.0, 
                        'reason': 'CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "106", "new_budget": 600.0, 'old_budget': 500.0, 
                        'reason': 'CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "107", "new_budget": 480.0, 'old_budget': 400.0, 
                        'reason': 'CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="015",
        instruction=(
            "You are a Performance Marketing Analyst."
            "A performance report shows that for the 'Fall Fashion - Women' ad set (ID 104), "
            "the paused video ad (ID 1107) has a 12% lower CPA than the active image ad (ID 1106). "
            "Since this exceeds the 'video_cpa_advantage_pct' policy threshold (currently 10%), "
            "perform a creative rotation. Pause ad 1106 and activate ad 1107. "
            "To support the new creative, increase the ad set's budget by 5%. "
            "Log the budget change with reason 'Creative Rotation Support' and "
            "log the entire operation as a 'creative_rotation' automation run with ID 'AR-CR-20250814-01' and "
            "input_ref adset_104_cpa_policy."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 12, "threshold": 10, "operator": "greater"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1106"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1107"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1106", "new_status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1107", "new_status": "active"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 5}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 777.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 777.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Creative Rotation Support"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-01", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "adset_104_cpa_policy", "errors_json": "{}"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="050",
        instruction=(
            "You are a Performance Auditor. Our policy requires a minimum 7-day ROAS, defined by 'min_roas_threshold_7d', for all ad sets using the 'lowest_cost' bid strategy. "
            "The used period is 2025-08-07 to 2025-08-13. "
            "If the ROAS is below the policy threshold, pause the ad set."
            "For logging, add a 'roas_policy_enforcement' automation run with input_ref 'policy_min_roas_threshold_7d'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_roas_threshold_7d"}), # returns 1.5
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="search_adsets_by_bid_strategy", kwargs={"bid_strategy": "lowest_cost"}),

            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}), # > 1.5
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}), # < 1.5
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}), # > 1.5
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}), # > 1.5
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}), # < 1.5
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}), # > 1.5
            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="update_adset_status", kwargs={"adset_id": "110", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "roas_policy_enforcement",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "policy_min_roas_threshold_7d", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="051",
        instruction=(
            "You are an Audience Growth Analyst. Review the viewership for the 'Electronics' category on 2025-08-13. "
            "If today's sessions are more than 10% above the 7-day average for the period 2025-08-07 to 2025-08-13, "
            "boost the budget for the 'Electronics - US' ad set by 15% to capitalize on the surge. "
            "Log the change with reason 'Surge in User Interest'."

            "Also, the 'App Installs - iOS' ad set is on 'cost_cap', but the team wants to experiment with the platform's algorithm. "
            "Change the strategy to 'lowest_cost' to see if it improves performance. The bid amount should be set to null. "
            "Log the change for the A/B test with reason 'A/B Test: Algorithmic Bid'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 15000.0, "previous_value": 13500.0}),
            Action(name="compare_value", kwargs={"value": 11.11111111111111, "threshold": 10, "operator": "greater"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - US"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1058.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1058.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Surge in User Interest"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - iOS'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "111"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "111"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "111", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "A/B Test: Algorithmic Bid"}),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="052",
        instruction=(
            "You are a Budget Efficiency Agent. Review viewership for the 'Office' category on 2025-08-13. "
            "If the number of 'active_users' is above 100, find all paused ad sets in this category. "
            "For each such ad set, check if it has a budget allocation in 'plan_2025-08-13'. "
            "If it does NOT, enable the ad set to test how it works now. "
            "Also log a 'low_viewership_test' automation run with input_ref set to plan name. "
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Office"}),
            Action(name="compare_value", kwargs={"value": 1000, "threshold": 100, "operator": "greater"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),

            Action(name="search_adsets_by_category", kwargs={"category": "Office"}), # Finds ad set 109
            Action(name="get_status_for_adset", kwargs={"adset_id": "109"}),

            Action(name="update_adset_status", kwargs={"adset_id": "109", "new_status": "active"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "low_viewership_test",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "plan_2025-08-13", "errors_json": "{}"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="053",
        instruction=(
            "You are a Strategy Analyst. For the 'Toys' category, compare its weekly sales units (Aug 7-13) "
            "to its daily active users on the last day of that week (Aug 13). "
            "If the weekly sold units is less than the daily active users, it indicates a conversion issue. "
            "If is a conversion issue, you should switch the bid strategy for 'Holiday - Toys' ad set"
            "from 'lowest_cost' to 'cost_cap' with a bid of $15.0 to focus on higher-intent users. "
            "Log the strategy change with reason 'Low sold units per active users'. "
            "Also log a 'viewership_to_sales_check' automation run with input_ref set to 'adset'. "
        ),
        actions=[
            Action(name="get_sales_for_category_in_period", kwargs={"start_date": "2025-08-07", "end_date": "2025-08-13", "category": "Toys"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Toys"}),
            Action(name="compare_value", kwargs={"value": 300, "threshold": 2000, "operator": "less"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Toys"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "107"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "107"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "107", "new_strategy": "cost_cap", "new_bid": 15.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 15.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low sold units per active users"}),
            Action(name="add_automation_run", kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "viewership_to_sales_check", "started_at": "2025-08-13T01:01:01Z", "ended_at": "2025-08-13T01:01:01Z", "status": "completed", "input_ref": "adset", "errors_json": "{}"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="054",
        instruction=(
            "You are a Trend Analyst. Compare 'Electronics' viewership sessions on 2025-08-08 to 2025-08-11. "
            "If the growth over these 3 days is less than 15%,  "
            "you should pause the 'Electronics - EU' ad set to conserve budget, but only if it is currently active. "
            "Also log a 'trend_pause' automation run with input_ref set to 'trend'. "

            "Also, the bid for 'Fall Fashion - Women' ad set is underperforming. "
            "Check if its current bid is less than $22.0. If it is, reset its strategy from 'cost_cap' to 'lowest_cost' to allow the algorithm to find a new cost baseline. "
            "Log the change with reason 'Performance Reset to Baseline'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-08", "category": "Electronics"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-11", "category": "Electronics"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 14000, "previous_value": 12500}), # Returns 12% growth
            Action(name="compare_value", kwargs={"value": 12, "threshold": 15, "operator": "less"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - EU'}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "112"}), # Returns 'active'
            Action(name="update_adset_status", kwargs={"adset_id": "112", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "trend", "errors_json": "{}"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Women"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="compare_value", kwargs={"value": 20.0, "threshold": 22.0, "operator": "less"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 20.0, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "Performance Reset to Baseline"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="055",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, "
            "the 'Mobile' category had more than double the user sessions of the 'Home' category. "
            "To capitalize on this, decrease the budget of the 'Holiday - Home Goods' "
            "ad set by 20% and increase the budget of the 'App Installs - Android' ad set by 20%. "
            "Log both changes with the reason 'Viewership-Based Reallocation'."

            "Also, the 'Back to School - Stationery' ad set is currently paused. "
            "Prepare it for reactivation by changing its strategy from 'lowest_cost' to 'cost_cap' with a starting bid of $5.0. "
            "After setting the strategy, activate the ad set."
            "Log the change with reason 'Reactivation with CPA Target'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Home"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Home Goods"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "App Installs - Android"}),
            
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 400.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 400.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Viewership-Based Reallocation"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1200.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1200.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Viewership-Based Reallocation"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Stationery"}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "109"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "109"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "109"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "109", "new_strategy": "cost_cap", "new_bid": 5.0}),
            Action(name="update_adset_status", kwargs={"adset_id": "109", "new_status": "active"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "109", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 5.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Reactivation with CPA Target"}),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="056",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Electronics' category had more user sessions than the 'Apparel' category. "
            "To capitalize on this, you should decrease the budget of the 'Apparel - US' ad set by 15% and increase the budget of the 'Electronics - EU' ad set by 15%. "
            "Log both changes with the reason 'Electronics Viewership Lead'."

            "Also, the 'Electronics - US' ad set (ID 101) has a consistently high ROAS. "
            "To maintain profitability while scaling, switch its bid strategy from 'cost_cap' to 'lowest_cost' to explore if the algorithm can find more conversions efficiently. "
            "Log this change with reason 'High ROAS test'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Apparel - US"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - EU"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 590.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 501.5}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 501.5, "changed_at": "2025-08-13T01:01:01Z", "reason": "Electronics Viewership Lead"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 805.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 805.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Electronics Viewership Lead"}),

            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "101"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "101"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "101", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 32.0, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "High ROAS test"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="057",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Apparel' category had over 1.4 times the user sessions of the 'Home' category. "
            "To lean into this trend, you should decrease the budget of the 'Holiday - Home Goods' ad set by 10% and increase the budget of the 'Fall Fashion - Women' ad set by 10%. "
            "Log both changes with the reason 'Apparel Engagement Focus'."

            "Also, the 'Electronics - EU' ad set (ID 112) is part of a 'Sales' campaign and must have a defined cost target. "
            "Update its strategy from 'lowest_cost' to 'cost_cap' and set the bid amount to $30.0. "
            "Log the change as a policy compliance action with reason 'Policy Compliance: Sales CPA'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Home"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Home Goods"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Women"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 450.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 450.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Apparel Engagement Focus"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 814.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 814.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Apparel Engagement Focus"}),

            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "112"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "112"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "112", "new_strategy": "cost_cap", "new_bid": 30.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 30.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Policy Compliance: Sales CPA"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="058",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Mobile' category had more than triple the sessions of the 'Toys' category. "
            "Deprioritize Toys by decreasing the 'Holiday - Toys' ad set budget by 25%, and reinvest that into Mobile by increasing the 'App Installs - iOS' ad set budget by 25%. "
            "Log both changes with the reason 'Mobile Dominance Shift'."

            "Also, the 'Holiday - Home Goods' ad set (ID 106) is currently on 'cost_cap' but the upcoming holiday sale requires maximizing reach. "
            "Change the bid strategy to 'lowest_cost' to allow the ad platform more flexibility. "
            "Log the change with reason 'Maximize holiday reach'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Toys"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Toys"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "App Installs - iOS"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 25}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 300.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 300.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mobile Dominance Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 25}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1250.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1250.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mobile Dominance Shift"}),

            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "106"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "106"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "106", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 18.0, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "Maximize holiday reach"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="059",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, viewership for 'Electronics' was over 1.8 times that of 'Home'. "
            "Shift budget from a lower-performing category by decreasing the 'Holiday - Home Goods' ad set budget by 5% and boosting a higher-performing one by increasing the 'Back to School - Laptops' budget by 5%. "
            "Log both changes with the reason 'Tech Trend Reallocation'."

            "Also, the 'App Installs - Android' ad set has an undefined bid amount. "
            "To better control the cost per install, switch its strategy to 'cost_cap' and set a specific bid of $2.0. "
            "Log the update with reason 'Set CPI Target'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Home"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Home Goods"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Laptops"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 5}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 475.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 475.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Tech Trend Reallocation"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 5}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 819.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 819.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Tech Trend Reallocation"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - Android'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "110"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "110", "new_strategy": "cost_cap", "new_bid": 2.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 2.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Set CPI Target"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="060",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Apparel' category had exactly double the user sessions of the 'Toys' category. "
            "This indicates a clear priority. Decrease the budget of the 'Holiday - Toys' ad set by 12% and increase the budget of the 'Fall Fashion - Men' ad set by 12%. "
            "Log both changes with the reason 'Fashion Season Push'."

            "Also, the 'Electronics - EU' ad set is using 'lowest_cost'. "
            "To better align with the US strategy, find the bid amount of the 'Electronics - US' ad set and apply it to the EU ad set, while also switching its strategy to 'cost_cap'."
            "Log the change with reason 'Align EU with US Bid Policy'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Toys"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Toys"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Men"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 12}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 352.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 352.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Fashion Season Push"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 12}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 840.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 840.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Fashion Season Push"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - US"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - EU"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "112"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "112"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "101"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "112", "new_strategy": "cost_cap", "new_bid": 32.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 32.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Align EU with US Bid Policy"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="061",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Mobile' category had over 1.25 times the sessions of the 'Electronics' category. "
            "Shift budgets to the stronger category by decreasing 'Electronics - EU' by 18% and increasing 'App Installs - Android' by 18%. "
            "Log both changes with the reason 'Mobile Growth Investment'."

            "Also, on 2025-08-13, the 'Apparel' category had more sessions than the 'Home' category. "
            "For the 'Apparel - US' ad set, its 7-day CPA is efficient at under $8.0. "
            "Based on these two positive signals, you should increase its budget by 10%. "
            "Round the budget and log the change with reason 'Positive Viewership & CPA'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - EU"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "App Installs - Android"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 700.0, "percent": 18}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 574.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 574.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mobile Growth Investment"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 18}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1180.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1180.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mobile Growth Investment"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'Apparel - US'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Home"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 649.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 650.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 650.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Positive Viewership & CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="062",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Electronics' category had more than double the user sessions of the 'Toys' category. "
            "Reallocate funds by decreasing the 'Holiday - Toys' ad set budget by 10% and increasing the 'Electronics - US' ad set budget by 10%. "
            "Log both changes with the reason 'High Engagement Reinvestment'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Toys"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Toys"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - US"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 360.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 360.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Engagement Reinvestment"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1012.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1012.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Engagement Reinvestment"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="063",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Apparel' category had four times the sessions of the 'Office' category. "
            "Take budget from the underperforming category by decreasing the 'Back to School - Stationery' ad set budget by 20%. Boost the 'Apparel - US' ad set by 20%. "
            "Log both changes with the reason 'Low Engagement De-Funding'."

            "Also, the current bid of $42.0 for 'Back to School - Laptops' is too high. "
            "Reduce the bid by 10% to improve efficiency, keeping the 'cost_cap' strategy. "
            "Log the adjustment with reason 'Efficiency Bid Reduction'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Office"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Stationery"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Apparel - US"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "109"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 300.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "109", "new_budget": 240.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "109", "old_budget": 300.0, "new_budget": 240.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Engagement De-Funding"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 708.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Engagement De-Funding"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Laptops"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "108"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 42.0, "percent": 10}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "108"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "108", "new_strategy": "cost_cap", "new_bid": 37.8}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 37.8, "changed_at": "2025-08-13T01:01:01Z", "reason": "Efficiency Bid Reduction"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="064",
        instruction=(
            "You are a Budget Strategist. On 2025-08-13, the 'Mobile' category had over 1.5 times the user sessions of the 'Apparel' category. "
            "To fund the top category, decrease the budget of the 'Fall Fashion - Women' ad set by 22% and increase the budget of the 'App Installs - iOS' ad set by 22%. "
            "Log both changes with the reason 'Top Performing Category Boost'."

            "Also, the 'Holiday - Toys' ad set (ID 107) needs to be prepared for a new plan that will use 'cost_cap'. "
            "Pre-emptively switch its strategy from 'lowest_cost' to 'cost_cap' with a conservative starting bid of $12.0. "
            "Log this preparatory change with reason 'Prepare for new plan'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Women"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "App Installs - iOS"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 740.0, "percent": 22}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 577.2}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 577.2, "changed_at": "2025-08-13T01:01:01Z", "reason": "Top Performing Category Boost"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 22}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1220.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1220.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Top Performing Category Boost"}),

            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "107"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "107"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "107", "new_strategy": "cost_cap", "new_bid": 12.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 12.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Prepare for new plan"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="065",
        instruction=(
            "You are a Budget Strategist. On 2025-08-12, the 'Electronics' category had more user sessions than the 'Apparel' category. "
            "Based on this trend, decrease the 'Fall Fashion - Men' ad set budget by 10% and increase the 'Electronics - US' ad set budget by 10%. "
            "Log both changes with the reason 'Viewership Trend Adjustment'."

            "Also, the strategy for the ad set 'Back to School - Laptops' is too aggressive with a bid over $40. "
            "Confirm the bid is over this threshold, and if so, revert the strategy to 'lowest_cost' to find more efficient conversions. "
            "Log the reversion with reason 'Cost Reduction Revert'."

        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-12", "category": "Apparel"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-12", "category": "Electronics"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Men"}),
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - US"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 750.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 675.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 675.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Viewership Trend Adjustment"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1012.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1012.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Viewership Trend Adjustment"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Laptops"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "108"}),
            Action(name="compare_value", kwargs={"value": 42.0, "threshold": 40.0, "operator": "greater"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "108"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "108", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 42.0, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "Cost Reduction Revert"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="070",
        instruction=(
            "You are a Trend Analyst. Check the 'Electronics' viewership sessions sessions on 2025-08-09 and compare it to 2025-08-10. "
            "If the growth over this day is less than 5%, it signals a stall. "
            "In response, pre-emptively pause the 'Electronics - US' ad set (ID 101) to conserve budget, if it is active. "
            "Also log a 'trend_pause' automation run with input_ref set to 'electronics_stall'."

            "Also, Management has approved a more aggressive bid for the 'Fall Fashion - Women' ad set. "
            "Increase its current 'cost_cap' bid amount from $20.0 to $24.0. The strategy type should remain the same. "
            "Log this manual bid update with reason 'Manual Bid Increase'."
        ),
        actions=[
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-09", "category": "Electronics"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-10", "category": "Electronics"}),
            Action(name="calculate_percentage_change", kwargs={"current_value": 13500, "previous_value": 13000}), # Returns 3.84% growth
            Action(name="compare_value", kwargs={"value": 3.8461538461538463, "threshold": 5, "operator": "less"}),
            Action(name="get_status_for_adset", kwargs={"adset_id": "101"}), # Returns 'active'
            Action(name="update_adset_status", kwargs={"adset_id": "101", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "electronics_stall", "errors_json": "{}"}),


            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Women'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "cost_cap", "new_bid": 24.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 24.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Manual Bid Increase"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="071",
        instruction=(
            "You are a Bid Optimizer. The 'App Installs - Android' ad set has an undefined bid amount. "
            "To better control the cost per install, switch its strategy to 'cost_cap' and set a specific bid of $2.0. "
            "Log the update with reason 'Set CPI Target'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - Android'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "110"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "110", "new_strategy": "cost_cap", "new_bid": 2.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 2.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Set CPI Target"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="072",
        instruction=(
            "You are a Bid Optimizer. The 'Electronics - EU' ad set is part of a 'Sales' campaign and must have a defined cost target. "
            "Update its strategy from 'lowest_cost' to 'cost_cap' and set the bid amount to $30.0. "
            "Log the change as a policy compliance action with reason 'Policy Compliance: Sales CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - EU'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "112"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "112"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "112", "new_strategy": "cost_cap", "new_bid": 30.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 30.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Policy Compliance: Sales CPA"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="073",
        instruction=(
            "You are a Bid Optimizer. For the 'Fall Collection Launch' campaign, all ad sets must be on 'cost_cap' to control spending during the launch. "
            "Find the ad set 'Fall Fashion - Men' and update its strategy from 'lowest_cost' to 'cost_cap' with a starting bid of $21.50. "
            "Log the change with reason 'Launch Cost Control'."

            "Also, the bid for 'Holiday - Home Goods' ad set is too conservative. "
            "Increase the current 'cost_cap' bid amount by 25% to capture more of the holiday audience. "
            "The strategy type will remain the same. "
            "You should log the bid increase as a strategy change with reason 'Aggressive Bid Increase'."

        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Men'}),
            Action(name="get_campaign_id_for_adset", kwargs={"adset_id": "105"}),
            Action(name="get_name_for_campaign", kwargs={"campaign_id": "3"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "105"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "105"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "105", "new_strategy": "cost_cap", "new_bid": 21.50}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 21.50, "changed_at": "2025-08-13T01:01:01Z", "reason": "Launch Cost Control"}),


            Action(name="search_adsets_by_name", kwargs={"name_query": 'Holiday - Home Goods'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "106"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 18.0, "percent": 25}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "106", "new_strategy": "cost_cap", "new_bid": 22.5}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 22.5, "changed_at": "2025-08-13T01:01:01Z", "reason": "Aggressive Bid Increase"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="090",
        instruction=(
            "You are a Growth Analyst. The 'Electronics' category had over 14,000 sessions on 2025-08-13, indicating high interest. "
            "Capitalize on this by increasing the budget for the 'Electronics - US' ad set by 15%, provided its 7-day ROAS (Aug 7-13) is above 9.0. "
            "The final budget must be rounded to the policy unit. Log the change with reasong 'High Viewership & ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - US'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 1058.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1060.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1060.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Viewership & ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="092",
        instruction=(
            "You are a Growth Analyst. The average daily sessions for the 'Apparel' category from Aug 7-13 exceeded 1,500. "
            "This sustained interest warrants a budget increase. For the 'Fall Fashion - Women' ad set, which has a 7-day CPA below $9.0, increase its budget by 20%. "
            "Round the final amount according to policy and log the update with reason 'Sustained Viewership & Low CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Women'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Apparel", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 20}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 888.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 890.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 890.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Sustained Viewership & Low CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="093",
        instruction=(
            "You are a Budget Analyst. Average active users for the 'Home' category (Aug 7-13) were below 3,000. "
            "This low engagement combined with a high 7-day CPA (over $8.0) for the 'Holiday - Home Goods' ad set requires a budget cut of 30%. "
            "Round the new budget and log the change with reason 'Low Engagement & High CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Holiday - Home Goods'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Home", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 30}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 350.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 350.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 350.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Engagement & High CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="094",
        instruction=(
            "You are a Growth Analyst. The 'Mobile' category on 2025-08-13 had over 15,000 sessions. "
            "This high traffic is valuable. For the 'App Installs - iOS' ad set, which has a 7-day CPA under $5.0, increase the budget by a significant 40%. "
            "Round the final budget according to policy and log the update with reason 'High Traffic & Efficient CPA'."

            "Also, the 'Apparel - US' ad set is on a 'lowest_cost' strategy but needs tighter cost control. "
            "Switch its bid strategy to 'cost_cap' and set a starting bid amount of $25.0 to enforce a CPA target. "
            "Log this as a strategy change with reason 'Enforce CPA Target'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - iOS'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 40}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 1400.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1400.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1400.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Traffic & Efficient CPA"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'Apparel - US'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "102"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "102"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "102", "new_strategy": "cost_cap", "new_bid": 25.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 25.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Enforce CPA Target"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="095",
        instruction=(
            "You are a Budget Analyst. On 2025-08-13, viewership for the 'Toys' category was under 7,000 sessions. "
            "This suggests low seasonal interest. Decrease the budget for the 'Holiday - Toys' ad set by 15%, since its ROAS (Aug 7-13) is just above breakeven. "
            "Round the new budget and log the change with reason 'Low Seasonal Viewership'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Holiday - Toys'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Toys"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 340.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 340.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 340.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Seasonal Viewership"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="096",
        instruction=(
            "You are a Growth Analyst. The average active users for 'Electronics' (Aug 7-13) was over 3,500. "
            "For the highly effective 'Back to School - Laptops' ad set, which has a 7-day ROAS over 11, increase its budget by 12%. "
            "Round the new budget and log the change with reason 'High Engagement & ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Back to School - Laptops'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 12}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 873.6, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 870.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 870.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Engagement & ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="097",
        instruction=(
            "You are a Budget Analyst. Average active users for 'Apparel' (Aug 7-13) was below 3500. "
            "This signals softening interest. For the 'Fall Fashion - Men' ad set, which has a high CPA (over $9), decrease the budget by 18%. "
            "Round the new budget according to policy and log the change with reason 'Softening Interest & High CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Men'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Apparel", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 750.0, "percent": 18}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 615.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 620.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 620.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Softening Interest & High CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="098",
        instruction=(
            "You are a Growth Analyst. The 'Electronics - EU' ad set has a strong 7-day ROAS over 12. "
            "On 2025-08-13, the Electronics category had over 14,500 sessions. This combination of factors warrants a 22% budget increase. "
            "Round the final budget based on policy and log the change with reason 'Strong Performance & Viewership'."

            "Also, to unify our mobile strategy, the 'App Installs - Android' ad set must mirror the 'App Installs - iOS' ad set. "
            "Update the Android ad set's strategy from 'lowest_cost' to 'cost_cap' and apply the same bid amount as the iOS ad set. "
            "Log the change as a strategy change with reason 'Strategy Alignment'."

        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - EU'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 22}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 854.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 850.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 850.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strong Performance & Viewership"}),


            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - Android'}),
            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - iOS'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "111"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "111"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "110"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "110"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "110", "new_strategy": "cost_cap", "new_bid": 2.5}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "110", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 2.5, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strategy Alignment"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="101",
        instruction=(
            "You are a Growth Analyst. The 'Apparel' category had over 11,000 sessions on 2025-08-13, but the 'Fall Fashion - Men' ad set has a 7-day CPA over $9.0. "
            "Due to this inefficiency despite high interest, decrease its budget by 15%. "
            "The final budget must be rounded to the policy unit. Log the change with reason 'High Viewership & Inefficient CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Men'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 750.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 637.5, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 640.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 640.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Viewership & Inefficient CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="102",
        instruction=(
            "You are a Budget Analyst. The average viewership for the 'Toys' category (Aug 7-13) is below 8,000 sessions, but the 'Holiday - Toys' ad set shows an excellent 7-day ROAS above 12.0. "
            "Reward this high-performing ad set in a low-traffic category with a 25% budget increase. "
            "Round the new budget and log the change with reason 'Reward High ROAS in Low Viewership Category'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Holiday - Toys'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Toys", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 25}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 500.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 500.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 500.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Reward High ROAS in Low Viewership Category"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="103",
        instruction=(
            "You are a Growth Analyst. The 'Mobile' category on 2025-08-13 had over 19,000 sessions. "
            "For the 'App Installs - Android' ad set, which has a 7-day (Aug 7-13) CPA under $6.0, increase the budget by 30%. "
            "Round the final amount and log the update with reason 'High Session Count & Efficient CPA'."

            "Also, the 'Electronics - EU' ad set is part of a 'Sales' campaign and must have a defined cost target. "
            "Update its strategy from 'lowest_cost' to 'cost_cap' and set the bid amount to $30.0. "
            "Log the change as a strategy change with reason 'Policy Compliance: Sales CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - Android'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 30}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 1300.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1300.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1300.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Session Count & Efficient CPA"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - EU'}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "112"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "112"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "112", "new_strategy": "cost_cap", "new_bid": 30.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_strategy_change", kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap", "old_bid": None, "new_bid": 30.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Policy Compliance: Sales CPA"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="104",
        instruction=(
            "You are a Budget Analyst. Average active users for 'Electronics' (Aug 7-13) was strong at over 3,700. "
            "The 'Electronics - EU' ad set has an excellent 7-day ROAS above 12.5. This justifies an 18% budget increase. "
            "Round the new budget according to policy and log the change with reason 'Strong User Base & ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - EU'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 18}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 826.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 830.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 830.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strong User Base & ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="105",
        instruction=(
            "You are a Growth Analyst. Viewership for 'Home' was low on 2025-08-13 (fewer than 9,000 sessions). "
            "The 'Holiday - Home Goods' ad set also has a 7-day CPA over $8.0. "
            "Given both poor signals, cut the budget by a significant 40%. "
            "Round the final budget and log the update with reason 'Low Viewership & Inefficient CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Holiday - Home Goods'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Home"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 40}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 300.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 300.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 300.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Viewership & Inefficient CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="106",
        instruction=(
            "You are a Budget Analyst. Average viewership for 'Apparel' (Aug 7-13) was high. "
            "The 'Fall Fashion - Men' ad set has a strong 7-day ROAS over 11.0. "
            "Reward this strong performance in a high-interest category with a 15% budget increase. "
            "Round the new budget and log the change with reason 'Sustained Viewership & Strong ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Fall Fashion - Men'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Apparel", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 862.5, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 860.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 860.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Sustained Viewership & Strong ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="107",
        instruction=(
            "You are a Growth Analyst. Viewership for 'Electronics' on 2025-08-13 is high, but the 'Electronics - US' ad set has a 7-day ROAS below 10.5. "
            "This indicates inefficiency. Decrease its budget by a modest 8% to improve overall campaign ROAS. "
            "Round the final budget and log the change with reason 'Inefficient ROAS Despite High Viewership'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - US'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 920.0, "percent": 8}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 846.4, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 850.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 850.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inefficient ROAS Despite High Viewership"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="108",
        instruction=(
            "You are a Budget Analyst. The 'Mobile' category had over 7,500 active users on 2025-08-13. "
            "The 'App Installs - iOS' ad set has an extremely efficient 7-day CPA under $4.6. "
            "This warrants an aggressive 35% budget increase. Round and log the change with reason 'High User Count & Excellent CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'App Installs - iOS'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Mobile"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "111", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 35}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 1350.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1350.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1350.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High User Count & Excellent CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="109",
        instruction=(
            "You are a Growth Analyst. The average number of sessions for the 'Toys' category (Aug 7-13) is low. "
            "The 'Holiday - Toys' ad set has a 7-day CPA above $7.5, which is inefficient for this category. "
            "Cut the budget by 22%. Round and log the change with reason 'Low Avg Viewership & High CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Holiday - Toys'}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Toys", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 22}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 312.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 310.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 310.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Avg Viewership & High CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="110",
        instruction=(
            "You are a Budget Analyst. The 'Apparel - US' ad set has a strong 7-day ROAS above 13.0. "
            "Furthermore, the Apparel category had high viewership on 2025-08-13. "
            "These combined positive signals justify a 15% budget increase. "
            "Round the budget and log the change with reason 'Excellent ROAS & High Viewership'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Apparel - US'}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 678.5, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Excellent ROAS & High Viewership"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="016",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Run a daily performance check for campaign 'Q3 Brand Awareness Push' for 2025-08-13. "
            "Identify any active ad sets that had ROAS 0. "
            "For any such ad set, pause it immediately. "
            "Then, create a new 'Sales' campaign called "
            "'Review_Underperformers_2025-08-13'. "
            "Create a new 'paused' ad set within this campaign, "
            "With category 'All' and name 'Video Ads Europe' "
            "but setting the budget to a minimal $10 for later review."
            "Also, for active ad sets with 'Back to School' substring in name "
            "increase budget by 30% if CPA between 2025-08-07 and 2025-08-13 is below $10."
            "Add logging for any budget change with reason 'CPA update'. "

        ),
        actions=[
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Q3 Brand Awareness Push"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "2"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_campaign", 
                kwargs={"campaign_id": "12", "name": "Review_Underperformers_2025-08-13", 
                "objective": "Sales", "created_date": "2025-08-14", "status": "active"}),
            Action(name="add_adset",
                kwargs={"adset_id": "114", "campaign_id": "12", "name": "Video Ads Europe", 
                "category": "All", "daily_budget": 10.0, "bid_strategy": "lowest_cost", 
                "bid_amount": None, "status": "paused", "updated_at": "2025-08-13T01:01:01Z"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 30}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 1014.0}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "108", "new_budget": 1014.0, 'old_budget': 780.0, 
                        'reason': 'CPA update', 'changed_at': '2025-08-13T01:01:01Z'}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="017",
        instruction=(
            "You are in charge of bugets."
            "You should decrease the budget for all ad sets from the 'Q3 Brand Awareness Push' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Global Summer Sale' campaign budget by 20% for every ad set. "
            "Log all budget changes with the reason 'Q3 Budget Shift'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Q3 Brand Awareness Push"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "2"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "103"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "103", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Q3 Budget Shift"}),

            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1104.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1104.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Q3 Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 708.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 708.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Q3 Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 840.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 840.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Q3 Budget Shift"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="018",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Fall Collection Launch' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Holiday Season Early Bird' campaign budget by 25% for every ad set. "
            "Log all budget changes with the reason 'Seasonal Budget Adjustment'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Seasonal Budget Adjustment"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Seasonal Budget Adjustment"}),
            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Holiday Season Early Bird"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 25}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 625.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 625.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Seasonal Budget Adjustment"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 25}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 500.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 500.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Seasonal Budget Adjustment"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="019",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Back to School Deals' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Mobile App Installs Campaign' budget by 10% for every ad set. "
            "Log all budget changes with the reason 'Performance Rebalance'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Back to School Deals"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "6"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Performance Rebalance"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "109"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "109", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "109", "old_budget": 300.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Performance Rebalance"}),
            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Mobile App Installs Campaign"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Performance Rebalance"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Performance Rebalance"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="020",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Holiday Season Early Bird' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Fall Collection Launch' campaign budget by 15% for every ad set. "
            "Log all budget changes with the reason 'Strategic Priority Shift'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Holiday Season Early Bird"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strategic Priority Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strategic Priority Shift"}),

            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 851.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 851.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strategic Priority Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 862.5}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 862.5, "changed_at": "2025-08-13T01:01:01Z", "reason": "Strategic Priority Shift"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="021",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Mobile App Installs Campaign' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Q3 Brand Awareness Push' campaign budget by 40% for its ad set. "
            "Log all budget changes with the reason 'Objective Realignment'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Mobile App Installs Campaign"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Objective Realignment"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Objective Realignment"}),

            Action(name="search_campaigns_by_name", kwargs={"name_query": "Q3 Brand Awareness Push"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "2"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "103"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1180.0, "percent": 40}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "103", "new_budget": 1652.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 1652.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Objective Realignment"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="022",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Global Summer Sale' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Back to School Deals' campaign budget by 15% for every ad set. "
            "Log all budget changes with the reason 'Mid-Q3 Budget Review'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mid-Q3 Budget Review"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mid-Q3 Budget Review"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mid-Q3 Budget Review"}),
            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Back to School Deals"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "6"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 897.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 897.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mid-Q3 Budget Review"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "109"}),
            Action(name="increase_value_with_percent", kwargs={"value": 300.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "109", "new_budget": 345.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "109", "old_budget": 300.0, "new_budget": 345.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Mid-Q3 Budget Review"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="023",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Fall Collection Launch' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Global Summer Sale' campaign budget by 10% for every ad set. "
            "Log all budget changes with the reason 'Inventory-Based Budget Shift'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1012.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1012.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 649.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 649.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 770.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 770.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="024",
        instruction=(
            "You are in charge of budgets."
            "You should decrease the budget for all ad sets from the 'Fall Collection Launch' campaign "
            "to the value of 'min_budget_allocation' from policy params, "
            "and increase 'Global Summer Sale' campaign budget by 10% for every ad set. "
            "Additionally, ensure all resulting budgets are rounded to the nearest unit "
            "specified in the 'budget_rounding_unit' policy parameter. "
            "Log all budget changes with the reason 'Inventory-Based Budget Shift'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}), # returns 10
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 100.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 100.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 100.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 10}),
            Action(name="round_number_to_unit", kwargs={"number": 1012.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1010.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1010.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="round_number_to_unit", kwargs={"number": 649.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 650.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 650.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 10}),
            Action(name="round_number_to_unit", kwargs={"number": 770.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 770.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 770.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inventory-Based Budget Shift"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="025",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Run a daily performance check for the 'Q3 Brand Awareness Push' campaign for the date 2025-08-12. "
            "Identify any active ad sets that had a ROAS of exactly 0. "
            "For any such ad set, pause it. "
            "Then, create a new 'Traffic' campaign called 'Flagged_For_Review_2025-08-12'. "
            "Create a new 'paused' ad set within this new campaign with the category 'All' and the name 'Brand Content - Low Performance', setting the budget to a minimal $20 for later review. "
            "Separately, for any active ad sets with 'Holiday' in their name, increase their budget by 25% if their CPA for the period 2025-08-07 to 2025-08-13 was below $9. "
            "Add logging for any budget change with the reason 'CPA Performance Boost'."
        ),
        actions=[
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Q3 Brand Awareness Push"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "2"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-12"}),
            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_campaign", kwargs={"campaign_id": "12", "name": "Flagged_For_Review_2025-08-12", "objective": "Traffic", "created_date": "2025-08-14", "status": "active"}),
            Action(name="add_adset", kwargs={"adset_id": "114", "campaign_id": "12", "name": "Brand Content - Low Performance", "category": "All", "daily_budget": 20.0, "bid_strategy": "lowest_cost", "bid_amount": None, "status": "paused", "updated_at": "2025-08-13T01:01:01Z"}),

            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 25}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 625.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "new_budget": 625.0, 'old_budget': 500.0, 'reason': 'CPA Performance Boost', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 25}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 500.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "new_budget": 500.0, 'old_budget': 400.0, 'reason': 'CPA Performance Boost', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="026",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Run a performance check on all active ad sets for 2025-08-13. "
            "If any ad set has a ROAS less than 0.1, pause it immediately. "
            "Then, create a new 'Awareness' campaign called 'Global_Underperformers_Aug13'. "
            "Create a new 'paused' ad set within this campaign, with category 'Cross-Category' and name 'General Review Bin', setting the budget to $15. "
            "Also, for active ad sets in the 'Fall Collection Launch' campaign, increase the budget by 20% if their CPA between 2025-08-07 and 2025-08-13 is below $10. "
            "Log all budget changes with the reason 'Low CPA Incentive'."
        ),
        actions=[
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),



            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_campaign", kwargs={"campaign_id": "12", "name": "Global_Underperformers_Aug13", "objective": "Awareness", "created_date": "2025-08-14", "status": "active"}),
            Action(name="add_adset", kwargs={"adset_id": "114", "campaign_id": "12", "name": "General Review Bin", "category": "Cross-Category", "daily_budget": 15.0, "bid_strategy": "lowest_cost", "bid_amount": None, "status": "paused", "updated_at": "2025-08-13T01:01:01Z"}),

            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 888.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "new_budget": 888.0, 'old_budget': 740.0, 'reason': 'Low CPA Incentive', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 900.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "new_budget": 900.0, 'old_budget': 750.0, 'reason': 'Low CPA Incentive', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="027",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Run a performance check on the 'Global Summer Sale' campaign for 2025-08-13. "
            "If any active ad set has a ROAS below 12.5, pause it immediately and create a new review campaign. "
            "The new 'Sales' campaign should be named 'Summer_Sale_Review_Bin'. "
            "Inside it, create a 'paused' ad set named 'For review' and 'Review' for category, and a budget of $50. "
            "Additionally, for active ad sets in the 'Holiday Season Early Bird' campaign, increase their budget by 15% if their CPA for the period 2025-08-07 to 2025-08-13 is below $8.5. "
            "Log any budget change with the reason 'ROAS/CPA Combined Action'."
        ),
        actions=[
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="update_adset_status", kwargs={"adset_id": "101", "new_status": "paused"}),
            Action(name="add_campaign", kwargs={"campaign_id": "12", "name": "Summer_Sale_Review_Bin", "objective": "Sales", "created_date": "2025-08-14", "status": "active"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_adset", kwargs={"adset_id": "114", "campaign_id": "12", "name": "For review", "category": "Review", "daily_budget": 50.0, "bid_strategy": "lowest_cost", "bid_amount": None, "status": "paused", "updated_at": "2025-08-13T01:01:01Z"}),

            Action(name="search_campaigns_by_name", kwargs={"name_query": "Holiday Season Early Bird"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 500.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 575.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "new_budget": 575.0, 'old_budget': 500.0, 'reason': 'ROAS/CPA Combined Action', 'changed_at': '2025-08-13T01:01:01Z'}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="increase_value_with_percent", kwargs={"value": 400.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 460.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "new_budget": 460.0, 'old_budget': 400.0, 'reason': 'ROAS/CPA Combined Action', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="028",
        instruction=(
            "You are a Performance Marketing Analyst."
            "A performance report shows that for the 'Electronics - US' ad set, "
            "the paused video ad has a 15% lower CPA than the active image ad. "
            "Since this exceeds the 'video_cpa_advantage_pct' policy threshold (currently 10%), "
            "perform a creative rotation. Pause the image ad and activate the video ad. "
            "To support the new video creative, increase the ad set's budget by 8%. "
            "Log the budget change with reason 'Video Performance Rotation' and "
            "log the entire operation as a 'creative_rotation' automation run with ID 'AR-CR-20250814-02' and "
            "input_ref 'adset_101_cpa_policy'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - US"}),
            Action(name="search_ads_by_adset", kwargs={"adset_id": "101"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1101"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1102"}),


            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 15, "threshold": 10, "operator": "greater"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1101"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1102"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1101", "new_status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1102", "new_status": "active"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 8}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 993.6}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 993.6, "changed_at": "2025-08-13T01:01:01Z", "reason": "Video Performance Rotation"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-02", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "adset_101_cpa_policy", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="029",
        instruction=(
            "You are a Performance Marketing Analyst."
            "Data for the 'Back to School - Laptops' ad set (ID 108) indicates the paused video ad (ID 1112) has a 25% lower CPA than the active image ad (ID 1111). "
            "Check if this meets the 'video_cpa_advantage_pct' policy threshold (10%) and if so, perform a creative rotation by swapping the ad statuses. "
            "Following the rotation, increase the ad set's budget by 10% to capitalize on the better performance. "
            "Log the budget change with reason 'Creative Optimization' and "
            "log the process as a 'creative_rotation' automation run with ID 'AR-CR-20250814-03' and "
            "input_ref 'adset_108_cpa_check'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 25, "threshold": 10, "operator": "greater"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1111"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1112"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1111", "new_status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1112", "new_status": "active"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 858.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 858.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Creative Optimization"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-03", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "adset_108_cpa_check", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="030",
        instruction=(
            "You are a Performance Marketing Analyst."
            "A test for the 'Apparel - US' ad set shows the paused carousel ad has a 30% higher CTR than the active image ad. "
            "There is no specific policy for CTR, so use the 'video_cpa_advantage_pct' value of 10% as a general threshold for significant improvement. "
            "If the CTR improvement exceeds this threshold, rotate the creatives by pausing image ad and activating carousel ad. "
            "Then, boost the ad set budget by 15%. "
            "Log the budget change with reason 'CTR-based Rotation' and "
            "log a 'creative_rotation' automation run as 'AR-CR-20250814-04' with input_ref 'apparel_ctr_test'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Apparel - US"}),
            Action(name="search_ads_by_adset", kwargs={"adset_id": "102"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1103"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1104"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1103"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1104"}),

            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 30, "threshold": 10, "operator": "greater"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1103", "new_status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1104", "new_status": "active"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 678.5}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 678.5, "changed_at": "2025-08-13T01:01:01Z", "reason": "CTR-based Rotation"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-04", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "apparel_ctr_test", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="031",
        instruction=(
            "You are a Performance Marketing Analyst."
            "A check on 'Fall Fashion - Women' adset shows the video ad has an 8% lower CPA than the image ad. "
            "This improvement is below the required 10% from the 'video_cpa_advantage_pct' policy. "
            "Because the test failed to show significant improvement, the creative rotation will not proceed. "
            "Instead, you should decrease the ad set's budget by 5% as the current creatives are not meeting efficiency goals. "
            "Log the budget change with reason 'Rotation Test Failed' and "
            "log a 'creative_rotation' automation run as 'skipped' with ID 'AR-CR-20250814-05', referencing 'adset_104_cpa_underperform'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Women"}),
            Action(name="search_ads_by_adset", kwargs={"adset_id": "104"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1106"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1107"}),


            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 8, "threshold": 10, "operator": "greater"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 740.0, "percent": 5}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 703.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 703.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Rotation Test Failed"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-05", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "skipped", 
                    "input_ref": "adset_104_cpa_underperform", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="032",
        instruction=(
            "You are a Performance Marketing Analyst."
            "The paused video ad for ad set 'Electronics - US' "
            "shows a 40% CPA improvement over the active image, far exceeding the 10% policy threshold. "
            "Perform the creative rotation. "
            "Given the strong performance, increase the budget by 20%. Also, increase the 'cost_cap' bid amount for this ad set by 10% to be more competitive. "
            "Log both the budget and strategy changes separately with the reason 'High-Performance Rotation' "
            "and log the full automation as a 'creative_rotation' run with ID 'AR-CR-20250814-06' and input_ref 'high_cpa_advantage'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - US"}),
            Action(name="search_ads_by_adset", kwargs={"adset_id": "101"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1101"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1102"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1101"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1102"}),

            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 40, "threshold": 10, "operator": "greater"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1101", "new_status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1102", "new_status": "active"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 920.0, "percent": 20}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 1104.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1104.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High-Performance Rotation"}),

            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "101"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "101"}),
            Action(name="increase_value_with_percent", kwargs={"value": 32.0, "percent": 10}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "101", "new_strategy": "cost_cap", "new_bid": 35.2}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.2, "changed_at": "2025-08-13T01:01:01Z", "reason": "High-Performance Rotation"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-06", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "high_cpa_advantage", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="033",
        instruction=(
            "You are in charge of budgets. The 'Holiday Season Early Bird' campaign is being deprioritized. Decrease the budget for all its ad sets by 50%. "
            "Reinvest these savings into the 'Mobile App Installs Campaign' by increasing the budget for its ad sets by 40%. "
            "Before decreasing any budget, ensure the resulting amount is not below the 'min_budget_allocation' policy. If it is, set it to the minimum value. "
            "All final budgets must be rounded to the unit specified in 'budget_rounding_unit'. "
            "Log all changes with the reason 'App Install Push'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Holiday Season Early Bird"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "5"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 50}),
            Action(name="compare_value", kwargs={"value": 250.0, "threshold": 100, "operator": "greater_equal"}),
            Action(name="round_number_to_unit", kwargs={"number": 250.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 250.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 250.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "App Install Push"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 50}),
            Action(name="compare_value", kwargs={"value": 200.0, "threshold": 100, "operator": "greater_equal"}),
            Action(name="round_number_to_unit", kwargs={"number": 200.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 200.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 200.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "App Install Push"}),
            
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Mobile App Installs Campaign"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "7"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 40}),
            Action(name="round_number_to_unit", kwargs={"number": 1400.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 1400.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 1400.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "App Install Push"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "111"}),
            Action(name="increase_value_with_percent", kwargs={"value": 1000.0, "percent": 40}),
            Action(name="round_number_to_unit", kwargs={"number": 1400.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "111", "new_budget": 1400.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 1400.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "App Install Push"}),
        ],
        outputs=[]
    ),
     Task(
        annotator="0",
        user_id="034",
        instruction=(
            "You are a Performance Marketing Analyst. The video ad for "
            "'Back to School - Laptops' adset has a 20% better CPA than expected. "
            "You can rotate the ads by disabling the image ad and enabling the video ad. "
            "Increase the budget by 15%. However, the new bid amount must be capped. "
            "Set the new bid to be the lesser of two values: either a 15% increase on the current bid, "
            "or the value of the 'max_bid_amount' policy. "
            "Log all budget, strategy, and a 'creative_rotation' automation run "
            "with reason 'Capped Bid Rotation', input_ref 'bid_cap' and run_id 'AR-CR-20250814-11'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Laptops"}),
            Action(name="search_ads_by_adset", kwargs={"adset_id": "108"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1111"}),
            Action(name="get_status_for_ad", kwargs={"ad_id": "1112"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1111"}),
            Action(name="get_creative_type_for_ad", kwargs={"ad_id": "1112"}),


            Action(name="get_policy_param", kwargs={"param_name": "video_cpa_advantage_pct"}),
            Action(name="compare_value", kwargs={"value": 20, "threshold": 10, "operator": "greater"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1111", "new_status": "paused"}),
            Action(name="update_ad_status", kwargs={"ad_id": "1112", "new_status": "active"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 15}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 897.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 897.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Capped Bid Rotation"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "108"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 42.0, "percent": 15}), # result 48.3
            Action(name="get_policy_param", kwargs={"param_name": "max_bid_amount"}), # result 50
            Action(name="compare_value", kwargs={"value": 48.3, "threshold": 50.0, "operator": "greater"}),

            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "108", "new_strategy": "cost_cap", "new_bid": 48.3}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 48.3, "changed_at": "2025-08-13T01:01:01Z", "reason": "Capped Bid Rotation"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-CR-20250814-11", "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    'reason': 'Capped Bid Rotation',
                    "input_ref": "bid_cap", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="035",
        instruction=(
            "You are the Head of Automation. Your task is to apply the full daily strategy for the "
            "'Fall Fashion - Women' adset from 'Fall Collection Launch' campaign as specified in 'plan_2025-08-13'. "
            "You must apply the planned budget and bid strategy. "
            "To ensure a complete audit trail, you must log every change."
        ),
        actions=[
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Fall Collection Launch"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "3"}),
            Action(name="get_plans", kwargs={}),
            Action(name="get_date_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 750.0}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "cost_cap", "new_bid": 22.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 22.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="036",
        instruction=(
            "You are the Head of Automation. Your task is to apply the full daily strategy for the "
            "'Electronics - US' ad set from the 'Global Summer Sale' campaign as specified in 'plan_2025-08-13'. "
            "You must apply the planned budget, bid strategy, and bid amount. "
            "Log all changes and record the entire operation as a 'strategy_apply' automation run with ID 'AR-APPLY-202508-01'."
        ),
        actions=[
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_name_for_adset", kwargs={"adset_id": "101"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "101"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "101"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "101", "new_strategy": "cost_cap", "new_bid": 35.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0, "new_bid": 35.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
            Action(name="add_automation_run", kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "strategy_apply", "started_at": "2025-08-13T01:01:01Z", "ended_at": "2025-08-13T01:01:01Z", "status": "completed", "input_ref": "plan_2025-08-13", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="037",
        instruction=(
            "You are the Head of Automation. Apply the daily plan from 'plan_2025-08-13' to the 'Apparel - US' ad set. "
            "This plan specifies 'lowest_cost' so only the budget needs to be updated. "
            "You must verify the ad set is currently active before applying the change. "
            "Log the budget change with the plan as the reason."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Apparel - US"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}), # Verifies 102 is active
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="038",
        instruction=(
            "You are the Head of Automation. It's time to apply the older plan 'plan_2025-08-12' to the "
            "'Fall Fashion - Women' ad set as part of a rollback test. "
            "Apply the specified budget and bid strategy from this older plan. "
            "Log all changes, referencing plan name as the reason."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Women"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-12"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "104"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 740.0}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "cost_cap", "new_bid": 20.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 740.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-12"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 20.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-12"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="039",
        instruction=(
            "You are the Head of Automation. Apply the strategy for 'Back to School - Laptops' ad set"
            " from 'plan_2025-08-13'. "
            "However, there is a special directive: apply the planned budget, "
            "but increase the planned bid amount by 10% for extra competitiveness. "
            "Log both the budget and the modified strategy changes, for reason use 'plan_2025-08-13_modified'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Laptops"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "108"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 800.0}),
            Action(name="increase_value_with_percent", kwargs={"value": 45.0, "percent": 10}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "108", "new_strategy": "cost_cap", "new_bid": 49.5}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 800.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13_modified"}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 49.5, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13_modified"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="040",
        instruction=(
            "You are the Head of Automation. Apply the full 'plan_2025-08-13' to the 'Fall Fashion - Men' ad set. "
            "Before applying, check if the ad set's current daily budget and bid strategy already match the plan. "
            "If they match, do not perform an update, "
            "but log a 'strategy_apply' automation run with status 'skipped', for input_ref the plan name. "
            "If they do not match, apply and log as normal."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Men"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}), # Returns 750.0
            Action(name="get_bid_strategy_for_adset", kwargs={"adset_id": "105"}), # Returns 'lowest_cost'
            # Plan for 105 is budget 750.0 and strategy 'lowest_cost'. They match.
            Action(name="compare_value", kwargs={"value": 750.0, "threshold": 750.0, "operator": "equal"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "strategy_apply",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "skipped", 
                    "input_ref": "plan_2025-08-13", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="041",
        instruction=(
            "You are the Head of Automation. Apply the budget from 'plan_2025-08-13' to 'Holiday - Home Goods'. "
            "Do not apply the bid strategy. "
            "Before applying, you must validate that the planned budget change (from current to planned) "
            "is less than a 20% increase, as a safety check. If it exceeds 20%, fail the run. "
            "Log the budget change and a 'budget_apply' automation run using for reason and input_ref the plan name."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Home Goods"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}), # Planned budget is 500.0
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}), # Current budget is 500.0
            Action(name="calculate_spend_variance", kwargs={"planned_spend": 500.0, "actual_spend": 500.0}), # Variance is 0%
            Action(name="compare_value", kwargs={"value": 0, "threshold": 20, "operator": "less"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 500.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 500.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "budget_apply",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "reason": "plan_2025-08-13",
                    "input_ref": "plan_2025-08-13", "errors_json": "{}"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="042",
        instruction=(
            "You are the Head of Automation. Apply the budget from 'plan_2025-08-13' "
            "to ad set 'Brand - Video Ads', but pause the ad set immediately after as part of a temporary scale-back. "
            "The bid strategy should not be changed. "
            "Log the budget change and record the full operation as an 'budget_apply_and_pause' automation run, "
            "for reason and input_ref use the plan name."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Brand - Video Ads"}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "103"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "103", "new_budget": 1200.0}),
            Action(name="update_adset_status", kwargs={"adset_id": "103", "new_status": "paused"}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 1200.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "plan_2025-08-13"}),
            Action(name="add_automation_run", 
                kwargs={"run_id": "AR-APPLY-202508-01", "run_type": "budget_apply_and_pause",
                    "started_at": "2025-08-13T01:01:01Z", 
                    "ended_at": "2025-08-13T01:01:01Z", "status": "completed", 
                    "input_ref": "plan_2025-08-13", "errors_json": "{}"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="044",
        instruction=(
            "You are a Compliance Officer. A new, stricter bidding policy is being enacted. "
            "You should update the 'max_bid_amount' policy parameter to 40. "
            "Update the bid amount to the new maximum allowed value for all active adsets that use a 'cost_cap' bid strategy "
            "only ff their current bid value is greater than the new maximum. "
            "Log each change in the strategy change log with the reason 'Policy Enforcement'."
        ),
        actions=[
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="update_policy_param", kwargs={"param_name": "max_bid_amount", "param_value": "40", "updated_at": "2025-08-13T01:01:01Z"}),
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="search_adsets_by_bid_strategy", kwargs={"bid_strategy": "cost_cap"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "101"}), # 32.0 < 40 (OK)
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}), # 20.0 < 40 (OK)
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "106"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "108"}), # 42.0 > 40 (Violation)
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "111"}), # 2.5 < 40 (OK)
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "108", "new_strategy": "cost_cap", "new_bid": 40.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 40.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Policy Enforcement"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="045",
        instruction=(
            "You are a Bid Management Agent. For all active 'cost_cap' ad sets, review their ROAS for yesterday (2025-08-13). "
            "If ROAS was greater than 11.0, increase the bid amount by 5%. "
            "If ROAS was less than 9.0, decrease the bid amount by 5%. "
            "Log any adjustments in the strategy change log with the reason 'Daily Bid Optimization'."
        ),
        actions=[
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="search_adsets_by_bid_strategy", kwargs={"bid_strategy": "cost_cap"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}), # ROAS is 10.0. No action.
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}), # ROAS is 11.21 > 11.0. Increase bid.
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}), # ROAS is 11.28 > 11.0. Increase bid.
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}), # ROAS is 0.55 < 9.0. Decrease bid.
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 20.0, "percent": 5}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "cost_cap", "new_bid": 21.0}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0, "new_bid": 21.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Daily Bid Optimization"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "106"}),
            Action(name="increase_value_with_percent", kwargs={"value": 18.0, "percent": 5}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "106", "new_strategy": "cost_cap", "new_bid": 18.9}),
            Action(name="log_strategy_change", kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 18.0, "new_bid": 18.9, "changed_at": "2025-08-13T01:01:01Z", "reason": "Daily Bid Optimization"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 42.0, "percent": 5}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "108", "new_strategy": "cost_cap", "new_bid": 44.1}),
            Action(name="log_strategy_change", kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0, "new_bid": 44.1, "changed_at": "2025-08-13T01:01:01Z", "reason": "Daily Bid Optimization"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "111"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 2.5, "percent": 5}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "111", "new_strategy": "cost_cap", "new_bid": 2.375}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5, "new_bid": 2.375, "changed_at": "2025-08-13T01:01:01Z", "reason": "Daily Bid Optimization"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="047",
        instruction=(
            "You are a Finance Analyst. You must ensure all ad set budgets in the 'Global Summer Sale' campaign are synchronized with the latest plan ('plan_2025-08-13'). "
            "For each ad set in that campaign, check if its current budget matches the plan's budget. "
            "If it does not, update the ad set's budget to match the plan. "
            "Log only the budgets that were changed with reason 'Plan Synchronization'."
        ),
        actions=[
            Action(name="search_campaigns_by_name", kwargs={"name_query": "Global Summer Sale"}),
            Action(name="search_adsets_by_campaign_id", kwargs={"campaign_id": "1"}), # Returns 101, 102, 112
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Plan Synchronization"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 600.0}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Plan Synchronization"}),

            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="048",
        instruction=(
            "You are an Ad Operations Specialist."
            "Find all active ad sets with a 'cost_cap' bid strategy that do NOT belong to a 'Sales' objective campaign. "
            "For each such ad set, change its bid strategy to the 'default_bid_strategy' from policy params. "
            "Log each strategy change with the reason 'cost_cap misuse'."
        ),
        actions=[
            Action(name="get_policy_param", kwargs={"param_name": "default_bid_strategy"}), # Returns 'lowest_cost'
            Action(name="search_adsets_by_status", kwargs={"status": "active"}),
            Action(name="search_campaigns_by_objective", kwargs={"objective": "Sales"}),
            Action(name="search_adsets_by_bid_strategy", kwargs={"bid_strategy": "cost_cap"}),
           
            Action(name="get_campaign_id_for_adset", kwargs={"adset_id": "101"}), # Camp 1 -> Sales (OK)
            Action(name="get_campaign_id_for_adset", kwargs={"adset_id": "104"}), # Camp 3 -> Traffic (Violation)
            Action(name="get_campaign_id_for_adset", kwargs={"adset_id": "106"}), # Camp 5
            Action(name="get_campaign_id_for_adset", kwargs={"adset_id": "108"}), # Camp 6 -> Sales (OK)
            Action(name="get_campaign_id_for_adset", kwargs={"adset_id": "111"}), # Camp 7 -> App Installs (Violation)
            

            Action(name="get_current_timestamp", kwargs={}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "104"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "104", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 20.0, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "cost_cap misuse"}),
            Action(name="get_bid_amount_for_adset", kwargs={"adset_id": "111"}),
            Action(name="update_bid_strategy_for_adset", kwargs={"adset_id": "111", "new_strategy": "lowest_cost", "new_bid": None}),
            Action(name="log_strategy_change", kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "lowest_cost", "old_bid": 2.5, "new_bid": None, "changed_at": "2025-08-13T01:01:01Z", "reason": "cost_cap misuse"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="049",
        instruction=(
            "You are a Plan Execution Agent. Your task is to apply the budget from 'plan_2025-08-13' to the 'Electronics - US' ad set. "
            "You should calculate the percentage increase from the current budget to the planned budget. "
            "This increase must not exceed 5%. "
            "If the increase is within the limit, increase the budget and log with reason 'Budget increase'. If it exceeds the limit, do not apply the change."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": 'Electronics - US'}),
            Action(name="get_allocations_for_plan", kwargs={"plan_id": "plan_2025-08-13"}), # Plan budget for 101 is 950.0
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "101"}), # Current budget is 920.0
            Action(name="calculate_spend_variance", kwargs={"planned_spend": 920.0, "actual_spend": 950.0}), # Calculates the % increase -> 3.26%
            Action(name="compare_value", kwargs={"value": 3.260869565217391, "threshold": 5, "operator": "less_equal"}), # 3.26% <= 5% is true.
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "101", "new_budget": 950.0}),
            Action(name="log_budget_change",
                kwargs={"adset_id": "101", "new_budget": 950.0, 'old_budget': 920.0, 
                        'reason': 'Budget increase', 'changed_at': '2025-08-13T01:01:01Z'}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="111",
        instruction=(
            "You are a Growth Analyst. The 'Apparel' category showed strong interest on 2025-08-13 with over 11,000 sessions. "
            "For the 'Fall Fashion - Men' ad set, which has an efficient 7-day CPA below $9.50, increase its budget by 18%. "
            "Round the final budget according to the rounding policy and log the update with reason 'High Viewership & Efficient CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Men"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "105"}),
            Action(name="increase_value_with_percent", kwargs={"value": 750.0, "percent": 18}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 885.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "105", "new_budget": 880.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 880.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Viewership & Efficient CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="112",
        instruction=(
            "You are a Budget Analyst. Average active users for 'Toys' (Aug 7-13) were below 2,500, indicating low engagement. "
            "The 'Holiday - Toys' ad set also has a high 7-day CPA over $7.0. "
            "Due to these poor metrics, decrease the budget by 20%. "
            "Round the new budget based on the policy and log it with reason 'Low Engagement & High CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Toys"}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Toys", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "107"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 400.0, "percent": 20}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 320.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "107", "new_budget": 320.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 320.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Engagement & High CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="113",
        instruction=(
            "You are a Growth Analyst. The 'Electronics' category is booming, with average sessions over 13,000 for Aug 7-13. "
            "The 'Electronics - EU' ad set has a stellar 7-day ROAS above 12.0. "
            "Reward this performance in a key category with a 25% budget increase. "
            "You should round baed on policy and log the change with reason 'Sustained Viewership & High ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - EU"}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="increase_value_with_percent", kwargs={"value": 700.0, "percent": 25}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 875.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 880.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 880.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Sustained Viewership & High ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="114",
        instruction=(
            "You are a Budget Analyst. On 2025-08-13, viewership for the 'Home' category was below 8,500 sessions. "
            "Given this low traffic and a mediocre 7-day ROAS (below 12.5) for the 'Holiday - Home Goods' ad set, a budget cut of 15% is required. "
            "Round the new budget based on policy and log the change with reason 'Low Traffic & Mediocre ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Holiday - Home Goods"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Home"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "106"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 500.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 425.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "106", "new_budget": 420.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 420.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Low Traffic & Mediocre ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="115",
        instruction=(
            "You are a Growth Analyst. The 'Back to School - Laptops' ad set has an excellent 7-day CPA below $9.0. "
            "Additionally, the average number of active users for 'Electronics' (Aug 7-13) was strong. "
            "This combination of efficiency and a large audience justifies a 20% budget increase. "
            "You should round based on policy and log the update with reason 'Efficient CPA & Strong User Base'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Back to School - Laptops"}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "108"}),
            Action(name="increase_value_with_percent", kwargs={"value": 780.0, "percent": 20}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 936.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "108", "new_budget": 940.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 940.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Efficient CPA & Strong User Base"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="116",
        instruction=(
            "You are a Budget Analyst. Despite high viewership on 2025-08-13 (over 11,000 sessions), the 'Apparel - US' ad set has a low 7-day ROAS (below 14.0). "
            "This inefficiency warrants a 10% budget decrease to reallocate funds. "
            "You should round the new budget according to policy and log the change with reason 'Inefficient ROAS in High Traffic Category'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Apparel - US"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 590.0, "percent": 10}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 531.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 530.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 530.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Inefficient ROAS in High Traffic Category"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="117",
        instruction=(
            "You are a Growth Analyst. The average active users for the 'Apparel' category (Aug 7-13) is strong. "
            "The 'Fall Fashion - Women' ad set has a solid 7-day ROAS over 11.0. "
            "This combination justifies a 12% budget increase to capture more market share. "
            "You should round the new budget based on policy and log the change with reason 'High User Base & Solid ROAS'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Fall Fashion - Women"}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Apparel", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "104"}),
            Action(name="increase_value_with_percent", kwargs={"value": 740.0, "percent": 12}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 828.8, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "104", "new_budget": 830.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 830.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High User Base & Solid ROAS"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="118",
        instruction=(
            "You are a Budget Analyst. On 2025-08-13, viewership for the 'Electronics' category was strong, "
            "but the 'Electronics - EU' ad set has a high 7-day CPA over $7.8. "
            "To improve efficiency, decrease the budget for this ad set by 10%. "
            "You should round the new budget according to policy and log the change with reason 'High Viewership & High CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Electronics - EU"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Electronics"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "112"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 700.0, "percent": 10}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 630.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "112", "new_budget": 630.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 630.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Viewership & High CPA"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="119",
        instruction=(
            "You are a Growth Analyst. The 'App Installs - Android' ad set has a low 7-day ROAS. "
            "Average active users for the 'Mobile' category (Aug 7-13) is also below 8,500. "
            "This combination of poor performance and middling engagement warrants a 25% budget cut. "
            "You should round the new budget based on policy and log it with the reason 'Poor ROAS & Low Engagement'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "App Installs - Android"}),
            Action(name="get_average_viewership_for_category_in_period", kwargs={"category": "Mobile", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_period", kwargs={"adset_id": "110", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "110"}),
            Action(name="decrease_value_with_percent", kwargs={"value": 1000.0, "percent": 25}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 750.0, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "110", "new_budget": 750.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 750.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "Poor ROAS & Low Engagement"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="120",
        instruction=(
            "You are a Budget Analyst. On 2025-08-13, the 'Apparel' category had over 11,500 sessions. "
            "The 'Apparel - US' ad set has a highly efficient 7-day CPA under $7.9. "
            "These positive signals justify a 15% budget increase. "
            "You should round the budget based on policy and log the change with reason 'High Sessions & Efficient CPA'."
        ),
        actions=[
            Action(name="search_adsets_by_name", kwargs={"name_query": "Apparel - US"}),
            Action(name="get_viewership_for_date_and_category", kwargs={"date": "2025-08-13", "category": "Apparel"}),
            Action(name="calculate_adset_cpa_for_period", kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_budget_for_adset", kwargs={"adset_id": "102"}),
            Action(name="increase_value_with_percent", kwargs={"value": 590.0, "percent": 15}),
            Action(name="get_policy_param", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="round_number_to_unit", kwargs={"number": 678.5, "unit": 10}),
            Action(name="update_daily_budget_for_adset", kwargs={"adset_id": "102", "new_budget": 680.0}),
            Action(name="get_current_timestamp", kwargs={}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 680.0, "changed_at": "2025-08-13T01:01:01Z", "reason": "High Sessions & Efficient CPA"}),
        ],
        outputs=[]
    )

]

