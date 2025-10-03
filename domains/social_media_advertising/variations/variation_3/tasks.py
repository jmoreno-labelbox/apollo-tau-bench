from domains.dto import Action, Task

TASKS =[        
        
        Task(
            annotator="v3",
            user_id="task_001",
        instruction=(
            "Adjust ad set 104 in the 'Fall Collection Launch' campaign to match the frozen plan for 2025-08-13 and verify that the budget and bid strategy are in accordance."
        ),
            actions=[
                Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
                Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
                Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
                Action(name="SetAdsetStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
                Action(name="FetchAdset", kwargs={"adset_id": "104"}),
                Action(
                    name="VerifyApplied",
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
            "Manage the daily allocation and rotation for 'Global Summer Sale' on 2025-08-13 according to policy and the frozen plan. Ensure ad sets 101 and 102 meet the plan’s budgets and strategies, implement the specified rotation for ad set 101 so that only one ad is active, log any delivery issues for the day using the available insights, and release the auditable documentation."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "allocation_rotation_daily",
                "input_ref": {"campaign_id": "1", "plan_id": "plan_2025-08-13", "date": "2025-08-13", "adsets": ["101", "102"]}
            }),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchCreativeRotation", kwargs={"adset_id": "101"}),
            Action(name="PauseOrActivateAd", kwargs={"ad_id": "1101", "status": "paused"}),
            Action(name="PauseOrActivateAd", kwargs={"ad_id": "1102", "status": "active"}),
            Action(name="VerifyApplied", kwargs={
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
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "101", "active_ads": 1}],
                "actual_rows": [{"adset_id": "101", "active_ads": 1}],
                "key_fields": ["adset_id", "active_ads"]
            }),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="RaiseExceptions", kwargs={
                "plan_id": "plan_2025-08-13",
                "insights": [],
                "rules": {"zero_delivery_impressions": 0}
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            Action(name="EndAutomationRun", kwargs={
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
            "Ensure the 'Global Summer Sale' campaign is consistent with the predefined plan for 2025-08-13. Set ad set 101 to the designated budget 950.0 and cost_cap using bid_amount 35.0, while maintaining a single-active condition where ad 1102 remains active and ad 1101 is paused. Export a concise CSV receipt of this alignment."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={
                "adset_id": "101",
                "bid_strategy": "cost_cap",
                "bid_amount": 35.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="ListAdsInAdset", kwargs={"adset_id": "101"}),
            Action(name="PauseOrActivateAd", kwargs={"ad_id": "1101", "status": "paused"}),
            Action(name="PauseOrActivateAd", kwargs={"ad_id": "1102", "status": "active"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "101", "active_ads": 1}],
                "actual_rows": [{"adset_id": "101", "active_ads": 1}],
                "key_fields": ["adset_id", "active_ads"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the frozen plan plan_2025-08-13 for 'Fall Collection Launch' scheduled on 2025-08-13 across ad sets 104 and 105. Secure the run with a checksum and the frozen plan, implementing the plan's budget and bid strategy on both ad sets. Verify the state that has been applied."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="ComputePlanChecksum", kwargs={"date": "2025-08-13"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "execution_with_audit",
                "input_ref": {"plan_id": "plan_2025-08-13", "campaign_id": "3", "adsets": ["104", "105"]}
            }),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={"plan_id": "plan_2025-08-13"}),

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
            "Handle the submission of daily insight evidence for 'Back to School Deals' ad set 108 on 2025-08-13 by retrieving insights from that specific day and affixing them to the fixed plan for that date. Supply a single-row CSV and compose a report with the appropriate date."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "insight_anchor",
                "input_ref": {"plan_id": "plan_2025-08-13", "adset_id": "108", "date": "2025-08-13"}
            }),
            Action(name="EndAutomationRun", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {}
            }),
            Action(name="ExportReportCsv", kwargs={
                "rows": [{"campaign_id": "6", "adset_id": "108", "date": "2025-08-13", "plan_id": "plan_2025-08-13"}]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
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
            "Coordinate the establishment of an Electronics snapshot on ad set 108 for 'Back to School Deals' effective 2025-08-13 by aligning with plan_2025-08-13 (budget 800.0, bid strategy cost_cap with bid 45.0), confirming the current state, and generating two items: a dated report for 2025-08-13 and a concise CSV including the fields [campaign_id, plan_id, adset_id, budget, bid_strategy, bid_amount]."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            Action(name="WriteReport", kwargs={"date": "2025-08-13"})
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
            "Handle the alignment of the 'Global Summer Sale' campaign to the frozen plan for 2025-08-13 for ad set 112. Utilize plan_2025-08-13 as the definitive guide and ensure the budget and bid strategy are implemented. Verify the revised state against the plan and produce a CSV summarizing the conclusive state."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={
                "adset_id": "112",
                "new_budget": 700.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="SetAdsetStrategy", kwargs={
                "adset_id": "112",
                "bid_strategy": "lowest_cost",
                "reason": "plan_2025-08-13"
            }),
            Action(name="VerifyApplied", kwargs={"plan_id": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Mandate the use of the plan-selected creative for 'Global Summer Sale' ad set 101 effective 2025-08-13. Ensure that ad 1102 (video) remains the only active ad in the ad set and that ad 1101 is paused, in alignment with plan_2025-08-13. Provide a concise CSV receipt containing plan_id, adset_id, activate_id, pause_id, and final_active_status."
        ),
    actions=[
        Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
        Action(name="StartAutomationRun", kwargs={
            "run_type": "creative_rotation",
            "input_ref": {"campaign_id": "1", "adset_id": "101", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),
        Action(name="SwapAdCreatives", kwargs={"activate_id": "1102", "pause_id": "1101"}),
        Action(name="ListAdsInAdset", kwargs={"adset_id": "101"}),
        Action(name="VerifyApplied", kwargs={
            "expected_rows": [{"adset_id": "101", "active_ads": 1}],
            "actual_rows": [{"adset_id": "101", "active_ads": 1}],
            "key_fields": ["adset_id", "active_ads"]
        }),
        Action(name="RecordCreativeRotation", kwargs={
            "ad_id": "1102",
            "from_creative": "image",
            "to_creative": "video",
            "rotation_date": "2025-08-13"
        }),
        Action(name="ExportReportCsv", kwargs={
            "rows": [{
                "plan_id": "plan_2025-08-13",
                "adset_id": "101",
                "activate_id": "1102",
                "pause_id": "1101",
                "final_active_status": "active"
            }]
        }),
        Action(name="EndAutomationRun", kwargs={
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
            "Coordinate the alignment of the 'Holiday Season Early Bird' ad set 106 with plan_2025-08-13 as of 2025-08-13—ensure a budget of 500.0 and a cost_cap at 18.0—then generate a concise CSV containing plan_id, campaign_id, adset_id, and checksum=a1b2c3d4e5f6 along with a dated markdown report."
        ),
    actions=[
        Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
        Action(name="ListCampaignAdsets", kwargs={"campaign_id": "5"}),
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),

        Action(name="StartAutomationRun", kwargs={
            "run_type": "inventory_snapshot",
            "input_ref": {"campaign_id": "5", "adset_id": "106", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),

        # Required writes to satisfy the criterion:
        Action(name="UpdateAdsetBudget", kwargs={
            "adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"
        }),
        Action(name="SetAdsetStrategy", kwargs={
            "adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"
        }),

        # Verify alignment on budget/strategy:
        Action(name="FetchAdset", kwargs={"adset_id": "106"}),
        Action(name="VerifyApplied", kwargs={
            "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "actual_rows":   [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),

        # Deterministic checksum + freeze (evidence):
        Action(name="ComputePlanChecksum", kwargs={"date": "2025-08-13"}),
        Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),

        # Receipts:
        Action(name="ExportReportCsv", kwargs={
            "rows": [{"plan_id": "plan_2025-08-13", "campaign_id": "5", "adset_id": "106", "checksum": "a1b2c3d4e5f6"}]
        }),
        Action(name="WriteReport", kwargs={
            "date": "2025-08-13",
            "title": "Inventory Snapshot 2025-08-13 - plan_2025-08-13",
            "tags": ["inventory", "snapshot", "plan_2025-08-13"]
        }),
        Action(name="EndAutomationRun", kwargs={
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
            "Implement the plan-selected creative type for 'Global Summer Sale' ad set 101 starting 2025-08-13. Use the frozen plan for 2025-08-13 to ensure the accuracy of the required creative_type. Maintain exactly one active ad in the ad set with the creative_type aligning with the plan. Produce an auditable run and deliver a concise CSV receipt including plan_id, adset_id, active_ad_id, and active_creative_type."
        ),
    actions=[
        Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
        Action(name="ListAdsInAdset", kwargs={"adset_id": "101"}),
        Action(name="StartAutomationRun", kwargs={
            "run_type": "creative_rotation",
            "input_ref": {"campaign_id": "1", "adset_id": "101", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),
        Action(name="SwapAdCreatives", kwargs={"activate_id": "1102", "pause_id": "1101"}),
        Action(name="ListAdsInAdset", kwargs={"adset_id": "101"}),
        Action(name="VerifyApplied", kwargs={
            "expected_rows": [{"adset_id": "101", "active_ads": 1, "active_creative_type": "video"}],
            "actual_rows": [{"adset_id": "101", "active_ads": 1, "active_creative_type": "video"}],
            "key_fields": ["adset_id", "active_ads", "active_creative_type"]
        }),
        Action(name="ExportReportCsv", kwargs={
            "rows": [{
                "plan_id": "plan_2025-08-13",
                "adset_id": "101",
                "active_ad_id": "1102",
                "active_creative_type": "video"
            }]
        }),
        Action(name="EndAutomationRun", kwargs={
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
            "Handle the alignment of the 'Global Summer Sale' campaign with the frozen plan for 2025-08-13 for ad set 101. Utilize plan_2025-08-13, ensuring that budget and bid are applied, and document all updates. Subsequently, confirm that the ad set accurately reflects the planned budget and bid strategy."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the alignment of the 'Fall Collection Launch' campaign with the frozen plan for 2025-08-13 for ad set 104. Make use of plan_2025-08-13, making sure the budget and bid are applied and all updates are recorded. Retrieve the ad set to verify the update is complete."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "104"}),
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
            "Handle the compliance confirmation for the 'Fall Collection Launch' campaign against the frozen plan for 2025-08-13 concerning ad set 105. Ensure the use of plan_id 'plan_2025-08-13' and verify that a budget of 750.0 with bid strategy lowest_cost is applied. Export a CSV with the final configuration."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Coordinate bringing ad set 106 in 'Holiday Season Early Bird' into alignment with plan_2025-08-13 and ensure the applied state matches the plan."
        ),
        actions=[
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Ensure the 'Holiday Season Early Bird' campaign is consistent with the frozen plan for 2025-08-13 for ad set 107. Utilize plan_2025-08-13 and make certain that the budget and bid strategy are implemented. Export a CSV that summarizes the final state."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Apply the budget rounding policy on 2025-08-13 for the Global Summer Sale campaign. Verify the policy rule named 'budget_rounding_unit' and coordinate ad sets to 'plan_2025-08-13': ad set 101 and ad set 112 budget, strategy, and bid according to plan guidelines. Confirm the final states correspond to the plan values."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetPolicyRule", kwargs={"rule_name": "budget_rounding_unit"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "112"}),

            Action(name="VerifyApplied", kwargs={
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
            "Handle a maintenance toggle for the 'Global Summer Sale' campaign on 2025-08-13. Briefly activate the campaign, confirm that ad set 102 aligns with the plan_2025-08-13 budget and bid strategy, then pause the campaign once more. Generate an auditable record and a CSV with the final configuration."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "maintenance_toggle",
                "input_ref": {"campaign_id": "1", "adset_id": "102", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="StartCampaign", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="StopCampaign", kwargs={"campaign_id": "1"}),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
                "rows": [
                    {"campaign_id": "1", "status": "paused", "plan_id": "plan_2025-08-13", "adset_id": "102", "budget": 600.0,
                     "bid_strategy": "lowest_cost"}
                ]
            }),
            Action(name="EndAutomationRun", kwargs={"run_id": "run_2025-08-13", "errors_json": {}})
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
            "Coordinate a review of the 'Fall Collection Launch' campaign on 2025-08-13 for adset 104. Verify that the ad budget, bid strategy, and bid are updated to match plan_2025-08-13. Draft a report and export a CSV."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "104"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                "actual_rows": [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle a post-pause compliance review for the 'Back to School Deals' campaign adset 108 on 2025-08-13, referencing the frozen source of truth plan_2025-08-13. Implement the necessary updates from the plan with the campaign reverting to a paused status following the review."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
            Action(name="StopCampaign", kwargs={"campaign_id": "6", "reason": "plan_2025-08-13"}),
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
            "Coordinate the alignment of the 'Holiday Season Early Bird' ad set 107 with plan_2025-08-13 as of 2025-08-13: Evaluate the ad set’s performance on 2025-08-13 and verify that the final state aligns with those metrics."
        ),
            actions=[
                Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
                Action(name="DailyAdsetInsights", kwargs={"adset_id": "107", "date": "2025-08-13"}),
                Action(name="CalcRoas", kwargs={"adset_id": "107", "date": "2025-08-13"}),
                Action(name="UpdateAdsetBudget", kwargs={
                    "adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"
                }),
                Action(name="SetAdsetStrategy", kwargs={
                    "adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"
                }),
                Action(name="FetchAdset", kwargs={"adset_id": "107"}),
                Action(name="VerifyApplied", kwargs={
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
            "Handle the application of the frozen plan plan_2025-08-13 to ad set 102 in 'Global Summer Sale', ensuring the budget and strategy align perfectly with the plan. Confirm the modifications and generate a compact CSV receipt including campaign_id, name, plan_id, adset_id, budget, bid_strategy, and ok."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "plan_execution",
                "input_ref": {"campaign_id": "1", "adset_id": "102", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="UpdateAdsetBudget", kwargs={
                "adset_id": "102",
                "new_budget": 600.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="EndAutomationRun", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {"applied": True, "adset_id": "102", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Coordinate the update of the live ad set 102 in 'Global Summer Sale' to align with the frozen plan for 2025-08-13. Apply the budget and bidding strategy as per plan_2025-08-13, and verify the live status."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="VerifyApplied", kwargs={
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
            "You handle a cross-campaign coordination on 2025-08-13, updating Global Summer Sale ad set 101 and ensuring Holiday Season Early Bird ad set 106 is aligned with plan_2025-08-13. You check that both ad sets are synchronized."
        ),
    actions=[
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
        Action(name="FetchAdset", kwargs={"adset_id": "101"}),
        Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
        Action(name="SetAdsetStrategy", kwargs={
            "adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"
        }),
        Action(name="FetchAdset", kwargs={"adset_id": "101"}),
        Action(name="FetchAdset", kwargs={"adset_id": "106"}),
        Action(name="VerifyApplied", kwargs={
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
            "You complete compliance for 'Back to School Deals' on 2025-08-13. Leveraging plan_id 'plan_2025-08-13', you make certain ad set 108 conforms with its budget and bid strategy. You verify the condition, compile a report with tags ['compliance','bts'] and generate a CSV file."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
                "tags": ["compliance", "bts"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "You align the 'Holiday Season Early Bird' campaign with the frozen plan dated 2025-08-13 for ad set 107. Utilize plan_2025-08-13 and make sure to apply the budget and bid, documenting all updates. Retrieve the ad set to verify the update."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "107"}),
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
            "Implement the frozen plan for 'Back to School Deals' on 2025-08-13 (plan_id 'plan_2025-08-13'). Ensure ad sets 107 and 108 align with the states for that date and confirm the updates."
        ),
            actions=[
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
        
                # Budgets first (ascending adset_id)
                Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
                Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
        
                # Then strategies (ascending adset_id)
                Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
                Action(name="SetAdsetStrategy", kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
        
                Action(name="VerifyApplied", kwargs={
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
            "You sustain an auditable health snapshot for 'Back to School Deals' on 2025-08-13 rooted in the frozen plan. Ensure the health snapshot run is finalized and export a CSV receipt with columns: campaign_id, plan_id, run_id."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="FreezePlan", kwargs={"plan_id": "plan_2025-08-13", "date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "health_snapshot",
                "input_ref": {"plan_id": "plan_2025-08-13"}
            }),
            Action(name="EndAutomationRun", kwargs={
                "run_id": "run_2025-08-13",
                "outputs_json": {"plan_id": "plan_2025-08-13"},
                "errors_json": {}
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "You balance ad set 102 for the 'Global Summer Sale' campaign to the frozen plan for 2025-08-13, confirm the final state, and generate a one-row CSV receipt containing: campaign_id, plan_id, adset_id, adset_name, budget, bid_strategy."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "102", "daily_budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "daily_budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "daily_budget", "bid_strategy"]
            }),
            Action(name="ExportReportCsv", kwargs={
                "rows": [{
                    "campaign_id": "1",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102",
                    "adset_name": "Apparel - CA",
                    "budget": 600.0,
                    "bid_strategy": "lowest_cost"
                }]
            }),
        ],
        outputs=[
            '"campaign_id": "1"',
            '"plan_id": "plan_2025-08-13"',
            '"adset_id": "102"',
            '"adset_name": "Apparel - CA"',
            '"budget": 600.0"',
            '"bid_strategy": "lowest_cost"',
        ]
    ),


    Task(
        annotator="v3",
        user_id="task_029",
        instruction=(
            "Handle the re-affirmation of 'Holiday Season Early Bird' ad set 106 to plan_id 'plan_2025-08-13' on 2025-08-13, ensuring both budget and bid are enforced. Next, verify the state applied."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the safeguarding of plan integrity for 'Global Summer Sale' on 2025-08-13 with plan_2025-08-13. Record evidence of integrity, freeze the plan, and compile a report with tags ['integrity','gss'], along with a CSV indicating plan_id and plan status."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="ComputePlanChecksum", kwargs={"date": "2025-08-13"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
                "tags": ["integrity", "gss"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle a quick apply-and-fetch for 'Back to School Deals' ad set 108 on 2025-08-13. Ensure the ad set aligns with the plan 'plan_2025-08-13', and then retrieve the ad set."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
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
            "Verify compliance on 'Global Summer Sale' ad set 101 for 2025-08-13. Align adset 101 according to plan_id 'plan_2025-08-13' and generate a CSV export."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the reconciliation of ad set 101 in 'Global Summer Sale' against the frozen plan for 2025-08-13 as the authoritative reference. Ensure that the plan's configuration is adhered to and confirm that the state applied corresponds with the plan; maintain a concise CSV summary."
        ),
        actions=[
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={
                "adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"
            }),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Make sure that in the 'Back to School Deals' campaign, ad set 108 aligns with the frozen plan dated 2025-08-13 identified by plan_2025-08-13. Implement necessary adjustments to meet alignment and then verify the completion of these changes."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Handle a minimal plan compliance approval for 'Fall Collection Launch' ad set 105 on 2025-08-13. Establish the budget and strategy according to plan_2025-08-13, afterward, verify with a CSV of the final state."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={
                "adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "105"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Confirm the complete alignment for 'Global Summer Sale' on 2025-08-13. Employ plan_2025-08-13 as the authoritative reference, guaranteeing that ad sets 101 and 112 conform to plan strategies. Compile the alignment into a report with tags ['alignment','gss'] and export to a CSV showing the aligned rows."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "112"}),
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
                "tags": ["alignment", "gss"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the reconciliation of the 'Fall Collection Launch' campaign to the frozen plan for 2025-08-13 for adsets 104 and 105. Implement the plan on the specified ad sets and verify the outcome."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the alignment of the 'Global Summer Sale' campaign on 2025-08-13 to the frozen source of truth plan_2025-08-13 for ad set 101. If necessary, apply the plan’s budget and bid strategy, confirm the alignment status, compose a dated note, and produce an abbreviated CSV receipt."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Coordinate a plan-scored alignment for 'Holiday Season Early Bird' ad set 107 as of 2025-08-13: adjust its budget to 400.0 and its bid strategy to lowest_cost as precisely recorded in plan_2025-08-13. Evaluate the 2025-08-13 performance for audit, preserve the plan snapshot as evidence, and furnish a compact CSV containing campaign_id, name, plan_id, adset_id, budget, and bid_strategy."
        ),
    actions=[
        Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),

        # Score delivery for the date (domain proposal: KPI-driven/scored)
        Action(name="DailyAdsetInsights", kwargs={"adset_id": "107", "date": "2025-08-13"}),
        Action(name="CalcRoas", kwargs={"adset_id": "107", "date": "2025-08-13"}),

        # Evidence of plan state
        Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),

        # Auditable run boundary
        Action(name="StartAutomationRun", kwargs={
            "run_type": "plan_apply_scored",
            "input_ref": {"campaign_id": "5", "adset_id": "107", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),

        # Deterministic writes from the plan
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
        Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
        Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

        # Verify final state
        Action(name="FetchAdset", kwargs={"adset_id": "107"}),
        Action(name="VerifyApplied", kwargs={
            "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
            "actual_rows":   [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),

        # Receipt
        Action(name="ExportReportCsv", kwargs={
            "rows": [{
                "campaign_id": "5",
                "name": "Holiday Season Early Bird",
                "plan_id": "plan_2025-08-13",
                "adset_id": "107",
                "budget": 400.0,
                "bid_strategy": "lowest_cost"
            }]
        }),

        Action(name="EndAutomationRun", kwargs={
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
            "Align the 'Fall Collection Launch' campaign with the frozen plan for 2025-08-13. Utilize plan_id 'plan_2025-08-13' as the definitive source: for ad sets 104 and 105, configure budget and bid strategy; Retrieve both ad sets to verify alignment."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "105"}),
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
            "Handle the completion of the configuration for the 'Fall Collection Launch' ad set 105 under plan_2025-08-13. Verify that its bid strategy remains lowest_cost and the budget is set at 750.0; then provide a compact CSV and a dated report."
        ),
            actions=[
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
                Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
        
                Action(name="StartAutomationRun", kwargs={
                    "run_type": "alignment",
                    "input_ref": {"adset_id": "105", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
                }),
                Action(name="SetAdsetStrategy", kwargs={
                    "adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"
                }),
                Action(name="WriteReport", kwargs={"date": "2025-08-13", "tags": ["105"]}),
                Action(name="FetchAdset", kwargs={"adset_id": "105"}),
                Action(name="VerifyApplied", kwargs={
                    "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                    "actual_rows":   [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                    "key_fields": ["adset_id", "budget", "bid_strategy"]
                }),
                Action(name="ExportReportCsv", kwargs={
                    "rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}]
                }),
                Action(name="EndAutomationRun", kwargs={
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
            "Coordinate reconciliation of ad set 102 in 'Global Summer Sale' with the frozen plan dated 2025-08-13 as the authoritative reference. Ensure the configuration applied corresponds with the plan and maintain a compact CSV summary."
        ),
        actions=[
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "102", "budget": 600.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the evaluation of delivery for 'Fall Collection Launch' scheduled on 2025-08-13 for ad set 104, calculate ROAS using insights from the same day, then coordinate aligning the ad set with plan_2025-08-13 and ensure the aligned end state matches the plan."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="CalcRoas", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={"plan_id": "plan_2025-08-13"}),
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
            "Carry out the reconciliation of ad sets 104 and 105 in 'Fall Collection Launch' using the frozen plan dated 2025-08-13 as the authoritative reference. Verify that the applied states are consistent with the plan for 104 (budget 750.0, cost_cap with bid 22.0) and 105 (budget 750.0, lowest_cost). Create a compact CSV summary and a dated note."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

            Action(name="VerifyApplied", kwargs={
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

            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),

            Action(name="ExportReportCsv", kwargs={
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
            "Handle the evaluation of delivery for 'Fall Collection Launch' on 2025-08-13 concerning ad set 105, calculate ROAS from insights of the same day, subsequently coordinate the alignment of the ad set with plan_2025-08-13, and finally verify the end state is aligned with the plan."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="CalcRoas", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={"plan_id": "plan_2025-08-13"}),
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
            "Coordinate the alignment of Holiday Season Early Bird ad set 106 to the frozen plan dated 2025-08-13. Implement a budget of 500.0 and use the bid strategy cost_cap, setting the bid_amount to 18.0 as per plan_id 'plan_2025-08-13', then ensure the applied state's confirmation."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "106"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the 'Fall Collection Launch' campaign on 2025-08-13 to align with the frozen plan plan_2025-08-13 by making sure ad set 105's budget and bid strategy are consistent with the plan. Verify the alignment in a dated report and export a CSV showing the finalized values."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Conduct an exception audit for 'Global Summer Sale' dated 2025-08-13 against plan_2025-08-13. Utilizing rules zero_delivery_impressions=0, cap_hit_spend=1000.0, and data_gap_days=2, document exceptions in the system based on the provided insights—101(impressions=1200, spend=480.0, missing_days=0) and 102(impressions=0, spend=0.0, missing_days=2). Generate two outputs: a CSV listing the triggered alerts for adset_id 102 (zero_delivery and data_gap), and a dated report with tags ['gss','exceptions']."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="RaiseExceptions", kwargs={
                "plan_id": "plan_2025-08-13",
                "insights": [
                    {"adset_id": "101", "impressions": 1200, "spend": 480.0, "missing_days": 0},
                    {"adset_id": "102", "impressions": 0, "spend": 0.0, "missing_days": 2}
                ],
                "rules": {"zero_delivery_impressions": 0, "cap_hit_spend": 1000.0, "data_gap_days": 2}
            }),
            Action(name="ExportReportCsv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "adset_id": "102", "alert": "zero_delivery"},
                    {"plan_id": "plan_2025-08-13", "adset_id": "102", "alert": "data_gap"}
                ],
            }),
            Action(name="WriteReport", kwargs={
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
            "Coordinate the creation of an auditable rolling range view for 'Global Summer Sale' spanning 2025-08-10 to 2025-08-13, linked to the 2025-08-13 state of record. Preserve evidence by maintaining the 2025-08-13 plan unchanged. Ensure to list the campaign’s expenditure over that period and include the aggregate spend value in the CSV. Offer a dated report along with a CSV that lists one entry for campaign_id '1' within the specified range using the metric 'spend'."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "rolling_range_view",
                "input_ref": {"campaign_id": "1", "range": "2025-08-10..2025-08-13", "anchor_date": "2025-08-13"}
            }),
            Action(name="RangeSpend", kwargs={"campaign_id": "1", "start_date": "2025-08-10", "end_date": "2025-08-13"}),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
                "rows": [
                    {"campaign_id": "1", "metric": "spend", "range": "2025-08-10..2025-08-13", "total_spend": 0.0}
                ]
            }),
            Action(name="EndAutomationRun", kwargs={"run_id": "run_2025-08-13", "errors_json": {}})
        ],
        outputs=[
            '"campaign_id": "1"'
        ]
    ),

    Task(
        annotator="v3",
        user_id="task_050",
        instruction=(
            "Organize the alignment of 'Holiday Season Early Bird' ad set 107 to plan_2025-08-13 as of 2025-08-13: adjust its budget to 400.0 and its bid strategy to lowest_cost. Submit a succinct task output containing plan_id, adset_id, budget, and bid_strategy."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "107"})
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
            "Coordinate the 'Back to School Deals' campaign with the frozen plan for 2025-08-13. Using plan_id 'plan_2025-08-13' as the authoritative source, ensure ad set 108 reflects budget 800.0 and cost_cap with bid 45.0. Confirm that the configuration aligns with the plan."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),

            Action(name="VerifyApplied", kwargs={
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
            "Ensure the 'Holiday Season Early Bird' campaign is in line with the frozen plan for 2025-08-13. Verify ad sets 106 and 107 correspond to the plan's budget and bid strategy, and confirm the applied values."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "107"}),
            Action(name="VerifyApplied", kwargs={
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
            "Handle the reconciliation of 'Global Summer Sale' to the frozen plan for 2025-08-13 for ad set 102. Ensure both the budget and bid strategy are applied and verified."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the alignment of 'Global Summer Sale' ad set 101 to the 2025-08-13 reference plan plan_2025-08-13. The target state is set to budget 950.0 and bid strategy cost_cap with bid_amount 35.0. Success is measured by the live configuration matching that target and generating auditable evidence. Deliverables include a dated note tagged ['alignment'] and a CSV with a single receipt row containing plan_id, adset_id, budget, bid_strategy, and bid_amount."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="ExportReportCsv", kwargs={
                "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}]
            }),
            Action(name="WriteReport", kwargs={
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
            "Initiate an automation run on 2025-08-13 to reconcile 'Global Summer Sale' ad sets 101 and 102 with plan_2025-08-13, and subsequently complete the run."
        ),
    actions=[
        Action(name="StartAutomationRun", kwargs={
            "run_type": "reconcile",
            "input_ref": {"plan_id": "plan_2025-08-13", "adsets": ["101", "102"]}
        }),
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
        Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
        Action(
            name="SetAdsetStrategy",
            kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}
        ),
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
        Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
        Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
        Action(name="EndAutomationRun", kwargs={
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
            "Confirm the 'Back to School Deals' ad set 107 against the frozen plan from 2025-08-13, ensure the verification by freezing the plan, and compile a report with the tag ['bts']."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="WriteReport", kwargs={
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
            "Handle the reconciliation of the ‘Global Summer Sale’ campaign with the frozen plan for 2025-08-13, making sure ad sets 101, 102, and 112 adhere to the specified budgets and bid strategies from plan_id ‘plan_2025-08-13’. Verify that the final ad set statuses align with the plan values."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "112"}),
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
            "Coordinate the reconciliation of the 'Global Summer Sale' campaign against the frozen plan for 2025-08-13. Ensure that ad sets 101 and 102 are in line with plan_2025-08-13, and verify that the final budgets and bid strategies are consistent. Produce a report dated 2025-08-13 with tags ['apply','verification','gss']. Export a CSV summarizing the aligned rows as well."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="VerifyApplied", kwargs={
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
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
                "tags": ["apply", "verification", "gss"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the staging of ad set 112 in 'Fall Collection Launch' for QA starting 2025-08-13 by ensuring it aligns precisely with plan_2025-08-13. Once the adjustments have been made, confirm that the implemented state matches the plan."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the creation of an insights snapshot for 'Back to School Deals' ad set 107 as of 2025-08-13, using plan_2025-08-13 as the definitive source. Maintain auditability (including plan evidence and snapshot context) and provide a succinct CSV that includes campaign_id, adset_id, date, and plan_id, along with a dated report."
        ),

        actions=[
            Action(name="StartAutomationRun", kwargs={
                "run_type": "snapshot",
                "input_ref": {"campaign": "Back to School Deals", "adset_id": "107", "date": "2025-08-13"}
            }),
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
                "rows": [{"campaign_id": "6", "adset_id": "107", "date": "2025-08-13", "plan_id": "plan_2025-08-13"}]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="EndAutomationRun", kwargs={
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
            "Handle generating two spend-window summaries for 'Global Summer Sale' ad set 101 for the periods 2025-08-10..2025-08-11 and 2025-08-12..2025-08-13, associate them with the 2025-08-13 plan state using a frozen snapshot, and provide a CSV artifact labeled ['spend','windows','gss'] along with a dated report."
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={
                "run_type": "window_spend_snapshot",
                "input_ref": {"campaign": "Global Summer Sale", "adset_id": "101", "snapshot_date": "2025-08-13"}
            }),
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="RangeSpend", kwargs={"adset_id": "101", "start_date": "2025-08-10", "end_date": "2025-08-11"}),
            Action(name="RangeSpend", kwargs={"adset_id": "101", "start_date": "2025-08-12", "end_date": "2025-08-13"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
                "rows": [
                    {"adset_id": "101", "range": "2025-08-10..2025-08-11", "plan_id": "plan_2025-08-13"},
                    {"adset_id": "101", "range": "2025-08-12..2025-08-13", "plan_id": "plan_2025-08-13"}
                ]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13", "tags": ["spend", "windows", "gss"]}),
            Action(name="EndAutomationRun", kwargs={"run_id": "run_2025-08-13", "errors_json": {}}),
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
            "Ensure and finalize the plan for 'Back to School Deals' on 2025-08-13 by validating integrity with a checksum, maintaining the frozen snapshot for audit purposes, and generating a one-row CSV as a receipt of the verification."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "plan_verification",
                "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="ComputePlanChecksum", kwargs={"date": "2025-08-13"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"plan_id": "plan_2025-08-13"}],
                "actual_rows":   [{"plan_id": "plan_2025-08-13"}],
                "key_fields": ["plan_id"]
            }),
            Action(name="EndAutomationRun", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {"verification": "ok", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the 'Fall Collection Launch' campaign to ensure it aligns with the frozen plan for 2025-08-13. Verify that ad sets 104 and 105 conform to plan_2025-08-13, making sure the budget and bid strategy values are consistent with the plan. Prepare a report dated 2025-08-13 with tags ['compliance','fall']. Additionally, export a CSV that lists the compliant ad sets."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),

            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "104"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "105"}),
            Action(name="VerifyApplied", kwargs={
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
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
                "tags": ["compliance", "fall"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Conduct an audit of 'Back to School Deals' ad set 108 as of 2025-08-13 in relation to plan_2025-08-13. Document the audit results as structured rule exceptions associated with plan_2025-08-13, and preserve the plan snapshot as evidence. Provide a one-row compact CSV containing the plan_id and adset_id, and compose a dated report tagged ['rules','audit','bts']."
        ),
            actions=[
                Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
                Action(name="FetchAdset", kwargs={"adset_id": "108"}),
                Action(name="RaiseExceptions", kwargs={
                    "date": "2025-08-13",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108",
                    "rules": {"policy_check": "audit"}
                }),
                Action(name="ExportReportCsv", kwargs={
                    "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "108"}]
                }),
                Action(name="WriteReport", kwargs={
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
            "Handle the planned creative rotation for 'Global Summer Sale' ad set 101 effective 2025-08-13: ensure ad 1102 (video) is the only ad running and pause ad 1101 (image), precisely as outlined in plan_2025-08-13. You may consult the 2025-08-13 insights for context only; they do not alter the rotation. Prepare a concise CSV that includes campaign_id, adset_id, activate_id, pause_id, and date."
        ),
            actions=[
                Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
                Action(name="DailyAdsetInsights", kwargs={"adset_id": "101", "date": "2025-08-13"}),
        
                Action(name="StartAutomationRun", kwargs={
                    "run_type": "creative_rotation",
                    "input_ref": {"campaign_id": "1", "adset_id": "101", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
                }),
        
                Action(name="RecordCreativeRotation", kwargs={
                    "ad_id": "1102",
                    "from_creative": "image",
                    "to_creative": "video",
                    "rotation_date": "2025-08-13"
                }),
                Action(name="SwapAdCreatives", kwargs={"activate_id": "1102", "pause_id": "1101"}),
        
                Action(name="ListAdsInAdset", kwargs={"adset_id": "101"}),
                Action(name="VerifyApplied", kwargs={
                    "expected_rows": [{"adset_id": "101", "active_ads": 1}],
                    "actual_rows":   [{"adset_id": "101", "active_ads": 1}],
                    "key_fields": ["adset_id", "active_ads"]
                }),
        
                Action(name="ExportReportCsv", kwargs={
                    "rows": [{
                        "campaign_id": "1",
                        "adset_id": "101",
                        "activate_id": "1102",
                        "pause_id": "1101",
                        "date": "2025-08-13"
                    }]
                }),
                Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
                Action(name="EndAutomationRun", kwargs={
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
            "Coordinate the reconciliation of adset 101 in 'Global Summer Sale' to align with the static plan for 2025-08-13, checking the applied budget and bid strategy. Keep a verifiable record with a dated report and document the reconciliation with a CSV artifact."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "actual_rows": [{"adset_id": "101", "budget": 950.0, "bid_strategy": "cost_cap", "bid_amount": 35.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Address the reconciliation of 'Fall Collection Launch', ensuring 'Fall Fashion - Women' and 'Fall Fashion - Men' are aligned with the fixed plan for 2025-08-13, and provide an audit record in CSV format."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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

            Action(name="ExportReportCsv", kwargs={
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
            "Put together a same-day audit overview for 'Back to School Deals' ad sets 108 and 109 as they stand on 2025-08-13, based on plan_2025-08-13 as the definitive reference. For context, you may refer to insights from 2025-08-13; no configuration modifications are needed. Present a concise CSV featuring one line per ad set, including campaign_id, adset_id, and date."
        ),
            actions=[
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
                Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
        
                Action(name="StartAutomationRun", kwargs={
                    "run_type": "audit_snapshot",
                    "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "adsets": ["108", "109"], "date": "2025-08-13"}
                }),
        
                Action(name="DailyAdsetInsights", kwargs={"adset_id": "108", "date": "2025-08-13"}),
                Action(name="DailyAdsetInsights", kwargs={"adset_id": "109", "date": "2025-08-13"}),
        
                # CSV: exactly one row per ad set (no extra campaign-level row)
                Action(name="ExportReportCsv", kwargs={
                    "rows": [
                        {"campaign_id": "6", "adset_id": "108", "date": "2025-08-13"},
                        {"campaign_id": "6", "adset_id": "109", "date": "2025-08-13"}
                    ]
                }),
        
                Action(name="EndAutomationRun", kwargs={
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
            "Handle the alignment of 'Holiday Season Early Bird' to the frozen plan for 2025-08-13 by reaffirming the live allocations for ad sets 106 and 107 so they correspond with plan_2025-08-13. Read the current live state, and apply the plan's budget and bidding strategy for each. Verify the adsets."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "5"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),

            Action(name="FetchAdset", kwargs={"adset_id": "106"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),

            Action(name="FetchAdset", kwargs={"adset_id": "107"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),

            Action(name="VerifyApplied", kwargs={
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
            "Coordinate aligning the 'Brand - Video Ads' ad set (id 103) in 'Q3 Brand Awareness Push' with 'plan_2025-08-13' to ensure the aligned state accurately reflects the budget and strategy. Evaluate delivery on 2025-08-13 against a required minimum of 1,500 impressions and document any shortfall as an exception. Produce an auditable CSV that includes the context of any exceptions."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Q3 Brand Awareness Push"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "2"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "103", "new_budget": 1200.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "103", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="RaiseExceptions", kwargs={
                "plan_id": "plan_2025-08-13",
                "insights": [{"adset_id": "103", "impressions": 0, "spend": 0.0, "missing_days": 0}],
                "rules": {"zero_delivery_impressions": 1500}
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle the 'App Installs - Android' ad set 110 in 'Mobile App Installs Campaign' to align with plan_2025-08-13 as of 2025-08-13: ensure its budget and bid strategy are set. Provide a concise CSV receipt."
        ),

        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "110"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "110", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
                "actual_rows": [{"adset_id": "110", "budget": 1000.0, "bid_strategy": "lowest_cost", "bid_amount": None}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Conduct an audit snapshot for 'Lead Gen - Tech Webinars' on 2025-08-13 linked to plan_2025-08-13. Document weekly sales for category 'Electronics' for the week beginning 2025-08-07, complete the audit process, and generate a dated report along with a CSV receipt."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Lead Gen - Tech Webinars"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="WeeklySales", kwargs={"category": "Electronics", "start_date": "2025-08-07"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "audit_snapshot",
                "input_ref": {"plan_id": "plan_2025-08-13"}
            }),
            Action(name="EndAutomationRun", kwargs={
                "run_id": "run_2025-08-13",
                "status": "success",
                "outputs_json": {"status": "confirmed", "plan_id": "plan_2025-08-13"},
                "errors_json": {}
            }),
            Action(name="WriteReport", kwargs={
                "date": "2025-08-13",
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Align 'Holiday - Toys' (ad set 107) within 'Holiday Season Early Bird' to match the frozen plan for 2025-08-13, applying both budget and bid strategy. Supply an audit snapshot anchoring at start date 2025-08-10, a dated report for 2025-08-13, and generate a CSV file with fields [campaign_id, adset_id]."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="RangeSpend", kwargs={"adset_id": "107", "start_date": "2025-08-10", "end_date": "2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "107", "budget": 400.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={"rows": [{"campaign_id": "5", "adset_id": "107"}]})
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
            "Coordinate the 'Holiday Season Early Bird' campaign with the frozen plan for 2025-08-13. Utilize the plan to guide updates and verify live alignment subsequently."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "5"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "106"}),
            Action(name="FetchAdset", kwargs={"adset_id": "107"})
        ],
        outputs=['"ok": true']
    ),

    Task(
        annotator="v3",
        user_id="task_075",
        instruction=(
            "Handle the 'Electronics - UK' ad set in 'Global Summer Sale' (adset_id '112') to ensure it matches the frozen plan as of 2025-08-13 identified by plan_2025-08-13: the adset state should correspond with the plan state. Coordinate a creative rotation for ad_id '1111' from 'image' to 'video' on 2025-08-13."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="FetchAdset", kwargs={"adset_id": "112"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "112", "budget": 700.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="RecordCreativeRotation", kwargs={
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
            "Coordinate the alignment of the 'Global Summer Sale' ad set 101 with the frozen plan for 2025-08-13, document daily health metrics (including ROAS), and prepare the CSV artifact containing the campaign name 'Global Summer Sale'."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="DailyAdsetInsights", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="CalcRoas", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle updates for live ad sets 101 and 102 within 'Global Summer Sale' to align with the frozen plan for 2025-08-13, incorporating necessary budget and bid modifications. Additionally, review policy guidelines concerning currency and budget rounding, and document the reconciliation process with a CSV receipt."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="GetPolicyRule", kwargs={"rule_name": "currency"}),
            Action(name="GetPolicyRule", kwargs={"rule_name": "budget_rounding_unit"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "102"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "102", "new_budget": 600.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "102", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "101"}),
            Action(name="FetchAdset", kwargs={"adset_id": "102"}),
            Action(name="VerifyApplied", kwargs={
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
            Action(name="ExportReportCsv", kwargs={
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
            "Coordinate the staging of a KPI-scored seed creative in 'Back to School Deals' ad set 108, effective from 2025-08-13, using plan_2025-08-13 as the frozen source of truth. Set up a paused image ad titled 'ad_108_seed_v1', confirm the ad set inventory includes only this change while staying in-policy, and provide both a concise CSV receipt and a report with the date."
        ),
            actions=[
                Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
                Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
                Action(name="DailyAdsetInsights", kwargs={"adset_id": "108", "date": "2025-08-13"}),
                Action(name="CalcRoas", kwargs={"adset_id": "108", "date": "2025-08-13"}),
                Action(name="StartAutomationRun", kwargs={
                    "run_type": "seed_creative",
                    "input_ref": {"campaign_id": "6", "adset_id": "108", "name": "ad_108_seed_v1", "date": "2025-08-13"}
                }),
                Action(name="ListAdsInAdset", kwargs={"adset_id": "108"}),
                Action(name="MakeAd", kwargs={"adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}),
                Action(name="ListAdsInAdset", kwargs={"adset_id": "108"}),
                Action(name="VerifyApplied", kwargs={
                    "expected_rows": [{"adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}],
                    "actual_rows":   [{"adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}],
                    "key_fields": ["adset_id", "name", "format", "status"]
                }),
                Action(name="ExportReportCsv", kwargs={
                    "rows": [{"campaign_id": "6", "adset_id": "108", "name": "ad_108_seed_v1", "format": "image", "status": "paused"}]
                }),
                Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
        
                Action(name="EndAutomationRun", kwargs={
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
            "Handle a bookkeeping automation cycle for 2025-08-13 linked to plan_2025-08-13. Ensure an audit trail is kept, verify the anchor states, freeze the plan for evidence, and provide a compact CSV receipt along with a dated report titled 'bts bookkeeping cycle 2025-08-13'."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "bookkeeping",
                "input_ref": {"plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"plan_id": "plan_2025-08-13"}],
                "actual_rows": [{"plan_id": "plan_2025-08-13"}],
                "key_fields": ["plan_id"]
            }),
            Action(name="EndAutomationRun", kwargs={"run_id": "run_2025-08-13", "errors_json": {}}),
            Action(name="ExportReportCsv", kwargs={
                "rows": [
                    {"plan_id": "plan_2025-08-13", "run_id": "run_2025-08-13"}
                ]
            }),
            Action(name="WriteReport", kwargs={"date": "2025-08-13", "title": "bts bookkeeping cycle 2025-08-13"})
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
            "Coordinate ad set 104 in 'Fall Collection Launch' to align with plan_2025-08-13, guaranteeing the budget and strategy align. Anchor to a frozen plan snapshot and offer a compact CSV containing the plan_id and adset_id, plus a dated report."
        ),
            actions=[
                Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
                Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
                Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
        
                Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
                Action(name="SetAdsetStrategy", kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
        
                Action(name="FetchAdset", kwargs={"adset_id": "104"}),
                Action(name="VerifyApplied", kwargs={
                    "expected_rows": [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                    "actual_rows":   [{"adset_id": "104", "budget": 750.0, "bid_strategy": "cost_cap", "bid_amount": 22.0}],
                    "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
                }),
        
                Action(name="ExportReportCsv", kwargs={
                    "rows": [{"plan_id": "plan_2025-08-13", "adset_id": "104"}]
                }),
                Action(name="WriteReport", kwargs={"date": "2025-08-13"}),
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
            "Handle the reconciliation of the 'Mobile App Installs Campaign' with the frozen plan for 2025-08-13 for adsets 110 and 111. Ensure the plan is applied to the appropriate ad sets and confirm the final live status."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Mobile App Installs Campaign"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "7"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "110"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "110", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "110", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "110"}),
            Action(name="FetchAdset", kwargs={"adset_id": "111"})
        ],
        outputs=['"ok": true']
    ),

    Task(
        annotator="v3",
        user_id="task_082",
        instruction=(
            "Coordinate plan adherence for 'Back to School Deals' on 2025-08-13 by adjusting only the zero-delivery ad set. Confirm that ad set 108 aligns with plan_2025-08-13 and refrain from modifying ad sets not included in the plan. Save a CSV file as proof."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(
                name="SetAdsetStrategy",
                kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}
            ),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "actual_rows": [{"adset_id": "108", "budget": 800.0, "bid_strategy": "cost_cap", "bid_amount": 45.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            "Ensure compliance with bidding for the 'Fall Collection Launch' ad set 105 dated 2025-08-13 by logging the strategy as lowest_cost corresponding to plan_2025-08-13. Supply the CSV."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "strategy_compliance",
                "input_ref": {"campaign_id": "3", "adset_id": "105", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
            }),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "actual_rows": [{"adset_id": "105", "budget": 750.0, "bid_strategy": "lowest_cost"}],
                "key_fields": ["adset_id", "budget", "bid_strategy"]
            }),
            Action(name="ExportReportCsv", kwargs={
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
            Action(name="EndAutomationRun", kwargs={"run_id": "run_2025-08-13", "errors_json": {}})
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
            "Carry out a freeze audit for the 'Back to School Deals' campaign scheduled on 2025-08-13 for ad set 111. Confirm that the adset corresponds with plan_2025-08-13. Record the audit results in a CSV and compose the report."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
                "actual_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}]
            }),
            Action(name="ExportReportCsv", kwargs={"date": "2025-08-13",
                "rows": [{"adset_id": "111", "plan_id": "plan_2025-08-13", "tag": "freeze_audit"}]
            }),
            Action(name="WriteReport", kwargs={
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
            "Initiate the 'Global Summer Sale' campaign on 2025-08-13 and confirm ad set 112 adheres to plan_2025-08-13: its bid strategy should be lowest_cost. Coordinate the export of a compact CSV detailing the final configuration with status=active, ensuring inclusion of campaign_id, name, plan_id, adset_id, bid_strategy, and status."
        ),
            actions=[
                Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
                Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
                Action(name="StartAutomationRun", kwargs={
                    "run_type": "launch_alignment",
                    "input_ref": {"campaign_id": "1", "plan_id": "plan_2025-08-13", "adset_id": "112", "date": "2025-08-13"}
                }),
                Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
                Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
                Action(name="SetAdsetStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
                Action(name="StartCampaign", kwargs={"campaign_id": "1"}),
                Action(name="FetchAdset", kwargs={"adset_id": "112"}),
                Action(name="VerifyApplied", kwargs={
                    "expected_rows": [{"adset_id": "112", "bid_strategy": "lowest_cost"}],
                    "actual_rows":   [{"adset_id": "112", "bid_strategy": "lowest_cost"}],
                    "key_fields": ["adset_id", "bid_strategy"]
                }),
        
                Action(name="ExportReportCsv", kwargs={
                    "rows": [{
                        "campaign_id": "1",
                        "name": "Global Summer Sale",
                        "status": "active",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "112",
                        "bid_strategy": "lowest_cost"
                    }]
                }),
        
                Action(name="EndAutomationRun", kwargs={
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
            "Coordinate an alignment cycle for 'Fall Collection Launch' on 2025-08-13 concentrating on ad set 105. Base it on plan_2025-08-13, adjust budget/strategy as required, and handle the export of a compact CSV receipt."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Handle a maintenance toggle for 'Fall Collection Launch' on 2025-08-13 to ensure ad set 104 is in line with plan_2025-08-13. Verify that the campaign ends paused and provide a compact CSV configuration receipt."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="StopCampaign", kwargs={"campaign_id": "3", "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Coordinate the reconciliation of the 'Holiday Season Early Bird' campaign with the frozen plan for 2025-08-13. Confirm that ad set 106 has a budget of 500.0 with a cost_cap bid of 18.0, and that ad set 107 has a budget of 400.0 with lowest_cost. Validate the outcomes against the plan."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "5"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Ensure the 'Global Summer Sale' campaign is in alignment with the frozen plan for 2025-08-13 for ad set 112. Confirm that budget 700.0 and bid strategy lowest_cost are implemented and validated."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "1"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "112"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "112", "new_budget": 700.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "112", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Make sure the 'Back to School Deals' campaign corresponds with the frozen plan for 2025-08-13 for ad set 111. Confirm the ad set matches the plan and proceed to export a CSV documenting the aligned rows."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "111", "new_budget": 1000.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5, "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Coordinate the alignment of 'Back to School Deals' ad set 111 with the frozen plan plan_2025-08-13 by utilizing the plan (budget=1000.0, strategy=cost_cap with bid=2.5), confirming that the live state matches, documenting the automation execution, and generating a concise CSV receipt with campaign_id, name, plan_id, adset_id, and bid_strategy."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "plan_execution",
                "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "adset_id": "111", "date": "2025-08-13"}
            }),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
            Action(name="UpdateAdsetBudget", kwargs={
                "adset_id": "111",
                "new_budget": 1000.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="SetAdsetStrategy", kwargs={
                "adset_id": "111",
                "bid_strategy": "cost_cap",
                "bid_amount": 2.5,
                "reason": "plan_2025-08-13"
            }),
            Action(name="FetchAdset", kwargs={"adset_id": "111"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
                "actual_rows":   [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="ExportReportCsv", kwargs={
                "rows": [{
                    "campaign_id": "6",
                    "name": "Back to School Deals",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111",
                    "bid_strategy": "cost_cap"
                }]
            }),
            Action(name="EndAutomationRun", kwargs={"run_id": "run_2025-08-13", "errors_json": {}}),
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
            "Coordinate the alignment of 'Fall Collection Launch' with the frozen plan for 2025-08-13 for both ad sets. Implement the plan values on ad set 104, ensure ad set 105 already complies with the plan without modifications, and validate the applied state against plan_2025-08-13."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "104", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 22.0, "reason": "plan_2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "104"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="VerifyApplied", kwargs={"plan_id": "plan_2025-08-13"}),
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
            "Handle a KPI-scored maintenance toggle for 'Holiday Season Early Bird' as of 2025-08-13: align ad set 106 to plan_2025-08-13 (budget 500.0 and cost_cap with bid_amount 18.0), calculate ROAS on 2025-08-13 for audit, freeze the plan snapshot as evidence, pause the campaign, and generate a concise CSV with campaign_id, status, plan_id, adset_id, and bid_strategy."
        ),
    actions=[
        Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
        Action(name="DailyAdsetInsights", kwargs={"adset_id": "106", "date": "2025-08-13"}),
        Action(name="CalcRoas", kwargs={"adset_id": "106", "date": "2025-08-13"}),
        Action(name="FreezePlan", kwargs={"date": "2025-08-13"}),
        Action(name="StartAutomationRun", kwargs={
            "run_type": "kpi_maintenance_toggle",
            "input_ref": {"campaign_id": "5", "adset_id": "106", "plan_id": "plan_2025-08-13", "date": "2025-08-13"}
        }),
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
        Action(name="UpdateAdsetBudget", kwargs={"adset_id": "106", "new_budget": 500.0, "reason": "plan_2025-08-13"}),
        Action(name="SetAdsetStrategy", kwargs={"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0, "reason": "plan_2025-08-13"}),
        Action(name="FetchAdset", kwargs={"adset_id": "106"}),
        Action(name="VerifyApplied", kwargs={
            "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "actual_rows":   [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),
        Action(name="StopCampaign", kwargs={"campaign_id": "5"}),
        Action(name="ExportReportCsv", kwargs={
            "rows": [
                {"campaign_id": "5", "status": "paused", "plan_id": "plan_2025-08-13",
                 "adset_id": "106", "bid_strategy": "cost_cap"}
            ]
        }),
        Action(name="EndAutomationRun", kwargs={
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
            "Coordinate the alignment of 'Back to School Deals' ad set 108 to the frozen plan for 2025-08-13. Apply plan_2025-08-13 budget and bid strategy, then confirm the accuracy of the values."
        ),
        actions=[
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "108"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
            Action(name="VerifyApplied", kwargs={
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
            "Handle the update of ad set 108 in 'Back to School Deals' in accordance with the plan for 2025-08-13, and ensure the live state is consistent."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "6"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "108", "new_budget": 800.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 45.0, "reason": "plan_2025-08-13"}),
            Action(name="FetchAdset", kwargs={"adset_id": "108"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the alignment of 'Holiday Season Early Bird' with the frozen plan for 2025-08-13 for ad set 107. Implement a budget of 400.0 and set to lowest_cost citing 'plan_2025-08-13', then confirm the state."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "107"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "107", "new_budget": 400.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "107", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Coordinate the alignment of the 'Global Summer Sale' ad set 101 to the frozen plan for 2025-08-13, updating its budget and bid strategy accordingly. Export a CSV as the receipt."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Global Summer Sale"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "101"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "101", "new_budget": 950.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy",
                   kwargs={"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 35.0, "reason": "plan_2025-08-13"}),
            Action(name="ExportReportCsv", kwargs={
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
            "Ensure the 'Fall Collection Launch' is reconciled to the frozen plan for 2025-08-13 for ad set 105. Set the budget to 750.0 and use the lowest_cost strategy with reason 'plan_2025-08-13', then verify that values match."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Fall Collection Launch"}),
            Action(name="ListCampaignAdsets", kwargs={"campaign_id": "3"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "105"}),
            Action(name="UpdateAdsetBudget", kwargs={"adset_id": "105", "new_budget": 750.0, "reason": "plan_2025-08-13"}),
            Action(name="SetAdsetStrategy", kwargs={"adset_id": "105", "bid_strategy": "lowest_cost", "reason": "plan_2025-08-13"}),
            Action(name="VerifyApplied", kwargs={
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
            "Handle 'Back to School Deals' by marking it under maintenance starting 2025-08-13. Coordinate ad set 111 to match plan_2025-08-13 with a budget of 1000.0 and a cost_cap bid_amount of 2.5, halt the campaign, and prepare a concise CSV receipt including campaign_id, status, plan_id, adset_id, and bid_strategy."
        ),
    actions=[
        Action(name="LookupCampaign", kwargs={"name": "Back to School Deals"}),
        Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
        Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "111"}),
        Action(name="StartAutomationRun", kwargs={
            "run_type": "alignment_then_pause",
            "input_ref": {"campaign_id": "6", "plan_id": "plan_2025-08-13", "adset_id": "111", "date": "2025-08-13"}
        }),
        Action(name="UpdateAdsetBudget", kwargs={
            "adset_id": "111", "new_budget": 1000.0, "reason": "plan_2025-08-13"
        }),
        Action(name="SetAdsetStrategy", kwargs={
            "adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5, "reason": "plan_2025-08-13"
        }),
        Action(name="VerifyApplied", kwargs={
            "expected_rows": [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
            "actual_rows":   [{"adset_id": "111", "budget": 1000.0, "bid_strategy": "cost_cap", "bid_amount": 2.5}],
            "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
        }),
        Action(name="StopCampaign", kwargs={"campaign_id": "6"}),
        Action(name="ExportReportCsv", kwargs={
            "rows": [{
                "campaign_id": "6",
                "status": "paused",
                "plan_id": "plan_2025-08-13",
                "adset_id": "111",
                "bid_strategy": "cost_cap"
            }]
        }),
        Action(name="EndAutomationRun", kwargs={
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
            "Apply the frozen plan plan_2025-08-13 to the 'Holiday Season Early Bird' ad set 106, adjusting the live budget and bid strategy to align with the plan (budget=500.0, strategy=cost_cap with bid=18.0). Confirm the applied state, log the automation process, and create a concise CSV receipt with campaign_id, name, plan_id, adset_id, and bid_strategy."
        ),
        actions=[
            Action(name="LookupCampaign", kwargs={"name": "Holiday Season Early Bird"}),
            Action(name="FetchPlanForDate", kwargs={"date": "2025-08-13"}),
            Action(name="GetAdsetFromPlan", kwargs={"plan_id": "plan_2025-08-13", "adset_id": "106"}),
            Action(name="StartAutomationRun", kwargs={
                "run_type": "plan_execution",
                "input_ref": {"campaign_id": "5", "plan_id": "plan_2025-08-13", "adset_id": "106", "date": "2025-08-13"}
            }),
            Action(name="UpdateAdsetBudget", kwargs={
                "adset_id": "106",
                "new_budget": 500.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="SetAdsetStrategy", kwargs={
                "adset_id": "106",
                "bid_strategy": "cost_cap",
                "bid_amount": 18.0,
                "reason": "plan_2025-08-13"
            }),
            Action(name="FetchAdset", kwargs={"adset_id": "106"}),
            Action(name="VerifyApplied", kwargs={
                "expected_rows": [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "actual_rows":   [{"adset_id": "106", "budget": 500.0, "bid_strategy": "cost_cap", "bid_amount": 18.0}],
                "key_fields": ["adset_id", "budget", "bid_strategy", "bid_amount"]
            }),
            Action(name="EndAutomationRun", kwargs={
                "run_id": "run_2025-08-13",
                "errors_json": {},
                "outputs_json": {"applied": True, "adset_id": "106", "plan_id": "plan_2025-08-13"}
            }),
            Action(name="ExportReportCsv", kwargs={
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
