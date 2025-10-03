
tasks = [
    {
        "annotator": v2,
        "user_id": "task_001",
        "instruction": "Handle the assessment of delivery for 'Fall Collection Launch' on 2025-08-13 concerning ad set 104, calculate ROAS using same-day insights, and subsequently adjust the ad set to plan_2025-08-13, ensuring the final aligned state reflects the plan accurately.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_002",
        "instruction": "Coordinate the reconciliation of ad set 102 in 'Global Summer Sale' with the frozen plan dated 2025-08-13 as the definitive reference. Confirm that the applied configuration corresponds with the plan and save a concise CSV summary.",
        "actions": [
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost",
                            "status": "ok"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"102\"",
                "\"budget\": 600.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"status\": \"ok\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_003",
        "instruction": "Coordinate the alignment of 'Fall Collection Launch' with the frozen plan set for 2025-08-13 for both ad sets. Implement the plan values for ad set 104, verify that ad set 105 already conforms to the plan without adjustments, and confirm the applied state matches plan_2025-08-13.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_004",
        "instruction": "Ensure the plan-designated creative type is implemented for 'Global Summer Sale' ad set 101 as of 2025-08-13. Reference the frozen plan for 2025-08-13 as the authoritative source for the necessary creative_type. Confirm there is precisely one active ad in the ad set and that its creative_type aligns with the plan. Execute an auditable run and generate a concise CSV receipt detailing plan_id, adset_id, active_ad_id, and active_creative_type.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "input_ref": {
                        "campaign_id": "1",
                        "adset_id": "101",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "ReplaceAdCreatives",
                "arguments": {
                    "activate_id": "1102",
                    "pause_id": "1101"
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1,
                            "active_creative_type": "video"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1,
                            "active_creative_type": "video"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "active_ads",
                        "active_creative_type"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "active_ad_id": "1102",
                            "active_creative_type": "video"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "rotation_ok": true,
                        "adset_id": "101",
                        "active_ad_id": "1102",
                        "active_creative_type": "video"
                    }
                }
            }
        ],
        "outputs": [
                "\"rotation_ok\": true",
                "\"adset_id\": \"101\"",
                "\"active_ad_id\": \"1102\"",
                "\"active_creative_type\": \"video\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_005",
        "instruction": "Handle the reconciliation of adset 101 ad set in 'Global Summer Sale' to align with the frozen plan for 2025-08-13, ensuring the budget and bid strategy are correct. Keep an auditable record by preparing a dated report and document the reconciliation with a CSV file.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"adset_id\": \"101\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_006",
        "instruction": "Coordinate the alignment of the 'Back to School Deals' campaign with the frozen plan for 2025-08-13. Use plan_id 'plan_2025-08-13' as the authoritative guide to confirm ad set 108 shows budget 800.0 and cost_cap with bid 45.0. Verify that the setup is consistent with the plan.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School Deals\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_007",
        "instruction": "Handle the daily allocation and rotation for 'Global Summer Sale' scheduled on 2025-08-13, ensuring compliance with the policy and the frozen plan. Adjust ad sets 101 and 102 to align with the plan\u2019s budgets and strategies, apply the documented rotation for ad set 101 so that only one ad remains active, document any delivery exceptions for the day using the available insights, and generate auditable artifacts.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "allocation_rotation_daily",
                    "input_ref": {
                        "campaign_id": "1",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13",
                        "adsets": [
                            "101",
                            "102"
                        ]
                    }
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FetchCreativeRotation",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdStatus",
                "arguments": {
                    "ad_id": "1101",
                    "status": "paused"
                },
            },
            {
                "name": "SetAdStatus",
                "arguments": {
                    "ad_id": "1102",
                    "status": "active"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "active_ads"
                    ]
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExceptionRaiser",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "insights": [],
                    "rules": {
                        "zero_delivery_impressions": 0
                    }
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0,
                            "old_ad_id": "1101",
                            "new_ad_id": "1102"
                        },
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "plan_id": "plan_2025-08-13",
                        "adsets": [
                            "101",
                            "102"
                        ],
                        "rotation": {
                            "101": {
                                "old_ad_id": "1101",
                                "new_ad_id": "1102"
                            }
                        }
                    }
                }
            }
        ],
        "outputs": [
                "\"run_id\": \"run_2025-08-13\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"adset_id\": \"102\"",
                "\"old_ad_id\": \"1101\"",
                "\"new_ad_id\": \"1102\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_008",
        "instruction": "Coordinate the reconciliation of 'App Installs - Android' ad set 110 within the 'Mobile App Installs Campaign' to correspond with plan_2025-08-13 as of 2025-08-13: configure its budget and bid strategy accordingly. Provide a concise CSV receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "110"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1000.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "110",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "110",
                            "budget": 1000.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "110",
                            "budget": 1000.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "7",
                            "adset_id": "110",
                            "new_budget": 1000.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"7\"",
                "\"adset_id\": \"110\"",
                "\"new_budget\": 1000.0\"",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_009",
        "instruction": "Handle the budget rounding policy enforcement on 2025-08-13 for the Global Summer Sale campaign. Validate the policy rule referred to as 'budget_rounding_unit' and synchronize ad sets to 'plan_2025-08-13': ensure ad set 101 and ad set 112 have budgets, strategies, and bids aligning with the plan's guidelines. Verify that the final states coincide with the plan's values.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FetchPolicyRule",
                "arguments": {
                    "rule_name": "budget_rounding_unit"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 700.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"name\": \"budget_rounding_unit\"",
                "\"value\": \"10\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"adset_id\": \"112\"",
                "\"budget\": 700.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_010",
        "instruction": "Coordinate a bookkeeping automation cycle for 2025-08-13, based on plan_2025-08-13. Keep a comprehensive audit trail, ensure the anchor states are verified, secure the plan for evidence, and provide a concise CSV receipt along with a dated report titled 'bts bookkeeping cycle 2025-08-13'.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "bookkeeping",
                    "input_ref": {
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "plan_id": "plan_2025-08-13"
                        }
                    ],
                    "actual_rows": [
                        {
                            "plan_id": "plan_2025-08-13"
                        }
                    ],
                    "key_fields": [
                        "plan_id"
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "run_id": "run_2025-08-13"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "title": "bts bookkeeping cycle 2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"run_id\": \"run_2025-08-13\"",
                "\"report_id\": \"rep_2025-08-13_bts-bookkeeping-cycle-2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_011",
        "instruction": "Coordinate the 'Holiday Season Early Bird' campaign to match the frozen plan for 2025-08-13. Employ the plan to implement updates and verify live alignment afterward.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                }
            }
        ],
        "outputs": [
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_012",
        "instruction": "Ensure the 'Global Summer Sale' campaign is aligned with the frozen plan for 2025-08-13 for ad set 101. Utilize plan_2025-08-13, confirming the budget and bid are implemented, and document all updates. Subsequently, check that the ad set adheres to the planned budget and bid strategy.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_013",
        "instruction": "Handle the verification of 'Back to School Deals' ad set 107 in comparison to the 2025-08-13 frozen plan, maintain the verification by solidifying the plan, and compile a report with tag ['bts'].",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "bts"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_014",
        "instruction": "Coordinate the reconciliation of the \u2018Global Summer Sale\u2019 campaign with the frozen plan for 2025-08-13, making sure ad sets 101, 102, and 112 align with the designated budgets and bid strategies from plan_id \u2018plan_2025-08-13\u2019. Verify that the final ad set states match the plan values.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 700.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "112"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"adset_id\": \"102\"",
                "\"budget\": 600.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"adset_id\": \"112\"",
                "\"budget\": 700.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_015",
        "instruction": "Coordinate the reconciliation of 'Holiday - Toys' (ad set 107) in 'Holiday Season Early Bird' to the frozen plan for 2025-08-13, ensuring that the budget and bid strategy are applied. Deliver an audit snapshot starting from 2025-08-10, a dated report for 2025-08-13, and a CSV artifact with fields [campaign_id, adset_id].",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AdsetRangeSpend",
                "arguments": {
                    "adset_id": "107",
                    "start_date": "2025-08-10",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "5",
                            "adset_id": "107"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"adset_id\": \"107\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_016",
        "instruction": "Organize the alignment of Holiday Season Early Bird ad set 106 to the 2025-08-13 frozen plan. Implement a budget of 500.0 and bid strategy cost_cap with bid_amount 18.0 per plan_id 'plan_2025-08-13', then verify the applied state.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"budget\": 500.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 18.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_017",
        "instruction": "Generate an auditable rolling range view for 'Global Summer Sale' spanning 2025-08-10 to 2025-08-13, linked to the 2025-08-13 state of record. Ensure evidence is anchored by maintaining the 2025-08-13 plan unchanged. Include the campaign\u2019s expenditure over that period, and ensure the cumulative spend value is reflected in the CSV. Supply a dated record along with a CSV detailing one row for campaign_id '1' over the specified range using metric 'spend'.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "rolling_range_view",
                    "input_ref": {
                        "campaign_id": "1",
                        "range": "2025-08-10..2025-08-13",
                        "anchor_date": "2025-08-13"
                    }
                },
            },
            {
                "name": "AdsetRangeSpend",
                "arguments": {
                    "campaign_id": "1",
                    "start_date": "2025-08-10",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "metric": "spend",
                            "range": "2025-08-10..2025-08-13",
                            "total_spend": 0.0
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_018",
        "instruction": "Coordinate a KPI-scored maintenance toggle for 'Holiday Season Early Bird' as of 2025-08-13: you should align ad set 106 with plan_2025-08-13 (budget 500.0 and cost_cap with bid_amount 18.0), calculate ROAS on 2025-08-13 for auditing, preserve the plan snapshot as evidence, halt the campaign, and deliver a concise CSV containing campaign_id, status, plan_id, adset_id, and bid_strategy.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "kpi_maintenance_toggle",
                    "input_ref": {
                        "campaign_id": "5",
                        "adset_id": "106",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "HaltCampaign",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "5",
                            "status": "paused",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "106",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "campaign_id": "5",
                        "status": "paused",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "106",
                        "bid_strategy": "cost_cap"
                    }
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"status\": \"paused\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_019",
        "instruction": "Handle the updates for the live ad sets 101 and 102 within 'Global Summer Sale' to align with the frozen plan set for 2025-08-13 by implementing the necessary budget and bidding adjustments. Additionally, assess the policy regulations concerning currency and budget rounding, and keep a record of the reconciliation in a CSV receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "FetchPolicyRule",
                "arguments": {
                    "rule_name": "currency"
                },
            },
            {
                "name": "FetchPolicyRule",
                "arguments": {
                    "rule_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101"
                        },
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_020",
        "instruction": "Coordinate the 'Global Summer Sale' campaign on 2025-08-13 to align with the frozen source of truth plan_2025-08-13 for ad set 101. Implement the plan's budget and bid strategy if required, verify the alignment, document a dated note, and export a minimized CSV receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "name": "Global Summer Sale",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0,
                            "ok": true
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0\"",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_021",
        "instruction": "Handle a quick application-and-fetch for 'Back to School Deals' ad set 108 on 2025-08-13. Make sure the ad set corresponds with the plan 'plan_2025-08-13', then retrieve the ad set.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_022",
        "instruction": "Coordinate the update of the live ad set 102 in 'Global Summer Sale' to align with the frozen plan for 2025-08-13. Apply the necessary budget and bidding according to plan_2025-08-13, and verify the live state.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"102\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_023",
        "instruction": "Handle the reconciliation of ad set 101 in 'Global Summer Sale' to the frozen plan for 2025-08-13, using it as the source of truth. Confirm that the plan's configuration is applied and the applied state aligns with the plan; maintain a concise CSV summary.",
        "actions": [
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0,
                            "status": "ok"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"status\": \"ok\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_024",
        "instruction": "Coordinate the alignment of ad set 101 in 'Global Summer Sale' to the frozen plan for 2025-08-13, ensuring its budget and bid strategy are updated in accordance with the plan. Generate a CSV to serve as the receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "name": "Global Summer Sale",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_025",
        "instruction": "Handle the reconciliation of the 'Mobile App Installs Campaign' with the frozen plan for 2025-08-13 concerning adsets 110 and 111. Implement the plan to the specified ad sets and ensure the final live state is verified.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Mobile App Installs Campaign"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "7"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "110"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "110",
                    "new_budget": 1000.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "110",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1000.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "111",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 2.5,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "111"
                }
            }
        ],
        "outputs": [
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_026",
        "instruction": "Coordinate the alignment of 'Holiday Season Early Bird' ad set 107 with plan_2025-08-13 as of 2025-08-13: adjust its budget to 400.0 and its bid strategy to lowest_cost. Provide a concise task output including plan_id, adset_id, budget, and bid_strategy.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_027",
        "instruction": "Handle a freeze audit for the 'Back to School Deals' campaign scheduled on 2025-08-13 for ad set 111. Verify that the adset matches with plan_2025-08-13. Record the audit in a CSV file and prepare the report.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "111",
                            "budget": 1000.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "111",
                            "budget": 1000.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "date": "2025-08-13",
                    "rows": [
                        {
                            "adset_id": "111",
                            "plan_id": "plan_2025-08-13",
                            "tag": "freeze_audit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "freeze",
                        "audit"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"111\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_028",
        "instruction": "Manage an auditable health snapshot for 'Back to School Deals' on 2025-08-13, linked to the frozen plan. Confirm that a finished health snapshot run is logged and export a CSV receipt including the columns: campaign_id, plan_id, run_id.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "health_snapshot",
                    "input_ref": {
                        "plan_id": "plan_2025-08-13"
                    }
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "outputs_json": {
                        "plan_id": "plan_2025-08-13"
                    },
                    "errors_json": {}
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "plan_id": "plan_2025-08-13",
                            "run_id": "run_2025-08-13"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"run_id\": \"run_2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_029",
        "instruction": "Handle the reconciliation of the 'Holiday Season Early Bird' campaign to the frozen plan dated 2025-08-13. Ensure that ad set 106 has a budget of 500.0 with a cost_cap bid of 18.0, and ad set 107 has a budget of 400.0 with lowest_cost. Cross-check the results against the plan.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"bid_strategy\": \"cost_cap\"",
                "\"adset_id\": \"107\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_030",
        "instruction": "Coordinate to ensure that, in the 'Back to School Deals' campaign, ad set 108 matches the frozen plan for 2025-08-13 identified by 'plan_2025-08-13'. Make any necessary adjustments to align and then proceed with verification of the changes.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School Deals\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0\"",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_031",
        "instruction": "Coordinate the alignment of the 'Holiday Season Early Bird' ad set 106 with plan_2025-08-13 as of 2025-08-13\u2014budget 500.0 and cost_cap at 18.0\u2014and generate a compact CSV featuring plan_id, campaign_id, adset_id, and checksum=a1b2c3d4e5f6, along with a dated markdown report.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "inventory_snapshot",
                    "input_ref": {
                        "campaign_id": "5",
                        "adset_id": "106",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "CalcPlanChecksum",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "campaign_id": "5",
                            "adset_id": "106",
                            "checksum": "a1b2c3d4e5f6"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "title": "Inventory Snapshot 2025-08-13 - plan_2025-08-13",
                    "tags": [
                        "inventory",
                        "snapshot",
                        "plan_2025-08-13"
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "snapshot_ok": true,
                        "campaign_id": "5",
                        "adset_id": "106",
                        "plan_id": "plan_2025-08-13",
                        "checksum": "a1b2c3d4e5f6"
                    }
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"adset_id\": \"106\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"checksum\": \"a1b2c3d4e5f6\"",
                "\"snapshot_ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_032",
        "instruction": "Conduct an exception audit for 'Global Summer Sale' dated 2025-08-13 against plan_2025-08-13. By employing rules zero_delivery_impressions=0, cap_hit_spend=1000.0, and data_gap_days=2, document exceptions in the system for the provided insights\u2014101(impressions=1200, spend=480.0, missing_days=0) and 102(impressions=0, spend=0.0, missing_days=2). Create two artifacts: a CSV listing the triggered alerts for adset_id 102 (zero_delivery and data_gap) and a dated report with tags ['gss','exceptions'].",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExceptionRaiser",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "insights": [
                        {
                            "adset_id": "101",
                            "impressions": 1200,
                            "spend": 480.0,
                            "missing_days": 0
                        },
                        {
                            "adset_id": "102",
                            "impressions": 0,
                            "spend": 0.0,
                            "missing_days": 2
                        }
                    ],
                    "rules": {
                        "zero_delivery_impressions": 0,
                        "cap_hit_spend": 1000.0,
                        "data_gap_days": 2
                    }
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "alert": "zero_delivery"
                        },
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "alert": "data_gap"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "gss",
                        "exceptions"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"count\": 2",
                "\"type\": \"zero_delivery\"",
                "\"type\": \"data_gap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_033",
        "instruction": "Handle the creation of an insights snapshot for 'Back to School Deals' ad set 107, effective as of 2025-08-13, and use plan_2025-08-13 as the unchanging reference. Ensure auditability by maintaining plan evidence and snapshot context while providing a concise CSV that includes campaign_id, adset_id, date, and plan_id, along with a dated report.",
        "actions": [
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "snapshot",
                    "input_ref": {
                        "campaign": "Back to School Deals",
                        "adset_id": "107",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "adset_id": "107",
                            "date": "2025-08-13",
                            "plan_id": "plan_2025-08-13"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"adset_id\": \"107\"",
                "\"date\": \"2025-08-13\"",
                "\"plan_id\": \"plan_2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_034",
        "instruction": "Coordinate the audit of 'Back to School Deals' ad set 108 as of 2025-08-13, using plan_2025-08-13 for comparison. Document the audit findings as structured rule exceptions tied to plan_2025-08-13, and secure the plan snapshot for verification. Supply a compact CSV with a single row containing plan_id and adset_id, and prepare a dated report tagged with ['rules','audit','bts'].",
        "actions": [
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "ExceptionRaiser",
                "arguments": {
                    "date": "2025-08-13",
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108",
                    "rules": {
                        "policy_check": "audit"
                    }
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "108"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "rules",
                        "audit",
                        "bts"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_035",
        "instruction": "Handle the 'Electronics - UK' ad set within the 'Global Summer Sale' (adset_id '112') to ensure it matches the frozen plan as of 2025-08-13 identified by plan_2025-08-13. The adset state should align with the plan state. Document a creative rotation for ad_id '1111' from 'image' to 'video' on 2025-08-13.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "CreativeRotationRecorder",
                "arguments": {
                    "ad_id": "1111",
                    "from_creative": "image",
                    "to_creative": "video",
                    "rotation_date": "2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"adset_id\": \"112\"",
                "\"ad_id\": \"1111\"",
                "\"date\": \"2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_036",
        "instruction": "Assess the delivery of 'Fall Collection Launch' on 2025-08-13 for ad set 105, calculate ROAS using insights from the same day, then adjust the ad set to match plan_2025-08-13, and subsequently confirm the final state is consistent with the plan.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_037",
        "instruction": "Handle the 'Back to School Deals' by setting it in maintenance effective 2025-08-13. Coordinate the alignment of ad set 111 to plan_2025-08-13, ensuring a budget of 1000.0 with a cost_cap bid_amount of 2.5; pause the campaign and produce a concise CSV receipt containing campaign_id, status, plan_id, adset_id, and bid_strategy.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "alignment_then_pause",
                    "input_ref": {
                        "campaign_id": "6",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "111",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1000.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "111",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 2.5,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "111",
                            "budget": 1000.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "111",
                            "budget": 1000.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "HaltCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "status": "paused",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "111",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "campaign_id": "6",
                        "status": "paused",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "111",
                        "bid_strategy": "cost_cap"
                    }
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"status\": \"paused\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"111\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_038",
        "instruction": "Coordinate the reconciliation of 'Global Summer Sale' into the frozen plan for 2025-08-13 concerning ad set 102. Confirm that the budget and bid strategy are applied and verified.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"102\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_039",
        "instruction": "Coordinate an alignment cycle for 'Fall Collection Launch' on 2025-08-13, concentrating on ad set 105. Anchor to plan_2025-08-13, adjust budget/strategy as necessary, and output a compact CSV receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "status": "active",
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"status\": \"active\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_040",
        "instruction": "Confirm compliance of the 'Fall Collection Launch' campaign against the frozen plan for 2025-08-13 concerning ad set 105. Utilize plan_id 'plan_2025-08-13' and make sure budget 750.0 and bid strategy lowest_cost are implemented. Export a CSV with the final configuration.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "name": "Fall Collection Launch",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_041",
        "instruction": "Handle the reconciliation of the 'Fall Collection Launch' campaign to the frozen plan for 2025-08-13 adsets 104 and 105. Implement the plan for the designated ad sets and verify the outcome.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap"
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap"
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                }
            }
        ],
        "outputs": [
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_042",
        "instruction": "Coordinate the finalization of compliance for 'Back to School Deals' on 2025-08-13. Using plan_id 'plan_2025-08-13', make sure ad set 108 meets its designated budget and bid strategy. Confirm the status, compile a report with tags ['compliance','bts'], and generate a CSV export.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "compliance",
                        "bts"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "name": "Back to School Deals",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School Deals\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0\"",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_043",
        "instruction": "Handle the reconciliation of the 'Fall Collection Launch' campaign with the frozen plan for 2025-08-13. Refer to plan_id 'plan_2025-08-13' as the authoritative source: assign budget and bid strategy for ad set 104 and 105; Ensure both ad sets are retrieved to verify alignment.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "105"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 22.0",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_044",
        "instruction": "Coordinate the final setup for the 'Fall Collection Launch' ad set 105 within plan_2025-08-13. Guarantee that its bid strategy is set to lowest_cost and the budget is 750.0, and generate a concise CSV along with a report dated appropriately.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "alignment",
                    "input_ref": {
                        "adset_id": "105",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "105"
                    ]
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "ok": true,
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "105",
                        "budget": 750.0,
                        "bid_strategy": "lowest_cost"
                    }
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_045",
        "instruction": "Oversee a compliance review for the 'Back to School Deals' campaign adset 108 on 2025-08-13, comparing it against the frozen source of truth plan_2025-08-13. Implement any necessary modifications as outlined in the plan and ensure the campaign returns to its paused status post-check.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "HaltCampaign",
                "arguments": {
                    "campaign_id": "6",
                    "reason": "plan_2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School Deals\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0",
                "\"status\": \"paused\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_046",
        "instruction": "Align the 'Fall Collection Launch' such that 'Fall Fashion - Women' and 'Fall Fashion - Men' are consistent with the frozen plan for 2025-08-13, and submit a CSV artifact as the audit documentation.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "adset_id": "104"
                        },
                        {
                            "campaign_id": "3",
                            "adset_id": "105"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_047",
        "instruction": "Handle the verification and sealing of the plan for 'Back to School Deals' on 2025-08-13 by affirming the integrity against a checksum, saving the frozen snapshot for audit purposes, and creating a one-row CSV receipt of the verification.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "plan_verification",
                    "input_ref": {
                        "campaign_id": "6",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalcPlanChecksum",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "plan_id": "plan_2025-08-13"
                        }
                    ],
                    "actual_rows": [
                        {
                            "plan_id": "plan_2025-08-13"
                        }
                    ],
                    "key_fields": [
                        "plan_id"
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "verification": "ok",
                        "plan_id": "plan_2025-08-13"
                    }
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "plan_id": "plan_2025-08-13",
                            "status": "ok"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"status\": \"ok\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_048",
        "instruction": "Coordinate the creation of two spend-window summaries for 'Global Summer Sale' ad set 101 for the periods of 2025-08-10..2025-08-11 and 2025-08-12..2025-08-13, associate them with the 2025-08-13 plan state using a frozen snapshot, and provide a CSV artifact labeled ['spend','windows','gss'] along with a dated report.",
        "actions": [
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "window_spend_snapshot",
                    "input_ref": {
                        "campaign": "Global Summer Sale",
                        "adset_id": "101",
                        "snapshot_date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "AdsetRangeSpend",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-10",
                    "end_date": "2025-08-11"
                },
            },
            {
                "name": "AdsetRangeSpend",
                "arguments": {
                    "adset_id": "101",
                    "start_date": "2025-08-12",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "adset_id": "101",
                            "range": "2025-08-10..2025-08-11",
                            "plan_id": "plan_2025-08-13"
                        },
                        {
                            "adset_id": "101",
                            "range": "2025-08-12..2025-08-13",
                            "plan_id": "plan_2025-08-13"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "spend",
                        "windows",
                        "gss"
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"adset_id\": \"101\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_049",
        "instruction": "Ensure the execution of the plan-selected creative for 'Global Summer Sale' ad set 101 as of 2025-08-13. Guarantee that ad 1102 (video) is the sole active ad within the ad set, and ad 1101 remains paused, aligning with plan_2025-08-13. Provide a concise CSV receipt including plan_id, adset_id, activate_id, pause_id, and final_active_status.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "input_ref": {
                        "campaign_id": "1",
                        "adset_id": "101",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "ReplaceAdCreatives",
                "arguments": {
                    "activate_id": "1102",
                    "pause_id": "1101"
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "active_ads"
                    ]
                },
            },
            {
                "name": "CreativeRotationRecorder",
                "arguments": {
                    "ad_id": "1102",
                    "from_creative": "image",
                    "to_creative": "video",
                    "rotation_date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "activate_id": "1102",
                            "pause_id": "1101",
                            "final_active_status": "active"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "rotation_ok": true,
                        "adset_id": "101",
                        "activate_id": "1102",
                        "pause_id": "1101"
                    }
                }
            }
        ],
        "outputs": [
                "\"rotation_ok\": True",
                "\"adset_id\": \"101\"",
                "\"activate_id\": \"1102\"",
                "\"pause_id\": \"1101\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_050",
        "instruction": "Handle the issuance of a minimal plan compliance pass for 'Fall Collection Launch' ad set 105 on 2025-08-13. Allocate budget and strategy according to plan_2025-08-13, then validate with a CSV of the final state.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "name": "Fall Collection Launch",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_051",
        "instruction": "Handle the application of frozen plan plan_2025-08-13 to 'Holiday Season Early Bird' ad set 106, updating the live budget and bid strategy to the plan (budget=500.0, strategy=cost_cap with bid=18.0). Ensure the applied state is verified, document the automation execution, and produce a concise CSV receipt containing campaign_id, name, plan_id, adset_id, and bid_strategy.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "plan_execution",
                    "input_ref": {
                        "campaign_id": "5",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "106",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "applied": true,
                        "adset_id": "106",
                        "plan_id": "plan_2025-08-13"
                    }
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "5",
                            "name": "Holiday Season Early Bird",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "106",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_052",
        "instruction": "Coordinate the alignment of the 'Fall Collection Launch' campaign on 2025-08-13 with the frozen plan plan_2025-08-13 by making sure ad set 105\u2019s budget and bid strategy reflect the plan. Validate the aligned state in an appropriately dated report and generate a CSV detailing the finalized values.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "name": "Fall Collection Launch",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost",
                            "ok": true
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_053",
        "instruction": "Handle the alignment of the 'Global Summer Sale' campaign with the frozen plan for 2025-08-13. Configure ad set 101 to adhere to the planned budget 950.0 and set the cost_cap with bid_amount 35.0, maintaining a single-active state where ad 1102 is active and ad 1101 is paused. Export a compact CSV receipt of the alignment.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdStatus",
                "arguments": {
                    "ad_id": "1101",
                    "status": "paused"
                },
            },
            {
                "name": "SetAdStatus",
                "arguments": {
                    "ad_id": "1102",
                    "status": "active"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "active_ads"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0,
                            "old_ad_id": "1101",
                            "new_ad_id": "1102"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0\"",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0\"",
                "\"old_ad_id\": \"1101\"",
                "\"new_ad_id\": \"1102\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_054",
        "instruction": "Coordinate the alignment of the 'Holiday Season Early Bird' campaign with the frozen plan for 2025-08-13. Make sure ad sets 106 and 107 are consistent with the plan's budget and bid strategy, and verify the applied values.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"budget\": 500.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 18.0",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_055",
        "instruction": "Handle a maintenance switch for the 'Global Summer Sale' campaign on 2025-08-13. Briefly activate the campaign, confirm ad set 102 aligns with plan_2025-08-13 budget and bid strategy, then return the campaign to paused status. Prepare an auditable record and a CSV showing the final configuration.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "maintenance_toggle",
                    "input_ref": {
                        "campaign_id": "1",
                        "adset_id": "102",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "LaunchCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "HaltCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "status": "paused",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"status\": \"paused\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"102\"",
                "\"budget\": 600.0\"",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_056",
        "instruction": "Coordinate a plan-scored alignment for 'Holiday Season Early Bird' ad set 107 as of 2025-08-13: set its budget to 400.0 and adjust its bid strategy to lowest_cost exactly as stated in plan_2025-08-13. Evaluate the performance of 2025-08-13 for auditing, preserve the plan snapshot as proof, and furnish a concise CSV with campaign_id, name, plan_id, adset_id, budget, and bid_strategy.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "plan_apply_scored",
                    "input_ref": {
                        "campaign_id": "5",
                        "adset_id": "107",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "5",
                            "name": "Holiday Season Early Bird",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "campaign_id": "5",
                        "name": "Holiday Season Early Bird",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "107",
                        "budget": 400.0,
                        "bid_strategy": "lowest_cost",
                        "ok": true
                    }
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_057",
        "instruction": "Handle the staging of ad set 112 in 'Fall Collection Launch' for QA, effective 2025-08-13, ensuring it is perfectly aligned with plan_2025-08-13. Once changes are applied, validate that the resulting state corresponds with the plan.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 700.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"adset_id\": \"112\"",
                "\"budget\": 700.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_058",
        "instruction": "Coordinate the alignment of 'Holiday Season Early Bird' with the frozen plan for 2025-08-13 by confirming the live allocations for ad sets 106 and 107 match plan_2025-08-13. Review the live state and implement the plan's budget and bidding strategy for each. You will need to verify the adsets.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"budget\": 500.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 18.0",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_059",
        "instruction": "Handle a cross-campaign alignment on 2025-08-13 by updating Global Summer Sale ad set 101 and confirming Holiday Season Early Bird ad set 106 conform to plan_2025-08-13. Validate that both ad sets are synchronized.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"adset_id\": \"106\"",
                "\"budget\": 500.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 18.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_060",
        "instruction": "Coordinate the 'Fall Collection Launch' campaign to comply with the frozen plan for 2025-08-13. Make sure ad sets 104 and 105 mirror plan_2025-08-13 so the budget and bid strategy values align with the plan. Draft a report dated 2025-08-13 with tags ['compliance','fall']. Additionally, export a CSV that lists the compliant ad sets.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "compliance",
                        "fall"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        },
                        {
                            "campaign_id": "3",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 22.0",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_061",
        "instruction": "Align the 'Holiday Season Early Bird' campaign with the frozen plan for 2025-08-13 for ad set 107. Utilize plan_2025-08-13 to ensure the budget and bid are correctly applied, making sure all updates are documented. Retrieve the ad set to verify the update.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_062",
        "instruction": "Create a snapshot of Electronics on ad set 108 for 'Back to School Deals' effective 2025-08-13 by aligning it with plan_2025-08-13 (budget 800.0, bid strategy cost_cap with bid 45.0), confirming the applied state, and crafting two artifacts: a report dated 2025-08-13 and a compact CSV containing fields [campaign_id, plan_id, adset_id, budget, bid_strategy, bid_amount].",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
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
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_063",
        "instruction": "Handle the alignment of the 'Global Summer Sale' campaign with the locked plan for 2025-08-13 for ad set 112. Utilize plan_2025-08-13 as the definitive reference and make sure to apply both budget and bid strategy. Verify the updated condition against the plan and produce a CSV that summarizes the final condition.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 700.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "name": "Global Summer Sale",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"112\"",
                "\"budget\": 700.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_064",
        "instruction": "Coordinate a same-day audit snapshot for 'Back to School Deals' ad sets 108 and 109 as of 2025-08-13, using plan_2025-08-13 as the fixed reference point. You can consult 2025-08-13 insights for additional context; however, no configuration modifications are needed. Provide a succinct CSV with one entry per ad set, including campaign_id, adset_id, and date.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "audit_snapshot",
                    "input_ref": {
                        "campaign_id": "6",
                        "plan_id": "plan_2025-08-13",
                        "adsets": [
                            "108",
                            "109"
                        ],
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "109",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "adset_id": "108",
                            "date": "2025-08-13"
                        },
                        {
                            "campaign_id": "6",
                            "adset_id": "109",
                            "date": "2025-08-13"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "campaign_id": "6",
                        "adset_id_108": "108",
                        "adset_id_109": "109",
                        "ok": true
                    }
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"108\"",
                "\"adset_id\": \"109\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_065",
        "instruction": "Ensure bidding compliance for 'Fall Collection Launch' ad set 105 on 2025-08-13 by documenting strategy lowest_cost for plan_2025-08-13. Supply the CSV.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "strategy_compliance",
                    "input_ref": {
                        "campaign_id": "3",
                        "adset_id": "105",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "name": "Fall Collection Launch",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_066",
        "instruction": "Coordinate 'Holiday Season Early Bird' ad set 107 to align with plan_2025-08-13 as of 2025-08-13: Evaluate the ad set\u2019s 2025-08-13 performance and verify that the final state corresponds to those values.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_067",
        "instruction": "Handle the alignment of ad set 104 in 'Fall Collection Launch' with plan_2025-08-13, ensuring both budget and strategy concur. Anchor this alignment to a frozen plan snapshot and produce a concise CSV containing plan_id and adset_id, accompanied by a dated report.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "104"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_068",
        "instruction": "Coordinate the reconciliation of ad sets 104 and 105 in 'Fall Collection Launch' with the frozen plan dated 2025-08-13 as the authoritative reference. Verify that applied states conform to the plan for 104 (budget 750.0, cost_cap with bid 22.0) and 105 (budget 750.0, lowest_cost). Maintain a compact CSV summary and a dated note.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap"
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap"
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0,
                            "status": "ok"
                        },
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost",
                            "status": "ok"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"adset_id\": \"105\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"status\": \"ok\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_069",
        "instruction": "Handle the alignment of 'Back to School Deals' ad set 111 to the frozen plan plan_2025-08-13 by implementing the plan (budget=1000.0, strategy=cost_cap with bid=2.5), ensuring the live state corresponds correctly, documenting the automation run, and producing a compact CSV receipt containing campaign_id, name, plan_id, adset_id, and bid_strategy.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "plan_execution",
                    "input_ref": {
                        "campaign_id": "6",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "111",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1000.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "111",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 2.5,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "111",
                            "budget": 1000.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "111",
                            "budget": 1000.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "name": "Back to School Deals",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "111",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School Deals\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"111\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_070",
        "instruction": "Coordinate the application of the frozen plan plan_2025-08-13 for ad set 102 within 'Global Summer Sale', making certain its budget and strategy adhere precisely to the plan. Verify the modifications and generate a compact CSV receipt including campaign_id, name, plan_id, adset_id, budget, bid_strategy, and ok.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "plan_execution",
                    "input_ref": {
                        "campaign_id": "1",
                        "adset_id": "102",
                        "plan_id": "plan_2025-08-13"
                    }
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "applied": true,
                        "adset_id": "102",
                        "plan_id": "plan_2025-08-13"
                    }
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "name": "Global Summer Sale",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost",
                            "ok": true
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"102\"",
                "\"budget\": 600.0\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_071",
        "instruction": "Ensure ad set 104 within the 'Fall Collection Launch' campaign matches the frozen plan for 2025-08-13 and verify that both the budget and bid strategy are in harmony.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 22.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_072",
        "instruction": "Match 'Holiday Season Early Bird' to the frozen plan for 2025-08-13 for ad set 107. Implement budget 400.0 and select lowest_cost stating the reason 'plan_2025-08-13', then confirm the status.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_073",
        "instruction": "Handle the reconciliation of the 'Global Summer Sale' campaign with the frozen plan for 2025-08-13. Make sure ad sets 101 and 102 are consistent with plan_2025-08-13, and confirm that the final budgets and bid strategies align. Draft a report dated 2025-08-13 with tags ['apply','verification','gss']. Additionally, export a CSV that summarizes the aligned rows.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "apply",
                        "verification",
                        "gss"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"adset_id\": \"102\"",
                "\"budget\": 600.0",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_074",
        "instruction": "Coordinate the alignment of 'Back to School Deals' ad set 108 with the frozen plan for 2025-08-13. Implement the budget and bid strategy of plan_2025-08-13, and then confirm the values.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School - Laptops\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"bid_strategy\": \"cost_cap\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_075",
        "instruction": "Take charge of aligning the 'Global Summer Sale' ad set 101 with the 2025-08-13 reference plan plan_2025-08-13. Your objective is to achieve a target state with a budget of 950.0 and a cost_cap bid strategy, featuring a bid_amount of 35.0. Success requires the live configuration to match that target and provide auditable proof. Deliverables include a dated note tagged ['alignment'] and a CSV that contains a single receipt row with plan_id, adset_id, budget, bid_strategy, and bid_amount.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "alignment"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_076",
        "instruction": "Ensure the 'Back to School Deals' campaign is aligned with the frozen plan for 2025-08-13 for ad set 111. Confirm that the adset corresponds with the plan, and export a CSV detailing the aligned rows.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "111"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "111",
                    "new_budget": 1000.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "111",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 2.5,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "111",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"111\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_077",
        "instruction": "Ensure implementation of the frozen plan for 'Back to School Deals' dated 2025-08-13 (plan_id 'plan_2025-08-13'). Confirm ad sets 107 and 108 reflect the coordinated states for that date and validate the adjustments.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        },
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost",
                            "bid_amount": null
                        },
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_078",
        "instruction": "Record an audit snapshot for 'Lead Gen - Tech Webinars' on 2025-08-13 associated with plan_2025-08-13. Document weekly sales for category 'Electronics' for the week starting 2025-08-07, conclude the audit process, and generate a dated report along with a CSV receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Lead Gen - Tech Webinars"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "WeeklyCategorySales",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "audit_snapshot",
                    "input_ref": {
                        "plan_id": "plan_2025-08-13"
                    }
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "status": "success",
                    "outputs_json": {
                        "status": "confirmed",
                        "plan_id": "plan_2025-08-13"
                    },
                    "errors_json": {}
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "4",
                            "plan_id": "plan_2025-08-13",
                            "category": "Electronics",
                            "week_start": "2025-08-07"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"4\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"category\": \"Electronics\"",
                "\"week_start\": \"2025-08-07\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_079",
        "instruction": "Launch the 'Global Summer Sale' campaign on 2025-08-13, and verify that ad set 112 aligns with plan_2025-08-13, maintaining its bid strategy as lowest_cost. Proceed to export a concise CSV that records the completed setup with status=active, capturing campaign_id, name, plan_id, adset_id, bid_strategy, and status.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "launch_alignment",
                    "input_ref": {
                        "campaign_id": "1",
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "112",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "LaunchCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "name": "Global Summer Sale",
                            "status": "active",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
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
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"status\": \"active\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"112\"",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_080",
        "instruction": "Initiate a KPI-scored seed creative within 'Back to School Deals' ad set 108 on 2025-08-13, using plan_2025-08-13 as the definitive reference. Formulate a paused image ad called 'ad_108_seed_v1', confirm that the ad set inventory accounts for this sole addition and complies with policies, and then produce a detailed compact CSV receipt along with a dated report.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "seed_creative",
                    "input_ref": {
                        "campaign_id": "6",
                        "adset_id": "108",
                        "name": "ad_108_seed_v1",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "CreateAd",
                "arguments": {
                    "adset_id": "108",
                    "name": "ad_108_seed_v1",
                    "format": "image",
                    "status": "paused"
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "name": "ad_108_seed_v1",
                            "format": "image",
                            "status": "paused"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "name": "ad_108_seed_v1",
                            "format": "image",
                            "status": "paused"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "name",
                        "format",
                        "status"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "adset_id": "108",
                            "name": "ad_108_seed_v1",
                            "format": "image",
                            "status": "paused"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"108\"",
                "\"name\": \"ad_108_seed_v1\"",
                "\"run_2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_081",
        "instruction": "You handle the intended creative rotation for 'Global Summer Sale' ad set 101 starting on 2025-08-13: ad 1102 (video) should be the only ad running and ad 1101 (image) must be paused, following plan_2025-08-13 precisely. Reference the 2025-08-13 insights solely for context\u2014they do not alter the rotation. Provide a compact CSV that includes campaign_id, adset_id, activate_id, pause_id, and date.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "input_ref": {
                        "campaign_id": "1",
                        "adset_id": "101",
                        "plan_id": "plan_2025-08-13",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "CreativeRotationRecorder",
                "arguments": {
                    "ad_id": "1102",
                    "from_creative": "image",
                    "to_creative": "video",
                    "rotation_date": "2025-08-13"
                },
            },
            {
                "name": "ReplaceAdCreatives",
                "arguments": {
                    "activate_id": "1102",
                    "pause_id": "1101"
                },
            },
            {
                "name": "ListAdsetAds",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "101",
                            "active_ads": 1
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "active_ads"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "adset_id": "101",
                            "activate_id": "1102",
                            "pause_id": "1101",
                            "date": "2025-08-13"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "ok": true,
                        "campaign_id": "1",
                        "adset_id": "101"
                    }
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"adset_id\": \"101\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_082",
        "instruction": "Ensure the integrity of 'Global Summer Sale' plan for 2025-08-13, as per plan_2025-08-13. Record evidence of integrity, freeze the plan, and furnish a report tagged with ['integrity','gss'], along with a CSV noting plan_id and plan status.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalcPlanChecksum",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "integrity",
                        "gss"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "Status": "frozen"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_083",
        "instruction": "Coordinate the reconciliation of ad set 102 in the 'Global Summer Sale' campaign with the frozen plan for 2025-08-13, confirm its final state, and generate a one-row CSV receipt containing: campaign_id, plan_id, adset_id, adset_name, budget, bid_strategy.",
        "actions": [
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "102",
                            "daily_budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "102",
                            "daily_budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "daily_budget",
                        "bid_strategy"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "102",
                            "adset_name": "Apparel - CA",
                            "budget": 600.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"102\"",
                "\"adset_name\": \"Apparel - CA\"",
                "\"budget\": 600.0\"",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_084",
        "instruction": "Align the 'Global Summer Sale' campaign with the frozen plan dated 2025-08-13 for ad set 112. Make sure the budget is set to 700.0 and the bid strategy is lowest_cost, applying and confirming these settings.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "112",
                    "new_budget": 700.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"112\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_085",
        "instruction": "Coordinate the reconciliation of 'Fall Collection Launch' with the frozen plan dated 2025-08-13 for ad set 105. Assign a budget of 750.0 and use lowest_cost, citing 'plan_2025-08-13' as the reason, ensuring the values align.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "105",
                            "budget": 750.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"105\"",
                "\"bid_strategy\": \"lowest_cost\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_086",
        "instruction": "Compile documentation for the daily insight regarding 'Back to School Deals' ad set 108 on 2025-08-13 by retrieving insights from that day and linking them to the frozen plan of that date. Prepare a one-row CSV and compose a date-specific report.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "insight_anchor",
                    "input_ref": {
                        "plan_id": "plan_2025-08-13",
                        "adset_id": "108",
                        "date": "2025-08-13"
                    }
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {}
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "6",
                            "adset_id": "108",
                            "date": "2025-08-13",
                            "plan_id": "plan_2025-08-13"
                        }
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"adset_id\": \"108\"",
                "\"date\": \"2025-08-13\"",
                "\"plan_id\": \"plan_2025-08-13\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_087",
        "instruction": "Initiate an automation run on 2025-08-13 to reconcile 'Global Summer Sale' ad sets 101 and 102 with plan_2025-08-13, and afterward conclude the run.",
        "actions": [
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "reconcile",
                    "input_ref": {
                        "plan_id": "plan_2025-08-13",
                        "adsets": [
                            "101",
                            "102"
                        ]
                    }
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "102"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "102",
                    "new_budget": 600.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "102",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "CompleteAutomationRun",
                "arguments": {
                    "run_id": "run_2025-08-13",
                    "errors_json": {},
                    "outputs_json": {
                        "run_id": "run_2025-08-13",
                        "plan_id": "plan_2025-08-13",
                        "adset_ids": [
                            "101",
                            "102"
                        ]
                    }
                }
            }
        ],
        "outputs": [
                "\"run_id\": \"run_2025-08-13\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_ids\": [\"101\", \"102\"]"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_088",
        "instruction": "Align 'Global Summer Sale' ad set 101 with the frozen plan for 2025-08-13, document daily health (including ROAS), and produce the CSV artifact containing the campaign name 'Global Summer Sale'.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ComputeRoas",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "adset_id": "101",
                            "name": "Global Summer Sale",
                            "roas": 10.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"roas\": 10.0",
                "\"adset_id\": \"101\"",
                "\"name\": \"Global Summer Sale\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_089",
        "instruction": "Handle the 'Fall Collection Launch' campaign to ensure it aligns with the fixed plan for 2025-08-13 for ad set 104. Utilize plan_2025-08-13 and make certain that budget and bid are enforced, while documenting all updates. Retrieve the ad set to verify the update.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "104"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 22.0"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_090",
        "instruction": "Coordinate the alignment of the 'Brand - Video Ads' ad set (id 103) in 'Q3 Brand Awareness Push' with 'plan_2025-08-13' to ensure the aligned state accurately mirrors both the budget and strategy. Evaluate delivery on 2025-08-13 to meet at least 1,500 impressions, and document any shortfall as an exception. Prepare an auditable CSV detailing the exception context.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Q3 Brand Awareness Push"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "2"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "103",
                    "new_budget": 1200.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "103",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetDailyAdsetInsights",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExceptionRaiser",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "insights": [
                        {
                            "adset_id": "103",
                            "impressions": 0,
                            "spend": 0.0,
                            "missing_days": 0
                        }
                    ],
                    "rules": {
                        "zero_delivery_impressions": 1500
                    }
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "103",
                            "alert": "zero_delivery"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"2\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"103\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_091",
        "instruction": "Coordinate a maintenance toggle for 'Fall Collection Launch' on 2025-08-13 to synchronize ad set 104 with plan_2025-08-13. Ensure that the campaign concludes as paused and provide a compact CSV configuration receipt.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "HaltCampaign",
                "arguments": {
                    "campaign_id": "3",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "status": "paused",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "104",
                            "bid_strategy": "cost_cap"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"status\": \"paused\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"bid_strategy\": \"cost_cap\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_092",
        "instruction": "Align ad set 106 in 'Holiday Season Early Bird' with plan_2025-08-13 and verify that the applied state corresponds to the plan.",
        "actions": [
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"budget\": 500.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 18.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_093",
        "instruction": "Handle the review of the 'Fall Collection Launch' campaign on 2025-08-13 for adset 104. Make sure the ad budget, bid strategy, and bid are aligned with plan_2025-08-13. Compose a report and export it as a CSV.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "3",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "104",
                            "budget": 750.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 22.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"name\": \"Fall Collection Launch\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"104\"",
                "\"budget\": 750.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 22.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_094",
        "instruction": "Coordinate the re-affirmation of 'Holiday Season Early Bird' ad set 106 to plan_id 'plan_2025-08-13' on 2025-08-13, ensuring the budget and bid are enforced. Then, confirm the applied state.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "106"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "106",
                    "new_budget": 500.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "106",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 18.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "106",
                            "budget": 500.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"106\"",
                "\"budget\": 500.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 18.0",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_095",
        "instruction": "Handle the confirmation of compliance for 'Global Summer Sale' ad set 101 on 2025-08-13. Ensure adset 101 is aligned according to plan_id 'plan_2025-08-13' and export the data as a CSV file.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_096",
        "instruction": "Ensure there is full alignment for 'Global Summer Sale' by 2025-08-13. With plan_2025-08-13 serving as the reference, guarantee that ad sets 101 and 112 are in sync with plan strategies. Record the alignment in a report, tagging it with ['alignment','gss'], and export a CSV of the aligned rows.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Global Summer Sale"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "101"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "101",
                    "new_budget": 950.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "101",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 35.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "112"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "112",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GenerateReport",
                "arguments": {
                    "date": "2025-08-13",
                    "tags": [
                        "alignment",
                        "gss"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "101",
                            "budget": 950.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 35.0
                        },
                        {
                            "campaign_id": "1",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "112",
                            "budget": 700.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"1\"",
                "\"name\": \"Global Summer Sale\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"101\"",
                "\"budget\": 950.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 35.0",
                "\"adset_id\": \"112\"",
                "\"budget\": 700.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_097",
        "instruction": "Handle the update of ad set 108 within 'Back to School Deals' according to the plan for 2025-08-13 and confirm that the current state is accurate.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"name\": \"Back to School Deals\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_098",
        "instruction": "Coordinate the execution of the frozen plan plan_2025-08-13 for 'Fall Collection Launch' on 2025-08-13 across ad sets 104 and 105. Use a checksum and frozen plan to ensure stability, apply the plan\u2019s budget and bidding strategy to both ad sets, and validate the application status.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Fall Collection Launch"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "CalcPlanChecksum",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "LockPlan",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "OpenAutomationRun",
                "arguments": {
                    "run_type": "execution_with_audit",
                    "input_ref": {
                        "plan_id": "plan_2025-08-13",
                        "campaign_id": "3",
                        "adsets": [
                            "104",
                            "105"
                        ]
                    }
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "104"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "104",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "104",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 22.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "105"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "105",
                    "new_budget": 750.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "105",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "plan_id": "plan_2025-08-13"
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"3\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"run_id\": \"run_2025-08-13\"",
                "\"ok\": true"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_099",
        "instruction": "Ensure the 'Holiday Season Early Bird' campaign aligns with the frozen plan for 2025-08-13 concerning ad set 107. Utilize plan_2025-08-13, confirming the application of budget and bid strategy. Generate a CSV outlining the final state.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Holiday Season Early Bird"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "107"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "107",
                    "new_budget": 400.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "107",
                    "bid_strategy": "lowest_cost",
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
                    "rows": [
                        {
                            "campaign_id": "5",
                            "name": "Holiday Season Early Bird",
                            "plan_id": "plan_2025-08-13",
                            "adset_id": "107",
                            "budget": 400.0,
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"5\"",
                "\"name\": \"Holiday Season Early Bird\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"107\"",
                "\"budget\": 400.0",
                "\"bid_strategy\": \"lowest_cost\""
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "task_100",
        "instruction": "Verify adherence to the plan for 'Back to School Deals' on 2025-08-13, adjusting only the zero-delivery ad set. Confirm that ad set 108 complies with plan_2025-08-13 without altering ad sets not allocated in the plan. Export a CSV as a record.",
        "actions": [
            {
                "name": "GetCampaign",
                "arguments": {
                    "name": "Back to School Deals"
                },
            },
            {
                "name": "ListAdsetsInCampaign",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "GetPlanOnDate",
                "arguments": {
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FindAdsetInPlan",
                "arguments": {
                    "plan_id": "plan_2025-08-13",
                    "adset_id": "108"
                },
            },
            {
                "name": "SetAdsetBudget",
                "arguments": {
                    "adset_id": "108",
                    "new_budget": 800.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "UpdateAdsetStrategy",
                "arguments": {
                    "adset_id": "108",
                    "bid_strategy": "cost_cap",
                    "bid_amount": 45.0,
                    "reason": "plan_2025-08-13"
                },
            },
            {
                "name": "GetAdset",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "AppliedStateVerifier",
                "arguments": {
                    "expected_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "actual_rows": [
                        {
                            "adset_id": "108",
                            "budget": 800.0,
                            "bid_strategy": "cost_cap",
                            "bid_amount": 45.0
                        }
                    ],
                    "key_fields": [
                        "adset_id",
                        "budget",
                        "bid_strategy",
                        "bid_amount"
                    ]
                },
            },
            {
                "name": "ExportReportToCsv",
                "arguments": {
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
                }
            }
        ],
        "outputs": [
                "\"campaign_id\": \"6\"",
                "\"plan_id\": \"plan_2025-08-13\"",
                "\"adset_id\": \"108\"",
                "\"budget\": 800.0",
                "\"bid_strategy\": \"cost_cap\"",
                "\"bid_amount\": 45.0"
        ]
    }
]
