from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="sma_t1",
        instruction=(
            "You align ad set 101 with the approved 2025-08-13 plan (plan_2025-08-13) in a policy-guided way. "
            "Ensure the ad set reflects daily_budget 950.0 effective 2025-08-15T02:10:00Z and cost_cap with bid_amount 35.0 "
            "effective 2025-08-15T02:15:00Z. Your audit trail should include AR-20250815-01 as a plan_freeze for the plan "
            "(spanning 2025-08-15T02:00:00Z–2025-08-15T02:01:00Z), AR-20250815-02 as a budget_apply window that covers the "
            "02:10:00Z budget change (spanning 02:10:00Z–02:12:00Z), and AR-20250815-03 as a strategy_apply window that covers "
            "the 02:15:00Z bidding change (spanning 02:15:00Z–02:16:00Z). Use reason plan_2025-08-13 and follow read-modify-write "
            "by deriving prior values from a pre-change read. Return a final state read."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250815-01", "run_type": "plan_freeze",
                           "started_at": "2025-08-15T02:00:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250815-01", "ended_at": "2025-08-15T02:01:00Z"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250815-02", "run_type": "budget_apply",
                           "started_at": "2025-08-15T02:10:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 950.0, "updated_at": "2025-08-15T02:10:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0,
                           "changed_at": "2025-08-15T02:10:00Z", "reason": "plan_2025-08-13"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250815-02", "ended_at": "2025-08-15T02:12:00Z"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250815-03", "run_type": "strategy_apply",
                           "started_at": "2025-08-15T02:15:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0,
                           "updated_at": "2025-08-15T02:15:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 32.0, "new_bid": 35.0,
                           "changed_at": "2025-08-15T02:15:00Z", "reason": "plan_2025-08-13"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250815-03", "ended_at": "2025-08-15T02:16:00Z"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"})
        ],
        outputs=[
            """[
          {"plan_id":"plan_2025-08-13","adset_id":"101","final_budget":950.0,"final_strategy":"cost_cap","final_bid_amount":35.0},
          {"runs":["AR-20250815-01","AR-20250815-02","AR-20250815-03"]}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t2",
        instruction=(
            "You rotate creatives for ad set 102 at 2025-08-15T03:00:00Z by activating ad 1104 and pausing ad 1103 with "
            "rationale carousel uplift. Confirm creative types are canonical, capture 2025-08-13 insights before and after, "
            "and keep a concise audit."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250815-03", "run_type": "creative_rotation",
                           "started_at": "2025-08-15T03:00:00Z", "ended_at": "2025-08-15T03:01:00Z",
                           "status": "completed", "input_ref": "adset_102_rotation_1103_1104",
                           "errors_json": "{}"}),

            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-15T03:00:00Z", "rationale": "carousel uplift"}),

            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250815-04", "run_type": "post_rotation_audit",
                           "started_at": "2025-08-15T03:01:00Z", "ended_at": "2025-08-15T03:02:00Z",
                           "status": "completed", "input_ref": "adset_102_rotation_1103_1104",
                           "errors_json": "{}"}),
        ],
        outputs=[
            """[
              {"adset_id":"102","activated":"1104","paused":"1103"},
              {"rotation_id":"CR-4","runs":["AR-20250815-03","AR-20250815-04"]}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t3",
        instruction=(
            "You have to  Rebalance Apparel deterministically for ad set 102 at 2025-08-19T11:40:00Z in line with policy "
            "(respect rounding and max totals). Increase its daily budget to 610.0, log the change with reason "
            "apparel_topup_1140, and verify immediately after the update. Record a concise audit "
            "(AR-20250819-04, budget_rebalance, 11:40:00Z–11:40:30Z, completed, input_ref adset_102)."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "max_daily_budget_total"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 610.0, "updated_at": "2025-08-19T11:40:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 610.0,
                           "changed_at": "2025-08-19T11:40:00Z", "reason": "apparel_topup_1140"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-04", "run_type": "budget_rebalance",
                                                         "started_at": "2025-08-19T11:40:00Z",
                                                         "ended_at": "2025-08-19T11:40:30Z",
                                                         "status": "completed", "input_ref": "adset_102",
                                                         "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"102","final_daily_budget":610.0},{"automation_run":"AR-20250819-04"}]']
    ),

    Task(
        annotator="v6",
        user_id="sma_t4",
        instruction=(
            "You have to  Produce a KPI snapshot for ad set 101 as of 2025-08-13 and record an audit run "
            "(run_id kpi_snapshot_101_2025-08-13; started_at 2025-08-13T00:00:00Z; ended_at 2025-08-13T00:00:01Z; "
            "status completed; input_ref adset:101|baseline:2025-08-13). Report ROAS and CTR for 2025-08-13 and the "
            "total spend for 2025-08-07..2025-08-13, and list ad sets below min_roas_threshold_7d for 2025-08-13. "
            "This is read-only; do not alter budgets, bids, or creatives."
        ),
        actions=[
            Action(name="create_automation_run", kwargs={
                "run_id": "kpi_snapshot_101_2025-08-13",
                "run_type": "kpi_snapshot",
                "started_at": "2025-08-13T00:00:00Z",
                "ended_at": "2025-08-13T00:00:00Z",
                "status": "in_progress",
                "input_ref": "adset:101|baseline:2025-08-13",
                "errors_json": "{}"
            }),
            Action(name="get_policy_parameter", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="update_automation_run_end", kwargs={
                "run_id": "kpi_snapshot_101_2025-08-13",
                "status": "completed",
                "ended_at": "2025-08-13T00:00:01Z"
            }),
        ],
        outputs=[
            '{"adset_id":"101","date":"2025-08-13","roas":10.0,"ctr":0.0397}',
            '{"spend":{"adset_id":"101","start_date":"2025-08-07","end_date":"2025-08-13","total_spend":6140.0}}',
            '{"underperforming":[{"adset_id":"103"},{"adset_id":"110"},{"adset_id":"111"}]}'
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t5",
        instruction=(
            "You have to Create and apply a two-line plan for 2025-08-27 across 102 and 112. "
            "Plan plan_2025-08-27b (author planning_agent_v1, created_at 2025-08-27T01:58:40Z, checksum p27b1360) totals 1360.0: "
            "102 → 600.0 (lowest_cost, image), 112 → 760.0 (lowest_cost, image). Freeze (AR-20250827-04, 01:58:40Z–02:00:10Z). "
            "Apply both budgets at 02:05:00Z with reason plan_2025-08-27b and verify."
        ),
        actions=[
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 1360.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-27b", "date": "2025-08-27", "total_budget": 1360.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-27T01:58:40Z",
                           "checksum": "p27b1360", "allocations": [
                           {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-27"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250827-04", "run_type": "plan_freeze",
                                                         "started_at": "2025-08-27T01:58:40Z",
                                                         "ended_at": "2025-08-27T02:00:10Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-27b"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 600.0, "updated_at": "2025-08-27T02:05:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0,
                           "changed_at": "2025-08-27T02:05:00Z", "reason": "plan_2025-08-27b"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 760.0, "updated_at": "2025-08-27T02:05:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 760.0,
                           "changed_at": "2025-08-27T02:05:00Z", "reason": "plan_2025-08-27b"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
        ],
        outputs=[
            """[
          {"plan_id":"plan_2025-08-27b","applied_to":["102","112"]},
          {"freeze_run":"AR-20250827-04"}
        ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t6",
        instruction=(
            "You have to Execute a plan-driven creative rotation for ad set 102 on 2025-08-28: make the carousel live and pause the prior image "
            "to refresh fatigue. Use plan_2025-08-28c as the audit reason. Record AR-20250828-06 (creative_rotation, "
            "10:00:00Z–10:02:00Z, completed, input_ref adset:102|rotation). Verify canonical creative types, capture pre/post ad listings, "
            "and log the rotation with the plan_id reason."
        ),
        actions=[
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250828-06", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-28T10:00:00Z",
                                                         "ended_at": "2025-08-28T10:02:00Z", "status": "completed",
                                                         "input_ref": "adset:102|rotation", "errors_json": "{}"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-28T10:01:00Z", "rationale": "plan_2025-08-28c"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
        ],
        outputs=[
            """[
              {"adset_id":"102","activated":"1104","paused":"1103"},
              {"automation_run":"AR-20250828-06"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t7",
        instruction=(
            "You align ad set 103 with the approved 2025-08-13 plan in a policy-guided way. "
            "Set daily_budget to 1120.0 effective 2025-08-15T02:30:00Z and apply cost_cap with bid_amount 6.5 at the same time. "
            "Use a minimal audit and verify the end state without creating any new ads."
        ),
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            Action(name="validate_allocations_against_policy", kwargs={
                "total_budget": 1120.0,
                "allocations": [
                    {"adset_id": "103", "budget": 1120.0, "bid_strategy": "cost_cap", "bid_amount": 6.5,
                     "creative_type": "video"}
                ]
            }),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "103", "new_budget": 1120.0, "updated_at": "2025-08-15T02:30:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 1120.0,
                           "changed_at": "2025-08-15T02:30:00Z", "reason": "plan_2025-08-13"}),

            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 6.5,
                           "updated_at": "2025-08-15T02:30:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.5, "changed_at": "2025-08-15T02:30:00Z",
                           "reason": "plan_2025-08-13"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
        ],
        outputs=['[{"adset_id":"103","final_budget":1120.0,"final_bid_amount":6.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t8",
        instruction=(
            "You adjust bids in response to the verified 2025-08-14 price for product 1. "
            "Set ad set 101 to cost_cap with bid 38.0 effective 2025-08-15T05:20:00Z and ad set 104 to cost_cap with bid 22.0 "
            "effective 2025-08-15T05:25:00Z. Log each change with reason price_2025-08-14, and report ROAS for both ad sets on 2025-08-13. "
            "Keep the audit concise and avoid referencing internal tool or table names."
        ),
        actions=[
            Action(name="get_product_price_on_date", kwargs={"product_id": "1", "date": "2025-08-14"}),
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 38.0,
                           "updated_at": "2025-08-15T05:20:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0,
                           "new_bid": 38.0, "changed_at": "2025-08-15T05:20:00Z", "reason": "price_2025-08-14"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-15T05:25:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 22.0, "changed_at": "2025-08-15T05:25:00Z", "reason": "price_2025-08-14"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"})
        ],
        outputs=[
            """[
              {"adset_id":"101","new_bid":38.0,"roas_date":"2025-08-13"},
              {"adset_id":"104","new_bid":22.0,"roas_date":"2025-08-13"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t9",
        instruction="You must refresh creatives for ad set 102 by adding a new carousel ad named Autumn Carousel and making it live by activating the new ad and pausing ad 1103 at 2025-08-17T10:06:00Z with rationale format test. You must record run AR-20250817-03 (creative_refresh, 2025-08-17T10:05:00Z–2025-08-17T10:07:00Z, completed, input_ref adset_102_autumn_carousel, errors_json {}). After rotation, you must list the ads and report baseline insights for ad set 102 on 2025-08-13.",
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="create_ad", kwargs={"adset_id": "102", "name": "Autumn Carousel", "creative_type": "carousel",
                                             "start_date": "2025-08-17"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                                                         "rotated_at": "2025-08-17T10:06:00Z",
                                                         "rationale": "format test"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250817-03", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-17T10:05:00Z",
                                                         "ended_at": "2025-08-17T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset_102_autumn_carousel",
                                                         "errors_json": "{}"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"})
        ],
        outputs=[
            """[
              {"adset_id":"102","activated":"1119","paused":"1103"},
              {"automation_run":"AR-20250817-03"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t10",
        instruction="You must scale ad set 101 based on the 2025-08-13 performance. Using max_daily_budget_total from policy and ROAS=10.0 on 2025-08-13 as justification, you must deliver the following end state: daily_budget becomes 1050.0 effective at 2025-08-15T05:40:00Z; the budget change audit entry is written with change_id BC-8 and reason scale_up_2025-08-13 assuming the current highest change_id is BC-7 in the database; an automation run AR-20250815-10 of type scale_up is recorded for 2025-08-15T05:40:00Z–2025-08-15T05:42:00Z with status completed and input_ref adset_101_scale_up; include a spend summary for 2025-08-07 through 2025-08-13 and the insights snapshot for 2025-08-13.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "max_daily_budget_total"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 1050.0, "updated_at": "2025-08-15T05:40:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1050.0,
                                                     "changed_at": "2025-08-15T05:40:00Z",
                                                     "reason": "scale_up_2025-08-13"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250815-10", "run_type": "scale_up", "started_at": "2025-08-15T05:40:00Z",
                           "ended_at": "2025-08-15T05:42:00Z", "status": "completed", "input_ref": "adset_101_scale_up",
                           "errors_json": "{}"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"})
        ],
        outputs=[
            """[
              {"adset_id":"101","new_budget":1050.0,"expected_change_id":"BC-8"},
              {"automation_run":"AR-20250815-10"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t11",
        instruction="You must create and freeze a daily plan for 2025-08-16. You must deliver this end state: a plan plan_2025-08-16 exists with total_budget 1670.0, author planning_agent_v1, created_at 2025-08-16T01:59:00Z, checksum p16x1670, and allocations: ad set 101 with budget 950.0 using cost_cap bid_amount 35.0 and creative_type video, and ad set 112 with budget 720.0 using lowest_cost and creative_type image. You must validate against canonical strategies and creative types and against policy. You must be able to fetch the plan by date 2025-08-16 and you must record AR-20250816-01 (plan_create, 2025-08-16T01:58:00Z–2025-08-16T02:00:00Z, completed, input_ref plan_2025-08-16, errors_json {}).",
        actions=[
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 1670.0, "allocations": [
                {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                 "creative_type": "video"},
                {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost", "creative_type": "image"}
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-16", "date": "2025-08-16", "total_budget": 1670.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-16T01:59:00Z", "checksum": "p16x1670",
                           "allocations": [
                               {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                                "creative_type": "video"},
                               {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost",
                                "creative_type": "image"}
                           ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-16"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250816-01", "run_type": "plan_create", "started_at": "2025-08-16T01:58:00Z",
                           "ended_at": "2025-08-16T02:00:00Z", "status": "completed", "input_ref": "plan_2025-08-16",
                           "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"plan_id":"plan_2025-08-16","total_budget":1670.0},
              {"automation_run":"AR-20250816-01"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t12",
        instruction="You must remedy low ROAS for ad set 110 from the 2025-08-13 evaluation using min_roas_threshold_7d=1.5. You must deliver this end state: the daily_budget is 800.0 effective at 2025-08-17T09:00:00Z with a budget change logged using reason low_roas_2025-08-13; a new video ad named Android CTA Variant exists in ad set 110 with start_date 2025-08-17 and is active while ad 1114 is paused; the creative rotation is logged with rationale cta_test at 2025-08-17T09:01:00Z; and AR-20250817-02 (roas_mitigation, 2025-08-17T09:00:00Z–2025-08-17T09:03:00Z, completed, input_ref adset_110_roas_remedy, errors_json {}) is recorded. You must be able to list the ads for ad set 110 after these changes.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "110", "new_budget": 800.0, "updated_at": "2025-08-17T09:00:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0,
                                                     "changed_at": "2025-08-17T09:00:00Z",
                                                     "reason": "low_roas_2025-08-13"}),
            Action(name="create_ad", kwargs={"adset_id": "110", "name": "Android CTA Variant", "creative_type": "video",
                                             "start_date": "2025-08-17"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1114"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "110", "old_ad_id": "1114", "new_ad_id": "1119",
                                                         "rotated_at": "2025-08-17T09:01:00Z",
                                                         "rationale": "cta_test"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250817-02", "run_type": "roas_mitigation",
                                                         "started_at": "2025-08-17T09:00:00Z",
                                                         "ended_at": "2025-08-17T09:03:00Z", "status": "completed",
                                                         "input_ref": "adset_110_roas_remedy", "errors_json": "{}"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "110"})
        ],
        outputs=[
            """[
              {"adset_id":"110","new_budget":800.0,"activated_ad":"1119","paused_ad":"1114"},
              {"automation_run":"AR-20250817-02"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t13",
        instruction=(
            "You prioritize video engagement for ad set 108 using the 2025-08-13 baseline. "
            "You deliver this end state: ad 1112 is active and ad 1111 is paused at 2025-08-16T09:00:00Z; "
            "the rotation is logged with rationale video_preference; "
            "AR-20250816-02 (creative_rotation, 2025-08-16T09:00:00Z–2025-08-16T09:02:00Z, completed, "
            "input_ref adset_108_video_shift) is recorded; "
            "and you report CTR and an insights snapshot for 2025-08-13 plus the updated ad list."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),

            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1112", "ad_id_to_pause": "1111"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "108", "old_ad_id": "1111", "new_ad_id": "1112",
                                                         "rotated_at": "2025-08-16T09:00:00Z",
                                                         "rationale": "video_preference"}),

            Action(name="create_automation_run", kwargs={"run_id": "AR-20250816-02", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-16T09:00:00Z",
                                                         "ended_at": "2025-08-16T09:02:00Z", "status": "completed",
                                                         "input_ref": "adset_108_video_shift", "errors_json": "{}"}),

            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"})
        ],
        outputs=[
            """[
              {"adset_id":"108","activated":"1112","paused":"1111"},
              {"insights_date":"2025-08-13","ctr_reported":true},
              {"updated_ads_list":true},
              {"automation_run":"AR-20250816-02"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t14",
        instruction=(
            "You refresh creative for ad set 101 leveraging the 2025-08-13 baseline. "
            "You deliver this end state: a new image ad named 'Smartphone X Image v2' exists in ad set 101 with start_date 2025-08-17 and is active; "
            "ad 1101 is paused at 2025-08-17T11:00:00Z; the rotation is logged with rationale freshness; "
            "AR-20250817-04 (creative_refresh, 2025-08-17T10:59:00Z–2025-08-17T11:01:00Z, completed, input_ref adset_101_image_refresh) is recorded; "
            "and you provide the updated ad list and ROAS for 2025-08-13."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),

            Action(name="create_ad",
                   kwargs={"adset_id": "101", "name": "Smartphone X Image v2", "creative_type": "image",
                           "start_date": "2025-08-17"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1101"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1119",
                                                         "rotated_at": "2025-08-17T11:00:00Z",
                                                         "rationale": "freshness"}),

            Action(name="create_automation_run", kwargs={"run_id": "AR-20250817-04", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-17T10:59:00Z",
                                                         "ended_at": "2025-08-17T11:01:00Z", "status": "completed",
                                                         "input_ref": "adset_101_image_refresh", "errors_json": "{}"}),

            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"})
        ],
        outputs=[
            """[
              {"adset_id":"101","activated":"1119","paused":"1101"},
              {"updated_ads_list":true,"roas_date":"2025-08-13"},
              {"automation_run":"AR-20250817-04"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t15",
        instruction="You must scale ad set 105 based on strong performance on 2025-08-13 while respecting policy rounding. You must deliver this end state: daily_budget becomes 820.0 effective at 2025-08-16T08:00:00Z using budget_rounding_unit=10, the change is logged with reason scale_up_2025-08-13, AR-20250816-03 (scale_up, 2025-08-16T08:00:00Z–2025-08-16T08:02:00Z, completed, input_ref adset_105_scale_up, errors_json {}) is recorded, and you provide spend for 2025-08-07 through 2025-08-13 and the insights snapshot for 2025-08-13.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "105", "new_budget": 820.0, "updated_at": "2025-08-16T08:00:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 820.0,
                                                     "changed_at": "2025-08-16T08:00:00Z",
                                                     "reason": "scale_up_2025-08-13"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250816-03", "run_type": "scale_up", "started_at": "2025-08-16T08:00:00Z",
                           "ended_at": "2025-08-16T08:02:00Z", "status": "completed", "input_ref": "adset_105_scale_up",
                           "errors_json": "{}"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "105", "date": "2025-08-13"})
        ],
        outputs=[
            """[
              {"adset_id":"105","new_budget":820.0},
              {"automation_run":"AR-20250816-03"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t16",
        instruction=(
            "You have to Mitigate 2025-08-13 underperformers (threshold 1.5) in a policy-compliant, audited way. "
            "Scale back ad set 110 to daily_budget 900.0 at 2025-08-19T11:00:00Z and log the change with reason "
            "underperforming_2025-08-13; tighten ad set 111 cost_cap bid to 2.0 at 11:02:00Z with the same reason; "
            "verify after each modification. Record a concise run (AR-20250819-06, mitigation_apply, "
            "11:00:00Z–11:05:00Z, completed, input_ref underperforming_2025-08-13)."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "110", "new_budget": 900.0, "updated_at": "2025-08-19T11:00:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 900.0,
                           "changed_at": "2025-08-19T11:00:00Z", "reason": "underperforming_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.0,
                           "updated_at": "2025-08-19T11:02:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 2.5, "new_bid": 2.0, "changed_at": "2025-08-19T11:02:00Z",
                           "reason": "underperforming_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-06", "run_type": "mitigation_apply",
                                                         "started_at": "2025-08-19T11:00:00Z",
                                                         "ended_at": "2025-08-19T11:05:00Z", "status": "completed",
                                                         "input_ref": "underperforming_2025-08-13",
                                                         "errors_json": "{}"}),
        ],
        outputs=[
            """[
              {"adset_id":"110","final_budget":900.0},
              {"adset_id":"111","final_bid_strategy":"cost_cap","final_bid_amount":2.0},
              {"automation_run":"AR-20250819-06"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t17",
        instruction=(
            "You have to Perform a clean creative rotation for ad set 102 using canonical types at 2025-08-24T10:06:00Z: "
            "activate carousel 1104, pause image 1103, rationale format_test_carousel. "
            "Audit with AR-20250824-06 (creative_rotation, 10:05:00Z–10:07:00Z, completed, input_ref adset:102|1103->1104) "
            "and verify ads after rotation."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250824-06", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-24T10:05:00Z",
                                                         "ended_at": "2025-08-24T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset:102|1103->1104", "errors_json": "{}"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-24T10:06:00Z", "rationale": "format_test_carousel"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
        ],
        outputs=[
            """[
          {"adset_id":"102","activated":"1104","paused":"1103"},
          {"automation_run":"AR-20250824-06"}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t18",
        instruction="You must true-up ad set 104 to match the frozen plan for 2025-08-13. You must deliver this end state: ad set 104 has daily_budget 750.0 and bid_strategy cost_cap with bid_amount 22.0 effective at 2025-08-17T12:40:00Z–2025-08-17T12:41:00Z, both changes logged with reason plan_2025-08-13_true_up, and AR-20250817-07 (plan_true_up, 2025-08-17T12:40:00Z–2025-08-17T12:42:00Z, completed, input_ref plan_2025-08-13, errors_json {}) recorded. You must read the plan and the specific allocation for ad set 104 before performing the updates.",
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "104", "new_budget": 750.0, "updated_at": "2025-08-17T12:40:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0,
                                                     "changed_at": "2025-08-17T12:40:00Z",
                                                     "reason": "plan_2025-08-13_true_up"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-17T12:41:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 22.0, "changed_at": "2025-08-17T12:41:00Z", "reason": "plan_2025-08-13_true_up"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250817-07", "run_type": "plan_true_up", "started_at": "2025-08-17T12:40:00Z",
                           "ended_at": "2025-08-17T12:42:00Z", "status": "completed", "input_ref": "plan_2025-08-13",
                           "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"})
        ],
        outputs=[
            """[
              {"adset_id":"104","new_budget":750.0,"strategy":"cost_cap","bid_amount":22.0},
              {"automation_run":"AR-20250817-07"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t19",
        instruction=(
            "You have to Mitigate underperformers detected on 2025-08-13 by scaling back 110 and tightening 111 while keeping cost_cap. "
            "Set 110 daily_budget to 920.0 at 11:10:00Z and 111 bid_amount to 2.1 at 11:12:00Z with reason underperforming_2025-08-13, "
            "verify after each, and record AR-20250827-06 (mitigation_apply, 11:10:00Z–11:13:00Z, completed, input_ref underperf_2025-08-13_pair_b)."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "110", "new_budget": 920.0, "updated_at": "2025-08-27T11:10:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 920.0,
                           "changed_at": "2025-08-27T11:10:00Z", "reason": "underperforming_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.1,
                           "updated_at": "2025-08-27T11:12:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 2.5, "new_bid": 2.1, "changed_at": "2025-08-27T11:12:00Z",
                           "reason": "underperforming_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            Action(name="create_automation_run", kwargs={"run_id": "AR-20250827-06", "run_type": "mitigation_apply",
                                                         "started_at": "2025-08-27T11:10:00Z",
                                                         "ended_at": "2025-08-27T11:13:00Z", "status": "completed",
                                                         "input_ref": "underperf_2025-08-13_pair_b",
                                                         "errors_json": "{}"}),
        ],
        outputs=[
            """[
          {"adset_id":"110","final_budget":920.0},
          {"adset_id":"111","final_bid_strategy":"cost_cap","final_bid_amount":2.1},
          {"automation_run":"AR-20250827-06"}
        ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t20",
        instruction=(
            "You have to Create and validate a plan for 2025-08-16 with two allocations, then confirm retrieval. "
            "The plan must be plan_2025-08-16 with total_budget 1670.0, author planning_agent_v1, "
            "created_at 2025-08-16T01:59:00Z, checksum p16x1670, and allocations: "
            "ad set 101 (950.0, cost_cap bid 35.0, creative video) and ad set 112 (720.0, lowest_cost, creative image). "
            "Keep a brief creation audit (AR-20250816-01, plan_create, 01:58:00Z–02:00:00Z, completed, input_ref plan_2025-08-16)."
        ),
        actions=[
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 1670.0, "allocations": [
                {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                 "creative_type": "video"},
                {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost", "creative_type": "image"}
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-16", "date": "2025-08-16", "total_budget": 1670.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-16T01:59:00Z", "checksum": "p16x1670",
                           "allocations": [
                               {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                                "creative_type": "video"},
                               {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost",
                                "creative_type": "image"}
                           ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-16"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250816-01", "run_type": "plan_create", "started_at": "2025-08-16T01:58:00Z",
                           "ended_at": "2025-08-16T02:00:00Z", "status": "completed", "input_ref": "plan_2025-08-16",
                           "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"plan_id":"plan_2025-08-16","total_budget":1670.0},
              {"automation_run":"AR-20250816-01"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t21",
        instruction=(
            "You have to Use 2025-08-13 Electronics viewership and week-of-2025-08-07 sales as context to pace ad set 101 conservatively. "
            "Top up its daily budget to 960.0 at 2025-08-19T09:15:00Z, log with reason pacing_electronics_2025-08-13, "
            "verify immediately after the change, and keep a small audit window "
            "(AR-20250819-08, pacing_apply, 09:15:00Z–09:16:00Z, completed, input_ref adset_101_pacing)."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_weekly_sales_by_category", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 960.0, "updated_at": "2025-08-19T09:15:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 960.0,
                           "changed_at": "2025-08-19T09:15:00Z", "reason": "pacing_electronics_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-08", "run_type": "pacing_apply",
                                                         "started_at": "2025-08-19T09:15:00Z",
                                                         "ended_at": "2025-08-19T09:16:00Z",
                                                         "status": "completed", "input_ref": "adset_101_pacing",
                                                         "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"101","final_daily_budget":960.0},{"automation_run":"AR-20250819-08"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t22",
        instruction="You must enforce bidding policy for ad set 111 using 2025-08-13 baselines. You must deliver this end state: ad set 111 uses cost_cap with bid_amount 2.5 effective at 2025-08-17T12:20:00Z and this change is logged with reason policy_enforcement_2025-08-13; AR-20250817-10 (bid_policy_true_up, 2025-08-17T12:20:00Z–2025-08-17T12:22:00Z, completed, input_ref adset_111_bid_enforcement, errors_json {}) recorded. You must reference max_bid_amount and canonical bid strategies and include ROAS for 2025-08-13.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5,
                           "updated_at": "2025-08-17T12:20:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5,
                           "new_bid": 2.5, "changed_at": "2025-08-17T12:20:00Z",
                           "reason": "policy_enforcement_2025-08-13"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250817-10", "run_type": "bid_policy_true_up",
                                                         "started_at": "2025-08-17T12:20:00Z",
                                                         "ended_at": "2025-08-17T12:22:00Z", "status": "completed",
                                                         "input_ref": "adset_111_bid_enforcement",
                                                         "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"})
        ],
        outputs=[
            """[
              {"adset_id":"111","strategy":"cost_cap","bid_amount":2.5},
              {"automation_run":"AR-20250817-10"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t23",
        instruction="You must create and freeze a daily plan for 2025-08-18. You must deliver this end state: a plan plan_2025-08-18 exists with total_budget 2380.0, author planning_agent_v1, created_at 2025-08-18T01:59:00Z, checksum p18x2380, and allocations: ad set 102 with budget 600.0 using lowest_cost and creative_type carousel, ad set 110 with budget 1000.0 using lowest_cost and creative_type video, ad set 101 with budget 780.0 using cost_cap bid_amount 35.0 and creative_type video. You must validate against canonical strategies and creative types and against policy. You must be able to fetch the plan and you must record AR-20250818-02 (plan_create, 2025-08-18T01:58:00Z–2025-08-18T02:00:00Z, completed, input_ref plan_2025-08-18, errors_json {}).",
        actions=[
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 2380.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "carousel"},
                {"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost", "creative_type": "video"},
                {"adset_id": "101", "budget": 780.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                 "creative_type": "video"}
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-18", "date": "2025-08-18", "total_budget": 2380.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-18T01:59:00Z", "checksum": "p18x2380",
                           "allocations": [
                               {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                                "creative_type": "carousel"},
                               {"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost",
                                "creative_type": "video"},
                               {"adset_id": "101", "budget": 780.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                                "creative_type": "video"}
                           ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-18"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-02", "run_type": "plan_create", "started_at": "2025-08-18T01:58:00Z",
                           "ended_at": "2025-08-18T02:00:00Z", "status": "completed", "input_ref": "plan_2025-08-18",
                           "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"plan_id":"plan_2025-08-18","total_budget":2380.0},
              {"automation_run":"AR-20250818-02"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t24",
        instruction=(
            "You have to Add a new carousel to ad set 102 and make it live: create 'Back to School Carousel' (start_date 2025-08-24), "
            "activate the new ad and pause 1103 at 10:08:00Z (rationale school_season_test). "
            "Record AR-20250824-07 (creative_refresh, 10:07:00Z–10:09:00Z, completed, input_ref adset_102_b2s) and verify ads."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="create_ad",
                   kwargs={"adset_id": "102", "name": "Back to School Carousel", "creative_type": "carousel",
                           "start_date": "2025-08-24"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250824-07", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-24T10:07:00Z",
                                                         "ended_at": "2025-08-24T10:09:00Z", "status": "completed",
                                                         "input_ref": "adset_102_b2s", "errors_json": "{}"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                           "rotated_at": "2025-08-24T10:08:00Z", "rationale": "school_season_test"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
        ],
        outputs=[
            """[
          {"adset_id":"102","activated":"1119","paused":"1103"},
          {"automation_run":"AR-20250824-07"}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t25",
        instruction=(
            "You rebalance Electronics budgets across ad sets 101, 108, and 112 in a policy-compliant, audited flow. "
            "Use spend from 2025-08-07 to 2025-08-13 and ROAS on 2025-08-13 as context, then set the final budgets explicitly to "
            "101→860.0, 108→780.0, 112→680.0 effective 2025-08-18T10:00:00Z. "
            "Capture old values from pre-change reads and log each change with reason electronics_three_way_rebalance_2025-08-13. "
            "Record a concise category_rebalance run AR-20250818-04 started at 2025-08-18T10:00:00Z and end it at 2025-08-18T10:03:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),

            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="create_automation_run", kwargs={
                "run_id": "AR-20250818-04",
                "run_type": "category_rebalance",
                "started_at": "2025-08-18T10:00:00Z",
                "input_ref": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 860.0, "updated_at": "2025-08-18T10:00:00Z"}),
            Action(name="log_budget_change", kwargs={
                "adset_id": "101",
                "old_budget": 920.0,
                "new_budget": 860.0,
                "changed_at": "2025-08-18T10:00:00Z",
                "reason": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="update_adset_budget",
                   kwargs={"adset_id": "108", "new_budget": 780.0, "updated_at": "2025-08-18T10:00:00Z"}),
            Action(name="log_budget_change", kwargs={
                "adset_id": "108",
                "old_budget": 780.0,
                "new_budget": 780.0,
                "changed_at": "2025-08-18T10:00:00Z",
                "reason": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 680.0, "updated_at": "2025-08-18T10:00:00Z"}),
            Action(name="log_budget_change", kwargs={
                "adset_id": "112",
                "old_budget": 700.0,
                "new_budget": 680.0,
                "changed_at": "2025-08-18T10:00:00Z",
                "reason": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-04", "ended_at": "2025-08-18T10:03:00Z"})
        ],
        outputs=[
            """[
              {"adset_id":"101","new_budget":860.0},
              {"adset_id":"108","new_budget":780.0},
              {"adset_id":"112","new_budget":680.0},
              {"automation_run":"AR-20250818-04"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t26",
        instruction=(
            "You have to Bring ad set 103 back into policy per the approved baseline plan_2025-08-13 and observed 2025-08-13 ROAS. "
            "Set daily_budget to 980.0 effective 2025-08-19T04:10:00Z and switch to cost_cap bid 15.0 at 04:12:00Z, "
            "using the plan_id as the reason and verifying after each change. Record a compact mitigation audit "
            "(AR-20250819-09, underperformance_mitigation, 04:10:00Z–04:13:00Z, completed, input_ref adset_103_2025-08-13)."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            Action(name="update_adset_budget",
                   kwargs={"adset_id": "103", "new_budget": 980.0, "updated_at": "2025-08-19T04:10:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 980.0,
                           "changed_at": "2025-08-19T04:10:00Z", "reason": "plan_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 15.0,
                           "updated_at": "2025-08-19T04:12:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 15.0, "changed_at": "2025-08-19T04:12:00Z",
                           "reason": "plan_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250819-09", "run_type": "underperformance_mitigation",
                           "started_at": "2025-08-19T04:10:00Z", "ended_at": "2025-08-19T04:13:00Z",
                           "status": "completed", "input_ref": "adset_103_2025-08-13", "errors_json": "{}"})
        ],
        outputs=[
            '{"adset_id":"103","new_budget":980.0,"new_strategy":"cost_cap","new_bid_amount":15.0}',
            '{"automation_run":"AR-20250819-09"}'
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t27",
        instruction=(
            "You have to Create and apply a two-line plan for 2025-08-24 across 102 and 112. "
            "Plan plan_2025-08-24b (author planning_agent_v1, created_at 2025-08-24T01:58:50Z, checksum p24b1360) totals 1360.0: "
            "102 → 600.0 (lowest_cost, image), 112 → 760.0 (lowest_cost, image). Freeze (AR-20250824-10, 01:58:50Z–02:00:10Z). "
            "Apply both budgets at 02:05:00Z with reason plan_2025-08-24b and verify."
        ),
        actions=[
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 1360.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-24b", "date": "2025-08-24", "total_budget": 1360.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-24T01:58:50Z",
                           "checksum": "p24b1360", "allocations": [
                           {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-24"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250824-10", "run_type": "plan_freeze",
                                                         "started_at": "2025-08-24T01:58:50Z",
                                                         "ended_at": "2025-08-24T02:00:10Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-24b"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 600.0, "updated_at": "2025-08-24T02:05:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0,
                           "changed_at": "2025-08-24T02:05:00Z", "reason": "plan_2025-08-24b"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 760.0, "updated_at": "2025-08-24T02:05:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 760.0,
                           "changed_at": "2025-08-24T02:05:00Z", "reason": "plan_2025-08-24b"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
        ],
        outputs=[
            """[
          {"plan_id":"plan_2025-08-24b","applied_to":["102","112"]},
          {"freeze_run":"AR-20250824-10"}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t28",
        instruction=(
            "You take a monitoring snapshot at 2025-08-18T11:20:00Z that reflects recent plan execution and baseline performance. "
            "Summarize recent plan_freeze reliability and include a lightweight KPI echo for 2025-08-13 (ROAS and CTR for ad set 101). "
            "Persist this as a completed automation run AR-20250818-10 (run_type monitoring_snapshot) with input_ref "
            "success_rate_percent=100.0;snapshot_runs=2, and then confirm the snapshot is present."
        ),
        actions=[
            Action(name="get_automation_run_history", kwargs={"run_type": "plan_freeze", "limit": 2}),

            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),

            Action(name="create_automation_run", kwargs={
                "run_id": "AR-20250818-10",
                "run_type": "monitoring_snapshot",
                "started_at": "2025-08-18T11:20:00Z",
                "ended_at": "2025-08-18T11:20:00Z",
                "status": "completed",
                "input_ref": "success_rate_percent=100.0;snapshot_runs=2",
                "errors_json": "{}"
            }),

            Action(name="get_automation_run_history", kwargs={"run_type": "monitoring_snapshot", "limit": 1})
        ],
        outputs=[
            """[
          {"monitoring_snapshot_id":"AR-20250818-10","status":"completed"},
          {"snapshot_runs":2,"success_rate":100.0}
        ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t29",
        instruction=(
            "You have to Apply a small rounding-compliant top-up to ad set 101. "
            "At 2025-08-24T09:40:00Z set daily_budget to 960.0 using budget_rounding_unit, log reason rounding_topup_2025-08-24, verify, "
            "and record AR-20250824-14 (budget_rebalance, 09:40:00Z–09:41:00Z, completed, input_ref adset_101_rounding_topup)."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 960.0, "updated_at": "2025-08-24T09:40:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 960.0,
                           "changed_at": "2025-08-24T09:40:00Z", "reason": "rounding_topup_2025-08-24"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250824-14", "run_type": "budget_rebalance",
                                                         "started_at": "2025-08-24T09:40:00Z",
                                                         "ended_at": "2025-08-24T09:41:00Z", "status": "completed",
                                                         "input_ref": "adset_101_rounding_topup", "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"101","final_daily_budget":960.0},{"automation_run":"AR-20250824-14"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t30",
        instruction="You must pause the Q3 Brand Awareness Push campaign and optimize its primary ad set. You must deliver this end state: campaign Q3 Brand Awareness Push has status paused; ad set 103 switches to cost_cap with bid_amount 20.0 at 2025-08-18T11:20:00Z, logged with reason brand_efficiency_2025-08-13; AR-20250818-09 (brand_pause_opt, 2025-08-18T11:19:00Z–2025-08-18T11:21:00Z, completed, input_ref brand_pause_opt_2025-08-18, errors_json {}) recorded; and campaign ad sets are listed.",
        actions=[
            Action(name="get_campaign_by_name", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="update_campaign_status", kwargs={"campaign_id": "2", "status": "paused"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "2"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 20.0,
                           "updated_at": "2025-08-18T11:20:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 20.0, "changed_at": "2025-08-18T11:20:00Z",
                           "reason": "brand_efficiency_2025-08-13"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250818-09", "run_type": "brand_pause_opt",
                                                         "started_at": "2025-08-18T11:19:00Z",
                                                         "ended_at": "2025-08-18T11:21:00Z", "status": "completed",
                                                         "input_ref": "brand_pause_opt_2025-08-18",
                                                         "errors_json": "{}"}),
            Action(name="get_adsets_by_campaign_id", kwargs={"campaign_id": "2"})
        ],
        outputs=[
            """[
              {"campaign_id":"2","status":"paused"},
              {"adset_id":"103","strategy":"cost_cap","bid_amount":20.0},
              {"automation_run":"AR-20250818-09"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t31",
        instruction="You refresh creative mix in the Summer T-Shirt ad set. You inspect ads in ad set 102, then you activate 1104 and pause 1103 as a rotation, logging the rotation with rationale cta_focus at 2025-08-18T11:30:00Z. You record AR-20250818-10 as a completed creative_rotation run with started_at 2025-08-18T11:30:00Z, ended_at 2025-08-18T11:31:00Z, input_ref adset:102|rotation:1103>1104, errors_json {}.",
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                                                         "rotated_at": "2025-08-18T11:30:00Z",
                                                         "rationale": "cta_focus"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250818-10", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-18T11:30:00Z",
                                                         "ended_at": "2025-08-18T11:31:00Z", "status": "completed",
                                                         "input_ref": "adset:102|rotation:1103>1104",
                                                         "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"adset_id":"102","rotated_from":"1103","to":"1104"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t32",
        instruction=(
            "You have to Run a creative refresh for ad set 102 by adding a new carousel ad named Autumn Carousel (start_date 2025-08-19), "
            "then activating the new ad and pausing 1103 at 10:06:00Z with rationale format_test. "
            "Use a minimal audit window (AR-20250819-10, creative_refresh, 10:05:00Z–10:07:00Z, completed, "
            "input_ref adset_102_autumn_carousel) and verify ads after rotation."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="create_ad", kwargs={"adset_id": "102", "name": "Autumn Carousel", "creative_type": "carousel",
                                             "start_date": "2025-08-19"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-10", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-19T10:05:00Z",
                                                         "ended_at": "2025-08-19T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset_102_autumn_carousel",
                                                         "errors_json": "{}"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                           "rotated_at": "2025-08-19T10:06:00Z", "rationale": "format_test"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=[
            """[
              {"adset_id":"102","activated":"1119","paused":"1103"},
              {"automation_run":"AR-20250819-10"}
            ]"""
        ]
    ),

    Task(
        annotator="v6",
        user_id="sma_t33",
        instruction=(
            "You have to Scale ad set 112 responsibly under policy, using rounding and max limits. "
            "Set its daily_budget to 820.0 effective 2025-08-19T11:50:00Z, log with reason scale_up_policy_2025-08-13, "
            "verify the change, and keep a short run (AR-20250819-12, scale_up, 11:50:00Z–11:52:00Z, completed, "
            "input_ref adset_112_scale_up)."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "max_daily_budget_total"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 820.0, "updated_at": "2025-08-19T11:50:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 820.0,
                           "changed_at": "2025-08-19T11:50:00Z", "reason": "scale_up_policy_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-12", "run_type": "scale_up",
                                                         "started_at": "2025-08-19T11:50:00Z",
                                                         "ended_at": "2025-08-19T11:52:00Z", "status": "completed",
                                                         "input_ref": "adset_112_scale_up", "errors_json": "{}"}),
        ],
        outputs=[
            """[
              {"adset_id":"112","new_budget":820.0},
              {"automation_run":"AR-20250819-12"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t34",
        instruction=(
            "You have to Audit and nudge ad set 104 in light of 2025-08-13 performance while keeping creatives intact. "
            "Raise its cost_cap bid to 22.0 effective 2025-08-19T05:25:00Z, log with reason light_scale_2025-08-13, "
            "verify after the update, and record a short run (AR-20250819-13, strategy_apply, 05:25:00Z–05:26:00Z, completed, "
            "input_ref adset_104_scale)."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-19T05:25:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 20.0, "new_bid": 22.0, "changed_at": "2025-08-19T05:25:00Z",
                           "reason": "light_scale_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-13", "run_type": "strategy_apply",
                                                         "started_at": "2025-08-19T05:25:00Z",
                                                         "ended_at": "2025-08-19T05:26:00Z", "status": "completed",
                                                         "input_ref": "adset_104_scale", "errors_json": "{}"}),
        ],
        outputs=[
            '[{"adset_id":"104","final_bid_strategy":"cost_cap","final_bid_amount":22.0},{"automation_run":"AR-20250819-13"}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t35",
        instruction="You must apply the plan for 2025-08-13 to ad sets 101 and 112 only. You must deliver this end state: ad set 101 daily_budget 950.0 and cost_cap bid_amount 35.0; ad set 112 daily_budget 700.0 with lowest_cost; all effective at 2025-08-18T12:10:00Z–2025-08-18T12:12:00Z; all changes logged with reason partial_plan_apply_2025-08-13; AR-20250818-13 (budget_apply, 2025-08-18T12:10:00Z–2025-08-18T12:13:00Z, completed, input_ref plan_2025-08-13_partial, errors_json {}) recorded.",
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 950.0, "updated_at": "2025-08-18T12:10:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0,
                                                     "changed_at": "2025-08-18T12:10:00Z",
                                                     "reason": "partial_plan_apply_2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0,
                           "updated_at": "2025-08-18T12:11:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0,
                           "new_bid": 35.0, "changed_at": "2025-08-18T12:11:00Z",
                           "reason": "partial_plan_apply_2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 700.0, "updated_at": "2025-08-18T12:12:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 700.0,
                                                     "changed_at": "2025-08-18T12:12:00Z",
                                                     "reason": "partial_plan_apply_2025-08-13"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-13", "run_type": "budget_apply", "started_at": "2025-08-18T12:10:00Z",
                           "ended_at": "2025-08-18T12:13:00Z", "status": "completed",
                           "input_ref": "plan_2025-08-13_partial", "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"adset_id":"101","budget":950.0,"strategy":"cost_cap","bid_amount":35.0},
              {"adset_id":"112","budget":700.0},
              {"automation_run":"AR-20250818-13"}
            ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t36",
        instruction=(
            "You have to Draft and freeze a compact plan for 2025-08-25 with two allocations and confirm retrieval. "
            "Plan plan_2025-08-25b totals 1360.0 (author planning_agent_v1, created_at 2025-08-25T01:59:30Z, checksum p25b1360): "
            "102 → 600.0 (lowest_cost, image), 112 → 760.0 (lowest_cost, image). "
            "Include AR-20250825-05 (plan_create, 01:59:00Z–02:00:00Z, completed)."
        ),
        actions=[
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 1360.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-25b", "date": "2025-08-25", "total_budget": 1360.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-25T01:59:30Z",
                           "checksum": "p25b1360", "allocations": [
                           {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-25"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250825-05", "run_type": "plan_create",
                                                         "started_at": "2025-08-25T01:59:00Z",
                                                         "ended_at": "2025-08-25T02:00:00Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-25b", "errors_json": "{}"}),
        ],
        outputs=[
            """[
          {"plan_id":"plan_2025-08-25b","total_budget":1360.0},
          {"automation_run":"AR-20250825-05"}
        ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t37",
        instruction=(
            "You have to Mitigate underperformance conservatively for ad set 110 detected on 2025-08-13 (threshold 1.5). "
            "Reduce daily_budget to 950.0 at 2025-08-19T11:10:00Z, log the change with reason underperforming_2025-08-13, "
            "verify the new state, and record a brief mitigation_apply run "
            "(AR-20250819-16, 11:10:00Z–11:11:00Z, completed, input_ref adset_110_mitigation)."
        ),
        actions=[
            Action(name="find_underperforming_adsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "110", "new_budget": 950.0, "updated_at": "2025-08-19T11:10:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 950.0,
                           "changed_at": "2025-08-19T11:10:00Z", "reason": "underperforming_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-16", "run_type": "mitigation_apply",
                                                         "started_at": "2025-08-19T11:10:00Z",
                                                         "ended_at": "2025-08-19T11:11:00Z", "status": "completed",
                                                         "input_ref": "adset_110_mitigation", "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"110","final_budget":950.0},{"automation_run":"AR-20250819-16"}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t38",
        instruction=(
            "You have to Tighten ad set 111 bidding under policy while maintaining cost_cap. "
            "Lower bid_amount to 2.2 effective 2025-08-19T11:20:00Z with reason underperforming_2025-08-13, verify immediately, "
            "and record a compact strategy_apply window (AR-20250819-17, 11:20:00Z–11:21:00Z, completed, input_ref adset_111_tighten)."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.2,
                           "updated_at": "2025-08-19T11:20:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 2.5, "new_bid": 2.2, "changed_at": "2025-08-19T11:20:00Z",
                           "reason": "underperforming_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-17", "run_type": "strategy_apply",
                                                         "started_at": "2025-08-19T11:20:00Z",
                                                         "ended_at": "2025-08-19T11:21:00Z", "status": "completed",
                                                         "input_ref": "adset_111_tighten", "errors_json": "{}"}),
        ],
        outputs=[
            '[{"adset_id":"111","final_bid_strategy":"cost_cap","final_bid_amount":2.2},{"automation_run":"AR-20250819-17"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t39",
        instruction="You must scale down Mobile performance spend. You must deliver this end state: ad set 110 daily_budget 900.0 at 2025-08-18T12:50:00Z logged with reason mobile_scale_down_2025-08-13; AR-20250818-16 (scale_down, 2025-08-18T12:50:00Z–2025-08-18T12:52:00Z, completed, input_ref adset_110_scale_down, errors_json {}) recorded; and you must list its ads and ROAS for 2025-08-13.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "110"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "110", "new_budget": 900.0, "updated_at": "2025-08-18T12:50:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 900.0,
                                                     "changed_at": "2025-08-18T12:50:00Z",
                                                     "reason": "mobile_scale_down_2025-08-13"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-16", "run_type": "scale_down", "started_at": "2025-08-18T12:50:00Z",
                           "ended_at": "2025-08-18T12:52:00Z", "status": "completed",
                           "input_ref": "adset_110_scale_down", "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"adset_id":"110","new_budget":900.0},
              {"automation_run":"AR-20250818-16"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t40",
        instruction="You must correct brand video inefficiency. You must deliver this end state: ad set 103 daily_budget 950.0 and cost_cap bid_amount 18.0 effective at 2025-08-18T13:00:00Z–2025-08-18T13:02:00Z; all changes logged with reason brand_video_efficiency_fix_2025-08-13; AR-20250818-17 (brand_efficiency_fix, 2025-08-18T13:00:00Z–2025-08-18T13:03:00Z, completed, input_ref adset_103_brand_fix, errors_json {}) recorded; and you must provide the 2025-08-13 insights snapshot.",
        actions=[
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "103", "new_budget": 950.0, "updated_at": "2025-08-18T13:00:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 950.0,
                                                     "changed_at": "2025-08-18T13:00:00Z",
                                                     "reason": "brand_video_efficiency_fix_2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 18.0,
                           "updated_at": "2025-08-18T13:02:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 18.0, "changed_at": "2025-08-18T13:02:00Z",
                           "reason": "brand_video_efficiency_fix_2025-08-13"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250818-17", "run_type": "brand_efficiency_fix",
                                                         "started_at": "2025-08-18T13:00:00Z",
                                                         "ended_at": "2025-08-18T13:03:00Z", "status": "completed",
                                                         "input_ref": "adset_103_brand_fix", "errors_json": "{}"})
        ],
        outputs=[
            """[
              {"adset_id":"103","new_budget":950.0,"strategy":"cost_cap","bid_amount":18.0},
              {"automation_run":"AR-20250818-17"}
            ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t41",
        instruction="You will tighten bidding for ad set 104 using policy rules. Confirm canonical bid strategies, read the current ad set to capture its existing strategy and bid, and assess performance on 2025-08-13. Apply a tighter cost_cap by setting bid_amount to 18.0 effective at 2025-08-18T14:04:00Z. Record the strategy change using the fetched prior values and reason ctr_tighten_2025-08-13. Verify the new ad set state afterward.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 18.0,
                           "updated_at": "2025-08-18T14:04:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 18.0, "changed_at": "2025-08-18T14:04:00Z", "reason": "ctr_tighten_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"})
        ],
        outputs=["adset=104 strategy=cost_cap bid=18.0 changed_at=2025-08-18T14:04:00Z reason=ctr_tighten_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t42",
        instruction="You will retune bidding for ad set 106 in line with policy. Confirm canonical bid strategies, read the ad set to capture its current values, and evaluate its 2025-08-13 performance. Switch the bidding to bid_cap with bid_amount 17.0 effective at 2025-08-18T14:08:00Z. Record the strategy change using the fetched prior values and reason performance_rebalance_2025-08-13. Verify the updated state.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "106", "bid_strategy": "bid_cap", "bid_amount": 17.0,
                           "updated_at": "2025-08-18T14:08:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "bid_cap", "old_bid": 18.0,
                           "new_bid": 17.0, "changed_at": "2025-08-18T14:08:00Z",
                           "reason": "performance_rebalance_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"})
        ],
        outputs=[
            "adset=106 strategy=bid_cap bid=17.0 changed_at=2025-08-18T14:08:00Z reason=performance_rebalance_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t43",
        instruction="You will modestly tighten bidding for ad set 108 per policy. Confirm canonical bid strategies, read the current ad set values, and consider its 2025-08-13 results. Keep cost_cap but reduce bid_amount to 40.0 effective at 2025-08-18T14:11:00Z. Log the strategy change with the fetched old values and reason cost_cap_tighten_2025-08-13. Verify the new state.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 40.0,
                           "updated_at": "2025-08-18T14:11:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0,
                           "new_bid": 40.0, "changed_at": "2025-08-18T14:11:00Z",
                           "reason": "cost_cap_tighten_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"})
        ],
        outputs=[
            "adset=108 strategy=cost_cap bid=40.0 changed_at=2025-08-18T14:11:00Z reason=cost_cap_tighten_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t44",
        instruction="You will reduce over-aggressive bidding for ad set 111. Confirm canonical strategies, read the ad set state, and factor its 2025-08-13 results. Maintain cost_cap but lower bid_amount to 2.2 effective at 2025-08-18T14:13:00Z. Log the change using the fetched previous values with reason cap_refinement_2025-08-13 and verify the new state.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.2,
                           "updated_at": "2025-08-18T14:13:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5,
                           "new_bid": 2.2, "changed_at": "2025-08-18T14:13:00Z",
                           "reason": "cap_refinement_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"})
        ],
        outputs=["adset=111 strategy=cost_cap bid=2.2 changed_at=2025-08-18T14:13:00Z reason=cap_refinement_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t45",
        instruction="You will align ad set 102 with policy by capping bids: set strategy to cost_cap with bid_amount 14.0 effective 2025-08-18T14:15:00Z, log the change with reason policy_alignment_2025-08-13, and verify the updated state. Avoid unrelated insight pulls. For determinism, assume the largest existing strategy_changes ID is SC-4 so the next log will be SC-5.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 14.0,
                           "updated_at": "2025-08-18T14:15:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 14.0, "changed_at": "2025-08-18T14:15:00Z",
                           "reason": "policy_alignment_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=[
            "adset=102 strategy=cost_cap bid=14.0 changed_at=2025-08-18T14:15:00Z reason=policy_alignment_2025-08-13"
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t46",
        instruction="You will align ad set 103 with policy by operating under a cost cap of 19.0 effective at 2025-08-18T14:17:00Z, using its current state and 2025-08-13 performance to justify the change. You will persist an auditable record of the adjustment with the fetched prior values and reason baseline_cap_2025-08-13, and you will verify the final state.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 19.0,
                           "updated_at": "2025-08-18T14:17:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 19.0, "changed_at": "2025-08-18T14:17:00Z",
                           "reason": "baseline_cap_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"})
        ],
        outputs=["adset=103 strategy=cost_cap bid=19.0 changed_at=2025-08-18T14:17:00Z reason=baseline_cap_2025-08-13"]
    ),
    Task(
        annotator="v6",
        user_id="sma_t47",
        instruction=(
            "You have to Perform a clean creative rotation for ad set 102 using canonical types: "
            "activate carousel 1104 and pause image 1103 at 2025-08-19T10:06:00Z, with rationale format_test_b. "
            "Keep a concise audit (AR-20250819-18, creative_rotation, 10:05:00Z–10:07:00Z, completed, input_ref adset:102|rotation|1103->1104) "
            "and verify ads post-rotation."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-18", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-19T10:05:00Z",
                                                         "ended_at": "2025-08-19T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset:102|rotation|1103->1104",
                                                         "errors_json": "{}"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-19T10:06:00Z", "rationale": "format_test_b"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=[
            """[
          {"adset_id":"102","activated":"1104","paused":"1103"},
          {"automation_run":"AR-20250819-18"}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t48",
        instruction="You normalize ad set 112 by moving from lowest_cost to cost_cap 4.0 effective 2025-08-18T14:20:00Z with reason performance_floor. Validate canonical strategies, source old values from the record, audit with a one-day ROAS check for 2025-08-13, then record automation run AR-20250818-67 (run_type strategy_apply) with started_at 2025-08-18T14:20:00Z, ended_at 2025-08-18T14:21:00Z, status completed, input_ref adset:112, errors_json {}. Verify final state.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "112", "bid_strategy": "cost_cap", "bid_amount": 4.0,
                           "updated_at": "2025-08-18T14:20:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 4.0, "changed_at": "2025-08-18T14:20:00Z",
                           "reason": "performance_floor"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250818-67", "run_type": "strategy_apply",
                                                         "started_at": "2025-08-18T14:20:00Z",
                                                         "ended_at": "2025-08-18T14:21:00Z", "status": "completed",
                                                         "input_ref": "adset:112", "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_bid_strategy":"cost_cap","final_bid_amount":4.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t49",
        instruction=(
            "You have to Produce a KPI snapshot for ad set 103 as of 2025-08-13 and record an audit run "
            "(run_id kpi_snapshot_103_2025-08-13; started_at 2025-08-13T00:00:00Z; ended_at 2025-08-13T00:00:01Z; status completed; "
            "input_ref adset:103|baseline:2025-08-13). Report ROAS and CTR for 2025-08-13 and the total spend for 2025-08-07..2025-08-13. Read-only."
        ),
        actions=[
            Action(name="create_automation_run", kwargs={
                "run_id": "kpi_snapshot_103_2025-08-13",
                "run_type": "kpi_snapshot",
                "started_at": "2025-08-13T00:00:00Z",
                "ended_at": "2025-08-13T00:00:00Z",
                "status": "in_progress",
                "input_ref": "adset:103|baseline:2025-08-13",
                "errors_json": "{}"
            }),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="update_automation_run_end", kwargs={
                "run_id": "kpi_snapshot_103_2025-08-13",
                "status": "completed",
                "ended_at": "2025-08-13T00:00:01Z"
            }),
        ],
        outputs=[
            '{"adset_id":"103","date":"2025-08-13","roas":0.0,"ctr":0.0327}',
            '{"spend":{"adset_id":"103","start_date":"2025-08-07","end_date":"2025-08-13","total_spend":2380.0}}'
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t50",
        instruction="You adjust the daily budget for ad set 102 from 590.0 to 610.0 effective 2025-08-18T14:24:00Z with reason apparel_push, referencing Apparel viewership on 2025-08-13 and recent spend from 2025-08-07 to 2025-08-13. Then record automation run AR-20250818-69 (run_type budget_apply) with started_at 2025-08-18T14:24:00Z, ended_at 2025-08-18T14:25:00Z, status completed, input_ref adset:102, errors_json {}. Verify the final state.",
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 610.0, "updated_at": "2025-08-18T14:24:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 610.0,
                                                     "changed_at": "2025-08-18T14:24:00Z", "reason": "apparel_push"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-69", "run_type": "budget_apply", "started_at": "2025-08-18T14:24:00Z",
                           "ended_at": "2025-08-18T14:25:00Z", "status": "completed", "input_ref": "adset:102",
                           "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":610.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t51",
        instruction=(
            "You have to Respond to verified product 1 price (2025-08-14) by modestly lifting ad set 101 bid under policy safeguards. "
            "Set cost_cap bid to 36.0 at 2025-08-19T05:30:00Z with reason price_alignment_2025-08-14, verify after the update, "
            "and archive in a brief strategy_apply window (AR-20250819-19, 05:30:00Z–05:31:00Z, completed, input_ref adset_101_price_align)."
        ),
        actions=[
            Action(name="get_product_price_on_date", kwargs={"product_id": "1", "date": "2025-08-14"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 36.0,
                           "updated_at": "2025-08-19T05:30:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 32.0, "new_bid": 36.0, "changed_at": "2025-08-19T05:30:00Z",
                           "reason": "price_alignment_2025-08-14"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-19", "run_type": "strategy_apply",
                                                         "started_at": "2025-08-19T05:30:00Z",
                                                         "ended_at": "2025-08-19T05:31:00Z", "status": "completed",
                                                         "input_ref": "adset_101_price_align", "errors_json": "{}"}),
        ],
        outputs=[
            '[{"adset_id":"101","final_bid_strategy":"cost_cap","final_bid_amount":36.0},{"automation_run":"AR-20250819-19"}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t52",
        instruction=(
            "You have to Perform a deterministic midday tune for ad set 108: increase daily_budget to 820.0 and raise cost_cap bid to 44.0 "
            "effective 2025-08-19T12:12:00Z, logging with reason weekday_midday_reactivity and verifying after each change. "
            "Record a strategy_apply audit (AR-20250819-20, 12:12:00Z–12:13:00Z, completed, input_ref adset_108_midday)."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "108", "new_budget": 820.0, "updated_at": "2025-08-19T12:12:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 820.0,
                           "changed_at": "2025-08-19T12:12:00Z", "reason": "weekday_midday_reactivity"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 44.0,
                           "updated_at": "2025-08-19T12:12:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 42.0, "new_bid": 44.0, "changed_at": "2025-08-19T12:12:00Z",
                           "reason": "weekday_midday_reactivity"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-20", "run_type": "strategy_apply",
                                                         "started_at": "2025-08-19T12:12:00Z",
                                                         "ended_at": "2025-08-19T12:13:00Z", "status": "completed",
                                                         "input_ref": "adset_108_midday", "errors_json": "{}"}),
        ],
        outputs=[
            """[
          {"adset_id":"108","final_daily_budget":820.0,"final_bid_strategy":"cost_cap","final_bid_amount":44.0},
          {"automation_run":"AR-20250819-20"}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t53",
        instruction="You calibrate the daily budget for ad set 105 from 750.0 to 720.0 effective 2025-08-18T14:30:00Z with reason inventory_softening, referencing Office viewership on 2025-08-13 and recent spend from 2025-08-07 through 2025-08-13. Record a completed automation run AR-20250818-72 (started_at 2025-08-18T14:30:00Z, ended_at 2025-08-18T14:31:00Z, input_ref adset:105, errors_json {}). Verify the final state.",
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "105", "new_budget": 720.0, "updated_at": "2025-08-18T14:30:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 720.0,
                                                     "changed_at": "2025-08-18T14:30:00Z",
                                                     "reason": "inventory_softening"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-72", "run_type": "budget_apply", "started_at": "2025-08-18T14:30:00Z",
                           "ended_at": "2025-08-18T14:31:00Z", "status": "completed", "input_ref": "adset:105",
                           "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"})
        ],
        outputs=['[{"adset_id":"105","final_budget":720.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t54",
        instruction="You increase the daily budget for ad set 106 from 500.0 to 520.0 effective 2025-08-18T14:32:00Z with reason conversion_tailwind, referencing Electronics viewership on 2025-08-13 and recent spend from 2025-08-07 through 2025-08-13. Record a completed automation run AR-20250818-73 (started_at 2025-08-18T14:32:00Z, ended_at 2025-08-18T14:33:00Z, input_ref adset:106, errors_json {}). Verify the final state.",
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "106", "new_budget": 520.0, "updated_at": "2025-08-18T14:32:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 520.0,
                                                     "changed_at": "2025-08-18T14:32:00Z",
                                                     "reason": "conversion_tailwind"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-73", "run_type": "budget_apply", "started_at": "2025-08-18T14:32:00Z",
                           "ended_at": "2025-08-18T14:33:00Z", "status": "completed", "input_ref": "adset:106",
                           "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"})
        ],
        outputs=['[{"adset_id":"106","final_budget":520.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t55",
        instruction=(
            "You reduce the daily budget for ad set 107 from 400.0 to 380.0 effective 2025-08-18T14:34:00Z with reason "
            "learning_phase. Use Toys viewership on 2025-08-13 and recent spend from 2025-08-07 to 2025-08-13 as context. "
            "Maintain a concise audit via AR-20250818-74 (budget_apply) started at 2025-08-18T14:34:00Z and ended at "
            "2025-08-18T14:35:00Z with input_ref adset:107. Verify the final state."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "107", "new_budget": 380.0, "updated_at": "2025-08-18T14:34:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 380.0,
                                                     "changed_at": "2025-08-18T14:34:00Z", "reason": "learning_phase"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-74", "run_type": "budget_apply", "started_at": "2025-08-18T14:34:00Z",
                           "input_ref": "adset:107"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-74", "ended_at": "2025-08-18T14:35:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"})
        ],
        outputs=['[{"adset_id":"107","final_budget":380.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t56",
        instruction="You reduce the daily budget for ad set 108 from 780.0 to 760.0 effective 2025-08-18T14:36:00Z with reason supply_variance, referencing Electronics viewership on 2025-08-13 and recent spend from 2025-08-07 to 2025-08-13. For determinism, assume the largest existing budget_changes change_id is BC-7 so your next log will be BC-8. Record a completed automation run AR-20250818-75 (started_at 2025-08-18T14:36:00Z, ended_at 2025-08-18T14:37:00Z, input_ref adset:108, errors_json {}). Verify the final state.",
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "108", "new_budget": 760.0, "updated_at": "2025-08-18T14:36:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 760.0,
                                                     "changed_at": "2025-08-18T14:36:00Z",
                                                     "reason": "supply_variance"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-75", "run_type": "budget_apply", "started_at": "2025-08-18T14:36:00Z",
                           "ended_at": "2025-08-18T14:37:00Z", "status": "completed", "input_ref": "adset:108",
                           "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_budget":760.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t57",
        instruction="You rotate creatives within ad set 102 by activating 1104 and pausing 1103 with rationale carousel_focus at 2025-08-18T14:38:00Z. Record a completed automation run AR-20250818-76 (started_at 2025-08-18T14:38:00Z, ended_at 2025-08-18T14:39:00Z, input_ref adset:102, errors_json {}). Verify the rotation by re-listing ads after the change; avoid unrelated reads.",
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                                                         "rotated_at": "2025-08-18T14:38:00Z",
                                                         "rationale": "carousel_focus"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250818-76", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-18T14:38:00Z",
                                                         "ended_at": "2025-08-18T14:39:00Z", "status": "completed",
                                                         "input_ref": "adset:102", "errors_json": "{}"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1104","paused":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t58",
        instruction="You rotate creatives within ad set 102 by activating 1103 and pausing 1104 with rationale image_focus at 2025-08-18T14:40:00Z. Record a completed automation run AR-20250818-77 (started_at 2025-08-18T14:40:00Z, ended_at 2025-08-18T14:41:00Z, input_ref adset:102, errors_json {}). Verify the rotation by re-listing ads after the change; avoid unrelated reads.",
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T14:40:00Z",
                                                         "rationale": "image_focus"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250818-77", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-18T14:40:00Z",
                                                         "ended_at": "2025-08-18T14:41:00Z", "status": "completed",
                                                         "input_ref": "adset:102", "errors_json": "{}"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1103","paused":"1104"}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t59",
        instruction=(
            "You have to Refresh ad set 102 with a new image creative and make it live: create an image ad named Autumn Image (start_date 2025-08-19), "
            "activate it and pause 1103 at 10:08:00Z with rationale format_test_image. "
            "Record a concise creative_refresh audit (AR-20250819-21, 10:07:30Z–10:09:00Z, completed, input_ref adset_102_autumn_image) "
            "and verify ads after rotation."
        ),
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="create_ad", kwargs={"adset_id": "102", "name": "Autumn Image", "creative_type": "image",
                                             "start_date": "2025-08-19"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-21", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-19T10:07:30Z",
                                                         "ended_at": "2025-08-19T10:09:00Z", "status": "completed",
                                                         "input_ref": "adset_102_autumn_image", "errors_json": "{}"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                           "rotated_at": "2025-08-19T10:08:00Z", "rationale": "format_test_image"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=[
            """[
          {"adset_id":"102","activated":"1119","paused":"1103"},
          {"automation_run":"AR-20250819-21"}
        ]"""
        ]
    ),
    Task(
        annotator="v6",
        user_id="sma_t60",
        instruction=(
            "You have to Perform a cross-channel budget rebalance for ad sets 101 and 102 in a deterministic, policy-compliant way. "
            "At 2025-08-19T08:50:00Z set 101 to 940.0 and 102 to 610.0, logging both with reason rebalance_2025-08-19, "
            "verifying after each, and recording a budget_rebalance window "
            "(AR-20250819-23, 08:50:00Z–08:51:00Z, completed, input_ref adsets_101_102_rebalance)."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 940.0, "updated_at": "2025-08-19T08:50:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 940.0,
                           "changed_at": "2025-08-19T08:50:00Z", "reason": "rebalance_2025-08-19"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 610.0, "updated_at": "2025-08-19T08:50:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 610.0,
                           "changed_at": "2025-08-19T08:50:00Z", "reason": "rebalance_2025-08-19"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),

            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-23", "run_type": "budget_rebalance",
                                                         "started_at": "2025-08-19T08:50:00Z",
                                                         "ended_at": "2025-08-19T08:51:00Z", "status": "completed",
                                                         "input_ref": "adsets_101_102_rebalance", "errors_json": "{}"}),
        ],
        outputs=[
            """[
          {"adset_id":"101","final_daily_budget":940.0},
          {"adset_id":"102","final_daily_budget":610.0},
          {"automation_run":"AR-20250819-23"}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t61",
        instruction="You align ad set 111 with plan_2025-08-13: apply budget 1000.0 and cost_cap 2.5 effective at 2025-08-18T14:50:00Z, then confirm the final state. Record plan snapshots with AR-20250818-82 (plan_freeze, started_at 2025-08-18T14:50:00Z, input_ref plan_2025-08-13) and AR-20250818-83 (budget_apply, started_at 2025-08-18T14:50:00Z, input_ref plan_2025-08-13).",
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-82", "run_type": "plan_freeze",
                           "started_at": "2025-08-18T14:50:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "111", "new_budget": 1000.0, "updated_at": "2025-08-18T14:50:00Z"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5,
                           "updated_at": "2025-08-18T14:50:00Z"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-83", "run_type": "budget_apply",
                           "started_at": "2025-08-18T14:50:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","plan_applied":"plan_2025-08-13"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t62",
        instruction="You calibrate ad set 102 with a paired move: raise the daily budget from 590.0 to 600.0 and set cost_cap 6.0, both effective at 2025-08-18T14:54:00Z, for reason paired_scale. Validate canonical strategies, log both changes, record AR-20250818-84 (strategy_apply, started_at 2025-08-18T14:54:00Z, input_ref adset:102), and confirm the final state.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 600.0, "updated_at": "2025-08-18T14:54:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0,
                                                     "changed_at": "2025-08-18T14:54:00Z", "reason": "paired_scale"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 6.0,
                           "updated_at": "2025-08-18T14:54:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.0, "changed_at": "2025-08-18T14:54:00Z",
                           "reason": "paired_scale"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-84", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T14:54:00Z", "input_ref": "adset:102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":600.0,"final_bid_strategy":"cost_cap","final_bid_amount":6.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t63",
        instruction="You rebalance ad set 101 by lowering the daily budget from 920.0 to 900.0 and retaining cost_cap 32.0, both effective at 2025-08-18T14:58:00Z, for reason margin_guard. Include ROAS for 2025-08-13 as context, record AR-20250818-85 (budget_apply, started_at 2025-08-18T14:58:00Z, input_ref adset:101), and verify the final state.",
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 900.0, "updated_at": "2025-08-18T14:58:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 900.0,
                                                     "changed_at": "2025-08-18T14:58:00Z", "reason": "margin_guard"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0,
                           "updated_at": "2025-08-18T14:58:00Z"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-85", "run_type": "budget_apply",
                           "started_at": "2025-08-18T14:58:00Z", "input_ref": "adset:101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_budget":900.0,"final_bid_amount":32.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t64",
        instruction="You maintain stability in ad set 102 by keeping ad 1103 active and pausing 1104 with rationale stability_check at 2025-08-18T15:02:00Z, and confirm with reads. Include a one-day CTR context for 2025-08-13. For determinism, assume the largest existing creative_rotations ID is CR-3 so the next will be CR-4. Record AR-20250818-86 (creative_rotation, started_at 2025-08-18T15:02:00Z, input_ref adset:102).",
        actions=[
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T15:02:00Z",
                                                         "rationale": "stability_check"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-86", "run_type": "creative_rotation",
                           "started_at": "2025-08-18T15:02:00Z", "input_ref": "adset:102"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","active_ad_after":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t65",
        instruction="You refine ad set 103 by moving to cost_cap 6.5 effective at 2025-08-18T15:04:00Z with reason video_efficiency. Validate canonical strategies, source old values, include a 2025-08-13 insight pull for context, record AR-20250818-87 (strategy_apply, started_at 2025-08-18T15:04:00Z, input_ref adset:103), and verify. For determinism, assume the largest existing strategy_changes ID is SC-4 so the next will be SC-5.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 6.5,
                           "updated_at": "2025-08-18T15:04:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.5, "changed_at": "2025-08-18T15:04:00Z",
                           "reason": "video_efficiency"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-87", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:04:00Z", "input_ref": "adset:103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"})
        ],
        outputs=['[{"adset_id":"103","final_bid_strategy":"cost_cap","final_bid_amount":6.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t66",
        instruction="You nudge ad set 104’s budget upward from 740.0 to 760.0 and keep bid strategy cost_cap 22.0, both effective at 2025-08-18T15:06:00Z, for reason inventory_tight. Use Electronics viewership on 2025-08-13 and the spend window 2025-08-07 to 2025-08-13 as context. Record AR-20250818-88 (budget_apply, started_at 2025-08-18T15:06:00Z, input_ref adset:104) and verify.",
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "104", "new_budget": 760.0, "updated_at": "2025-08-18T15:06:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 760.0,
                                                     "changed_at": "2025-08-18T15:06:00Z",
                                                     "reason": "inventory_tight"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-18T15:06:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 20.0, "new_bid": 22.0, "changed_at": "2025-08-18T15:06:00Z",
                           "reason": "inventory_tight"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-88", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:06:00Z", "input_ref": "adset:104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_budget":760.0,"final_bid_amount":22.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t67",
        instruction="You standardize ad set 105 from lowest_cost to cost_cap 3.5 effective 2025-08-18T15:10:00Z with reason standardize_bidding. Validate canonical strategies, source prior values, record AR-20250818-89 (strategy_apply, started_at 2025-08-18T15:10:00Z, input_ref adset:105), and close that run at 2025-08-18T15:10:00Z. Use a CTR read for 2025-08-13 as verification context (no extra post-change ad set read).",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "105", "bid_strategy": "cost_cap", "bid_amount": 3.5,
                           "updated_at": "2025-08-18T15:10:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 3.5, "changed_at": "2025-08-18T15:10:00Z",
                           "reason": "standardize_bidding"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-89", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:10:00Z", "input_ref": "adset:105"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-89", "ended_at": "2025-08-18T15:10:00Z"})
        ],
        outputs=['[{"adset_id":"105","final_bid_strategy":"cost_cap","final_bid_amount":3.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t68",
        instruction="You apply a no-op budget confirmation for ad set 102 by re-writing daily_budget 590.0 effective 2025-08-18T15:12:00Z with reason budget_confirm. For deterministic context, audit same-day spend and CTR on 2025-08-13 (spend window 2025-08-13 to 2025-08-13, CTR date 2025-08-13). Record AR-20250818-90 (budget_apply, started_at 2025-08-18T15:12:00Z, input_ref adset:102) and verify.",
        actions=[
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "102", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 590.0, "updated_at": "2025-08-18T15:12:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 590.0,
                                                     "changed_at": "2025-08-18T15:12:00Z", "reason": "budget_confirm"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-90", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:12:00Z", "input_ref": "adset:102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":590.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t69",
        instruction="You tilt ad set 108 by decreasing budget from 780.0 to 770.0 and increasing cost_cap from 42.0 to 43.0 effective 2025-08-18T15:14:00Z with reason shift_to_quality. Use record-sourced old values, validate canonical strategies, record AR-20250818-91 (strategy_apply, started_at 2025-08-18T15:14:00Z, input_ref adset:108), and verify via a post-change read.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "108", "new_budget": 770.0, "updated_at": "2025-08-18T15:14:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 770.0,
                                                     "changed_at": "2025-08-18T15:14:00Z",
                                                     "reason": "shift_to_quality"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 43.0,
                           "updated_at": "2025-08-18T15:14:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0,
                           "new_bid": 43.0, "changed_at": "2025-08-18T15:14:00Z", "reason": "shift_to_quality"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-91", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:14:00Z", "input_ref": "adset:108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_budget":770.0,"final_bid_amount":43.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t70",
        instruction="You standardize ad set 107 from lowest_cost to cost_cap 3.0 effective 2025-08-18T15:18:00Z with reason standardize_lowspend, validating canonical strategies, using record-sourced old values, recording AR-20250818-92 strategy_apply for input_ref adset:107, and verifying with a ROAS read for 2025-08-13.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "107", "bid_strategy": "cost_cap", "bid_amount": 3.0,
                           "updated_at": "2025-08-18T15:18:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 3.0, "changed_at": "2025-08-18T15:18:00Z",
                           "reason": "standardize_lowspend"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-92", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:18:00Z", "input_ref": "adset:107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"})
        ],
        outputs=['[{"adset_id":"107","final_bid_strategy":"cost_cap","final_bid_amount":3.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t71",
        instruction=(
            "You have to Create and apply a plan for 2025-08-22 focusing on ad set 112’s pacing. "
            "Plan plan_2025-08-22c (author planning_agent_v1, created_at 2025-08-22T01:57:50Z, checksum p22c0760) "
            "allocates 760.0 to ad set 112 (lowest_cost, image). Freeze (AR-20250822-07, 01:57:50Z–01:59:30Z). "
            "Apply budget at 02:05:00Z with reason plan_2025-08-22c, verify, and record budget_apply "
            "(AR-20250822-08, 02:05:00Z–02:06:00Z)."
        ),
        actions=[
            Action(name="list_canonical_creative_types", kwargs={}),
            Action(name="validate_allocations_against_policy", kwargs={"total_budget": 760.0, "allocations": [
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="create_plan",
                   kwargs={"plan_id": "plan_2025-08-22c", "date": "2025-08-22", "total_budget": 760.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-22T01:57:50Z",
                           "checksum": "p22c0760", "allocations": [
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-22"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250822-07", "run_type": "plan_freeze",
                                                         "started_at": "2025-08-22T01:57:50Z",
                                                         "ended_at": "2025-08-22T01:59:30Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-22c", "errors_json": "{}"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 760.0, "updated_at": "2025-08-22T02:05:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 760.0,
                           "changed_at": "2025-08-22T02:05:00Z", "reason": "plan_2025-08-22c"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250822-08", "run_type": "budget_apply",
                                                         "started_at": "2025-08-22T02:05:00Z",
                                                         "ended_at": "2025-08-22T02:06:00Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-22c", "errors_json": "{}"}),
        ],
        outputs=[
            """[
          {"plan_id":"plan_2025-08-22c","adset_id":"112","final_daily_budget":760.0},
          {"runs":["AR-20250822-07","AR-20250822-08"]}
        ]"""
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t72",
        instruction="You align ad set 112 at cost_cap 4.2 effective 2025-08-18T15:24:00Z with reason cp_flooring. Confirm canonical strategies and read the ad set; its budget is already 700.0, so do not log a redundant budget change. Record AR-20250818-94 (strategy_apply, started_at 2025-08-18T15:24:00Z, input_ref adset:112) and verify.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "112", "bid_strategy": "cost_cap", "bid_amount": 4.2,
                           "updated_at": "2025-08-18T15:24:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 4.2, "changed_at": "2025-08-18T15:24:00Z",
                           "reason": "cp_flooring"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-94", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:24:00Z", "input_ref": "adset:112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_bid_strategy":"cost_cap","final_bid_amount":4.2}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t73",
        instruction="You verify canonical strategies and apply cost_cap 5.0 to ad set 102 effective 2025-08-18T15:28:00Z with reason conservative_cap. Log the change, record AR-20250818-95 (strategy_apply, started_at 2025-08-18T15:28:00Z, input_ref adset:102), then verify via a post-change ad set read and a 2025-08-13 insights fetch.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 5.0,
                           "updated_at": "2025-08-18T15:28:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 5.0, "changed_at": "2025-08-18T15:28:00Z",
                           "reason": "conservative_cap"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-95", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:28:00Z", "input_ref": "adset:102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"})
        ],
        outputs=['[{"adset_id":"102","final_bid_strategy":"cost_cap","final_bid_amount":5.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t74",
        instruction="You apply a minimal increase for ad set 101 budget from 920.0 to 930.0 effective 2025-08-18T15:30:00Z with reason micro_scale and keep cost_cap 32.0. Include a 2025-08-13 CTR snapshot for context, keep the audit concise, and confirm the final state.",
        actions=[
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 930.0, "updated_at": "2025-08-18T15:30:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 930.0,
                                                     "changed_at": "2025-08-18T15:30:00Z", "reason": "micro_scale"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0,
                           "updated_at": "2025-08-18T15:30:00Z"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-96", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:30:00Z", "input_ref": "adset:101"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-96", "ended_at": "2025-08-18T15:30:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_budget":930.0,"final_bid_amount":32.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t75",
        instruction=(
            "You make a stability-oriented no-op rotation for ad set 102, keeping 1103 active and 1104 paused with rationale "
            "stability_noop at 2025-08-18T15:34:00Z; then you verify via reads and include a ROAS context read for 2025-08-13."
        ),
        actions=[
            Action(name="calculate_adset_roas_for_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T15:34:00Z",
                                                         "rationale": "stability_noop"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","active_ad_after":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t76",
        instruction="You confirm plan_2025-08-13 allocation for ad set 111 by ensuring budget 1000.0 and cost_cap 2.5 effective 2025-08-18T15:36:00Z, recording AR-20250818-98 (plan_freeze, started_at 2025-08-18T15:36:00Z, input_ref plan_2025-08-13) and AR-20250818-99 (budget_apply, started_at 2025-08-18T15:36:00Z, input_ref plan_2025-08-13), and verifying final state.",
        actions=[
            Action(name="get_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_allocation_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-98", "run_type": "plan_freeze",
                           "started_at": "2025-08-18T15:36:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "111", "new_budget": 1000.0, "updated_at": "2025-08-18T15:36:00Z"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5,
                           "updated_at": "2025-08-18T15:36:00Z"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-99", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:36:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","plan_confirmed":"plan_2025-08-13"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t77",
        instruction="You calibrate budget for ad set 102 from 590.0 to 620.0 effective 2025-08-18T16:00:00Z with reason office_retarget_calibration, using Office viewership on 2025-08-13 and a deterministic same-day spend window (2025-08-13 to 2025-08-13). Record AR-20250818-56 (budget_apply, started_at 2025-08-18T16:00:00Z, input_ref adset:102), close that run at 2025-08-18T16:00:00Z, and verify final state.",
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "102", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 620.0, "updated_at": "2025-08-18T16:00:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 620.0,
                                                     "changed_at": "2025-08-18T16:00:00Z",
                                                     "reason": "office_retarget_calibration"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-56", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:00:00Z", "input_ref": "adset:102"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-56", "ended_at": "2025-08-18T16:00:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":620.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t78",
        instruction="You validate canonical strategies and move ad set 102 from lowest_cost to cost_cap 5.0 effective 2025-08-18T16:05:00Z with reason retarget_cost_focus, auditing with Apparel viewership on 2025-08-13. Record AR-20250818-57 (strategy_apply, started_at 2025-08-18T16:05:00Z, input_ref adset:102) and verify.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 5.0,
                           "updated_at": "2025-08-18T16:05:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 5.0, "changed_at": "2025-08-18T16:05:00Z",
                           "reason": "retarget_cost_focus"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-57", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:05:00Z", "input_ref": "adset:102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_bid_strategy":"cost_cap","final_bid_amount":5.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t79",
        instruction="You establish a spend and engagement baseline for ad set 102 and confirm its budget with an audited no-op: re-write daily_budget 590.0 effective 2025-08-18T16:10:00Z with reason budget_confirm. Use a deterministic same-day spend window (2025-08-13 to 2025-08-13) and CTR date 2025-08-13. Record AR-20250818-58 (budget_apply, started_at 2025-08-18T16:10:00Z, input_ref adset:102) and verify.",
        actions=[
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "102", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="compute_ctr_for_adset_day", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "102", "new_budget": 590.0, "updated_at": "2025-08-18T16:10:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 590.0,
                                                     "changed_at": "2025-08-18T16:10:00Z", "reason": "budget_confirm"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-58", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:10:00Z", "input_ref": "adset:102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":590.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t80",
        instruction=(
            "You have to Combine recent Electronics signals and product 1 price (2025-08-14) to pace ad set 101 prudently. "
            "At 2025-08-19T09:10:00Z set daily_budget to 970.0, log reason cross_signal_pacing_2025-08-13, "
            "verify the new state, and record a concise budget_rebalance window "
            "(AR-20250819-25, 09:10:00Z–09:11:00Z, completed, input_ref adset_101_cross_signal)."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_product_price_on_date", kwargs={"product_id": "1", "date": "2025-08-14"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 970.0, "updated_at": "2025-08-19T09:10:00Z"}),
            Action(name="log_budget_change",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 970.0,
                           "changed_at": "2025-08-19T09:10:00Z", "reason": "cross_signal_pacing_2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="create_automation_run", kwargs={"run_id": "AR-20250819-25", "run_type": "budget_rebalance",
                                                         "started_at": "2025-08-19T09:10:00Z",
                                                         "ended_at": "2025-08-19T09:11:00Z", "status": "completed",
                                                         "input_ref": "adset_101_cross_signal", "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"101","final_daily_budget":970.0},{"automation_run":"AR-20250819-25"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t81",
        instruction="You align ad set 104’s bidding per policy by tightening cost_cap from 20.0 to 21.0 effective 2025-08-18T16:14:00Z, log the change with reason incremental_efficiency, record AR-20250818-101 (strategy_apply, started_at 2025-08-18T16:14:00Z, input_ref adset:104) and close it at 2025-08-18T16:14:00Z, then verify via a single read.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 21.0,
                           "updated_at": "2025-08-18T16:14:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 21.0, "changed_at": "2025-08-18T16:14:00Z",
                           "reason": "incremental_efficiency"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-101", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:14:00Z", "input_ref": "adset:104"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-101", "ended_at": "2025-08-18T16:14:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_bid_strategy":"cost_cap","final_bid_amount":21.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t82",
        instruction="You nudge ad set 104’s daily budget from 740.0 to 745.0 effective 2025-08-18T16:16:00Z for reason incremental_topup. Record AR-20250818-102 (budget_apply, started_at 2025-08-18T16:16:00Z, input_ref adset:104), close it at 2025-08-18T16:16:00Z, and verify via one post-change read.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "104", "new_budget": 745.0, "updated_at": "2025-08-18T16:16:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 745.0,
                                                     "changed_at": "2025-08-18T16:16:00Z",
                                                     "reason": "incremental_topup"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-102", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:16:00Z", "input_ref": "adset:104"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-102", "ended_at": "2025-08-18T16:16:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_budget":745.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t83",
        instruction="You standardize ad set 103 by moving from lowest_cost to cost_cap 6.0 effective 2025-08-18T16:18:00Z with reason standardize_policy. Record AR-20250818-103 (strategy_apply, started_at 2025-08-18T16:18:00Z, input_ref adset:103), close it at 2025-08-18T16:18:00Z, and verify.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 6.0,
                           "updated_at": "2025-08-18T16:18:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.0, "changed_at": "2025-08-18T16:18:00Z",
                           "reason": "standardize_policy"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-103", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:18:00Z", "input_ref": "adset:103"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-103", "ended_at": "2025-08-18T16:18:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"})
        ],
        outputs=['[{"adset_id":"103","final_bid_strategy":"cost_cap","final_bid_amount":6.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t84",
        instruction="You trim ad set 108’s daily budget from 780.0 to 775.0 effective 2025-08-18T16:20:00Z with reason controlled_reduction. Record AR-20250818-104 (budget_apply, started_at 2025-08-18T16:20:00Z, input_ref adset:108), close it at 2025-08-18T16:20:00Z, and verify.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "108", "new_budget": 775.0, "updated_at": "2025-08-18T16:20:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 775.0,
                                                     "changed_at": "2025-08-18T16:20:00Z",
                                                     "reason": "controlled_reduction"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-104", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:20:00Z", "input_ref": "adset:108"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-104", "ended_at": "2025-08-18T16:20:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_budget":775.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t85",
        instruction="You rebalance ad set 101’s daily budget from 920.0 to 915.0 effective 2025-08-18T16:22:00Z for reason margin_tighten. Record AR-20250818-105 (budget_apply, started_at 2025-08-18T16:22:00Z, input_ref adset:101), close it at 2025-08-18T16:22:00Z, and verify.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "101", "new_budget": 915.0, "updated_at": "2025-08-18T16:22:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 915.0,
                                                     "changed_at": "2025-08-18T16:22:00Z",
                                                     "reason": "margin_tighten"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-105", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:22:00Z", "input_ref": "adset:101"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-105", "ended_at": "2025-08-18T16:22:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_budget":915.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t86",
        instruction="You perform a creative rotation in ad set 102: activate 1104 and pause 1103 at 2025-08-18T16:24:00Z with rationale carousel_focus. Record AR-20250818-106 (creative_rotation, started_at 2025-08-18T16:24:00Z, input_ref adset:102), close it at 2025-08-18T16:24:00Z, and verify with a post-rotation ads read.",
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                                                         "rotated_at": "2025-08-18T16:24:00Z",
                                                         "rationale": "carousel_focus"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-106", "run_type": "creative_rotation",
                           "started_at": "2025-08-18T16:24:00Z", "input_ref": "adset:102"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-106", "ended_at": "2025-08-18T16:24:00Z"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1104","paused":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t87",
        instruction=(
            "You tighten ad set 106’s bidding by setting cost_cap to 17.5 at 2025-08-18T16:26:00Z for reason efficiency_tune. "
            "Validate against canonical strategies, include a concise AR-20250818-107 strategy_apply audit "
            "(started and ended at 2025-08-18T16:26:00Z; input_ref adset:106), and return the final state."
        ),
        actions=[
            Action(name="list_canonical_bid_strategies", kwargs={}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),

            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 17.5,
                           "updated_at": "2025-08-18T16:26:00Z"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-107", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:26:00Z", "input_ref": "adset:106"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-107", "ended_at": "2025-08-18T16:26:00Z"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"})
        ],
        outputs=['[{"adset_id":"106","final_bid_strategy":"cost_cap","final_bid_amount":17.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t88",
        instruction="You reduce ad set 111’s daily budget from 1000.0 to 990.0 effective 2025-08-18T16:28:00Z for reason budget_guard. Record AR-20250818-108 (budget_apply, started_at 2025-08-18T16:28:00Z, input_ref adset:111), close it at 2025-08-18T16:28:00Z, and verify.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "111", "new_budget": 990.0, "updated_at": "2025-08-18T16:28:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 990.0,
                                                     "changed_at": "2025-08-18T16:28:00Z",
                                                     "reason": "budget_guard"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-108", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:28:00Z", "input_ref": "adset:111"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-108", "ended_at": "2025-08-18T16:28:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","final_budget":990.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t89",
        instruction="You standardize ad set 105 from lowest_cost to cost_cap 3.2 effective 2025-08-18T16:30:00Z with reason policy_standardization. Keep a minimal audit trail (single change log) and confirm the result with one post-change read. For determinism, assume the highest existing strategy_changes ID is SC-4, so the new entry is SC-5.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "105", "bid_strategy": "cost_cap", "bid_amount": 3.2,
                           "updated_at": "2025-08-18T16:30:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"change_id": "SC-5", "adset_id": "105", "old_strategy": "lowest_cost",
                           "new_strategy": "cost_cap", "old_bid": None, "new_bid": 3.2,
                           "changed_at": "2025-08-18T16:30:00Z", "reason": "policy_standardization"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"})
        ],
        outputs=['[{"adset_id":"105","final_bid_strategy":"cost_cap","final_bid_amount":3.2}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t90",
        instruction="You convert ad set 107 from lowest_cost to cost_cap 3.1 effective 2025-08-18T16:32:00Z with reason standardize_lowspend. Record AR-20250818-110 (strategy_apply, started_at 2025-08-18T16:32:00Z, input_ref adset:107), close it at 2025-08-18T16:32:00Z, and verify.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "107", "bid_strategy": "cost_cap", "bid_amount": 3.1,
                           "updated_at": "2025-08-18T16:32:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 3.1, "changed_at": "2025-08-18T16:32:00Z",
                           "reason": "standardize_lowspend"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-110", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:32:00Z", "input_ref": "adset:107"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-110", "ended_at": "2025-08-18T16:32:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"})
        ],
        outputs=['[{"adset_id":"107","final_bid_strategy":"cost_cap","final_bid_amount":3.1}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t91",
        instruction="You increase ad set 112’s daily budget from 700.0 to 710.0 effective 2025-08-18T16:34:00Z with reason pacing_boost. Record AR-20250818-111 (budget_apply, started_at 2025-08-18T16:34:00Z, input_ref adset:112), close it at 2025-08-18T16:34:00Z, and verify.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "112", "new_budget": 710.0, "updated_at": "2025-08-18T16:34:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 710.0,
                                                     "changed_at": "2025-08-18T16:34:00Z",
                                                     "reason": "pacing_boost"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-111", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:34:00Z", "input_ref": "adset:112"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-111", "ended_at": "2025-08-18T16:34:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_budget":710.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t92",
        instruction="You trim the budget on ad set 103 to 1160.0 effective 2025-08-18T16:36:00Z with reason headroom_guard. Keep the audit trail minimal and confirm with a single post-change read. Avoid creating automation-run records.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "103", "new_budget": 1160.0, "updated_at": "2025-08-18T16:36:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 1160.0,
                                                     "changed_at": "2025-08-18T16:36:00Z",
                                                     "reason": "headroom_guard"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"})
        ],
        outputs=['[{"adset_id":"103","final_budget":1160.0}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t93",
        instruction="You tighten ad set 101 cost_cap from 32.0 to 33.0 effective 2025-08-18T16:38:00Z with reason bid_recenter. Maintain a minimal audit trail and confirm with one post-change read; do not create automation runs.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 33.0,
                           "updated_at": "2025-08-18T16:38:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 32.0, "new_bid": 33.0, "changed_at": "2025-08-18T16:38:00Z",
                           "reason": "bid_recenter"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_bid_strategy":"cost_cap","final_bid_amount":33.0}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t94",
        instruction="You rotate creatives in ad set 102 to stabilize: activate 1103 and pause 1104 at 2025-08-18T16:40:00Z with rationale stability_focus. Record AR-20250818-114 (creative_rotation, started_at 2025-08-18T16:40:00Z, input_ref adset:102), close it at 2025-08-18T16:40:00Z, and verify by reading ads.",
        actions=[
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="rotate_ad_creative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="log_creative_rotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T16:40:00Z",
                                                         "rationale": "stability_focus"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-114", "run_type": "creative_rotation",
                           "started_at": "2025-08-18T16:40:00Z", "input_ref": "adset:102"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-114", "ended_at": "2025-08-18T16:40:00Z"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1103","paused":"1104"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t95",
        instruction="You lift ad set 108’s cost_cap from 42.0 to 43.0 effective 2025-08-18T16:42:00Z with reason value_seek. Record AR-20250818-115 (strategy_apply, started_at 2025-08-18T16:42:00Z, input_ref adset:108), close it at 2025-08-18T16:42:00Z, and verify.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 43.0,
                           "updated_at": "2025-08-18T16:42:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 42.0, "new_bid": 43.0, "changed_at": "2025-08-18T16:42:00Z",
                           "reason": "value_seek"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-115", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:42:00Z", "input_ref": "adset:108"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-115", "ended_at": "2025-08-18T16:42:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_bid_strategy":"cost_cap","final_bid_amount":43.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t96",
        instruction=(
            "You raise ad set 106’s daily budget to 508.0 at 2025-08-18T16:44:00Z with reason light_scale, guided by policy and recent context. "
            "Use the 2025-08-13 Electronics baseline (viewership and same-day spend) and include a single audit entry AR-20250818-116 "
            "(budget_apply; 2025-08-18T16:44:00Z; input_ref adset:106). Return the final state."
        ),
        actions=[
            Action(name="get_viewership_for_category", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="get_adset_spend_for_date_range",
                   kwargs={"adset_id": "106", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),

            Action(name="update_adset_budget",
                   kwargs={"adset_id": "106", "new_budget": 508.0, "updated_at": "2025-08-18T16:44:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 508.0,
                                                     "changed_at": "2025-08-18T16:44:00Z", "reason": "light_scale"}),

            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-116", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:44:00Z", "input_ref": "adset:106"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-116", "ended_at": "2025-08-18T16:44:00Z"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"})
        ],
        outputs=['[{"adset_id":"106","final_budget":508.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t97",
        instruction="You reduce ad set 105’s daily budget from 750.0 to 740.0 effective 2025-08-18T16:46:00Z with reason inventory_softness. Record AR-20250818-117 (budget_apply, started_at 2025-08-18T16:46:00Z, input_ref adset:105), close it at 2025-08-18T16:46:00Z, and verify.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "105", "new_budget": 740.0, "updated_at": "2025-08-18T16:46:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 740.0,
                                                     "changed_at": "2025-08-18T16:46:00Z",
                                                     "reason": "inventory_softness"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-117", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:46:00Z", "input_ref": "adset:105"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-117", "ended_at": "2025-08-18T16:46:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"})
        ],
        outputs=['[{"adset_id":"105","final_budget":740.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t98",
        instruction="You fine-tune ad set 111 cost_cap from 2.5 to 2.6 effective 2025-08-18T16:48:00Z with reason incremental_bid_lift. Keep the audit minimal (single change log) and confirm with one post-change read. For determinism, assume the highest existing strategy_changes ID is SC-4, so the new entry is SC-5. Do not create automation runs.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.6,
                           "updated_at": "2025-08-18T16:48:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"change_id": "SC-5", "adset_id": "111", "old_strategy": "cost_cap",
                           "new_strategy": "cost_cap", "old_bid": 2.5, "new_bid": 2.6,
                           "changed_at": "2025-08-18T16:48:00Z", "reason": "incremental_bid_lift"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","final_bid_strategy":"cost_cap","final_bid_amount":2.6}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t99",
        instruction="You standardize ad set 112 from lowest_cost to cost_cap 4.0 effective 2025-08-18T16:50:00Z with reason baseline_cap. Record AR-20250818-119 (strategy_apply, started_at 2025-08-18T16:50:00Z, input_ref adset:112), close it at 2025-08-18T16:50:00Z, and verify.",
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="update_adset_bid_strategy",
                   kwargs={"adset_id": "112", "bid_strategy": "cost_cap", "bid_amount": 4.0,
                           "updated_at": "2025-08-18T16:50:00Z"}),
            Action(name="log_strategy_change",
                   kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 4.0, "changed_at": "2025-08-18T16:50:00Z",
                           "reason": "baseline_cap"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-119", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:50:00Z", "input_ref": "adset:112"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-119", "ended_at": "2025-08-18T16:50:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_bid_strategy":"cost_cap","final_bid_amount":4.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t100",
        instruction="You modestly trim ad set 104’s daily budget from 740.0 to 735.0 effective 2025-08-18T16:52:00Z with reason pacing_smooth. Record AR-20250818-120 (budget_apply, started_at 2025-08-18T16:52:00Z, input_ref adset:104), close it at 2025-08-18T16:52:00Z, and verify.",
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="update_adset_budget",
                   kwargs={"adset_id": "104", "new_budget": 735.0, "updated_at": "2025-08-18T16:52:00Z"}),
            Action(name="log_budget_change", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 735.0,
                                                     "changed_at": "2025-08-18T16:52:00Z",
                                                     "reason": "pacing_smooth"}),
            Action(name="create_automation_run",
                   kwargs={"run_id": "AR-20250818-120", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:52:00Z", "input_ref": "adset:104"}),
            Action(name="update_automation_run_end",
                   kwargs={"run_id": "AR-20250818-120", "ended_at": "2025-08-18T16:52:00Z"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_budget":735.0}]']
    )
]

