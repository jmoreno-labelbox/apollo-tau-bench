from domains.dto import Action, Task

TASKS =[        
        
        Task(
            annotator="v3",
            user_id="task_001",
            instruction=(
                "You bring ad set 104 in the 'Fall Collection Launch' campaign into alignment with the frozen plan for 2025-08-13 "
                "and confirm the aligned state for budget and bid strategy."
            ),
            actions=[
                Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
                Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
                Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
                Action(name="set_adset_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
                Action(name="fetch_adset", kwargs={"adset_id": "104"}),
                Action(
                    name="verify_applied",
                    kwargs={
                        "expected_rows": [
                            {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}
                        ],
                        "actual_rows": [
                            {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}
                        ],
                        "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
                    }
                ),
            ],
            outputs=[
                '"campaign_id": "3"',
                '"plan_id": "plan_2025-08-13"',
                '"adset_id": "104"',
                '"budget": 750.0',
                '"bid_strategy": "cost_cap"',
                '"bid_amount": 22.0',
                '"ok": true'
            ]
        ),
    
      Task(
        annotator="v3",
        user_id="task_002",
        instruction=(
            "You run daily allocation and rotation for 'Global Summer Sale' on 2025-08-13 in line with policy and the frozen plan. "
            "Bring ad sets 101 and 102 to the plan’s budgets and strategies, enforce the recorded rotation for ad set 101 so exactly one ad is active, "
            "log any delivery exceptions for the day using the available insights, and publish auditable artifacts."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "allocation_rotation_daily",
                "input_ref": {"campaign_id": "1", "plan_id": "plan_2025-08-13", "date": "2025-08-13", "adsets": ["101", "102"]}
            }),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_creative_rotation", kwargs={"adset_id": "101"}),
            Action(name="pause_or_activate_ad", kwargs={"ad_id": "1101", "status": "paused"}),
            Action(name="pause_or_activate_ad", kwargs={"ad_id": "1102", "status": "active"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "active_ads": 1}],
                "actual_rows": [{"adset_id": "101", "active_ads": 1}],
                "key_fields": ["adset_id", "active_ads"]
            }),
            Action(name="daily_adset_insights", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="raise_exceptions", kwargs={
                "plan_id": "plan_2025-08-13",
                "insights": [],
                "rules": {"zero_delivery_impressions": 0}
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "1",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101",
                    "budget": 950.0,
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "old_ad_id": "1101",
                    "new_ad_id": "1102"
                },{
                    "campaign_id": "1",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102",
                    "budget": 600.0,
                    "bid_strategy": "lowest_cost"
                }]
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {
                    "plan_id": "plan_2025-08-13",
                    "adsets": ["101", "102"],
                    "rotation": {"101": {"old_ad_id": "1101", "new_ad_id": "1102"}}
                }
            })
        ],
        outputs=[
            '"run_id": "run_2025-08-13"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"adset_id": "102"',
            '"old_ad_id": "1101"',
            '"new_ad_id": "1102"'
        ]
    ),
        
    Task(
        annotator="v3",
        user_id="task_003",
        instruction=(
            "You ensure the 'Global Summer Sale' campaign is aligned with the frozen plan for 2025-08-13. "
            "You set ad set 101 to the planned budget 950.0 and cost_cap with bid_amount 35.0, and you enforce a single-active state "
            "where ad 1102 is active and ad 1101 is paused. You export a compact CSV receipt of the alignment."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={
                "adset_id": "101",
                "bid_strategy": "cost_cap",
                "bid_amount": 35.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="list_ads_in_adset", kwargs={"adset_id": "101"}),
            Action(name="pause_or_activate_ad", kwargs={"ad_id": "1101", "status": "paused"}),
            Action(name="pause_or_activate_ad", kwargs={"ad_id": "1102", "status": "active"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "active_ads": 1}],
                "actual_rows": [{"adset_id": "101", "active_ads": 1}],
                "key_fields": ["adset_id", "active_ads"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "1",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101",
                    "budget": 950.0,
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "old_ad_id": "1101",
                    "new_ad_id": "1102"
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0"',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0"',
            '"old_ad_id": "1101"',
            '"new_ad_id": "1102"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_004",
        instruction=(
            "You execute the frozen plan plan_2025-08-13 for 'Fall Collection Launch' on 2025-08-13 across ad sets 104 and 105. "
            "Anchor the run with a checksum and frozen plan, apply the plan’s budget and bid strategy to both ad sets. "
            "You verify the applied state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="compute_plan_checksum", kwargs={"date": "2025-08-13"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "execution_with_audit",
                "input_ref": {"plan_id": "plan_2025-08-13", "campaign_id": "3", "adsets": ["104", "105"]}
            }),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={"plan_id": "plan_2025-08-13"}),

        ],
        outputs=[
            '"campaign_id": "3"',
            '"plan_id": "plan_2025-08-13"',
            '"run_id": "run_2025-08-13"',
            '"ok": true',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_005",
        instruction=(
            "You file evidence of the daily insight for 'Back to School Deals' ad set 108 on 2025-08-13 by fetching that day's insights "
            "and anchoring them to the frozen plan for that date. Provide a one-row CSV and write a dated report."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "insight_anchor",
                "input_ref": {"plan_id": "plan_2025-08-13", "adset_id": "108", "date": "2025-08-13"}
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "6", "adset_id": "108", "date": "2025-08-13", "plan_id": "plan_2025-08-13"}]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"adset_id": "108"',
            '"date": "2025-08-13"',
            '"plan_id": "plan_2025-08-13"'
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_006",
        instruction=(
            "You create an Electronics snapshot on ad set 108 for 'Back to School Deals' effective 2025-08-13 by aligning it to plan_2025-08-13 "
            "(budget 800.0, bid strategy cost_cap with bid 45.0), verifying the applied state, and producing two artifacts: "
            "a dated report for 2025-08-13 and a compact CSV with fields [campaign_id, plan_id, adset_id, budget, bid_strategy, bid_amount]."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "6",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "108",
                        "budget": 800.0,
                        "bid_strategy": "cost_cap",
                        "bid_amount": 45.0
                    }
                ]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"})
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_007",
        instruction=(
            "You align the 'Global Summer Sale' campaign to the frozen plan for 2025-08-13 for ad set 112. "
            "You use plan_2025-08-13 as the source of truth and ensure both budget and bid strategy are applied. "
            "You confirm the updated state against the plan and export a CSV summarizing the final state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={
                "adset_id": "112",
                "new_budget": 700.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="set_adset_strategy", kwargs={
                "adset_id": "112",
                "bid_strategy": "lowest_cost",
                "reason": "plan_2025-08-13"
            }),
            Action(name="verify_applied", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "1",
                        "name": "Global Summer Sale",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "112",
                        "budget": 700.0,
                        "bid_strategy": "lowest_cost"
                    }
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "112"',
            '"budget": 700.0',
            '"bid_strategy": "lowest_cost"',
        ]),
        
Task(
    annotator="v3",
    user_id="task_008",
    instruction=(
        "You enforce the plan-selected creative for 'Global Summer Sale' ad set 101 as of 2025-08-13. "
        "You ensure ad 1102 (video) is the single active ad in the ad set and ad 1101 is paused, consistent with plan_2025-08-13. "
        "You deliver a compact CSV receipt with plan_id, adset_id, activate_id, pause_id, and final_active_status."
    ),
    actions=[
        Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
        Action(name="start_automation_run", kwargs={
            "run_type": "creative_rotation",
            "input_ref": {"campaign_id": "1", "adset_id": "101", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),
        Action(name="swap_ad_creatives", kwargs={"activate_id": "1102", "pause_id": "1101"}),
        Action(name="list_ads_in_adset", kwargs={"adset_id": "101"}),
        Action(name="verify_applied", kwargs={
            "expected_rows": [{"adset_id": "101", "active_ads": 1}],
            "actual_rows": [{"adset_id": "101", "active_ads": 1}],
            "key_fields": ["adset_id", "active_ads"]
        }),
        Action(name="record_creative_rotation", kwargs={
            "ad_id": "1102",
            "from_creative": "image",
            "to_creative": "video",
            "rotation_date": "2025-08-13"
        }),
        Action(name="export_report_csv", kwargs={
            "rows": [{
                "plan_id": "plan_2025-08-13",
                "adset_id": "101",
                "activate_id": "1102",
                "pause_id": "1101",
                "final_active_status": "active"
            }]
        }),
        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "rotation_ok": True,
                "adset_id": "101",
                "activate_id": "1102",
                "pause_id": "1101"
            }
        })
    ],
    outputs=[
        '"rotation_ok": True',
        '"adset_id": "101"',
        '"activate_id": "1102"',
        '"pause_id": "1101"'
    ]
),
        
Task(
    annotator="v3",
    user_id="task_009",
    instruction=(
        "You align the 'Holiday Season Early Bird' ad set 106 to plan_2025-08-13 as of 2025-08-13—"
        "budget 500.0 and cost_cap at 18.0—and you deliver a compact CSV with plan_id, campaign_id, adset_id, "
        "and checksum=a1b2c3d4e5f6 plus a dated markdown report."
    ),
    actions=[
        Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
        Action(name="list_campaign_adsets", kwargs={"campaign_id": "5"}),
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),

        Action(name="start_automation_run", kwargs={
            "run_type": "inventory_snapshot",
            "input_ref": {"campaign_id": "5", "adset_id": "106", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),

        # Required writes to satisfy the criterion:
        Action(name="update_adset_budget", kwargs={
            "adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"
        }),
        Action(name="set_adset_strategy", kwargs={
            "adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"
        }),

        # Verify alignment on budget/strategy:
        Action(name="fetch_adset", kwargs={"adset_id": "106"}),
        Action(name="verify_applied", kwargs={
            "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "actual_rows":   [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),

        # Deterministic checksum + freeze (evidence):
        Action(name="compute_plan_checksum", kwargs={"date": "2025-08-13"}),
        Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),

        # Receipts:
        Action(name="export_report_csv", kwargs={
            "rows": [{"plan_id": "plan_2025-08-13", "campaign_id": "5", "adset_id": "106", "checksum": "a1b2c3d4e5f6"}]
        }),
        Action(name="write_report", kwargs={
            "date": "2025-08-13",
            "title": "Inventory Snapshot 2025-08-13 - plan_2025-08-13",
            "tags": ["inventory", "snapshot", "plan_2025-08-13"]
        }),
        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "snapshot_ok": True,
                "campaign_id": "5",
                "adset_id": "106",
                "plan_id": "plan_2025-08-13",
                "checksum": "a1b2c3d4e5f6"
            }
        })
    ],
    outputs=[
        '"campaign_id": "5"',
        '"adset_id": "106"',
        '"plan_id": "plan_2025-08-13"',
        '"checksum": "a1b2c3d4e5f6"',
        '"snapshot_ok": true'
    ]
),    
Task(
    annotator="v3",
    user_id="task_010",
    instruction=(
        "You enforce the plan-selected creative type for 'Global Summer Sale' ad set 101 as of 2025-08-13. "
        "Use the frozen plan for 2025-08-13 as the source of truth for the required creative_type. "
        "Ensure exactly one active ad in the ad set and that the active ad's creative_type matches the plan. "
        "Publish an auditable run and export a compact CSV receipt with plan_id, adset_id, active_ad_id, and active_creative_type."
    ),
    actions=[
        Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
        Action(name="list_ads_in_adset", kwargs={"adset_id": "101"}),
        Action(name="start_automation_run", kwargs={
            "run_type": "creative_rotation",
            "input_ref": {"campaign_id": "1", "adset_id": "101", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),
        Action(name="swap_ad_creatives", kwargs={"activate_id": "1102", "pause_id": "1101"}),
        Action(name="list_ads_in_adset", kwargs={"adset_id": "101"}),
        Action(name="verify_applied", kwargs={
            "expected_rows": [{"adset_id": "101", "active_ads": 1, "active_creative_type": "video"}],
            "actual_rows": [{"adset_id": "101", "active_ads": 1, "active_creative_type": "video"}],
            "key_fields": ["adset_id", "active_ads", "active_creative_type"]
        }),
        Action(name="export_report_csv", kwargs={
            "rows": [{
                "plan_id": "plan_2025-08-13",
                "adset_id": "101",
                "active_ad_id": "1102",
                "active_creative_type": "video"
            }]
        }),
        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "rotation_ok": True,
                "adset_id": "101",
                "active_ad_id": "1102",
                "active_creative_type": "video"
            }
        })
    ],
    outputs=[
        '"rotation_ok": true',
        '"adset_id": "101"',
        '"active_ad_id": "1102"',
        '"active_creative_type": "video"'
    ]
),

    Task(
        annotator="v3",
        user_id="task_011",
        instruction=(
            "You bring the 'Global Summer Sale' campaign into alignment with the frozen plan for 2025-08-13 for ad set 101. "
            "You use plan_2025-08-13 and ensure budget and bid are applied, with all updates recorded. "
            "You then verify the ad set reflects the planned budget and bid strategy."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_012",
        instruction=(
            "You bring the 'Fall Collection Launch' campaign into alignment with the frozen plan for 2025-08-13 for ad set 104. "
            "You use plan_2025-08-13 and ensure budget and bid are applied, with all updates recorded. You fetch the ad set to confirm the update."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "104"}),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"budget": 750.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 22.0'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_013",
        instruction=(
            "You confirm compliance for the 'Fall Collection Launch' campaign against the frozen plan for 2025-08-13 "
            "for ad set 105. You use plan_id 'plan_2025-08-13' and you ensure budget 750.0 and bid strategy lowest_cost "
            "are applied. You export a CSV with the final configuration."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "3",
                        "name": "Fall Collection Launch",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "105",
                        "budget": 750.0,
                        "bid_strategy": "lowest_cost"
                    }
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "lowest_cost"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_014",
        instruction=(
            "You bring ad set 106 in 'Holiday Season Early Bird' into alignment with plan_2025-08-13 and confirm the applied state matches the plan."
        ),
        actions=[
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "actual_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"budget": 500.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 18.0',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_015",
        instruction=(
            "You confirm the 'Holiday Season Early Bird' campaign is aligned to the frozen plan for 2025-08-13 for ad set 107. "
            "You use plan_2025-08-13 and you ensure budget and bid strategy are applied. "
            "You export a CSV summarizing the final state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "5",
                        "name": "Holiday Season Early Bird",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "107",
                        "budget": 400.0,
                        "bid_strategy": "lowest_cost"
                    }
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"name": "Holiday Season Early Bird"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "107"',
            '"budget": 400.0',
            '"bid_strategy": "lowest_cost"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_016",
        instruction=(
            "You enforce the budget rounding policy on 2025-08-13 for the Global Summer Sale campaign. "
            "You confirm the policy rule named 'budget_rounding_unit' and align ad sets to 'plan_2025-08-13': "
            "ad set 101 and ad set 112 budget, strategy, and bid in line with plan guidelines. "
            "You confirm the final states match the plan values."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_policy_rule", kwargs={"rule_name": "budget_rounding_unit"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "112"}),

            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"name": "budget_rounding_unit"',
            '"value": "10"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
            '"adset_id": "112"',
            '"budget": 700.0',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_017",
        instruction=(
            "You carry out a maintenance toggle for the 'Global Summer Sale' campaign on 2025-08-13. "
            "You briefly activate the campaign, ensure ad set 102 matches plan_2025-08-13 budget and bid strategy, "
            "then return the campaign to a paused state. Provide an auditable record and a CSV with the final configuration."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "maintenance_toggle",
                "input_ref": {"campaign_id": "1", "adset_id": "102", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="start_campaign", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="stop_campaign", kwargs={"campaign_id": "1"}),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "1", "status": "paused", "plan_id": "plan_2025-08-13", "adset_id": "102", "budget": 600.0,
                     "bid_strategy": "lowest_cost"}
                ]
            }),
            Action(name="end_automation_run", kwargs={"run_id": "run_2025-08-13", "errors_json": {}})
        ],
        outputs=[
            '"campaign_id": "1"',
            '"status": "paused"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
            '"budget": 600.0"',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_018",
        instruction=(
            "You review the 'Fall Collection Launch' campaign on 2025-08-13 for adset 104. "
            "You ensure ad budget, bid strategy, and bid are updated to match plan_2025-08-13. "
            "You write a report and export a CSV."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "104"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                "actual_rows": [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "3", "plan_id": "plan_2025-08-13", "adset_id": "104",
                          "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"budget": 750.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 22.0',
            '"ok": true',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_019",
        instruction=(
            "You conduct a post-pause compliance check for the 'Back to School Deals' campaign adset 108 on 2025-08-13 against the "
            "frozen source of truth plan_2025-08-13. You will complete the changes found in the plan with the campaign "
            "returning to a paused state after the check. "
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
            Action(name="stop_campaign", kwargs={"campaign_id": "6", "reason": "plan_2025-08-13"}),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School Deals"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0',
            '"status": "paused"',
        ]
    ),

        Task(
            annotator="v3",
            user_id="task_020",
            instruction=(
                "You align the 'Holiday Season Early Bird' ad set 107 to plan_2025-08-13 as of 2025-08-13: "
                "You consider the ad set’s 2025-08-13 performance and confirm the final state matches those values."
            ),
            actions=[
                Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
                Action(name="daily_adset_insights", kwargs={"adset_id": "107", "date": "2025-08-13"}),
                Action(name="calc_roas", kwargs={"adset_id": "107", "date": "2025-08-13"}),
                Action(name="update_adset_budget", kwargs={
                    "adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"
                }),
                Action(name="set_adset_strategy", kwargs={
                    "adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"
                }),
                Action(name="fetch_adset", kwargs={"adset_id": "107"}),
                Action(name="verify_applied", kwargs={
                    "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
                    "actual_rows":   [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
                    "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
                }),
            ],
            outputs=[
                '"plan_id": "plan_2025-08-13"',
                '"adset_id": "107"',
                '"budget": 400.0',
                '"bid_strategy": "lowest_cost"',
                '"ok": true'
            ]
        ),

    Task(
        annotator="v3",
        user_id="task_021",
        instruction=(
            "You apply the frozen plan plan_2025-08-13 to ad set 102 in 'Global Summer Sale', "
            "ensuring its budget and strategy exactly match the plan. You confirm the change and "
            "export a compact CSV receipt with campaign_id, name, plan_id, adset_id, budget, "
            "bid_strategy, and ok."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "plan_execution",
                "input_ref": {"campaign_id": "1", "adset_id": "102", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="update_adset_budget", kwargs={
                "adset_id": "102",
                "new_budget": 600.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {"applied": True, "adset_id": "102", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "1",
                    "name": "Global Summer Sale",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102",
                    "budget": 600.0,
                    "bid_strategy": "lowest_cost",
                    "ok": True
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
            '"budget": 600.0"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_022",
        instruction=(
            "You update the live ad set 102 in 'Global Summer Sale' to match the frozen plan for 2025-08-13. "
            "You apply the required budget and bidding per plan_2025-08-13, and confirm the live state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}]}),
            ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
        ],
    ),

Task(
    annotator="v3",
    user_id="task_023",
    instruction=(
        "You perform a cross-campaign alignment on 2025-08-13, updating Global Summer Sale ad set 101 and confirming "
        "Holiday Season Early Bird ad set 106 match plan_2025-08-13. You verify both ad sets are aligned."
    ),
    actions=[
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
        Action(name="fetch_adset", kwargs={"adset_id": "101"}),
        Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
        Action(name="set_adset_strategy", kwargs={
            "adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"
        }),
        Action(name="fetch_adset", kwargs={"adset_id": "101"}),
        Action(name="fetch_adset", kwargs={"adset_id": "106"}),
        Action(name="verify_applied", kwargs={
            "expected_rows": [
                {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}
            ],
            "actual_rows": [
                {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}
            ],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),
    ],
    outputs=[
        '"plan_id": "plan_2025-08-13"',
        '"adset_id": "101"',
        '"budget": 950.0',
        '"bid_strategy": "cost_cap"',
        '"bid_amount": 35.0',
        '"adset_id": "106"',
        '"budget": 500.0',
        '"bid_strategy": "cost_cap"',
        '"bid_amount": 18.0',
        '"ok": true'
    ]
),

    Task(
        annotator="v3",
        user_id="task_024",
        instruction=(
            "You finalize compliance for 'Back to School Deals' on 2025-08-13. "
            "Using plan_id 'plan_2025-08-13', you ensure ad set 108 is aligned with its budget and bid strategy. "
            "You confirm the state, write a report with tags ['compliance','bts'] and export a CSV."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["compliance", "bts"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "6", "name": "Back to School Deals", "plan_id": "plan_2025-08-13", "adset_id": "108",
                          "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School Deals"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0"',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0"',
            '"ok": true',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_025",
        instruction=(
            "You bring the 'Holiday Season Early Bird' campaign into alignment with the frozen plan for 2025-08-13 for ad set 107. "
            "You use plan_2025-08-13 and ensure budget and bid are applied, with all updates recorded. You fetch the ad set to confirm the update."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "107"}),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"name": "Holiday Season Early Bird"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "107"',
            '"budget": 400.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),
        
        Task(
            annotator="v3",
            user_id="task_026",
            instruction=(
                "You enforce the frozen plan for 'Back to School Deals' dated 2025-08-13 (plan_id 'plan_2025-08-13'). "
                "You ensure ad sets 107 and 108 match the aligned states for that date and verify the updates."
            ),
            actions=[
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
        
                # Budgets first (ascending adset_id)
                Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
                Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
        
                # Then strategies (ascending adset_id)
                Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
                Action(name="set_adset_strategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
        
                Action(name="verify_applied", kwargs={
                    "expected_rows": [
                        {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None},
                        {"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}
                    ],
                    "actual_rows": [
                        {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None},
                        {"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}
                    ],
                    "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
                }),
            ],
            outputs=[
                '"plan_id": "plan_2025-08-13"',
                '"ok": true'
            ]
        ),

    Task(
        annotator="v3",
        user_id="task_027",
        instruction=(
            "You maintain an auditable health snapshot for 'Back to School Deals' on 2025-08-13 anchored to the frozen plan. "
            "Ensure a completed health snapshot run is recorded and export a CSV receipt with columns: campaign_id, plan_id, run_id."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="freeze_plan", kwargs={"plan_id": "plan_2025-08-13", "date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "health_snapshot",
                "input_ref": {"plan_id": "plan_2025-08-13"}
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "outputs_json": {"plan_id": "plan_2025-08-13"},
                "errors_json": {}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "6", "plan_id": "plan_2025-08-13", "run_id": "run_2025-08-13"}],
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"run_id": "run_2025-08-13"'
        ]
    ),
        
        
    Task(
        annotator="v3",
        user_id="task_028",
        instruction=(
            "You reconcile ad set 102 under the 'Global Summer Sale' campaign to the frozen plan for 2025-08-13, "
            "confirm the final state, and produce a one-row CSV receipt containing: "
            "campaign_id, plan_id, adset_id, adset_name, budget, bid_strategy."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "102", "daily_budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "daily_budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "daily_budget", "bid_strategy"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "1",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102",
                    "adset_name": "Apparel - US",
                    "budget": 600.0,
                    "bid_strategy": "lowest_cost"
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
            '"adset_name": "Apparel - US"',
            '"budget": 600.0"',
            '"bid_strategy": "lowest_cost"',
        ]
    ),


    Task(
        annotator="v3",
        user_id="task_029",
        instruction=(
            "You re-affirm 'Holiday Season Early Bird' ad set 106 to plan_id 'plan_2025-08-13' on 2025-08-13, "
            "enforcing budget and bid. You then verify the applied state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "actual_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"budget": 500.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 18.0',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_030",
        instruction=(
            "You safeguard the plan integrity for 'Global Summer Sale' on 2025-08-13 using plan_2025-08-13. "
            "You'll record integrity evidence, freeze the plan, and provide a report with tags ['integrity','gss'], "
            "and a CSV that notes plan_id and plan status."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="compute_plan_checksum", kwargs={"date": "2025-08-13"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["integrity", "gss"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"plan_id": "plan_2025-08-13", "Status": "frozen"}],
            }),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_031",
        instruction=(
            "You do a quick apply-and-fetch for 'Back to School Deals' ad set 108 on 2025-08-13. "
            "You ensure the ad set matches the plan 'plan_2025-08-13', then fetch the ad set."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_032",
        instruction=(
            "You confirm compliance on 'Global Summer Sale' ad set 101 for 2025-08-13. "
            "You align adset 101 per plan_id 'plan_2025-08-13' and export a CSV."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "101",
                          "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_033",
        instruction=(
            "You reconcile ad set 101 in 'Global Summer Sale' to the frozen plan for 2025-08-13 as the source of truth. "
            "You will ensure the plan’s configuration is applied and confirm the applied state matches the plan; persist a compact CSV summary."
        ),
        actions=[
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={
                "adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"
            }),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "adset_id": "101", "budget": 950.0,
                     "bid_strategy": "cost_cap", "bid_amount": 35.0, "status": "ok"}
                ]
            }),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
            '"status": "ok"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_034",
        instruction=(
            "You ensure that, in the 'Back to School Deals' campaign, ad set 108 conforms to the frozen plan as of 2025-08-13 "
            "identified by plan_2025-08-13'. You will make any changes to align and then complete verification of the changes."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School Deals"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0"',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_035",
        instruction=(
            "You issue a minimal plan compliance pass for 'Fall Collection Launch' ad set 105 on 2025-08-13. "
            "Set budget and strategy per plan_2025-08-13, then confirm with a CSV of the final state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={
                "adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "105"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "3",
                    "name": "Fall Collection Launch",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105",
                    "budget": 750.0,
                    "bid_strategy": "lowest_cost"
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_036",
        instruction=(
            "You confirm end-to-end alignment for 'Global Summer Sale' on 2025-08-13. "
            "Using plan_2025-08-13 as the source of truth, ensure ad sets 101 and 112 align with plan "
            "strategies. Document the alignment in a report with tags ['alignment','gss'] Export to CSV listing the aligned rows."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "112"}),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["alignment", "gss"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
            '"adset_id": "112"',
            '"budget": 700.0',
            '"bid_strategy": "lowest_cost"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_037",
        instruction=(
            "You reconcile the 'Fall Collection Launch' campaign to the frozen plan for 2025-08-13 adsets 104 and 105. "
            "Apply the plan to the specified ad sets and confirm the result."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap"},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap"},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            })
        ],
        outputs=['"ok": true']
    ),

    

    Task(
        annotator="v3",
        user_id="task_038",
        instruction=(
            "You align the 'Global Summer Sale' campaign on 2025-08-13 to the frozen source of truth plan_2025-08-13 for ad set 101. "
            "Apply the plan’s budget and bid strategy if needed, confirm the aligned state, write a dated note, and export a compact CSV receipt."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "1",
                    "name": "Global Summer Sale",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101",
                    "budget": 950.0,
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "ok": True
                }],
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0"',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0"',
            '"ok": true',
        ]
    ),
    
Task(
    annotator="v3",
    user_id="task_039",
    instruction=(
        "You perform a plan-scored alignment for 'Holiday Season Early Bird' ad set 107 as of 2025-08-13: "
        "you set its budget to 400.0 and its bid strategy to lowest_cost exactly as recorded in plan_2025-08-13. "
        "You score the 2025-08-13 performance for audit, freeze the plan snapshot as evidence, and provide a compact CSV "
        "with campaign_id, name, plan_id, adset_id, budget, and bid_strategy."
    ),
    actions=[
        Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),

        # Score delivery for the date (domain proposal: KPI-driven/scored)
        Action(name="daily_adset_insights", kwargs={"adset_id": "107", "date": "2025-08-13"}),
        Action(name="calc_roas", kwargs={"adset_id": "107", "date": "2025-08-13"}),

        # Evidence of plan state
        Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),

        # Auditable run boundary
        Action(name="start_automation_run", kwargs={
            "run_type": "plan_apply_scored",
            "input_ref": {"campaign_id": "5", "adset_id": "107", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),

        # Deterministic writes from the plan
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
        Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
        Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

        # Verify final state
        Action(name="fetch_adset", kwargs={"adset_id": "107"}),
        Action(name="verify_applied", kwargs={
            "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
            "actual_rows":   [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),

        # Receipt
        Action(name="export_report_csv", kwargs={
            "rows": [{
                "campaign_id": "5",
                "name": "Holiday Season Early Bird",
                "plan_id": "plan_2025-08-13",
                "adset_id": "107",
                "budget": 400.0,
                "bid_strategy": "lowest_cost"
            }]
        }),

        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "campaign_id": "5",
                "name": "Holiday Season Early Bird",
                "plan_id": "plan_2025-08-13",
                "adset_id": "107",
                "budget": 400.0,
                "bid_strategy": "lowest_cost",
                "ok": True
            }
        })
    ],
    outputs=[
        '"campaign_id": "5"',
        '"name": "Holiday Season Early Bird"',
        '"plan_id": "plan_2025-08-13"',
        '"adset_id": "107"',
        '"budget": 400.0',
        '"bid_strategy": "lowest_cost"'
    ]
),

    Task(
        annotator="v3",
        user_id="task_040",
        instruction=(
            "You reconcile the 'Fall Collection Launch' campaign to the frozen plan for 2025-08-13. "
            "Use plan_id 'plan_2025-08-13' as the source of truth: for ad set 104 and 105 set budget "
            "and bid strategy; You will fetch both ad sets to confirm alignment."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "104"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "105"}),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"budget": 750.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 22.0',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

        Task(
            annotator="v3",
            user_id="task_041",
            instruction=(
                "You finalize the configuration for the 'Fall Collection Launch' ad set 105 under plan_2025-08-13. "
                "You ensure its bid strategy is lowest_cost and its budget is 750.0, and you provide a compact CSV and a dated report."
            ),
            actions=[
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
                Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
        
                Action(name="start_automation_run", kwargs={
                    "run_type": "alignment",
                    "input_ref": {"adset_id": "105", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
                }),
                Action(name="set_adset_strategy", kwargs={
                    "adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"
                }),
                Action(name="write_report", kwargs={"date": "2025-08-13", "tags": ["105"]}),
                Action(name="fetch_adset", kwargs={"adset_id": "105"}),
                Action(name="verify_applied", kwargs={
                    "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                    "actual_rows":   [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                    "key_fields": ["adset_id", "budget", "bid_strategy"]
                }),
                Action(name="export_report_csv", kwargs={
                    "rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}]
                }),
                Action(name="end_automation_run", kwargs={
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "ok": True,
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "105",
                        "budget": 750.0,
                        "bid_strategy": "lowest_cost"
                    }
                })
            ],
            outputs=[
                '"plan_id": "plan_2025-08-13"',
                '"adset_id": "105"',
                '"budget": 750.0',
                '"bid_strategy": "lowest_cost"',
                '"ok": true'
            ]
        ),
        
    Task(
        annotator="v3",
        user_id="task_042",
        instruction=(
            "You reconcile ad set 102 in 'Global Summer Sale' to the frozen plan dated 2025-08-13 as the source of truth. "
            "You'll confirm the applied configuration matches the plan and persist a compact CSV summary."
        ),
        actions=[
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102",
                    "budget": 600.0,
                    "bid_strategy": "lowest_cost",
                    "status": "ok"
                }]
            }),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
            '"budget": 600.0',
            '"bid_strategy": "lowest_cost"',
            '"status": "ok"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_043",
        instruction=(
            "You evaluate delivery for 'Fall Collection Launch' on 2025-08-13 for ad set 104, compute ROAS from the "
            "same-day insights, and then align the ad set to plan_2025-08-13 then verify the aligned end state against the plan."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="calc_roas", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={"plan_id": "plan_2025-08-13"}),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"budget": 750.0',
            '"bid_strategy": "cost_cap"',
            '"ok": true',
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_044",
        instruction=(
            "You reconcile ad sets 104 and 105 in 'Fall Collection Launch' to the frozen plan dated 2025-08-13 as the source of truth. "
            "Confirm applied states match the plan for 104 (budget 750.0, cost_cap with bid 22.0) and 105 (budget 750.0, lowest_cost). "
            "Persist a compact CSV summary and a dated note."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap"},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap"},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),

            Action(name="write_report", kwargs={"date": "2025-08-13"}),

            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0,
                     "status": "ok"},
                    {"plan_id": "plan_2025-08-13", "adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost", "status": "ok"}
                ]
            })
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "cost_cap"',
            '"bid_strategy": "lowest_cost"',
            '"status": "ok"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_045",
        instruction=(
            "You evaluate delivery for 'Fall Collection Launch' on 2025-08-13 for ad set 105, compute ROAS from the "
            "same-day insights, and then align the ad set to plan_2025-08-13 then verify the aligned end state against the plan."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="calc_roas", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={"plan_id": "plan_2025-08-13"}),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "lowest_cost"',
            '"ok": true',
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_046",
        instruction=(
            "You align Holiday Season Early Bird ad set 106 to the 2025-08-13 frozen plan. "
            "Apply budget 500.0 and bid strategy cost_cap with bid_amount 18.0 per plan_id 'plan_2025-08-13', then confirm the applied state."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "106"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "actual_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            })
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"budget": 500.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 18.0',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_047",
        instruction=(
            "You align the 'Fall Collection Launch' campaign on 2025-08-13 with the frozen plan plan_2025-08-13 by ensuring ad set 105’s budget and bid strategy match the plan. "
            "Confirm the aligned state in a dated report and export a CSV recording the settled values."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "3",
                    "name": "Fall Collection Launch",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105",
                    "budget": 750.0,
                    "bid_strategy": "lowest_cost",
                    "ok": True
                }],
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"budget": 750.0"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_048",
        instruction=(
            "You run an exception audit for 'Global Summer Sale' dated 2025-08-13 against plan_2025-08-13. "
            "Using rules zero_delivery_impressions=0, cap_hit_spend=1000.0, and data_gap_days=2, you record exceptions in the system "
            "for the provided insights—101(impressions=1200, spend=480.0, missing_days=0) and "
            "102(impressions=0, spend=0.0, missing_days=2). You produce two artifacts: a CSV enumerating the triggered alerts "
            "for adset_id 102 (zero_delivery and data_gap), and a dated report with tags ['gss','exceptions']."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="raise_exceptions", kwargs={
                "plan_id": "plan_2025-08-13",
                "insights": [
                    {"adset_id": "101", "impressions": 1200, "spend": 480.0, "missing_days": 0},
                    {"adset_id": "102", "impressions": 0, "spend": 0.0, "missing_days": 2}
                ],
                "rules": {"zero_delivery_impressions": 0, "cap_hit_spend": 1000.0, "data_gap_days": 2}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "adset_id": "102", "alert": "zero_delivery"},
                    {"plan_id": "plan_2025-08-13", "adset_id": "102", "alert": "data_gap"}
                ],
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["gss", "exceptions"]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"count": 2',
            '"type": "zero_delivery"',
            '"type": "data_gap"',
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_049",
        instruction=(
            "You produce an auditable rolling range view for 'Global Summer Sale' covering 2025-08-10..2025-08-13 tied to the "
            "2025-08-13 state of record. Anchor evidence by keeping the 2025-08-13 plan frozen. Include the campaign’s spend over that range, "
            "and include the total spend value in the CSV. Provide a dated record and a CSV enumerating one row for campaign_id '1' "
            "over the stated range with metric 'spend'."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "rolling_range_view",
                "input_ref": {"campaign_id": "1", "range": "2025-08-10..2025-08-13", "anchor_date": "2025-08-13"}
            }),
            Action(name="range_spend", kwargs={"campaign_id": "1", "start_date": "2025-08-10", "end_date": "2025-08-13"}),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "1", "metric": "spend", "range": "2025-08-10..2025-08-13", "total_spend": 0.0}
                ]
            }),
            Action(name="end_automation_run", kwargs={"run_id": "run_2025-08-13", "errors_json": {}})
        ],
        outputs=[
            '"campaign_id": "1"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_050",
        instruction=(
            "You align 'Holiday Season Early Bird' ad set 107 to plan_2025-08-13 as of 2025-08-13: "
            "set its budget to 400.0 and its bid strategy to lowest_cost. "
            "You return a compact task output containing plan_id, adset_id, budget, and bid_strategy."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "107"})
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "107"',
            '"budget": 400.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_051",
        instruction=(
            "You align the 'Back to School Deals' campaign to the frozen plan for 2025-08-13. "
            "Using plan_id 'plan_2025-08-13' as the source of truth, you ensure ad set 108 reflects budget 800.0 "
            "and cost_cap with bid 45.0. You confirm the configuration matches the plan."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),

            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}
                ],
                "actual_rows": [
                    {"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School Deals"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_052",
        instruction=(
            "You align the 'Holiday Season Early Bird' campaign to the frozen plan for 2025-08-13. "
            "Ensure ad sets 106 and 107 match the plan's budget and bid strategy, and verify the applied values."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "106"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "107"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"name": "Holiday Season Early Bird"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"budget": 500.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 18.0',
            '"adset_id": "107"',
            '"budget": 400.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_053",
        instruction=(
            "You reconcile 'Global Summer Sale' to the frozen plan for 2025-08-13 for ad set 102. "
            "You ensure budget and bid strategy is applied and verified."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_054",
        instruction=(
            "You are responsible for alignment of 'Global Summer Sale' ad set 101 to the 2025-08-13 reference plan "
            "plan_2025-08-13. Your target state is budget 950.0 and bid strategy cost_cap with bid_amount 35.0. "
            "Success is defined as the live configuration matching that target and producing auditable evidence. "
            "Deliverables: a dated note tagged ['alignment'] and a CSV containing a single receipt row with "
            "plan_id, adset_id, budget, bid_strategy, and bid_amount."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}]
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["alignment"]
            }),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"ok": true',
        ]
    ),

Task(
    annotator="v3",
    user_id="task_055",
    instruction=(
        "You start an automation run on 2025-08-13 to reconcile 'Global Summer Sale' ad sets 101 and 102 to plan_2025-08-13, "
        "and then complete the run."
    ),
    actions=[
        Action(name="start_automation_run", kwargs={
            "run_type": "reconcile",
            "input_ref": {"plan_id": "plan_2025-08-13", "adsets": ["101", "102"]}
        }),
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
        Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
        Action(
            name="set_adset_strategy",
            kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}
        ),
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
        Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
        Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "run_id": "run_2025-08-13",
                "plan_id": "plan_2025-08-13",
                "adset_ids": ["101", "102"]
            }
        }),
    ],
    outputs=[
        '"run_id": "run_2025-08-13"',
        '"plan_id": "plan_2025-08-13"',
        '"adset_ids": ["101", "102"]',
    ],
),

    Task(
        annotator="v3",
        user_id="task_056",
        instruction=(
            "You verify 'Back to School Deals' ad set 107 against the 2025-08-13 frozen plan, persist the verification by freezing the plan, "
            "and write a report with tag ['bts']."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["bts"]
            })
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "107"',
            '"ok": true',
        ]
    ),


    Task(
        annotator="v3",
        user_id="task_057",
        instruction=(
            "You will reconcile the ‘Global Summer Sale’ campaign to the frozen plan for 2025-08-13, "
            "ensuring ad sets 101, 102, and 112 match the specified budgets and bid strategies from plan_id "
            "‘plan_2025-08-13’. Confirm that final ad set states are consistent with the plan values."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "112"}),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
            '"adset_id": "102"',
            '"budget": 600.0',
            '"bid_strategy": "lowest_cost"',
            '"adset_id": "112"',
            '"budget": 700.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_058",
        instruction=(
            "You reconcile the 'Global Summer Sale' campaign to the frozen plan for 2025-08-13. You ensure ad sets 101 "
            "and 102 reflect plan_2025-08-13 and you verify final budgets and bid strategies match. "
            "You write a report dated 2025-08-13 with tags ['apply','verification','gss']. You also export a CSV summarizing the aligned rows."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["apply", "verification", "gss"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "101",
                     "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "102",
                     "budget": 600.0, "bid_strategy": "lowest_cost", "bid_amount": None}
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"budget": 950.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 35.0',
            '"adset_id": "102"',
            '"budget": 600.0',
            '"bid_strategy": "lowest_cost"',
            '"ok": true',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_059",
        instruction=(
            "You stage ad set 112 in 'Fall Collection Launch' for QA effective 2025-08-13 by aligning it exactly to plan_2025-08-13 "
            "After applying changes, you verify the applied state matches the plan."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}]
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"adset_id": "112"',
            '"budget": 700.0',
            '"ok": true'
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_060",
        instruction=(
            "You create an insights snapshot for 'Back to School Deals' ad set 107 as of 2025-08-13, "
            "anchored to plan_2025-08-13 as the frozen source of truth. "
            "You preserve auditability (plan evidence and snapshot context) and deliver a compact CSV with "
            "campaign_id, adset_id, date, and plan_id, plus a dated report."
        ),

        actions=[
            Action(name="start_automation_run", kwargs={
                "run_type": "snapshot",
                "input_ref": {"campaign": "Back to School Deals", "adset_id": "107", "date": "2025-08-13"}
            }),
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "6", "adset_id": "107", "date": "2025-08-13", "plan_id": "plan_2025-08-13"}]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {}
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"adset_id": "107"',
            '"date": "2025-08-13"',
            '"plan_id": "plan_2025-08-13"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_061",
        instruction=(
            "You produce two spend‑window summaries for 'Global Summer Sale' ad set 101 for 2025-08-10..2025-08-11 and 2025-08-12..2025-08-13, "
            "tie them to the 2025-08-13 plan state with a frozen snapshot, and deliver a CSV artifact tagged ['spend','windows','gss'] plus a dated report."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={
                "run_type": "window_spend_snapshot",
                "input_ref": {"campaign": "Global Summer Sale", "adset_id": "101", "snapshot_date": "2025-08-13"}
            }),
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="range_spend", kwargs={"adset_id": "101", "start_date": "2025-08-10", "end_date": "2025-08-11"}),
            Action(name="range_spend", kwargs={"adset_id": "101", "start_date": "2025-08-12", "end_date": "2025-08-13"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"adset_id": "101", "range": "2025-08-10..2025-08-11", "plan_id": "plan_2025-08-13"},
                    {"adset_id": "101", "range": "2025-08-12..2025-08-13", "plan_id": "plan_2025-08-13"}
                ]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13", "tags": ["spend", "windows", "gss"]}),
            Action(name="end_automation_run", kwargs={"run_id": "run_2025-08-13", "errors_json": {}}),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"adset_id": "101"'
        ]
    ),

        Task(
        annotator="v3",
        user_id="task_062",
        instruction=(
            "You verify and seal the plan for 'Back to School Deals' on 2025-08-13 by confirming integrity against a checksum, "
            "persisting the frozen snapshot for audit, and producing a one-row CSV receipt of the verification."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "plan_verification",
                "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="compute_plan_checksum", kwargs={"date": "2025-08-13"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"plan_id": "plan_2025-08-13"}],
                "actual_rows":   [{"plan_id": "plan_2025-08-13"}],
                "key_fields": ["plan_id"]
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {"verification": "ok", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "6",
                    "plan_id": "plan_2025-08-13",
                    "status": "ok"
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"status": "ok"'
        ],
    ),
    
    Task(
        annotator="v3",
        user_id="task_063",
        instruction=(
            "You bring the 'Fall Collection Launch' campaign into compliance with the frozen plan for 2025-08-13. "
            "You ensure ad sets 104 and 105 reflect plan_2025-08-13 so that budget and bid strategy values  "
            " match the plan. You write a report dated 2025-08-13 with tags ['compliance','fall']. "
            "You also export a CSV listing the compliant ad sets."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),

            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "104"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "105"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["compliance", "fall"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "3", "plan_id": "plan_2025-08-13", "adset_id": "104",
                     "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0},
                    {"campaign_id": "3", "plan_id": "plan_2025-08-13", "adset_id": "105",
                     "budget": 750.0, "bid_strategy": "lowest_cost"}
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"budget": 750.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 22.0',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "lowest_cost"',
            '"ok": true',
        ]
    ),

        Task(
            annotator="v3",
            user_id="task_064",
            instruction=(
                "You audit 'Back to School Deals' ad set 108 as of 2025-08-13 against plan_2025-08-13. "
                "You record the audit outcome as structured rule exceptions linked to plan_2025-08-13 and freeze the plan snapshot as evidence. "
                "You deliver a one-row compact CSV with plan_id and adset_id and write a dated report tagged ['rules','audit','bts']."
            ),
            actions=[
                Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
                Action(name="fetch_adset", kwargs={"adset_id": "108"}),
                Action(name="raise_exceptions", kwargs={
                    "date": "2025-08-13",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108",
                    "rules": {"policy_check": "audit"}
                }),
                Action(name="export_report_csv", kwargs={
                    "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "108"}]
                }),
                Action(name="write_report", kwargs={
                    "date": "2025-08-13",
                    "tags": ["rules", "audit", "bts"]
                })
            ],
            outputs=[
                '"plan_id": "plan_2025-08-13"',
                '"adset_id": "108"'
            ]
        ),
                             
        Task(
            annotator="v3",
            user_id="task_065",
            instruction=(
                "You enact the planned creative rotation for 'Global Summer Sale' ad set 101 as of 2025-08-13: "
                "ad 1102 (video) must be the single active ad and ad 1101 (image) must be paused, exactly as in plan_2025-08-13. "
                "You may reference the 2025-08-13 insights for context only—they do not change the rotation. "
                "You provide a compact CSV containing campaign_id, adset_id, activate_id, pause_id, and date."
            ),
            actions=[
                Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
                Action(name="daily_adset_insights", kwargs={"adset_id": "101", "date": "2025-08-13"}),
        
                Action(name="start_automation_run", kwargs={
                    "run_type": "creative_rotation",
                    "input_ref": {"campaign_id": "1", "adset_id": "101", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
                }),
        
                Action(name="record_creative_rotation", kwargs={
                    "ad_id": "1102",
                    "from_creative": "image",
                    "to_creative": "video",
                    "rotation_date": "2025-08-13"
                }),
                Action(name="swap_ad_creatives", kwargs={"activate_id": "1102", "pause_id": "1101"}),
        
                Action(name="list_ads_in_adset", kwargs={"adset_id": "101"}),
                Action(name="verify_applied", kwargs={
                    "expected_rows": [{"adset_id": "101", "active_ads": 1}],
                    "actual_rows":   [{"adset_id": "101", "active_ads": 1}],
                    "key_fields": ["adset_id", "active_ads"]
                }),
        
                Action(name="export_report_csv", kwargs={
                    "rows": [{
                        "campaign_id": "1",
                        "adset_id": "101",
                        "activate_id": "1102",
                        "pause_id": "1101",
                        "date": "2025-08-13"
                    }]
                }),
                Action(name="write_report", kwargs={"date": "2025-08-13"}),
                Action(name="end_automation_run", kwargs={
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "ok": True,
                        "campaign_id": "1",
                        "adset_id": "101"
                    }
                })
            ],
            outputs=[
                '"campaign_id": "1"',
                '"adset_id": "101"'
            ]
        ),

    Task(
        annotator="v3",
        user_id="task_066",
        instruction=(
            "You reconcile adset 101 ad set in 'Global Summer Sale' to match the frozen plan for 2025-08-13, "
            "verifying the applied budget and bid strategy. Maintain an auditable record with a dated report "
            "and record the reconciliation with a CSV artifact."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap",
                          "bid_amount": 35.0}]
            })
        ],
        outputs=[
            '"campaign_id": "1"',
            '"adset_id": "101"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_067",
        instruction=(
            "You reconcile 'Fall Collection Launch' so that 'Fall Fashion - Women' and 'Fall Fashion - Men' reflect the frozen plan for 2025-08-13, "
            "and you provide a CSV artifact as the audit record."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost", "bid_amount": None}
                ],
                "actual_rows": [
                    {"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0},
                    {"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost", "bid_amount": None}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),

            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "3", "adset_id": "104"},
                    {"campaign_id": "3", "adset_id": "105"}
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
        ],
    ),

        Task(
            annotator="v3",
            user_id="task_068",
            instruction=(
                "You compile a same-day audit snapshot for 'Back to School Deals' ad sets 108 and 109 as of 2025-08-13, "
                "anchored to plan_2025-08-13 as the frozen source of truth. You may reference 2025-08-13 insights for context; "
                "no configuration changes are required. You deliver a compact CSV with one row per ad set containing campaign_id, "
                "adset_id, and date."
            ),
            actions=[
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
                Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
        
                Action(name="start_automation_run", kwargs={
                    "run_type": "audit_snapshot",
                    "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "adsets": ["108", "109"], "date": "2025-08-13"}
                }),
        
                Action(name="daily_adset_insights", kwargs={"adset_id": "108", "date": "2025-08-13"}),
                Action(name="daily_adset_insights", kwargs={"adset_id": "109", "date": "2025-08-13"}),
        
                # CSV: exactly one row per ad set (no extra campaign-level row)
                Action(name="export_report_csv", kwargs={
                    "rows": [
                        {"campaign_id": "6", "adset_id": "108", "date": "2025-08-13"},
                        {"campaign_id": "6", "adset_id": "109", "date": "2025-08-13"}
                    ]
                }),
        
                Action(name="end_automation_run", kwargs={
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "campaign_id": "6",
                        "adset_id_108": "108",
                        "adset_id_109": "109",
                        "ok": True
                    }
                })
            ],
            outputs=[
                '"adset_id": "108"',
                '"adset_id": "109"'
            ]
        ),

    Task(
        annotator="v3",
        user_id="task_069",
        instruction=(
            "You align 'Holiday Season Early Bird' to the frozen plan for 2025-08-13 by reaffirming the live allocations for ad sets 106 and 107 "
            "to match plan_2025-08-13. You read the live state, apply the plan's budget and bidding strategy for each. You will verify the adsets."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "5"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),

            Action(name="fetch_adset", kwargs={"adset_id": "106"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),

            Action(name="fetch_adset", kwargs={"adset_id": "107"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"budget": 500.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 18.0',
            '"adset_id": "107"',
            '"budget": 400.0',
            '"bid_strategy": "lowest_cost"',
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_070",
        instruction=(
            "You align the 'Brand - Video Ads' ad set (id 103) in 'Q3 Brand Awareness Push' to  "
            "'plan_2025-08-13' so that the aligned state reflects budget and strategy. You assess delivery on "
            "2025-08-13 against a minimum of 1,500 impressions and record any shortfall as an exception. You provide an auditable "
            "CSV capturing the exception context."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "2"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "103", "new_budget": 1200.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "103", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="raise_exceptions", kwargs={
                "plan_id": "plan_2025-08-13",
                "insights": [{"adset_id": "103", "impressions": 0, "spend": 0.0, "missing_days": 0}],
                "rules": {"zero_delivery_impressions": 1500}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "103", "alert": "zero_delivery"}],
            }),
        ],
        outputs=[
            '"campaign_id": "2"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "103"',
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_071",
        instruction=(
            "You reconcile 'App Installs - Android' ad set 110 in 'Mobile App Installs Campaign' to match plan_2025-08-13 as of 2025-08-13: "
            "set its budget and its bid strategy. You return a compact CSV receipt."
        ),

        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "110"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "110", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
                "actual_rows": [{"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "7", "adset_id": "110", "new_budget": 1000.0, "bid_strategy": "lowest_cost"}]
            })
        ],
        outputs=[
            '"campaign_id": "7"',
            '"adset_id": "110"',
            '"new_budget": 1000.0"',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_072",
        instruction=(
            "You log an audit snapshot for 'Lead Gen - Tech Webinars' on 2025-08-13 tied to plan_2025-08-13. "
            "You record weekly sales for category 'Electronics' for the week starting 2025-08-07, finalize the audit run, "
            "and produce a dated report and a CSV receipt."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Lead Gen - Tech Webinars"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="weekly_sales", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "audit_snapshot",
                "input_ref": {"plan_id": "plan_2025-08-13"}
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "status": "success",
                "outputs_json": {"status": "confirmed", "plan_id": "plan_2025-08-13"},
                "errors_json": {}
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "4",
                    "plan_id": "plan_2025-08-13",
                    "category": "Electronics",
                    "week_start": "2025-08-07"
                }],
            }),
        ],
        outputs=[
            '"campaign_id": "4"',
            '"plan_id": "plan_2025-08-13"',
            '"category": "Electronics"',
            '"week_start": "2025-08-07"',
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_073",
        instruction=(
            "You reconcile 'Holiday - Toys' (ad set 107) in 'Holiday Season Early Bird' to the frozen plan for 2025-08-13, "
            "ensuring budget and bid strategy are applied. Provide an audit snapshot anchored with start date 2025-08-10, "
            "a dated report for 2025-08-13, and a CSV artifact with fields [campaign_id, adset_id]."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="range_spend", kwargs={"adset_id": "107", "start_date": "2025-08-10", "end_date": "2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={"rows": [{"campaign_id": "5", "adset_id": "107"}]})
        ],
        outputs=[
            '"campaign_id": "5"',
            '"adset_id": "107"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_074",
        instruction=(
            "You align the 'Holiday Season Early Bird' campaign to the frozen plan for 2025-08-13. "
            "Use the plan to drive updates and confirm live alignment afterward."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "5"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "106"}),
            Action(name="fetch_adset", kwargs={"adset_id": "107"})
        ],
        outputs=['"ok": true']
    ),

    Task(
        annotator="v3",
        user_id="task_075",
        instruction=(
            "You ensure the 'Electronics - EU' ad set in 'Global Summer Sale' (adset_id '112') is aligned to the frozen plan as of 2025-08-13 "
            "identified by plan_2025-08-13: the adset state must match the plan state. You record a creative rotation for ad_id '1111' "
            "from 'image' to 'video' on 2025-08-13. "
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="fetch_adset", kwargs={"adset_id": "112"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="record_creative_rotation", kwargs={
                "ad_id": "1111",
                "from_creative": "image",
                "to_creative": "video",
                "rotation_date": "2025-08-13",
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"adset_id": "112"',
            '"ad_id": "1111"',
            '"date": "2025-08-13"'
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_076",
        instruction=(
            "You bring 'Global Summer Sale' ad set 101 into alignment with the frozen plan for 2025-08-13, "
            "capture daily health (including ROAS), and provide the CSV artifact including the campaign name 'Global Summer Sale'."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="daily_adset_insights", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="calc_roas", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [{"campaign_id": "1", "adset_id": "101", "name": "Global Summer Sale", "roas": 10.0}]
            })
        ],
        outputs=[
            '"roas": 10.0',
            '"adset_id": "101"',
            '"name": "Global Summer Sale"'
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_077",
        instruction=(
            "You update the live ad sets 101 and 102 in 'Global Summer Sale' to match the frozen plan for 2025-08-13, "
            "applying the required budget and bidding changes. You also review policy rules for currency and budget rounding, "
            "and you document the reconciliation via a CSV receipt. "
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="get_policy_rule", kwargs={"rule_name": "currency"}),
            Action(name="get_policy_rule", kwargs={"rule_name": "budget_rounding_unit"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "101"}),
            Action(name="fetch_adset", kwargs={"adset_id": "102"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0},
                    {"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "adset_id": "101"},
                    {"plan_id": "plan_2025-08-13", "adset_id": "102"}
                ]
            }),
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
        ],
    ),
        
        Task(
            annotator="v3",
            user_id="task_078",
            instruction=(
                "You stage a KPI-scored seed creative in 'Back to School Deals' ad set 108 as of 2025-08-13, anchored to plan_2025-08-13 as the frozen source of truth. "
                "You create a paused image ad named 'ad_108_seed_v1', ensure the ad set inventory reflects this single addition and remains in-policy, "
                "and you deliver a compact CSV receipt and a dated report."
            ),
            actions=[
                Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
                Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
                Action(name="daily_adset_insights", kwargs={"adset_id": "108", "date": "2025-08-13"}),
                Action(name="calc_roas", kwargs={"adset_id": "108", "date": "2025-08-13"}),
                Action(name="start_automation_run", kwargs={
                    "run_type": "seed_creative",
                    "input_ref": {"campaign_id": "6", "adset_id": "108", "name": "ad_108_seed_v1", "date": "2025-08-13"}
                }),
                Action(name="list_ads_in_adset", kwargs={"adset_id": "108"}),
                Action(name="make_ad", kwargs={"adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}),
                Action(name="list_ads_in_adset", kwargs={"adset_id": "108"}),
                Action(name="verify_applied", kwargs={
                    "expected_rows": [{"adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}],
                    "actual_rows":   [{"adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}],
                    "key_fields": ["adset_id", "name", "format", "status"]
                }),
                Action(name="export_report_csv", kwargs={
                    "rows": [{"campaign_id": "6", "adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}]
                }),
                Action(name="write_report", kwargs={"date": "2025-08-13"}),
        
                Action(name="end_automation_run", kwargs={
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                })
            ],
            outputs=[
                '"adset_id": "108"',
                '"name": "ad_108_seed_v1"',
                '"run_2025-08-13"'
            ]
        ),
        
    Task(
        annotator="v3",
        user_id="task_079",
        instruction=(
            "You record a bookkeeping automation cycle for 2025-08-13 anchored to plan_2025-08-13. "
            "Maintain an audit trail, confirm the anchor states, freeze the plan for evidence, "
            "and deliver a compact CSV receipt and a dated report titled 'bts bookkeeping cycle 2025-08-13'."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "bookkeeping",
                "input_ref": {"plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"plan_id": "plan_2025-08-13"}],
                "actual_rows": [{"plan_id": "plan_2025-08-13"}],
                "key_fields": ["plan_id"]
            }),
            Action(name="end_automation_run", kwargs={"run_id": "run_2025-08-13", "errors_json": {}}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "run_id": "run_2025-08-13"}
                ]
            }),
            Action(name="write_report", kwargs={"date": "2025-08-13", "title": "bts bookkeeping cycle 2025-08-13"})
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"run_id": "run_2025-08-13"',
            '"report_id": "rep_2025-08-13_bts-bookkeeping-cycle-2025-08-13"'
        ]
    ),
        
        Task(
            annotator="v3",
            user_id="task_080",
            instruction=(
                "You align ad set 104 in 'Fall Collection Launch' to plan_2025-08-13 ensuring budget and strategy match. "
                "You anchor to a frozen plan snapshot and deliver a compact CSV with plan_id and adset_id plus a dated report."
            ),
            actions=[
                Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
                Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
                Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
        
                Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
                Action(name="set_adset_strategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
        
                Action(name="fetch_adset", kwargs={"adset_id": "104"}),
                Action(name="verify_applied", kwargs={
                    "expected_rows": [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                    "actual_rows":   [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                    "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
                }),
        
                Action(name="export_report_csv", kwargs={
                    "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "104"}]
                }),
                Action(name="write_report", kwargs={"date": "2025-08-13"}),
            ],
            outputs=[
                '"plan_id": "plan_2025-08-13"',
                '"adset_id": "104"'
            ],
        ),

    Task(
        annotator="v3",
        user_id="task_081",
        instruction=(
            "You reconcile the 'Mobile App Installs Campaign' with the frozen plan for 2025-08-13 for adsets 110 and 111. "
            "Apply the plan to the targeted ad sets and verify the final live state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "7"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "110"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "110", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "110", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "110"}),
            Action(name="fetch_adset", kwargs={"adset_id": "111"})
        ],
        outputs=['"ok": true']
    ),

    Task(
        annotator="v3",
        user_id="task_082",
        instruction=(
            "You reaffirm plan adherence for 'Back to School Deals' on 2025-08-13 by correcting the zero-delivery ad set only. "
            "You ensure ad set 108 matches plan_2025-08-13 and you do not modify ad sets that are not allocated "
            "in the plan. You export to CSV as a receipt."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(
                name="set_adset_strategy",
                kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}
            ),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "6", "plan_id": "plan_2025-08-13", "adset_id": "108",
                    "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0
                }],
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"budget": 800.0',
            '"bid_strategy": "cost_cap"',
            '"bid_amount": 45.0'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_083",
        instruction=(
            "You confirm bidding compliance for 'Fall Collection Launch' ad set 105 on 2025-08-13 by recording strategy lowest_cost "
            "for plan_2025-08-13. You provide the CSV."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "strategy_compliance",
                "input_ref": {"campaign_id": "3", "adset_id": "105", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "3",
                        "name": "Fall Collection Launch",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "105",
                        "budget": 750.0,
                        "bid_strategy": "lowest_cost",
                    }
                ]
            }),
            Action(name="end_automation_run", kwargs={"run_id": "run_2025-08-13", "errors_json": {}})
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"budget": 750.0',
            '"bid_strategy": "lowest_cost"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_084",
        instruction=(
            "You conduct a freeze audit for the 'Back to School Deals' campaign on 2025-08-13 for ad set "
            "111. You confirm the adset is aligned with plan_2025-08-13. "
            "You document the audit in CSV and write the report."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
                "actual_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}]
            }),
            Action(name="export_report_csv", kwargs={"date": "2025-08-13",
                "rows": [{"adset_id": "111", "plan_id": "plan_2025-08-13", "tag": "freeze_audit"}]
            }),
            Action(name="write_report", kwargs={
                "date": "2025-08-13",
                "tags": ["freeze", "audit"]
            })
        ],
        outputs=[
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "111"',
        ],
    ),
                
        Task(
            annotator="v3",
            user_id="task_085",
            instruction=(
                "You start the 'Global Summer Sale' campaign on 2025-08-13 and ensure ad set 112 matches plan_2025-08-13: "
                "its bid strategy is lowest_cost. You export a compact CSV capturing the final configuration with status=active, "
                "including campaign_id, name, plan_id, adset_id, bid_strategy, and status."
            ),
            actions=[
                Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
                Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
                Action(name="start_automation_run", kwargs={
                    "run_type": "launch_alignment",
                    "input_ref": {"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "112", "date": "2025-08-13"}
                }),
                Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
                Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
                Action(name="set_adset_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
                Action(name="start_campaign", kwargs={"campaign_id": "1"}),
                Action(name="fetch_adset", kwargs={"adset_id": "112"}),
                Action(name="verify_applied", kwargs={
                    "expected_rows": [{"adset_id": "112", "bid_strategy": "lowest_cost"}],
                    "actual_rows":   [{"adset_id": "112", "bid_strategy": "lowest_cost"}],
                    "key_fields": ["adset_id", "bid_strategy"]
                }),
        
                Action(name="export_report_csv", kwargs={
                    "rows": [{
                        "campaign_id": "1",
                        "name": "Global Summer Sale",
                        "status": "active",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "112",
                        "bid_strategy": "lowest_cost"
                    }]
                }),
        
                Action(name="end_automation_run", kwargs={
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "campaign_id": "1",
                        "name": "Global Summer Sale",
                        "status": "active",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "112",
                        "bid_strategy": "lowest_cost"
                    }
                })
            ],
            outputs=[
                '"campaign_id": "1"',
                '"name": "Global Summer Sale"',
                '"status": "active"',
                '"plan_id": "plan_2025-08-13"',
                '"adset_id": "112"',
                '"bid_strategy": "lowest_cost"'
            ]
        ),
        
    Task(
        annotator="v3",
        user_id="task_086",
        instruction=(
            "You perform an alignment cycle for 'Fall Collection Launch' on 2025-08-13 focused on ad set 105. "
            "Anchor to plan_2025-08-13, align budget/strategy as needed, and export a compact CSV receipt."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "3",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "105",
                        "status": "active",
                        "bid_strategy": "lowest_cost",
                    }
                ]
            })
        ],
        outputs=[
            '"campaign_id": "3"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"bid_strategy": "lowest_cost"',
            '"status": "active"'
        ],
    ),

    Task(
        annotator="v3",
        user_id="task_087",
        instruction=(
            "You perform a maintenance toggle for 'Fall Collection Launch' on 2025-08-13 to bring ad set 104 into alignment with plan_2025-08-13. "
            "Ensure the campaign ends paused and return a compact CSV configuration receipt."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="stop_campaign", kwargs={"campaign_id": "3", "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {"campaign_id": "3", "status": "paused", "plan_id": "plan_2025-08-13",
                     "adset_id": "104", "bid_strategy": "cost_cap"}
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"status": "paused"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "104"',
            '"bid_strategy": "cost_cap"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_088",
        instruction=(
            "You reconcile the 'Holiday Season Early Bird' campaign to the frozen plan for 2025-08-13. "
            "Ensure ad set 106 is budget 500.0 with cost_cap bid 18.0, and ad set 107 is budget 400.0 with lowest_cost. "
            "Verify the results against the plan."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "5"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [
                    {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}
                ],
                "actual_rows": [
                    {"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}
                ],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"name": "Holiday Season Early Bird"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"bid_strategy": "cost_cap"',
            '"adset_id": "107"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_089",
        instruction=(
            "You align the 'Global Summer Sale' campaign to the frozen plan for 2025-08-13 for ad set 112. "
            "Ensure budget 700.0 and bid strategy lowest_cost are applied and verified."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "1"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "112"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_090",
        instruction=(
            "You align the 'Back to School Deals' campaign to the frozen plan for 2025-08-13 for ad set 111. "
            "You'll verify adset is in line with the plan and you will export a CSV recording the aligned rows."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "111", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5, "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "6",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "111",
                        "bid_strategy": "cost_cap"
                    }
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "111"',
            '"bid_strategy": "cost_cap"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_091",
        instruction=(
            "You align 'Back to School Deals' ad set 111 to frozen plan plan_2025-08-13 by applying the plan "
            "(budget=1000.0, strategy=cost_cap with bid=2.5), verifying the live state matches, recording the "
            "automation run, and exporting a compact CSV receipt with campaign_id, name, plan_id, adset_id, and bid_strategy."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "plan_execution",
                "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "adset_id": "111", "date": "2025-08-13"}
            }),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="update_adset_budget", kwargs={
                "adset_id": "111",
                "new_budget": 1000.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="set_adset_strategy", kwargs={
                "adset_id": "111",
                "bid_strategy": "cost_cap",
                "bid_amount": 2.5,
                "reason": "plan_2025-08-13"
            }),
            Action(name="fetch_adset", kwargs={"adset_id": "111"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
                "actual_rows":   [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "6",
                    "name": "Back to School Deals",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111",
                    "bid_strategy": "cost_cap"
                }]
            }),
            Action(name="end_automation_run", kwargs={"run_id": "run_2025-08-13", "errors_json": {}}),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School Deals"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "111"',
            '"bid_strategy": "cost_cap"'
        ],
    ),


    Task(
        annotator="v3",
        user_id="task_092",
        instruction=(
            "You align 'Fall Collection Launch' to the frozen plan for 2025-08-13 for both ad sets. "
            "Apply the plan values to ad set 104, confirm ad set 105 already matches the plan without changes, "
            "and verify the applied state against plan_2025-08-13."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="verify_applied", kwargs={"plan_id": "plan_2025-08-13"}),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"ok": true'
        ]
    ),Task(
    annotator="v3",
    user_id="task_093",
    instruction=(
        "You perform a KPI-scored maintenance toggle for 'Holiday Season Early Bird' as of 2025-08-13: "
        "you align ad set 106 to plan_2025-08-13 (budget 500.0 and cost_cap with bid_amount 18.0), "
        "compute ROAS on 2025-08-13 for audit, freeze the plan snapshot as evidence, pause the campaign, "
        "and provide a compact CSV with campaign_id, status, plan_id, adset_id, and bid_strategy."
    ),
    actions=[
        Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
        Action(name="daily_adset_insights", kwargs={"adset_id": "106", "date": "2025-08-13"}),
        Action(name="calc_roas", kwargs={"adset_id": "106", "date": "2025-08-13"}),
        Action(name="freeze_plan", kwargs={"date": "2025-08-13"}),
        Action(name="start_automation_run", kwargs={
            "run_type": "kpi_maintenance_toggle",
            "input_ref": {"campaign_id": "5", "adset_id": "106", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
        Action(name="update_adset_budget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
        Action(name="set_adset_strategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
        Action(name="fetch_adset", kwargs={"adset_id": "106"}),
        Action(name="verify_applied", kwargs={
            "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "actual_rows":   [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),
        Action(name="stop_campaign", kwargs={"campaign_id": "5"}),
        Action(name="export_report_csv", kwargs={
            "rows": [
                {"campaign_id": "5", "status": "paused", "plan_id": "plan_2025-08-13",
                 "adset_id": "106", "bid_strategy": "cost_cap"}
            ]
        }),
        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "campaign_id": "5",
                "status": "paused",
                "plan_id": "plan_2025-08-13",
                "adset_id": "106",
                "bid_strategy": "cost_cap"
            }
        })
    ],
    outputs=[
        '"campaign_id": "5"',
        '"status": "paused"',
        '"plan_id": "plan_2025-08-13"',
        '"adset_id": "106"',
        '"bid_strategy": "cost_cap"'
    ]
),
        
    Task(
        annotator="v3",
        user_id="task_094",
        instruction=(
            "You align 'Back to School Deals' ad set 108 to the frozen plan for 2025-08-13. "
            "Apply plan_2025-08-13 budget and bid strategy, then verify the values."
        ),
        actions=[
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School - Laptops"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"bid_strategy": "cost_cap"',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_095",
        instruction=(
            "You will update ad set 108 in 'Back to School Deals' against the plan for 2025-08-13 and verify the live state matches."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "6"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="fetch_adset", kwargs={"adset_id": "108"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
        ],
        outputs=[
            '"campaign_id": "6"',
            '"name": "Back to School Deals"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "108"',
            '"ok": true'
        ]
    ),


    Task(
        annotator="v3",
        user_id="task_096",
        instruction=(
            "You align 'Holiday Season Early Bird' to the frozen plan for 2025-08-13 for ad set 107. "
            "Apply budget 400.0 and lowest_cost with reason 'plan_2025-08-13', then verify the state."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"name": "Holiday Season Early Bird"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "107"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_097",
        instruction=(
            "You align the 'Global Summer Sale' ad set 101 to the frozen plan for 2025-08-13, "
            "updating its budget and bid strategy to match the plan. "
            "You will export a CSV as the receipt."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="export_report_csv", kwargs={
                "rows": [
                    {
                        "campaign_id": "1",
                        "name": "Global Summer Sale",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "101",
                        "bid_strategy": "cost_cap"
                    }
                ],
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"name": "Global Summer Sale"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "101"',
            '"bid_strategy": "cost_cap"',
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_098",
        instruction=(
            "You reconcile 'Fall Collection Launch' to the frozen plan for 2025-08-13 for ad set 105. "
            "Apply budget 750.0 and lowest_cost with reason 'plan_2025-08-13', and verify values match."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="list_campaign_adsets", kwargs={"campaign_id": "3"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="update_adset_budget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="set_adset_strategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
        ],
        outputs=[
            '"campaign_id": "3"',
            '"name": "Fall Collection Launch"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "105"',
            '"bid_strategy": "lowest_cost"',
            '"ok": true'
        ]
    ),

Task(
    annotator="v3",
    user_id="task_099",
    instruction=(
        "You place 'Back to School Deals' in maintenance as of 2025-08-13. "
        "You align ad set 111 to plan_2025-08-13 with budget 1000.0 and cost_cap bid_amount 2.5, "
        "pause the campaign, and deliver a compact CSV receipt with campaign_id, status, plan_id, adset_id, and bid_strategy."
    ),
    actions=[
        Action(name="lookup_campaign", kwargs={"name": "Back to School Deals"}),
        Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
        Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
        Action(name="start_automation_run", kwargs={
            "run_type": "alignment_then_pause",
            "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "adset_id": "111", "date": "2025-08-13"}
        }),
        Action(name="update_adset_budget", kwargs={
            "adset_id": "111", "new_budget": 1000.0, "reason": "plan_2025-08-13"
        }),
        Action(name="set_adset_strategy", kwargs={
            "adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5, "reason": "plan_2025-08-13"
        }),
        Action(name="verify_applied", kwargs={
            "expected_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
            "actual_rows":   [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),
        Action(name="stop_campaign", kwargs={"campaign_id": "6"}),
        Action(name="export_report_csv", kwargs={
            "rows": [{
                "campaign_id": "6",
                "status": "paused",
                "plan_id": "plan_2025-08-13",
                "adset_id": "111",
                "bid_strategy": "cost_cap"
            }]
        }),
        Action(name="end_automation_run", kwargs={
            "run_id": "run_2025-08-13",
            "errors_json": {},
            "outputs_json": {
                "campaign_id": "6",
                "status": "paused",
                "plan_id": "plan_2025-08-13",
                "adset_id": "111",
                "bid_strategy": "cost_cap"
            }
        })
    ],
    outputs=[
        '"campaign_id": "6"',
        '"status": "paused"',
        '"plan_id": "plan_2025-08-13"',
        '"adset_id": "111"',
        '"bid_strategy": "cost_cap"'
    ]
),

    Task(
        annotator="v3",
        user_id="task_100",
        instruction=(
            "You apply frozen plan plan_2025-08-13 to 'Holiday Season Early Bird' ad set 106, "
            "updating the live budget and bid strategy to match the plan (budget=500.0, "
            "strategy=cost_cap with bid=18.0). You verify the applied state, record the "
            "automation run, and export a compact CSV receipt with campaign_id, name, "
            "plan_id, adset_id, and bid_strategy."
        ),
        actions=[
            Action(name="lookup_campaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="fetch_plan_for_date", kwargs={"date": "2025-08-13"}),
            Action(name="get_adset_from_plan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="start_automation_run", kwargs={
                "run_type": "plan_execution",
                "input_ref": {"campaign_id": "5", "plan_id": "plan_2025-08-13", "adset_id": "106", "date": "2025-08-13"}
            }),
            Action(name="update_adset_budget", kwargs={
                "adset_id": "106",
                "new_budget": 500.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="set_adset_strategy", kwargs={
                "adset_id": "106",
                "bid_strategy": "cost_cap",
                "bid_amount": 18.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="fetch_adset", kwargs={"adset_id": "106"}),
            Action(name="verify_applied", kwargs={
                "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "actual_rows":   [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="end_automation_run", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {"applied": True, "adset_id": "106", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="export_report_csv", kwargs={
                "rows": [{
                    "campaign_id": "5",
                    "name": "Holiday Season Early Bird",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106",
                    "bid_strategy": "cost_cap"
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "5"',
            '"name": "Holiday Season Early Bird"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "106"',
            '"bid_strategy": "cost_cap"'
        ]
    )


]
