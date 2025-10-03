from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="sma_t1",
        instruction=(
            "Handle the alignment of ad set 101 with the approved 2025-08-13 plan (plan_2025-08-13) in accordance with policy guidelines. Make certain the ad set exhibits a daily_budget of 950.0 effective from 2025-08-15T02:10:00Z and ensures a cost_cap with a bid_amount of 35.0 effective from 2025-08-15T02:15:00Z. Your audit trail needs to include AR-20250815-01 as a plan_freeze for the plan (covering 2025-08-15T02:00:00Z–2025-08-15T02:01:00Z), AR-20250815-02 as a budget_apply window encompassing the 02:10:00Z budget change (extending over 02:10:00Z–02:12:00Z), and AR-20250815-03 as a strategy_apply window encompassing the 02:15:00Z bidding change (extending over 02:15:00Z–02:16:00Z). Utilize reason plan_2025-08-13 and observe the read-modify-write process by deriving prior values from a pre-change read. Conduct a final state read."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),

            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250815-01", "run_type": "plan_freeze",
                           "started_at": "2025-08-15T02:00:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250815-01", "ended_at": "2025-08-15T02:01:00Z"}),

            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250815-02", "run_type": "budget_apply",
                           "started_at": "2025-08-15T02:10:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 950.0, "updated_at": "2025-08-15T02:10:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0,
                           "changed_at": "2025-08-15T02:10:00Z", "reason": "plan_2025-08-13"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250815-02", "ended_at": "2025-08-15T02:12:00Z"}),

            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250815-03", "run_type": "strategy_apply",
                           "started_at": "2025-08-15T02:15:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0,
                           "updated_at": "2025-08-15T02:15:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 32.0, "new_bid": 35.0,
                           "changed_at": "2025-08-15T02:15:00Z", "reason": "plan_2025-08-13"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250815-03", "ended_at": "2025-08-15T02:16:00Z"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"})
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
            "Coordinate the rotation of creatives for ad set 102 at 2025-08-15T03:00:00Z by activating ad 1104 and pausing ad 1103 with rationale carousel uplift. Verify that creative types are canonical, capture insights from 2025-08-13 both before and after, and maintain a concise audit trail."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "102", "date": "2025-08-13"}),

            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250815-03", "run_type": "creative_rotation",
                           "started_at": "2025-08-15T03:00:00Z", "ended_at": "2025-08-15T03:01:00Z",
                           "status": "completed", "input_ref": "adset_102_rotation_1103_1104",
                           "errors_json": "{}"}),

            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-15T03:00:00Z", "rationale": "carousel uplift"}),

            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "102", "date": "2025-08-13"}),

            Action(name="CreateAutomationRun",
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
            "Handle the rebalancing of Apparel deterministically for ad set 102 on 2025-08-19T11:40:00Z in accordance with policy (ensure rounding and max totals are respected). Elevate its daily budget to 610.0, document the alteration with reason apparel_topup_1140, and confirm the update right after. Maintain a succinct audit record (AR-20250819-04, budget_rebalance, 11:40:00Z–11:40:30Z, completed, input_ref adset_102)."
        ),
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_daily_budget_total"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 610.0, "updated_at": "2025-08-19T11:40:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 610.0,
                           "changed_at": "2025-08-19T11:40:00Z", "reason": "apparel_topup_1140"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-04", "run_type": "budget_rebalance",
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
            "Coordinate a KPI snapshot for ad set 101 as recorded on 2025-08-13 and log an audit run (run_id kpi_snapshot_101_2025-08-13; started_at 2025-08-13T00:00:00Z; ended_at 2025-08-13T00:00:01Z; status completed; input_ref adset:101|baseline:2025-08-13). Present ROAS and CTR for 2025-08-13 and the total expenditure for 2025-08-07..2025-08-13, additionally listing ad sets below min_roas_threshold_7d for 2025-08-13. This task is for observation only; do not modify budgets, bids, or creatives."
        ),
        actions=[
            Action(name="CreateAutomationRun", kwargs={
                "run_id": "kpi_snapshot_101_2025-08-13",
                "run_type": "kpi_snapshot",
                "started_at": "2025-08-13T00:00:00Z",
                "ended_at": "2025-08-13T00:00:00Z",
                "status": "in_progress",
                "input_ref": "adset:101|baseline:2025-08-13",
                "errors_json": "{}"
            }),
            Action(name="GetPolicyParameter", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="UpdateAutomationRunEnd", kwargs={
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
            "Handle the creation and implementation of a two-line plan for 2025-08-27 across 102 and 112. Plan plan_2025-08-27b (author planning_agent_v1, created_at 2025-08-27T01:58:40Z, checksum p27b1360) totals 1360.0: 102 → 600.0 (lowest_cost, image), 112 → 760.0 (lowest_cost, image). Coordinate the freeze (AR-20250827-04, 01:58:40Z–02:00:10Z). Apply both budgets at 02:05:00Z using the reason plan_2025-08-27b and verify."
        ),
        actions=[
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 1360.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="CreatePlan",
                   kwargs={"plan_id": "plan_2025-08-27b", "date": "2025-08-27", "total_budget": 1360.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-27T01:58:40Z",
                           "checksum": "p27b1360", "allocations": [
                           {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-27"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250827-04", "run_type": "plan_freeze",
                                                         "started_at": "2025-08-27T01:58:40Z",
                                                         "ended_at": "2025-08-27T02:00:10Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-27b"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 600.0, "updated_at": "2025-08-27T02:05:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0,
                           "changed_at": "2025-08-27T02:05:00Z", "reason": "plan_2025-08-27b"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 760.0, "updated_at": "2025-08-27T02:05:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 760.0,
                           "changed_at": "2025-08-27T02:05:00Z", "reason": "plan_2025-08-27b"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
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
            "Conduct a plan-driven creative rotation for ad set 102 on 2025-08-28: activate the carousel and pause the prior image to alleviate fatigue. Utilize plan_2025-08-28c as the audit reason. Record AR-20250828-06 (creative_rotation, 10:00:00Z–10:02:00Z, completed, input_ref adset:102|rotation). Confirm canonical creative types, document pre/post ad listings, and register the rotation using the plan_id reason."
        ),
        actions=[
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250828-06", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-28T10:00:00Z",
                                                         "ended_at": "2025-08-28T10:02:00Z", "status": "completed",
                                                         "input_ref": "adset:102|rotation", "errors_json": "{}"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-28T10:01:00Z", "rationale": "plan_2025-08-28c"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
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
            "Coordinate the alignment of ad set 103 with the approved plan dated 2025-08-13 in a policy-driven manner. Set the daily_budget to 1120.0 starting 2025-08-15T02:30:00Z and simultaneously apply a cost_cap with a bid_amount of 6.5. Conduct a minimal audit and confirm the final state without generating any new ads."
        ),
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),

            Action(name="ValidateAllocationsAgainstPolicy", kwargs={
                "total_budget": 1120.0,
                "allocations": [
                    {"adset_id": "103", "budget": 1120.0, "bid_strategy": "cost_cap", "bid_amount": 6.5,
                     "creative_type": "video"}
                ]
            }),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "103", "new_budget": 1120.0, "updated_at": "2025-08-15T02:30:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 1120.0,
                           "changed_at": "2025-08-15T02:30:00Z", "reason": "plan_2025-08-13"}),

            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 6.5,
                           "updated_at": "2025-08-15T02:30:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.5, "changed_at": "2025-08-15T02:30:00Z",
                           "reason": "plan_2025-08-13"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
        ],
        outputs=['[{"adset_id":"103","final_budget":1120.0,"final_bid_amount":6.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t8",
        instruction=(
            "Modify bids reflecting the confirmed 2025-08-14 price for product 1. Configure ad set 101 to cost_cap with a bid of 38.0 as of 2025-08-15T05:20:00Z and set ad set 104 to cost_cap with a bid of 22.0 starting 2025-08-15T05:25:00Z. Document each modification mentioning the reason price_2025-08-14, and report the ROAS for both ad sets as of 2025-08-13. Keep the audit brief and refrain from naming any internal tools or tables."
        ),
        actions=[
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "1", "date": "2025-08-14"}),
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 38.0,
                           "updated_at": "2025-08-15T05:20:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0,
                           "new_bid": 38.0, "changed_at": "2025-08-15T05:20:00Z", "reason": "price_2025-08-14"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-15T05:25:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 22.0, "changed_at": "2025-08-15T05:25:00Z", "reason": "price_2025-08-14"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"})
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
        instruction="Handle the update of creatives for ad set 102 by incorporating a new carousel ad titled Autumn Carousel and initiate its activation by launching the new ad while pausing ad 1103 at 2025-08-17T10:06:00Z, applying rationale format test. You should document run AR-20250817-03 (creative_refresh, 2025-08-17T10:05:00Z–2025-08-17T10:07:00Z, completed, input_ref adset_102_autumn_carousel, errors_json {}). Following rotation, compile the ads and provide a baseline insights report for ad set 102 on 2025-08-13.",
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="CreateAd", kwargs={"adset_id": "102", "name": "Autumn Carousel", "creative_type": "carousel",
                                             "start_date": "2025-08-17"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                                                         "rotated_at": "2025-08-17T10:06:00Z",
                                                         "rationale": "format test"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250817-03", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-17T10:05:00Z",
                                                         "ended_at": "2025-08-17T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset_102_autumn_carousel",
                                                         "errors_json": "{}"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "102", "date": "2025-08-13"})
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
        instruction="Coordinate the scaling of ad set 101 based on the performance of 2025-08-13. Utilizing max_daily_budget_total from policy and citing ROAS=10.0 on 2025-08-13 as the basis, deliver the following end state: adjust the daily_budget to 1050.0 taking effect at 2025-08-15T05:40:00Z; ensure a budget change audit entry is made with change_id BC-8 and reason scale_up_2025-08-13, assuming the current highest change_id is BC-7 in the database; log an automation run AR-20250815-10 of type scale_up for 2025-08-15T05:40:00Z–2025-08-15T05:42:00Z with status completed and input_ref adset_101_scale_up; attach a spend summary for 2025-08-07 through 2025-08-13 along with the insights snapshot for 2025-08-13.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_daily_budget_total"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 1050.0, "updated_at": "2025-08-15T05:40:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 1050.0,
                                                     "changed_at": "2025-08-15T05:40:00Z",
                                                     "reason": "scale_up_2025-08-13"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250815-10", "run_type": "scale_up", "started_at": "2025-08-15T05:40:00Z",
                           "ended_at": "2025-08-15T05:42:00Z", "status": "completed", "input_ref": "adset_101_scale_up",
                           "errors_json": "{}"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "101", "date": "2025-08-13"})
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
        instruction="Handle the creation and freezing of a daily plan for 2025-08-16. Ensure this end state is achieved: a plan plan_2025-08-16 exists with a total_budget of 1670.0, author planning_agent_v1, created_at 2025-08-16T01:59:00Z, checksum p16x1670, and allocations: ad set 101 with budget 950.0 using cost_cap bid_amount 35.0 and creative_type video, and ad set 112 with budget 720.0 using lowest_cost and creative_type image. Validate this against canonical strategies and creative types as well as against policy. Ensure accessibility of the plan by date 2025-08-16 and record AR-20250816-01 (plan_create, 2025-08-16T01:58:00Z–2025-08-16T02:00:00Z, completed, input_ref plan_2025-08-16, errors_json {}).",
        actions=[
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 1670.0, "allocations": [
                {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                 "creative_type": "video"},
                {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost", "creative_type": "image"}
            ]}),
            Action(name="CreatePlan",
                   kwargs={"plan_id": "plan_2025-08-16", "date": "2025-08-16", "total_budget": 1670.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-16T01:59:00Z", "checksum": "p16x1670",
                           "allocations": [
                               {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                                "creative_type": "video"},
                               {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost",
                                "creative_type": "image"}
                           ]}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-16"}),
            Action(name="CreateAutomationRun",
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
        instruction="Address the low ROAS for ad set 110 from the 2025-08-13 evaluation using min_roas_threshold_7d=1.5. Ensure this end state is completed: the daily_budget is set to 800.0 effective at 2025-08-17T09:00:00Z with a budget change logged under reason low_roas_2025-08-13; a new video ad named Android CTA Variant is present in ad set 110 with start_date 2025-08-17 and is active while ad 1114 is on pause; log the creative rotation with rationale cta_test at 2025-08-17T09:01:00Z; and record AR-20250817-02 (roas_mitigation, 2025-08-17T09:00:00Z–2025-08-17T09:03:00Z, completed, input_ref adset_110_roas_remedy, errors_json {}). Ensure the ability to list the ads for ad set 110 following these updates.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "min_roas_threshold_7d"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "110", "new_budget": 800.0, "updated_at": "2025-08-17T09:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 800.0,
                                                     "changed_at": "2025-08-17T09:00:00Z",
                                                     "reason": "low_roas_2025-08-13"}),
            Action(name="CreateAd", kwargs={"adset_id": "110", "name": "Android CTA Variant", "creative_type": "video",
                                             "start_date": "2025-08-17"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1114"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "110", "old_ad_id": "1114", "new_ad_id": "1119",
                                                         "rotated_at": "2025-08-17T09:01:00Z",
                                                         "rationale": "cta_test"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250817-02", "run_type": "roas_mitigation",
                                                         "started_at": "2025-08-17T09:00:00Z",
                                                         "ended_at": "2025-08-17T09:03:00Z", "status": "completed",
                                                         "input_ref": "adset_110_roas_remedy", "errors_json": "{}"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "110"})
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
            "Manage video engagement prioritization for ad set 108 using the 2025-08-13 baseline. Achieve this outcome: ad 1112 remains active and ad 1111 is paused at 2025-08-16T09:00:00Z; document the rotation with the rationale video_preference; record AR-20250816-02 (creative_rotation, 2025-08-16T09:00:00Z–2025-08-16T09:02:00Z, completed, input_ref adset_108_video_shift); and compile a report on CTR along with an insights snapshot for 2025-08-13 including the revised ad list."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "108"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),

            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1112", "ad_id_to_pause": "1111"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "108", "old_ad_id": "1111", "new_ad_id": "1112",
                                                         "rotated_at": "2025-08-16T09:00:00Z",
                                                         "rationale": "video_preference"}),

            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250816-02", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-16T09:00:00Z",
                                                         "ended_at": "2025-08-16T09:02:00Z", "status": "completed",
                                                         "input_ref": "adset_108_video_shift", "errors_json": "{}"}),

            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "108"})
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
            "Revitalize creative for ad set 101 by utilizing the 2025-08-13 baseline. Ensure this end state: a new image ad titled 'Smartphone X Image v2' is added to ad set 101, starting 2025-08-17 and is active; ad 1101 becomes paused at 2025-08-17T11:00:00Z; register the rotation with the rationale freshness; log AR-20250817-04 (creative_refresh, 2025-08-17T10:59:00Z–2025-08-17T11:01:00Z, completed, input_ref adset_101_image_refresh); and furnish the updated ad list along with the ROAS for 2025-08-13."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "101", "date": "2025-08-13"}),

            Action(name="CreateAd",
                   kwargs={"adset_id": "101", "name": "Smartphone X Image v2", "creative_type": "image",
                           "start_date": "2025-08-17"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1101"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "101", "old_ad_id": "1101", "new_ad_id": "1119",
                                                         "rotated_at": "2025-08-17T11:00:00Z",
                                                         "rationale": "freshness"}),

            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250817-04", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-17T10:59:00Z",
                                                         "ended_at": "2025-08-17T11:01:00Z", "status": "completed",
                                                         "input_ref": "adset_101_image_refresh", "errors_json": "{}"}),

            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "101"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"})
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
        instruction="Handle the scaling of ad set 105 based on its strong performance on 2025-08-13 while adhering to policy rounding. Achieve this final state: set daily_budget to 820.0 effective at 2025-08-16T08:00:00Z using budget_rounding_unit=10, ensure the change is logged stating reason scale_up_2025-08-13, AR-20250816-03 (scale_up, 2025-08-16T08:00:00Z–2025-08-16T08:02:00Z, completed, input_ref adset_105_scale_up, errors_json {}) is documented, and provide spend data from 2025-08-07 to 2025-08-13 along with the insights snapshot for 2025-08-13.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "105", "new_budget": 820.0, "updated_at": "2025-08-16T08:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 820.0,
                                                     "changed_at": "2025-08-16T08:00:00Z",
                                                     "reason": "scale_up_2025-08-13"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250816-03", "run_type": "scale_up", "started_at": "2025-08-16T08:00:00Z",
                           "ended_at": "2025-08-16T08:02:00Z", "status": "completed", "input_ref": "adset_105_scale_up",
                           "errors_json": "{}"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "105", "date": "2025-08-13"})
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
            "Coordinate the mitigation of underperformers from 2025-08-13 (threshold 1.5) in a policy-compliant, audited manner. Reduce ad set 110 to a daily_budget of 900.0 at 2025-08-19T11:00:00Z and log this change citing reason underperforming_2025-08-13; adjust ad set 111 cost_cap bid to 2.0 at 11:02:00Z with the same justification; confirm after each adjustment. Document a succinct run (AR-20250819-06, mitigation_apply, 11:00:00Z–11:05:00Z, completed, input_ref underperforming_2025-08-13)."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "110", "new_budget": 900.0, "updated_at": "2025-08-19T11:00:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 900.0,
                           "changed_at": "2025-08-19T11:00:00Z", "reason": "underperforming_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.0,
                           "updated_at": "2025-08-19T11:02:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 2.5, "new_bid": 2.0, "changed_at": "2025-08-19T11:02:00Z",
                           "reason": "underperforming_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),

            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-06", "run_type": "mitigation_apply",
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
            "Handle a clean creative rotation for ad set 102 utilizing canonical types at 2025-08-24T10:06:00Z: activate carousel 1104, pause image 1103, rationale format_test_carousel. Check with AR-20250824-06 (creative_rotation, 10:05:00Z–10:07:00Z, completed, input_ref adset:102|1103->1104) and confirm ads after rotation."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250824-06", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-24T10:05:00Z",
                                                         "ended_at": "2025-08-24T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset:102|1103->1104", "errors_json": "{}"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-24T10:06:00Z", "rationale": "format_test_carousel"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
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
        instruction="Coordinate the true-up of ad set 104 to align with the frozen plan for 2025-08-13. Achieve this final state: ad set 104 has daily_budget 750.0 and bid_strategy cost_cap with bid_amount 22.0 active at 2025-08-17T12:40:00Z–2025-08-17T12:41:00Z, both modifications logged with reason plan_2025-08-13_true_up, and AR-20250817-07 (plan_true_up, 2025-08-17T12:40:00Z–2025-08-17T12:42:00Z, completed, input_ref plan_2025-08-13, errors_json {}) documented. Understand the plan and specific allocation for ad set 104 prior to applying the updates.",
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "104", "new_budget": 750.0, "updated_at": "2025-08-17T12:40:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 750.0,
                                                     "changed_at": "2025-08-17T12:40:00Z",
                                                     "reason": "plan_2025-08-13_true_up"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-17T12:41:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 22.0, "changed_at": "2025-08-17T12:41:00Z", "reason": "plan_2025-08-13_true_up"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250817-07", "run_type": "plan_true_up", "started_at": "2025-08-17T12:40:00Z",
                           "ended_at": "2025-08-17T12:42:00Z", "status": "completed", "input_ref": "plan_2025-08-13",
                           "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"})
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
            "Handle the underperformers identified on 2025-08-13 by reducing 110 and adjusting 111 while maintaining cost_cap. Adjust 110 daily_budget to 920.0 at 11:10:00Z and modify 111 bid_amount to 2.1 at 11:12:00Z citing reason underperforming_2025-08-13, confirm after changes, and register AR-20250827-06 (mitigation_apply, 11:10:00Z–11:13:00Z, completed, input_ref underperf_2025-08-13_pair_b)."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "110", "new_budget": 920.0, "updated_at": "2025-08-27T11:10:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 920.0,
                           "changed_at": "2025-08-27T11:10:00Z", "reason": "underperforming_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.1,
                           "updated_at": "2025-08-27T11:12:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 2.5, "new_bid": 2.1, "changed_at": "2025-08-27T11:12:00Z",
                           "reason": "underperforming_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),

            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250827-06", "run_type": "mitigation_apply",
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
            "Coordinate and assess a plan for 2025-08-16 with two allocations, then ensure retrieval confirmation. The plan should be plan_2025-08-16 with total_budget 1670.0, author planning_agent_v1, created_at 2025-08-16T01:59:00Z, checksum p16x1670, and allocations: ad set 101 (950.0, cost_cap bid 35.0, creative video) and ad set 112 (720.0, lowest_cost, creative image). Maintain a concise creation audit (AR-20250816-01, plan_create, 01:58:00Z–02:00:00Z, completed, input_ref plan_2025-08-16)."
        ),
        actions=[
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 1670.0, "allocations": [
                {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                 "creative_type": "video"},
                {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost", "creative_type": "image"}
            ]}),
            Action(name="CreatePlan",
                   kwargs={"plan_id": "plan_2025-08-16", "date": "2025-08-16", "total_budget": 1670.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-16T01:59:00Z", "checksum": "p16x1670",
                           "allocations": [
                               {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                                "creative_type": "video"},
                               {"adset_id": "112", "budget": 720.0, "bid_strategy": "lowest_cost",
                                "creative_type": "image"}
                           ]}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-16"}),
            Action(name="CreateAutomationRun",
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
            "Handle the use of 2025-08-13 Electronics viewership and week-of-2025-08-07 sales as context to manage ad set 101 conservatively. Increase its daily budget to 960.0 at 2025-08-19T09:15:00Z, document this with the reason pacing_electronics_2025-08-13, verify promptly after the adjustment, and maintain a brief audit window (AR-20250819-08, pacing_apply, 09:15:00Z–09:16:00Z, completed, input_ref adset_101_pacing)."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetWeeklySalesByCategory", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 960.0, "updated_at": "2025-08-19T09:15:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 960.0,
                           "changed_at": "2025-08-19T09:15:00Z", "reason": "pacing_electronics_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-08", "run_type": "pacing_apply",
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
        instruction="Oversee the implementation of bidding policy for ad set 111 using 2025-08-13 baselines. Ensure this end state: ad set 111 operates with cost_cap using bid_amount 2.5 effective at 2025-08-17T12:20:00Z and this modification is logged with the reason policy_enforcement_2025-08-13; AR-20250817-10 (bid_policy_true_up, 2025-08-17T12:20:00Z–2025-08-17T12:22:00Z, completed, input_ref adset_111_bid_enforcement, errors_json {}) notated. Refer to max_bid_amount and standardized bid strategies and include ROAS for 2025-08-13.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_bid_amount"}),
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5,
                           "updated_at": "2025-08-17T12:20:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5,
                           "new_bid": 2.5, "changed_at": "2025-08-17T12:20:00Z",
                           "reason": "policy_enforcement_2025-08-13"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250817-10", "run_type": "bid_policy_true_up",
                                                         "started_at": "2025-08-17T12:20:00Z",
                                                         "ended_at": "2025-08-17T12:22:00Z", "status": "completed",
                                                         "input_ref": "adset_111_bid_enforcement",
                                                         "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"})
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
        instruction="Handle the creation and freezing of a daily plan for 2025-08-18. The final state must include: a plan plan_2025-08-18 with total_budget 2380.0, author planning_agent_v1, created_at 2025-08-18T01:59:00Z, checksum p18x2380, and allocations: ad set 102 with budget 600.0 using lowest_cost and creative_type carousel, ad set 110 with budget 1000.0 using lowest_cost and creative_type video, ad set 101 with budget 780.0 using cost_cap bid_amount 35.0 and creative_type video. Validate against canonical strategies and creative types as well as policy requirements. Ensure you can retrieve the plan and document AR-20250818-02 (plan_create, 2025-08-18T01:58:00Z–2025-08-18T02:00:00Z, completed, input_ref plan_2025-08-18, errors_json {}).",
        actions=[
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 2380.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "carousel"},
                {"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost", "creative_type": "video"},
                {"adset_id": "101", "budget": 780.0, "bid_strategy": "cost_cap", "bid_amount": 35.0,
                 "creative_type": "video"}
            ]}),
            Action(name="CreatePlan",
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
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-18"}),
            Action(name="CreateAutomationRun",
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
            "Coordinate adding a new carousel to ad set 102 and set it live: create 'Back to School Carousel' (start_date 2025-08-24), activate the new ad, and pause 1103 at 10:08:00Z (rationale school_season_test). Document AR-20250824-07 (creative_refresh, 10:07:00Z–10:09:00Z, completed, input_ref adset_102_b2s) and confirm ad verification."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="CreateAd",
                   kwargs={"adset_id": "102", "name": "Back to School Carousel", "creative_type": "carousel",
                           "start_date": "2025-08-24"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250824-07", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-24T10:07:00Z",
                                                         "ended_at": "2025-08-24T10:09:00Z", "status": "completed",
                                                         "input_ref": "adset_102_b2s", "errors_json": "{}"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                           "rotated_at": "2025-08-24T10:08:00Z", "rationale": "school_season_test"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
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
            "Handle the rebalancing of Electronics budgets across ad sets 101, 108, and 112 ensuring a policy-compliant and audited process. Refer to spend data from 2025-08-07 to 2025-08-13 and ROAS statistics on 2025-08-13 as context, then explicitly set the final budgets to 101→860.0, 108→780.0, 112→680.0 with effect from 2025-08-18T10:00:00Z. Capture the previous values from pre-change inspections and document each alteration with the reason electronics_three_way_rebalance_2025-08-13. Record a concise category_rebalance run AR-20250818-04 beginning at 2025-08-18T10:00:00Z and conclude it at 2025-08-18T10:03:00Z."
        ),
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "min_budget_allocation"}),

            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "101", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "112", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CreateAutomationRun", kwargs={
                "run_id": "AR-20250818-04",
                "run_type": "category_rebalance",
                "started_at": "2025-08-18T10:00:00Z",
                "input_ref": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 860.0, "updated_at": "2025-08-18T10:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={
                "adset_id": "101",
                "old_budget": 920.0,
                "new_budget": 860.0,
                "changed_at": "2025-08-18T10:00:00Z",
                "reason": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "108", "new_budget": 780.0, "updated_at": "2025-08-18T10:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={
                "adset_id": "108",
                "old_budget": 780.0,
                "new_budget": 780.0,
                "changed_at": "2025-08-18T10:00:00Z",
                "reason": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 680.0, "updated_at": "2025-08-18T10:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={
                "adset_id": "112",
                "old_budget": 700.0,
                "new_budget": 680.0,
                "changed_at": "2025-08-18T10:00:00Z",
                "reason": "electronics_three_way_rebalance_2025-08-13"
            }),

            Action(name="UpdateAutomationRunEnd",
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
            "Coordinate the return of ad set 103 to policy compliance according to the approved baseline plan_2025-08-13 and the observed ROAS on 2025-08-13. Adjust daily_budget to 980.0 effective 2025-08-19T04:10:00Z and transition to a cost_cap bid of 15.0 at 04:12:00Z, using the plan_id as justification and verify after each modification. Maintain a compact mitigation audit record (AR-20250819-09, underperformance_mitigation, 04:10:00Z–04:13:00Z, completed, input_ref adset_103_2025-08-13)."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),

            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "103", "new_budget": 980.0, "updated_at": "2025-08-19T04:10:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 980.0,
                           "changed_at": "2025-08-19T04:10:00Z", "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),

            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 15.0,
                           "updated_at": "2025-08-19T04:12:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 15.0, "changed_at": "2025-08-19T04:12:00Z",
                           "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),

            Action(name="CreateAutomationRun",
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
            "Ensure you develop and implement a two-line plan for 2025-08-24 across 102 and 112. Plan plan_2025-08-24b (author planning_agent_v1, created_at 2025-08-24T01:58:50Z, checksum p24b1360) amounts to 1360.0: 102 → 600.0 (lowest_cost, image), 112 → 760.0 (lowest_cost, image). Pause (AR-20250824-10, 01:58:50Z–02:00:10Z). Implement both budgets at 02:05:00Z with reason plan_2025-08-24b and confirm."
        ),
        actions=[
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 1360.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="CreatePlan",
                   kwargs={"plan_id": "plan_2025-08-24b", "date": "2025-08-24", "total_budget": 1360.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-24T01:58:50Z",
                           "checksum": "p24b1360", "allocations": [
                           {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-24"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250824-10", "run_type": "plan_freeze",
                                                         "started_at": "2025-08-24T01:58:50Z",
                                                         "ended_at": "2025-08-24T02:00:10Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-24b"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 600.0, "updated_at": "2025-08-24T02:05:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0,
                           "changed_at": "2025-08-24T02:05:00Z", "reason": "plan_2025-08-24b"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 760.0, "updated_at": "2025-08-24T02:05:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 760.0,
                           "changed_at": "2025-08-24T02:05:00Z", "reason": "plan_2025-08-24b"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
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
            "You need to capture a monitoring snapshot at 2025-08-18T11:20:00Z that represents recent plan execution and baseline performance. Compile a summary of recent plan_freeze reliability and incorporate a lightweight KPI echo for 2025-08-13 (ROAS and CTR for ad set 101). Record this as a completed automation run AR-20250818-10 (run_type monitoring_snapshot) with input_ref success_rate_percent=100.0;snapshot_runs=2, and then verify the snapshot's availability."
        ),
        actions=[
            Action(name="GetAutomationRunHistory", kwargs={"run_type": "plan_freeze", "limit": 2}),

            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),

            Action(name="CreateAutomationRun", kwargs={
                "run_id": "AR-20250818-10",
                "run_type": "monitoring_snapshot",
                "started_at": "2025-08-18T11:20:00Z",
                "ended_at": "2025-08-18T11:20:00Z",
                "status": "completed",
                "input_ref": "success_rate_percent=100.0;snapshot_runs=2",
                "errors_json": "{}"
            }),

            Action(name="GetAutomationRunHistory", kwargs={"run_type": "monitoring_snapshot", "limit": 1})
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
            "Handle a small rounding-compliant top-up for ad set 101. At 2025-08-24T09:40:00Z, adjust the daily_budget to 960.0 using budget_rounding_unit, log the reason as rounding_topup_2025-08-24, verify the actions, and record AR-20250824-14 (budget_rebalance, 09:40:00Z–09:41:00Z, completed, input_ref adset_101_rounding_topup)."
        ),
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 960.0, "updated_at": "2025-08-24T09:40:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 960.0,
                           "changed_at": "2025-08-24T09:40:00Z", "reason": "rounding_topup_2025-08-24"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250824-14", "run_type": "budget_rebalance",
                                                         "started_at": "2025-08-24T09:40:00Z",
                                                         "ended_at": "2025-08-24T09:41:00Z", "status": "completed",
                                                         "input_ref": "adset_101_rounding_topup", "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"101","final_daily_budget":960.0},{"automation_run":"AR-20250824-14"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t30",
        instruction="Coordinate the pausing of the Q3 Brand Awareness Push campaign and optimize its primary ad set. The end state to achieve: campaign Q3 Brand Awareness Push is in status paused; ad set 103 transitions to cost_cap with bid_amount 20.0 at 2025-08-18T11:20:00Z, documented with reason brand_efficiency_2025-08-13; record AR-20250818-09 (brand_pause_opt, 2025-08-18T11:19:00Z–2025-08-18T11:21:00Z, completed, input_ref brand_pause_opt_2025-08-18, errors_json {}) and list the campaign ad sets.",
        actions=[
            Action(name="GetCampaignByName", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="UpdateCampaignStatus", kwargs={"campaign_id": "2", "status": "paused"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "2"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 20.0,
                           "updated_at": "2025-08-18T11:20:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 20.0, "changed_at": "2025-08-18T11:20:00Z",
                           "reason": "brand_efficiency_2025-08-13"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250818-09", "run_type": "brand_pause_opt",
                                                         "started_at": "2025-08-18T11:19:00Z",
                                                         "ended_at": "2025-08-18T11:21:00Z", "status": "completed",
                                                         "input_ref": "brand_pause_opt_2025-08-18",
                                                         "errors_json": "{}"}),
            Action(name="GetAdsetsByCampaignId", kwargs={"campaign_id": "2"})
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
        instruction="Handle the refresh of the creative mix within the Summer T-Shirt ad set. Evaluate the ads in ad set 102, thereafter activate 1104 and place 1103 on pause as part of a rotation, documenting the rotation with the justification cta_focus at 2025-08-18T11:30:00Z. Register AR-20250818-10 as a completed creative_rotation run with started_at 2025-08-18T11:30:00Z, ended_at 2025-08-18T11:31:00Z, input_ref adset:102|rotation:1103>1104, errors_json {}.",
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                                                         "rotated_at": "2025-08-18T11:30:00Z",
                                                         "rationale": "cta_focus"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250818-10", "run_type": "creative_rotation",
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
            "You need to coordinate a creative refresh for ad set 102 by incorporating a new carousel ad titled Autumn Carousel (start_date 2025-08-19), then enable the new ad and pause 1103 at 10:06:00Z citing the rationale format_test. Implement a minimal audit window (AR-20250819-10, creative_refresh, 10:05:00Z–10:07:00Z, completed, input_ref adset_102_autumn_carousel) and ensure ads are verified post-rotation."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="CreateAd", kwargs={"adset_id": "102", "name": "Autumn Carousel", "creative_type": "carousel",
                                             "start_date": "2025-08-19"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-10", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-19T10:05:00Z",
                                                         "ended_at": "2025-08-19T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset_102_autumn_carousel",
                                                         "errors_json": "{}"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                           "rotated_at": "2025-08-19T10:06:00Z", "rationale": "format_test"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
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
            "Handle ad set 112 scaling responsibly per policy, by utilizing rounding and maximum limits. Adjust its daily_budget to 820.0 effective 2025-08-19T11:50:00Z, record with reason scale_up_policy_2025-08-13, confirm the amendment, and maintain a brief execution (AR-20250819-12, scale_up, 11:50:00Z–11:52:00Z, completed, input_ref adset_112_scale_up)."
        ),
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "max_daily_budget_total"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 820.0, "updated_at": "2025-08-19T11:50:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 820.0,
                           "changed_at": "2025-08-19T11:50:00Z", "reason": "scale_up_policy_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-12", "run_type": "scale_up",
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
            "Coordinate the auditing and nudging of ad set 104 based on 2025-08-13 performance, ensuring creatives remain unchanged. Increase its cost_cap bid to 22.0 effective 2025-08-19T05:25:00Z, document with reason light_scale_2025-08-13, validate post-modification, and document a brief execution (AR-20250819-13, strategy_apply, 05:25:00Z–05:26:00Z, completed, input_ref adset_104_scale)."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-19T05:25:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 20.0, "new_bid": 22.0, "changed_at": "2025-08-19T05:25:00Z",
                           "reason": "light_scale_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-13", "run_type": "strategy_apply",
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
        instruction="Ensure the 2025-08-13 plan is applied solely to ad sets 101 and 112. Achieve this final state: ad set 101 with a daily_budget of 950.0 and a cost_cap bid_amount of 35.0; ad set 112 with a daily_budget of 700.0 using lowest_cost; all effective from 2025-08-18T12:10:00Z–2025-08-18T12:12:00Z; document all modifications noting the reason partial_plan_apply_2025-08-13; AR-20250818-13 (budget_apply, 2025-08-18T12:10:00Z–2025-08-18T12:13:00Z, completed, input_ref plan_2025-08-13_partial, errors_json {}) logged.",
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 950.0, "updated_at": "2025-08-18T12:10:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 950.0,
                                                     "changed_at": "2025-08-18T12:10:00Z",
                                                     "reason": "partial_plan_apply_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0,
                           "updated_at": "2025-08-18T12:11:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 32.0,
                           "new_bid": 35.0, "changed_at": "2025-08-18T12:11:00Z",
                           "reason": "partial_plan_apply_2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 700.0, "updated_at": "2025-08-18T12:12:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 700.0,
                                                     "changed_at": "2025-08-18T12:12:00Z",
                                                     "reason": "partial_plan_apply_2025-08-13"}),
            Action(name="CreateAutomationRun",
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
            "Organize and secure a compact plan for 2025-08-25 featuring two allocations, and validate retrieval. Plan plan_2025-08-25b sums to 1360.0 (author planning_agent_v1, created_at 2025-08-25T01:59:30Z, checksum p25b1360): 102 → 600.0 (lowest_cost, image), 112 → 760.0 (lowest_cost, image). Incorporate AR-20250825-05 (plan_create, 01:59:00Z–02:00:00Z, completed)."
        ),
        actions=[
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 1360.0, "allocations": [
                {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="CreatePlan",
                   kwargs={"plan_id": "plan_2025-08-25b", "date": "2025-08-25", "total_budget": 1360.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-25T01:59:30Z",
                           "checksum": "p25b1360", "allocations": [
                           {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-25"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250825-05", "run_type": "plan_create",
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
            "Handle the conservative mitigation of underperformance for ad set 110 identified on 2025-08-13 (threshold 1.5). Adjust the daily_budget to 950.0 at 2025-08-19T11:10:00Z, note the alteration with the reason underperforming_2025-08-13, confirm the updated status, and document a brief period for mitigation_apply execution (AR-20250819-16, 11:10:00Z–11:11:00Z, completed, input_ref adset_110_mitigation)."
        ),
        actions=[
            Action(name="FindUnderperformingAdsets", kwargs={"roas_threshold": 1.5, "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "110", "new_budget": 950.0, "updated_at": "2025-08-19T11:10:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 950.0,
                           "changed_at": "2025-08-19T11:10:00Z", "reason": "underperforming_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-16", "run_type": "mitigation_apply",
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
            "Coordinate the tightening of ad set 111 bidding according to policy while ensuring the cost_cap remains intact. Decrease bid_amount to 2.2 starting 2025-08-19T11:20:00Z for the reason underperforming_2025-08-13, validate immediately, and note a concise strategy_apply interval (AR-20250819-17, 11:20:00Z–11:21:00Z, completed, input_ref adset_111_tighten)."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.2,
                           "updated_at": "2025-08-19T11:20:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 2.5, "new_bid": 2.2, "changed_at": "2025-08-19T11:20:00Z",
                           "reason": "underperforming_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-17", "run_type": "strategy_apply",
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
        instruction="Handle the reduction of Mobile performance spending. Ensure this final condition is met: ad set 110 daily_budget 900.0 at 2025-08-18T12:50:00Z logged with reason mobile_scale_down_2025-08-13; AR-20250818-16 (scale_down, 2025-08-18T12:50:00Z–2025-08-18T12:52:00Z, completed, input_ref adset_110_scale_down, errors_json {}) recorded; and catalog its ads and ROAS for 2025-08-13.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "110"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "110"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "110", "new_budget": 900.0, "updated_at": "2025-08-18T12:50:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "110", "old_budget": 1000.0, "new_budget": 900.0,
                                                     "changed_at": "2025-08-18T12:50:00Z",
                                                     "reason": "mobile_scale_down_2025-08-13"}),
            Action(name="CreateAutomationRun",
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
        instruction="Coordinate the resolution of brand video inefficiency. Achieve this end state: ad set 103 daily_budget 950.0 and cost_cap bid_amount 18.0 effective at 2025-08-18T13:00:00Z–2025-08-18T13:02:00Z; all modifications logged with reason brand_video_efficiency_fix_2025-08-13; AR-20250818-17 (brand_efficiency_fix, 2025-08-18T13:00:00Z–2025-08-18T13:03:00Z, completed, input_ref adset_103_brand_fix, errors_json {}) recorded; and deliver the 2025-08-13 insights snapshot.",
        actions=[
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "103", "new_budget": 950.0, "updated_at": "2025-08-18T13:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 950.0,
                                                     "changed_at": "2025-08-18T13:00:00Z",
                                                     "reason": "brand_video_efficiency_fix_2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 18.0,
                           "updated_at": "2025-08-18T13:02:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 18.0, "changed_at": "2025-08-18T13:02:00Z",
                           "reason": "brand_video_efficiency_fix_2025-08-13"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250818-17", "run_type": "brand_efficiency_fix",
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
        instruction="Handle tightening bidding for ad set 104 using policy rules. Verify canonical bid strategies, review the current ad set to capture its existing strategy and bid, and evaluate performance on 2025-08-13. Implement a tighter cost_cap by setting bid_amount to 18.0 effective at 2025-08-18T14:04:00Z. Record the strategy change using the fetched prior values and reason ctr_tighten_2025-08-13. Check the new ad set state afterward.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 18.0,
                           "updated_at": "2025-08-18T14:04:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 18.0, "changed_at": "2025-08-18T14:04:00Z", "reason": "ctr_tighten_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"})
        ],
        outputs=["adset=104 strategy=cost_cap bid=18.0 changed_at=2025-08-18T14:04:00Z reason=ctr_tighten_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t42",
        instruction="Manage retuning bidding for ad set 106 in accordance with policy. Verify canonical bid strategies, examine the ad set to capture its current values, and analyze its performance on 2025-08-13. Alter the bidding to bid_cap with bid_amount 17.0 effective at 2025-08-18T14:08:00Z. Document the strategy change using the fetched prior values and reason performance_rebalance_2025-08-13. Confirm the updated state.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "106", "bid_strategy": "bid_cap", "bid_amount": 17.0,
                           "updated_at": "2025-08-18T14:08:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "106", "old_strategy": "cost_cap", "new_strategy": "bid_cap", "old_bid": 18.0,
                           "new_bid": 17.0, "changed_at": "2025-08-18T14:08:00Z",
                           "reason": "performance_rebalance_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"})
        ],
        outputs=[
            "adset=106 strategy=bid_cap bid=17.0 changed_at=2025-08-18T14:08:00Z reason=performance_rebalance_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t43",
        instruction="Handle the moderate tightening of bidding for ad set 108 as specified by policy. Verify canonical bid strategies, review the current ad set values, and consider its 2025-08-13 results. Retain the cost_cap but adjust the bid_amount down to 40.0 effective at 2025-08-18T14:11:00Z. Record the strategy change with the retrieved old values and rationale cost_cap_tighten_2025-08-13. Confirm the new state.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 40.0,
                           "updated_at": "2025-08-18T14:11:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0,
                           "new_bid": 40.0, "changed_at": "2025-08-18T14:11:00Z",
                           "reason": "cost_cap_tighten_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"})
        ],
        outputs=[
            "adset=108 strategy=cost_cap bid=40.0 changed_at=2025-08-18T14:11:00Z reason=cost_cap_tighten_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t44",
        instruction="Conduct a reduction in over-aggressive bidding for ad set 111. Validate the canonical strategies, examine the ad set state, and incorporate its 2025-08-13 results. Keep the cost_cap but decrease the bid_amount to 2.2 effective at 2025-08-18T14:13:00Z. Archive the change using the obtained prior values citing cap_refinement_2025-08-13 as the reason, and check the new state.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.2,
                           "updated_at": "2025-08-18T14:13:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "111", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 2.5,
                           "new_bid": 2.2, "changed_at": "2025-08-18T14:13:00Z",
                           "reason": "cap_refinement_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"})
        ],
        outputs=["adset=111 strategy=cost_cap bid=2.2 changed_at=2025-08-18T14:13:00Z reason=cap_refinement_2025-08-13"]
    ),
    Task(
        annotator="0",
        user_id="sma_t45",
        instruction="Handle the alignment of ad set 102 with the policy by capping bids: strategy should be cost_cap with a bid_amount of 14.0 effective 2025-08-18T14:15:00Z, record the change citing policy_alignment_2025-08-13, and confirm the updated status. Avoid pulling unrelated insights. For consistency, consider the largest existing strategy_changes ID is SC-4, thus the next log will be SC-5.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 14.0,
                           "updated_at": "2025-08-18T14:15:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 14.0, "changed_at": "2025-08-18T14:15:00Z",
                           "reason": "policy_alignment_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=[
            "adset=102 strategy=cost_cap bid=14.0 changed_at=2025-08-18T14:15:00Z reason=policy_alignment_2025-08-13"
        ]
    ),
    Task(
        annotator="0",
        user_id="sma_t46",
        instruction="Coordinate the alignment of ad set 103 with policy by using a cost cap of 19.0 effective 2025-08-18T14:17:00Z, based on its current state and performance from 2025-08-13 to validate the change. Ensure to maintain a verifiable record of the adjustment with the retrieved prior values and reason baseline_cap_2025-08-13, and confirm the final state.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 19.0,
                           "updated_at": "2025-08-18T14:17:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 19.0, "changed_at": "2025-08-18T14:17:00Z",
                           "reason": "baseline_cap_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"})
        ],
        outputs=["adset=103 strategy=cost_cap bid=19.0 changed_at=2025-08-18T14:17:00Z reason=baseline_cap_2025-08-13"]
    ),
    Task(
        annotator="v6",
        user_id="sma_t47",
        instruction=(
            "You must Handle a clean creative rotation for ad set 102 using canonical types: activate carousel 1104 and pause image 1103 at 2025-08-19T10:06:00Z, utilizing rationale format_test_b. Maintain a concise audit (AR-20250819-18, creative_rotation, 10:05:00Z–10:07:00Z, completed, input_ref adset:102|rotation|1103->1104) and confirm ads post-rotation."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-18", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-19T10:05:00Z",
                                                         "ended_at": "2025-08-19T10:07:00Z", "status": "completed",
                                                         "input_ref": "adset:102|rotation|1103->1104",
                                                         "errors_json": "{}"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                           "rotated_at": "2025-08-19T10:06:00Z", "rationale": "format_test_b"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
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
        instruction="Coordinate the normalization of ad set 112 by transitioning from lowest_cost to cost_cap 4.0 effective 2025-08-18T14:20:00Z with the reason performance_floor. Assess canonical strategies, extract old values from the record, conduct an audit with a one-day ROAS check for 2025-08-13, and then document automation run AR-20250818-67 (run_type strategy_apply) with started_at 2025-08-18T14:20:00Z, ended_at 2025-08-18T14:21:00Z, status completed, input_ref adset:112, errors_json {}. Confirm final state.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "112", "bid_strategy": "cost_cap", "bid_amount": 4.0,
                           "updated_at": "2025-08-18T14:20:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 4.0, "changed_at": "2025-08-18T14:20:00Z",
                           "reason": "performance_floor"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250818-67", "run_type": "strategy_apply",
                                                         "started_at": "2025-08-18T14:20:00Z",
                                                         "ended_at": "2025-08-18T14:21:00Z", "status": "completed",
                                                         "input_ref": "adset:112", "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_bid_strategy":"cost_cap","final_bid_amount":4.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t49",
        instruction=(
            "Ensure to create a KPI snapshot for ad set 103 as of 2025-08-13 and log an audit run (run_id kpi_snapshot_103_2025-08-13; started_at 2025-08-13T00:00:00Z; ended_at 2025-08-13T00:00:01Z; status completed; input_ref adset:103|baseline:2025-08-13). Summarize ROAS and CTR for 2025-08-13 and total spending between 2025-08-07 and 2025-08-13. Read-only."
        ),
        actions=[
            Action(name="CreateAutomationRun", kwargs={
                "run_id": "kpi_snapshot_103_2025-08-13",
                "run_type": "kpi_snapshot",
                "started_at": "2025-08-13T00:00:00Z",
                "ended_at": "2025-08-13T00:00:00Z",
                "status": "in_progress",
                "input_ref": "adset:103|baseline:2025-08-13",
                "errors_json": "{}"
            }),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "103", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="UpdateAutomationRunEnd", kwargs={
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
        instruction="Modify the daily budget for ad set 102 from 590.0 to 610.0 starting 2025-08-18T14:24:00Z with reason apparel_push, using Apparel viewership from 2025-08-13 and recent spend from 2025-08-07 to 2025-08-13 as references. Subsequently, log the automation run AR-20250818-69 (run_type budget_apply) with started_at 2025-08-18T14:24:00Z, ended_at 2025-08-18T14:25:00Z, status completed, input_ref adset:102, errors_json {}. Confirm the final state.",
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "102", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 610.0, "updated_at": "2025-08-18T14:24:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 610.0,
                                                     "changed_at": "2025-08-18T14:24:00Z", "reason": "apparel_push"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-69", "run_type": "budget_apply", "started_at": "2025-08-18T14:24:00Z",
                           "ended_at": "2025-08-18T14:25:00Z", "status": "completed", "input_ref": "adset:102",
                           "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":610.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t51",
        instruction=(
            "Handle the response to verified product 1 price (2025-08-14) by slightly increasing ad set 101 bid under policy safeguards. Adjust the cost_cap bid to 36.0 at 2025-08-19T05:30:00Z citing the reason price_alignment_2025-08-14, confirm after the update, and archive within a short strategy_apply window (AR-20250819-19, 05:30:00Z–05:31:00Z, completed, input_ref adset_101_price_align)."
        ),
        actions=[
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "1", "date": "2025-08-14"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 36.0,
                           "updated_at": "2025-08-19T05:30:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 32.0, "new_bid": 36.0, "changed_at": "2025-08-19T05:30:00Z",
                           "reason": "price_alignment_2025-08-14"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-19", "run_type": "strategy_apply",
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
            "Coordinate a deterministic midday tune for ad set 108: elevate daily_budget to 820.0 and increase the cost_cap bid to 44.0 effective 2025-08-19T12:12:00Z, recording with reason weekday_midday_reactivity and confirm after each adjustment. Document a strategy_apply audit (AR-20250819-20, 12:12:00Z–12:13:00Z, completed, input_ref adset_108_midday)."
        ),
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "108", "new_budget": 820.0, "updated_at": "2025-08-19T12:12:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 820.0,
                           "changed_at": "2025-08-19T12:12:00Z", "reason": "weekday_midday_reactivity"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 44.0,
                           "updated_at": "2025-08-19T12:12:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 42.0, "new_bid": 44.0, "changed_at": "2025-08-19T12:12:00Z",
                           "reason": "weekday_midday_reactivity"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-20", "run_type": "strategy_apply",
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
        instruction="Adjust the daily budget for ad set 105 from 750.0 to 720.0 effective 2025-08-18T14:30:00Z due to inventory_softening, while referring to Office viewership on 2025-08-13 and recent spend from 2025-08-07 through 2025-08-13. Log a completed automation run AR-20250818-72 (started_at 2025-08-18T14:30:00Z, ended_at 2025-08-18T14:31:00Z, input_ref adset:105, errors_json {}). Ensure the final state is validated.",
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "105", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "105", "new_budget": 720.0, "updated_at": "2025-08-18T14:30:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 720.0,
                                                     "changed_at": "2025-08-18T14:30:00Z",
                                                     "reason": "inventory_softening"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-72", "run_type": "budget_apply", "started_at": "2025-08-18T14:30:00Z",
                           "ended_at": "2025-08-18T14:31:00Z", "status": "completed", "input_ref": "adset:105",
                           "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"})
        ],
        outputs=['[{"adset_id":"105","final_budget":720.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t54",
        instruction="Raise the daily budget for ad set 106 from 500.0 to 520.0 effective 2025-08-18T14:32:00Z due to conversion_tailwind, considering Electronics viewership on 2025-08-13 and recent spend from 2025-08-07 through 2025-08-13. Log a completed automation run AR-20250818-73 (started_at 2025-08-18T14:32:00Z, ended_at 2025-08-18T14:33:00Z, input_ref adset:106, errors_json {}). Confirm the final state is validated.",
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "106", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "106", "new_budget": 520.0, "updated_at": "2025-08-18T14:32:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 520.0,
                                                     "changed_at": "2025-08-18T14:32:00Z",
                                                     "reason": "conversion_tailwind"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-73", "run_type": "budget_apply", "started_at": "2025-08-18T14:32:00Z",
                           "ended_at": "2025-08-18T14:33:00Z", "status": "completed", "input_ref": "adset:106",
                           "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"})
        ],
        outputs=['[{"adset_id":"106","final_budget":520.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t55",
        instruction=(
            "Handle the reduction in daily budget for ad set 107, adjusting from 400.0 to 380.0 effective 2025-08-18T14:34:00Z due to the learning_phase. Use Toys viewership on 2025-08-13 and spending data from 2025-08-07 to 2025-08-13 as reference. Keep a precise audit via AR-20250818-74 (budget_apply) which began at 2025-08-18T14:34:00Z and concluded at 2025-08-18T14:35:00Z utilizing input_ref adset:107. Confirm the final condition."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Toys", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "107", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "107", "new_budget": 380.0, "updated_at": "2025-08-18T14:34:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "107", "old_budget": 400.0, "new_budget": 380.0,
                                                     "changed_at": "2025-08-18T14:34:00Z", "reason": "learning_phase"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-74", "run_type": "budget_apply", "started_at": "2025-08-18T14:34:00Z",
                           "input_ref": "adset:107"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-74", "ended_at": "2025-08-18T14:35:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"})
        ],
        outputs=['[{"adset_id":"107","final_budget":380.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t56",
        instruction="Coordinate the reduction of the daily budget for ad set 108, modifying from 780.0 to 760.0 effective 2025-08-18T14:36:00Z with the explanation of supply_variance, using Electronics viewership on 2025-08-13 and spending from 2025-08-07 to 2025-08-13 as context. For consistency, assume the highest existing budget_changes change_id is BC-7, thus your subsequent log should be BC-8. Register a completed automation run AR-20250818-75 (initiated_at 2025-08-18T14:36:00Z, concluded_at 2025-08-18T14:37:00Z, input_ref adset:108, errors_json {}). Confirm the final condition.",
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "108", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "108", "new_budget": 760.0, "updated_at": "2025-08-18T14:36:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 760.0,
                                                     "changed_at": "2025-08-18T14:36:00Z",
                                                     "reason": "supply_variance"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-75", "run_type": "budget_apply", "started_at": "2025-08-18T14:36:00Z",
                           "ended_at": "2025-08-18T14:37:00Z", "status": "completed", "input_ref": "adset:108",
                           "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_budget":760.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t57",
        instruction="Handle the rotation of creatives within ad set 102 by activating 1104 and pausing 1103 with rationale carousel_focus at 2025-08-18T14:38:00Z. Document a completed automation run AR-20250818-76 (started_at 2025-08-18T14:38:00Z, ended_at 2025-08-18T14:39:00Z, input_ref adset:102, errors_json {}). Confirm the rotation by re-listing ads following the change; refrain from unrelated reads.",
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                                                         "rotated_at": "2025-08-18T14:38:00Z",
                                                         "rationale": "carousel_focus"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250818-76", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-18T14:38:00Z",
                                                         "ended_at": "2025-08-18T14:39:00Z", "status": "completed",
                                                         "input_ref": "adset:102", "errors_json": "{}"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1104","paused":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t58",
        instruction="Coordinate the rotation of creatives within ad set 102 by activating 1103 and pausing 1104 with rationale image_focus at 2025-08-18T14:40:00Z. Document a completed automation run AR-20250818-77 (started_at 2025-08-18T14:40:00Z, ended_at 2025-08-18T14:41:00Z, input_ref adset:102, errors_json {}). Confirm the rotation by re-listing ads following the change; refrain from unrelated reads.",
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T14:40:00Z",
                                                         "rationale": "image_focus"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250818-77", "run_type": "creative_rotation",
                                                         "started_at": "2025-08-18T14:40:00Z",
                                                         "ended_at": "2025-08-18T14:41:00Z", "status": "completed",
                                                         "input_ref": "adset:102", "errors_json": "{}"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1103","paused":"1104"}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t59",
        instruction=(
            "Handle the refresh of ad set 102 with a new image creative and set it live: create an image ad titled Autumn Image (start_date 2025-08-19), activate it and pause 1103 at 10:08:00Z with rationale format_test_image. Maintain a concise creative_refresh audit (AR-20250819-21, 10:07:30Z–10:09:00Z, completed, input_ref adset_102_autumn_image) and check ads after rotation."
        ),
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="CreateAd", kwargs={"adset_id": "102", "name": "Autumn Image", "creative_type": "image",
                                             "start_date": "2025-08-19"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-21", "run_type": "creative_refresh",
                                                         "started_at": "2025-08-19T10:07:30Z",
                                                         "ended_at": "2025-08-19T10:09:00Z", "status": "completed",
                                                         "input_ref": "adset_102_autumn_image", "errors_json": "{}"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1119", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation",
                   kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1119",
                           "rotated_at": "2025-08-19T10:08:00Z", "rationale": "format_test_image"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
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
            "Coordinate a cross-channel budget rebalance for ad sets 101 and 102 in a deterministic, policy-compliant manner. At 2025-08-19T08:50:00Z, adjust 101 to 940.0 and 102 to 610.0, logging both with reason rebalance_2025-08-19, verifying after each, and maintaining a budget_rebalance record (AR-20250819-23, 08:50:00Z–08:51:00Z, completed, input_ref adsets_101_102_rebalance)."
        ),
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 940.0, "updated_at": "2025-08-19T08:50:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 940.0,
                           "changed_at": "2025-08-19T08:50:00Z", "reason": "rebalance_2025-08-19"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 610.0, "updated_at": "2025-08-19T08:50:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 610.0,
                           "changed_at": "2025-08-19T08:50:00Z", "reason": "rebalance_2025-08-19"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),

            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-23", "run_type": "budget_rebalance",
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
        instruction="Handle the alignment of ad set 111 with plan_2025-08-13: implement a budget of 1000.0 and a cost_cap of 2.5 starting from 2025-08-18T14:50:00Z, then verify the final state. Document plan snapshots using AR-20250818-82 (plan_freeze, initiated at 2025-08-18T14:50:00Z, input_ref plan_2025-08-13) and AR-20250818-83 (budget_apply, initiated at 2025-08-18T14:50:00Z, input_ref plan_2025-08-13).",
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-82", "run_type": "plan_freeze",
                           "started_at": "2025-08-18T14:50:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "111", "new_budget": 1000.0, "updated_at": "2025-08-18T14:50:00Z"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5,
                           "updated_at": "2025-08-18T14:50:00Z"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-83", "run_type": "budget_apply",
                           "started_at": "2025-08-18T14:50:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","plan_applied":"plan_2025-08-13"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t62",
        instruction="Coordinate the calibration of ad set 102 with a paired move: increase the daily budget from 590.0 to 600.0 and implement a cost_cap of 6.0, both set to begin at 2025-08-18T14:54:00Z, for the reason paired_scale. Validate canonical strategies, log both modifications, record AR-20250818-84 (strategy_apply, initiated at 2025-08-18T14:54:00Z, input_ref adset:102), and confirm the final state.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 600.0, "updated_at": "2025-08-18T14:54:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 600.0,
                                                     "changed_at": "2025-08-18T14:54:00Z", "reason": "paired_scale"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 6.0,
                           "updated_at": "2025-08-18T14:54:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.0, "changed_at": "2025-08-18T14:54:00Z",
                           "reason": "paired_scale"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-84", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T14:54:00Z", "input_ref": "adset:102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":600.0,"final_bid_strategy":"cost_cap","final_bid_amount":6.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t63",
        instruction="Handle the rebalancing of ad set 101 by reducing the daily budget from 920.0 to 900.0 while keeping the cost_cap at 32.0, effective as of 2025-08-18T14:58:00Z, due to the margin_guard reason. Include the ROAS from 2025-08-13 as context, record AR-20250818-85 (budget_apply, started_at 2025-08-18T14:58:00Z, input_ref adset:101), and check the final state for verification.",
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 900.0, "updated_at": "2025-08-18T14:58:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 900.0,
                                                     "changed_at": "2025-08-18T14:58:00Z", "reason": "margin_guard"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0,
                           "updated_at": "2025-08-18T14:58:00Z"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-85", "run_type": "budget_apply",
                           "started_at": "2025-08-18T14:58:00Z", "input_ref": "adset:101"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_budget":900.0,"final_bid_amount":32.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t64",
        instruction="Ensure stability in ad set 102 by leaving ad 1103 active and pausing 1104 for the purpose of stability_check at 2025-08-18T15:02:00Z, and confirm using reads. Include a one-day CTR context for 2025-08-13. For determinism, consider the largest existing creative_rotations ID as CR-3, so the next will be CR-4. Record AR-20250818-86 (creative_rotation, started_at 2025-08-18T15:02:00Z, input_ref adset:102).",
        actions=[
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T15:02:00Z",
                                                         "rationale": "stability_check"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-86", "run_type": "creative_rotation",
                           "started_at": "2025-08-18T15:02:00Z", "input_ref": "adset:102"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","active_ad_after":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t65",
        instruction="Handle the refinement of ad set 103 by transitioning to a cost_cap of 6.5 effective at 2025-08-18T15:04:00Z with the justification video_efficiency. Confirm canonical strategies, retrieve previous values, incorporate a 2025-08-13 insight pull for context, document AR-20250818-87 (strategy_apply, started_at 2025-08-18T15:04:00Z, input_ref adset:103), and validate. For determinizm, consider the highest existing strategy_changes ID is SC-4 so the subsequent one will be SC-5.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 6.5,
                           "updated_at": "2025-08-18T15:04:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.5, "changed_at": "2025-08-18T15:04:00Z",
                           "reason": "video_efficiency"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-87", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:04:00Z", "input_ref": "adset:103"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"})
        ],
        outputs=['[{"adset_id":"103","final_bid_strategy":"cost_cap","final_bid_amount":6.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t66",
        instruction="Coordinate an increase in ad set 104’s budget from 740.0 to 760.0 and maintain the bid strategy cost_cap at 22.0, with both changes effective at 2025-08-18T15:06:00Z, for the reason inventory_tight. Leverage Electronics viewership on 2025-08-13 and the expenditure window 2025-08-07 to 2025-08-13 for context. Register AR-20250818-88 (budget_apply, started_at 2025-08-18T15:06:00Z, input_ref adset:104) and confirm.",
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "104", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "104", "new_budget": 760.0, "updated_at": "2025-08-18T15:06:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 760.0,
                                                     "changed_at": "2025-08-18T15:06:00Z",
                                                     "reason": "inventory_tight"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0,
                           "updated_at": "2025-08-18T15:06:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 20.0, "new_bid": 22.0, "changed_at": "2025-08-18T15:06:00Z",
                           "reason": "inventory_tight"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-88", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:06:00Z", "input_ref": "adset:104"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_budget":760.0,"final_bid_amount":22.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t67",
        instruction="Handle the adjustment of ad set 105 from lowest_cost to cost_cap 3.5 effective 2025-08-18T15:10:00Z, citing standardize_bidding as the rationale. Check canonical strategies, gather prior values, note AR-20250818-89 (strategy_apply, started_at 2025-08-18T15:10:00Z, input_ref adset:105), and wrap up that session by 2025-08-18T15:10:00Z. Employ a CTR read dated 2025-08-13 for verification (excluding additional post-change ad set read).",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "105", "bid_strategy": "cost_cap", "bid_amount": 3.5,
                           "updated_at": "2025-08-18T15:10:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "105", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 3.5, "changed_at": "2025-08-18T15:10:00Z",
                           "reason": "standardize_bidding"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-89", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:10:00Z", "input_ref": "adset:105"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-89", "ended_at": "2025-08-18T15:10:00Z"})
        ],
        outputs=['[{"adset_id":"105","final_bid_strategy":"cost_cap","final_bid_amount":3.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t68",
        instruction="Coordinate a no-op budget confirmation for ad set 102 by updating daily_budget to 590.0 effective 2025-08-18T15:12:00Z, justified by budget_confirm. To ensure consistency, review spending and CTR for 2025-08-13 (spend window from 2025-08-13 to 2025-08-13, CTR date 2025-08-13). Log AR-20250818-90 (budget_apply, started_at 2025-08-18T15:12:00Z, input_ref adset:102) and confirm verification.",
        actions=[
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "102", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 590.0, "updated_at": "2025-08-18T15:12:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 590.0,
                                                     "changed_at": "2025-08-18T15:12:00Z", "reason": "budget_confirm"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-90", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:12:00Z", "input_ref": "adset:102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":590.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t69",
        instruction="Adjust ad set 108 by reducing the budget from 780.0 to 770.0 and raising the cost_cap from 42.0 to 43.0, effective 2025-08-18T15:14:00Z with the reason shift_to_quality. Utilize record-sourced old values, confirm canonical strategies, log AR-20250818-91 (strategy_apply, started_at 2025-08-18T15:14:00Z, input_ref adset:108), and confirm with a post-change read.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "108", "new_budget": 770.0, "updated_at": "2025-08-18T15:14:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 770.0,
                                                     "changed_at": "2025-08-18T15:14:00Z",
                                                     "reason": "shift_to_quality"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 43.0,
                           "updated_at": "2025-08-18T15:14:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 42.0,
                           "new_bid": 43.0, "changed_at": "2025-08-18T15:14:00Z", "reason": "shift_to_quality"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-91", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:14:00Z", "input_ref": "adset:108"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_budget":770.0,"final_bid_amount":43.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t70",
        instruction="Harmonize ad set 107 by shifting from lowest_cost to cost_cap 3.0, effective 2025-08-18T15:18:00Z with the reason standardize_lowspend, ensuring canonical strategies, using record-sourced old values, capturing AR-20250818-92 strategy_apply for input_ref adset:107, and confirming with a ROAS read for 2025-08-13.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "107", "bid_strategy": "cost_cap", "bid_amount": 3.0,
                           "updated_at": "2025-08-18T15:18:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 3.0, "changed_at": "2025-08-18T15:18:00Z",
                           "reason": "standardize_lowspend"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-92", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:18:00Z", "input_ref": "adset:107"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"})
        ],
        outputs=['[{"adset_id":"107","final_bid_strategy":"cost_cap","final_bid_amount":3.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t71",
        instruction=(
            "You must formulate and implement a strategy for 2025-08-22 concentrating on the pacing of ad set 112. The strategy plan_2025-08-22c (author planning_agent_v1, created_at 2025-08-22T01:57:50Z, checksum p22c0760) assigns 760.0 to ad set 112 (lowest_cost, image). Pause operation (AR-20250822-07, 01:57:50Z–01:59:30Z). Deploy the budget at 02:05:00Z citing plan_2025-08-22c as the reason, authenticate, and document budget_apply (AR-20250822-08, 02:05:00Z–02:06:00Z)."
        ),
        actions=[
            Action(name="ListCanonicalCreativeTypes", kwargs={}),
            Action(name="ValidateAllocationsAgainstPolicy", kwargs={"total_budget": 760.0, "allocations": [
                {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost", "creative_type": "image"},
            ]}),
            Action(name="CreatePlan",
                   kwargs={"plan_id": "plan_2025-08-22c", "date": "2025-08-22", "total_budget": 760.0,
                           "author": "planning_agent_v1", "created_at": "2025-08-22T01:57:50Z",
                           "checksum": "p22c0760", "allocations": [
                           {"adset_id": "112", "budget": 760.0, "bid_strategy": "lowest_cost",
                            "creative_type": "image"},
                       ]}),
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-22"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250822-07", "run_type": "plan_freeze",
                                                         "started_at": "2025-08-22T01:57:50Z",
                                                         "ended_at": "2025-08-22T01:59:30Z", "status": "completed",
                                                         "input_ref": "plan_2025-08-22c", "errors_json": "{}"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 760.0, "updated_at": "2025-08-22T02:05:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 760.0,
                           "changed_at": "2025-08-22T02:05:00Z", "reason": "plan_2025-08-22c"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250822-08", "run_type": "budget_apply",
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
        instruction="Coordinate ad set 112 at cost_cap 4.2 effective 2025-08-18T15:24:00Z using cp_flooring as the justification. Validate canonical approaches and review the ad set; with a budget already set at 700.0, avoid recording an unnecessary budget alteration. Note AR-20250818-94 (strategy_apply, started_at 2025-08-18T15:24:00Z, input_ref adset:112) and verify.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "112", "bid_strategy": "cost_cap", "bid_amount": 4.2,
                           "updated_at": "2025-08-18T15:24:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 4.2, "changed_at": "2025-08-18T15:24:00Z",
                           "reason": "cp_flooring"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-94", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:24:00Z", "input_ref": "adset:112"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_bid_strategy":"cost_cap","final_bid_amount":4.2}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t73",
        instruction="Verify the canonical strategies and enforce cost_cap 5.0 on ad set 102 effective 2025-08-18T15:28:00Z, citing the reason as conservative_cap. Record the modification, note AR-20250818-95 (strategy_apply, started_at 2025-08-18T15:28:00Z, input_ref adset:102), and then confirm via a post-change ad set read along with a 2025-08-13 insights fetch.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 5.0,
                           "updated_at": "2025-08-18T15:28:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 5.0, "changed_at": "2025-08-18T15:28:00Z",
                           "reason": "conservative_cap"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-95", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T15:28:00Z", "input_ref": "adset:102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="GetDailyInsightsForAdset", kwargs={"adset_id": "102", "date": "2025-08-13"})
        ],
        outputs=['[{"adset_id":"102","final_bid_strategy":"cost_cap","final_bid_amount":5.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t74",
        instruction="Implement a slight increase for ad set 101 budget from 920.0 to 930.0 effective 2025-08-18T15:30:00Z for the reason micro_scale while maintaining cost_cap 32.0. Incorporate a 2025-08-13 CTR snapshot for context, ensure the audit remains concise, and verify the final state.",
        actions=[
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 930.0, "updated_at": "2025-08-18T15:30:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 930.0,
                                                     "changed_at": "2025-08-18T15:30:00Z", "reason": "micro_scale"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0,
                           "updated_at": "2025-08-18T15:30:00Z"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-96", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:30:00Z", "input_ref": "adset:101"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-96", "ended_at": "2025-08-18T15:30:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_budget":930.0,"final_bid_amount":32.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t75",
        instruction=(
            "Handle a stability-oriented no-op rotation for ad set 102, ensuring 1103 remains active and 1104 stays paused with rationale stability_noop at 2025-08-18T15:34:00Z. Afterward, conduct verification through reads and incorporate a ROAS context read for 2025-08-13."
        ),
        actions=[
            Action(name="CalculateAdsetRoasForDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T15:34:00Z",
                                                         "rationale": "stability_noop"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","active_ad_after":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t76",
        instruction="Verify the plan_2025-08-13 allocation for ad set 111 by confirming budget 1000.0 and cost_cap 2.5 effective 2025-08-18T15:36:00Z. Record AR-20250818-98 (plan_freeze, started_at 2025-08-18T15:36:00Z, input_ref plan_2025-08-13) and AR-20250818-99 (budget_apply, started_at 2025-08-18T15:36:00Z, input_ref plan_2025-08-13), then validate the final state.",
        actions=[
            Action(name="GetPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetAllocationFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-98", "run_type": "plan_freeze",
                           "started_at": "2025-08-18T15:36:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "111", "new_budget": 1000.0, "updated_at": "2025-08-18T15:36:00Z"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5,
                           "updated_at": "2025-08-18T15:36:00Z"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-99", "run_type": "budget_apply",
                           "started_at": "2025-08-18T15:36:00Z", "input_ref": "plan_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","plan_confirmed":"plan_2025-08-13"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t77",
        instruction="Handle the budget calibration for ad set 102, adjusting it from 590.0 to 620.0, effective 2025-08-18T16:00:00Z, citing the reason office_retarget_calibration. Utilize Office viewership data from 2025-08-13 and apply it within a deterministic same-day spend window (2025-08-13 to 2025-08-13). Log AR-20250818-56 (budget_apply, started_at 2025-08-18T16:00:00Z, input_ref adset:102), conclude that session at 2025-08-18T16:00:00Z, and confirm the final state.",
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Office", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "102", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 620.0, "updated_at": "2025-08-18T16:00:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 620.0,
                                                     "changed_at": "2025-08-18T16:00:00Z",
                                                     "reason": "office_retarget_calibration"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-56", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:00:00Z", "input_ref": "adset:102"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-56", "ended_at": "2025-08-18T16:00:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":620.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t78",
        instruction="Coordinate validation of canonical strategies, transitioning ad set 102 from lowest_cost to cost_cap 5.0, effective 2025-08-18T16:05:00Z, due to retarget_cost_focus. Conduct an audit with Apparel viewership data from 2025-08-13. Register AR-20250818-57 (strategy_apply, started_at 2025-08-18T16:05:00Z, input_ref adset:102) and confirm the process.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetViewershipForCategory", kwargs={"category": "Apparel", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "102", "bid_strategy": "cost_cap", "bid_amount": 5.0,
                           "updated_at": "2025-08-18T16:05:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "102", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 5.0, "changed_at": "2025-08-18T16:05:00Z",
                           "reason": "retarget_cost_focus"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-57", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:05:00Z", "input_ref": "adset:102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_bid_strategy":"cost_cap","final_bid_amount":5.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t79",
        instruction="Establish a baseline for spending and engagement for ad set 102, confirming its budget through an audited no-op: re-write daily_budget 590.0 effective 2025-08-18T16:10:00Z with reason budget_confirm. Utilize a deterministic same-day spend window (2025-08-13 to 2025-08-13) and CTR date 2025-08-13. Record AR-20250818-58 (budget_apply, started_at 2025-08-18T16:10:00Z, input_ref adset:102) and check for verification.",
        actions=[
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "102", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="ComputeCtrForAdsetDay", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "102", "new_budget": 590.0, "updated_at": "2025-08-18T16:10:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "102", "old_budget": 590.0, "new_budget": 590.0,
                                                     "changed_at": "2025-08-18T16:10:00Z", "reason": "budget_confirm"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-58", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:10:00Z", "input_ref": "adset:102"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","final_budget":590.0}]']
    ),
    Task(
        annotator="v6",
        user_id="sma_t80",
        instruction=(
            "You must Integrate recent Electronics signals with product 1 price (2025-08-14) to manage pacing for ad set 101 wisely. At 2025-08-19T09:10:00Z, set daily_budget to 970.0, document reason cross_signal_pacing_2025-08-13, confirm the updated state, and log a concise budget_rebalance window (AR-20250819-25, 09:10:00Z–09:11:00Z, completed, input_ref adset_101_cross_signal)."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetProductPriceOnDate", kwargs={"product_id": "1", "date": "2025-08-14"}),
            Action(name="GetPolicyParameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 970.0, "updated_at": "2025-08-19T09:10:00Z"}),
            Action(name="LogBudgetChange",
                   kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 970.0,
                           "changed_at": "2025-08-19T09:10:00Z", "reason": "cross_signal_pacing_2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="CreateAutomationRun", kwargs={"run_id": "AR-20250819-25", "run_type": "budget_rebalance",
                                                         "started_at": "2025-08-19T09:10:00Z",
                                                         "ended_at": "2025-08-19T09:11:00Z", "status": "completed",
                                                         "input_ref": "adset_101_cross_signal", "errors_json": "{}"}),
        ],
        outputs=['[{"adset_id":"101","final_daily_budget":970.0},{"automation_run":"AR-20250819-25"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t81",
        instruction="Ensure ad set 104’s bidding aligns with the policy by adjusting the cost_cap from 20.0 to 21.0 effective 2025-08-18T16:14:00Z, document the adjustment with reason incremental_efficiency, log AR-20250818-101 (strategy_apply, started_at 2025-08-18T16:14:00Z, input_ref adset:104) and finalize it at 2025-08-18T16:14:00Z, then confirm through a single read.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 21.0,
                           "updated_at": "2025-08-18T16:14:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "104", "old_strategy": "cost_cap", "new_strategy": "cost_cap", "old_bid": 20.0,
                           "new_bid": 21.0, "changed_at": "2025-08-18T16:14:00Z",
                           "reason": "incremental_efficiency"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-101", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:14:00Z", "input_ref": "adset:104"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-101", "ended_at": "2025-08-18T16:14:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_bid_strategy":"cost_cap","final_bid_amount":21.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t82",
        instruction="Adjust ad set 104’s daily budget from 740.0 to 745.0 effective 2025-08-18T16:16:00Z due to incremental_topup. Record AR-20250818-102 (budget_apply, started_at 2025-08-18T16:16:00Z, input_ref adset:104), conclude it at 2025-08-18T16:16:00Z, and confirm through a post-change read.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "104", "new_budget": 745.0, "updated_at": "2025-08-18T16:16:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 745.0,
                                                     "changed_at": "2025-08-18T16:16:00Z",
                                                     "reason": "incremental_topup"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-102", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:16:00Z", "input_ref": "adset:104"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-102", "ended_at": "2025-08-18T16:16:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_budget":745.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t83",
        instruction="Handle the standardization of ad set 103 by transitioning from lowest_cost to cost_cap 6.0, effective from 2025-08-18T16:18:00Z, citing standardize_policy as the reason. Maintain a record AR-20250818-103 (strategy_apply, started_at 2025-08-18T16:18:00Z, input_ref adset:103), finalize it by 2025-08-18T16:18:00Z, and confirm accuracy.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "103", "bid_strategy": "cost_cap", "bid_amount": 6.0,
                           "updated_at": "2025-08-18T16:18:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "103", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 6.0, "changed_at": "2025-08-18T16:18:00Z",
                           "reason": "standardize_policy"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-103", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:18:00Z", "input_ref": "adset:103"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-103", "ended_at": "2025-08-18T16:18:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"})
        ],
        outputs=['[{"adset_id":"103","final_bid_strategy":"cost_cap","final_bid_amount":6.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t84",
        instruction="Coordinate the reduction of ad set 108's daily budget from 780.0 to 775.0, starting on 2025-08-18T16:20:00Z, for the purpose of controlled_reduction. Ensure to document AR-20250818-104 (budget_apply, started_at 2025-08-18T16:20:00Z, input_ref adset:108), complete it at 2025-08-18T16:20:00Z, and check for correctness.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "108", "new_budget": 775.0, "updated_at": "2025-08-18T16:20:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "108", "old_budget": 780.0, "new_budget": 775.0,
                                                     "changed_at": "2025-08-18T16:20:00Z",
                                                     "reason": "controlled_reduction"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-104", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:20:00Z", "input_ref": "adset:108"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-104", "ended_at": "2025-08-18T16:20:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_budget":775.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t85",
        instruction="Handle the rebalance of ad set 101's daily budget, adjusting it from 920.0 to 915.0, effective 2025-08-18T16:22:00Z, due to margin_tighten. Log AR-20250818-105 (budget_apply, started_at 2025-08-18T16:22:00Z, input_ref adset:101), close it at 2025-08-18T16:22:00Z, and confirm.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "101", "new_budget": 915.0, "updated_at": "2025-08-18T16:22:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "101", "old_budget": 920.0, "new_budget": 915.0,
                                                     "changed_at": "2025-08-18T16:22:00Z",
                                                     "reason": "margin_tighten"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-105", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:22:00Z", "input_ref": "adset:101"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-105", "ended_at": "2025-08-18T16:22:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_budget":915.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t86",
        instruction="Coordinate a creative rotation in ad set 102 by activating 1104 and pausing 1103 at 2025-08-18T16:24:00Z for the reason carousel_focus. Log AR-20250818-106 (creative_rotation, started_at 2025-08-18T16:24:00Z, input_ref adset:102), close it at 2025-08-18T16:24:00Z, and confirm with a post-rotation ads read.",
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1104", "ad_id_to_pause": "1103"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1103", "new_ad_id": "1104",
                                                         "rotated_at": "2025-08-18T16:24:00Z",
                                                         "rationale": "carousel_focus"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-106", "run_type": "creative_rotation",
                           "started_at": "2025-08-18T16:24:00Z", "input_ref": "adset:102"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-106", "ended_at": "2025-08-18T16:24:00Z"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1104","paused":"1103"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t87",
        instruction=(
            "Handle the tightening of ad set 106’s bidding by adjusting the cost_cap to 17.5 on 2025-08-18T16:26:00Z for efficiency_tune reasons. Ensure it aligns with canonical strategies, compile a succinct AR-20250818-107 strategy_apply audit (initiated and concluded at 2025-08-18T16:26:00Z; input_ref adset:106), and deliver the final outcome."
        ),
        actions=[
            Action(name="ListCanonicalBidStrategies", kwargs={}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),

            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 17.5,
                           "updated_at": "2025-08-18T16:26:00Z"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-107", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:26:00Z", "input_ref": "adset:106"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-107", "ended_at": "2025-08-18T16:26:00Z"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"})
        ],
        outputs=['[{"adset_id":"106","final_bid_strategy":"cost_cap","final_bid_amount":17.5}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t88",
        instruction="Coordinate the reduction of ad set 111’s daily budget from 1000.0 to 990.0 effective 2025-08-18T16:28:00Z for budget_guard purposes. Document AR-20250818-108 (budget_apply, initiated at 2025-08-18T16:28:00Z, input_ref adset:111), conclude it at 2025-08-18T16:28:00Z, and confirm accuracy.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "111", "new_budget": 990.0, "updated_at": "2025-08-18T16:28:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "111", "old_budget": 1000.0, "new_budget": 990.0,
                                                     "changed_at": "2025-08-18T16:28:00Z",
                                                     "reason": "budget_guard"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-108", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:28:00Z", "input_ref": "adset:111"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-108", "ended_at": "2025-08-18T16:28:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","final_budget":990.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t89",
        instruction="Handle the transition of ad set 105 from lowest_cost to cost_cap 3.2, effective starting 2025-08-18T16:30:00Z, citing policy_standardization as the reason. Maintain a minimal audit trail (a single change log) and verify the outcome with one post-change read. For consistency, assume the most recent strategy_changes ID is SC-4, so the new entry should be SC-5.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "105", "bid_strategy": "cost_cap", "bid_amount": 3.2,
                           "updated_at": "2025-08-18T16:30:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"change_id": "SC-5", "adset_id": "105", "old_strategy": "lowest_cost",
                           "new_strategy": "cost_cap", "old_bid": None, "new_bid": 3.2,
                           "changed_at": "2025-08-18T16:30:00Z", "reason": "policy_standardization"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"})
        ],
        outputs=['[{"adset_id":"105","final_bid_strategy":"cost_cap","final_bid_amount":3.2}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t90",
        instruction="Facilitate the shift of ad set 107 from lowest_cost to cost_cap 3.1, starting on 2025-08-18T16:32:00Z, with the purpose being standardize_lowspend. Log AR-20250818-110 recording (strategy_apply, initiated at 2025-08-18T16:32:00Z, input_ref adset:107), conclude it by 2025-08-18T16:32:00Z, and confirm.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "107", "bid_strategy": "cost_cap", "bid_amount": 3.1,
                           "updated_at": "2025-08-18T16:32:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "107", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 3.1, "changed_at": "2025-08-18T16:32:00Z",
                           "reason": "standardize_lowspend"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-110", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:32:00Z", "input_ref": "adset:107"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-110", "ended_at": "2025-08-18T16:32:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "107"})
        ],
        outputs=['[{"adset_id":"107","final_bid_strategy":"cost_cap","final_bid_amount":3.1}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t91",
        instruction="Handle the increase of ad set 112’s daily budget from 700.0 to 710.0 effective 2025-08-18T16:34:00Z for the purpose of pacing_boost. Log AR-20250818-111 (budget_apply, started_at 2025-08-18T16:34:00Z, input_ref adset:112), finalizing it at 2025-08-18T16:34:00Z, and confirm the action.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "112", "new_budget": 710.0, "updated_at": "2025-08-18T16:34:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "112", "old_budget": 700.0, "new_budget": 710.0,
                                                     "changed_at": "2025-08-18T16:34:00Z",
                                                     "reason": "pacing_boost"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-111", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:34:00Z", "input_ref": "adset:112"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-111", "ended_at": "2025-08-18T16:34:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_budget":710.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t92",
        instruction="You adjust the budget on ad set 103 to 1160.0 effective 2025-08-18T16:36:00Z due to headroom_guard. Ensure the audit trail is minimal and verify with a single post-change read. Avoid establishing automation-run records.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "103", "new_budget": 1160.0, "updated_at": "2025-08-18T16:36:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "103", "old_budget": 1180.0, "new_budget": 1160.0,
                                                     "changed_at": "2025-08-18T16:36:00Z",
                                                     "reason": "headroom_guard"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "103"})
        ],
        outputs=['[{"adset_id":"103","final_budget":1160.0}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t93",
        instruction="Handle the adjustment of ad set 101 cost_cap from 32.0 to 33.0 as of 2025-08-18T16:38:00Z with the justification bid_recenter. Ensure to keep a minimal audit trail and verify with a post-change read once; do not initiate automation runs.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 33.0,
                           "updated_at": "2025-08-18T16:38:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "101", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 32.0, "new_bid": 33.0, "changed_at": "2025-08-18T16:38:00Z",
                           "reason": "bid_recenter"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "101"})
        ],
        outputs=['[{"adset_id":"101","final_bid_strategy":"cost_cap","final_bid_amount":33.0}]']
    ),

    Task(
        annotator="0",
        user_id="sma_t94",
        instruction="Coordinate the rotation of creatives in ad set 102 for stabilization: enable 1103 and deactivate 1104 at 2025-08-18T16:40:00Z with the aim of stability_focus. Log AR-20250818-114 (creative_rotation, started_at 2025-08-18T16:40:00Z, input_ref adset:102), conclude it at 2025-08-18T16:40:00Z, and confirm by reading ads.",
        actions=[
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"}),
            Action(name="RotateAdCreative", kwargs={"ad_id_to_activate": "1103", "ad_id_to_pause": "1104"}),
            Action(name="LogCreativeRotation", kwargs={"adset_id": "102", "old_ad_id": "1104", "new_ad_id": "1103",
                                                         "rotated_at": "2025-08-18T16:40:00Z",
                                                         "rationale": "stability_focus"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-114", "run_type": "creative_rotation",
                           "started_at": "2025-08-18T16:40:00Z", "input_ref": "adset:102"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-114", "ended_at": "2025-08-18T16:40:00Z"}),
            Action(name="GetAdsByAdsetId", kwargs={"adset_id": "102"})
        ],
        outputs=['[{"adset_id":"102","activated":"1103","paused":"1104"}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t95",
        instruction="Handle an increase in ad set 108’s cost_cap from 42.0 to 43.0 starting 2025-08-18T16:42:00Z due to value_seek. Register AR-20250818-115 (strategy_apply, initiated at 2025-08-18T16:42:00Z, input_ref adset:108), close it at 2025-08-18T16:42:00Z, and confirm accuracy.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 43.0,
                           "updated_at": "2025-08-18T16:42:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "108", "old_strategy": "cost_cap", "new_strategy": "cost_cap",
                           "old_bid": 42.0, "new_bid": 43.0, "changed_at": "2025-08-18T16:42:00Z",
                           "reason": "value_seek"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-115", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:42:00Z", "input_ref": "adset:108"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-115", "ended_at": "2025-08-18T16:42:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "108"})
        ],
        outputs=['[{"adset_id":"108","final_bid_strategy":"cost_cap","final_bid_amount":43.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t96",
        instruction=(
            "Coordinate a raise in ad set 106’s daily budget to 508.0 at 2025-08-18T16:44:00Z with light_scale justification, in accordance with policy and recent analysis. Reference the 2025-08-13 Electronics baseline (viewership and same-day spend) and include a singular audit entry AR-20250818-116 (budget_apply; 2025-08-18T16:44:00Z; input_ref adset:106). Deliver the final outcome."
        ),
        actions=[
            Action(name="GetViewershipForCategory", kwargs={"category": "Electronics", "date": "2025-08-13"}),
            Action(name="GetAdsetSpendForDateRange",
                   kwargs={"adset_id": "106", "start_date": "2025-08-13", "end_date": "2025-08-13"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"}),

            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "106", "new_budget": 508.0, "updated_at": "2025-08-18T16:44:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "106", "old_budget": 500.0, "new_budget": 508.0,
                                                     "changed_at": "2025-08-18T16:44:00Z", "reason": "light_scale"}),

            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-116", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:44:00Z", "input_ref": "adset:106"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-116", "ended_at": "2025-08-18T16:44:00Z"}),

            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "106"})
        ],
        outputs=['[{"adset_id":"106","final_budget":508.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t97",
        instruction="Handle the reduction of ad set 105’s daily budget from 750.0 to 740.0 effective 2025-08-18T16:46:00Z due to inventory_softness. Record AR-20250818-117 (budget_apply, started_at 2025-08-18T16:46:00Z, input_ref adset:105), conclude it at 2025-08-18T16:46:00Z, and verify.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "105", "new_budget": 740.0, "updated_at": "2025-08-18T16:46:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "105", "old_budget": 750.0, "new_budget": 740.0,
                                                     "changed_at": "2025-08-18T16:46:00Z",
                                                     "reason": "inventory_softness"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-117", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:46:00Z", "input_ref": "adset:105"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-117", "ended_at": "2025-08-18T16:46:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "105"})
        ],
        outputs=['[{"adset_id":"105","final_budget":740.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t98",
        instruction="Coordinate the adjustment of ad set 111 cost_cap from 2.5 to 2.6 effective 2025-08-18T16:48:00Z because of incremental_bid_lift. Maintain a minimal audit (single change log) and affirm with one post-change read. For consistency, consider the highest current strategy_changes ID as SC-4, making the new entry SC-5. Avoid creating automation runs.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.6,
                           "updated_at": "2025-08-18T16:48:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"change_id": "SC-5", "adset_id": "111", "old_strategy": "cost_cap",
                           "new_strategy": "cost_cap", "old_bid": 2.5, "new_bid": 2.6,
                           "changed_at": "2025-08-18T16:48:00Z", "reason": "incremental_bid_lift"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "111"})
        ],
        outputs=['[{"adset_id":"111","final_bid_strategy":"cost_cap","final_bid_amount":2.6}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t99",
        instruction="Handle the standardization of ad set 112 from lowest_cost to cost_cap 4.0 as of 2025-08-18T16:50:00Z for the reason baseline_cap. Document AR-20250818-119 (strategy_apply, started_at 2025-08-18T16:50:00Z, input_ref adset:112), finalize it at 2025-08-18T16:50:00Z, and confirm.",
        actions=[
            Action(name="GetPolicyParameter", kwargs={"param_name": "canonical_bid_strategies"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"}),
            Action(name="UpdateAdsetBidStrategy",
                   kwargs={"adset_id": "112", "bid_strategy": "cost_cap", "bid_amount": 4.0,
                           "updated_at": "2025-08-18T16:50:00Z"}),
            Action(name="LogStrategyChange",
                   kwargs={"adset_id": "112", "old_strategy": "lowest_cost", "new_strategy": "cost_cap",
                           "old_bid": None, "new_bid": 4.0, "changed_at": "2025-08-18T16:50:00Z",
                           "reason": "baseline_cap"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-119", "run_type": "strategy_apply",
                           "started_at": "2025-08-18T16:50:00Z", "input_ref": "adset:112"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-119", "ended_at": "2025-08-18T16:50:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "112"})
        ],
        outputs=['[{"adset_id":"112","final_bid_strategy":"cost_cap","final_bid_amount":4.0}]']
    ),
    Task(
        annotator="0",
        user_id="sma_t100",
        instruction="Coordinate a modest reduction of ad set 104’s daily budget from 740.0 to 735.0 as of 2025-08-18T16:52:00Z due to pacing_smooth. Record AR-20250818-120 (budget_apply, started_at 2025-08-18T16:52:00Z, input_ref adset:104), conclude it at 2025-08-18T16:52:00Z, and validate.",
        actions=[
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"}),
            Action(name="UpdateAdsetBudget",
                   kwargs={"adset_id": "104", "new_budget": 735.0, "updated_at": "2025-08-18T16:52:00Z"}),
            Action(name="LogBudgetChange", kwargs={"adset_id": "104", "old_budget": 740.0, "new_budget": 735.0,
                                                     "changed_at": "2025-08-18T16:52:00Z",
                                                     "reason": "pacing_smooth"}),
            Action(name="CreateAutomationRun",
                   kwargs={"run_id": "AR-20250818-120", "run_type": "budget_apply",
                           "started_at": "2025-08-18T16:52:00Z", "input_ref": "adset:104"}),
            Action(name="UpdateAutomationRunEnd",
                   kwargs={"run_id": "AR-20250818-120", "ended_at": "2025-08-18T16:52:00Z"}),
            Action(name="GetAdsetDetailsById", kwargs={"adset_id": "104"})
        ],
        outputs=['[{"adset_id":"104","final_budget":735.0}]']
    )
]

