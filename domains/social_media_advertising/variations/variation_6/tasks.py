# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "TASK_01",
        "instruction": "As the Snapshot Planner at 2025-08-14T00:00:00Z, prepare plan_soc_001 (date 2025-08-13) utilizing the exact adset names from the DB as a full-fidelity envelope; ensure totals remain unchanged. Implement and document the process.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_001",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T00:00:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8860.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_001",
                    "timestamp": "2025-08-14T00:00:00Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_001",
                    "status": "applied",
                    "applied_at": "2025-08-14T00:00:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T00:00:00Z",
                    "ended_at": "2025-08-14T00:00:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_001",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T00:00:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_001\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T00:00:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_02",
        "instruction": "Acting as the Envelope Publisher at 2025-08-14T00:03:00Z, release plan_soc_002 (date 2025-08-13) as a precise DB snapshot (unchanged), including full adset mapping, strategies (like cost caps), creatives, and allocations. Execute and document accordingly.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_002",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T00:03:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8860.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_002",
                    "timestamp": "2025-08-14T00:03:00Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_002",
                    "status": "applied",
                    "applied_at": "2025-08-14T00:03:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T00:03:00Z",
                    "ended_at": "2025-08-14T00:03:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_002",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T00:03:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_002\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T00:03:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_03",
        "instruction": "As the Allocation Analyst at 2025-08-14T00:06:00Z, prepare plan_soc_003 (dated 2025-08-13) as a complete envelope using the precise adset names from the DB; retain totals and refrain from making changes. Execute and document.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_003",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T00:06:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8860.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_003",
                    "timestamp": "2025-08-14T00:06:00Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_003",
                    "status": "applied",
                    "applied_at": "2025-08-14T00:06:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T00:06:00Z",
                    "ended_at": "2025-08-14T00:06:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_003",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T00:06:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_003\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T00:06:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_04",
        "instruction": "Serving as the Baseline Publisher at 2025-08-14T00:30:00Z, release plan_soc_010 (2025-08-13) as an unaltered snapshot of current budgets/strategies, ensuring the total (8860) is maintained without modifications. Implement and log.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_010",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T00:30:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8860.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_010",
                    "timestamp": "2025-08-14T00:30:00Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_010",
                    "status": "applied",
                    "applied_at": "2025-08-14T00:30:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T00:30:00Z",
                    "ended_at": "2025-08-14T00:30:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_010",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T00:30:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_010\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T00:30:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_05",
        "instruction": "As the Creative Provisioner, the date is 2025-08-14T00:35:00Z. In adset 102, arrange for one new active image ad (commencing 2025-08-14), maintain single-active status by pausing any current active ad, and document the execution.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "CreateAd",
                "arguments": {
                    "adset_id": "102",
                    "name": "auto_102_20250814_001",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "request_id": "en-1"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1103",
                    "status": "paused",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T00:35:00Z",
                    "ended_at": "2025-08-14T00:37:00Z",
                    "status": "completed",
                    "input_ref": "en-1",
                    "outputs_json": {
                        "adset_id": "102",
                        "ads_created_count": 1,
                        "new_ad_name": "auto_102_20250814_001",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"102\"",
                "\"ads_created_count\": \"1\"",
                "\"new_ad_name\": \"auto_102_20250814_001\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_06",
        "instruction": "Act as the Envelope Publisher, with the date being 2025-08-14T00:30:00Z. Release plan_soc_006a (dated 2025-08-13) as a comprehensive envelope snapshot of the present DB (budgets, bid strategies, creatives), ensuring the total remains (8860) and all policy constraints are upheld. Retain adset names unchanged from the DB and apply deterministic defaults.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_006a",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T00:30:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8860.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_006a",
                    "timestamp": "2025-08-14T00:30:00Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_006a"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_006a",
                    "status": "applied",
                    "applied_at": "2025-08-14T00:30:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T00:30:00Z",
                    "ended_at": "2025-08-14T00:30:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_006a",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T00:30:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_006a\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T00:30:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_07",
        "instruction": "You are the Revenue Planner and the date is 2025-08-14T01:17:30Z. Formulate plan_soc_005 (2025-08-13) to shift 50 units from the lower-ROAS to higher-ROAS categories between Electronics and Mobile; modify only the bottom donor and top recipient adsets, leaving others unchanged. Assess category lift using adset-level ROAS on 2025-08-13 (donor = lowest-ROAS Mobile adset, recipient = highest-ROAS Electronics adset). Maintain the overall total (8860) and adhere to policy constraints, using the adset names exactly as they appear in the DB.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_005",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:17:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8860.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 950.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 750.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_005",
                    "timestamp": "2025-08-14T01:17:30Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_005"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_005",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:17:30Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:17:30Z",
                    "ended_at": "2025-08-14T01:17:30Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_005",
                        "applied_adsets_count": 2,
                        "total_budget": 8860.0,
                        "applied_at": "2025-08-14T01:17:30Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_005\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T01:17:30Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\"",
                "\"total_budget\": \"8860.0\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_08",
        "instruction": "Acting as the Apparel Portfolio Owner at 2025-08-14T01:20:30Z, devise plan_soc_006 (2025-08-13) exclusively for Apparel: reduce by \u221225 from any adset with CPA>45 and allocate the freed budget evenly to peers with CPA<25 in accordance with policy rounding. If there are no donors, execute a no-op.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_006",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:20:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 2080.0,
                    "adset_mapping": [
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_006",
                    "timestamp": "2025-08-14T01:20:30Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_006",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:20:30Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:20:30Z",
                    "ended_at": "2025-08-14T01:20:30Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_006",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T01:20:30Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_006\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T01:20:30Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_09",
        "instruction": "As the Bidding Architect with the current time at 2025-08-14T01:24:30Z, handle the preparation of plan_soc_007 for 2025-08-13. Set adset 106 to have a cost_cap of 18.0 and adset 111 to a cost_cap of 2.5, ensuring the rest of the strategies and budgets remain constant; maintain the totals for each category. Utilize the adset names directly from the database, and for any necessary timestamps, apply the seed time precisely.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_007",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:24:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 1500.0,
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_007",
                    "timestamp": "2025-08-14T01:24:30Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_007"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_007",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:24:30Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:24:30Z",
                    "ended_at": "2025-08-14T01:24:30Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_007",
                        "applied_adsets_count": 0,
                        "applied_adsets": [],
                        "applied_at": "2025-08-14T01:24:30Z",
                        "run_status": "completed",
                        "total_budget": 1500.0
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_007\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T01:24:30Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_10",
        "instruction": "As the Creative Rotation Owner with the current time noted as 2025-08-14T01:28:00Z, coordinate the switch of adsets 103 and 107 to video format (justification 'video consistency for single-active'), enforce single-active status, and document the execution. Conclude by 2025-08-14T01:29:00Z (rot-003).",
        "actions": [
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T01:28:00Z",
                    "ended_at": "2025-08-14T01:29:00Z",
                    "status": "completed",
                    "input_ref": "rot-003",
                    "outputs_json": {
                        "rotation_request_id": "rot-003",
                        "target_type": "video",
                        "rotated_adsets": [],
                        "rotated_adsets_count": 0,
                        "skipped": [
                            {
                                "adset_id": "103",
                                "reason": "already_video"
                            },
                            {
                                "adset_id": "107",
                                "reason": "already_video"
                            }
                        ],
                        "single_active_enforced": true,
                        "rationale": "video consistency for single-active"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-003\"",
                "\"rotated_adsets_count\": \"0\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T01:29:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_11",
        "instruction": "As the Envelope Planner, at 2025-08-14T01:30:00Z, prepare env_soc_008 for the date 2025-08-13, ensuring min_per_category = 100 and that the total remains unchanged. In the Home category, increase the top 7-day sales adset (adset 106) by 30, compensating by reducing Brand - Video Ads (adset 103) by 30; all other adsets should remain as they are. Utilize adset names directly from the database. Set operation timestamps to 2025-08-14T01:32:00Z (apply) and 2025-08-14T01:34:00Z (mark applied), based on the initial seed time.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-07"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-08"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-09"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-10"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-11"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-12"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "env_soc_008",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:30:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 1680.0,
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 530.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1150.0
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "env_soc_008",
                    "timestamp": "2025-08-14T01:32:00Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "env_soc_008"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "env_soc_008",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:34:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:32:00Z",
                    "ended_at": "2025-08-14T01:34:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "env_soc_008",
                        "applied_adsets_count": 2,
                        "applied_adsets": [
                            "103",
                            "106"
                        ],
                        "total_budget": 1680.0,
                        "applied_at": "2025-08-14T01:34:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"env_soc_008\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T01:34:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\"",
                "\"total_budget\": \"1680.0\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_12",
        "instruction": "Act as the Efficiency Lead at 2025-08-14T01:35:00Z. Arrange plan_soc_009 for 2025-08-13 to transfer \u221240 from image adsets with a CPA above 60 to video adsets with CPAs under 25, within the same categories, while maintaining the total for each category. If no suitable donor and recipient pairs exist in a category, create a no-op envelope that retains all existing budgets and strategies, and document deterministic reasons for any no-op outcomes in the run metadata. Adhere to the timing window starting at 2025-08-14T01:36:30Z and ending at 2025-08-14T01:38:00Z, and use the request id ap-1.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "107",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "109",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_009",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:35:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 8560.0,
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 400.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_009",
                    "timestamp": "2025-08-14T01:36:30Z",
                    "request_id": "ap-1"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_009"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_009",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:38:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:36:30Z",
                    "ended_at": "2025-08-14T01:38:00Z",
                    "status": "completed",
                    "input_ref": "ap-1",
                    "outputs_json": {
                        "plan_id": "plan_soc_009",
                        "applied_adsets_count": 0,
                        "applied_adsets": [],
                        "applied_at": "2025-08-14T01:38:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_009\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T01:38:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_13",
        "instruction": "As the Electronics Fine Tuner, the current time is 2025-08-14T05:00:00Z. Release plan_soc_054 for the date 2025-08-13: adjust shift 20 from adset 101 to adset 112 within Electronics ensuring the category total remains constant; retain existing strategies and replicate current creatives. Reference created_at 2025-08-14T05:00:00Z, implement at 2025-08-14T05:02:00Z (request_id ap-052), and assume the plan is applied at 2025-08-14T05:03:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_054",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T05:00:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 900.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 720.0
                        }
                    ],
                    "total_budget": 1620.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_054",
                    "timestamp": "2025-08-14T05:02:00Z",
                    "request_id": "ap-052"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_054"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_054",
                    "status": "applied",
                    "applied_at": "2025-08-14T05:03:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T05:02:00Z",
                    "ended_at": "2025-08-14T05:03:00Z",
                    "status": "completed",
                    "request_id": "ap-052",
                    "input_ref": "ap-052",
                    "outputs_json": {
                        "plan_id": "plan_soc_054",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T05:03:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_054\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T05:03:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_14",
        "instruction": "As the Q3 Video Uplift Lead, it is now 2025-08-14T05:10:00Z. Transition adsets 104 and 107 to video format at 2025-08-14T05:10:00Z using rotation request_id rot-018 with the justification 'Q3 video uplift'. Maintain a single-active status. If an adset is already in the video format, handle it as a no-op and document the reason as 'already_in_target_state'. Mark the process as complete at 2025-08-14T05:11:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T05:10:00Z",
                    "request_id": "rot-018",
                    "rationale": "Q3 video uplift",
                    "ad_name": "rot-018-104-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T05:10:00Z",
                    "ended_at": "2025-08-14T05:11:00Z",
                    "status": "completed",
                    "request_id": "rot-018",
                    "input_ref": "rot-018",
                    "outputs_json": {
                        "rotation_request_id": "rot-018",
                        "rotated_adsets_count": 1,
                        "rotation_noops": [
                            {
                                "adset_id": "107",
                                "reason": "already_in_target_state"
                            }
                        ],
                        "run_status": "completed",
                        "ended_at": "2025-08-14T05:11:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-018\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_15",
        "instruction": "Act as the Apparel Level-Setter as of 2025-08-14T01:47:00Z. Organize plan_soc_011 (date 2025-08-13) to align Apparel budgets to the category average (rounded to whole numbers) while keeping other non-Apparel categories untouched. Adhere to the timing window from start=2025-08-14T01:49:00Z to end=2025-08-14T01:50:00Z, and apply request id ap-010 for consistent audit tracking. Maintain current strategies and creatives unless a policy stipulates otherwise.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_011",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:47:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 2080.0,
                    "adset_mapping": [
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 1,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "102",
                            "budget": 693.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 693.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 694.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_011",
                    "timestamp": "2025-08-14T01:49:00Z",
                    "request_id": "ap-010"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_011"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_011",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:50:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:49:00Z",
                    "ended_at": "2025-08-14T01:50:00Z",
                    "status": "completed",
                    "input_ref": "ap-010",
                    "outputs_json": {
                        "plan_id": "plan_soc_011",
                        "applied_adsets_count": 3,
                        "applied_at": "2025-08-14T01:50:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_011\"",
                "\"applied_adsets_count\": \"3\"",
                "\"applied_at\": \"2025-08-14T01:50:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_16",
        "instruction": "Serve as the Toys Expansion Owner with the current time being 2025-08-14T01:51:00Z. Establish the 'Toys \u2014 Expansion' adset (adset_id '141') within campaign_id '5' with a daily_budget of 220, the bid_strategy set to lowest_cost, and status marked as active; ensure the creation of precisely one active video ad called 'Toys \u2014 Expansion Video v1' with the deterministic ad_id '14101'. The adset should conclude having a single active ad. Treat the provisioning run as commencing at 2025-08-14T01:51:00Z and finishing at 2025-08-14T01:53:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "141",
                        "campaign_id": "5",
                        "name": "Toys — Expansion",
                        "category": "Toys",
                        "daily_budget": 220.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T01:51:00Z"
                    },
                    "timestamp": "2025-08-14T01:51:00Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "14101",
                        "adset_id": "141",
                        "name": "Toys — Expansion Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T01:51:00Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T01:51:00Z",
                    "ended_at": "2025-08-14T01:53:00Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "141",
                        "new_ad_id": "14101",
                        "ads_created": 1,
                        "final_type": "video",
                        "single_active_enforced": true,
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"141\"",
                "\"ads_created\": \"1\"",
                "\"new_ad_id\": \"14101\"",
                "\"final_type\": \"video\"",
                "\"single_active_enforced\": \"True\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_17",
        "instruction": "As the Bid Policy Curator, the current time is 2025-08-14T01:54:00Z. Draft plan_soc_012 (2025-08-13) to (i) change any cost_cap where bid_amount is less than 5 to lowest_cost, and (ii) redistribute +20 within Electronics by allocating it to the highest-ROAS Electronics adset and deducting \u221220 from the lowest-ROAS Electronics adset, both based on insights from 2025-08-13; ensure category totals remain unchanged. Note audit markers at 2025-08-14T01:56:00Z (ap-011) and 2025-08-14T01:57:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_012",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:54:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "total_budget": 2620.0,
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 900.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 720.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "lowest_cost"
                        }
                    ]
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_012",
                    "timestamp": "2025-08-14T01:56:00Z",
                    "request_id": "ap-011"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_012"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_012",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:57:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:56:00Z",
                    "ended_at": "2025-08-14T01:57:00Z",
                    "status": "completed",
                    "input_ref": "ap-011",
                    "outputs_json": {
                        "plan_id": "plan_soc_012",
                        "applied_adsets_count": 3,
                        "applied_at": "2025-08-14T01:57:00Z",
                        "run_status": "completed",
                        "total_budget": 2620.0
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_012\"",
                "\"applied_adsets_count\": \"3\"",
                "\"applied_at\": \"2025-08-14T01:57:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_18",
        "instruction": "Acting as the Creative Harmonizer, the time is now 2025-08-14T01:58:00Z. Change adset 110 to use an image and adset 112 to use a video, ensuring there is only one active creative per adset. Adhere to rotation request_id rot-004 with the reasoning 'align with 7-day winners'. Log completion with ended_at 2025-08-14T02:00:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "110",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T01:58:00Z",
                    "request_id": "rot-004",
                    "rationale": "align with 7-day winners",
                    "ad_name": "rot-004-110-image"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T01:58:00Z",
                    "request_id": "rot-004",
                    "rationale": "align with 7-day winners",
                    "ad_name": "rot-004-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T01:58:00Z",
                    "ended_at": "2025-08-14T02:00:00Z",
                    "status": "completed",
                    "request_id": "rot-004",
                    "input_ref": "rot-004",
                    "outputs_json": {
                        "rotation_request_id": "rot-004",
                        "rotated_adsets_count": 2,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T02:00:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-004\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T02:00:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_19",
        "instruction": "Assume the role of Cross-Category Balancer and the current time is 2025-08-14T02:00:30Z. Release plan_soc_013 for the date 2025-08-13. For Mobile (adsets 110, 111), increase by +15 for each adset with a CPA on 2025-08-13 of less than 25; offset these increases by decreasing \u221215 from Electronics donors among (101, 108, 112) where the CPA on 2025-08-13 exceeds 50. Maintain the minimum per-category of 100 and ensure category totals remain steady. If no Electronics donors match CPA > 50, create a no-op snapshot that reflects current budgets, strategies, and active creative types for adsets 101, 108, 110, 111, 112. Utilize apply timestamp 2025-08-14T02:02:00Z with request_id ap-012 and regard the plan as applied at 2025-08-14T02:04:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_013",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:00:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 4400.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_013",
                    "timestamp": "2025-08-14T02:02:00Z",
                    "request_id": "ap-012"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_013"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_013",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:04:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:02:00Z",
                    "ended_at": "2025-08-14T02:04:00Z",
                    "status": "completed",
                    "input_ref": "ap-012",
                    "outputs_json": {
                        "plan_id": "plan_soc_013",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T02:04:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_013\"",
                "\"applied_adsets_count\": 0",
                "\"applied_at\": \"2025-08-14T02:04:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_20",
        "instruction": "Act as the Seasonal Merchandiser with the time being 2025-08-14T02:05:00Z. Set up a new Apparel adset (adset_id 126) called 'Apparel \u2014 Seasonal' under campaign_id '3' with a daily_budget of 260, bid_strategy of lowest_cost, and status active. Make sure an active image ad is initiated on 2025-08-14 named 'Apparel \u2014 Seasonal Image v1'. Change the adset's active creative to video using rotation request_id rot-001, designate the new ad as rot-001-126-video, and provide rationale as 'seasonal refresh'.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "126",
                        "campaign_id": "3",
                        "name": "Apparel — Seasonal",
                        "category": "Apparel",
                        "daily_budget": 260.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T02:05:00Z"
                    },
                    "timestamp": "2025-08-14T02:05:00Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_126_20250814_1",
                        "adset_id": "126",
                        "name": "Apparel — Seasonal Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T02:05:00Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "126",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:05:00Z",
                    "request_id": "rot-001",
                    "rationale": "seasonal refresh",
                    "ad_name": "rot-001-126-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:05:00Z",
                    "ended_at": "2025-08-14T02:07:00Z",
                    "status": "completed",
                    "request_id": "rot-001",
                    "input_ref": "rot-001",
                    "outputs_json": {
                        "rotation_request_id": "rot-001",
                        "rotated_adsets_count": 1,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T02:07:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-001\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T02:07:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_21",
        "instruction": "Assume the role of Rounding Guardian and the current time is 2025-08-14T02:07:00Z. Release plan_soc_014 for the date of 2025-08-13. Ensure that cost_cap bids are standardized to whole numbers and adjust the budgets so that the total for each category remains unchanged. Focus only on adsets 111 (Mobile) and 106 (Home). Alter adset 111 cost_cap bid from 2.5 to 2.0; maintain adset 106 at 18.0. Keep budgets unchanged for both adsets. Utilize created_at 2025-08-14T02:07:00Z. Apply a timestamp of 2025-08-14T02:09:00Z with request_id ap-013, ensure verification pass compliance, and acknowledge the plan as implemented at 2025-08-14T02:10:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_014",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:07:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.0
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ],
                    "total_budget": 1500.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_014",
                    "timestamp": "2025-08-14T02:09:00Z",
                    "request_id": "ap-013"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_014"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_014",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:10:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:09:00Z",
                    "ended_at": "2025-08-14T02:10:00Z",
                    "status": "completed",
                    "input_ref": "ap-013",
                    "outputs_json": {
                        "plan_id": "plan_soc_014",
                        "applied_adsets_count": 1,
                        "applied_at": "2025-08-14T02:10:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_014\"",
                "\"applied_adsets_count\": \"1\"",
                "\"applied_at\": \"2025-08-14T02:10:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_22",
        "instruction": "Take on the responsibilities of Video Rollout Owner and note the current time is 2025-08-14T02:11:00Z. Transition adsets 104 and 108 to video format at 2025-08-14T02:11:00Z, permitting only one active creative per adset. Verify adset 111's existing creative type from the database; if it is already in video format on 2025-08-13, refrain from rotating and exclude it from the count. Use rotation request_id rot-008-triad and designate the new ads as rot-008-<adset_id>-video (for instance, rot-008-104-video, rot-008-108-video). Apply the reasoning 'align to video winners' and recognize the rotation as accomplished at 2025-08-14T02:12:30Z.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:11:00Z",
                    "request_id": "rot-008-triad",
                    "rationale": "align to video winners",
                    "ad_name": "rot-008-104-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "108",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:11:00Z",
                    "request_id": "rot-008-triad",
                    "rationale": "align to video winners",
                    "ad_name": "rot-008-108-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:11:00Z",
                    "ended_at": "2025-08-14T02:12:30Z",
                    "status": "completed",
                    "request_id": "rot-008-triad",
                    "input_ref": "rot-008-triad",
                    "outputs_json": {
                        "rotation_request_id": "rot-008-triad",
                        "rotated_adsets_count": 2,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T02:12:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-008-triad\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T02:12:30Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_23",
        "instruction": "As the Waste Trimmer, the current time is 2025-08-14T02:13:00Z. Publish plan_soc_015 for the date 2025-08-13. If an adset is paused, adjust its budget to 0 and distribute the freed budget EQUALLY among active peers within the SAME category, ensuring rounding is according to the policy budget_rounding_unit; do not alter other categories. In cases where there are no active peers in that category, issue a NO-OP snapshot for the adset (no redistribution). For Office, verify that adset 109 has no active peers and maintain its budget as is. The created_at time is 2025-08-14T02:13:00Z. Implement at 2025-08-14T02:15:00Z with request_id ap-014, ensure verification before finalizing, and recognize the plan as applied at 2025-08-14T02:16:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_015",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:13:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "109",
                            "name": "Back to School - Stationery",
                            "category": "Office",
                            "campaign_id": "6"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "109",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "109",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "109",
                            "budget": 300.0
                        }
                    ],
                    "total_budget": 300.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_015",
                    "timestamp": "2025-08-14T02:15:00Z",
                    "request_id": "ap-014"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_015"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_015",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:16:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:15:00Z",
                    "ended_at": "2025-08-14T02:16:00Z",
                    "status": "completed",
                    "request_id": "ap-014-rec",
                    "input_ref": "ap-014",
                    "outputs_json": {
                        "plan_id": "plan_soc_015",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T02:16:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_015\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T02:16:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_24",
        "instruction": "In the role of Electronics Normalizer, the current time is 2025-08-14T02:18:30Z. Release plan_soc_016 for the date 2025-08-13 to align Electronics budgets toward the median while keeping the category total intact: configure adset 112 to 780, adjust adset 101 to 840, and keep adset 108 unchanged; other categories remain as they are. The created_at timestamp is 2025-08-14T02:18:30Z. Schedule the application for 2025-08-14T02:20:00Z with request_id ap-015, mandate a verification check, and regard the plan as applied at 2025-08-14T02:21:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_016",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:18:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 840.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 780.0
                        }
                    ],
                    "total_budget": 1620.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_016",
                    "timestamp": "2025-08-14T02:20:00Z",
                    "request_id": "ap-015"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_016"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_016",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:21:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:20:00Z",
                    "ended_at": "2025-08-14T02:21:00Z",
                    "status": "completed",
                    "input_ref": "ap-015",
                    "outputs_json": {
                        "plan_id": "plan_soc_016",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T02:21:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_016\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T02:21:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_25",
        "instruction": "As the Media Ops Coordinator and with the current time being 2025-08-14T01:15:00Z, handle the provisioning of a new adset (adset_id 120) named 'Electronics \u2014 Promo' within campaign_id '6'. The category should be Electronics, daily_budget set to 300, bid_strategy as lowest_cost, and status active. Verify that exactly one active image ad is available starting 2025-08-14 named 'Electronics Promo V1' using the deterministic ad_id auto_120_20250814_1. The creation timestamp is 2025-08-14T01:15:00Z, and the provisioning window spans 2025-08-14T01:15:00Z\u20132025-08-14T01:17:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "120",
                        "campaign_id": "6",
                        "name": "Electronics — Promo",
                        "category": "Electronics",
                        "daily_budget": 300.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "created_at": "2025-08-14T01:15:00Z",
                        "updated_at": "2025-08-14T01:15:00Z"
                    },
                    "timestamp": "2025-08-14T01:15:00Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_120_20250814_1",
                        "adset_id": "120",
                        "name": "Electronics Promo V1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T01:15:00Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T01:15:00Z",
                    "ended_at": "2025-08-14T01:17:00Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "120",
                        "ads_created": 1,
                        "final_type": "image",
                        "run_type": "provisioning",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"120\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"image\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_26",
        "instruction": "In your role as the Policy-Driven Planner with the current time noted as 2025-08-14T01:41:00Z, coordinate the publication of plan_soc_010 for the date 2025-08-13 focusing on Mobile. Ensure a per-category minimum of 200: precisely increase Mobile by 60, dividing it equally by setting adsets 110 and 111 to 1030 each. This adjustment should be entirely funded from adset 103 (All), reducing it to 1120, while keeping all other categories unchanged. Use the created_at timestamp 2025-08-14T01:41:00Z. The apply timestamp should be 2025-08-14T01:43:00Z with request_id ap-009, necessitate a verification pass, and regard the plan as applied at 2025-08-14T01:44:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_010",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T01:41:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1120.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1030.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1030.0
                        }
                    ],
                    "total_budget": 3180.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_010",
                    "timestamp": "2025-08-14T01:43:00Z",
                    "request_id": "ap-009"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_010"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_010",
                    "status": "applied",
                    "applied_at": "2025-08-14T01:44:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T01:43:00Z",
                    "ended_at": "2025-08-14T01:44:00Z",
                    "status": "completed",
                    "input_ref": "ap-009",
                    "outputs_json": {
                        "plan_id": "plan_soc_010",
                        "applied_adsets_count": 3,
                        "applied_at": "2025-08-14T01:44:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_010\"",
                "\"applied_adsets_count\": \"3\"",
                "\"applied_at\": \"2025-08-14T01:44:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_27",
        "instruction": "Act as the Zero-Purchase Controller with the current time of 2025-08-14T02:23:30Z. Announce plan_soc_017 for the date 2025-08-13. For any adset that shows purchases=0 on 2025-08-13, decrease its budget by 20 and proportionally reallocate the total deductions within that adset's category according to clicks, rounding to the policy budget_rounding_unit, ensuring each category\u2019s total remains unchanged. If a zero-purchase adset stands alone in its category, issue a no-op snapshot for that category. Focus the scope on adset 103 (category All). Use created_at 2025-08-14T02:23:30Z. Apply the timestamp 2025-08-14T02:25:00Z with request_id ap-016, mandate a verification pass, and recognize the plan as applied at 2025-08-14T02:26:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_017",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:23:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        }
                    ],
                    "total_budget": 1180.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_017",
                    "timestamp": "2025-08-14T02:25:00Z",
                    "request_id": "ap-016"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_017"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_017",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:26:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:25:00Z",
                    "ended_at": "2025-08-14T02:26:00Z",
                    "status": "completed",
                    "input_ref": "ap-016",
                    "outputs_json": {
                        "plan_id": "plan_soc_017",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T02:26:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_017\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T02:26:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_28",
        "instruction": "Serve as the Cross-Promo Pilot with the timestamp 2025-08-14T02:27:00Z. Set up a new adset (adset_id 128) titled 'All \u2014 Cross-Promo' within campaign_id '2', classified under category All, with a daily_budget of 200, bid_strategy of lowest_cost, and status set to active. Make sure exactly one active video ad is available starting 2025-08-14 bearing the name 'All \u2014 Cross-Promo Video v1' using deterministic ad_id auto_128_20250814_1. Consider 2025-08-14T02:27:00Z as the creation timestamp and define the provisioning window as 2025-08-14T02:27:00Z\u20132025-08-14T02:28:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "128",
                        "campaign_id": "2",
                        "name": "All — Cross-Promo",
                        "category": "All",
                        "daily_budget": 200.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "created_at": "2025-08-14T02:27:00Z",
                        "updated_at": "2025-08-14T02:27:00Z"
                    },
                    "timestamp": "2025-08-14T02:27:00Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_128_20250814_1",
                        "adset_id": "128",
                        "name": "All — Cross-Promo Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T02:27:00Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T02:27:00Z",
                    "ended_at": "2025-08-14T02:28:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "128",
                        "ads_created": 1,
                        "final_type": "video",
                        "run_type": "provisioning",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"128\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_29",
        "instruction": "Assume the role of Strategy Migrator and the time is 2025-08-14T02:29:00Z. Plan plan_soc_018 targets 2025-08-13: adjust adsets 104 and 108 to lowest_cost, maintaining adset 106 at cost_cap with bid_amount 18.0. Keep the overall budget constant by not changing the budgets (104=740, 108=780, 106=500). Plan constants \u2014 created_at: 2025-08-14T02:29:00Z; apply_timestamp: 2025-08-14T02:30:30Z (request_id ap-017); applied_at: 2025-08-14T02:31:30Z; verification: required.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_018",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:29:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "104",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        }
                    ],
                    "total_budget": 2020.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_018",
                    "timestamp": "2025-08-14T02:30:30Z",
                    "request_id": "ap-017"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_018"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_018",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:31:30Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:30:30Z",
                    "ended_at": "2025-08-14T02:31:30Z",
                    "status": "completed",
                    "input_ref": "ap-017",
                    "outputs_json": {
                        "plan_id": "plan_soc_018",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T02:31:30Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_018\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T02:31:30Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_30",
        "instruction": "Act as the Engagement Driver and the time is 2025-08-14T02:32:00Z. Shift adsets 102 and 112 to video at 2025-08-14T02:32:00Z using rotation request_id rot-006 with rationale 'video engagement spike'. Ensure there is only one active creative per adset, and acknowledge the rotation as complete at 2025-08-14T02:33:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "102",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:32:00Z",
                    "request_id": "rot-006",
                    "rationale": "video engagement spike",
                    "ad_name": "rot-006-102-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:32:00Z",
                    "request_id": "rot-006",
                    "rationale": "video engagement spike",
                    "ad_name": "rot-006-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:32:00Z",
                    "ended_at": "2025-08-14T02:33:00Z",
                    "status": "completed",
                    "request_id": "rot-006",
                    "input_ref": "rot-006",
                    "outputs_json": {
                        "rotation_request_id": "rot-006",
                        "rotated_adsets_count": 2,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-006\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_31",
        "instruction": "As the CPC Reallocator, the current time is 2025-08-14T02:33:30Z. Handle plan_soc_019 scheduled for 2025-08-13: reallocate 15 from adsets with CPC exceeding 3.0 and assign 15 to those with CPC less than 1.0 within identical categories, maintaining constant total per category. Ascertain CPC using insights for 2025-08-13 on adsets 101, 108, and 112. Given the absence of CPC>3.0 donors for these adsets, create a no-op snapshot with unchanged budgets (101=920, 108=780, 112=700). Utilize created_at 2025-08-14T02:33:30Z. Apply the timestamp 2025-08-14T02:35:00Z with request_id ap-018, insist on verification pass, and regard the plan as applied by 2025-08-14T02:36:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "108",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_019",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:33:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 2400.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_019",
                    "timestamp": "2025-08-14T02:35:00Z",
                    "request_id": "ap-018"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_019"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_019",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:36:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:35:00Z",
                    "ended_at": "2025-08-14T02:36:00Z",
                    "status": "completed",
                    "input_ref": "ap-018",
                    "outputs_json": {
                        "plan_id": "plan_soc_019",
                        "changes": 0,
                        "applied_at": "2025-08-14T02:36:00Z",
                        "run_type": "plan_apply",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_019\"",
                "\"changes\": \"0\"",
                "\"applied_at\": \"2025-08-14T02:36:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_32",
        "instruction": "As the Retargeting Owner, the moment is 2025-08-14T02:36:30Z. Organize adset 127 titled 'Electronics \u2014 Retargeting' under campaign_id 6, with a daily_budget of 280, employing the lowest_cost bid_strategy, status set to active, within the Electronics category. Guarantee the launch of one active image ad titled 'Electronics \u2014 Retargeting Image v1' commencing on 2025-08-14. The provisioning should be considered finalized at 2025-08-14T02:38:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "127",
                        "campaign_id": "6",
                        "name": "Electronics — Retargeting",
                        "category": "Electronics",
                        "daily_budget": 280.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T02:36:30Z"
                    },
                    "timestamp": "2025-08-14T02:36:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_127_20250814_1",
                        "adset_id": "127",
                        "name": "Electronics — Retargeting Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T02:36:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T02:36:30Z",
                    "ended_at": "2025-08-14T02:38:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "127",
                        "ads_created": 1,
                        "final_type": "image",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"127\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"image\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_33",
        "instruction": "As the Guardrails Planner with the current time being 2025-08-14T02:38:00Z, issue plan_soc_020 for the date 2025-08-13. Adjust Mobile adsets 110 and 111 by increasing them by +20 each, financing it through a reduction in Electronics adsets 101 and 112 by \u221220 each. Ensure all other adsets remain unchanged, enforce a per-category minimum of 100, and maintain the exact overall budget with no net changes across categories. Mark the creation time as 2025-08-14T02:38:00Z. Execute the application at 2025-08-14T02:40:00Z with the request_id ap-019, and regard the plan as applied at 2025-08-14T02:41:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_020",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:38:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 900.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1020.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1020.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 680.0
                        }
                    ],
                    "total_budget": 3620.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_020",
                    "timestamp": "2025-08-14T02:40:00Z",
                    "request_id": "ap-019"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_020",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:41:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:40:00Z",
                    "ended_at": "2025-08-14T02:41:00Z",
                    "status": "completed",
                    "input_ref": "ap-019",
                    "outputs_json": {
                        "plan_id": "plan_soc_020",
                        "applied_adsets_count": 4,
                        "applied_at": "2025-08-14T02:41:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_020\"",
                "\"applied_adsets_count\": \"4\"",
                "\"applied_at\": \"2025-08-14T02:41:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_34",
        "instruction": "Assuming the role of the Video Maintainer with the current timestamp being 2025-08-14T02:41:30Z, change adset 101 to video and confirm adset 111 continues as video (allowing for no-op). Enforce having only one active creative per adset. Use the rotation request_id rot-007, designate the new ad as rot-007-101-video, and apply the rationale 'maintain video policy'. Acknowledge the completion of the rotation at 2025-08-14T02:43:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "101",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:43:30Z",
                    "request_id": "rot-007",
                    "rationale": "maintain video policy",
                    "ad_name": "rot-007-101-video"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:41:30Z",
                    "ended_at": "2025-08-14T02:43:30Z",
                    "status": "completed",
                    "request_id": "rot-007",
                    "input_ref": "rot-007",
                    "outputs_json": {
                        "rotation_request_id": "rot-007",
                        "rotated_adsets_count": 1,
                        "confirmed_video_count": 1,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T02:43:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-007\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"confirmed_video_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_35",
        "instruction": "As the Smoother, the current time is 2025-08-14T02:42:30Z. Disseminate plan_soc_021 dated 2025-08-13. Restrict absolute budget differences compared to the existing snapshot to \u00b125 per adset. Focus solely on adsets 101, 108, 110, 111, and 112, maintaining allocations as per the snapshot (no changes), and do not alter strategies and creatives. Apply created_at 2025-08-14T02:42:30Z. Use apply timestamp 2025-08-14T02:44:00Z with request_id ap-020, mandate a verification pass, and recognize the plan as applied at 2025-08-14T02:45:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_021",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:42:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 4400.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_021",
                    "timestamp": "2025-08-14T02:44:00Z",
                    "request_id": "ap-020"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_021"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_021",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:45:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:44:00Z",
                    "ended_at": "2025-08-14T02:45:00Z",
                    "status": "completed",
                    "input_ref": "ap-020",
                    "outputs_json": {
                        "plan_id": "plan_soc_021",
                        "changes": 0,
                        "applied_at": "2025-08-14T02:45:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_021\"",
                "\"changes\": \"0\"",
                "\"applied_at\": \"2025-08-14T02:45:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_36",
        "instruction": "Assigned as the Home Video Champion, the time is now 2025-08-14T02:45:30Z. Set up adset 129 labeled 'Home \u2014 Video First' within campaign_id 5, including daily_budget 260, bid_strategy lowest_cost, category Home, and set to active status. Guarantee that a single active video ad launches on 2025-08-14 titled 'Home \u2014 Video First v1'. Acknowledge the provisioning as completed by 2025-08-14T02:47:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "129",
                        "campaign_id": "5",
                        "name": "Home — Video First",
                        "category": "Home",
                        "daily_budget": 260.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T02:45:30Z"
                    },
                    "timestamp": "2025-08-14T02:45:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_129_20250814_1",
                        "adset_id": "129",
                        "name": "Home — Video First v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T02:45:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T02:45:30Z",
                    "ended_at": "2025-08-14T02:47:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "129",
                        "ads_created": 1,
                        "final_type": "video",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"129\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_37",
        "instruction": "As the Rounding Supervisor at 2025-08-14T02:46:30Z, issue publication of plan_soc_022 for the date 2025-08-13. Adjust all adset budgets to be rounded to the nearest multiple of 10, ensuring each category's total remains unchanged. Implement these specific changes to avoid non-operations: in Electronics, adjust adset 101 to 930 and adset 108 to 770, with adset 112 staying at 700; in Mobile, let adsets 110 and 111 remain at 1000. Use created_at 2025-08-14T02:46:30Z. Implement at 2025-08-14T02:48:00Z with request_id ap-021 and recognize the plan as applied at 2025-08-14T02:49:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_022",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:46:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 930.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 770.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 4400.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_022",
                    "timestamp": "2025-08-14T02:48:00Z",
                    "request_id": "ap-021"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_022",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:49:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:48:00Z",
                    "ended_at": "2025-08-14T02:49:00Z",
                    "status": "completed",
                    "input_ref": "ap-021",
                    "outputs_json": {
                        "plan_id": "plan_soc_022",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T02:49:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_022\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T02:49:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_38",
        "instruction": "Acting as the Unified Creative Lead at 2025-08-14T02:49:30Z, switch adsets 102 and 104 to video format and ensure adset 110 continues as video (permitting no-op), enforcing that each adset has only one active creative. Utilize rotation request_id rot-008, name the new ads rot-008-<adset_id>-<type>, and apply the rationale 'uniform creative for test'. Mark the rotation as finalized at 2025-08-14T02:51:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "102",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:51:30Z",
                    "request_id": "rot-008",
                    "rationale": "uniform creative for test",
                    "ad_name": "rot-008-102-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:51:30Z",
                    "request_id": "rot-008",
                    "rationale": "uniform creative for test",
                    "ad_name": "rot-008-104-video"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:49:30Z",
                    "ended_at": "2025-08-14T02:51:30Z",
                    "status": "completed",
                    "request_id": "rot-008",
                    "input_ref": "rot-008",
                    "outputs_json": {
                        "rotation_request_id": "rot-008",
                        "rotated_adsets_count": 2,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-008\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_39",
        "instruction": "You are designated as the Viewership Optimizer and the current time is 2025-08-14T02:50:30Z. Release plan_soc_023 for the date 2025-08-13. Based on the day's viewership boost, keep the total expenditure intact while reallocating +30 from Home to Toys: adjust adset 106 to 470 and adset 107 to 430, leaving strategies and creatives the same. Use created_at 2025-08-14T02:50:30Z. Apply the timestamp 2025-08-14T02:52:00Z (request_id ap-022) and regard the plan as applied at 2025-08-14T02:53:00Z.",
        "actions": [
            {
                "name": "GetViewershipForCategory",
                "arguments": {
                    "category": "Home",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetViewershipForCategory",
                "arguments": {
                    "category": "Toys",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_023",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:50:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 470.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 430.0
                        }
                    ],
                    "total_budget": 900.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_023",
                    "timestamp": "2025-08-14T02:52:00Z",
                    "request_id": "ap-022"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_023"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_023",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:53:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:52:00Z",
                    "ended_at": "2025-08-14T02:53:00Z",
                    "status": "completed",
                    "input_ref": "ap-022",
                    "outputs_json": {
                        "plan_id": "plan_soc_023",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T02:53:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_023\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T02:53:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_40",
        "instruction": "Assume the role of the ROAS Optimizer with the time set at 2025-08-14T02:55:00Z. Issue plan_soc_024 for the date 2025-08-13. Change cost_cap adsets with a CPA on 2025-08-13 of < 20 to lowest_cost, and provide an additional +15 funded by \u221215 from peers within the same category having a CPA > 60; if no donors are present, maintain the original budgets. Focus only on adsets 101 (Electronics) and 106 (Home). Ensure creatives replicate the currently active types from DB reads: adset 101 = image, adset 106 = image (unchanged). Use created_at 2025-08-14T02:55:00Z. Implement the apply timestamp 2025-08-14T02:57:00Z with request_id ap-023, perform a verification pass, and view the plan as applied at 2025-08-14T02:58:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_024",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T02:55:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        }
                    ],
                    "total_budget": 1420.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_024",
                    "timestamp": "2025-08-14T02:57:00Z",
                    "request_id": "ap-023"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_024"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_024",
                    "status": "applied",
                    "applied_at": "2025-08-14T02:58:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T02:57:00Z",
                    "ended_at": "2025-08-14T02:58:00Z",
                    "status": "completed",
                    "input_ref": "ap-023",
                    "outputs_json": {
                        "plan_id": "plan_soc_024",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T02:58:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_024\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T02:58:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_41",
        "instruction": "As the Parity Director, at 2025-08-14T02:58:00Z, switch adset 105 to video and adset 112 to video by 2025-08-14T02:59:30Z, ensuring each adset contains only one active creative. Utilize the rotation request_id rot-004, citing 'type parity per category' as the reason. Mark the rotation as finalized at 2025-08-14T02:59:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "105",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:59:30Z",
                    "request_id": "rot-004",
                    "rationale": "type parity per category",
                    "ad_name": "rot-004-105-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:59:30Z",
                    "request_id": "rot-004",
                    "rationale": "type parity per category",
                    "ad_name": "rot-004-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:58:00Z",
                    "ended_at": "2025-08-14T02:59:30Z",
                    "status": "completed",
                    "request_id": "rot-004",
                    "input_ref": "rot-004",
                    "outputs_json": {
                        "rotation_request_id": "rot-004",
                        "rotated_adsets_count": 2,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T02:59:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-004\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_42",
        "instruction": "Being the Strategy Guardian at 2025-08-14T03:00:00Z, release plan_soc_025 for the date 2025-08-13, which locks adset 111 at a cost_cap of 2.5 and adset 106 at a cost_cap of 18.0, while other adsets remain at lowest_cost and budgets stay unchanged. Note the created_at time as 2025-08-14T03:00:00Z. Employ the apply timestamp of 2025-08-14T03:02:00Z with request_id ap-024, ensure a verification pass is mandated, and declare the plan applied by 2025-08-14T03:03:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_025",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:00:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ],
                    "total_budget": 1500.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_025",
                    "timestamp": "2025-08-14T03:02:00Z",
                    "request_id": "ap-024"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_025"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_025",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:03:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:02:00Z",
                    "ended_at": "2025-08-14T03:03:00Z",
                    "status": "completed",
                    "input_ref": "ap-024",
                    "outputs_json": {
                        "plan_id": "plan_soc_025",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T03:03:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_025\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T03:03:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_43",
        "instruction": "As the A/B Creative Lead, situated at 2025-08-14T02:16:30Z, arrange for a new Mobile adset (adset_id 137, category Mobile) titled 'Mobile \u2014 Creatives A/B' within campaign_id '7' with a daily_budget of 240, bid_strategy set to lowest_cost, and maintain status active. Activate a single image ad called 'Mobile A/B - Image v1', commencing on 2025-08-14. For auditing purposes, collect a 7-day CPA snapshot for adset 137 covering 2025-08-08..2025-08-14 according to policy timezone and currency; initiate rotation regardless if the timeframe is vacant since the adset is novel. Transition the adset\u2019s active creative to video through rotation request_id rot-004, label the new ad rot-004-137-video, using 'video test' as the rationale. Treat the rotation as finalized at 2025-08-14T02:18:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "137",
                        "campaign_id": "7",
                        "name": "Mobile — Creatives A/B",
                        "category": "Mobile",
                        "daily_budget": 240.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T02:16:30Z"
                    },
                    "timestamp": "2025-08-14T02:16:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_137_20250814_1",
                        "adset_id": "137",
                        "name": "Mobile A/B - Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T02:16:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T02:16:30Z",
                    "ended_at": "2025-08-14T02:18:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "run_type": "provisioning",
                        "run_status": "completed",
                        "adset_id": "137",
                        "ads_created": 1
                    },
                    "errors_json": null
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-08"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-09"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-10"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-11"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-12"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "137",
                    "date": "2025-08-14"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "insights_snapshot",
                    "started_at": "2025-08-14T02:16:30Z",
                    "ended_at": "2025-08-14T02:18:00Z",
                    "status": "completed",
                    "request_id": "is-001",
                    "input_ref": "insights-137-20250808-20250814",
                    "outputs_json": {
                        "adset_id": "137",
                        "metric": "CPA",
                        "window": {
                            "start": "2025-08-08",
                            "end": "2025-08-14"
                        },
                        "currency": "USD",
                        "timezone": "UTC",
                        "days": [
                            "2025-08-08",
                            "2025-08-09",
                            "2025-08-10",
                            "2025-08-11",
                            "2025-08-12",
                            "2025-08-13",
                            "2025-08-14"
                        ],
                        "entries": []
                    },
                    "errors_json": null
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "137",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:18:00Z",
                    "request_id": "rot-004",
                    "rationale": "video test",
                    "ad_name": "rot-004-137-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T02:16:30Z",
                    "ended_at": "2025-08-14T02:18:00Z",
                    "status": "completed",
                    "request_id": "rot-004",
                    "input_ref": "rot-004",
                    "outputs_json": {
                        "rotation_request_id": "rot-004",
                        "rotated_adsets_count": 1,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-004\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_44",
        "instruction": "Act as the CPC Splitter at time 2025-08-14T03:04:30Z. Execute the publication of plan_soc_026 for the date 2025-08-13. Within the Electronics section, relocate 40 from adset 101 (experiencing higher CPC on 2025-08-13) to adset 112 (experiencing lower CPC on 2025-08-13); keep all other adsets intact. Utilize created_at timestamp 2025-08-14T03:04:30Z. Employ apply timestamp 2025-08-14T03:06:00Z with request_id ap-025, necessitate a verification pass, and regard the plan as applied by 2025-08-14T03:07:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_026",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:04:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 880.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 740.0
                        }
                    ],
                    "total_budget": 1620.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_026",
                    "timestamp": "2025-08-14T03:06:00Z",
                    "request_id": "ap-025"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_026"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_026",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:07:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:06:00Z",
                    "ended_at": "2025-08-14T03:07:00Z",
                    "status": "completed",
                    "input_ref": "ap-025",
                    "outputs_json": {
                        "plan_id": "plan_soc_026",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T03:07:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_026\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T03:07:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_45",
        "instruction": "As the Video Enforcer, note that the time is 2025-08-14T03:07:30Z. Shift adset 107 to image as of 2025-08-14T03:07:30Z, using rotation request_id rot-010 with the reasoning 'reinforce best type'. Designate the new ad as rot-010-107-image, mandate single-active status, and log completion at 2025-08-14T03:08:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "107",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T03:07:30Z",
                    "request_id": "rot-010",
                    "rationale": "reinforce best type",
                    "ad_name": "rot-010-107-image"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:07:30Z",
                    "ended_at": "2025-08-14T03:08:30Z",
                    "status": "completed",
                    "request_id": "rot-010",
                    "input_ref": "rot-010",
                    "outputs_json": {
                        "rotation_request_id": "rot-010",
                        "rotated_adsets_count": 1,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-010\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_46",
        "instruction": "As the CTR Normalizer, be aware that it is 2025-08-14T03:08:30Z. Release plan_soc_027 for the date 2025-08-13 to proportionally redistribute Apparel budgets among adsets 102, 104, and 105 according to their CTR from 2025-08-13, maintaining the total for the Apparel category constant. Define CTR as clicks/impressions using insights from 2025-08-13. Employ the policy budget_rounding_unit=10 with round-half-up; post-rounding, if the aggregated total diverges from the category total, adjust any +/- residual starting with the highest CTR adset, resolving ties by ascending adset_id. Retain each adset's bid_strategy and bid_amount from the DB, and replicate each adset's currently active creative type. For the day's insights: 102 has CTR=1080/27500, 104 has CTR=1280/31500, 105 has CTR=1250/31000. With the Apparel total matching the DB daily_budget sum for 102/104/105 and following the aforementioned rules, assign the final budgets precisely as: 102 \u2192 680.0, 104 \u2192 700.0, 105 \u2192 700.0 (totaling 2080.0). Use timestamp 2025-08-14T03:10:00Z for application with request_id ap-026, confirm success, and deem the plan enacted at 2025-08-14T03:11:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_027",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:08:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "102",
                            "budget": 680.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 700.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 2080.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_027",
                    "timestamp": "2025-08-14T03:10:00Z",
                    "request_id": "ap-026"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_027"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_027",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:11:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:10:00Z",
                    "ended_at": "2025-08-14T03:11:00Z",
                    "status": "completed",
                    "input_ref": "ap-026",
                    "outputs_json": {
                        "plan_id": "plan_soc_027",
                        "applied_adsets_count": 3,
                        "applied_at": "2025-08-14T03:11:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_027\"",
                "\"applied_adsets_count\": \"3\"",
                "\"applied_at\": \"2025-08-14T03:11:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_47",
        "instruction": "As the Accessories Owner at the time 2025-08-14T03:11:30Z, arrange a new Electronics adset (adset_id 130) under campaign_id '6' with the name 'Electronics \u2014 Accessories'. Set a daily_budget of 210, a bid_strategy of lowest_cost, and ensure the status is active. Initiate an active video ad named 'Electronics Accessories Video v1' starting on 2025-08-14. Document the provisioning process to conclude 120 seconds after the initial time.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "130",
                        "campaign_id": "6",
                        "name": "Electronics — Accessories",
                        "category": "Electronics",
                        "daily_budget": 210.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T03:11:30Z"
                    },
                    "timestamp": "2025-08-14T03:11:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_130_20250814_1",
                        "adset_id": "130",
                        "name": "Electronics Accessories Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T03:11:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T03:11:30Z",
                    "ended_at": "2025-08-14T03:13:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-3",
                    "outputs_json": {
                        "run_type": "provisioning",
                        "run_status": "completed",
                        "adset_id": "130",
                        "ads_created": 1,
                        "final_type": "video"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"130\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_48",
        "instruction": "Acting as the Purchase-Driven Planner at 2025-08-14T03:12:30Z, publish plan_soc_028 for the date 2025-08-13. Within the Apparel adsets (102, 104, 105), allocate +10 only to those adsets with purchases \u2265 5, financed by \u221210 from those adsets with zero purchases on 2025-08-13, while maintaining the total for the Apparel category constant and keeping each adset's strategy and creative type unchanged. Since no Apparel donors have zero purchases on 2025-08-13, maintain the current budgets of all three adsets. Use 2025-08-14T03:14:00Z (ap-027) as the timestamp for application, and acknowledge the plan as applied at 2025-08-14T03:15:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "102",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "104",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "105",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_028",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:12:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "104",
                            "name": "Fall Fashion - Women",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "104",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 20.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "104",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "102",
                            "budget": 590.0
                        },
                        {
                            "adset_id": "104",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 750.0
                        }
                    ],
                    "total_budget": 2080.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_028",
                    "timestamp": "2025-08-14T03:14:00Z",
                    "request_id": "ap-027"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_028",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:15:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:14:00Z",
                    "ended_at": "2025-08-14T03:15:00Z",
                    "status": "completed",
                    "input_ref": "ap-027",
                    "outputs_json": {
                        "plan_id": "plan_soc_028",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T03:15:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_028\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T03:15:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_49",
        "instruction": "As the Home/Toys Video Lead, the current time is 2025-08-14T03:15:30Z. Switch adsets 104 and 108 to video at 2025-08-14T03:15:30Z using rotation request_id rot-010 with the justification 'uniform video in Home/Toys'. Mark the rotation as finished at 2025-08-14T03:16:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:15:30Z",
                    "request_id": "rot-010",
                    "rationale": "uniform video in Home/Toys",
                    "ad_name": "rot-010-104-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "108",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:15:30Z",
                    "request_id": "rot-010",
                    "rationale": "uniform video in Home/Toys",
                    "ad_name": "rot-010-108-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:15:30Z",
                    "ended_at": "2025-08-14T03:16:30Z",
                    "status": "completed",
                    "request_id": "rot-010",
                    "input_ref": "rot-010",
                    "outputs_json": {
                        "rotation_request_id": "rot-010",
                        "rotated_adsets_count": 2,
                        "run_type": "creative_rotation",
                        "run_status": "completed",
                        "ended_at": "2025-08-14T03:16:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-010\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_50",
        "instruction": "Serving as the Electronics Floor Manager, the current time is 2025-08-14T03:16:30Z. Implement plan_soc_029 for the date 2025-08-13 to ensure Electronics \u2265 100 per adset and maintain the category total. Within the Electronics category, increase adset 112 by +20 and decrease adset 101 by \u221220, while keeping adset 108 unchanged. Adjust creatives to reflect the active types from DB reads: 101=image, 108=image, 112=image. Utilize the created_at timestamp 2025-08-14T03:16:30Z. Apply the use timestamp 2025-08-14T03:18:00Z with request_id ap-028, ensure it undergoes a verification pass, and acknowledge the plan as applied at 2025-08-14T03:19:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_029",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:16:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "108",
                            "name": "Back to School - Laptops",
                            "category": "Electronics",
                            "campaign_id": "6"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "108",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 42.0
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "108",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 900.0
                        },
                        {
                            "adset_id": "108",
                            "budget": 780.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 720.0
                        }
                    ],
                    "total_budget": 2400.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_029",
                    "timestamp": "2025-08-14T03:18:00Z",
                    "request_id": "ap-028"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_029"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_029",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:19:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:18:00Z",
                    "ended_at": "2025-08-14T03:19:00Z",
                    "status": "completed",
                    "input_ref": "ap-028",
                    "outputs_json": {
                        "plan_id": "plan_soc_029",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T03:19:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_029\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T03:19:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_51",
        "instruction": "As the Influencer Pilot, and the current time being 2025-08-14T03:19:30Z, handle the provisioning of a new Apparel adset (adset_id 131, category Apparel) with the name 'Apparel \u2014 Influencer' under campaign_id '3'. Set a daily_budget of 240, utilize bid_strategy lowest_cost, and ensure the status is active. One active video ad should commence on 2025-08-14 named 'Apparel \u2014 Influencer Video v1'. Conclude the provisioning by 2025-08-14T03:21:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "131",
                        "campaign_id": "3",
                        "name": "Apparel — Influencer",
                        "category": "Apparel",
                        "daily_budget": 240.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "created_at": "2025-08-14T03:19:30Z",
                        "updated_at": "2025-08-14T03:19:30Z"
                    },
                    "timestamp": "2025-08-14T03:19:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_131_20250814_1",
                        "adset_id": "131",
                        "name": "Apparel — Influencer Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T03:19:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T03:19:30Z",
                    "ended_at": "2025-08-14T03:21:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "131",
                        "ads_created": 1,
                        "final_type": "video",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"131\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_52",
        "instruction": "Occupying the role of Market Entry Pilot, with the time set at 2025-08-14T03:03:30Z, coordinate the provisioning of a new Mobile adset (adset_id 141, category Mobile) titled 'Mobile \u2014 New Market' under campaign_id '7'. Ensure the daily_budget is 270, the bid_strategy is lowest_cost, and the status is active. An active image ad should initiate on 2025-08-14 named 'Mobile \u2014 New Market Image v1'. Wrap up the provisioning by 2025-08-14T03:05:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "141",
                        "campaign_id": "7",
                        "name": "Mobile — New Market",
                        "category": "Mobile",
                        "daily_budget": 270.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T03:03:30Z"
                    },
                    "timestamp": "2025-08-14T03:03:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_141_20250814_1",
                        "adset_id": "141",
                        "name": "Mobile — New Market Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T03:03:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T03:03:30Z",
                    "ended_at": "2025-08-14T03:05:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-3",
                    "outputs_json": {
                        "adset_id": "141",
                        "ads_created": 1,
                        "final_type": "image",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"141\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"image\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_53",
        "instruction": "Assume the role of the Mobile Fixer and note the time as 2025-08-14T03:22:30Z. Publish plan_soc_031 for the date 2025-08-13. Lock adset 111 with a cost_cap of 2.5 and adset 106 with a cost_cap of 18.0. During Mobile activities on 2025-08-13, reallocate 30 of the budget from the adset with the highest CPA to the one with the lowest CPA (using defined parameters: donor=110, recipient=111 based on that day\u2019s CPAs), keeping other categories constant. Replicate active creative types according to DB entries: adset 106=image, adset 110=video, adset 111=video. Employ created_at 2025-08-14T03:22:30Z. Use apply timestamp 2025-08-14T03:24:00Z along with request_id ap-029, ensure a verification pass, and recognize the plan as applied at 2025-08-14T03:25:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_031",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:22:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 970.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1030.0
                        }
                    ],
                    "total_budget": 2500.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_031",
                    "timestamp": "2025-08-14T03:24:00Z",
                    "request_id": "ap-029"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_031"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_031",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:25:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:24:00Z",
                    "ended_at": "2025-08-14T03:25:00Z",
                    "status": "completed",
                    "input_ref": "ap-029",
                    "outputs_json": {
                        "plan_id": "plan_soc_031",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T03:25:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_031\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T03:25:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_54",
        "instruction": "Take charge as the Video-Lift Owner and recognize the time as 2025-08-14T03:25:30Z. Set up a new Toys adset (adset_id 134, category Toys) titled 'Toys \u2014 Video Lift' under campaign_id '5' with a daily_budget of 225, utilizing bid_strategy lowest_cost, and setting the status to active. Ensure an active image ad commences on 2025-08-14, named 'Toys \u2014 Video Lift Image v1'. Shift the adset\u2019s active creative to video using rotation request_id rot-004, with the reason 'video lift' at 2025-08-14T03:27:00Z. Regard the provisioning as finished at 2025-08-14T03:27:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "134",
                        "campaign_id": "5",
                        "name": "Toys — Video Lift",
                        "category": "Toys",
                        "daily_budget": 225.0,
                        "bid_strategy": "lowest_cost",
                        "bid_amount": null,
                        "status": "active",
                        "updated_at": "2025-08-14T03:25:30Z"
                    },
                    "timestamp": "2025-08-14T03:25:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_134_20250814_1",
                        "adset_id": "134",
                        "name": "Toys — Video Lift Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T03:25:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "134",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:27:00Z",
                    "request_id": "rot-004",
                    "rationale": "video lift",
                    "ad_name": "rot-004-134-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T03:25:30Z",
                    "ended_at": "2025-08-14T03:27:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-3",
                    "outputs_json": {
                        "adset_id": "134",
                        "ads_created": 2,
                        "final_type": "video",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"134\"",
                "\"ads_created\": \"2\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_55",
        "instruction": "As the Bid Rounding Lead, and with the current time being 2025-08-14T03:27:30Z, release plan_soc_032 for the date 2025-08-13. Adjust cost_cap bid amounts by rounding them down to one decimal place, while keeping budgets intact. Focus on the adsets 101 (Electronics), 106 (Home), and 111 (Mobile). Set the final rounded bids to: adset 101 \u2192 cost_cap 2.5, adset 106 \u2192 cost_cap 18.0, adset 111 \u2192 cost_cap 2.5. Reflect the active creative types as per the DB reads: adset 101=image, adset 106=image, adset 111=video. Use the created_at timestamp of 2025-08-14T03:27:30Z. Implement the apply timestamp of 2025-08-14T03:29:00Z with request_id ap-030, ensure a verification pass is conducted, and consider the plan applied at 2025-08-14T03:30:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_032",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:27:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ],
                    "total_budget": 2420.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_032",
                    "timestamp": "2025-08-14T03:29:00Z",
                    "request_id": "ap-030"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_032"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_032",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:30:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:29:00Z",
                    "ended_at": "2025-08-14T03:30:00Z",
                    "status": "completed",
                    "input_ref": "ap-030",
                    "outputs_json": {
                        "plan_id": "plan_soc_032",
                        "applied_adsets_count": 1,
                        "applied_at": "2025-08-14T03:30:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_032\"",
                "\"applied_adsets_count\": \"1\"",
                "\"applied_at\": \"2025-08-14T03:30:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_56",
        "instruction": "As the Parity Enforcer, with the time noted as 2025-08-14T03:30:30Z, shift adset 101 to video and adset 112 to video precisely at 2025-08-14T03:30:30Z, ensuring only one active creative per adset. Utilize the rotation request_id rot-004 with the justification 'video parity across All/Electronics'. Treat the rotation as finalized at 2025-08-14T03:30:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "101",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:30:30Z",
                    "request_id": "rot-004",
                    "rationale": "video parity across All/Electronics",
                    "ad_name": "rot-004-101-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:30:30Z",
                    "request_id": "rot-004",
                    "rationale": "video parity across All/Electronics",
                    "ad_name": "rot-004-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:30:30Z",
                    "ended_at": "2025-08-14T03:30:30Z",
                    "status": "completed",
                    "request_id": "rot-004",
                    "input_ref": "rot-004",
                    "outputs_json": {
                        "rotation_request_id": "rot-004",
                        "rotated_adsets_count": 2,
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-004\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_57",
        "instruction": "Acting as the Two-Hop Reallocator at 2025-08-14T03:31:30Z, release plan_soc_033 for 2025-08-13. Adhere to the budget_rounding_unit of 10 by reallocating 20 from All to Mobile and 20 from Home to Electronics. Resolve unequivocally with 103 (All) and 106 (Home) as donors, and 111 (Mobile) and 112 (Electronics) as recipients. Establish final budgets as follows: 103\u21921160.0, 106\u2192480.0, 111\u21921020.0, 112\u2192720.0; maintain strategies unaltered and keep the total constant. Set created_at as 2025-08-14T03:31:30Z. Apply timestamp should be 2025-08-14T03:33:00Z with request_id ap-031, a verification pass is required, and recognize the plan as executed at 2025-08-14T03:34:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_033",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:31:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1160.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 480.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1020.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 720.0
                        }
                    ],
                    "total_budget": 3380.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_033",
                    "timestamp": "2025-08-14T03:33:00Z",
                    "request_id": "ap-031"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_033"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_033",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:34:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:33:00Z",
                    "ended_at": "2025-08-14T03:34:00Z",
                    "status": "completed",
                    "input_ref": "ap-031",
                    "outputs_json": {
                        "plan_id": "plan_soc_033",
                        "applied_adsets_count": 4,
                        "applied_at": "2025-08-14T03:34:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_033\"",
                "\"applied_adsets_count\": \"4\"",
                "\"applied_at\": \"2025-08-14T03:34:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_58",
        "instruction": "As the Home Launch Owner at 2025-08-14T03:40:30Z, launch a new video creative for adset 121 at 2025-08-14T03:41:00Z utilizing rotation request_id rot-010 with reason 'Home Launch video upgrade', and enforce a single-active policy (pause any prior active creative). Designate the new ad as rot-010-121-video. Mark the rotation as complete by 2025-08-14T03:42:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "121",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:41:00Z",
                    "request_id": "rot-010",
                    "rationale": "Home Launch video upgrade",
                    "ad_name": "rot-010-121-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:41:00Z",
                    "ended_at": "2025-08-14T03:42:00Z",
                    "status": "completed",
                    "request_id": "rot-010",
                    "input_ref": "rot-010",
                    "outputs_json": {
                        "rotation_request_id": "rot-010",
                        "rotated_adsets_count": 1,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T03:42:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-010\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T03:42:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_59",
        "instruction": "Act as the Audience-Signal Planner and note that the current time is 2025-08-14T03:36:30Z. Release plan_soc_034 intended for the date 2025-08-13. Given that the All category has a single adset (adset_id 103) on 2025-08-13, there is no opportunity for intra-All reallocation; execute a no-op envelope maintaining the budget for adset 103 as it is. Apply the created_at as 2025-08-14T03:36:30Z. Implement the apply timestamp 2025-08-14T03:38:00Z with request_id ap-032, necessitate a verification pass, and deem the plan applied at 2025-08-14T03:39:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_034",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:36:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        }
                    ],
                    "total_budget": 1180.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_034",
                    "timestamp": "2025-08-14T03:38:00Z",
                    "request_id": "ap-032"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_034"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_034",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:39:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:38:00Z",
                    "ended_at": "2025-08-14T03:39:00Z",
                    "status": "completed",
                    "input_ref": "ap-032",
                    "outputs_json": {
                        "plan_id": "plan_soc_034",
                        "applied_adsets_count": 0,
                        "noops": [
                            {
                                "adset_id": "103",
                                "reason": "already_in_target_state"
                            }
                        ],
                        "applied_at": "2025-08-14T03:39:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_034\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T03:39:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_60",
        "instruction": "Function as the Electronics Video Champion with the current time as 2025-08-14T03:39:30Z. For adset 103, if the active creative on 2025-08-14 is already a video, document a no-op rotation citing 'already_in_target_state' as the reason. If not, switch to video at 2025-08-14T03:39:30Z, using rotation request_id rot-011, with the rationale 'consolidate video in Electronics', and designate the new ad as rot-011-103-video. Acknowledge the rotation as finalized at 2025-08-14T03:40:30Z.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:39:30Z",
                    "ended_at": "2025-08-14T03:40:30Z",
                    "status": "completed",
                    "request_id": "rot-011",
                    "input_ref": "rot-011",
                    "outputs_json": {
                        "rotation_request_id": "rot-011",
                        "rotated_adsets_count": 0,
                        "noops": [
                            {
                                "adset_id": "103",
                                "reason": "already_in_target_state"
                            }
                        ],
                        "run_status": "completed",
                        "ended_at": "2025-08-14T03:40:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-011\"",
                "\"rotated_adsets_count\": \"0\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T03:40:30Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_61",
        "instruction": "As the CTR Gatekeeper, note that the time is 2025-08-14T03:40:30Z. Release plan_soc_035 for date 2025-08-13. On 2025-08-13, assess CTR for adsets 103 (All), 106 (Home), 111 (Mobile), and 112 (Electronics): in each category, adjust budgets by \u221210 for CTR below 0.5% and increase by +10 for CTR exceeding 2.5%, ensuring adjustments remain confined within the same category. As there is only one adset per category, budgets will remain stable. Plan constants: created_at 2025-08-14T03:40:30Z; apply timestamp 2025-08-14T03:42:00Z (request_id ap-033); applied_at 2025-08-14T03:43:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "103",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_035",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:40:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 3380.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_035",
                    "timestamp": "2025-08-14T03:42:00Z",
                    "request_id": "ap-033"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_035"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_035",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:43:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:42:00Z",
                    "ended_at": "2025-08-14T03:43:00Z",
                    "status": "completed",
                    "input_ref": "ap-033",
                    "outputs_json": {
                        "plan_id": "plan_soc_035",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T03:43:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_035\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T03:43:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_62",
        "instruction": "Serving as the Single-Active Steward at the time 2025-08-14T03:22:00Z, implement the single-active policy for date 2025-08-13 across the account: if an adset comprises more than one active ad with the identical creative type, conclude with precisely one active ad by swapping them out for a singular new ad named rot-011-<adset_id>-<type>. Should multiple types be active, refrain from altering types during this cycle; simply condense duplicates. Utilize apply timestamp 2025-08-14T03:22:00Z with rotation request_id rot-011 and justification 'single-active policy'. Mark the enforcement as finished at 2025-08-14T03:23:00Z.",
        "actions": [
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "109"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T03:22:00Z",
                    "request_id": "rot-011",
                    "rationale": "single-active policy",
                    "ad_name": "rot-011-112-image"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1116",
                    "status": "paused",
                    "timestamp": "2025-08-14T03:22:00Z",
                    "request_id": "rot-011-1116-pause"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "1117",
                    "status": "paused",
                    "timestamp": "2025-08-14T03:22:00Z",
                    "request_id": "rot-011-1117-pause"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:22:00Z",
                    "ended_at": "2025-08-14T03:23:00Z",
                    "status": "completed",
                    "request_id": "rot-011-log",
                    "input_ref": "rot-011",
                    "outputs_json": {
                        "scope": "account",
                        "enforced_single_active": true,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"scope\": \"account\"",
                "\"enforced_single_active\": \"True\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_63",
        "instruction": "Act as the Fair-Share Planner and the time is 2025-08-14T03:44:30Z. Release plan_soc_036 for the date 2025-08-13. In each category, reallocate +20 to the lowest-CPA adset by reducing \u221220 from the highest-CPA adset, ensuring category totals remain unchanged and each allocation is \u2265 the per-adset minimum and aligns with the budget rounding unit. Utilize the deterministic pairs: Electronics 101 \u2192 112; Apparel 105 \u2192 102; Mobile 110 \u2192 111. Plan constants: created_at 2025-08-14T03:44:30Z; apply timestamp 2025-08-14T03:46:00Z (request_id ap-034); applied_at 2025-08-14T03:47:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_036",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:44:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 900.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 720.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 730.0
                        },
                        {
                            "adset_id": "102",
                            "budget": 610.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 980.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1020.0
                        }
                    ],
                    "total_budget": 4960.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_036",
                    "timestamp": "2025-08-14T03:46:00Z",
                    "request_id": "ap-034"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_036"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_036",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:47:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:46:00Z",
                    "ended_at": "2025-08-14T03:47:00Z",
                    "status": "completed",
                    "input_ref": "ap-034",
                    "outputs_json": {
                        "plan_id": "plan_soc_036",
                        "applied_adsets_count": 6,
                        "applied_at": "2025-08-14T03:47:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_036\"",
                "\"applied_adsets_count\": \"6\"",
                "\"applied_at\": \"2025-08-14T03:47:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_64",
        "instruction": "Serve as the High-ROAS Video Lead and the time is 2025-08-14T03:47:30Z. Transition adsets 110 and 104 to video at 2025-08-14T03:47:30Z using rotation request_id rot-011 under the justification 'harmonize video on high-ROAS sets', maintaining single-active. If an adset already has video active at that time, consider it a no-op. Designate any new ads as rot-011-<adset_id>-video. Mark the rotation as finalized at 2025-08-14T03:48:30Z.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:47:30Z",
                    "request_id": "rot-011",
                    "rationale": "harmonize video on high-ROAS sets",
                    "ad_name": "rot-011-104-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:47:30Z",
                    "ended_at": "2025-08-14T03:48:30Z",
                    "status": "completed",
                    "request_id": "rot-011",
                    "input_ref": "rot-011",
                    "outputs_json": {
                        "rotation_request_id": "rot-011",
                        "rotated_adsets_count": 1,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T03:48:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-011\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_65",
        "instruction": "Act as the Swap Steward with the current time being 2025-08-14T03:48:30Z. Release plan_soc_037 for 2025-08-13, which reallocates budgets between adset 101 and adset 103 by transferring 10 from 103 to 101; maintain all other adsets as they are. Budgets must adhere to the rounding unit of 10, resulting in adset 101 = 930 and adset 103 = 1170. Use created_at 2025-08-14T03:48:30Z. Apply timestamp 2025-08-14T03:50:00Z with request_id ap-035, necessitate a verification pass, and consider the plan fully implemented by 2025-08-14T03:51:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_037",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:48:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 930.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1170.0
                        }
                    ],
                    "total_budget": 2100.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_037",
                    "timestamp": "2025-08-14T03:50:00Z",
                    "request_id": "ap-035"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_037"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_037",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:51:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:50:00Z",
                    "ended_at": "2025-08-14T03:51:00Z",
                    "status": "completed",
                    "input_ref": "ap-035",
                    "outputs_json": {
                        "plan_id": "plan_soc_037",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T03:51:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_037\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T03:51:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_66",
        "instruction": "Assume the role of the Audience Seeder and note that the current time is 2025-08-14T03:51:30Z. Establish a new adset (adset_id 132) titled 'All \u2014 New Audience' within campaign_id '2', ensuring it has a daily_budget of 210, adopts the bid_strategy lowest_cost, and is marked as active, being created_at 2025-08-14T03:51:30Z (category All). Make sure an active image ad commences on 2025-08-14 under the name 'All \u2014 New Audience Image v1'. Utilize provisioning_default_duration_secs=120 to deem the run complete at 2025-08-14T03:53:30Z. Document provisioning.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "132",
                        "campaign_id": "2",
                        "name": "All — New Audience",
                        "category": "All",
                        "daily_budget": 210.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "created_at": "2025-08-14T03:51:30Z",
                        "updated_at": "2025-08-14T03:51:30Z"
                    },
                    "timestamp": "2025-08-14T03:51:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_132_20250814_1",
                        "adset_id": "132",
                        "name": "All — New Audience Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T03:51:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T03:51:30Z",
                    "ended_at": "2025-08-14T03:53:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-1",
                    "outputs_json": {
                        "adset_id": "132",
                        "ads_created": 1,
                        "final_type": "image",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"132\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"image\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_67",
        "instruction": "As the Mobile Format Pilot, and with the current time being 2025-08-14T03:54:00Z, assess Mobile adsets 110 and 111 specifically for the date 2025-08-13. Adjust any adset within {110,111} that has an active image creative and a CPA < 25 to video format at 2025-08-14T03:54:00Z using rotation request_id rot-012, justifying with 'mobile video uplift'. Should no adset be adjusted, proceed to forgo the budget bonus entirely without drafting a bonus plan. Treat the rotation process as concluded at 2025-08-14T03:55:00Z.",
        "actions": [
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:54:00Z",
                    "ended_at": "2025-08-14T03:55:00Z",
                    "status": "completed",
                    "request_id": "rot-012",
                    "input_ref": "rot-012",
                    "outputs_json": {
                        "rotation_request_id": "rot-012",
                        "rotated_adsets_count": 0,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T03:55:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-012\"",
                "\"rotated_adsets_count\": \"0\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\"",
                "\"ended_at\": \"2025-08-14T03:55:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_68",
        "instruction": "Act as the Electronics Expander, taking note that the time is 2025-08-14T03:55:30Z. Analyze the performance of adset 112 for the date 2025-08-13: if the CPA (calculated as spend divided by purchases) exceeds 7.0 and no creative rotations have occurred between 2025-08-07 and 2025-08-13, switch its active creative to video at 2025-08-14T03:55:30Z using rotation request_id rot-112-v1, with rationale 'video expansion'; designate the new ad according to the deterministic pattern rot-004-112-video, ensuring only one active creative. If not, leave it unchanged. Mark the process as finished at 2025-08-14T03:56:30Z.",
        "actions": [
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetCreativeRotationHistory",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:55:30Z",
                    "request_id": "rot-112-v1",
                    "rationale": "video expansion",
                    "ad_name": "rot-004-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:55:30Z",
                    "ended_at": "2025-08-14T03:56:30Z",
                    "status": "completed",
                    "request_id": "rot-112-v1",
                    "input_ref": "rot-112-v1",
                    "outputs_json": {
                        "rotation_request_id": "rot-112-v1",
                        "rotated_adsets_count": 1,
                        "run_status": "completed",
                        "run_type": "creative_rotation"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-112-v1\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_69",
        "instruction": "As the Snapshot Keeper, with the current time being 2025-08-14T03:56:30Z, arrange for the publication of plan_soc_039 targeting the date 2025-08-13. This should replicate the existing budgets, strategies, and active creative types for adsets 101, 106, 111, and 112, keeping them unchanged. Utilize created_at 2025-08-14T03:56:30Z and apply the timestamp 2025-08-14T03:58:00Z with request_id ap-037. Treat the plan as implemented as of 2025-08-14T03:59:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_039",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T03:56:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 3120.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_039",
                    "timestamp": "2025-08-14T03:58:00Z",
                    "request_id": "ap-037"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_039"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_039",
                    "status": "applied",
                    "applied_at": "2025-08-14T03:59:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T03:58:00Z",
                    "ended_at": "2025-08-14T03:59:00Z",
                    "status": "completed",
                    "request_id": "ap-037",
                    "input_ref": "ap-037",
                    "outputs_json": {
                        "plan_id": "plan_soc_039",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T03:59:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_039\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T03:59:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_70",
        "instruction": "As the Electronics Creative Owner and with the current moment being 2025-08-14T03:35:00Z, verify that adset 120 has exactly one active creative, a video titled 'Electronics Promo V2' (start_date 2025-08-14). Employ rotation request_id rot-001 with the rationale 'video upgrade for Electronics Promo'. The creative-change process should be considered finalized at 2025-08-14T03:36:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "120",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:35:00Z",
                    "request_id": "rot-001",
                    "rationale": "video upgrade for Electronics Promo",
                    "ad_name": "Electronics Promo V2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:35:00Z",
                    "ended_at": "2025-08-14T03:36:00Z",
                    "status": "completed",
                    "request_id": "rot-001",
                    "input_ref": "rot-001",
                    "outputs_json": {
                        "adset_id": "120",
                        "new_active": "Electronics Promo V2",
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"120\"",
                "\"new_active\": \"Electronics Promo V2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_71",
        "instruction": "As the Frequency Controller, with the current time being 2025-08-14T04:00:00Z, initiate the publication of plan_soc_040 for the date 2025-08-13. Reallocate 20 of the budget from adsets having frequency > 3.5 to those with frequency < 1.2 within each category, while ensuring the total for each category remains constant, adhering to the minimum allocation policy and budget rounding unit. Identify donors as all adsets over the threshold and recipients as those below it. If multiple recipients are present in a category, distribute each donor's 20 uniformly across the recipients, rounding according to the policy unit and resolving any tie by ascending adset_id order. Should the daily insights for 2025-08-13 lack a 'frequency' field for adsets 101, 106, 111, and 112, consider frequency unavailable and release a snapshot reflecting current budgets, strategies, and active creative types for those adsets, unchanged. Apply created_at 2025-08-14T04:00:00Z, apply timestamp 2025-08-14T04:02:00Z with request_id ap-038, and mark the plan as applied at 2025-08-14T04:03:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_040",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:00:00Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 3120.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_040",
                    "timestamp": "2025-08-14T04:02:00Z",
                    "request_id": "ap-038"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_040"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_040",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:03:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:02:00Z",
                    "ended_at": "2025-08-14T04:03:00Z",
                    "status": "completed",
                    "request_id": "ap-038",
                    "input_ref": "ap-038",
                    "outputs_json": {
                        "plan_id": "plan_soc_040",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T04:03:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_040\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:03:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_72",
        "instruction": "As the UGC Owner, with the current time logged at 2025-08-14T02:54:00Z, set up a new adset (adset_id 135) titled 'Apparel \u2014 UGC' under campaign_id '3', categorized as Apparel, with a daily_budget of 230, bid_strategy of lowest_cost, and status set to active. Make sure that an active video ad named 'Apparel UGC Video v1' commences on 2025-08-14. Utilize request_ids en-1 (adset), en-2 (ad), and en-3 (run). Finalize the provisioning process by 2025-08-14T02:55:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "135",
                        "campaign_id": "3",
                        "name": "Apparel — UGC",
                        "category": "Apparel",
                        "daily_budget": 230.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T02:54:00Z"
                    },
                    "timestamp": "2025-08-14T02:54:00Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_135_20250814_1",
                        "adset_id": "135",
                        "name": "Apparel UGC Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T02:54:00Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T02:54:00Z",
                    "ended_at": "2025-08-14T02:55:00Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "135",
                        "ads_created": "1",
                        "final_type": "video",
                        "run_type": "provisioning",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"135\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_73",
        "instruction": "Assume the role of the Image Advocate, and the time is 2025-08-14T04:03:30Z. Ensure image parity by verifying that Mobile adsets 110 and 111 feature an image as the sole active creative on 2025-08-13. For any adsets where the active type isn't an image, change to image at 2025-08-14T04:03:30Z utilizing rotation request_id rot-010, naming the new ads precisely rot-010-<adset_id>-image and employing rationale 'image parity across Mobile'. Mark the rotation as complete at 2025-08-14T04:04:00Z.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "110",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T04:03:30Z",
                    "request_id": "rot-010",
                    "rationale": "image parity across Mobile",
                    "ad_name": "rot-010-110-image"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "111",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T04:03:30Z",
                    "request_id": "rot-010",
                    "rationale": "image parity across Mobile",
                    "ad_name": "rot-010-111-image"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:03:30Z",
                    "ended_at": "2025-08-14T04:04:00Z",
                    "status": "completed",
                    "request_id": "rot-010",
                    "input_ref": "rot-010",
                    "outputs_json": {
                        "rotation_request_id": "rot-010",
                        "rotated_adsets_count": 2,
                        "run_status": "completed",
                        "ended_at": "2025-08-14T04:04:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-010\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_74",
        "instruction": "Act as the ROAS Booster, and the time is 2025-08-14T04:04:30Z. Implement plan_soc_041 for the date 2025-08-13. In each category, increase the budget by +5 for adsets with ROAS \u2265 2.0 and subtract \u22125 from adsets with ROAS < 1.0, ensuring category totals are maintained and adhering to policy minimum allocation and budget rounding unit. Calculate ROAS from the daily insights of 2025-08-13 as revenue \u00f7 spend. Should a category lack donors or recipients, refrain from making changes in that category. Utilize created_at 2025-08-14T04:04:30Z. Apply timestamp 2025-08-14T04:06:00Z with request_id ap-039 and regard the plan as applied at 2025-08-14T04:07:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_041",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:04:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 4120.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_041",
                    "timestamp": "2025-08-14T04:06:00Z",
                    "request_id": "ap-039"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_041"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_041",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:07:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:06:00Z",
                    "ended_at": "2025-08-14T04:07:00Z",
                    "status": "completed",
                    "request_id": "ap-039",
                    "input_ref": "ap-039",
                    "outputs_json": {
                        "plan_id": "plan_soc_041",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T04:07:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_041\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:07:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_75",
        "instruction": "As the Creative Trials Owner, at the time 2025-08-14T04:07:30Z, manage the provisioning of adset 136 (category Home) titled 'Home \u2014 Creative Trials' within campaign_id '5' with a daily_budget of 230, using the bid_strategy lowest_cost, and ensure its status is active, while keeping budget policies compliant. Ensure there is exactly one active video ad named 'Home Creative Trials - Video v1' starting on 2025-08-14 (end_date None) by verifying that no other ads are active under adset 136. Employ request_ids en-1 (adset) and en-2 (ad). Consider the provisioning process complete at 2025-08-14T04:09:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "136",
                        "campaign_id": "5",
                        "name": "Home — Creative Trials",
                        "category": "Home",
                        "daily_budget": 230.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T04:07:30Z"
                    },
                    "timestamp": "2025-08-14T04:07:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_136_20250814_1",
                        "adset_id": "136",
                        "name": "Home Creative Trials - Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T04:07:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "136"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T04:07:30Z",
                    "ended_at": "2025-08-14T04:09:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "136",
                        "ads_created": 1,
                        "final_type": "video",
                        "run_type": "provisioning",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"136\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_76",
        "instruction": "As the All-Category Flattener, at the time of 2025-08-14T04:08:30Z, implement plan_soc_042 for the date 2025-08-13 to align budgets in category All to be within \u00b115 of the category\u2019s mean, ensuring compliance with policy rounding. If the budgets are already within the specified tolerance, maintain them as they are. Refer to created_at 2025-08-14T04:08:30Z. Apply the timestamp 2025-08-14T04:10:00Z (request_id ap-040) and regard the plan as implemented at 2025-08-14T04:11:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_042",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:08:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1180.0
                        }
                    ],
                    "total_budget": 1180.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_042",
                    "timestamp": "2025-08-14T04:10:00Z",
                    "request_id": "ap-040"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_042"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_042",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:11:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:10:00Z",
                    "ended_at": "2025-08-14T04:11:00Z",
                    "status": "completed",
                    "request_id": "ap-040",
                    "input_ref": "ap-040",
                    "outputs_json": {
                        "plan_id": "plan_soc_042",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T04:11:00Z",
                        "run_status": "completed",
                        "run_type": "plan_apply"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_042\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:11:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_77",
        "instruction": "Acting as the Baseline Consolidator at the time 2025-08-14T04:11:30Z, ensure adsets 104 and 101 switch to video on 2025-08-14T04:11:30Z using the rotation request_id rot-013 with the rationale 'consolidate video baseline'. Only one creative should be active. Mark the rotation as concluded at 2025-08-14T04:12:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:11:30Z",
                    "request_id": "rot-013",
                    "rationale": "consolidate video baseline",
                    "ad_name": "rot-013-104-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "101",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:11:30Z",
                    "request_id": "rot-013",
                    "rationale": "consolidate video baseline",
                    "ad_name": "rot-013-101-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:11:30Z",
                    "ended_at": "2025-08-14T04:12:30Z",
                    "status": "completed",
                    "request_id": "rot-013",
                    "input_ref": "rot-013",
                    "outputs_json": {
                        "rotation_request_id": "rot-013",
                        "rotated_adsets_count": 2,
                        "run_type": "creative_rotation",
                        "run_status": "completed",
                        "ended_at": "2025-08-14T04:12:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-013\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_78",
        "instruction": "In your role as the Revenue Shifter at 2025-08-14T04:12:30Z, dispatch plan_soc_043 for the date 2025-08-13 to redistribute the budget according to the revenue data from the past 7 days: reallocate +20 from adset 107 (Toys) to adset 112 (Electronics), ensuring total balances remain intact and adhering to policy min_budget_allocation and budget_rounding_unit for the period 2025-08-07..2025-08-13. Record as created on 2025-08-14T04:12:30Z. Implement at 2025-08-14T04:14:00Z (request_id ap-041) and regard the plan as implemented by 2025-08-14T04:15:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetSalesByCategoryRange",
                "arguments": {
                    "category": "Electronics",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetSalesByCategoryRange",
                "arguments": {
                    "category": "Toys",
                    "start_date": "2025-08-07",
                    "end_date": "2025-08-13"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_043",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:12:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "107",
                            "budget": 380.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 720.0
                        }
                    ],
                    "total_budget": 1100.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_043",
                    "timestamp": "2025-08-14T04:14:00Z",
                    "request_id": "ap-041"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_043"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_043",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:15:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:14:00Z",
                    "ended_at": "2025-08-14T04:15:00Z",
                    "status": "completed",
                    "request_id": "ap-041",
                    "input_ref": "ap-041",
                    "outputs_json": {
                        "plan_id": "plan_soc_043",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T04:15:00Z",
                        "run_status": "completed",
                        "run_type": "plan_apply"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_043\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T04:15:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_79",
        "instruction": "Act as the Accessories Creative Owner with the timestamp 2025-08-14T04:15:30Z. By 2025-08-14T04:16:00Z, make sure that adset 130 concludes with precisely one active IMAGE creative labeled rot-010-130-image, utilizing rotation request_id rot-010 with the explanation 'single-active with new image'. If adset 130 lacks an active creative at the initial time, first establish a single active baseline creative with deterministic ad_id auto_130_20250814_1 named 'Accessories Promo \u2014 Video v1'. Assume the rotation commenced at 2025-08-14T04:15:30Z and finalized at 2025-08-14T04:17:00Z.",
        "actions": [
            {
                "name": "GetAdsByAdsetId",
                "arguments": {
                    "adset_id": "130"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_130_20250814_1",
                        "adset_id": "130",
                        "name": "Accessories Promo — Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T04:15:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "130",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T04:16:00Z",
                    "request_id": "rot-010",
                    "rationale": "single-active with new image",
                    "ad_name": "rot-010-130-image"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:15:30Z",
                    "ended_at": "2025-08-14T04:17:00Z",
                    "status": "completed",
                    "request_id": "rot-010",
                    "input_ref": "rot-010",
                    "outputs_json": {
                        "rotation_request_id": "rot-010",
                        "rotated_adsets_count": 1,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-010\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_80",
        "instruction": "Function as the Drift Controller with the time set at 2025-08-14T04:15:30Z. Announce plan_soc_044 for the date 2025-08-13, restricting net spend drift compared to 2025-08-12 to \u00b150 in total, while reallocating +30 to Mobile and \u221230 from All. Distribute +20 to adset 110 and +10 to adset 111, and decrease adset 103 by \u221230, fulfilling the budget_rounding_unit. Reference created_at 2025-08-14T04:15:30Z. Apply the use timestamp 2025-08-14T04:17:00Z (request_id ap-042) and regard the plan as implemented at 2025-08-14T04:18:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_044",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:15:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "103",
                            "budget": 1150.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1020.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1010.0
                        }
                    ],
                    "total_budget": 3180.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_044",
                    "timestamp": "2025-08-14T04:17:00Z",
                    "request_id": "ap-042"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_044"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_044",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:18:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:17:00Z",
                    "ended_at": "2025-08-14T04:18:00Z",
                    "status": "completed",
                    "request_id": "ap-042",
                    "input_ref": "ap-042",
                    "outputs_json": {
                        "plan_id": "plan_soc_044",
                        "applied_adsets_count": 3,
                        "applied_at": "2025-08-14T04:18:00Z",
                        "run_status": "completed",
                        "run_type": "plan_apply"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_044\"",
                "\"applied_adsets_count\": \"3\"",
                "\"applied_at\": \"2025-08-14T04:18:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_81",
        "instruction": "Acting as the Stability Lead at 2025-08-14T04:18:30Z, rotate adset 110 to image at 2025-08-14T04:18:30Z utilizing rotation request_id rot-110-stb with rationale 'stabilize creative baseline'. Designate the new ad as rot-110-stb-110-image and enforce a single-active creative. Mark the rotation as complete at 2025-08-14T04:19:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "110",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T04:18:30Z",
                    "request_id": "rot-110-stb",
                    "rationale": "stabilize creative baseline",
                    "ad_name": "rot-110-stb-110-image"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:18:30Z",
                    "ended_at": "2025-08-14T04:19:30Z",
                    "status": "completed",
                    "request_id": "rot-110-stb",
                    "input_ref": "rot-110-stb",
                    "outputs_json": {
                        "rotation_request_id": "rot-110-stb",
                        "rotated_adsets_count": 1,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-110-stb\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_82",
        "instruction": "As the Home CTR Tuner at 2025-08-14T04:19:30Z, publish plan_soc_045 for the date 2025-08-13. Specify CTR precisely as clicks \u00f7 impressions for 2025-08-13 (consider only this date). From adsets 101..112 classified as 'Home', if there are at least two, reallocate 20 of budget from the lowest-CTR Home adset (on 2025-08-13) to the highest-CTR Home adset (on 2025-08-13); otherwise, duplicate the existing budgets, strategies, and active creative types without adjustment. Maintain the total for the Home category unchanged, adhere to min_budget_allocation and budget_rounding_unit as per policy, continue with current strategies unaltered, and replicate present active creative types. Utilize created_at timestamp 2025-08-14T04:19:30Z. Apply the apply timestamp 2025-08-14T04:21:00Z (request_id ap-043) and regard the plan as applied at 2025-08-14T04:22:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "104"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "108"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_045",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:19:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        }
                    ],
                    "total_budget": 500.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_045",
                    "timestamp": "2025-08-14T04:21:00Z",
                    "request_id": "ap-043"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_045"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_045",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:22:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:21:00Z",
                    "ended_at": "2025-08-14T04:22:00Z",
                    "status": "completed",
                    "input_ref": "ap-043",
                    "outputs_json": {
                        "plan_id": "plan_soc_045",
                        "changes": 0,
                        "applied_at": "2025-08-14T04:22:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_045\"",
                "\"changes\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:22:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_83",
        "instruction": "As the Clearance Owner, and at the time of 2025-08-14T04:22:30Z, handle the provisioning of a new adset (adset_id 137) entitled 'Electronics \u2014 Clearance' for campaign_id '6', under the category 'Electronics', with a daily_budget of 200, a bid_strategy of lowest_cost, and an active status; ensure created_at and updated_at are set to 2025-08-14T04:22:30Z. Guarantee an active video ad starts on 2025-08-14 named 'Electronics Clearance - Video v1'. Acknowledge provisioning completion at 2025-08-14T04:23:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "137",
                        "campaign_id": "6",
                        "name": "Electronics — Clearance",
                        "category": "Electronics",
                        "daily_budget": 200.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "created_at": "2025-08-14T04:22:30Z",
                        "updated_at": "2025-08-14T04:22:30Z"
                    },
                    "timestamp": "2025-08-14T04:22:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_137_20250814_1",
                        "adset_id": "137",
                        "name": "Electronics Clearance - Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T04:22:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T04:22:30Z",
                    "ended_at": "2025-08-14T04:23:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "137",
                        "ads_created": 1,
                        "final_type": "video",
                        "run_type": "provisioning",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"137\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_84",
        "instruction": "As the Clicks Booster, at the time of 2025-08-14T04:23:30Z, coordinate the publication of plan_soc_046 for the date 2025-08-13. Define clicks for selection employing only data from 2025-08-13. In each category, allocate +20 to adsets with clicks \u2265 500, financed by \u221220 from peers with clicks \u2264 100. If there are multiple donors and/or recipients in a category, consolidate all donor reductions into a pool, and distribute the pool equally among all recipients; round according to the policy budget_rounding_unit, and if a remainder persists post-rounding, assign extra units to recipients in ascending adset_id order. Should a category lack qualifying donors (\u2264 100) on 2025-08-13, maintain existing budgets, strategies, and active creative types for the adsets you have reviewed. Set created_at to 2025-08-14T04:23:30Z. Utilize apply timestamp 2025-08-14T04:25:00Z with request_id ap-044 and recognize the plan as applied at 2025-08-14T04:26:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_046",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:23:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 3120.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_046",
                    "timestamp": "2025-08-14T04:25:00Z",
                    "request_id": "ap-044"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_046"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_046",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:26:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:25:00Z",
                    "ended_at": "2025-08-14T04:26:00Z",
                    "status": "completed",
                    "request_id": "ap-044",
                    "input_ref": "ap-044",
                    "outputs_json": {
                        "plan_id": "plan_soc_046",
                        "applied_adsets_count": 0,
                        "applied_at": "2025-08-14T04:26:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_046\"",
                "\"applied_adsets_count\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:26:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_85",
        "instruction": "As the Unified Experiment Lead, at the time of 2025-08-14T04:26:30Z, switch adsets 102 and 112 to video format using rotation request_id rot-014 with the reason being 'unify creative for experiment', ensuring only one creative is active. Mark the rotation as finalized at 2025-08-14T04:27:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "102",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:26:30Z",
                    "request_id": "rot-014",
                    "rationale": "unify creative for experiment",
                    "ad_name": "rot-014-102-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:26:30Z",
                    "request_id": "rot-014",
                    "rationale": "unify creative for experiment",
                    "ad_name": "rot-014-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:26:30Z",
                    "ended_at": "2025-08-14T04:27:30Z",
                    "status": "completed",
                    "request_id": "rot-014",
                    "input_ref": "rot-014",
                    "outputs_json": {
                        "rotation_request_id": "rot-014",
                        "rotated_adsets_count": 2,
                        "run_type": "creative_rotation",
                        "run_status": "completed",
                        "ended_at": "2025-08-14T04:27:30Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-014\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_86",
        "instruction": "Operating as the Mobile Percentile Setter, the time is 2025-08-14T04:27:30Z. Release plan_soc_047 for the date 2025-08-13 that aligns Mobile budgets with the 25th percentile (calculated based on Mobile adset daily budgets on 2025-08-13), decreasing only those that exceed that percentile while maintaining the overall Mobile category total intact. Retain existing strategies as they are and replicate the current active creative types. Use the created_at time of 2025-08-14T04:27:30Z. Apply the changes with timestamp 2025-08-14T04:29:00Z using request_id ap-045, mandate verification, and regard the plan as implemented at 2025-08-14T04:30:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_047",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:27:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ],
                    "total_budget": 2000.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_047",
                    "timestamp": "2025-08-14T04:29:00Z",
                    "request_id": "ap-045"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_047"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_047",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:30:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:29:00Z",
                    "ended_at": "2025-08-14T04:30:00Z",
                    "status": "completed",
                    "input_ref": "ap-045",
                    "outputs_json": {
                        "plan_id": "plan_soc_047",
                        "changes": 0,
                        "applied_at": "2025-08-14T04:30:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_047\"",
                "\"changes\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:30:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_87",
        "instruction": "Take charge as the Cross-Promo Creative Owner with the time marked at 2025-08-14T04:30:30Z. Ensure adset 125 is present under campaign_id '2' named 'All \u2014 Cross-Promo' with category 'All', daily_budget 200, bid_strategy lowest_cost, and status active; make sure to set created_at and updated_at to 2025-08-14T04:30:30Z. At 2025-08-14T04:31:00Z, transition that adset\u2019s active creative to video using rotation request_id rot-015, naming the new ad 'Cross-Promo V2', with the rationale 'add Cross-Promo V2 and enforce single-active'. Mark the rotation as complete at 2025-08-14T04:32:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "125",
                        "campaign_id": "2",
                        "name": "All — Cross-Promo",
                        "category": "All",
                        "daily_budget": 200.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "created_at": "2025-08-14T04:30:30Z",
                        "updated_at": "2025-08-14T04:30:30Z"
                    },
                    "timestamp": "2025-08-14T04:30:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "125",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:31:00Z",
                    "request_id": "rot-015",
                    "rationale": "add Cross-Promo V2 and enforce single-active",
                    "ad_name": "Cross-Promo V2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:31:00Z",
                    "ended_at": "2025-08-14T04:32:00Z",
                    "status": "completed",
                    "request_id": "rot-015",
                    "input_ref": "rot-015",
                    "outputs_json": {
                        "rotation_request_id": "rot-015",
                        "rotated_adsets_count": 1,
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-015\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_88",
        "instruction": "Act as the ROAS Migrator with the time set to 2025-08-14T04:31:30Z. Release plan_soc_048 for the date 2025-08-13. Specify ROAS precisely as revenue \u00f7 spend using solely the data from 2025-08-13. Assess adsets 101, 106, 110, 111, and 112. Within every category, if there's a minimum of one donor (ROAS < 0.8) and at least one recipient (ROAS \u2265 2.5), relocate 15 of the budget from each donor and allocate the pooled funds to the single highest-ROAS recipient in that category; ensure the category total remains unchanged. If not, replicate current budgets, maintain existing strategies, and continue with the currently active creative types. Employ created_at 2025-08-14T04:31:30Z. Set the apply timestamp to 2025-08-14T04:33:00Z with request_id ap-046 and determine the plan as applied at 2025-08-14T04:34:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "110"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "101",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "106",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "110",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "111",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "GetDailyInsightsForAdset",
                "arguments": {
                    "adset_id": "112",
                    "date": "2025-08-13"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_048",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:31:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "110",
                            "name": "App Installs - Android",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "110",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "110",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "110",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 700.0
                        }
                    ],
                    "total_budget": 4120.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_048",
                    "timestamp": "2025-08-14T04:33:00Z",
                    "request_id": "ap-046"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_048"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_048",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:34:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:33:00Z",
                    "ended_at": "2025-08-14T04:34:00Z",
                    "status": "completed",
                    "input_ref": "ap-046",
                    "outputs_json": {
                        "plan_id": "plan_soc_048",
                        "changes": 0,
                        "applied_at": "2025-08-14T04:34:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_048\"",
                "\"changes\": \"0\"",
                "\"applied_at\": \"2025-08-14T04:34:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_89",
        "instruction": "You hold the title of Scale Captain and the current time is 2025-08-14T04:34:30Z. Handle the rotation of adset 104 to video at 2025-08-14T04:34:30Z by using rotation request_id rot-015 with the rationale 'scale proven type', ensuring only one active creative. For adset 111, initiate by checking the active creative type; if it is already a video on 2025-08-14T04:34:30Z, omit rotation as a no-op and document the skip reason 'already_in_target_state'. Adhere to the policy default pattern rot-004-<adset_id>-<type> for naming new creatives; for this instance, the new ad name is rot-004-104-video. Finalize the rotation by 2025-08-14T04:35:30Z.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:34:30Z",
                    "request_id": "rot-015",
                    "rationale": "scale proven type",
                    "ad_name": "rot-004-104-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:34:30Z",
                    "ended_at": "2025-08-14T04:35:30Z",
                    "status": "completed",
                    "request_id": "rot-015",
                    "input_ref": "rot-015",
                    "outputs_json": {
                        "rotation_request_id": "rot-015",
                        "rotated_adsets_count": 1,
                        "run_type": "creative_rotation",
                        "run_status": "completed",
                        "noops_skipped": [
                            {
                                "adset_id": "111",
                                "reason": "already_in_target_state"
                            }
                        ]
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-015\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_90",
        "instruction": "Your role is the Two-Pair Shifter and the time now is 2025-08-14T04:35:30Z. Execute the publication of plan_soc_049 for the date 2025-08-13 with these specific outcomes: budgets at 102:620, 103:1150, 106:530, 107:370 (USD), achieved exclusively by +30 from 103\u2192102 and +30 from 107\u2192106; strategies should match the existing DB values precisely; creatives should reflect the currently active type of each adset; other adsets must remain unchanged and overall totals should stay stable. Refer to 2025-08-14T04:37:00Z (request_id ap-047) as the apply instant and 2025-08-14T04:38:00Z as the applied_at for audit purposes.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_049",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:35:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "102",
                            "budget": 620.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 1150.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 530.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 370.0
                        }
                    ],
                    "total_budget": 2670.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_049",
                    "timestamp": "2025-08-14T04:37:00Z",
                    "request_id": "ap-047"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_049"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_049",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:38:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:37:00Z",
                    "ended_at": "2025-08-14T04:38:00Z",
                    "status": "completed",
                    "input_ref": "ap-047",
                    "outputs_json": {
                        "plan_id": "plan_soc_049",
                        "applied_adsets_count": 4,
                        "applied_at": "2025-08-14T04:38:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_049\"",
                "\"applied_adsets_count\": \"4\"",
                "\"applied_at\": \"2025-08-14T04:38:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_91",
        "instruction": "As the Mobile Performance Owner, at the time of 2025-08-14T04:38:30Z, organize the provisioning of a new Mobile adset (adset_id 138, category Mobile) titled 'Mobile \u2014 Performance' within campaign_id '7'. Set a daily_budget of 260, use the bid_strategy lowest_cost, and mark the status as active. Make sure an active video ad called 'Mobile \u2014 Performance Video v1' initiates on 2025-08-14, meeting the single-active condition. Complete the provisioning by 2025-08-14T04:39:30Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "138",
                        "campaign_id": "7",
                        "name": "Mobile — Performance",
                        "category": "Mobile",
                        "daily_budget": 260.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T04:38:30Z"
                    },
                    "timestamp": "2025-08-14T04:38:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_138_20250814_1",
                        "adset_id": "138",
                        "name": "Mobile — Performance Video v1",
                        "creative_type": "video",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T04:38:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T04:38:30Z",
                    "ended_at": "2025-08-14T04:39:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "138",
                        "ads_created": 1,
                        "final_type": "video",
                        "run_type": "provisioning",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"138\"",
                "\"ads_created\": \"1\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_92",
        "instruction": "Act as the Bid Simplifier at the timestamp of 2025-08-14T04:39:30Z. Implement plan_soc_050 for the date 2025-08-13. Secure adset 111 at a cost_cap=2.5 and adset 106 at a cost_cap=18.0. Adjust adset 101 to the lowest_cost setting; leave budgets as they are (101:920, 106:500, 111:1000). Apply the timestamp 2025-08-14T04:41:00Z (request_id ap-048) and regard the plan as implemented by 2025-08-14T04:42:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "111"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_050",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:39:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "111",
                            "name": "App Installs - iOS",
                            "category": "Mobile",
                            "campaign_id": "7"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "111",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 2.5
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "111",
                            "creative_type": "video"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 920.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 500.0
                        },
                        {
                            "adset_id": "111",
                            "budget": 1000.0
                        }
                    ],
                    "total_budget": 2420.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_050",
                    "timestamp": "2025-08-14T04:41:00Z",
                    "request_id": "ap-048"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_050"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_050",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:42:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:41:00Z",
                    "ended_at": "2025-08-14T04:42:00Z",
                    "status": "completed",
                    "request_id": "ap-048",
                    "input_ref": "ap-048",
                    "outputs_json": {
                        "plan_id": "plan_soc_050",
                        "applied_adsets_count": 1,
                        "applied_at": "2025-08-14T04:42:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_050\"",
                "\"applied_adsets_count\": \"1\"",
                "\"applied_at\": \"2025-08-14T04:42:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_93",
        "instruction": "As the Type Balancer, the current time is 2025-08-14T04:42:30Z. Adjust adsets 101 and 105 to use video format at 2025-08-14T04:42:30Z with rotation request_id rot-016, noting the rationale 'type-balancing by category'. Ensure single-active is enforced. The run should be marked complete by 2025-08-14T04:43:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "101",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:42:30Z",
                    "request_id": "rot-016",
                    "rationale": "type-balancing by category",
                    "ad_name": "rot-016-101-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "105",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:42:30Z",
                    "request_id": "rot-016",
                    "rationale": "type-balancing by category",
                    "ad_name": "rot-016-105-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:42:30Z",
                    "ended_at": "2025-08-14T04:43:00Z",
                    "status": "completed",
                    "request_id": "rot-016",
                    "input_ref": "rot-016",
                    "outputs_json": {
                        "rotation_request_id": "rot-016",
                        "rotated_adsets_count": 2,
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-016\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_94",
        "instruction": "Acting as the Percentile Governor, the time is logged as 2025-08-14T04:43:30Z. Release plan_soc_051 for the date 2025-08-13: limit Electronics by transitioning 50 from adset 101 to Apparel adset 105; maintain current strategies and mirror existing active creatives; ensure the total remains unchanged with budgets set in increments of 10. Documented at created_at 2025-08-14T04:43:30Z, apply timestamp at 2025-08-14T04:45:00Z (request_id ap-049), and finalize the plan's application by 2025-08-14T04:46:00Z.",
        "actions": [
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "101"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "105"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_051",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:43:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "101",
                            "name": "Electronics - CA",
                            "category": "Electronics",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "105",
                            "name": "Fall Fashion - Men",
                            "category": "Apparel",
                            "campaign_id": "3"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "101",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 32.0
                        },
                        {
                            "adset_id": "105",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "101",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "105",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "101",
                            "budget": 870.0
                        },
                        {
                            "adset_id": "105",
                            "budget": 800.0
                        }
                    ],
                    "total_budget": 1670.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_051",
                    "timestamp": "2025-08-14T04:45:00Z",
                    "request_id": "ap-049"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_051"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_051",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:46:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:45:00Z",
                    "ended_at": "2025-08-14T04:46:00Z",
                    "status": "completed",
                    "request_id": "ap-049",
                    "input_ref": "ap-049",
                    "outputs_json": {
                        "plan_id": "plan_soc_051",
                        "applied_adsets_count": 2,
                        "applied_at": "2025-08-14T04:46:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_051\"",
                "\"applied_adsets_count\": \"2\"",
                "\"applied_at\": \"2025-08-14T04:46:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_95",
        "instruction": "As the Seasonal Creative Owner, at the time of 2025-08-14T04:46:30Z, confirm that adset 123 is set up as 'Apparel \u2014 Seasonal' within campaign_id '3', categorized under Apparel, with a daily_budget of 260, using bid_strategy lowest_cost, and maintaining an active status. Make sure it initially features an active image ad titled 'Seasonal V1' beginning on 2025-08-14. At 2025-08-14T04:47:00Z, switch the active creative to a new video ad called 'Seasonal V2' by utilizing rotation request_id rot-020, justified by 'Seasonal V2 rollout', and ensure single-active enforcement. Mark the provisioning as complete at 2025-08-14T04:48:30Z, with the rotation concluding at 2025-08-14T04:48:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "123",
                        "campaign_id": "3",
                        "name": "Apparel — Seasonal",
                        "category": "Apparel",
                        "daily_budget": 260.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T04:46:30Z"
                    },
                    "timestamp": "2025-08-14T04:46:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_123_20250814_1",
                        "adset_id": "123",
                        "name": "Seasonal V1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T04:46:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T04:46:30Z",
                    "ended_at": "2025-08-14T04:48:30Z",
                    "status": "completed",
                    "request_id": "en-3",
                    "input_ref": "en-2",
                    "outputs_json": {
                        "adset_id": "123",
                        "ads_created": 1,
                        "final_type": "image"
                    },
                    "errors_json": null
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "123",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:47:00Z",
                    "request_id": "rot-020",
                    "rationale": "Seasonal V2 rollout",
                    "ad_name": "Seasonal V2"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:47:00Z",
                    "ended_at": "2025-08-14T04:48:00Z",
                    "status": "completed",
                    "request_id": "rot-020",
                    "input_ref": "rot-020",
                    "outputs_json": {
                        "adset_id": "123",
                        "new_active": "Seasonal V2",
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"123\"",
                "\"new_active\": \"Seasonal V2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_96",
        "instruction": "Functioning as the Video Expansion Lead at 2025-08-14T05:20:00Z, transition adset 112 to video format precisely at 2025-08-14T05:20:00Z, utilizing rotation request_id rot-020 and supporting the action with the rationale 'category parity'. For adset 102, should its active creative already be an image, regard it as a no-op stating 'already_in_target_state'. Uphold the single-active requirement. Conclude the operation by 2025-08-14T05:21:00Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T05:20:00Z",
                    "request_id": "rot-020",
                    "rationale": "category parity",
                    "ad_name": "rot-020-112-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T05:20:00Z",
                    "ended_at": "2025-08-14T05:21:00Z",
                    "status": "completed",
                    "request_id": "rot-020",
                    "input_ref": "rot-020",
                    "outputs_json": {
                        "rotation_request_id": "rot-020",
                        "rotated_adsets_count": 1,
                        "rotation_noops": [
                            {
                                "adset_id": "102",
                                "reason": "already_in_target_state"
                            }
                        ],
                        "run_status": "completed",
                        "ended_at": "2025-08-14T05:21:00Z"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-020\"",
                "\"rotated_adsets_count\": \"1\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_97",
        "instruction": "As the Video Uplift Lead, the current time is 2025-08-14T04:50:30Z. At this time, switch adsets 112 and 108 to video by utilizing rotation request_id rot-017 with the explanation 'video uplift across categories'. Ensure only one creative is active and document the rotation as finalized at 2025-08-14T04:51:30Z.",
        "actions": [
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:50:30Z",
                    "request_id": "rot-017",
                    "rationale": "video uplift across categories",
                    "ad_name": "rot-017-112-video"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "108",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:50:30Z",
                    "request_id": "rot-017",
                    "rationale": "video uplift across categories",
                    "ad_name": "rot-017-108-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T04:50:30Z",
                    "ended_at": "2025-08-14T04:51:30Z",
                    "status": "completed",
                    "request_id": "rot-017",
                    "input_ref": "rot-017",
                    "outputs_json": {
                        "rotation_request_id": "rot-017",
                        "rotated_adsets_count": 2,
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"rotation_request_id\": \"rot-017\"",
                "\"rotated_adsets_count\": \"2\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_98",
        "instruction": "Being the Share-of-Voice Planner, note that the time is 2025-08-14T04:51:30Z. Proceed to release plan_soc_053 for the date 2025-08-13 by distributing the All category's budget into its corresponding categories based on that date's viewership percentages, while keeping the total unchanged. Capture the snapshot at a budget total of 3380, adhering to policy minimums and rounding rules: assign 103 to the policy minimum (100) and decrease 112 by the same value to maintain the unchanged total, resulting in 103=100, 112=1070, 102=890, 106=740, 107=580. Mark 2025-08-14T04:51:30Z as created_at. Utilize the apply timestamp 2025-08-14T04:53:00Z with request_id ap-051, and register it as applied at 2025-08-14T04:54:00Z. Log the run as finalized with applied_at 2025-08-14T04:54:00Z and run_status completed.",
        "actions": [
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "103"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "112"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "102"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "106"
                },
            },
            {
                "name": "GetAdsetDetailsById",
                "arguments": {
                    "adset_id": "107"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "min_budget_allocation"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "budget_rounding_unit"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "currency"
                },
            },
            {
                "name": "GetPolicyParameter",
                "arguments": {
                    "param_name": "timezone"
                },
            },
            {
                "name": "FreezePlan",
                "arguments": {
                    "plan_id": "plan_soc_053",
                    "date": "2025-08-13",
                    "created_at": "2025-08-14T04:51:30Z",
                    "author": "automation_agent",
                    "checksum": "CHK001",
                    "policy_snapshot": {
                        "min_budget_allocation": 100,
                        "budget_rounding_unit": 10,
                        "currency": "USD",
                        "timezone": "UTC"
                    },
                    "adset_mapping": [
                        {
                            "adset_id": "102",
                            "name": "Apparel - CA",
                            "category": "Apparel",
                            "campaign_id": "1"
                        },
                        {
                            "adset_id": "103",
                            "name": "Brand - Video Ads",
                            "category": "All",
                            "campaign_id": "2"
                        },
                        {
                            "adset_id": "106",
                            "name": "Holiday - Home Goods",
                            "category": "Home",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "107",
                            "name": "Holiday - Toys",
                            "category": "Toys",
                            "campaign_id": "5"
                        },
                        {
                            "adset_id": "112",
                            "name": "Electronics - UK",
                            "category": "Electronics",
                            "campaign_id": "1"
                        }
                    ],
                    "strategies": [
                        {
                            "adset_id": "102",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "103",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "106",
                            "bid_strategy": "cost_cap",
                            "bid_amount": 18.0
                        },
                        {
                            "adset_id": "107",
                            "bid_strategy": "lowest_cost"
                        },
                        {
                            "adset_id": "112",
                            "bid_strategy": "lowest_cost"
                        }
                    ],
                    "creatives": [
                        {
                            "adset_id": "102",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "103",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "106",
                            "creative_type": "image"
                        },
                        {
                            "adset_id": "107",
                            "creative_type": "video"
                        },
                        {
                            "adset_id": "112",
                            "creative_type": "image"
                        }
                    ],
                    "allocations": [
                        {
                            "adset_id": "102",
                            "budget": 890.0
                        },
                        {
                            "adset_id": "103",
                            "budget": 100.0
                        },
                        {
                            "adset_id": "106",
                            "budget": 740.0
                        },
                        {
                            "adset_id": "107",
                            "budget": 580.0
                        },
                        {
                            "adset_id": "112",
                            "budget": 1070.0
                        }
                    ],
                    "total_budget": 3380.0
                },
            },
            {
                "name": "ApplyPlanAllocations",
                "arguments": {
                    "plan_id": "plan_soc_053",
                    "timestamp": "2025-08-14T04:53:00Z",
                    "request_id": "ap-051"
                },
            },
            {
                "name": "VerifyPlanAgainstAdsets",
                "arguments": {
                    "plan_id": "plan_soc_053"
                },
            },
            {
                "name": "UpdatePlanStatus",
                "arguments": {
                    "plan_id": "plan_soc_053",
                    "status": "applied",
                    "applied_at": "2025-08-14T04:54:00Z"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "plan_apply",
                    "started_at": "2025-08-14T04:53:00Z",
                    "ended_at": "2025-08-14T04:54:00Z",
                    "status": "completed",
                    "request_id": "ap-051",
                    "input_ref": "ap-051",
                    "outputs_json": {
                        "plan_id": "plan_soc_053",
                        "applied_adsets_count": 5,
                        "applied_at": "2025-08-14T04:54:00Z",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"plan_id\": \"plan_soc_053\"",
                "\"applied_adsets_count\": \"5\"",
                "\"applied_at\": \"2025-08-14T04:54:00Z\"",
                "\"run_type\": \"plan_apply\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_99",
        "instruction": "As the Evergreen Owner, handle the task at 2025-08-14T04:54:30Z. Set up a new adset 'Electronics \u2014 Evergreen' (adset_id 139) under campaign_id '1' with the category Electronics, a daily_budget of 240, lowest_cost as the bid_strategy, and a status of active (updated_at 2025-08-14T04:54:30Z). Make sure an active image ad initiates on 2025-08-14, titled 'Electronics Evergreen - Image v1'. Change the adset\u2019s active creative to a video at 2025-08-14T04:56:00Z using rotation request_id rot-ever-1, with the reason 'evergreen video', naming the new ad rot-ever-1-139-video. Consider provisioning and rotation finished at 2025-08-14T04:56:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "139",
                        "campaign_id": "1",
                        "name": "Electronics — Evergreen",
                        "category": "Electronics",
                        "daily_budget": 240.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T04:54:30Z"
                    },
                    "timestamp": "2025-08-14T04:54:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_139_20250814_1",
                        "adset_id": "139",
                        "name": "Electronics Evergreen - Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T04:54:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "139",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:56:00Z",
                    "request_id": "rot-ever-1",
                    "rationale": "evergreen video",
                    "ad_name": "rot-ever-1-139-video"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "provisioning",
                    "started_at": "2025-08-14T04:54:30Z",
                    "ended_at": "2025-08-14T04:56:00Z",
                    "status": "completed",
                    "request_id": "rot-ever-1",
                    "input_ref": "rot-ever-1",
                    "outputs_json": {
                        "adset_id": "139",
                        "ads_created": 2,
                        "final_type": "video",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"139\"",
                "\"ads_created\": \"2\"",
                "\"final_type\": \"video\"",
                "\"run_type\": \"provisioning\"",
                "\"run_status\": \"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_100",
        "instruction": "As the Toys Creative Owner, manage tasks starting at 2025-08-14T03:42:30Z. Initiate adset 122 under campaign_id '5', identified as 'Toys \u2014 Expansion' (category Toys), with a daily_budget of 220, implementing the lowest_cost bid_strategy, and marking status as active. Guarantee an active IMAGE ad commences on 2025-08-14, labeled 'Toys Expansion Image v1'. Switch the adset\u2019s active creative to VIDEO at 2025-08-14T03:43:00Z using rotation request_id rot-100, with the rationale 'video test', and title the new ad 'rot-100-122-video'. Ensure single-active enforcement by pausing the previous active. Conclude rotation activities at 2025-08-14T03:44:00Z.",
        "actions": [
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "adsets",
                    "row": {
                        "adset_id": "122",
                        "campaign_id": "5",
                        "name": "Toys — Expansion",
                        "category": "Toys",
                        "daily_budget": 220.0,
                        "bid_strategy": "lowest_cost",
                        "status": "active",
                        "updated_at": "2025-08-14T03:42:30Z"
                    },
                    "timestamp": "2025-08-14T03:42:30Z",
                    "request_id": "en-1"
                },
            },
            {
                "name": "InsertEntity",
                "arguments": {
                    "table": "ads",
                    "row": {
                        "ad_id": "auto_122_20250814_1",
                        "adset_id": "122",
                        "name": "Toys Expansion Image v1",
                        "creative_type": "image",
                        "status": "active",
                        "start_date": "2025-08-14",
                        "end_date": null
                    },
                    "timestamp": "2025-08-14T03:42:30Z",
                    "request_id": "en-2"
                },
            },
            {
                "name": "RotateAdCreative",
                "arguments": {
                    "adset_id": "122",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:43:00Z",
                    "request_id": "rot-100",
                    "rationale": "video test",
                    "ad_name": "rot-100-122-video"
                },
            },
            {
                "name": "UpdateAdStatus",
                "arguments": {
                    "ad_id": "auto_122_20250814_1",
                    "status": "paused",
                    "timestamp": "2025-08-14T03:43:00Z",
                    "request_id": "en-3"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "run_type": "creative_rotation",
                    "started_at": "2025-08-14T03:43:00Z",
                    "ended_at": "2025-08-14T03:44:00Z",
                    "status": "completed",
                    "request_id": "en-4",
                    "input_ref": "rot-100",
                    "outputs_json": {
                        "adset_id": "122",
                        "new_active": "rot-100-122-video",
                        "run_type": "creative_rotation",
                        "run_status": "completed"
                    },
                    "errors_json": null
                }
            }
        ],
        "outputs": [
                "\"adset_id\": \"122\"",
                "\"new_active\": \"rot-100-122-video\"",
                "\"run_type\": \"creative_rotation\"",
                "\"run_status\": \"completed\""
        ]
    }
]
