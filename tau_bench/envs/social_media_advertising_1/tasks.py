
tasks = [
    {
        "annotator": 0,
        "user_id": "066",
        "instruction": "As a Trend Analyst, evaluate the 'Electronics' viewership sessions on 2025-08-07 in comparison to 2025-08-10. Should the growth across these 3 days exceed 10%, it indicates strong momentum. Consequently, suspend the lower-priority 'Electronics - UK' ad set (ID 112) to concentrate on other electronics ad sets if it is currently active. Additionally, log a 'trend_analysis' automation run with input_ref specified as 'electronics_momentum'. Furthermore, the 'App Installs - Android' ad set lacks a defined bid amount. To better manage the cost per install, adjust its strategy to 'cost_cap' and set a precise bid of $2.0. Record the strategy change with the reason noted as 'Set CPI Target'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-07",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-10",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 13500,
                    "previous_value": 12000
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 12.5,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "112",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "trend_analysis",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "electronics_momentum",
                    "errors_json": "{}"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_strategy": "cost_cap",
                    "new_bid": 2.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "110",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 2.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Set CPI Target"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "067",
        "instruction": "As a Trend Analyst, review the 'Apparel' viewership sessions on 2025-08-12 against 2025-08-13. If the growth over this day is less than 2%, it suggests a weak trend. Consequently, proactively pause the 'Apparel - CA' ad set (ID 102) to save budget, only if it is currently active. Additionally, log a 'trend_pause' automation run with input_ref specified as 'apparel_weak_growth'. Moreover, the 'App Installs - iOS' ad set operates on 'cost_cap', but the team is interested in testing the platform's algorithm. Modify the strategy to 'lowest_cost' to evaluate if it enhances performance. The bid amount should be set to null. Record the change for the A/B test with the reason stated as 'A/B Test: Algorithmic Bid'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-12",
                    "category": "Apparel"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 12000,
                    "previous_value": 11800
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 1.694915254237288,
                    "threshold": 2,
                    "operator": "less"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "102",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "apparel_weak_growth",
                    "errors_json": "{}"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "111",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 2.5,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "A/B Test: Algorithmic Bid"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "068",
        "instruction": "As a Trend Analyst, handle the comparison of 'Electronics' viewership sessions from 2025-08-10 to 2025-08-13. Should growth across these three days fall below 12%, it suggests a deceleration, and you must pause the 'Back to School - Laptops' ad set to conserve budget. Additionally, record a 'trend_pause' automation run with input_ref set to 'electronics_slowing'. Moreover, for the 'Fall Fashion - Men' ad set within a 'Traffic' campaign, since its 'lowest_cost' strategy is failing to generate sufficient volume, transition its strategy to 'cost_cap' with an ample bid of $28.0 to enhance competitiveness in the auction. Document the strategy modification citing 'Increase competitiveness' as the reason.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-10",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 15000,
                    "previous_value": 13500
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 11.11111111111111,
                    "threshold": 12,
                    "operator": "less"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "108",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "electronics_slowing",
                    "errors_json": "{}"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_strategy": "cost_cap",
                    "new_bid": 28.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "105",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 28.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Increase competitiveness"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "069",
        "instruction": "As a Trend Analyst, examine the 'Electronics' viewership sessions from 2025-08-07 and evaluate them against those on 2025-08-13. If growth across these six days surpasses 30%, the trend is deemed to be diminished. Consequently, pause the 'Electronics - CA' ad set to prevent ad fatigue, ensuring it is currently active. Log a 'trend_analysis' automation run with input_ref 'electronics_exhaustion_check'. If no action is necessary, record the status as 'skipped'. Furthermore, the 'Brand - Video Ads' ad set pertains to an 'Awareness' campaign. Although its present 'lowest_cost' strategy is appropriate, reset any residual bid data by reapplying the 'lowest_cost' strategy, explicitly setting the bid amount to null. Document this as a strategy reset, specifying 'Strategy Reset' as the reason.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - US"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-07",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 15000,
                    "previous_value": 12000
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 25,
                    "threshold": 30,
                    "operator": "greater"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "trend_analysis",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "skipped",
                    "input_ref": "electronics_exhaustion_check",
                    "errors_json": "{}"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Brand - Video Ads"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "103",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "103",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "lowest_cost",
                    "old_bid": null,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strategy Reset"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "074",
        "instruction": "Your role is a Bid Optimizer. Prepare the 'Fall Fashion - Men' ad set for a new creative test by adjusting its strategy to 'cost_cap' with a bid of $23.0. Then, pause the ad set until the new creatives are ready. Document the strategy adjustment with the reason 'Prep for Creative Test'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_strategy": "cost_cap",
                    "new_bid": 23.0
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "105",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "105",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 23.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Prep for Creative Test"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "076",
        "instruction": "As a Bid Optimizer, you need to ensure the bid for the 'Electronics - CA' ad set matches the latest plan. Locate the bid amount in 'plan_2025-08-12' and implement it. Maintain the strategy as 'cost_cap'. Record the update with the reason 'Realign to Plan 2025-08-12'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - US"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-12"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_strategy": "cost_cap",
                    "new_bid": 32.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "101",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 32.0,
                    "new_bid": 32.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Realign to Plan 2025-08-12"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "082",
        "instruction": "You are a Bid Optimizer. To get ready for an upcoming A/B test, adjust the strategy of the 'Brand - Video Ads' ad set to 'bid_cap' with the specified value of $0.50. Next, make sure the ad set remains active for the test to proceed. Record the change in strategy with the reason 'A/B Test Preparation'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Brand - Video Ads"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "103",
                    "new_strategy": "bid_cap",
                    "new_bid": 0.5
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "103",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "bid_cap",
                    "old_bid": null,
                    "new_bid": 0.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "A/B Test Preparation"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "085",
        "instruction": "You are a Bid Optimizer. The 'Fall Fashion - Women' ad set requires its bid to be adjusted in accordance with the 'plan_2025-08-13'. Locate the bid amount for this ad set in the plan and implement it, ensuring the strategy remains 'cost_cap'. Document the strategy change with the reason 'Plan Alignment'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "cost_cap",
                    "new_bid": 22.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 20.0,
                    "new_bid": 22.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Plan Alignment"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "086",
        "instruction": "You are a Bid Optimizer. Handle the reset of the bid strategy for 'Apparel - CA' ad set. Modify its strategy to 'cost_cap' but adjust the bid amount to $0 to effectively suspend bidding without stopping the ad set. Record this as a strategy change with reason 'bidding_pause'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - US"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_strategy": "cost_cap",
                    "new_bid": 0.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "102",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 0.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "bidding_pause"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "002",
        "instruction": "You are a Performance Marketing Analyst. Implement the minimum ROAS threshold of 1.5 to all active ad sets. For the period data from 2025-08-07 to 2025-08-13, stop any ad set with ROAS below 1.5, and for those with ROAS above 13, enhance their budget by 10%. Log any budget modification with reason 'ROAS update'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0,
                    "old_budget": 590.0,
                    "reason": "ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "003",
        "instruction": "As a Performance Marketing Analyst, ensure that the minimum ROAS threshold of 1.5 is applied to all active ad sets. When reviewing data from the period 2025-08-07 to 2025-08-13, halt any ad set with ROAS under 1.5. Ad sets with ROAS over 13 should have their budget increased by 10%. For ad sets titled 'App Installs - Android' and 'App Installs - iOS', enforce a special rule: boost the budget by 15% if the CPA is below $6. Log any budget modifications with the reason 'ROAS update'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1150.0
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1150.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0,
                    "old_budget": 590.0,
                    "reason": "ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1150.0,
                    "old_budget": 1000.0,
                    "reason": "ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1150.0,
                    "old_budget": 1000.0,
                    "reason": "ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "004",
        "instruction": "In your capacity as a Performance Marketing Analyst, apply a minimum ROAS threshold of 1.5 to all active ad sets. For the data spanning 2025-08-07 to 2025-08-13, any ad set with a ROAS below 1.5 should be paused. Increase the budget by 10% for ad sets with ROAS exceeding 13. Implement a special rule for ad sets from the 'Mobile App Installs Campaign': increase the budget by 15% if the CPA falls below $16. Record any changes to the budget with the reason 'ROAS/CPA update'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "7"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1150.0
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1150.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0,
                    "old_budget": 590.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1150.0,
                    "old_budget": 1000.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1150.0,
                    "old_budget": 1000.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "005",
        "instruction": "You are a Performance Marketing Analyst. Handle the application of the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. For data within the period 2025-08-07 to 2025-08-13, suspend any ad set where the ROAS falls below the policy value of 'min_roas_threshold_7d', and if an ad set's ROAS exceeds 13, augment their budget by 10%. For ad sets within the campaign 'Mobile App Installs Campaign', implement a special rule (taking higher priority): if CPA is under $7, amplify the budget by 15%. Ensure you log any budget modification with the reason 'ROAS/CPA update'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "7"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1150.0
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1150.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0,
                    "old_budget": 590.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1150.0,
                    "old_budget": 1000.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1150.0,
                    "old_budget": 1000.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "006",
        "instruction": "You are a Performance Marketing Analyst. Coordinate the application of the minimum ROAS threshold from 'min_roas_threshold_7d' policy name. For the period from 2025-08-07 to 2025-08-13, halt any ad set with ROAS below the policy value of 'min_roas_threshold_7d', and for ad sets with a ROAS greater than 12, escalate their budgets by 20%. For ad sets in the campaign 'Fall Collection Launch', apply a priority rule: if CPA is higher than $9, boost the budget by 15%. Ensure logging of any budget alterations with the reason 'ROAS/CPA update'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 862.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0,
                    "old_budget": 590.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 862.5,
                    "old_budget": 750.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0,
                    "old_budget": 400.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0,
                    "old_budget": 700.0,
                    "reason": "ROAS/CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "007",
        "instruction": "As a Performance Marketing Analyst, implement the 'min_roas_threshold_7d' policy by applying its minimum ROAS threshold. For data ranging from 2025-08-07 to 2025-08-13, suspend any ad set with ROAS less than the 'min_roas_threshold_7d' policy value, and for ad sets with ROAS over 12, boost their budget by 20%. For ad sets within the 'Fall Collection Launch' campaign, enforce a specific rule (this rule overrides others): if CPA is below $10, increase the budget by 15%.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 15
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 851.0
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 862.5
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "008",
        "instruction": "Acting as a Performance Marketing Analyst, enforce the 'min_roas_threshold_7d' policy name by utilizing its minimum ROAS threshold. For the period from 2025-08-07 to 2025-08-13, halt any ad set that has ROAS under the 'min_roas_threshold_7d' policy value, and for those ad sets with ROAS exceeding 12, raise their budget by 20%. For ad sets associated with the 'Fall Collection Launch' campaign, apply an alternative rule (this rule takes priority): if CPA is below $9, increase the budget by 15%.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 851.0
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "009",
        "instruction": "You are a Performance Marketing Analyst. Utilize the minimum ROAS threshold as outlined in 'min_roas_threshold_7d' policy name. During the period from 2025-08-07 to 2025-08-13, suspend any ad set having ROAS less than the policy value of 'min_roas_threshold_7d'. Moreover, for ad sets with ROAS exceeding 12, amplify their budget by 20%. In the case of ad sets related to the campaign 'Holiday Season Early Bird', apply a special rule (which takes precedence): if CPA falls below $10, augment budget by 20%.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Holiday Season Early Bird"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "010",
        "instruction": "You are a Performance Marketing Analyst. Implement the minimum ROAS threshold from the 'min_roas_threshold_7d' policy name. For the timeframe between 2025-08-07 and 2025-08-13, halt any ad set with ROAS under the policy value of 'min_roas_threshold_7d'. Additionally, for ad sets with ROAS higher than 11.5, elevate their budget by 20%. Regarding ad sets containing the 'Holiday' substring in their name, execute a special rule (which takes precedence): if CPA is under $10, boost the budget by 20%. Record any budget alteration with the reason 'CPA/ROAS update'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0,
                    "old_budget": 590.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0,
                    "old_budget": 700.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0,
                    "old_budget": 500.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0,
                    "old_budget": 400.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "011",
        "instruction": "As a Performance Marketing Analyst, for the timeframe 2025-08-07 to 2025-08-13, handle any active ad set with ROAS under the 'min_roas_threshold_7d' policy by pausing them, and for those active ad sets with ROAS greater than 12.5, coordinate to increase their budget by 20%. For ad sets that include 'Holiday' in their name, apply a prioritized rule: if CPA is below $20, increase the budget by 20%. Ensure to log any budget alterations indicating 'CPA/ROAS update' as the reason.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0,
                    "old_budget": 590.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0,
                    "old_budget": 700.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0,
                    "old_budget": 500.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0,
                    "old_budget": 400.0,
                    "reason": "CPA/ROAS update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "012",
        "instruction": "As a Performance Marketing Analyst, for the period from 2025-08-07 to 2025-08-13, pause any ad sets where the CPA falls below $10, and for those ad sets with a CPA of $10 or more, coordinate an increase of their budget by 10%. Ad sets with 'Holiday' in their name should follow a special rule: if their CPA is below $20, enhance the budget by 20%. Make sure to log every budget adjustment citing 'CPA update' as the reason.",
        "actions": [
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "102",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "104",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "105",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "108",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "111",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "112",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1012.0
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1012.0,
                    "old_budget": 920.0,
                    "reason": "CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 600.0,
                    "old_budget": 500.0,
                    "reason": "CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 480.0,
                    "old_budget": 400.0,
                    "reason": "CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "015",
        "instruction": "You are a Performance Marketing Analyst. A performance report reveals that within the 'Fall Fashion - Women' ad set (ID 104), the inactive video ad (ID 1107) has a 12% lower CPA compared to the active image ad (ID 1106). As this surpasses the 'video_cpa_advantage_pct' policy limit (currently 10%), handle a creative rotation. Pause ad 1106 and activate ad 1107. To support the newly activated creative, augment the ad set's budget by 5%. Document the budget adjustment with the reason 'Creative Rotation Support' and log the entire process as a 'creative_rotation' automation run with ID 'AR-CR-20250814-01' using input_ref adset_104_cpa_policy.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 12,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1106"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1107"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1106",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1107",
                    "new_status": "active"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 777.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 777.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Creative Rotation Support"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-01",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "adset_104_cpa_policy",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "050",
        "instruction": "You are a Performance Auditor. Our policy mandates a minimum 7-day ROAS, specified by 'min_roas_threshold_7d', for all ad sets employing the 'lowest_cost' bid strategy. The evaluated period is 2025-08-07 to 2025-08-13. If the ROAS falls below the policy criteria, pause the ad set. For logging purposes, record a 'roas_policy_enforcement' automation run with input_ref 'policy_min_roas_threshold_7d'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_roas_threshold_7d"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "SearchAdsetsByBidStrategy",
                "arguments": {
                    "bid_strategy": "lowest_cost"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "103",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "110",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "roas_policy_enforcement",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "policy_min_roas_threshold_7d",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "051",
        "instruction": "As an Audience Growth Analyst, assess the viewership of the 'Electronics' category on 2025-08-13. Should today's sessions surpass the 7-day average for the period from 2025-08-07 to 2025-08-13 by over 10%, increase the budget for the 'Electronics - CA' ad set by 15% to take advantage of the increase. Record the update with the reason 'Surge in User Interest'. Additionally, the 'App Installs - iOS' ad set currently operates on 'cost_cap', but the team is interested in testing the platform's algorithm. Adjust the strategy to 'lowest_cost' to determine if performance improves. The bid amount should remain null. Document this adjustment for the A/B test with the reason 'A/B Test: Algorithmic Bid'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 15000.0,
                    "previous_value": 13500.0
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 11.11111111111111,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - CA"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1058.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1058.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Surge in User Interest"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "111",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 2.5,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "A/B Test: Algorithmic Bid"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "052",
        "instruction": "As a Budget Efficiency Agent, evaluate the viewership of the 'Office' category on 2025-08-13. If 'active_users' exceed 100, identify all paused ad sets in this category. For each identified ad set, verify the absence of budget allocation in 'plan_2025-08-13'. If absent, activate the ad set to evaluate its current performance. Also, log a 'low_viewership_test' automation run, ensuring the input_ref is set to the plan name.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Office"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 1000,
                    "threshold": 100,
                    "operator": "greater"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "SearchAdsetsByCategory",
                "arguments": {
                    "category": "Office"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "109",
                    "new_status": "active"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "low_viewership_test",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "plan_2025-08-13",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "053",
        "instruction": "As a Strategy Analyst, your task is to evaluate weekly sales units for the 'Toys' category from Aug 7-13 and compare them with the daily active users on Aug 13. If the weekly sales units are fewer than the daily active users, a conversion issue is present. In this case, adjust the bid strategy for the 'Holiday - Toys' ad set from 'lowest_cost' to 'cost_cap', setting a bid of $15.0 to target users with higher purchase intent. Record the strategy modification citing 'Low sold units per active users' as the reason. Additionally, register a 'viewership_to_sales_check' automation execution with input_ref assigned to 'adset'.",
        "actions": [
            {
                "name": "GetSalesForCategoryInPeriod",
                "arguments": {
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13",
                    "category": "Toys"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Toys"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 300,
                    "threshold": 2000,
                    "operator": "less"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_strategy": "cost_cap",
                    "new_bid": 15.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "107",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 15.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low sold units per active users"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "viewership_to_sales_check",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "adset",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "054",
        "instruction": "Take on the role of a Trend Analyst. Scrutinize the 'Electronics' viewership sessions from 2025-08-08 to 2025-08-11. Should the growth across these three days be under 15%, you are to pause the 'Electronics - UK' ad set, provided it is presently active, to save budget. Furthermore, log a 'trend_pause' automation execution with input_ref marked as 'trend'. Additionally, the 'Fall Fashion - Women' ad set bid is not performing well. Verify whether its current bid is below $22.0. If affirmative, switch its strategy from 'cost_cap' to 'lowest_cost' to enable the algorithm to identify a new cost baseline. Document the modification with 'Performance Reset to Baseline' as the rationale.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-08",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-11",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 14000,
                    "previous_value": 12500
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 12,
                    "threshold": 15,
                    "operator": "less"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - EU"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "112",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "trend",
                    "errors_json": "{}"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 20.0,
                    "threshold": 22.0,
                    "operator": "less"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 20.0,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Performance Reset to Baseline"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "055",
        "instruction": "As a Budget Strategist, handle the following tasks: On 2025-08-13, the 'Mobile' category experienced a session count exceeding that of the 'Home' category by more than double. Therefore, adjust the budget by reducing the 'Holiday - Home Goods' ad set by 20% and increasing the 'App Installs - Android' ad set by 20%. Record both adjustments citing the reason 'Viewership-Based Reallocation'. Additionally, the 'Back to School - Stationery' ad set is paused currently. Prepare to reactivate it by modifying its strategy from 'lowest_cost' to 'cost_cap' with an initial bid amount of $5.0. Once the strategy is established, activate the ad set. Document the change with the reason 'Reactivation with CPA Target'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Home"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 400.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 400.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Viewership-Based Reallocation"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1200.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 1200.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Viewership-Based Reallocation"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Stationery"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "109",
                    "new_strategy": "cost_cap",
                    "new_bid": 5.0
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "109",
                    "new_status": "active"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "109",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 5.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Reactivation with CPA Target"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "056",
        "instruction": "With the role of a Budget Strategist, coordinate the following actions: On 2025-08-13, the 'Electronics' category surpassed the 'Apparel' category in user sessions. Consequently, adjust financial allocations by reducing the 'Apparel - CA' ad set's budget by 15% and increasing the 'Electronics - UK' ad set's budget by 15%. Log these modifications under the reason 'Electronics Viewership Lead'. Moreover, the 'Electronics - CA' ad set (ID 101) has demonstrated a consistently high ROAS. To sustain profitability and encourage scaling, change its bid strategy from 'cost_cap' to 'lowest_cost' to test if the algorithm can effectively identify additional conversions. Note this adjustment with the reason 'High ROAS test'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - UK"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 501.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 501.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Electronics Viewership Lead"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 805.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 805.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Electronics Viewership Lead"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "101",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 32.0,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High ROAS test"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "057",
        "instruction": "As a Budget Strategist, on 2025-08-13, it was observed that the 'Apparel' category experienced over 1.4 times the user sessions compared to the 'Home' category. To capitalize on this trend, reduce the allocation for the 'Holiday - Home Goods' ad set by 10% and enhance the funding for the 'Fall Fashion - Women' ad set by 10%. Document both adjustments with the reason 'Apparel Engagement Focus'. In addition, the 'Electronics - UK' ad set (ID 112) belongs to a 'Sales' campaign and requires a specific cost target. Adjust its strategy from 'lowest_cost' to 'cost_cap' and set the bid value to $30.0. Record the modification as a policy compliance action with the reason 'Policy Compliance: Sales CPA'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Home"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 450.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 450.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Apparel Engagement Focus"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 814.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 814.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Apparel Engagement Focus"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_strategy": "cost_cap",
                    "new_bid": 30.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "112",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 30.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Policy Compliance: Sales CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "058",
        "instruction": "In your role as a Budget Strategist, on 2025-08-13, the 'Mobile' category recorded sessions more than three times those of the 'Toys' category. To respond to this, decrease emphasis on Toys by cutting the 'Holiday - Toys' ad set budget by 25%, and redirect that amount to Mobile by raising the 'App Installs - iOS' ad set budget by 25%. Record both modifications with the reason 'Mobile Dominance Shift'. Additionally, the 'Holiday - Home Goods' ad set (ID 106) is presently set on 'cost_cap' but the imminent holiday sale demands maximizing reach. Modify the bid strategy to 'lowest_cost' to provide the ad platform with more adaptability. Document the change with the reason 'Maximize holiday reach'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Toys"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 300.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 300.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mobile Dominance Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1250.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 1250.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mobile Dominance Shift"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "106",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 18.0,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Maximize holiday reach"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "059",
        "instruction": "As a Budget Strategist, note that on 2025-08-13, the 'Electronics' viewership exceeded 'Home' by over 1.8 times. Reallocate by reducing the 'Holiday - Home Goods' ad set budget by 5% and enhancing the 'Back to School - Laptops' budget by 5%. Record both adjustments with the rationale 'Tech Trend Reallocation'. Additionally, the 'App Installs - Android' ad set lacks a defined bid amount. To manage the cost per install effectively, change its strategy to 'cost_cap' and assign a specific bid of $2.0. Document the update with the reason 'Set CPI Target'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Home"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 475.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 475.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Tech Trend Reallocation"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 819.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 819.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Tech Trend Reallocation"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_strategy": "cost_cap",
                    "new_bid": 2.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "110",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 2.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Set CPI Target"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "060",
        "instruction": "As a Budget Strategist, acknowledge that on 2025-08-13, the 'Apparel' category had exactly twice the user sessions compared to the 'Toys' category, signifying a clear focus. Reduce the 'Holiday - Toys' ad set budget by 12% and augment the 'Fall Fashion - Men' ad set budget by 12%. Record both modifications with the justification 'Fashion Season Push'. Furthermore, the 'Electronics - UK' ad set currently employs 'lowest_cost'. To synchronize with the CA strategy, identify the bid amount of the 'Electronics - CA' ad set and apply it to the UK ad set, switching its strategy to 'cost_cap' as well. Document the change with the reason 'Align UK with CA Bid Policy'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Toys"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 12
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 352.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 352.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Fashion Season Push"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 12
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 840.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 840.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Fashion Season Push"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - CA"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - UK"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_strategy": "cost_cap",
                    "new_bid": 32.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "112",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 32.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Align UK with CA Bid Policy"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "061",
        "instruction": "You are a Budget Strategist. On 2025-08-13, the 'Mobile' category experienced over 1.25 times the sessions compared to the 'Electronics' category. Adjust budgets to the more successful category by reducing 'Electronics - UK' by 18% and boosting 'App Installs - Android' by 18%. Document both modifications with the reason 'Mobile Growth Investment'. Also, on 2025-08-13, the 'Apparel' category received more sessions than the 'Home' category. Regarding the 'Apparel - CA' ad set, its 7-day CPA remains efficient below $8.0. Considering these two favorable indicators, you should enhance its budget by 10%. Round the budget and note the change with reason 'Positive Viewership & CPA'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - UK"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 18
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 574.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 574.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mobile Growth Investment"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 18
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1180.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 1180.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mobile Growth Investment"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - US"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Home"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 649.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 650.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 650.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Positive Viewership & CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "062",
        "instruction": "You are a Budget Strategist. On 2025-08-13, the 'Electronics' category had more than double the user sessions compared to the 'Toys' category. Redistribute funds by cutting the 'Holiday - Toys' ad set budget by 10% and increasing the 'Electronics - CA' ad set budget by 10%. Record both adjustments with the reason 'High Engagement Reinvestment'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Toys"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - CA"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 360.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 360.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Engagement Reinvestment"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1012.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1012.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Engagement Reinvestment"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "063",
        "instruction": "You are a Budget Strategist. On 2025-08-13, the 'Apparel' division experienced fourfold the sessions compared to the 'Office' division. Transfer budget from the underperforming area by reducing the 'Back to School - Stationery' ad set budget by 20%. Amplify the 'Apparel - CA' ad set by 20%. Record both modifications with the justification 'Low Engagement De-Funding'. Additionally, the existing bid of $42.0 for 'Back to School - Laptops' is excessively high. Decrease the bid by 10% to enhance efficiency, adhering to the 'cost_cap' strategy. Log the adjustment under 'Efficiency Bid Reduction'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Office"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Stationery"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 300.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "109",
                    "new_budget": 240.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "109",
                    "old_budget": 300.0,
                    "new_budget": 240.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Engagement De-Funding"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 708.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Engagement De-Funding"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 42.0,
                    "percent": 10
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_strategy": "cost_cap",
                    "new_bid": 37.8
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "108",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 42.0,
                    "new_bid": 37.8,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Efficiency Bid Reduction"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "064",
        "instruction": "You are a Budget Strategist. On 2025-08-13, the 'Mobile' sector registered over 1.5 times the user sessions as the 'Apparel' sector. To support the leading sector, lessen the budget of the 'Fall Fashion - Women' ad set by 22% and augment the budget of the 'App Installs - iOS' ad set by 22%. Document both modifications with the explanation 'Top Performing Category Boost'. Moreover, the 'Holiday - Toys' ad set (ID 107) must be ready for an upcoming strategy that will implement 'cost_cap'. Proactively convert its strategy from 'lowest_cost' to 'cost_cap' with an initial bid of $12.0. Record this preparatory adjustment with the reason 'Prepare for new plan'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 22
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 577.2
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 577.2,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Top Performing Category Boost"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 22
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1220.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 1220.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Top Performing Category Boost"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_strategy": "cost_cap",
                    "new_bid": 12.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "107",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 12.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Prepare for new plan"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "065",
        "instruction": "As a Budget Strategist, note that on 2025-08-12, the 'Electronics' category experienced more user sessions compared to the 'Apparel' category. Considering this trend, reduce the budget for the 'Fall Fashion - Men' ad set by 10% and increase the budget for the 'Electronics - CA' ad set by the same percentage. Record both modifications with the reason 'Viewership Trend Adjustment'. Additionally, review the ad set 'Back to School - Laptops'; its strategy is overly aggressive with a bid exceeding $40. Verify if the bid surpasses this threshold and, if confirmed, modify the strategy to 'lowest_cost' for more economical conversions. Document the change with reason 'Cost Reduction Revert'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-12",
                    "category": "Apparel"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-12",
                    "category": "Electronics"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - CA"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 675.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 675.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Viewership Trend Adjustment"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1012.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1012.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Viewership Trend Adjustment"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 42.0,
                    "threshold": 40.0,
                    "operator": "greater"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "108",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 42.0,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Cost Reduction Revert"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "070",
        "instruction": "Act as a Trend Analyst by evaluating the 'Electronics' viewership sessions on 2025-08-09 and comparing them to 2025-08-10. Should the growth for this period fall below 5%, it indicates a slowdown. Consequently, if active, temporarily pause the 'Electronics - CA' ad set (ID 101) to save budget. Also, document a 'trend_pause' automation execution with input_ref labeled 'electronics_stall'. Furthermore, Management has sanctioned a more aggressive approach for the 'Fall Fashion - Women' ad set. Increase its current 'cost_cap' bid from $20.0 to $24.0, ensuring the strategy type remains unchanged. Record this manual bid adjustment with reason 'Manual Bid Increase'.",
        "actions": [
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-09",
                    "category": "Electronics"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-10",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculatePercentageChange",
                "arguments": {
                    "current_value": 13500,
                    "previous_value": 13000
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 3.8461538461538463,
                    "threshold": 5,
                    "operator": "less"
                },
            },
            {
                "name": "GetStatusForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "101",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "trend_pause",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "electronics_stall",
                    "errors_json": "{}"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "cost_cap",
                    "new_bid": 24.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 20.0,
                    "new_bid": 24.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Manual Bid Increase"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "071",
        "instruction": "Act as a Bid Optimizer. The 'App Installs - Android' ad set currently has no defined bid. In order to better manage the cost per install, adjust its strategy to 'cost_cap' and assign a precise bid of $2.0. Record the update with the reason 'Set CPI Target'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_strategy": "cost_cap",
                    "new_bid": 2.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "110",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 2.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Set CPI Target"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "072",
        "instruction": "Function as a Bid Optimizer. The 'Electronics - UK' ad set belongs to a 'Sales' campaign and requires a specified cost target. Alter its strategy from 'lowest_cost' to 'cost_cap' and determine the bid amount as $30.0. Document the modification for policy compliance, citing reason 'Policy Compliance: Sales CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - EU"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_strategy": "cost_cap",
                    "new_bid": 30.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "112",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 30.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Policy Compliance: Sales CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "073",
        "instruction": "As a Bid Optimizer, handle the 'Fall Collection Launch' campaign by ensuring that all ad sets utilize 'cost_cap' to manage spending during the launch. Locate the ad set 'Fall Fashion - Men' and switch its strategy from 'lowest_cost' to 'cost_cap', starting with a bid of $21.50. Document the adjustment, citing 'Launch Cost Control' as the reason. Additionally, the current bid for the 'Holiday - Home Goods' ad set is overly cautious. Enhance the existing 'cost_cap' bid amount by 25% to engage more with the holiday audience, maintaining the same strategy type. Record the bid enhancement as a strategic update, with the reason being 'Aggressive Bid Increase'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetCampaignIdForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetNameForCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_strategy": "cost_cap",
                    "new_bid": 21.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "105",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 21.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Launch Cost Control"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 18.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_strategy": "cost_cap",
                    "new_bid": 22.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "106",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 18.0,
                    "new_bid": 22.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Aggressive Bid Increase"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "090",
        "instruction": "As a Growth Analyst, take advantage of the 'Electronics' category, which had over 14,000 sessions on 2025-08-13, showing significant interest. Boost the budget for the 'Electronics - CA' ad set by 15% if its 7-day ROAS (Aug 7-13) exceeds 9.0. Ensure the final budget is adjusted to match the policy unit. Note the change with the reason 'High Viewership & ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - US"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1058.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1060.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1060.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Viewership & ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "092",
        "instruction": "Your role is Growth Analyst. During August 7-13, the 'Apparel' category saw average daily sessions surpassing 1,500. This consistent engagement justifies a budget increment. For the 'Fall Fashion - Women' ad set, where the 7-day CPA is less than $9.0, adjust its budget upwards by 20%. Ensure to round the final figure in accordance with policy and document the revision with the reason 'Sustained Viewership & Low CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Apparel",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 20
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 888.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 890.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 890.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Sustained Viewership & Low CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "093",
        "instruction": "As a Budget Analyst, note that the 'Home' category had average active users below 3,000 between Aug 7-13. This low level of engagement, coupled with a high 7-day CPA (more than $8.0) for the 'Holiday - Home Goods' ad set, necessitates a budget reduction of 30%. Round the adjusted budget and record the modification with the reason 'Low Engagement & High CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Home",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 30
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 350.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 350.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 350.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Engagement & High CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "094",
        "instruction": "As a Growth Analyst, you should note that the 'Mobile' category had upwards of 15,000 sessions on 2025-08-13. This substantial traffic is an asset. For the 'App Installs - iOS' ad set, which maintains a 7-day CPA below $5.0, boost the budget by an impactful 40%. Ensure the final budget is rounded in line with policy, and record the update citing 'High Traffic & Efficient CPA' as the reason. Additionally, the 'Apparel - CA' ad set currently uses a 'lowest_cost' strategy, but requires stricter cost management. Alter its bid strategy to 'cost_cap' and assign a starting bid amount of $25.0 to establish a CPA target. Document this as a strategy adjustment with the reason 'Enforce CPA Target'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 40
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1400.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1400.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 1400.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Traffic & Efficient CPA"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - US"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_strategy": "cost_cap",
                    "new_bid": 25.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "102",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 25.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Enforce CPA Target"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "095",
        "instruction": "In your role as a Budget Analyst, observe that on 2025-08-13, the 'Toys' category recorded fewer than 7,000 sessions. This indicates a lack of seasonal interest. Cut the budget for the 'Holiday - Toys' ad set by 15%, considering its ROAS for Aug 7-13 is marginally above breakeven. Adjust the new budget accordingly and log the adjustment with 'Low Seasonal Viewership' as the reason.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Toys"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 340.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 340.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 340.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Seasonal Viewership"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "096",
        "instruction": "As a Growth Analyst, handle the increase of the budget for the 'Back to School - Laptops' ad set, noted for its 7-day ROAS exceeding 11, by 12% due to the average active users for 'Electronics' (Aug 7-13) being over 3,500. Ensure the new budget is rounded and record the update with the reason 'High Engagement & ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 12
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 873.6,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 870.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 870.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Engagement & ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "097",
        "instruction": "Coordinate the reduction of the budget for the 'Fall Fashion - Men' ad set by 18%, taking into account the average active users for 'Apparel' (Aug 7-13) were below 3500, which indicates diminishing interest, and its high CPA of over $9. Round the adjusted budget as per policy and document the reason as 'Softening Interest & High CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Apparel",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 18
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 615.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 620.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 620.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Softening Interest & High CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "098",
        "instruction": "As a Growth Analyst, observe that the 'Electronics - UK' ad set demonstrates a robust 7-day ROAS exceeding 12. On 2025-08-13, the Electronics category recorded over 14,500 sessions. This factors' synergy justifies a 22% budget augmentation. Round the ultimate budget according to policy and document the modification with the reason 'Strong Performance & Viewership'. Additionally, for a consistent mobile strategy, ensure the 'App Installs - Android' ad set replicates the 'App Installs - iOS' ad set. Modify the Android ad set's strategy from 'lowest_cost' to 'cost_cap', and align the bid amount with that of the iOS ad set. Record the change as a strategy update with the reason 'Strategy Alignment'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - EU"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 22
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 854.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 850.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 850.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strong Performance & Viewership"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_strategy": "cost_cap",
                    "new_bid": 2.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "110",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 2.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strategy Alignment"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "101",
        "instruction": "As a Growth Analyst, note that the 'Apparel' category surpassed 11,000 sessions on 2025-08-13, yet the 'Fall Fashion - Men' ad set carries a 7-day CPA exceeding $9.0. Given this inefficiency despite significant interest, reduce its budget by 15%. The final budget should be rounded to accord with the policy unit. Record the change with the reason 'High Viewership & Inefficient CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 637.5,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 640.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 640.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Viewership & Inefficient CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "102",
        "instruction": "As a Budget Analyst, observe that the average viewership for the 'Toys' category from Aug 7-13 is below 8,000 sessions, yet the 'Holiday - Toys' ad set demonstrates an outstanding 7-day ROAS exceeding 12.0. Enhance the budget for this high-performing ad set within a low-traffic category by 25%. Ensure the new budget is rounded and document the change citing 'Reward High ROAS in Low Viewership Category'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Toys",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 25
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 500.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 500.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 500.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Reward High ROAS in Low Viewership Category"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "103",
        "instruction": "In your role as a Growth Analyst, note that the 'Mobile' category on 2025-08-13 achieved over 19,000 sessions. For the 'App Installs - Android' ad set, which maintains a 7-day (Aug 7-13) CPA below $6.0, elevate the budget by 30%. Round the ultimate amount and document the update with the reason 'High Session Count & Efficient CPA'. Additionally, the 'Electronics - UK' ad set, part of a 'Sales' campaign, requires a specified cost target. Change its strategy from 'lowest_cost' to 'cost_cap' and assign a bid amount of $30.0. Record the modification as a strategy update with the reason 'Policy Compliance: Sales CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 30
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1300.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1300.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 1300.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Session Count & Efficient CPA"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - EU"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_strategy": "cost_cap",
                    "new_bid": 30.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "112",
                    "old_strategy": "lowest_cost",
                    "new_strategy": "cost_cap",
                    "old_bid": null,
                    "new_bid": 30.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Policy Compliance: Sales CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "104",
        "instruction": "As a Budget Analyst, handle the evaluation of average active users for 'Electronics' from August 7 to 13, noting a strong performance with over 3,700 users. The ad set 'Electronics - UK' boasts a remarkable 7-day ROAS exceeding 12.5. These metrics support an 18% boost in budget. Adjust the new budget according to policy rules and document the modification with the reason 'Strong User Base & ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - EU"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 18
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 826.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 830.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 830.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strong User Base & ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "105",
        "instruction": "In your role as a Growth Analyst, assess the viewership for 'Home' on 2025-08-13, which was low at under 9,000 sessions. Additionally, the 'Holiday - Home Goods' ad set has a 7-day CPA above $8.0. Due to these negative indicators, coordinate a substantial 40% budget reduction. Adjust the final budget according to policy and record the change with the note 'Low Viewership & Inefficient CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Home"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 40
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 300.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 300.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 300.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Viewership & Inefficient CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "106",
        "instruction": "Handle your role as a Budget Analyst. The 'Apparel' viewership from Aug 7-13 demonstrated high numbers. The 'Fall Fashion - Men' ad set boasts a robust 7-day ROAS exceeding 11.0. Enhance this strong performance in a high-interest segment by increasing the budget by 15%. Round the adjusted budget and document the modification with the reason 'Sustained Viewership & Strong ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Apparel",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 862.5,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 860.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 860.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Sustained Viewership & Strong ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "107",
        "instruction": "Coordinate your tasks as a Growth Analyst. Despite high viewership for 'Electronics' on 2025-08-13, the 'Electronics - CA' ad set registers a 7-day ROAS below 10.5, indicating poor efficiency. Reduce its budget modestly by 8% to boost overall campaign ROAS. Round the updated budget and note the change with the reason 'Inefficient ROAS Despite High Viewership'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - US"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 8
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 846.4,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 850.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 850.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inefficient ROAS Despite High Viewership"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "108",
        "instruction": "As a Budget Analyst, you will note that the 'Mobile' category exceeded 7,500 active users on 2025-08-13. The 'App Installs - iOS' ad set demonstrates great efficiency with a 7-day CPA below $4.6. This situation justifies a substantial budget increase of 35%. Remember to round and log the adjustment with the reason 'High User Count & Excellent CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - iOS"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Mobile"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "111",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 35
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1350.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1350.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 1350.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High User Count & Excellent CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "109",
        "instruction": "Your role as a Growth Analyst involves recognizing that the 'Toys' category had a low average session count from Aug 7-13. The 'Holiday - Toys' ad set's 7-day CPA exceeds $7.5, making it inefficient for this category. Reduce the budget by 22%. Ensure you round and log the modification with the reason 'Low Avg Viewership & High CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Toys",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 22
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 312.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 310.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 310.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Avg Viewership & High CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "110",
        "instruction": "As a Budget Analyst, note that the 'Apparel - CA' ad set has achieved a strong 7-day ROAS exceeding 13.0. Additionally, on 2025-08-13, the Apparel category experienced high viewership. These favorable indicators warrant a 15% budget increase. Please round off the budget and document the change with the reason 'Excellent ROAS & High Viewership'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 678.5,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 680.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 680.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Excellent ROAS & High Viewership"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "016",
        "instruction": "In your role as a Performance Marketing Analyst, conduct a daily analysis for the 'Q3 Brand Awareness Push' campaign dated 2025-08-13. Identify any live ad sets that reported a ROAS of 0. For such ad sets, promptly pause them. Subsequently, establish a new 'Sales' campaign named 'Review_Underperformers_2025-08-13'. Develop a new 'paused' ad set under this campaign, categorizing it as 'All' with the title 'Video Ads Europe', and assign a budget of just $10 for future assessment. Moreover, increase the budget by 30% for active ad sets that contain 'Back to School' in their names if the CPA between 2025-08-07 and 2025-08-13 is under $10. Ensure to log any budget adjustments with the rationale 'CPA update'.",
        "actions": [
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Q3 Brand Awareness Push"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "2"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddCampaign",
                "arguments": {
                    "campaign_id": "12",
                    "name": "Review_Underperformers_2025-08-13",
                    "objective": "Sales",
                    "created_date": "2025-08-14",
                    "status": "active"
                },
            },
            {
                "name": "AddAdset",
                "arguments": {
                    "adset_id": "114",
                    "campaign_id": "12",
                    "name": "Video Ads Europe",
                    "category": "All",
                    "daily_budget": 10.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": null,
                    "status": "paused",
                    "updated_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 30
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 1014.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 1014.0,
                    "old_budget": 780.0,
                    "reason": "CPA update",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "017",
        "instruction": "Take responsibility for budget management. Reduce the budget for all ad sets in the 'Q3 Brand Awareness Push' campaign to the 'min_budget_allocation' value as specified in policy parameters, and boost the 'Global Summer Sale' campaign budget by 20% for each ad set. Record all budget modifications citing 'Q3 Budget Shift' as the reason.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Q3 Brand Awareness Push"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "2"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "103",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "103",
                    "old_budget": 1180.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Q3 Budget Shift"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1104.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1104.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Q3 Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 708.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 708.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Q3 Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 840.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 840.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Q3 Budget Shift"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "018",
        "instruction": "Handle budget management. Lower the budget for all ad sets in the 'Fall Collection Launch' campaign to the 'min_budget_allocation' value from policy parameters, and enhance the 'Holiday Season Early Bird' campaign budget by 25% for each ad set. Document all budget alterations using 'Seasonal Budget Adjustment' as the justification.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Seasonal Budget Adjustment"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Seasonal Budget Adjustment"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Holiday Season Early Bird"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 625.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 625.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Seasonal Budget Adjustment"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 500.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 500.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Seasonal Budget Adjustment"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "019",
        "instruction": "Handle the budgets by reducing the allocation for all ad sets within the 'Back to School Deals' campaign to 'min_budget_allocation' as outlined in policy parameters, and by increasing the budget of each ad set in the 'Mobile App Installs Campaign' by 10%. Record all budget adjustments with the explanation 'Performance Rebalance'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Back to School Deals"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Performance Rebalance"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "109",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "109",
                    "old_budget": 300.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Performance Rebalance"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "7"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 1100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Performance Rebalance"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 1100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Performance Rebalance"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "020",
        "instruction": "Coordinate the budgets by lowering the funds for every ad set in the 'Holiday Season Early Bird' campaign to reach 'min_budget_allocation' according to policy parameters and by elevating each ad set's budget in the 'Fall Collection Launch' campaign by 15%. Document all budget modifications using 'Strategic Priority Shift' as the reason.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Holiday Season Early Bird"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strategic Priority Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strategic Priority Shift"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 851.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 851.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strategic Priority Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 862.5
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 862.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Strategic Priority Shift"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "021",
        "instruction": "Handle the management of budgets. Adjust the budget for every ad set within the 'Mobile App Installs Campaign' campaign, reducing it to the 'min_budget_allocation' specified in policy parameters, and raise the 'Q3 Brand Awareness Push' campaign budget by 40% for its ad set. Record all budget modifications citing 'Objective Realignment' as the reason.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "7"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Objective Realignment"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Objective Realignment"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Q3 Brand Awareness Push"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "2"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1180.0,
                    "percent": 40
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "103",
                    "new_budget": 1652.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "103",
                    "old_budget": 1180.0,
                    "new_budget": 1652.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Objective Realignment"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "022",
        "instruction": "Manage the budget allocation. Reduce the budget for each ad set in the 'Global Summer Sale' campaign to 'min_budget_allocation' as dictated by policy params, and enhance the 'Back to School Deals' campaign budget by 15% for each ad set. Document every budget change with the reason 'Mid-Q3 Budget Review'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mid-Q3 Budget Review"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mid-Q3 Budget Review"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mid-Q3 Budget Review"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Back to School Deals"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 897.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 897.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mid-Q3 Budget Review"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 300.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "109",
                    "new_budget": 345.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "109",
                    "old_budget": 300.0,
                    "new_budget": 345.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Mid-Q3 Budget Review"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "023",
        "instruction": "You are responsible for handling budgets. Adjust the budget for all ad sets within the 'Fall Collection Launch' campaign to align with the 'min_budget_allocation' outlined in the policy parameters, and raise the 'Global Summer Sale' campaign budget by 10% for each ad set. Document all budget modifications with the rationale 'Inventory-Based Budget Shift'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1012.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1012.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 649.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 649.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 770.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 770.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "024",
        "instruction": "You are tasked with managing budgets. Adjust the budget for all ad sets under the 'Fall Collection Launch' campaign to the 'min_budget_allocation' stipulated in policy parameters, and increase the 'Global Summer Sale' campaign budget by 10% for each ad set. Moreover, ensure all adjusted budgets are rounded to the nearest unit as specified by the 'budget_rounding_unit' policy parameter. Record all budget changes citing 'Inventory-Based Budget Shift' as the reason.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 100.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 100.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 100.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 10
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1012.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1010.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1010.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 649.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 650.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 650.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 10
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 770.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 770.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 770.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inventory-Based Budget Shift"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "025",
        "instruction": "As a Performance Marketing Analyst, handle a daily performance assessment for the 'Q3 Brand Awareness Push' campaign specifically for the date 2025-08-12. Identify any active ad sets with a ROAS precisely at 0. Pause each of these ad sets. Next, launch a 'Traffic' campaign titled 'Flagged_For_Review_2025-08-12'. Develop a new 'paused' ad set in this campaign, categorized under 'All' and named 'Brand Content - Low Performance', with a minimal budget of $20 intended for future evaluation. Additionally, for each active ad set containing 'Holiday' in its name, if their CPA from 2025-08-07 to 2025-08-13 was under $9, escalate their budget by 25%. Ensure you log any budget modification, specifying 'CPA Performance Boost' as the reason.",
        "actions": [
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Q3 Brand Awareness Push"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "2"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-12"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddCampaign",
                "arguments": {
                    "campaign_id": "12",
                    "name": "Flagged_For_Review_2025-08-12",
                    "objective": "Traffic",
                    "created_date": "2025-08-14",
                    "status": "active"
                },
            },
            {
                "name": "AddAdset",
                "arguments": {
                    "adset_id": "114",
                    "campaign_id": "12",
                    "name": "Brand Content - Low Performance",
                    "category": "All",
                    "daily_budget": 20.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": null,
                    "status": "paused",
                    "updated_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 625.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 625.0,
                    "old_budget": 500.0,
                    "reason": "CPA Performance Boost",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 25
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 500.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 500.0,
                    "old_budget": 400.0,
                    "reason": "CPA Performance Boost",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "026",
        "instruction": "Function as a Performance Marketing Analyst by coordinating a performance evaluation on all active ad sets for the date 2025-08-13. If any ad set shows a ROAS of less than 0.1, promptly pause it. Subsequently, initiate a new 'Awareness' campaign under the name 'Global_Underperformers_Aug13'. Establish a new 'paused' ad set inside this campaign, with the 'Cross-Category' designation and named 'General Review Bin', allocating a budget of $15. Furthermore, increase the budget by 20% for active ad sets in the 'Fall Collection Launch' campaign, provided their CPA between 2025-08-07 and 2025-08-13 was less than $10. Document all modifications to budgets stating 'Low CPA Incentive' as the justification.",
        "actions": [
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddCampaign",
                "arguments": {
                    "campaign_id": "12",
                    "name": "Global_Underperformers_Aug13",
                    "objective": "Awareness",
                    "created_date": "2025-08-14",
                    "status": "active"
                },
            },
            {
                "name": "AddAdset",
                "arguments": {
                    "adset_id": "114",
                    "campaign_id": "12",
                    "name": "General Review Bin",
                    "category": "Cross-Category",
                    "daily_budget": 15.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": null,
                    "status": "paused",
                    "updated_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 888.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 888.0,
                    "old_budget": 740.0,
                    "reason": "Low CPA Incentive",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 900.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 900.0,
                    "old_budget": 750.0,
                    "reason": "Low CPA Incentive",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "027",
        "instruction": "As a Performance Marketing Analyst, carry out a performance evaluation on the 'Global Summer Sale' campaign for 2025-08-13. If any ongoing ad set presents a ROAS under 12.5, suspend it instantly and initiate a new review campaign. The new 'Sales' campaign is to be titled 'Summer_Sale_Review_Bin'. Within this, form a 'paused' ad set labeled 'For review' with 'Review' as the category, and a budget allocated at $50. Moreover, for the ongoing ad sets in the 'Holiday Season Early Bird' campaign, enhance their budget by 15% if their CPA from the period 2025-08-07 to 2025-08-13 is less than $8.5. Document any budget adjustments with the justification 'ROAS/CPA Combined Action'.",
        "actions": [
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "101",
                    "new_status": "paused"
                },
            },
            {
                "name": "AddCampaign",
                "arguments": {
                    "campaign_id": "12",
                    "name": "Summer_Sale_Review_Bin",
                    "objective": "Sales",
                    "created_date": "2025-08-14",
                    "status": "active"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAdset",
                "arguments": {
                    "adset_id": "114",
                    "campaign_id": "12",
                    "name": "For review",
                    "category": "Review",
                    "daily_budget": 50.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": null,
                    "status": "paused",
                    "updated_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Holiday Season Early Bird"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 575.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 575.0,
                    "old_budget": 500.0,
                    "reason": "ROAS/CPA Combined Action",
                    "changed_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 460.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 460.0,
                    "old_budget": 400.0,
                    "reason": "ROAS/CPA Combined Action",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "028",
        "instruction": "Act as a Performance Marketing Analyst.A performance report indicates that within the 'Electronics - CA' ad set, the halted video ad achieves a 15% lower CPA compared to the active image ad. As this surpasses the 'video_cpa_advantage_pct' policy threshold (presently 10%), coordinate a creative rotation. Cease the image ad and activate the video ad. To support the newly active video creative, augment the ad set's budget by 8%. Record the budget modification with the rationale 'Video Performance Rotation' and document the entire process as a 'creative_rotation' automation run with ID 'AR-CR-20250814-02' and input_ref 'adset_101_cpa_policy'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - CA"
                },
            },
            {
                "name": "SearchAdsByAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1101"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1102"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 15,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1101"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1102"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1101",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1102",
                    "new_status": "active"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 8
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 993.6
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 993.6,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Video Performance Rotation"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-02",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "adset_101_cpa_policy",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "029",
        "instruction": "As a Performance Marketing Analyst, examine the 'Back to School - Laptops' ad set (ID 108). It shows that the paused video ad (ID 1112) achieves a CPA 25% lower than the active image ad (ID 1111). Determine whether this aligns with the 'video_cpa_advantage_pct' policy threshold (10%). If it does, conduct a creative rotation by altering the ad statuses. Afterward, raise the ad set's budget by 10% to leverage the superior performance. Document the budget alteration with the reason 'Creative Optimization' and record the procedure as a 'creative_rotation' automation run with ID 'AR-CR-20250814-03' and input_ref 'adset_108_cpa_check'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 25,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1111"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1112"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1111",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1112",
                    "new_status": "active"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 858.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 858.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Creative Optimization"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-03",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "adset_108_cpa_check",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "030",
        "instruction": "As a Performance Marketing Analyst, review the test results for the 'Apparel - CA' ad set showing that the paused carousel ad possesses a 30% greater CTR than the active image ad. Since there isn't a dedicated policy for CTR, apply the 'video_cpa_advantage_pct' value of 10% as a general benchmark for notable improvement. When the CTR enhancement surpasses this threshold, conduct a rotation of the creatives by pausing the image ad and activating the carousel ad. Subsequently, amplify the ad set budget by 15%. Note the budget increase with 'CTR-based Rotation' as the reason and document a 'creative_rotation' automation run using 'AR-CR-20250814-04' with input_ref 'apparel_ctr_test'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "SearchAdsByAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1103"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1104"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1103"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1104"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 30,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1103",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1104",
                    "new_status": "active"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 678.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 678.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "CTR-based Rotation"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-04",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "apparel_ctr_test",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "031",
        "instruction": "As a Performance Marketing Analyst, a review of the 'Fall Fashion - Women' adset indicates that the video ad has a CPA that is 8% lower than the image ad. This enhancement does not meet the necessary 10% according to the 'video_cpa_advantage_pct' policy. Due to the lack of significant improvement, the creative rotation will be halted. Instead, handle a 5% reduction in the ad set's budget since the current creatives are not achieving efficiency objectives. Record the budget adjustment with the reason 'Rotation Test Failed' and document a 'creative_rotation' automation run as 'skipped' with ID 'AR-CR-20250814-05', referencing 'adset_104_cpa_underperform'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "SearchAdsByAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1106"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1107"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 8,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 703.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 703.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Rotation Test Failed"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-05",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "skipped",
                    "input_ref": "adset_104_cpa_underperform",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "032",
        "instruction": "In your capacity as a Performance Marketing Analyst, note that the paused video ad for ad set 'Electronics - CA' achieves a 40% improvement in CPA compared to the active image, significantly surpassing the 10% policy threshold. Coordinate the creative rotation. Owing to the excellent performance, boost the budget by 20%. Additionally, increase the 'cost_cap' bid amount for this ad set by 10% to enhance competitiveness. Document both the budget and strategy modifications separately with the reason 'High-Performance Rotation' and log the entire process as a 'creative_rotation' run with ID 'AR-CR-20250814-06' and input_ref 'high_cpa_advantage'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - CA"
                },
            },
            {
                "name": "SearchAdsByAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1101"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1102"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1101"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1102"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 40,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1101",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1102",
                    "new_status": "active"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 920.0,
                    "percent": 20
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 1104.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 1104.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High-Performance Rotation"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 32.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_strategy": "cost_cap",
                    "new_bid": 35.2
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "101",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 32.0,
                    "new_bid": 35.2,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High-Performance Rotation"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-06",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "high_cpa_advantage",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "033",
        "instruction": "You are responsible for managing budgets. The 'Holiday Season Early Bird' campaign has been deprioritized. Reduce the budget for all its ad sets by 50%. Reallocate these funds to the 'Mobile App Installs Campaign' by increasing its ad sets' budget by 40%. Prior to reducing any budget, confirm the new amount doesn't fall beneath the 'min_budget_allocation' policy. If it does, adjust it to the minimum value. Ensure all final budgets are rounded according to the 'budget_rounding_unit'. Record all modifications with the justification 'App Install Push'.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Holiday Season Early Bird"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 50
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 250.0,
                    "threshold": 100,
                    "operator": "greater_equal"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 250.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 250.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 250.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "App Install Push"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 50
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 200.0,
                    "threshold": 100,
                    "operator": "greater_equal"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 200.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 200.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 200.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "App Install Push"
                },
            },
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "7"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 40
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1400.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1400.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 1400.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "App Install Push"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 40
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 1400.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1400.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "111",
                    "old_budget": 1000.0,
                    "new_budget": 1400.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "App Install Push"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "034",
        "instruction": "You are a Performance Marketing Analyst. The video ad for the 'Back to School - Laptops' adset performs 20% better in CPA than anticipated. Rotate the ads by disabling the image ad and activating the video ad. Boost the budget by 15%. Nevertheless, the new bid amount must be limited. Set the new bid to the smaller of the following: either a 15% increase on the current bid, or the 'max_bid_amount' policy value. Document all budget, strategy, and 'creative_rotation' automation execution with the reason 'Capped Bid Rotation', input_ref 'bid_cap' and run_id 'AR-CR-20250814-11'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "SearchAdsByAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1111"
                },
            },
            {
                "name": "GetStatusForAd",
                "arguments": {
                    "ad_id": "1112"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1111"
                },
            },
            {
                "name": "GetCreativeTypeForAd",
                "arguments": {
                    "ad_id": "1112"
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "video_cpa_advantage_pct"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 20,
                    "threshold": 10,
                    "operator": "greater"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1111",
                    "new_status": "paused"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1112",
                    "new_status": "active"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 15
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 897.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 897.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Capped Bid Rotation"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 42.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "max_bid_amount"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 48.3,
                    "threshold": 50.0,
                    "operator": "greater"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_strategy": "cost_cap",
                    "new_bid": 48.3
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "108",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 42.0,
                    "new_bid": 48.3,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Capped Bid Rotation"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-CR-20250814-11",
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "reason": "Capped Bid Rotation",
                    "input_ref": "bid_cap",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "035",
        "instruction": "As the Head of Automation, handle the implementation of the complete daily strategy for the 'Fall Fashion - Women' adset from the 'Fall Collection Launch' campaign as defined in 'plan_2025-08-13'. Ensure the budget and bid strategy are applied as outlined. Maintain an audit trail by documenting every modification.",
        "actions": [
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Fall Collection Launch"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlans",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetDateForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "cost_cap",
                    "new_bid": 22.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 750.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 20.0,
                    "new_bid": 22.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "036",
        "instruction": "Acting as the Head of Automation, coordinate the execution of the entire daily strategy for the 'Electronics - CA' ad set from the 'Global Summer Sale' campaign as laid out in 'plan_2025-08-13'. Make sure to apply the planned budget, bid strategy, and bid amount. Log all alterations and document the whole process as a 'strategy_apply' automation operation with ID 'AR-APPLY-202508-01'.",
        "actions": [
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetNameForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_strategy": "cost_cap",
                    "new_bid": 35.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 950.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "101",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 32.0,
                    "new_bid": 35.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "strategy_apply",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "plan_2025-08-13",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "037",
        "instruction": "As the Head of Automation, handle the implementation of the daily plan from 'plan_2025-08-13' to the 'Apparel - CA' ad set. This plan defines 'lowest_cost', so updating only the budget is necessary. Ensure the ad set is currently active before making the changes. Document the budget alteration, citing the plan as the justification.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 600.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "038",
        "instruction": "Being the Head of Automation, coordinate the application of the older plan 'plan_2025-08-12' to the 'Fall Fashion - Women' ad set as part of a rollback test. Implement the budget and bid strategy as specified by this past plan. Record all modifications, mentioning the plan name as the rationale.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-12"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 740.0
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "cost_cap",
                    "new_bid": 20.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 740.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-12"
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 20.0,
                    "new_bid": 20.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-12"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "039",
        "instruction": "As the Head of Automation, handle the strategy implementation for the 'Back to School - Laptops' ad set utilizing 'plan_2025-08-13'. Follow the special directive to apply the planned budget while boosting the planned bid amount by 10% for added competitiveness. Document both the budget and the modified strategy alterations, using 'plan_2025-08-13_modified' as the reason.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 45.0,
                    "percent": 10
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_strategy": "cost_cap",
                    "new_bid": 49.5
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 800.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13_modified"
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "108",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 42.0,
                    "new_bid": 49.5,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13_modified"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "040",
        "instruction": "As the Head of Automation, coordinate the implementation of the entire 'plan_2025-08-13' with the 'Fall Fashion - Men' ad set. Prior to execution, verify if the ad set's current daily budget and bid strategy are already in alignment with the plan. If they align, refrain from proceeding with an update, but log a 'strategy_apply' automation run with the status 'skipped', referencing the plan name as input_ref. If they don't align, proceed with the application and log accordingly.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetBidStrategyForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 750.0,
                    "threshold": 750.0,
                    "operator": "equal"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "strategy_apply",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "skipped",
                    "input_ref": "plan_2025-08-13",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "041",
        "instruction": "As the Head of Automation, ensure the budget from 'plan_2025-08-13' is allocated to 'Holiday - Home Goods'. Avoid applying the bid strategy. Prior to execution, confirm that the budget modification (from current to planned) does not exceed a 20% increase for safety purposes. If it surpasses 20%, terminate the process. Document the budget alteration and register a 'budget_apply' automation run, noting the plan name for both reason and input_ref.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "CalculateSpendVariance",
                "arguments": {
                    "planned_spend": 500.0,
                    "actual_spend": 500.0
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 0,
                    "threshold": 20,
                    "operator": "less"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 500.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "budget_apply",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "reason": "plan_2025-08-13",
                    "input_ref": "plan_2025-08-13",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "042",
        "instruction": "Being the Head of Automation, allocate the budget from 'plan_2025-08-13' to ad set 'Brand - Video Ads', then promptly pause the ad set as a precautionary measure for temporary reduction. The bid strategy is to remain unchanged. Capture the budget modification and log the entire process as a 'budget_apply_and_pause' automation run, utilizing the plan name for reason and input_ref.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Brand - Video Ads"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "103",
                    "new_budget": 1200.0
                },
            },
            {
                "name": "UpdateAdsetStatus",
                "arguments": {
                    "adset_id": "103",
                    "new_status": "paused"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "103",
                    "old_budget": 1180.0,
                    "new_budget": 1200.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AddAutomationRun",
                "arguments": {
                    "run_id": "AR-APPLY-202508-01",
                    "run_type": "budget_apply_and_pause",
                    "started_at": "2025-08-13T01:01:01Z",
                    "ended_at": "2025-08-13T01:01:01Z",
                    "status": "completed",
                    "input_ref": "plan_2025-08-13",
                    "errors_json": "{}"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "044",
        "instruction": "As a Compliance Officer, you must enforce a newly implemented, more stringent bidding policy. Update the 'max_bid_amount' policy parameter to 40. For all active adsets that exclusively employ a 'cost_cap' bid strategy, adjust the bid amount to the newly permitted maximum value only if their current bid surpasses this new threshold. Each modification should be documented in the strategy change log citing 'Policy Enforcement' as the reason.",
        "actions": [
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdatePolicyParam",
                "arguments": {
                    "param_name": "max_bid_amount",
                    "param_value": "40",
                    "updated_at": "2025-08-13T01:01:01Z"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "SearchAdsetsByBidStrategy",
                "arguments": {
                    "bid_strategy": "cost_cap"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_strategy": "cost_cap",
                    "new_bid": 40.0
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "108",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 42.0,
                    "new_bid": 40.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Policy Enforcement"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "045",
        "instruction": "As a Bid Management Agent, you need to assess the ROAS for all active 'cost_cap' ad sets as of yesterday (2025-08-13). If the ROAS exceeded 11.0, enhance the bid amount by 5%. Conversely, if the ROAS fell below 9.0, reduce the bid amount by 5%. Document any changes in the strategy change log under the reason 'Daily Bid Optimization'.",
        "actions": [
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "SearchAdsetsByBidStrategy",
                "arguments": {
                    "bid_strategy": "cost_cap"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForDay",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 20.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "cost_cap",
                    "new_bid": 21.0
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 20.0,
                    "new_bid": 21.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Daily Bid Optimization"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 18.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_strategy": "cost_cap",
                    "new_bid": 18.9
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "106",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 18.0,
                    "new_bid": 18.9,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Daily Bid Optimization"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 42.0,
                    "percent": 5
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_strategy": "cost_cap",
                    "new_bid": 44.1
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "108",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 42.0,
                    "new_bid": 44.1,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Daily Bid Optimization"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 2.5,
                    "percent": 5
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_strategy": "cost_cap",
                    "new_bid": 2.375
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "111",
                    "old_strategy": "cost_cap",
                    "new_strategy": "cost_cap",
                    "old_bid": 2.5,
                    "new_bid": 2.375,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Daily Bid Optimization"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "047",
        "instruction": "As a Finance Analyst, handle the verification that all ad set budgets within the 'Global Summer Sale' campaign align with the most recent plan ('plan_2025-08-13'). For each ad set in that campaign, review whether its current budget corresponds with the plan's budget. If they do not match, adjust the ad set's budget to align with the plan. Record only the budgets that were altered, citing 'Plan Synchronization' as the reason.",
        "actions": [
            {
                "name": "SearchCampaignsByName",
                "arguments": {
                    "name_query": "Global Summer Sale"
                },
            },
            {
                "name": "SearchAdsetsByCampaignId",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "old_budget": 920.0,
                    "new_budget": 950.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Plan Synchronization"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 600.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Plan Synchronization"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "048",
        "instruction": "Operating as an Ad Operations Specialist, identify all active ad sets employing a 'cost_cap' bid strategy that are not part of a 'Sales' objective campaign. For each such ad set, modify its bid strategy to 'default_bid_strategy' as specified in policy parameters. Record every strategy modification with 'cost_cap misuse' as the rationale.",
        "actions": [
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "default_bid_strategy"
                },
            },
            {
                "name": "SearchAdsetsByStatus",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "SearchCampaignsByObjective",
                "arguments": {
                    "objective": "Sales"
                },
            },
            {
                "name": "SearchAdsetsByBidStrategy",
                "arguments": {
                    "bid_strategy": "cost_cap"
                },
            },
            {
                "name": "GetCampaignIdForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetCampaignIdForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetCampaignIdForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetCampaignIdForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetCampaignIdForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "104",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 20.0,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "cost_cap misuse"
                },
            },
            {
                "name": "GetBidAmountForAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "UpdateBidStrategyForAdset",
                "arguments": {
                    "adset_id": "111",
                    "new_strategy": "lowest_cost",
                    "new_bid": null
                },
            },
            {
                "name": "LogStrategyChange",
                "arguments": {
                    "adset_id": "111",
                    "old_strategy": "cost_cap",
                    "new_strategy": "lowest_cost",
                    "old_bid": 2.5,
                    "new_bid": null,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "cost_cap misuse"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "049",
        "instruction": "You are a Plan Execution Agent. Handle the task of allocating the budget from 'plan_2025-08-13' to the 'Electronics - CA' ad set. Assess the percentage increase from the current budget to the intended budget. Ensure this increase does not surpass 5%. If the increase remains within the limit, adjust the budget accordingly and record with the justification 'Budget increase'. If it surpasses the limit, refrain from making the change.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - US"
                },
            },
            {
                "name": "GetAllocationsForPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "CalculateSpendVariance",
                "arguments": {
                    "planned_spend": 920.0,
                    "actual_spend": 950.0
                },
            },
            {
                "name": "CompareValue",
                "arguments": {
                    "value": 3.260869565217391,
                    "threshold": 5,
                    "operator": "less_equal"
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "old_budget": 920.0,
                    "reason": "Budget increase",
                    "changed_at": "2025-08-13T01:01:01Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "111",
        "instruction": "You are a Growth Analyst. The 'Apparel' category exhibited significant interest on 2025-08-13 with over 11,000 sessions. For the 'Fall Fashion - Men' ad set, which maintains an effective 7-day CPA under $9.50, boost its budget by 18%. Adjust the final budget based on the rounding policy and document the update with the reason 'High Viewership & Efficient CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Men"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "105",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 750.0,
                    "percent": 18
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 885.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 880.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "105",
                    "old_budget": 750.0,
                    "new_budget": 880.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Viewership & Efficient CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "112",
        "instruction": "As a Budget Analyst, it is observed that the average active users for 'Toys' from Aug 7-13 fall below 2,500, signaling low engagement. Additionally, the 'Holiday - Toys' ad set exhibits a high 7-day CPA exceeding $7.0. In light of these unfavorable metrics, reduce the budget by 20%. Ensure the new budget is rounded according to the policy and record it with the reason 'Low Engagement & High CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Toys"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Toys",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 400.0,
                    "percent": 20
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 320.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 320.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "107",
                    "old_budget": 400.0,
                    "new_budget": 320.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Engagement & High CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "113",
        "instruction": "Being a Growth Analyst, you note that the 'Electronics' category is thriving, achieving average sessions surpassing 13,000 from Aug 7-13. The 'Electronics - UK' ad set enjoys an exceptional 7-day ROAS over 12.0. Recognize this positive performance in a crucial category by boosting the budget by 25%. Follow rounding procedures as per policy and document the modification with the reason 'Sustained Viewership & High ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - UK"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 25
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 875.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 880.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 880.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Sustained Viewership & High ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "114",
        "instruction": "As a Budget Analyst, observe that on 2025-08-13, the 'Home' category's viewership fell under 8,500 sessions. Due to this low traffic and the 'Holiday - Home Goods' ad set exhibiting a subpar 7-day ROAS (under 12.5), it is essential to implement a 15% budget reduction. Adjust the new budget according to policy and document the modification stating 'Low Traffic & Mediocre ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Holiday - Home Goods"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Home"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "106",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 500.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 425.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 420.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "106",
                    "old_budget": 500.0,
                    "new_budget": 420.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Low Traffic & Mediocre ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "115",
        "instruction": "Being a Growth Analyst, note the 'Back to School - Laptops' ad set achieves an impressive 7-day CPA below $9.0. Also, there was a robust average of active users in 'Electronics' from Aug 7-13. This efficiency coupled with a substantial user base warrants a 20% budget enhancement. Ensure to adjust according to policy and record the update with the explanation 'Efficient CPA & Strong User Base'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Back to School - Laptops"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "108",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 780.0,
                    "percent": 20
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 936.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 940.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "108",
                    "old_budget": 780.0,
                    "new_budget": 940.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Efficient CPA & Strong User Base"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "116",
        "instruction": "As a Budget Analyst, handle the situation where despite high viewership on 2025-08-13 (over 11,000 sessions), the 'Apparel - CA' ad set shows a low 7-day ROAS (below 14.0). This inefficiency demands a 10% budget reduction to reallocate funds. Ensure to round the new budget according to policy and record the adjustment with the reason 'Inefficient ROAS in High Traffic Category'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 10
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 531.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 530.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 530.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Inefficient ROAS in High Traffic Category"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "117",
        "instruction": "As a Growth Analyst, coordinate the evaluation of the 'Apparel' category, which shows a strong average of active users from Aug 7-13. The 'Fall Fashion - Women' ad set presents a robust 7-day ROAS over 11.0. Such a combination supports a 12% budget increase to seize additional market share. Ensure to round the new budget following policy and document the adjustment with the reason 'High User Base & Solid ROAS'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Fall Fashion - Women"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Apparel",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "104",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 740.0,
                    "percent": 12
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 828.8,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 830.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "104",
                    "old_budget": 740.0,
                    "new_budget": 830.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High User Base & Solid ROAS"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "118",
        "instruction": "As a Budget Analyst, on 2025-08-13, the viewership for the 'Electronics' category was robust; however, the 'Electronics - UK' ad set experienced a high 7-day CPA exceeding $7.8. To enhance efficiency, reduce the budget for this ad set by 10%. Ensure the new budget is rounded according to policy and document the change with the reason 'High Viewership & High CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Electronics - UK"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Electronics"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "112",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 700.0,
                    "percent": 10
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 630.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 630.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "112",
                    "old_budget": 700.0,
                    "new_budget": 630.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Viewership & High CPA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "119",
        "instruction": "Being a Growth Analyst, note that the 'App Installs - Android' ad set has a disappointing 7-day ROAS. Additionally, average active users for the 'Mobile' category (Aug 7-13) are below 8,500. This underwhelming performance combined with moderate engagement necessitates a 25% budget reduction. Round the new budget in accordance with policy and record it with the reason 'Poor ROAS & Low Engagement'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "App Installs - Android"
                },
            },
            {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "arguments": {
                    "category": "Mobile",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "CalculateAdsetRoasForPeriod",
                "arguments": {
                    "adset_id": "110",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "DecreaseValueWithPercent",
                "arguments": {
                    "value": 1000.0,
                    "percent": 25
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 750.0,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 750.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "110",
                    "old_budget": 1000.0,
                    "new_budget": 750.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "Poor ROAS & Low Engagement"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "120",
        "instruction": "As a Budget Analyst, you should note that on 2025-08-13, the 'Apparel' category experienced more than 11,500 sessions. The 'Apparel - CA' ad set is performing with remarkable efficiency, showing a 7-day CPA below $7.9. Such favorable indicators warrant an increase in budget by 15%. Ensure to adjust the budget according to policy and record the update along with the reason 'High Sessions & Efficient CPA'.",
        "actions": [
            {
                "name": "SearchAdsetsByName",
                "arguments": {
                    "name_query": "Apparel - CA"
                },
            },
            {
                "name": "GetViewershipForDateAndCategory",
                "arguments": {
                    "date": "2025-08-13",
                    "category": "Apparel"
                },
            },
            {
                "name": "CalculateAdsetCpaForPeriod",
                "arguments": {
                    "adset_id": "102",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "IncreaseValueWithPercent",
                "arguments": {
                    "value": 590.0,
                    "percent": 15
                },
            },
            {
                "name": "GetPolicyParam",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "RoundNumberToUnit",
                "arguments": {
                    "number": 678.5,
                    "unit": 10
                },
            },
            {
                "name": "UpdateDailyBudgetForAdset",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 680.0
                },
            },
            {
                "name": "GetCurrentTimestamp",
                "arguments": {
                {}
                },
            },
            {
                "name": "LogBudgetChange",
                "arguments": {
                    "adset_id": "102",
                    "old_budget": 590.0,
                    "new_budget": 680.0,
                    "changed_at": "2025-08-13T01:01:01Z",
                    "reason": "High Sessions & Efficient CPA"
                }
            }
        ],
        "outputs": []
    }
]
