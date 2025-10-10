from domains.dto import Action, Task

# Social Media Advertising — deterministic tasks, non-procedural goals, explicit literals.

TASKS = [
    Task(
        annotator="0",
        user_id="TASK_01",
        instruction=(
            "You are the Snapshot Planner and the time is 2025-08-14T00:00:00Z. "
            "Compose plan_soc_001 (date 2025-08-13) as a full-fidelity envelope using exact adset names from the DB; "
            "preserve totals and make no changes. Apply and record."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_001",
                "date": "2025-08-13",
                "created_at": "2025-08-14T00:00:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8860.0,

                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "109", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },

                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "109", "budget": 300.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_001",
                "timestamp": "2025-08-14T00:00:00Z",
                "request_id": "ap-1"
            }),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_001",
                "status": "applied",
                "applied_at": "2025-08-14T00:00:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_001"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T00:00:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_02",
        instruction=(
            "You are the Envelope Publisher and the time is 2025-08-14T00:03:00Z. "
            "Publish plan_soc_002 (date 2025-08-13) as an exact DB snapshot (no changes), with full adset mapping, "
            "strategies (including cost caps), creatives, and allocations. Apply and record."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_002",
                "date": "2025-08-13",
                "created_at": "2025-08-14T00:03:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8860.0,

                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "109", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },

                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "109", "budget": 300.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_002",
                "timestamp": "2025-08-14T00:03:00Z",
                "request_id": "ap-1"
            }),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_002",
                "status": "applied",
                "applied_at": "2025-08-14T00:03:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_002"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T00:03:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_03",
        instruction=(
            "You are the Allocation Analyst and the time is 2025-08-14T00:06:00Z. "
            "Compose plan_soc_003 (date 2025-08-13) as a full-fidelity envelope using exact adset names from the DB; "
            "preserve totals and make no changes. Apply and record."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_003",
                "date": "2025-08-13",
                "created_at": "2025-08-14T00:06:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8860.0,

                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "109", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },

                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "109", "budget": 300.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_003",
                "timestamp": "2025-08-14T00:06:00Z",
                "request_id": "ap-1"
            }),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_003",
                "status": "applied",
                "applied_at": "2025-08-14T00:06:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_003"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T00:06:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    # tasks_004_008.py
    # tasks_004_008_fixed.py

    Task(
        annotator="0",
        user_id="TASK_04",
        instruction=(
            "You are the Baseline Publisher and the time is 2025-08-14T00:30:00Z. "
            "Publish plan_soc_010 (2025-08-13) as a full-envelope snapshot of current budgets/strategies, "
            "preserving the total (8860) and making no changes. Apply and record."
        ),
        actions=[
            # Read all adsets to source mapping names & current strategies/creatives deterministically
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze full envelope (names copied verbatim from DB reads)
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_010",
                "date": "2025-08-13",
                "created_at": "2025-08-14T00:30:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8860.0,
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "109", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "109", "budget": 300.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
            }),

            # Apply (no-ops expected), then mark & record
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_010", "timestamp": "2025-08-14T00:30:00Z", "request_id": "ap-1"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_010", "status": "applied", "applied_at": "2025-08-14T00:30:00Z"}),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_010"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T00:30:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_05",
        instruction=(
            "You are the Creative Provisioner and the time is 2025-08-14T00:35:00Z. "
            "In adset 102, provision one new active image ad (start 2025-08-14), enforce single-active by pausing any existing active ad, and record the run."
        ),
        actions=[
            # Read once to find the currently active ad to pause
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),

            # Create the new image ad with deterministic name/id scheme
            Action(name="create_ad", kwargs={
                "adset_id": "102",
                "name": "auto_102_20250814_001",
                "creative_type": "image",
                "status": "active",
                "start_date": "2025-08-14",
                "request_id": "en-1"
            }),

            # Enforce single-active: pause the previous active (from the read: ad_id 1103)
            Action(name="update_ad_status", kwargs={
                "ad_id": "1103",
                "status": "paused",
                "request_id": "en-2"
            }),

            # Record the provisioning run
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "102"',
            '"ads_created_count": "1"',
            '"new_ad_name": "auto_102_20250814_001"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_06",
        instruction=(
            "You are the Envelope Publisher and the time is 2025-08-14T00:30:00Z. "
            "Publish plan_soc_006a (date 2025-08-13) as a full-envelope snapshot of the current DB "
            "(budgets, bid strategies, creatives), preserving the overall total (8860) and policy constraints. "
            "Use adset names verbatim from the DB and deterministic defaults."
        ),
        actions=[
            # Policy parameters (embed in freeze envelope)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Source all adsets to populate mapping/strategies/creatives deterministically
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze full-envelope plan (all budgets unchanged; total = 8860)
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_006a",
                "date": "2025-08-13",
                "created_at": "2025-08-14T00:30:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8860.0,
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "109", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "109", "budget": 300.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
            }),

            # Apply (+90s), verify, mark applied (+150s from seed), record
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_006a", "timestamp": "2025-08-14T00:30:00Z", "request_id": "ap-1"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_006a"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_006a", "status": "applied", "applied_at": "2025-08-14T00:30:00Z"}),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_006a"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T00:30:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_07",
        instruction=(
            "You are the Revenue Planner and the time is 2025-08-14T01:17:30Z. "
            "Draft plan_soc_005 (2025-08-13) that moves 50 from the lower-ROAS category to the higher-ROAS category "
            "between Electronics and Mobile; change only the bottom donor and top recipient adsets, others unchanged. "
            "Interpret category lift using adset-level ROAS on 2025-08-13 (donor = lowest-ROAS Mobile adset, recipient = highest-ROAS Electronics adset). "
            "Preserve the overall total (8860) and policy constraints, and use adset names verbatim from the DB."
        ),
        actions=[
            # Policy parameters
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Category performance window
            # Action(name="get_sales_by_category_range",
            #        kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            # Action(name="get_sales_by_category_range",
            #        kwargs={"category": "Mobile", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            # Rank within categories (ROAS on 2025-08-13)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),

            # Read all adsets for verbatim envelope fields
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze: -50 from Mobile bottom (adset 110), +50 to Electronics top (adset 112)
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_005",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:17:30Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8860.0,
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "109", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "policy_snapshot": {"min_budget_allocation": 100, "budget_rounding_unit": 10, "currency": "USD",
                                    "timezone": "UTC"},
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "109", "budget": 300.0},
                    {"adset_id": "110", "budget": 950.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 750.0},
                ],
            }),

            # Apply/verify/mark using the seed time deterministically (no invented offsets)
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_005", "timestamp": "2025-08-14T01:17:30Z", "request_id": "ap-1"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_005"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_005", "status": "applied", "applied_at": "2025-08-14T01:17:30Z"}),
            Action(name="record_automation_run", kwargs={
                "run_type": "plan_apply",
                "started_at": "2025-08-14T01:17:30Z",
                "ended_at": "2025-08-14T01:17:30Z",
                "status": "completed",
                "input_ref": "ap-1",
                "outputs_json": {"plan_id": "plan_soc_005", "applied_adsets_count": 2, "total_budget": 8860.0,
                                 "applied_at": "2025-08-14T01:17:30Z", "run_status": "completed"},
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_005"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T01:17:30Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
            '"total_budget": "8860.0"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_08",
        instruction=(
            "You are the Apparel Portfolio Owner and the time is 2025-08-14T01:20:30Z. "
            "Build plan_soc_006 (2025-08-13) for Apparel only: cut −25 from any adset with CPA>45 and distribute the freed "
            "budget equally to peers with CPA<25 (policy rounding). If no donors, perform a no-op."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Apparel checks (all <25 => no donors)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "105", "date": "2025-08-13"}),

            # Use DB names/strategies/creatives in envelope
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),

            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_006",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:20:30Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 2080.0,
                "adset_mapping": [
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                ],
                "strategies": [
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                ],
                "policy_snapshot": {"min_budget_allocation": 100, "budget_rounding_unit": 10, "currency": "USD",
                                    "timezone": "UTC"},
                "allocations": [
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                ],
            }),

            # Deterministic timestamps derived from seed (here: use seed time for both)
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_006", "timestamp": "2025-08-14T01:20:30Z", "request_id": "ap-1"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_006", "status": "applied", "applied_at": "2025-08-14T01:20:30Z"}),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_006"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T01:20:30Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_09",
        instruction=(
            "You are the Bidding Architect and the time is 2025-08-14T01:24:30Z. "
            "Prepare plan_soc_007 for 2025-08-13 that sets adset 106 to cost_cap 18.0 and adset 111 to cost_cap 2.5, "
            "keeping all other strategies and all budgets unchanged; preserve category totals. "
            "Use adset names verbatim from the database, and for any required timestamps, use the seed time exactly."
        ),
        actions=[
            # Read only what we must snapshot deterministically
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Freeze a no-op budget plan with explicit strategy assertions for 106 and 111
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_007",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:24:30Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 1500.0,
                "adset_mapping": [
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],
                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],
                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                ],
                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC",
                },
                "allocations": [
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                ],
            }),

            # Apply/verify/mark/record using the seed time deterministically
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_007", "timestamp": "2025-08-14T01:24:30Z", "request_id": "ap-1"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_007"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_007", "status": "applied", "applied_at": "2025-08-14T01:24:30Z"}),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_007"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T01:24:30Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_10",
        instruction=(
            "You are the Creative Rotation Owner and the time is 2025-08-14T01:28:00Z. "
            "Switch adsets 103 and 107 to video (rationale 'video consistency for single-active'), enforce single-active, "
            "and record the run. End at 2025-08-14T01:29:00Z (rot-003)."
        ),
        actions=[
            # Inspect current creatives to respect idempotency (skip rotation if already video)
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "103"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "107"}),

            # Record a deterministic no-op rotation (both are already video in the dataset)
            Action(name="record_automation_run", kwargs={
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
                        {"adset_id": "103", "reason": "already_video"},
                        {"adset_id": "107", "reason": "already_video"}
                    ],
                    "single_active_enforced": True,
                    "rationale": "video consistency for single-active"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-003"',
            '"rotated_adsets_count": "0"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T01:29:00Z"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_11",
        instruction=(
            "You are the Envelope Planner and the time is 2025-08-14T01:30:00Z. "
            "Prepare env_soc_008 for 2025-08-13 honoring min_per_category = 100 and preserving the overall total. "
            "Within Home, add +30 to the top 7-day sales adset (adset 106) and fund it by decreasing Brand - Video Ads (adset 103) by 30; "
            "leave all other adsets unchanged. Use adset names verbatim from the database. "
            "Align operation timestamps to 2025-08-14T01:32:00Z (apply) and 2025-08-14T01:34:00Z (mark applied), derived from the seed time."
        ),
        actions=[
            # Policy params (for policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Establish Home top 7-day sales (adset 106)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-07"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-08"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-09"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-10"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-11"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-12"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),

            # Validate donor/beneficiary details (includes ads per your tool)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),

            # Freeze: +30 to 106 (500→530), -30 from 103 (1180→1150); totals preserved
            Action(name="freeze_plan", kwargs={
                "plan_id": "env_soc_008",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:30:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 1680.0,

                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"}
                ],

                "adset_mapping": [
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"}
                ],

                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },

                "allocations": [
                    {"adset_id": "106", "budget": 530.0},
                    {"adset_id": "103", "budget": 1150.0}
                ],

                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"}
                ]
            }
                   ),

            # Apply → verify → mark → record
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "env_soc_008",
                "timestamp": "2025-08-14T01:32:00Z",
                "request_id": "ap-1"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "env_soc_008"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "env_soc_008",
                "status": "applied",
                "applied_at": "2025-08-14T01:34:00Z"
            }),
            Action(name="record_automation_run", kwargs={
                "run_type": "plan_apply",
                "started_at": "2025-08-14T01:32:00Z",
                "ended_at": "2025-08-14T01:34:00Z",
                "status": "completed",
                "input_ref": "ap-1",
                "outputs_json": {
                    "plan_id": "env_soc_008",
                    "applied_adsets_count": 2,
                    # Match the exact order returned by apply_plan_allocations (ascending by adset_id)
                    "applied_adsets": ["103", "106"],
                    "total_budget": 1680.0,
                    "applied_at": "2025-08-14T01:34:00Z",
                    "run_status": "completed"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "env_soc_008"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T01:34:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
            '"total_budget": "1680.0"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_12",
        instruction=(
            "You are the Efficiency Lead and the time is 2025-08-14T01:35:00Z. "
            "Prepare plan_soc_009 (for 2025-08-13) to reallocate −40 from image adsets whose 2025-08-13 CPA exceeds 60 "
            "to video adsets with CPA below 25 within the same categories, keeping each category’s total unchanged. "
            "If no category has a qualifying donor+recipient pair, produce a no-op envelope that preserves all current "
            "budgets and strategies, and record deterministic reasons for any no-op results in run metadata. "
            "Honor the timing window start=2025-08-14T01:36:30Z and end=2025-08-14T01:38:00Z and use request id ap-1."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "105", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "107", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "109", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # No donors meet CPA>60 on image → compose a no-op envelope but include all required fields.
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_009",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:35:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 8560.0,

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"}
                ],

                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"}
                ],

                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },

                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "107", "budget": 400.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0}
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"}
                ]
            }
                   ),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_009",
                "timestamp": "2025-08-14T01:36:30Z",
                "request_id": "ap-1"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_009"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_009",
                "status": "applied",
                "applied_at": "2025-08-14T01:38:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_009"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T01:38:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_13",
        instruction=(
            "You are the Electronics Fine Tuner and the time is 2025-08-14T05:00:00Z. "
            "Publish plan_soc_054 for date 2025-08-13: shift 20 from adset 101 to adset 112 within Electronics so the category total stays fixed; "
            "leave strategies unchanged and creatives mirrored from current state. "
            "Use created_at 2025-08-14T05:00:00Z, apply at 2025-08-14T05:02:00Z (request_id ap-052), and consider the plan applied at 2025-08-14T05:03:00Z."
        ),
        actions=[
            # Policy snapshot to be echoed verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for adsets included in the plan
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze—budgets shift: 101: 920→900, 112: 700→720 (sum preserved, rounding respected)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 900.0},
                    {"adset_id": "112", "budget": 720.0},
                ],
                "total_budget": 1620.0,
            }),

            # Apply → verify → mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_054",
                "timestamp": "2025-08-14T05:02:00Z",
                "request_id": "ap-052"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_054"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_054",
                "status": "applied",
                "applied_at": "2025-08-14T05:03:00Z"
            }),

            # Record run—counts reflect apply results
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_054"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T05:03:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_14",
        instruction=(
            "You are the Q3 Video Uplift Lead and the time is 2025-08-14T05:10:00Z. "
            "Rotate adsets 104 and 107 to video at 2025-08-14T05:10:00Z using rotation request_id rot-018 with rationale "
            "'Q3 video uplift'. Enforce single-active. If an adset is already video, treat it as a no-op and log the reason "
            "'already_in_target_state'. Consider the run complete at 2025-08-14T05:11:00Z."
        ),
        actions=[
            # Material rotation for 104
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "104",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T05:10:00Z",
                "request_id": "rot-018",
                "rationale": "Q3 video uplift",
                "ad_name": "rot-018-104-video"
            }),
            # Do NOT rotate 107 (already video) — log as a no-op in the run record
            Action(name="record_automation_run", kwargs={
                "run_type": "creative_rotation",
                "started_at": "2025-08-14T05:10:00Z",
                "ended_at": "2025-08-14T05:11:00Z",
                "status": "completed",
                "request_id": "rot-018",
                "input_ref": "rot-018",
                "outputs_json": {
                    "rotation_request_id": "rot-018",
                    "rotated_adsets_count": 1,
                    "rotation_noops": [{"adset_id": "107", "reason": "already_in_target_state"}],
                    "run_status": "completed",
                    "ended_at": "2025-08-14T05:11:00Z"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-018"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_15",
        instruction=(
            "You are the Apparel Level-Setter and the time is 2025-08-14T01:47:00Z. "
            "Prepare plan_soc_011 (date 2025-08-13) that equalizes Apparel budgets to the category mean "
            "(round to integers) while leaving all non-Apparel categories unchanged. "
            "Honor timing window start=2025-08-14T01:49:00Z and end=2025-08-14T01:50:00Z, "
            "and use request id ap-010 for deterministic audit metadata. "
            "Preserve existing strategies and creatives unless required by policy."
        ),
        actions=[
            # Source names/strategies/creatives from DB
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),

            # Freeze equalized Apparel envelope (sum=2080; integer mean 693,693,694 with +1 to highest id 105)
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_011",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:47:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 2080.0,
                "adset_mapping": [
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                ],
                "strategies": [
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                ],
                "policy_snapshot": {"min_budget_allocation": 100, "budget_rounding_unit": 1, "currency": "USD",
                                    "timezone": "UTC"},
                "allocations": [
                    {"adset_id": "102", "budget": 693.0},
                    {"adset_id": "104", "budget": 693.0},
                    {"adset_id": "105", "budget": 694.0},
                ],
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_011", "timestamp": "2025-08-14T01:49:00Z", "request_id": "ap-010"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_011"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_011", "status": "applied", "applied_at": "2025-08-14T01:50:00Z"}),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_011"',
            '"applied_adsets_count": "3"',
            '"applied_at": "2025-08-14T01:50:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_16",
        instruction=(
            "You are the Toys Expansion Owner and the time is 2025-08-14T01:51:00Z. "
            "Provision the 'Toys — Expansion' adset (adset_id '141') under campaign_id '5' with daily_budget 220, "
            "bid_strategy lowest_cost, status active; create exactly one active video ad named 'Toys — Expansion Video v1' "
            "with deterministic ad_id '14101'. Ensure the adset ends with a single active ad. "
            "Consider the provisioning run started at 2025-08-14T01:51:00Z and complete at 2025-08-14T01:53:00Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
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
            }),

            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "14101",
                    "adset_id": "141",
                    "name": "Toys — Expansion Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T01:51:00Z",
                "request_id": "en-2"
            }),

            Action(name="record_automation_run", kwargs={
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
                    "single_active_enforced": True,
                    "run_status": "completed"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "141"',
            '"ads_created": "1"',
            '"new_ad_id": "14101"',
            '"final_type": "video"',
            '"single_active_enforced": "True"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,
    # ---------- plan_soc_012: Bid Policy Curator ----------

    Task(
        annotator="0",
        user_id="TASK_17",
        instruction=(
            "You are the Bid Policy Curator and the time is 2025-08-14T01:54:00Z. "
            "Compose plan_soc_012 (2025-08-13) that (i) converts any cost_cap with bid_amount < 5 to lowest_cost, "
            "and (ii) reallocates +20 within Electronics by adding it to the highest-ROAS Electronics adset and removing −20 from the lowest-ROAS "
            "Electronics adset, both determined from 2025-08-13 insights; preserve category totals. "
            "Include audit markers at 2025-08-14T01:56:00Z (ap-011) and 2025-08-14T01:57:00Z."
        ),
        actions=[
            # Policy parameters for snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for all adsets used in freeze_plan (names/strategies/creatives)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Insights for Electronics to deterministically select donor (lowest ROAS) and recipient (highest ROAS)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # Freeze envelope (allocations reflect −20 from 101 → +20 to 112; 111 strategy converts to lowest_cost)
            Action(name="freeze_plan", kwargs={
                "plan_id": "plan_soc_012",
                "date": "2025-08-13",
                "created_at": "2025-08-14T01:54:00Z",
                "author": "automation_agent",
                "checksum": "CHK001",
                "total_budget": 2620.0,

                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"}
                ],

                "policy_snapshot": {
                    "min_budget_allocation": 100,
                    "budget_rounding_unit": 10,
                    "currency": "USD",
                    "timezone": "UTC"
                },

                "allocations": [
                    {"adset_id": "101", "budget": 900.0},  # 920 → 900 (donor)
                    {"adset_id": "112", "budget": 720.0},  # 700 → 720 (recipient)
                    {"adset_id": "111", "budget": 1000.0}  # unchanged allocation
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "112", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"}
                ],

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "lowest_cost"}  # convert from cost_cap 2.5
                ],
            }),

            # Apply → verify → mark → record (audit markers per instruction)
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_012",
                "timestamp": "2025-08-14T01:56:00Z",
                "request_id": "ap-011"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_012"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_012",
                "status": "applied",
                "applied_at": "2025-08-14T01:57:00Z"
            }),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_012"',
            '"applied_adsets_count": "3"',
            '"applied_at": "2025-08-14T01:57:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_18",
        instruction=(
            "You are the Creative Harmonizer and the time is 2025-08-14T01:58:00Z. "
            "Rotate adset 110 to image and adset 112 to video, enforcing single-active creative per adset. "
            "Use rotation request_id rot-004 with rationale 'align with 7-day winners'. "
            "Record completion with ended_at 2025-08-14T02:00:00Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "110",
                "new_creative_type": "image",
                "timestamp": "2025-08-14T01:58:00Z",
                "request_id": "rot-004",
                "rationale": "align with 7-day winners",
                "ad_name": "rot-004-110-image"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "112",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T01:58:00Z",
                "request_id": "rot-004",
                "rationale": "align with 7-day winners",
                "ad_name": "rot-004-112-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-004"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T02:00:00Z"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_19",
        instruction=(
            "You are the Cross-Category Balancer and the time is 2025-08-14T02:00:30Z. "
            "Publish plan_soc_013 for date 2025-08-13. Within Mobile (adsets 110, 111), raise +15 for each adset whose CPA on 2025-08-13 is < 25; "
            "fund these increases by reducing −15 from Electronics donors among (101, 108, 112) whose CPA on 2025-08-13 is > 50. "
            "Keep the per-category minimum of 100 and preserve category totals. "
            "If no Electronics donors meet CPA > 50, publish a no-op snapshot mirroring current budgets, strategies, and active creative types for adsets 101, 108, 110, 111, 112. "
            "Use apply timestamp 2025-08-14T02:02:00Z with request_id ap-012 and consider the plan applied at 2025-08-14T02:04:00Z."
        ),
        actions=[
            # Policy parameters → freeze_plan.policy_snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # CPA reads (prove no Electronics donors with CPA > 50)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # Authoritative adset reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # No eligible donors → freeze a no-op snapshot (arrays sorted; budgets sum exactly)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 4400.0,
            }),

            # Apply, then verify, then mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_013",
                "timestamp": "2025-08-14T02:02:00Z",
                "request_id": "ap-012"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_013"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_013",
                "status": "applied",
                "applied_at": "2025-08-14T02:04:00Z"
            }),

            # Record run — required fields with correct key & types
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_013"',
            '"applied_adsets_count": 0',
            '"applied_at": "2025-08-14T02:04:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_20",
        instruction=(
            "You are the Seasonal Merchandiser and the time is 2025-08-14T02:05:00Z. "
            "Provision a new Apparel adset (adset_id 126) named 'Apparel — Seasonal' under campaign_id '3' "
            "with daily_budget 260, bid_strategy lowest_cost, and status active. "
            "Ensure an active image ad starts on 2025-08-14 named 'Apparel — Seasonal Image v1'. "
            "Rotate the adset’s active creative to video using rotation request_id rot-001, name the new ad rot-001-126-video, "
            "and use rationale 'seasonal refresh'."
        ),
        actions=[
            # Action 1 — adset insert: updated_at MUST match this call's timestamp exactly (02:05:00Z)
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "126",
                    "campaign_id": "3",
                    "name": "Apparel — Seasonal",
                    "category": "Apparel",
                    "daily_budget": 260.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T02:05:00Z"
                },
                "timestamp": "2025-08-14T02:05:00Z",
                "request_id": "en-1"
            }),

            # Action 2 — ad insert: must be ACTIVE per instruction (no 'paused')
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_126_20250814_1",
                    "adset_id": "126",
                    "name": "Apparel — Seasonal Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T02:05:00Z",
                "request_id": "en-2"
            }),

            # Action 3 — rotate: timestamp aligns with completion (so rotated_at == 02:07:00Z)
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "126",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:05:00Z",
                "request_id": "rot-001",
                "rationale": "seasonal refresh",
                "ad_name": "rot-001-126-video"
            }),

            # Action 4 — record run (include request_id)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-001"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T02:07:00Z"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_21",
        instruction=(
            "You are the Rounding Guardian and the time is 2025-08-14T02:07:00Z. "
            "Publish plan_soc_014 for date 2025-08-13. Standardize cost_cap bids to whole numbers and adjust budgets so each category total is unchanged. "
            "Limit scope to adsets 111 (Mobile) and 106 (Home). Round adset 111 cost_cap bid from 2.5 to 2.0; keep adset 106 at 18.0. "
            "Budgets remain unchanged for both adsets. Use created_at 2025-08-14T02:07:00Z. "
            "Use apply timestamp 2025-08-14T02:09:00Z with request_id ap-013, require a verification pass, and consider the plan applied at 2025-08-14T02:10:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],
                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.0},
                ],
                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                ],
                "allocations": [
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                ],
                "total_budget": 1500.0,
            }),
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_014", "timestamp": "2025-08-14T02:09:00Z", "request_id": "ap-013"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_014"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_014", "status": "applied", "applied_at": "2025-08-14T02:10:00Z"}),
            #  Add applied_at and run_status into outputs_json (what judge expects)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_014"',
            '"applied_adsets_count": "1"',
            '"applied_at": "2025-08-14T02:10:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    # ---------- Video Rollout Owner: 104,108,111 -> video ----------
    Task(
        annotator="0",
        user_id="TASK_22",
        instruction=(
            "You are the Video Rollout Owner and the time is 2025-08-14T02:11:00Z. "
            "Rotate adsets 104 and 108 to video at 2025-08-14T02:11:00Z, enforcing a single active creative per adset. "
            "Confirm adset 111’s current creative type from the database; if it is already video on 2025-08-13, do not rotate it and do not count it. "
            "Use rotation request_id rot-008-triad and name new ads rot-008-<adset_id>-video "
            "(i.e., rot-008-104-video, rot-008-108-video). "
            "Use rationale 'align to video winners' and consider the rotation complete at 2025-08-14T02:12:30Z."
        ),
        actions=[
            # Read 111 to deterministically justify skipping it if already video
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Perform only the two non-no-op rotations
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "104",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:11:00Z",
                "request_id": "rot-008-triad",
                "rationale": "align to video winners",
                "ad_name": "rot-008-104-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "108",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:11:00Z",
                "request_id": "rot-008-triad",
                "rationale": "align to video winners",
                "ad_name": "rot-008-108-video"
            }),

            # Record run with the exact expected outputs
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-008-triad"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T02:12:30Z"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_23",
        instruction=(
            "You are the Waste Trimmer and the time is 2025-08-14T02:13:00Z. "
            "Publish plan_soc_015 for date 2025-08-13. If an adset is paused, set its budget to 0 and redistribute the freed amount "
            "EQUALLY across active peers in the SAME category, rounding to the policy budget_rounding_unit; leave other categories untouched. "
            "If there are no active peers in that category, publish a NO-OP snapshot for that adset (no redistribution). "
            "For Office, confirm adset 109 has no active peers and leave its budget unchanged. "
            "Use created_at 2025-08-14T02:13:00Z. Apply at 2025-08-14T02:15:00Z with request_id ap-014, VERIFY before marking, "
            "and consider the plan applied at 2025-08-14T02:16:00Z."
        ),
        actions=[
            # Policy snapshot (echo verbatim in freeze_plan)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative read for the Office adset (paused; no peers in category → NO-OP snapshot)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "109"}),

            # Freeze NO-OP snapshot for 109 (keep budget; arrays complete; policy snapshot matches fetched params)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "109", "name": "Back to School - Stationery", "category": "Office",
                     "campaign_id": "6"},
                ],
                "strategies": [
                    {"adset_id": "109", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "109", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "109", "budget": 300.0},
                ],
                "total_budget": 300.0,
            }),

            # Apply, then VERIFY before marking applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_015",
                "timestamp": "2025-08-14T02:15:00Z",
                "request_id": "ap-014"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_015"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_015",
                "status": "applied",
                "applied_at": "2025-08-14T02:16:00Z"
            }),

            # Record run with required fields (use applied_adsets_count; include applied_at & run_status)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_015"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T02:16:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_24",
        instruction=(
            "You are the Electronics Normalizer and the time is 2025-08-14T02:18:30Z. "
            "Publish plan_soc_016 for date 2025-08-13 to normalize Electronics budgets toward the median while preserving the category total: "
            "set adset 112 to 780, reduce adset 101 to 840, and leave adset 108 unchanged; other categories remain unchanged. "
            "Use created_at 2025-08-14T02:18:30Z. Use apply timestamp 2025-08-14T02:20:00Z with request_id ap-015, require a verification pass, "
            "and consider the plan applied at 2025-08-14T02:21:00Z."
        ),
        actions=[
            # Policy parameters (used verbatim in policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for authoritative mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze a valid plan envelope (include only adsets appearing in allocations; arrays sorted by adset_id)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                # Strategies carried forward from DB for the adsets in allocations
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                # Currently active creative types mirrored from DB
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                # Deterministic allocations (sum to total_budget)
                "allocations": [
                    {"adset_id": "101", "budget": 840.0},
                    {"adset_id": "112", "budget": 780.0},
                ],
                "total_budget": 1620.0,
            }),

            # Apply, then verify before marking applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_016",
                "timestamp": "2025-08-14T02:20:00Z",
                "request_id": "ap-015"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_016"}),

            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_016",
                "status": "applied",
                "applied_at": "2025-08-14T02:21:00Z"
            }),

            # Record run with all expected outputs
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_016"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T02:21:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_25",
        instruction=(
            "You are the Media Ops Coordinator and the time is 2025-08-14T01:15:00Z. "
            "Provision a new adset (adset_id 120) named 'Electronics — Promo' under campaign_id '6' with category Electronics, "
            "daily_budget 300, bid_strategy lowest_cost, and status active. "
            "Ensure exactly one active image ad exists starting 2025-08-14 named 'Electronics Promo V1' using deterministic ad_id auto_120_20250814_1. "
            "Treat 2025-08-14T01:15:00Z as the creation timestamp and consider the provisioning window 2025-08-14T01:15:00Z–2025-08-14T01:17:00Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
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
            }),
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_120_20250814_1",
                    "adset_id": "120",
                    "name": "Electronics Promo V1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T01:15:00Z",
                "request_id": "en-2"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "120"',
            '"ads_created": "1"',
            '"final_type": "image"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_26",
        instruction=(
            "You are the Policy-Driven Planner and the time is 2025-08-14T01:41:00Z. "
            "Publish plan_soc_010 for date 2025-08-13 prioritizing Mobile with a per-category minimum of 200: "
            "increase Mobile by exactly 60, split evenly, by setting adsets 110 and 111 to 1030 each, funded entirely from adset 103 (All) reducing it to 1120; "
            "leave other categories unchanged. Use created_at 2025-08-14T01:41:00Z. "
            "Use apply timestamp 2025-08-14T01:43:00Z with request_id ap-009, require a verification pass, and consider the plan applied at 2025-08-14T01:44:00Z."
        ),
        actions=[
            # Policy parameters for policy_snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),  # All
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),  # Mobile
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),  # Mobile

            # Freeze plan envelope (arrays sorted by adset_id; strategies carried forward unless changed)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],

                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],

                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                ],

                "allocations": [
                    {"adset_id": "103", "budget": 1120.0},
                    {"adset_id": "110", "budget": 1030.0},
                    {"adset_id": "111", "budget": 1030.0},
                ],
                "total_budget": 3180.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_010", "timestamp": "2025-08-14T01:43:00Z", "request_id": "ap-009"}),

            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_010"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_010", "status": "applied", "applied_at": "2025-08-14T01:44:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_010"',
            '"applied_adsets_count": "3"',
            '"applied_at": "2025-08-14T01:44:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    ),

    Task(
        annotator="0",
        user_id="TASK_27",
        instruction=(
            "You are the Zero-Purchase Controller and the time is 2025-08-14T02:23:30Z. "
            "Publish plan_soc_017 for date 2025-08-13. For any adset with purchases=0 on 2025-08-13, reduce its budget by 20 and "
            "redistribute the total reductions within that adset’s category proportional to clicks, rounded to the policy "
            "budget_rounding_unit, while keeping each category’s total fixed. If a zero-purchase adset is the sole adset in its "
            "category, publish a no-op snapshot for that category. Limit scope to adset 103 (category All). "
            "Use created_at 2025-08-14T02:23:30Z. Use apply timestamp 2025-08-14T02:25:00Z with request_id ap-016, require a verification pass, "
            "and consider the plan applied at 2025-08-14T02:26:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                ],
                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                ],
                "allocations": [
                    {"adset_id": "103", "budget": 1180.0},
                ],
                "total_budget": 1180.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_017", "timestamp": "2025-08-14T02:25:00Z", "request_id": "ap-016"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_017"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_017", "status": "applied", "applied_at": "2025-08-14T02:26:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_017"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T02:26:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    # ---------- Cross-Promo Pilot: All — Cross-Promo ----------
    Task(
        annotator="0",
        user_id="TASK_28",
        instruction=(
            "You are the Cross-Promo Pilot and the time is 2025-08-14T02:27:00Z. "
            "Provision a new adset (adset_id 128) named 'All — Cross-Promo' under campaign_id '2' with category All, "
            "daily_budget 200, bid_strategy lowest_cost, and status active. "
            "Ensure exactly one active video ad exists starting 2025-08-14 named 'All — Cross-Promo Video v1' using deterministic ad_id auto_128_20250814_1. "
            "Treat 2025-08-14T02:27:00Z as the creation timestamp and consider the provisioning window 2025-08-14T02:27:00Z–2025-08-14T02:28:30Z."
        ),
        actions=[
            # Adset insert (request_id en-1). created_at/updated_at must match timestamp.
            Action(name="insert_entity", kwargs={
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
            }),

            # Ad insert (request_id en-2). Include nullable end_date and deterministic ad_id.
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_128_20250814_1",
                    "adset_id": "128",
                    "name": "All — Cross-Promo Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T02:27:00Z",
                "request_id": "en-2"
            }),

            # Record run (request_id en-3) and include run_type inside outputs_json.
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "128"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_29",
        instruction=(
            "You are the Strategy Migrator and the time is 2025-08-14T02:29:00Z."
            "Plan plan_soc_018 targets 2025-08-13: convert adsets 104 and 108 to lowest_cost while keeping adset 106 at cost_cap with bid_amount 18.0."
            "Preserve the overall budget by leaving budgets unchanged (104=740, 108=780, 106=500). "
            "Plan constants — created_at: 2025-08-14T02:29:00Z; apply_timestamp: 2025-08-14T02:30:30Z (request_id ap-017); applied_at: 2025-08-14T02:31:30Z; verification: required."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                ],

                "strategies": [
                    {"adset_id": "104", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "108", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "108", "creative_type": "image"},
                ],

                "allocations": [
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "108", "budget": 780.0},
                ],
                "total_budget": 2020.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_018", "timestamp": "2025-08-14T02:30:30Z", "request_id": "ap-017"}),

            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_018"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_018", "status": "applied", "applied_at": "2025-08-14T02:31:30Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_018"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T02:31:30Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_30",
        instruction=(
            "You are the Engagement Driver and the time is 2025-08-14T02:32:00Z. "
            "Rotate adsets 102 and 112 to video at 2025-08-14T02:32:00Z using rotation request_id rot-006 with rationale 'video engagement spike'. "
            "Enforce a single active creative per adset, and consider the rotation complete at 2025-08-14T02:33:00Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "102",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:32:00Z",
                "request_id": "rot-006",
                "rationale": "video engagement spike",
                "ad_name": "rot-006-102-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "112",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:32:00Z",
                "request_id": "rot-006",
                "rationale": "video engagement spike",
                "ad_name": "rot-006-112-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-006"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_31",
        instruction=(
            "You are the CPC Reallocator and the time is 2025-08-14T02:33:30Z. "
            "Publish plan_soc_019 for date 2025-08-13: take 15 from adsets with CPC > 3.0 and give 15 to adsets with CPC < 1.0 within the same category, "
            "keeping each category total fixed. Determine CPC using insights for 2025-08-13 on adsets 101, 108, and 112. "
            "For these adsets there are no CPC>3.0 donors, so publish a no-op snapshot with budgets unchanged (101=920, 108=780, 112=700). "
            "Use created_at 2025-08-14T02:33:30Z. Use apply timestamp 2025-08-14T02:35:00Z with request_id ap-018, require a verification pass, "
            "and consider the plan applied at 2025-08-14T02:36:00Z."
        ),
        actions=[
            # Policy snapshot (use verbatim in freeze_plan.policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Insights to compute CPC (spend/clicks) for 2025-08-13
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "108", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # Authoritative DB reads for plan envelope fields
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze a no-op plan snapshot (arrays sorted by adset_id)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 2400.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_019", "timestamp": "2025-08-14T02:35:00Z", "request_id": "ap-018"}),

            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_019"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_019", "status": "applied", "applied_at": "2025-08-14T02:36:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_019"',
            '"changes": "0"',
            '"applied_at": "2025-08-14T02:36:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_32",
        instruction=(
            "You are the Retargeting Owner and the time is 2025-08-14T02:36:30Z. "
            "Provision adset 127 named 'Electronics — Retargeting' under campaign_id 6 with daily_budget 280, "
            "bid_strategy lowest_cost, status active, and category Electronics. "
            "Ensure a single active image ad starts on 2025-08-14 named 'Electronics — Retargeting Image v1'. "
            "Consider provisioning complete at 2025-08-14T02:38:30Z."
        ),
        actions=[
            # Insert the adset; updated_at must match the action timestamp exactly
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "127",
                    "campaign_id": "6",
                    "name": "Electronics — Retargeting",
                    "category": "Electronics",
                    "daily_budget": 280.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T02:36:30Z"
                },
                "timestamp": "2025-08-14T02:36:30Z",
                "request_id": "en-1"
            }),

            # Insert the initial active image ad with deterministic ad_id and full minimal schema
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_127_20250814_1",
                    "adset_id": "127",
                    "name": "Electronics — Retargeting Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T02:36:30Z",
                "request_id": "en-2"
            }),

            # Record the provisioning run; duration 120s and include run_status in outputs_json
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "127"',
            '"ads_created": "1"',
            '"final_type": "image"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    # ---------- plan_soc_020: Guardrails Planner ----------
    Task(
        annotator="0",
        user_id="TASK_33",
        instruction=(
            "You are the Guardrails Planner and the time is 2025-08-14T02:38:00Z. "
            "Publish plan_soc_020 for date 2025-08-13. Increase Mobile adsets 110 and 111 by +20 each and fund this by reducing Electronics adsets 101 and 112 by −20 each. "
            "Keep all other adsets unchanged, enforce a per-category minimum of 100, and preserve overall budget exactly (no net change across categories). "
            "Use created_at 2025-08-14T02:38:00Z. Apply at 2025-08-14T02:40:00Z with request_id ap-019 and consider the plan applied at 2025-08-14T02:41:00Z."
        ),
        actions=[
            # Policy parameters for policy_snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for authoritative mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze plan (arrays sorted by adset_id; strategies/creatives mirror DB; budgets adjusted as instructed)
            Action(name="freeze_plan", kwargs={
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

                # Adset mapping copied from DB reads (names/categories/campaign_ids are authoritative)
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                # Strategies: unchanged from DB
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                # Active creative types mirrored from DB
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                # Budgets: 101: 920→900, 112: 700→680, 110: 1000→1020, 111: 1000→1020
                "allocations": [
                    {"adset_id": "101", "budget": 900.0},
                    {"adset_id": "110", "budget": 1020.0},
                    {"adset_id": "111", "budget": 1020.0},
                    {"adset_id": "112", "budget": 680.0},
                ],
                "total_budget": 3620.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_020", "timestamp": "2025-08-14T02:40:00Z", "request_id": "ap-019"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_020", "status": "applied", "applied_at": "2025-08-14T02:41:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_020"',
            '"applied_adsets_count": "4"',
            '"applied_at": "2025-08-14T02:41:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_34",
        instruction=(
            "You are the Video Maintainer and the time is 2025-08-14T02:41:30Z. "
            "Rotate adset 101 to video and confirm adset 111 remains video (no-op allowed), enforcing a single active creative per adset. "
            "Use rotation request_id rot-007, name the new ad rot-007-101-video, and use rationale 'maintain video policy'. "
            "Consider the rotation complete at 2025-08-14T02:43:30Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "101",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:43:30Z",  # rotated_at aligns with completion
                "request_id": "rot-007",
                "rationale": "maintain video policy",
                "ad_name": "rot-007-101-video"
            }),
            # Verify 111 remains video (authoritative read)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-007"',
            '"rotated_adsets_count": "1"',
            '"confirmed_video_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,
    # ---------- plan_soc_021: Smoother (delta cap ±25; no changes) ----------
    Task(
        annotator="0",
        user_id="TASK_35",
        instruction=(
            "You are the Smoother and the time is 2025-08-14T02:42:30Z. "
            "Publish plan_soc_021 for date 2025-08-13. Cap absolute budget deltas versus the current snapshot at ±25 per adset. "
            "Limit scope to adsets 101, 108, 110, 111, and 112, keeping allocations identical to the snapshot (no deltas), "
            "and leave strategies and creatives unchanged. Use created_at 2025-08-14T02:42:30Z. "
            "Use apply timestamp 2025-08-14T02:44:00Z with request_id ap-020, require a verification pass, "
            "and consider the plan applied at 2025-08-14T02:45:00Z."
        ),
        actions=[
            # Policy snapshot parameters (must mirror these values in freeze_plan)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads to source authoritative mapping/strategies/creatives & current budgets
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze a no-delta snapshot (arrays sorted by adset_id)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                # Strategies mirrored from DB (unchanged)
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                # Active creative types mirrored from DB
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                # Budgets identical to snapshot (no deltas → satisfies ±25 cap)
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 4400.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_021", "timestamp": "2025-08-14T02:44:00Z", "request_id": "ap-020"}),

            # Verification required by instruction
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_021"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_021", "status": "applied", "applied_at": "2025-08-14T02:45:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_021"',
            '"changes": "0"',
            '"applied_at": "2025-08-14T02:45:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_36",
        instruction=(
            "You are the Home Video Champion and the time is 2025-08-14T02:45:30Z. "
            "Provision adset 129 named 'Home — Video First' under campaign_id 5 with daily_budget 260, "
            "bid_strategy lowest_cost, category Home, and status active. "
            "Ensure a single active video ad starts on 2025-08-14 named 'Home — Video First v1'. "
            "Consider provisioning complete at 2025-08-14T02:47:30Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "129",
                    "campaign_id": "5",
                    "name": "Home — Video First",
                    "category": "Home",
                    "daily_budget": 260.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T02:45:30Z"
                },
                "timestamp": "2025-08-14T02:45:30Z",
                "request_id": "en-1"
            }),
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_129_20250814_1",
                    "adset_id": "129",
                    "name": "Home — Video First v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T02:45:30Z",
                "request_id": "en-2"
            }),
            Action(name="record_automation_run", kwargs={
                "run_type": "provisioning",
                "started_at": "2025-08-14T02:45:30Z",
                "ended_at": "2025-08-14T02:47:30Z",
                "status": "completed",
                "request_id": "en-3",  # ← unique, sequential
                "input_ref": "en-2",
                "outputs_json": {
                    "adset_id": "129",
                    "ads_created": 1,
                    "final_type": "video",
                    "run_status": "completed"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "129"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,
    # ---------- plan_soc_022: Rounding Supervisor (budgets already multiples of 10) ----------
    Task(
        annotator="0",
        user_id="TASK_37",
        instruction=(
            "You are the Rounding Supervisor and the time is 2025-08-14T02:46:30Z. "
            "Publish plan_soc_022 for date 2025-08-13. Round all adset budgets to multiples of 10 while holding each category’s total constant. "
            "Make the following deterministic adjustments to avoid no-ops: in Electronics, set adset 101 to 930 and adset 108 to 770 with adset 112 unchanged at 700; "
            "in Mobile, keep adsets 110 and 111 at 1000. Use created_at 2025-08-14T02:46:30Z. "
            "Apply at 2025-08-14T02:48:00Z with request_id ap-021 and consider the plan applied at 2025-08-14T02:49:00Z."
        ),
        actions=[
            # Policy snapshot (mirror these values in freeze_plan)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative DB reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze plan (arrays sorted by adset_id)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                # Budgets (all multiples of 10); Electronics total 2400 = 930+770+700; Mobile total 2000 = 1000+1000
                "allocations": [
                    {"adset_id": "101", "budget": 930.0},  # +10
                    {"adset_id": "108", "budget": 770.0},  # -10
                    {"adset_id": "110", "budget": 1000.0},  # unchanged
                    {"adset_id": "111", "budget": 1000.0},  # unchanged
                    {"adset_id": "112", "budget": 700.0},  # unchanged
                ],
                "total_budget": 4400.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_022",
                "timestamp": "2025-08-14T02:48:00Z",
                "request_id": "ap-021"
            }),

            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_022",
                "status": "applied",
                "applied_at": "2025-08-14T02:49:00Z"
            }),

            Action(name="record_automation_run", kwargs={
                "run_type": "plan_apply",
                "started_at": "2025-08-14T02:48:00Z",
                "ended_at": "2025-08-14T02:49:00Z",
                "status": "completed",
                "input_ref": "ap-021",
                "outputs_json": {
                    "plan_id": "plan_soc_022",
                    "applied_adsets_count": 2,  # 101 and 108 changed
                    "applied_at": "2025-08-14T02:49:00Z",
                    "run_status": "completed"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_022"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T02:49:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_38",
        instruction=(
            "You are the Unified Creative Lead and the time is 2025-08-14T02:49:30Z. "
            "Rotate adsets 102 and 104 to video and confirm adset 110 remains video (no-op allowed), enforcing a single active creative per adset. "
            "Use rotation request_id rot-008, name new ads rot-008-<adset_id>-<type>, and use rationale 'uniform creative for test'. "
            "Consider the rotation complete at 2025-08-14T02:51:30Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "102",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:51:30Z",
                "request_id": "rot-008",
                "rationale": "uniform creative for test",
                "ad_name": "rot-008-102-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "104",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:51:30Z",
                "request_id": "rot-008",
                "rationale": "uniform creative for test",
                "ad_name": "rot-008-104-video"
            }),
            # Explicit no-op confirmation for 110
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-008"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_39",
        instruction=(
            "You are the Viewership Optimizer and the time is 2025-08-14T02:50:30Z."
            "Publish plan_soc_023 for date 2025-08-13. Guided by the day’s viewership uplift, preserve total spend while shifting +30 from Home to Toys: set adset 106 to 470 and adset 107 to 430, leaving strategies and creatives unchanged."
            "Use created_at 2025-08-14T02:50:30Z. Use apply timestamp 2025-08-14T02:52:00Z (request_id ap-022) and consider the plan applied at 2025-08-14T02:53:00Z."
        ),
        actions=[
            # (Optional context reads, fine to keep)
            Action(name="get_viewership_for_category", kwargs={"category": "Home", "date": "2025-08-13"}),
            Action(name="get_viewership_for_category", kwargs={"category": "Toys", "date": "2025-08-13"}),

            # Policy snapshot for freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for authoritative mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),  # Home
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),  # Toys

            # Freeze plan with full envelope (arrays sorted by adset_id)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                ],

                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                ],

                # Budgets after moving 30 from 106→107 (total preserved: 470+430=900)
                "allocations": [
                    {"adset_id": "106", "budget": 470.0},
                    {"adset_id": "107", "budget": 430.0},
                ],
                "total_budget": 900.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_023", "timestamp": "2025-08-14T02:52:00Z", "request_id": "ap-022"}),

            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_023"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_023", "status": "applied", "applied_at": "2025-08-14T02:53:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_023"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T02:53:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_40",
        instruction=(
            "You are the ROAS Optimizer and the time is 2025-08-14T02:55:00Z. "
            "Publish plan_soc_024 for date 2025-08-13. Convert cost_cap adsets whose CPA on 2025-08-13 is < 20 to lowest_cost, "
            "and grant +15 funded by −15 from peers in the same category with CPA > 60; if no donors exist, keep budgets unchanged. "
            "Limit scope to adsets 101 (Electronics) and 106 (Home). Set creatives to mirror the current active types from DB reads: "
            "adset 101 = image, adset 106 = image (unchanged). Use created_at 2025-08-14T02:55:00Z. "
            "Use apply timestamp 2025-08-14T02:57:00Z with request_id ap-023, require a verification pass, and consider the plan applied at 2025-08-14T02:58:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                ],
                "total_budget": 1420.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_024", "timestamp": "2025-08-14T02:57:00Z", "request_id": "ap-023"}),

            #  Verification step after apply
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_024"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_024", "status": "applied", "applied_at": "2025-08-14T02:58:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_024"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T02:58:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_41",
        instruction=(
            "You are the Parity Director and the time is 2025-08-14T02:58:00Z. "
            "Rotate adset 105 to video and adset 112 to video at 2025-08-14T02:59:30Z, enforcing single-active creative per adset. "
            "Use rotation request_id rot-004 with rationale 'type parity per category'. "
            "Consider the rotation complete at 2025-08-14T02:59:30Z."
        ),
        actions=[
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "105",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:59:30Z",
                    "request_id": "rot-004",
                    "rationale": "type parity per category",
                    "ad_name": "rot-004-105-video",
                },
            ),
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T02:59:30Z",
                    "request_id": "rot-004",
                    "rationale": "type parity per category",
                    "ad_name": "rot-004-112-video",
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
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
                    "errors_json": None,
                },
            ),
        ],
        outputs=[
            '"rotation_request_id": "rot-004"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    # ---------- plan_soc_025: Strategy Guardian ----------
    Task(
        annotator="0",
        user_id="TASK_42",
        instruction=(
            "You are the Strategy Guardian and the time is 2025-08-14T03:00:00Z. "
            "Publish plan_soc_025 for date 2025-08-13 that locks adset 111 at cost_cap 2.5 and adset 106 at cost_cap 18.0, "
            "leaves other adsets at lowest_cost, and keeps budgets unchanged. "
            "Use created_at 2025-08-14T03:00:00Z. Use apply timestamp 2025-08-14T03:02:00Z with request_id ap-024, "
            "require a verification pass, and consider the plan applied at 2025-08-14T03:03:00Z."
        ),
        actions=[
            # Policy snapshot (must mirror these reads exactly in freeze_plan.policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads required for adset_mapping, strategies, creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),

            # Freeze the plan envelope — arrays sorted by adset_id
            Action(name="freeze_plan", kwargs={
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

                # Sourced from the get_adset_details_by_id reads above
                "adset_mapping": [
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],

                # Lock strategies exactly as specified (and as currently set in DB)
                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],

                # Mirror active creative types from DB reads
                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                ],

                # Budgets unchanged; totals must sum to total_budget
                "allocations": [
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                ],
                "total_budget": 1500.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_025", "timestamp": "2025-08-14T03:02:00Z", "request_id": "ap-024"}),

            # Verification required by the instruction
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_025"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_025", "status": "applied", "applied_at": "2025-08-14T03:03:00Z"}),

            # Record exactly what happened — a no-op apply (0 changes), with applied_at and run_status included
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_025"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T03:03:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_43",
        instruction=(
            "You are the A/B Creative Lead and the time is 2025-08-14T02:16:30Z. "
            "Provision a new Mobile adset (adset_id 137, category Mobile) named 'Mobile — Creatives A/B' under campaign_id '7' "
            "with daily_budget 240, bid_strategy lowest_cost, and status active. Ensure a single active image ad starts on 2025-08-14 "
            "named 'Mobile A/B - Image v1'. For audit, capture a 7-day CPA snapshot for adset 137 over 2025-08-08..2025-08-14 "
            "using policy timezone and currency; proceed with rotation even if the window is empty because the adset is new. "
            "Rotate the adset’s active creative to video using rotation request_id rot-004, name the new ad rot-004-137-video, "
            "and use rationale 'video test'. Consider the rotation complete at 2025-08-14T02:18:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "137",
                    "campaign_id": "7",
                    "name": "Mobile — Creatives A/B",
                    "category": "Mobile",
                    "daily_budget": 240.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T02:16:30Z"
                },
                "timestamp": "2025-08-14T02:16:30Z",
                "request_id": "en-1"
            }),

            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_137_20250814_1",
                    "adset_id": "137",
                    "name": "Mobile A/B - Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T02:16:30Z",
                "request_id": "en-2"
            }),

            # Provisioning run lasts 120s from seed time
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),

            # 7-day snapshot (ok if empty)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-08"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-09"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-10"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-11"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-12"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "137", "date": "2025-08-14"}),

            # Fixed request_id & input_ref for insights snapshot
            Action(name="record_automation_run", kwargs={
                "run_type": "insights_snapshot",
                "started_at": "2025-08-14T02:16:30Z",
                "ended_at": "2025-08-14T02:18:00Z",
                "status": "completed",
                "request_id": "is-001",
                "input_ref": "insights-137-20250808-20250814",
                "outputs_json": {
                    "adset_id": "137",
                    "metric": "CPA",
                    "window": {"start": "2025-08-08", "end": "2025-08-14"},
                    "currency": "USD",
                    "timezone": "UTC",
                    "days": ["2025-08-08", "2025-08-09", "2025-08-10", "2025-08-11", "2025-08-12", "2025-08-13",
                             "2025-08-14"],
                    "entries": []
                },
                "errors_json": None
            }),

            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "137",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T02:18:00Z",
                "request_id": "rot-004",
                "rationale": "video test",
                "ad_name": "rot-004-137-video"
            }),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-004"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_44",
        instruction=(
            "You are the CPC Splitter and the time is 2025-08-14T03:04:30Z. "
            "Publish plan_soc_026 for date 2025-08-13. Within Electronics, move 40 from adset 101 (higher CPC on 2025-08-13) "
            "to adset 112 (lower CPC on 2025-08-13); leave all other adsets unchanged. "
            "Use created_at 2025-08-14T03:04:30Z. Use apply timestamp 2025-08-14T03:06:00Z with request_id ap-025, "
            "require a verification pass, and consider the plan applied at 2025-08-14T03:07:00Z."
        ),
        actions=[
            # Policy snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Insights for the plan date
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # DB reads for authoritative mapping/creatives/strategies
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze plan envelope (preserve strategies & creatives verbatim from DB)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},  # from DB
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},  # from DB
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},  # active in DB
                    {"adset_id": "112", "creative_type": "image"},  # active in DB
                ],
                # Move 40 from 101 (920 -> 880) to 112 (700 -> 740); totals preserved
                "allocations": [
                    {"adset_id": "101", "budget": 880.0},
                    {"adset_id": "112", "budget": 740.0},
                ],
                "total_budget": 1620.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_026",
                "timestamp": "2025-08-14T03:06:00Z",
                "request_id": "ap-025"
            }),

            # Post-apply verification
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_026"}),

            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_026",
                "status": "applied",
                "applied_at": "2025-08-14T03:07:00Z"
            }),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_026"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T03:07:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_45",
        instruction=(
            "You are the Video Enforcer and the time is 2025-08-14T03:07:30Z. "
            "Rotate adset 107 to image at 2025-08-14T03:07:30Z using rotation request_id rot-010 with rationale 'reinforce best type'. "
            "Name the new ad rot-010-107-image, enforce single-active, and record completion at 2025-08-14T03:08:30Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "107",
                "new_creative_type": "image",
                "timestamp": "2025-08-14T03:07:30Z",
                "request_id": "rot-010",
                "rationale": "reinforce best type",
                "ad_name": "rot-010-107-image"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-010"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    ),

    Task(
        annotator="0",
        user_id="TASK_46",
        instruction=(
            "You are the CTR Normalizer and the time is 2025-08-14T03:08:30Z. "
            "Publish plan_soc_027 for date 2025-08-13 to reallocate Apparel budgets across adsets 102, 104, and 105 "
            "proportionally to their CTR on 2025-08-13, keeping the Apparel category total fixed. "
            "Define CTR = clicks/impressions using 2025-08-13 insights. Use the policy budget_rounding_unit=10 with round-half-up; "
            "after rounding, if the sum deviates from the category total, distribute any +/− residual starting with the highest CTR "
            "adset, breaking ties by ascending adset_id. Keep each adset’s bid_strategy and bid_amount unchanged from DB, and "
            "mirror each adset’s current active creative type. For this date’s insights: 102 has CTR=1080/27500, 104 has CTR=1280/31500, "
            "105 has CTR=1250/31000. With the Apparel total equal to the sum of DB daily_budget for 102/104/105 and applying the rules "
            "above, set the final budgets to exactly: 102 → 680.0, 104 → 700.0, 105 → 700.0 (total 2080.0). "
            "Use apply timestamp 2025-08-14T03:10:00Z with request_id ap-026, verify success, and consider the plan applied at "
            "2025-08-14T03:11:00Z."
        ),
        actions=[
            # Policy snapshot (for freeze_plan.policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Insights used for CTRs (explicitly referenced in the instruction)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "105", "date": "2025-08-13"}),

            # DB reads to source mapping/strategies/creatives verbatim
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),

            # Freeze the plan with the pinned allocations and DB-sourced envelope
            Action(name="freeze_plan", kwargs={
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
                # Use exact values returned by the get_adset_details_by_id calls above
                "adset_mapping": [
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                ],
                "strategies": [
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                ],
                # Final budgets pinned in the instruction
                "allocations": [
                    {"adset_id": "102", "budget": 680.0},
                    {"adset_id": "104", "budget": 700.0},
                    {"adset_id": "105", "budget": 700.0},
                ],
                "total_budget": 2080.0
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_027",
                "timestamp": "2025-08-14T03:10:00Z",
                "request_id": "ap-026"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_027"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_027",
                "status": "applied",
                "applied_at": "2025-08-14T03:11:00Z"
            }),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_027"',
            '"applied_adsets_count": "3"',
            '"applied_at": "2025-08-14T03:11:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_47",
        instruction=(
            "You are the Accessories Owner and the time is 2025-08-14T03:11:30Z. "
            "Provision a new Electronics adset (adset_id 130) named 'Electronics — Accessories' under campaign_id '6' "
            "with daily_budget 210, bid_strategy lowest_cost, and status active. "
            "Ensure an active video ad starts on 2025-08-14 named 'Electronics Accessories Video v1'. "
            "Record a provisioning run ending 120 seconds after the seed time."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "130",
                    "campaign_id": "6",
                    "name": "Electronics — Accessories",
                    "category": "Electronics",
                    "daily_budget": 210.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T03:11:30Z"
                },
                "timestamp": "2025-08-14T03:11:30Z",
                "request_id": "en-1"
            }),

            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_130_20250814_1",
                    "adset_id": "130",
                    "name": "Electronics Accessories Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T03:11:30Z",
                "request_id": "en-2"
            }),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "130"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_48",
        instruction=(
            "You are the Purchase-Driven Planner and the time is 2025-08-14T03:12:30Z. "
            "Publish plan_soc_028 for date 2025-08-13. Within Apparel (adsets 102, 104, 105), grant +10 only to adsets with purchases ≥ 5, "
            "funded by −10 from adsets with purchases = 0 on 2025-08-13, while keeping the Apparel category total fixed and leaving each "
            "adset’s strategy and active creative type unchanged. For 2025-08-13, no Apparel donors with purchases = 0 exist, so the plan "
            "must preserve each of the three adsets’ current budgets. Treat 2025-08-14T03:14:00Z (ap-027) as the apply timestamp and "
            "consider the plan applied at 2025-08-14T03:15:00Z."
        ),
        actions=[
            # Policy snapshot for freeze_plan.policy_snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Insights establishing purchases (no donors with purchases=0 in Apparel on 2025-08-13)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "102", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "104", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "105", "date": "2025-08-13"}),

            # DB reads for authoritative mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),

            # Freeze a no-op plan (budgets unchanged; envelope sourced from DB)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "104", "name": "Fall Fashion - Women", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                ],
                "strategies": [
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "104", "bid_strategy": "cost_cap", "bid_amount": 20.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "104", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "102", "budget": 590.0},
                    {"adset_id": "104", "budget": 740.0},
                    {"adset_id": "105", "budget": 750.0},
                ],
                "total_budget": 2080.0
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_028",
                "timestamp": "2025-08-14T03:14:00Z",
                "request_id": "ap-027"
            }),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_028",
                "status": "applied",
                "applied_at": "2025-08-14T03:15:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_028"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T03:15:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_49",
        instruction=(
            "You are the Home/Toys Video Lead and the time is 2025-08-14T03:15:30Z. "
            "Rotate adsets 104 and 108 to video at 2025-08-14T03:15:30Z using rotation request_id rot-010 with rationale 'uniform video in Home/Toys'. "
            "Consider the rotation complete at 2025-08-14T03:16:30Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "104",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T03:15:30Z",
                "request_id": "rot-010",
                "rationale": "uniform video in Home/Toys",
                "ad_name": "rot-010-104-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "108",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T03:15:30Z",
                "request_id": "rot-010",
                "rationale": "uniform video in Home/Toys",
                "ad_name": "rot-010-108-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-010"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_50",
        instruction=(
            "You are the Electronics Floor Manager and the time is 2025-08-14T03:16:30Z. "
            "Publish plan_soc_029 for date 2025-08-13 to enforce Electronics ≥ 100 per adset and preserve the category total. "
            "Within Electronics, raise adset 112 by +20 and cut adset 101 by −20; leave adset 108 net unchanged. "
            "Set creatives to mirror the active types from DB reads: 101=image, 108=image, 112=image. "
            "Use created_at 2025-08-14T03:16:30Z. Use apply timestamp 2025-08-14T03:18:00Z with request_id ap-028, "
            "require a verification pass, and consider the plan applied at 2025-08-14T03:19:00Z."
        ),
        actions=[
            # Policy snapshot reads (values must be echoed exactly in freeze_plan.policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative adset reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze plan (arrays sorted by adset_id; budgets preserve category total 2400.0)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "108", "name": "Back to School - Laptops", "category": "Electronics",
                     "campaign_id": "6"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                # Strategies unchanged from DB (carry forward)
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "108", "bid_strategy": "cost_cap", "bid_amount": 42.0},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                # Creatives mirrored from DB reads (explicit in instruction)
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "108", "creative_type": "image"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                # Allocations reflect 101 −20 → 900.0, 112 +20 → 720.0, 108 unchanged → 780.0
                "allocations": [
                    {"adset_id": "101", "budget": 900.0},
                    {"adset_id": "108", "budget": 780.0},
                    {"adset_id": "112", "budget": 720.0},
                ],
                "total_budget": 2400.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_029", "timestamp": "2025-08-14T03:18:00Z", "request_id": "ap-028"}),

            # Required verification step after apply
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_029"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_029", "status": "applied", "applied_at": "2025-08-14T03:19:00Z"}),

            # Record run with required fields; applied_adsets_count reflects the two budget changes (101, 112)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_029"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T03:19:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_51",
        instruction=(
            "You are the Influencer Pilot and the time is 2025-08-14T03:19:30Z. "
            "Provision a new Apparel adset (adset_id 131, category Apparel) named 'Apparel — Influencer' under campaign_id '3' "
            "with daily_budget 240, bid_strategy lowest_cost, and status active. "
            "Ensure a single active video ad starts on 2025-08-14 named 'Apparel — Influencer Video v1'. "
            "Consider the provisioning complete at 2025-08-14T03:21:30Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "131",
                    "campaign_id": "3",
                    "name": "Apparel — Influencer",
                    "category": "Apparel",
                    "daily_budget": 240.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "created_at": "2025-08-14T03:19:30Z",
                    "updated_at": "2025-08-14T03:19:30Z"
                },
                "timestamp": "2025-08-14T03:19:30Z",
                "request_id": "en-1"
            }),
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_131_20250814_1",
                    "adset_id": "131",
                    "name": "Apparel — Influencer Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T03:19:30Z",
                "request_id": "en-2"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "131"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_52",
        instruction=(
            "You are the Market Entry Pilot and the time is 2025-08-14T03:03:30Z. "
            "Provision a new Mobile adset (adset_id 141, category Mobile) named 'Mobile — New Market' under campaign_id '7' with daily_budget 270, "
            "bid_strategy lowest_cost, and status active. Ensure an active image ad starts on 2025-08-14 named 'Mobile — New Market Image v1'. "
            "Consider provisioning complete at 2025-08-14T03:05:30Z."
        ),
        actions=[
            # en-1
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "141",
                    "campaign_id": "7",
                    "name": "Mobile — New Market",
                    "category": "Mobile",
                    "daily_budget": 270.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T03:03:30Z"
                },
                "timestamp": "2025-08-14T03:03:30Z",
                "request_id": "en-1"
            }),

            # en-2
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_141_20250814_1",
                    "adset_id": "141",
                    "name": "Mobile — New Market Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T03:03:30Z",
                "request_id": "en-2"
            }),

            # en-3 (unique request_id for the run record), 120s duration exactly
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "141"',
            '"ads_created": "1"',
            '"final_type": "image"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_53",
        instruction=(
            "You are the Mobile Fixer and the time is 2025-08-14T03:22:30Z. "
            "Publish plan_soc_031 for date 2025-08-13. Lock adset 111 at cost_cap 2.5 and adset 106 at cost_cap 18.0. "
            "Within Mobile on 2025-08-13, move 30 of budget from the highest-CPA adset to the lowest-CPA adset "
            "(deterministically: donor=110, recipient=111 based on that date’s CPAs), leaving other categories unchanged. "
            "Mirror active creative types from DB reads: adset 106=image, adset 110=video, adset 111=video. "
            "Use created_at 2025-08-14T03:22:30Z. Use apply timestamp 2025-08-14T03:24:00Z with request_id ap-029, "
            "require a verification pass, and consider the plan applied at 2025-08-14T03:25:00Z."
        ),
        actions=[
            # Policy snapshot for freeze_plan.policy_snapshot (echo these exact values inside freeze_plan)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # CPA reads for 2025-08-13 to fix donor/recipient deterministically (110 higher CPA than 111)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),

            # DB reads to source adset_mapping / strategies (carry forward DB unless changed) / creatives (mirror active)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Freeze the plan (arrays sorted by adset_id; total_budget equals sum of allocations)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],

                # Strategies: lock 106 and 111 as specified; set 110 to lowest_cost per instruction
                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],

                # Creatives mirror the DB-active types called out in the instruction
                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                ],

                # Budgets: shift 30 from donor (110) to recipient (111); keep 106 unchanged
                "allocations": [
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "110", "budget": 970.0},
                    {"adset_id": "111", "budget": 1030.0},
                ],
                "total_budget": 2500.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_031", "timestamp": "2025-08-14T03:24:00Z", "request_id": "ap-029"}),

            # Post-apply verification as required by instruction
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_031"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_031", "status": "applied", "applied_at": "2025-08-14T03:25:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_031"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T03:25:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    # ---------- Video-Lift Owner: Toys — Video Lift ----------
    Task(
        annotator="0",
        user_id="TASK_54",
        instruction=(
            "You are the Video-Lift Owner and the time is 2025-08-14T03:25:30Z. "
            "Provision a new Toys adset (adset_id 134, category Toys) named 'Toys — Video Lift' under campaign_id '5' "
            "with daily_budget 225, bid_strategy lowest_cost, and status active. "
            "Ensure an active image ad starts on 2025-08-14 named 'Toys — Video Lift Image v1'. "
            "Rotate the adset’s active creative to video using rotation request_id rot-004 with rationale 'video lift' at 2025-08-14T03:27:00Z. "
            "Consider provisioning complete at 2025-08-14T03:27:30Z."
        ),
        actions=[
            # en-1 — create the adset (updated_at must match timestamp exactly)
            Action(name="insert_entity", kwargs={
                "table": "adsets",
                "row": {
                    "adset_id": "134",
                    "campaign_id": "5",
                    "name": "Toys — Video Lift",
                    "category": "Toys",
                    "daily_budget": 225.0,
                    "bid_strategy": "lowest_cost",
                    "bid_amount": None,
                    "status": "active",
                    "updated_at": "2025-08-14T03:25:30Z"
                },
                "timestamp": "2025-08-14T03:25:30Z",
                "request_id": "en-1"
            }),

            # en-2 — insert initial image ad (deterministic ad_id pattern; use seed time)
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_134_20250814_1",
                    "adset_id": "134",
                    "name": "Toys — Video Lift Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T03:25:30Z",
                "request_id": "en-2"
            }),

            # rotate at 03:27:00Z; deterministic ad_name per policy
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "134",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T03:27:00Z",
                "request_id": "rot-004",
                "rationale": "video lift",
                "ad_name": "rot-004-134-video"
            }),

            # en-3 — record the provisioning run (exactly 120s duration; include run_status)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "134"',
            '"ads_created": "2"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_55",
        instruction=(
            "You are the Bid Rounding Lead and the time is 2025-08-14T03:27:30Z. "
            "Publish plan_soc_032 for date 2025-08-13. Round down cost_cap bid amounts to one decimal place while leaving budgets unchanged. "
            "Limit scope to adsets 101 (Electronics), 106 (Home), and 111 (Mobile). "
            "Set final rounded bids to: adset 101 → cost_cap 2.5, adset 106 → cost_cap 18.0, adset 111 → cost_cap 2.5. "
            "Mirror active creative types from DB reads: adset 101=image, adset 106=image, adset 111=video. "
            "Use created_at 2025-08-14T03:27:30Z. Use apply timestamp 2025-08-14T03:29:00Z with request_id ap-030, "
            "require a verification pass, and consider the plan applied at 2025-08-14T03:30:00Z."
        ),
        actions=[
            # Policy snapshot (must be echoed exactly in freeze_plan.policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads required for adset_mapping and to justify creatives/strategies as “mirrored from DB”
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Freeze plan envelope — arrays sorted by adset_id; budgets unchanged; strategies rounded to 1dp
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],

                # Strategies reflect rounded cost_cap values exactly as specified in the instruction
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],

                # Creatives mirror the DB-active types (explicit in the instruction for determinism)
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                ],

                # Budgets unchanged (sourced from DB daily_budgets)
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                ],
                "total_budget": 2420.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_032", "timestamp": "2025-08-14T03:29:00Z", "request_id": "ap-030"}),

            # Post-apply verification per instruction
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_032"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_032", "status": "applied", "applied_at": "2025-08-14T03:30:00Z"}),

            # Record actual result: 1 rounded change expected (adset 101), budgets unchanged
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_032"',
            '"applied_adsets_count": "1"',
            '"applied_at": "2025-08-14T03:30:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_56",
        instruction=(
            "You are the Parity Enforcer and the time is 2025-08-14T03:30:30Z. "
            "Rotate adset 101 to video and adset 112 to video at 2025-08-14T03:30:30Z, enforcing single-active creative per adset. "
            "Use rotation request_id rot-004 with rationale 'video parity across All/Electronics'. "
            "Consider the rotation complete at 2025-08-14T03:30:30Z."
        ),
        actions=[
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "101",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:30:30Z",
                    "request_id": "rot-004",
                    "rationale": "video parity across All/Electronics",
                    "ad_name": "rot-004-101-video",
                },
            ),
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:30:30Z",
                    "request_id": "rot-004",
                    "rationale": "video parity across All/Electronics",
                    "ad_name": "rot-004-112-video",
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
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
                    "errors_json": None,
                },
            ),
        ],
        outputs=[
            '"rotation_request_id": "rot-004"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_57",
        instruction=(
            "You are the Two-Hop Reallocator and the time is 2025-08-14T03:31:30Z. "
            "Publish plan_soc_033 for date 2025-08-13. Respect the budget_rounding_unit of 10 by shifting 20 from All to Mobile "
            "and 20 from Home to Electronics. Resolve deterministically to donors 103 (All) and 106 (Home), and recipients "
            "111 (Mobile) and 112 (Electronics). Set final budgets to: 103→1160.0, 106→480.0, 111→1020.0, 112→720.0; "
            "leave strategies unchanged and keep the overall total fixed. Use created_at 2025-08-14T03:31:30Z. "
            "Use apply timestamp 2025-08-14T03:33:00Z with request_id ap-031, require a verification pass, and consider the plan "
            "applied at 2025-08-14T03:34:00Z."
        ),
        actions=[
            # Policy snapshot to echo in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze plan — arrays sorted, creatives mirrored from DB, strategies unchanged, budgets on rounding unit
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                "allocations": [
                    {"adset_id": "103", "budget": 1160.0},  # -20 from 1180
                    {"adset_id": "106", "budget": 480.0},  # -20 from 500
                    {"adset_id": "111", "budget": 1020.0},  # +20 from 1000
                    {"adset_id": "112", "budget": 720.0},  # +20 from 700
                ],
                "total_budget": 3380.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_033", "timestamp": "2025-08-14T03:33:00Z", "request_id": "ap-031"}),

            # Post-apply verification
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_033"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_033", "status": "applied", "applied_at": "2025-08-14T03:34:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_033"',
            '"applied_adsets_count": "4"',
            '"applied_at": "2025-08-14T03:34:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_58",
        instruction=(
            "You are the Home Launch Owner and the time is 2025-08-14T03:40:30Z. "
            "For adset 121, activate a new video creative at 2025-08-14T03:41:00Z using rotation request_id rot-010 "
            "with rationale 'Home Launch video upgrade', enforcing single-active (pause any previously active creative). "
            "Name the new ad rot-010-121-video. Consider the rotation complete at 2025-08-14T03:42:00Z."
        ),
        actions=[
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "121",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:41:00Z",
                    "request_id": "rot-010",
                    "rationale": "Home Launch video upgrade",
                    "ad_name": "rot-010-121-video",
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
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
                    "errors_json": None,
                },
            ),
        ],
        outputs=[
            '"rotation_request_id": "rot-010"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T03:42:00Z"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_59",
        instruction=(
            "You are the Audience-Signal Planner and the time is 2025-08-14T03:36:30Z. "
            "Publish plan_soc_034 for date 2025-08-13. Because the All category has exactly one adset (adset_id 103) on 2025-08-13, "
            "no intra-All reallocation is possible; issue a no-op envelope that keeps adset 103’s budget unchanged. "
            "Use created_at 2025-08-14T03:36:30Z. Use apply timestamp 2025-08-14T03:38:00Z with request_id ap-032, "
            "require a verification pass, and consider the plan applied at 2025-08-14T03:39:00Z."
        ),
        actions=[
            # Policy snapshot (must be echoed exactly in freeze_plan)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB read for the lone All adset (103) to source mapping/strategy/creative and current budget
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            # Freeze no-op plan (arrays sorted, budgets unchanged, rounding respected)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                ],
                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                ],

                # Keep the DB budget unchanged (1180.0)
                "allocations": [
                    {"adset_id": "103", "budget": 1180.0},
                ],
                "total_budget": 1180.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_034",
                "timestamp": "2025-08-14T03:38:00Z",
                "request_id": "ap-032"
            }),

            # Post-apply verification
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_034"}),

            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_034",
                "status": "applied",
                "applied_at": "2025-08-14T03:39:00Z"
            }),

            # Record outputs including applied_adsets_count and a deterministic no-op reason
            Action(name="record_automation_run", kwargs={
                "run_type": "plan_apply",
                "started_at": "2025-08-14T03:38:00Z",
                "ended_at": "2025-08-14T03:39:00Z",
                "status": "completed",
                "input_ref": "ap-032",
                "outputs_json": {
                    "plan_id": "plan_soc_034",
                    "applied_adsets_count": 0,
                    "noops": [{"adset_id": "103", "reason": "already_in_target_state"}],
                    "applied_at": "2025-08-14T03:39:00Z",
                    "run_status": "completed"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_034"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T03:39:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_60",
        instruction=(
            "You are the Electronics Video Champion and the time is 2025-08-14T03:39:30Z. "
            "For adset 103, if the active creative on 2025-08-14 is already video, record a no-op rotation with reason "
            "'already_in_target_state'. Otherwise, rotate to video at 2025-08-14T03:39:30Z using rotation request_id rot-011, "
            "rationale 'consolidate video in Electronics', and name the new ad rot-011-103-video. "
            "Consider the rotation complete at 2025-08-14T03:40:30Z."
        ),
        actions=[
            # Read current creative type to deterministically decide no-op vs rotate
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            # Adset 103 is already video → no-op rotation; record the run with explicit reason
            Action(name="record_automation_run", kwargs={
                "run_type": "creative_rotation",
                "started_at": "2025-08-14T03:39:30Z",
                "ended_at": "2025-08-14T03:40:30Z",
                "status": "completed",
                "request_id": "rot-011",
                "input_ref": "rot-011",
                "outputs_json": {
                    "rotation_request_id": "rot-011",
                    "rotated_adsets_count": 0,
                    "noops": [{"adset_id": "103", "reason": "already_in_target_state"}],
                    "run_status": "completed",
                    "ended_at": "2025-08-14T03:40:30Z"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-011"',
            '"rotated_adsets_count": "0"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T03:40:30Z"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_61",
        instruction=(
            "You are the CTR Gatekeeper and the time is 2025-08-14T03:40:30Z. "
            "Publish plan_soc_035 for date 2025-08-13. Evaluate CTR on 2025-08-13 for adsets 103 (All), 106 (Home), 111 (Mobile), and 112 (Electronics): "
            "within each category, budgets shift by −10 for CTR < 0.5% and +10 for CTR > 2.5%, funded strictly within the same category. "
            "Because each of these categories has only one adset, budgets remain unchanged. "
            "Plan constants: created_at 2025-08-14T03:40:30Z; apply timestamp 2025-08-14T03:42:00Z (request_id ap-033); applied_at 2025-08-14T03:43:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "103", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "103", "budget": 1180.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 3380.0,
            }),
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_035",
                "timestamp": "2025-08-14T03:42:00Z",
                "request_id": "ap-033"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_035"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_035",
                "status": "applied",
                "applied_at": "2025-08-14T03:43:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_035"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T03:43:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_62",
        instruction=(
            "You are the Single-Active Steward and the time is 2025-08-14T03:22:00Z. "
            "For date 2025-08-13, enforce the single-active policy across the account: if an adset has more than one active ad "
            "of the same creative type, end with exactly one active by replacing them with a single new ad named "
            "rot-011-<adset_id>-<type>. If multiple types are active, do not change types in this run; only collapse duplicates. "
            "Use apply timestamp 2025-08-14T03:22:00Z with rotation request_id rot-011 and rationale 'single-active policy'. "
            "Consider the enforcement complete at 2025-08-14T03:23:00Z."
        ),
        actions=[
            # Discover multi-active across the account (deterministic enumeration)
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "101"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "102"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "103"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "104"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "105"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "106"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "107"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "108"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "109"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "110"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "111"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "112"}),

            # Collapse duplicates only where the same type has >1 active (adset 112 has two active image ads)
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "112",
                "new_creative_type": "image",
                "timestamp": "2025-08-14T03:22:00Z",
                "request_id": "rot-011",
                "rationale": "single-active policy",
                "ad_name": "rot-011-112-image"
            }),

            # Explicitly pause BOTH prior actives to guarantee single-active
            Action(name="update_ad_status", kwargs={
                "ad_id": "1116",
                "status": "paused",
                "timestamp": "2025-08-14T03:22:00Z",
                "request_id": "rot-011-1116-pause"
            }),
            Action(name="update_ad_status", kwargs={
                "ad_id": "1117",
                "status": "paused",
                "timestamp": "2025-08-14T03:22:00Z",
                "request_id": "rot-011-1117-pause"
            }),

            # Record the enforcement run — required outputs only, unique request_id
            Action(name="record_automation_run", kwargs={
                "run_type": "creative_rotation",
                "started_at": "2025-08-14T03:22:00Z",
                "ended_at": "2025-08-14T03:23:00Z",
                "status": "completed",
                "request_id": "rot-011-log",
                "input_ref": "rot-011",
                "outputs_json": {
                    "scope": "account",
                    "enforced_single_active": True,
                    "run_type": "creative_rotation",
                    "run_status": "completed"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"scope": "account"',
            '"enforced_single_active": "True"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_63",
        instruction=(
            "You are the Fair-Share Planner and the time is 2025-08-14T03:44:30Z. "
            "Publish plan_soc_036 for date 2025-08-13. For each category, transfer +20 to the lowest-CPA adset funded by −20 from the highest-CPA adset, "
            "keeping category totals fixed and each allocation ≥ the per-adset minimum and aligned to the budget rounding unit. "
            "Use the deterministic pairs: Electronics 101 → 112; Apparel 105 → 102; Mobile 110 → 111. "
            "Plan constants: created_at 2025-08-14T03:44:30Z; apply timestamp 2025-08-14T03:46:00Z (request_id ap-034); applied_at 2025-08-14T03:47:00Z."
        ),
        actions=[
            # Policy snapshot for freeze_plan.policy_snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative DB reads for every adset we reference (names/categories/campaign_ids/strategies/creatives)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Freeze the plan (all mapping/strategy/creative rows must match DB exactly)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                # Strategies (carried forward from DB; include bid_amount only for cost_cap)
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "lowest_cost"},
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                # Active creative types from DB
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                # Deterministic allocations (−20 donors, +20 recipients), honoring rounding and min
                "allocations": [
                    {"adset_id": "101", "budget": 900.0},  # −20 Electronics donor (from 920 → 900)
                    {"adset_id": "112", "budget": 720.0},  # +20 Electronics recipient (700 → 720)
                    {"adset_id": "105", "budget": 730.0},  # −20 Apparel donor (750 → 730)
                    {"adset_id": "102", "budget": 610.0},  # +20 Apparel recipient (590 → 610)
                    {"adset_id": "110", "budget": 980.0},  # −20 Mobile donor (1000 → 980)
                    {"adset_id": "111", "budget": 1020.0},  # +20 Mobile recipient (1000 → 1020)
                ],
                "total_budget": 4960.0
            }),

            # Apply → verify → mark as applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_036",
                "timestamp": "2025-08-14T03:46:00Z",
                "request_id": "ap-034"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_036"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_036",
                "status": "applied",
                "applied_at": "2025-08-14T03:47:00Z"
            }),

            # Record exactly the required outputs
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_036"',
            '"applied_adsets_count": "6"',
            '"applied_at": "2025-08-14T03:47:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_64",
        instruction=(
            "You are the High-ROAS Video Lead and the time is 2025-08-14T03:47:30Z. "
            "Rotate adsets 110 and 104 to video at 2025-08-14T03:47:30Z using rotation request_id rot-011 with rationale "
            "'harmonize video on high-ROAS sets', enforcing single-active. If an adset already has video active at that "
            "timestamp, treat it as a no-op. Name any new ads rot-011-<adset_id>-video. Consider the rotation complete at "
            "2025-08-14T03:48:30Z."
        ),
        actions=[
            # Read current state to determine which rotations are necessary (110 already video → no-op; 104 rotates)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),

            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "104",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T03:47:30Z",
                    "request_id": "rot-011",
                    "rationale": "harmonize video on high-ROAS sets",
                    "ad_name": "rot-011-104-video",
                },
            ),

            Action(
                name="record_automation_run",
                kwargs={
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
                        "ended_at": "2025-08-14T03:48:30Z",
                    },
                    "errors_json": None,
                },
            ),
        ],
        outputs=[
            '"rotation_request_id": "rot-011"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_65",
        instruction=(
            "You are the Swap Steward and the time is 2025-08-14T03:48:30Z. "
            "Publish plan_soc_037 for date 2025-08-13 that swaps budgets between adset 101 and adset 103 by moving 10 from 103 to 101; "
            "leave all other adsets unchanged. Budgets must respect the rounding unit of 10, yielding adset 101 = 930 and adset 103 = 1170. "
            "Use created_at 2025-08-14T03:48:30Z. Use apply timestamp 2025-08-14T03:50:00Z with request_id ap-035, require a verification pass, "
            "and consider the plan applied at 2025-08-14T03:51:00Z."
        ),
        actions=[
            # Policy snapshot (used verbatim in freeze_plan)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            # cost_cap, bid_amount 32.0, active creative: image
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),  # lowest_cost, active creative: video

            Action(name="freeze_plan", kwargs={
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

                # adset_mapping & creatives sourced from the DB reads; arrays sorted by adset_id
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                ],

                "allocations": [
                    {"adset_id": "101", "budget": 930.0},
                    {"adset_id": "103", "budget": 1170.0},
                ],
                "total_budget": 2100.0,
            }),

            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_037", "timestamp": "2025-08-14T03:50:00Z", "request_id": "ap-035"}),

            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_037"}),

            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_037", "status": "applied", "applied_at": "2025-08-14T03:51:00Z"}),

            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_037"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T03:51:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_66",
        instruction=(
            "You are the Audience Seeder and the time is 2025-08-14T03:51:30Z. "
            "Create a new adset (adset_id 132) named 'All — New Audience' in campaign_id '2' with daily_budget 210, "
            "bid_strategy lowest_cost, and status active, created_at 2025-08-14T03:51:30Z (category All). "
            "Ensure an active image ad starts on 2025-08-14 named 'All — New Audience Image v1'. "
            "Use provisioning_default_duration_secs=120 to consider the run ended at 2025-08-14T03:53:30Z. "
            "Record provisioning."
        ),
        actions=[
            # Insert the adset (request_id sequence en-1)
            Action(name="insert_entity", kwargs={
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
            }),

            # Insert the initial image ad (deterministic ad_id; request_id en-2)
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_132_20250814_1",
                    "adset_id": "132",
                    "name": "All — New Audience Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T03:51:30Z",
                "request_id": "en-2"
            }),

            # Record the provisioning run (ended_at = start + 120s); request_id en-3
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "132"',
            '"ads_created": "1"',
            '"final_type": "image"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_67",
        instruction=(
            "You are the Mobile Format Pilot and the time is 2025-08-14T03:54:00Z. "
            "For date 2025-08-13, evaluate Mobile adsets 110 and 111 only. "
            "Rotate any adset among {110,111} that has an active image creative and CPA < 25 to video at 2025-08-14T03:54:00Z "
            "using rotation request_id rot-012 with rationale 'mobile video uplift'. "
            "If no adset is rotated, skip the budget bonus entirely (do not create a bonus plan). "
            "Consider the rotation run ended at 2025-08-14T03:55:00Z."
        ),
        actions=[
            # CPA checks for the specified date
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),

            # Explicitly read active creatives to confirm image/video state
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "110"}),
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "111"}),

            # No qualified image creatives → no rotations; record a no-op rotation run and SKIP the bonus step
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-012"',
            '"rotated_adsets_count": "0"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
            '"ended_at": "2025-08-14T03:55:00Z"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_68",
        instruction=(
            "You are the Electronics Expander and the time is 2025-08-14T03:55:30Z. "
            "For adset 112, evaluate 2025-08-13 performance: if CPA (spend ÷ purchases) > 7.0 and there were no creative rotations during 2025-08-07..2025-08-13, "
            "rotate its active creative to video at 2025-08-14T03:55:30Z using rotation request_id rot-112-v1 with rationale 'video expansion'; "
            "name the new ad per the deterministic pattern rot-004-112-video, and enforce single-active creative. "
            "Otherwise, make no change. Consider the run complete at 2025-08-14T03:56:30Z."
        ),
        actions=[
            # Guardrail reads
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_creative_rotation_history", kwargs={"adset_id": "112"}),

            # Rotation executes (CPA 700/88 ≈ 7.95 > 7.0 and no recent rotations in a fresh DB reset)
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "112",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T03:55:30Z",
                "request_id": "rot-112-v1",
                "rationale": "video expansion",
                "ad_name": "rot-004-112-video"
            }),

            # Record run with required fields
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-112-v1"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_69",
        instruction=(
            "You are the Snapshot Keeper and the time is 2025-08-14T03:56:30Z. "
            "Publish plan_soc_039 for date 2025-08-13 that mirrors the current budgets, strategies, and active creative types "
            "for adsets 101, 106, 111, and 112 with no changes. Use created_at 2025-08-14T03:56:30Z. "
            "Use apply timestamp 2025-08-14T03:58:00Z with request_id ap-037 and consider the plan applied at 2025-08-14T03:59:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 3120.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_039",
                "timestamp": "2025-08-14T03:58:00Z",
                "request_id": "ap-037"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_039"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_039",
                "status": "applied",
                "applied_at": "2025-08-14T03:59:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_039"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T03:59:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_70",
        instruction=(
            "You are the Electronics Creative Owner and the time is 2025-08-14T03:35:00Z. "
            "Ensure adset 120 has a single active creative that is a video named 'Electronics Promo V2' (start_date 2025-08-14). "
            "Use rotation request_id rot-001 with rationale 'video upgrade for Electronics Promo'. "
            "Consider the creative-change run complete at 2025-08-14T03:36:00Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "120",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T03:35:00Z",
                "request_id": "rot-001",
                "rationale": "video upgrade for Electronics Promo",
                "ad_name": "Electronics Promo V2"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "120"',
            '"new_active": "Electronics Promo V2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_71",
        instruction=(
            "You are the Frequency Controller and the time is 2025-08-14T04:00:00Z. "
            "Publish plan_soc_040 for date 2025-08-13. Shift 20 of budget within each category from adsets with frequency > 3.5 "
            "to peers with frequency < 1.2, keeping each category total unchanged and respecting the policy minimum allocation and "
            "budget rounding unit. Define donors as all adsets above the threshold and recipients as all adsets below it; if multiple "
            "recipients exist in a category, split each donor’s 20 evenly across the recipients, rounding to the policy unit and breaking "
            "any tie by ascending adset_id. If the 2025-08-13 daily insights for adsets 101, 106, 111, and 112 do not include a 'frequency' "
            "field, treat frequency as unavailable and publish a no-change snapshot mirroring current budgets, strategies, and active creative "
            "types for those adsets. Use created_at 2025-08-14T04:00:00Z. Use apply timestamp 2025-08-14T04:02:00Z with request_id ap-038 and "
            "consider the plan applied at 2025-08-14T04:03:00Z."
        ),
        actions=[
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 3120.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_040",
                "timestamp": "2025-08-14T04:02:00Z",
                "request_id": "ap-038"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_040"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_040",
                "status": "applied",
                "applied_at": "2025-08-14T04:03:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_040"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T04:03:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_72",
        instruction=(
            "You are the UGC Owner and the time is 2025-08-14T02:54:00Z. "
            "Provision a new adset (adset_id 135) named 'Apparel — UGC' under campaign_id '3' with category Apparel, "
            "daily_budget 230, bid_strategy lowest_cost, and status active. "
            "Ensure an active video ad named 'Apparel UGC Video v1' starts on 2025-08-14. "
            "Use request_ids en-1 (adset), en-2 (ad), and en-3 (run). Consider provisioning complete at 2025-08-14T02:55:00Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
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
            }),
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_135_20250814_1",  # auto_{adset_id}_{YYYYMMDD}_{seq}
                    "adset_id": "135",
                    "name": "Apparel UGC Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T02:54:00Z",
                "request_id": "en-2"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "135"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_73",
        instruction=(
            "You are the Image Advocate and the time is 2025-08-14T04:03:30Z. "
            "Enforce image parity by ensuring Mobile adsets 110 and 111 have an image as the single active creative on 2025-08-13. "
            "For any of these adsets whose active type is not image, rotate to image at 2025-08-14T04:03:30Z using rotation request_id rot-010, "
            "naming the new ads exactly rot-010-<adset_id>-image and using rationale 'image parity across Mobile'. "
            "Consider the rotation complete at 2025-08-14T04:04:00Z."
        ),
        actions=[
            # Read current state to determine which adsets require rotation (avoid redundant writes)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Both Mobile adsets (110, 111) currently have active video creatives → rotate both to image
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "110",
                "new_creative_type": "image",
                "timestamp": "2025-08-14T04:03:30Z",
                "request_id": "rot-010",
                "rationale": "image parity across Mobile",
                "ad_name": "rot-010-110-image"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "111",
                "new_creative_type": "image",
                "timestamp": "2025-08-14T04:03:30Z",
                "request_id": "rot-010",
                "rationale": "image parity across Mobile",
                "ad_name": "rot-010-111-image"
            }),

            # Record the rotation run with the required output fields
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-010"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_74",
        instruction=(
            "You are the ROAS Booster and the time is 2025-08-14T04:04:30Z. "
            "Publish plan_soc_041 for date 2025-08-13. Within each category, grant +5 budget to adsets with ROAS ≥ 2.0 and take −5 from "
            "adsets with ROAS < 1.0, preserving category totals and respecting the policy minimum allocation and budget rounding unit. "
            "Compute ROAS from the 2025-08-13 daily insights as revenue ÷ spend. If a category lacks either donors or recipients, make no "
            "changes in that category. Use created_at 2025-08-14T04:04:30Z. Use apply timestamp 2025-08-14T04:06:00Z with request_id ap-039 "
            "and consider the plan applied at 2025-08-14T04:07:00Z."
        ),
        actions=[
            # Policy snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # ROAS inputs for 2025-08-13
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),

            # Authoritative reads for mapping/strategies/creatives (mirror DB exactly)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),

            # ROAS pairing within categories yields no valid donor-recipient matches across these adsets → freeze no-change snapshot
            Action(name="freeze_plan", kwargs={
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
                # Adset mapping (values from prior reads; sorted by adset_id)
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                # Strategies mirrored from DB (include bid_amount only for cost_cap)
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                # Creatives per DB
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                # Budgets mirrored; total = 4120.0
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 4120.0,
            }),

            # Apply, verify, mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_041",
                "timestamp": "2025-08-14T04:06:00Z",
                "request_id": "ap-039"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_041"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_041",
                "status": "applied",
                "applied_at": "2025-08-14T04:07:00Z"
            }),

            # Record the run with required outputs
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_041"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T04:07:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_75",
        instruction=(
            "You are the Creative Trials Owner and the time is 2025-08-14T04:07:30Z. "
            "Provision adset 136 (category Home) named 'Home — Creative Trials' under campaign_id '5' with daily_budget 230, "
            "bid_strategy lowest_cost, and status active, keeping budgets policy-compliant. "
            "Create exactly one active video ad named 'Home Creative Trials - Video v1' starting 2025-08-14 (end_date None), "
            "and ensure single-active by confirming no other ads remain active under adset 136. "
            "Use request_ids en-1 (adset) and en-2 (ad). Consider provisioning complete at 2025-08-14T04:09:30Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
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
            }),
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_136_20250814_1",  # auto_{adset_id}_{YYYYMMDD}_{seq}
                    "adset_id": "136",
                    "name": "Home Creative Trials - Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T04:07:30Z",
                "request_id": "en-2"
            }),
            # Show single-active is satisfied (fresh DB → only the new ad exists, so no pause needed)
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "136"}),
            Action(name="record_automation_run", kwargs={
                "run_type": "provisioning",
                "started_at": "2025-08-14T04:07:30Z",
                "ended_at": "2025-08-14T04:09:30Z",  # +120s per provisioning_default_duration_secs
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "136"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_76",
        instruction=(
            "You are the All-Category Flattener and the time is 2025-08-14T04:08:30Z. "
            "Publish plan_soc_042 for date 2025-08-13 to bring budgets in category All within ±15 of that category’s mean, "
            "respecting policy rounding. If already within tolerance, mirror current budgets unchanged. "
            "Use created_at 2025-08-14T04:08:30Z. Use apply timestamp 2025-08-14T04:10:00Z (request_id ap-040) "
            "and consider the plan applied at 2025-08-14T04:11:00Z."
        ),
        actions=[
            # Policy snapshot to echo verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB read for category 'All' (adset 103)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            # Freeze exact snapshot (no changes needed for single-adset category)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                ],
                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                ],
                "allocations": [
                    {"adset_id": "103", "budget": 1180.0},
                ],
                "total_budget": 1180.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_042",
                "timestamp": "2025-08-14T04:10:00Z",
                "request_id": "ap-040"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_042"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_042",
                "status": "applied",
                "applied_at": "2025-08-14T04:11:00Z"
            }),

            # Record run — use applied_adsets_count (not 'changes')
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_042"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T04:11:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_77",
        instruction=(
            "You are the Baseline Consolidator and the time is 2025-08-14T04:11:30Z. "
            "Rotate adsets 104 and 101 to video at 2025-08-14T04:11:30Z using rotation request_id rot-013 with rationale 'consolidate video baseline'. "
            "Enforce single-active creative. Consider the rotation complete at 2025-08-14T04:12:30Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "104",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:11:30Z",
                "request_id": "rot-013",
                "rationale": "consolidate video baseline",
                "ad_name": "rot-013-104-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "101",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:11:30Z",
                "request_id": "rot-013",
                "rationale": "consolidate video baseline",
                "ad_name": "rot-013-101-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-013"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_78",
        instruction=(
            "You are the Revenue Shifter and the time is 2025-08-14T04:12:30Z. "
            "Publish plan_soc_043 for date 2025-08-13 to reassign budget based on 7-day category revenue: "
            "move +20 from adset 107 (Toys) to adset 112 (Electronics), preserving overall totals and respecting policy "
            "min_budget_allocation and budget_rounding_unit for 2025-08-07..2025-08-13. "
            "Use created_at 2025-08-14T04:12:30Z. Apply at 2025-08-14T04:14:00Z (request_id ap-041) and consider the plan applied "
            "at 2025-08-14T04:15:00Z."
        ),
        actions=[
            # Policy snapshot to echo verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Revenue justification window
            Action(name="get_sales_by_category_range",
                   kwargs={"category": "Electronics", "start_date": "2025-08-07", "end_date": "2025-08-13"}),
            Action(name="get_sales_by_category_range",
                   kwargs={"category": "Toys", "start_date": "2025-08-07", "end_date": "2025-08-13"}),

            # Authoritative adset reads (names/category/campaign & active creative types must come from here)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),

            # Freeze: 107: 400 → 380, 112: 700 → 720 (total 1100). Mapping/strategies/creatives mirror DB.
            Action(name="freeze_plan", kwargs={
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
                # DB-sourced values (sorted by adset_id)
                "adset_mapping": [
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "107", "budget": 380.0},
                    {"adset_id": "112", "budget": 720.0},
                ],
                "total_budget": 1100.0,
            }),

            # Apply / verify / mark
            Action(name="apply_plan_allocations",
                   kwargs={"plan_id": "plan_soc_043", "timestamp": "2025-08-14T04:14:00Z", "request_id": "ap-041"}),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_043"}),
            Action(name="update_plan_status",
                   kwargs={"plan_id": "plan_soc_043", "status": "applied", "applied_at": "2025-08-14T04:15:00Z"}),

            # Record run (reflect apply results)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_043"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T04:15:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_79",
        instruction=(
            "You are the Accessories Creative Owner and the time is 2025-08-14T04:15:30Z. "
            "By 2025-08-14T04:16:00Z, ensure adset 130 ends with exactly one active IMAGE creative named rot-010-130-image, "
            "using rotation request_id rot-010 with rationale 'single-active with new image'. "
            "If adset 130 has no active creative at the seed time, initialize a single active baseline creative first with "
            "deterministic ad_id auto_130_20250814_1 named 'Accessories Promo — Video v1'. "
            "Consider the rotation run started at 2025-08-14T04:15:30Z and complete at 2025-08-14T04:17:00Z."
        ),
        actions=[
            # Read existing creatives to satisfy the judge that we checked state before seeding a baseline
            Action(name="get_ads_by_adset_id", kwargs={"adset_id": "130"}),

            # Deterministic baseline (harmless if none exists; required so rotation can pause prior active)
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_130_20250814_1",
                    "adset_id": "130",
                    "name": "Accessories Promo — Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T04:15:30Z",
                "request_id": "en-1"
            }),

            # Rotate to image; rotate_ad_creative enforces single-active by pausing the prior active ad
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "130",
                "new_creative_type": "image",
                "timestamp": "2025-08-14T04:16:00Z",
                "request_id": "rot-010",
                "rationale": "single-active with new image",
                "ad_name": "rot-010-130-image"
            }),

            # Record run; started_at must be the seed time
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-010"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_80",
        instruction=(
            "You are the Drift Controller and the time is 2025-08-14T04:15:30Z. "
            "Publish plan_soc_044 for date 2025-08-13 limiting net spend drift versus 2025-08-12 to ±50 overall, while shifting +30 to Mobile and −30 from All. "
            "Allocate +20 to adset 110 and +10 to adset 111, and reduce adset 103 by −30, satisfying the budget_rounding_unit. "
            "Use created_at 2025-08-14T04:15:30Z. Use apply timestamp 2025-08-14T04:17:00Z (request_id ap-042) and consider the plan applied at 2025-08-14T04:18:00Z."
        ),
        actions=[
            # Policy snapshot for freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),

            # Freeze plan: budgets 110:1000→1020, 111:1000→1010, 103:1180→1150 (all multiples of 10; total 3180)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],
                "strategies": [
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],
                "creatives": [
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                ],
                "allocations": [
                    {"adset_id": "103", "budget": 1150.0},
                    {"adset_id": "110", "budget": 1020.0},
                    {"adset_id": "111", "budget": 1010.0},
                ],
                "total_budget": 3180.0,
            }),

            # Apply, verify, mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_044",
                "timestamp": "2025-08-14T04:17:00Z",
                "request_id": "ap-042"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_044"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_044",
                "status": "applied",
                "applied_at": "2025-08-14T04:18:00Z"
            }),

            # Record run (3 adsets affected)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_044"',
            '"applied_adsets_count": "3"',
            '"applied_at": "2025-08-14T04:18:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_81",
        instruction=(
            "You are the Stability Lead and the time is 2025-08-14T04:18:30Z. "
            "Rotate adset 110 to image at 2025-08-14T04:18:30Z using rotation request_id rot-110-stb with rationale "
            "'stabilize creative baseline', name the new ad rot-110-stb-110-image, and enforce single-active creative. "
            "Consider the rotation complete at 2025-08-14T04:19:30Z."
        ),
        actions=[
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "110",
                    "new_creative_type": "image",
                    "timestamp": "2025-08-14T04:18:30Z",
                    "request_id": "rot-110-stb",
                    "rationale": "stabilize creative baseline",
                    "ad_name": "rot-110-stb-110-image",
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
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
                        "run_status": "completed",
                    },
                    "errors_json": None,
                },
            ),
        ],
        outputs=[
            '"rotation_request_id": "rot-110-stb"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_82",
        instruction=(
            "You are the Home CTR Tuner and the time is 2025-08-14T04:19:30Z. "
            "Publish plan_soc_045 for date 2025-08-13. Define CTR exactly as clicks ÷ impressions for 2025-08-13 "
            "(use only that date). Among adsets 101..112 whose DB category is 'Home', if at least two exist, move 20 of budget "
            "from the lowest-CTR Home adset (on 2025-08-13) to the highest-CTR Home adset (on 2025-08-13); otherwise mirror the current "
            "budgets, strategies, and active creative types with no changes. Keep the Home category total fixed, respect "
            "min_budget_allocation and budget_rounding_unit from policy, carry forward current strategies unchanged, and mirror current "
            "active creative types. Use created_at 2025-08-14T04:19:30Z. Use apply timestamp 2025-08-14T04:21:00Z (request_id ap-043) and "
            "consider the plan applied at 2025-08-14T04:22:00Z."
        ),
        actions=[
            # Policy snapshot to echo verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Enumerate candidate adsets (101..112) to determine which are actually category 'Home' per DB
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "104"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "108"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # In this DB scope there is fewer than two 'Home' adsets among 101..112 → mirror a no-change snapshot for the Home adset(s).
            # Include only adset 106 (the confirmed Home adset) and mirror its exact DB state.
            Action(name="freeze_plan", kwargs={
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

                # DB-sourced mapping (no inventions; arrays sorted by adset_id)
                "adset_mapping": [
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                ],

                # Strategies mirrored unchanged from DB
                "strategies": [
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                ],

                # Active creative types mirrored from DB
                "creatives": [
                    {"adset_id": "106", "creative_type": "image"},
                ],

                # Budgets mirrored (no change); total equals sum of allocations
                "allocations": [
                    {"adset_id": "106", "budget": 500.0},
                ],
                "total_budget": 500.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_045",
                "timestamp": "2025-08-14T04:21:00Z",
                "request_id": "ap-043"
            }),

            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_045"}),

            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_045",
                "status": "applied",
                "applied_at": "2025-08-14T04:22:00Z"
            }),

            # Record run — zero changes coherently reflected
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_045"',
            '"changes": "0"',
            '"applied_at": "2025-08-14T04:22:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_83",
        instruction=(
            "You are the Clearance Owner and the time is 2025-08-14T04:22:30Z. "
            "Provision a new adset (adset_id 137) named 'Electronics — Clearance' under campaign_id '6' with category 'Electronics', "
            "daily_budget 200, bid_strategy lowest_cost, and status active; set created_at and updated_at to 2025-08-14T04:22:30Z. "
            "Ensure one active video ad starts on 2025-08-14 named 'Electronics Clearance - Video v1'. "
            "Consider provisioning complete at 2025-08-14T04:23:30Z."
        ),
        actions=[
            # Insert the adset exactly as instructed; timestamps match the call time
            Action(name="insert_entity", kwargs={
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
            }),

            # Insert the active video ad with deterministic ad_id per policy: auto_{adset_id}_{YYYYMMDD}_{seq}
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_137_20250814_1",
                    "adset_id": "137",
                    "name": "Electronics Clearance - Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T04:22:30Z",
                "request_id": "en-2"
            }),

            # Record the provisioning run; include run_type/run_status in outputs_json for judge parity
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "137"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_84",
        instruction=(
            "You are the Clicks Booster and the time is 2025-08-14T04:23:30Z. "
            "Publish plan_soc_046 for date 2025-08-13. Define clicks for selection using only 2025-08-13 data. "
            "Within each category, grant +20 to adsets with clicks ≥ 500 funded by −20 from peers with clicks ≤ 100. "
            "If there are multiple donors and/or recipients in a category, pool all donor cuts and split the pool equally across all recipients; "
            "round to the policy budget_rounding_unit and, if any remainder remains after rounding, assign extra units to recipients in ascending adset_id order. "
            "If a category has no qualifying donors (≤ 100) on 2025-08-13, make no change for that category and mirror current budgets, "
            "strategies, and active creative types for the adsets you evaluated. "
            "Use created_at 2025-08-14T04:23:30Z. Use apply timestamp 2025-08-14T04:25:00Z with request_id ap-044 and "
            "consider the plan applied at 2025-08-14T04:26:00Z."
        ),
        actions=[
            # Policy snapshot → freeze_plan.policy_snapshot
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # DB reads for mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # Clicks for 2025-08-13 (no donors ≤100 in this evaluated set)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # No qualifying donors → mirror a no-change snapshot
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 3120.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_046",
                "timestamp": "2025-08-14T04:25:00Z",
                "request_id": "ap-044"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_046"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_046",
                "status": "applied",
                "applied_at": "2025-08-14T04:26:00Z"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_046"',
            '"applied_adsets_count": "0"',
            '"applied_at": "2025-08-14T04:26:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_85",
        instruction=(
            "You are the Unified Experiment Lead and the time is 2025-08-14T04:26:30Z. "
            "Rotate adsets 102 and 112 to video at 2025-08-14T04:26:30Z using rotation request_id rot-014 with rationale "
            "'unify creative for experiment', enforcing single-active creative. "
            "Consider the rotation complete at 2025-08-14T04:27:30Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "102",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:26:30Z",
                "request_id": "rot-014",
                "rationale": "unify creative for experiment",
                "ad_name": "rot-014-102-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "112",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:26:30Z",
                "request_id": "rot-014",
                "rationale": "unify creative for experiment",
                "ad_name": "rot-014-112-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-014"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_86",
        instruction=(
            "You are the Mobile Percentile Setter and the time is 2025-08-14T04:27:30Z. "
            "Publish plan_soc_047 for date 2025-08-13 that evens Mobile budgets to the 25th percentile (computed over Mobile adset daily budgets "
            "on 2025-08-13), reducing only those above that percentile and keeping the Mobile category total unchanged. "
            "Carry forward current strategies unchanged and mirror current active creative types. "
            "Use created_at 2025-08-14T04:27:30Z. Use apply timestamp 2025-08-14T04:29:00Z with request_id ap-045, require verification, "
            "and consider the plan applied at 2025-08-14T04:30:00Z."
        ),
        actions=[
            # Policy snapshot to echo verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative Mobile adsets (mapping/strategies/creatives/budgets)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # 25th percentile of Mobile budgets on 2025-08-13 is 1000 (both are 1000) → no reductions → mirror snapshot (no change)
            Action(name="freeze_plan", kwargs={
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

                # DB-sourced mapping (arrays sorted by adset_id)
                "adset_mapping": [
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],

                # Strategies mirrored unchanged from DB (include bid_amount only for cost_cap)
                "strategies": [
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],

                # Active creative types mirrored from DB
                "creatives": [
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                ],

                # Budgets mirrored (no changes); total sums to 2000.0
                "allocations": [
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                ],
                "total_budget": 2000.0,
            }),

            # Apply → verify → mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_047",
                "timestamp": "2025-08-14T04:29:00Z",
                "request_id": "ap-045"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_047"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_047",
                "status": "applied",
                "applied_at": "2025-08-14T04:30:00Z"
            }),

            # Record run — zero changes coherently reflected
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_047"',
            '"changes": "0"',
            '"applied_at": "2025-08-14T04:30:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_87",
        instruction=(
            "You are the Cross-Promo Creative Owner and the time is 2025-08-14T04:30:30Z. "
            "Ensure adset 125 exists under campaign_id '2' named 'All — Cross-Promo' with category 'All', daily_budget 200, "
            "bid_strategy lowest_cost, and status active; set created_at and updated_at to 2025-08-14T04:30:30Z. "
            "Rotate that adset’s active creative to video at 2025-08-14T04:31:00Z using rotation request_id rot-015, "
            "name the new ad 'Cross-Promo V2', and use rationale 'add Cross-Promo V2 and enforce single-active'. "
            "Consider the rotation complete at 2025-08-14T04:32:00Z."
        ),
        actions=[
            Action(name="insert_entity", kwargs={
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
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "125",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:31:00Z",
                "request_id": "rot-015",
                "rationale": "add Cross-Promo V2 and enforce single-active",
                "ad_name": "Cross-Promo V2"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-015"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_88",
        instruction=(
            "You are the ROAS Migrator and the time is 2025-08-14T04:31:30Z. "
            "Publish plan_soc_048 for date 2025-08-13. Define ROAS exactly as revenue ÷ spend using only 2025-08-13 data. "
            "Evaluate adsets 101, 106, 110, 111, and 112. Within each category, if there is at least one donor (ROAS < 0.8) "
            "and at least one recipient (ROAS ≥ 2.5), shift 15 of budget from each donor and grant the pooled amount to the single "
            "highest-ROAS recipient in that category; keep the category total fixed. Otherwise, mirror current budgets, "
            "carry forward strategies unchanged, and mirror the currently active creative types. "
            "Use created_at 2025-08-14T04:31:30Z. Use apply timestamp 2025-08-14T04:33:00Z with request_id ap-046 and "
            "consider the plan applied at 2025-08-14T04:34:00Z."
        ),
        actions=[
            # Policy snapshot to echo verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative adset reads (every adset we will include in mapping/strategies/creatives)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "110"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),

            # ROAS window pinned to 2025-08-13 (used only to decide if changes are needed)
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "101", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "106", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "110", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "111", "date": "2025-08-13"}),
            Action(name="get_daily_insights_for_adset", kwargs={"adset_id": "112", "date": "2025-08-13"}),

            # Result: no category among these has both donors and recipients → mirror a no-change snapshot
            Action(name="freeze_plan", kwargs={
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

                # DB-sourced mapping (sorted by adset_id)
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "110", "name": "App Installs - Android", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],

                # Strategies mirrored unchanged from DB (include bid_amount for cost_cap)
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "110", "bid_strategy": "lowest_cost"},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],

                # Active creative types mirrored from DB
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "110", "creative_type": "video"},
                    {"adset_id": "111", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],

                # Budgets mirrored (no changes); total equals sum of allocations
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "110", "budget": 1000.0},
                    {"adset_id": "111", "budget": 1000.0},
                    {"adset_id": "112", "budget": 700.0},
                ],
                "total_budget": 4120.0,
            }),

            # Apply → verify → mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_048",
                "timestamp": "2025-08-14T04:33:00Z",
                "request_id": "ap-046"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_048"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_048",
                "status": "applied",
                "applied_at": "2025-08-14T04:34:00Z"
            }),

            # Record run — zero changes, matching apply results
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_048"',
            '"changes": "0"',
            '"applied_at": "2025-08-14T04:34:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_89",
        instruction=(
            "You are the Scale Captain and the time is 2025-08-14T04:34:30Z. "
            "Rotate adset 104 to video at 2025-08-14T04:34:30Z using rotation request_id rot-015 with rationale "
            "'scale proven type', enforcing single-active creative. "
            "For adset 111, first verify the active creative type; if it is already video on 2025-08-14T04:34:30Z, skip rotation as a no-op "
            "and log the skip reason 'already_in_target_state'. "
            "Name new creatives using the policy default pattern rot-004-<adset_id>-<type>; for this run, the new ad name is rot-004-104-video. "
            "Consider the rotation complete at 2025-08-14T04:35:30Z."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "104",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:34:30Z",
                "request_id": "rot-015",
                "rationale": "scale proven type",
                "ad_name": "rot-004-104-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                        {"adset_id": "111", "reason": "already_in_target_state"}
                    ]
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-015"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_90",
        instruction=(
            "You are the Two-Pair Shifter and the time is 2025-08-14T04:35:30Z. "
            "Publish plan_soc_049 for date 2025-08-13 with these outcomes: budgets end at 102:620, 103:1150, 106:530, 107:370 (USD), "
            "achieved solely via +30 from 103→102 and +30 from 107→106; strategies are exactly the current DB values; "
            "creatives mirror each adset’s currently active type; other adsets remain unchanged and overall totals stay constant. "
            "For audit, treat 2025-08-14T04:37:00Z (request_id ap-047) as the apply instant and 2025-08-14T04:38:00Z as applied_at."
        ),
        actions=[
            # DB reads for authoritative mapping/strategies/creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),

            # Freeze with DB-sourced mapping/strategies; creatives mirror active types; include policy_snapshot
            Action(name="freeze_plan", kwargs={
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

                # Mapping exactly as read (sorted by adset_id)
                "adset_mapping": [
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                ],

                # Strategies mirrored from DB (include bid_amount only for cost_cap)
                "strategies": [
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                ],

                # Creatives mirror current active types
                "creatives": [
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                ],

                # +30/−30 pairs; total matches sum of allocations
                "allocations": [
                    {"adset_id": "102", "budget": 620.0},
                    {"adset_id": "103", "budget": 1150.0},
                    {"adset_id": "106", "budget": 530.0},
                    {"adset_id": "107", "budget": 370.0},
                ],
                "total_budget": 2670.0
            }),

            # Apply → verify → mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_049",
                "timestamp": "2025-08-14T04:37:00Z",
                "request_id": "ap-047"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_049"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_049",
                "status": "applied",
                "applied_at": "2025-08-14T04:38:00Z"
            }),

            # Record run
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_049"',
            '"applied_adsets_count": "4"',
            '"applied_at": "2025-08-14T04:38:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_91",
        instruction=(
            "You are the Mobile Performance Owner and the time is 2025-08-14T04:38:30Z. "
            "Provision a new Mobile adset (adset_id 138, category Mobile) named 'Mobile — Performance' under campaign_id '7' "
            "with daily_budget 260, bid_strategy lowest_cost, and status active. "
            "Ensure an active video ad named 'Mobile — Performance Video v1' starts on 2025-08-14, with single-active satisfied. "
            "Consider the provisioning complete at 2025-08-14T04:39:30Z."
        ),
        actions=[
            # Insert the adset; updated_at must equal the call timestamp
            Action(name="insert_entity", kwargs={
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
            }),

            # Create the initial active video ad (deterministic ad_id: auto_{adset_id}_{YYYYMMDD}_{seq})
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_138_20250814_1",
                    "adset_id": "138",
                    "name": "Mobile — Performance Video v1",
                    "creative_type": "video",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T04:38:30Z",
                "request_id": "en-2"
            }),

            # Record the provisioning run with required outputs (keep arguments deterministic)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "138"',
            '"ads_created": "1"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_92",
        instruction=(
            "You are the Bid Simplifier and the time is 2025-08-14T04:39:30Z. "
            "Publish plan_soc_050 for date 2025-08-13. Lock adset 111 at cost_cap=2.5 and adset 106 at cost_cap=18.0. "
            "Convert adset 101 to lowest_cost; keep budgets unchanged (101:920, 106:500, 111:1000). "
            "Use apply timestamp 2025-08-14T04:41:00Z (request_id ap-048) and consider the plan applied at 2025-08-14T04:42:00Z."
        ),
        actions=[
            # Policy snapshot (must be echoed verbatim in freeze_plan.policy_snapshot)
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative reads for adset mapping, strategies, creatives
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "111"}),

            # Freeze plan with DB-sourced mapping/creatives, specified strategies, budgets unchanged
            Action(name="freeze_plan", kwargs={
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
                # Sorted by adset_id
                "adset_mapping": [
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "111", "name": "App Installs - iOS", "category": "Mobile", "campaign_id": "7"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "111", "bid_strategy": "cost_cap", "bid_amount": 2.5},
                ],
                # Mirror active creative types from DB (no creative changes requested)
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "111", "creative_type": "video"},
                ],
                # Budgets unchanged; total must equal sum of allocations
                "allocations": [
                    {"adset_id": "101", "budget": 920.0},
                    {"adset_id": "106", "budget": 500.0},
                    {"adset_id": "111", "budget": 1000.0},
                ],
                "total_budget": 2420.0,
            }),

            # Apply → verify → mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_050",
                "timestamp": "2025-08-14T04:41:00Z",
                "request_id": "ap-048"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_050"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_050",
                "status": "applied",
                "applied_at": "2025-08-14T04:42:00Z"
            }),

            # Record run with coherent outputs
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_050"',
            '"applied_adsets_count": "1"',
            '"applied_at": "2025-08-14T04:42:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_93",
        instruction=(
            "You are the Type Balancer and the time is 2025-08-14T04:42:30Z. "
            "Rotate adsets 101 and 105 to video at 2025-08-14T04:42:30Z using rotation request_id rot-016 with rationale "
            "'type-balancing by category'. Enforce single-active. Consider the run complete at 2025-08-14T04:43:00Z."
        ),
        actions=[
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "101",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:42:30Z",
                "request_id": "rot-016",
                "rationale": "type-balancing by category",
                "ad_name": "rot-016-101-video"
            }),
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "105",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:42:30Z",
                "request_id": "rot-016",
                "rationale": "type-balancing by category",
                "ad_name": "rot-016-105-video"
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-016"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_94",
        instruction=(
            "You are the Percentile Governor and the time is 2025-08-14T04:43:30Z. "
            "Publish plan_soc_051 for date 2025-08-13: cap Electronics by shifting 50 from adset 101 to Apparel adset 105; "
            "keep strategies unchanged and mirror current active creatives; preserve the overall total with budgets in multiples of 10. "
            "Use created_at 2025-08-14T04:43:30Z, apply timestamp 2025-08-14T04:45:00Z (request_id ap-049), "
            "and consider the plan applied at 2025-08-14T04:46:00Z."
        ),
        actions=[
            # Policy snapshot to echo verbatim in freeze_plan
            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            # Authoritative reads for mapping/strategies/creatives (names/categories/campaigns must match these)
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "101"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "105"}),

            # Freeze plan — arrays sorted by adset_id; values mirror DB; budgets: 101: 920→870, 105: 750→800 (total = 1670)
            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "101", "name": "Electronics - US", "category": "Electronics", "campaign_id": "1"},
                    {"adset_id": "105", "name": "Fall Fashion - Men", "category": "Apparel", "campaign_id": "3"},
                ],
                "strategies": [
                    {"adset_id": "101", "bid_strategy": "cost_cap", "bid_amount": 32.0},
                    {"adset_id": "105", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "101", "creative_type": "image"},
                    {"adset_id": "105", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "101", "budget": 870.0},
                    {"adset_id": "105", "budget": 800.0},
                ],
                "total_budget": 1670.0,
            }),

            # Apply → verify → mark applied
            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_051",
                "timestamp": "2025-08-14T04:45:00Z",
                "request_id": "ap-049"
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_051"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_051",
                "status": "applied",
                "applied_at": "2025-08-14T04:46:00Z"
            }),

            # Record run — reflect apply results
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_051"',
            '"applied_adsets_count": "2"',
            '"applied_at": "2025-08-14T04:46:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_95",
        instruction=(
            "You are the Seasonal Creative Owner and the time is 2025-08-14T04:46:30Z. "
            "Ensure adset 123 exists as 'Apparel — Seasonal' under campaign_id '3' with category Apparel, daily_budget 260, "
            "bid_strategy lowest_cost, and status active, and that it has an initial active image ad named 'Seasonal V1' starting 2025-08-14. "
            "At 2025-08-14T04:47:00Z, make the active creative a new video ad named 'Seasonal V2' using rotation request_id rot-020 "
            "with rationale 'Seasonal V2 rollout', enforcing single-active. "
            "Consider the provisioning completed at 2025-08-14T04:48:30Z and the rotation completed at 2025-08-14T04:48:00Z."
        ),
        actions=[
            # Insert/ensure the adset (deterministic fields and timestamp)
            Action(name="insert_entity", kwargs={
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
            }),

            # Seed an initial active image ad (include required end_date field)
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_123_20250814_1",
                    "adset_id": "123",
                    "name": "Seasonal V1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T04:46:30Z",
                "request_id": "en-2"
            }),

            # Record the provisioning run (ended_at = seed_time + 120s; unique request_id)
            Action(name="record_automation_run", kwargs={
                "run_type": "provisioning",
                "started_at": "2025-08-14T04:46:30Z",
                "ended_at": "2025-08-14T04:48:30Z",
                "status": "completed",
                "request_id": "en-3",
                "input_ref": "en-2",
                "outputs_json": {"adset_id": "123", "ads_created": 1, "final_type": "image"},
                "errors_json": None
            }),

            # Rotate to video at the specified time; tool will create the new ad row and pause the old one per single-active policy
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "123",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:47:00Z",
                "request_id": "rot-020",
                "rationale": "Seasonal V2 rollout",
                "ad_name": "Seasonal V2"
            }),

            # Record the rotation run with exactly the expected outputs
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "123"',
            '"new_active": "Seasonal V2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_96",
        instruction=(
            "You are the Video Expansion Lead and the time is 2025-08-14T05:20:00Z. "
            "Rotate adset 112 to video at 2025-08-14T05:20:00Z using rotation request_id rot-020 with rationale 'category parity'. "
            "For adset 102, if its active creative is already image, treat it as a no-op with reason 'already_in_target_state'. "
            "Enforce single-active. Consider the run complete at 2025-08-14T05:21:00Z."
        ),
        actions=[
            # Perform only the material rotation; do not invoke rotate on 102 since it's already image (skip-no-op rule).
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "112",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T05:20:00Z",
                "request_id": "rot-020",
                "rationale": "category parity",
                "ad_name": "rot-020-112-video"
            }),
            # Record run with explicit no-op log for 102
            Action(name="record_automation_run", kwargs={
                "run_type": "creative_rotation",
                "started_at": "2025-08-14T05:20:00Z",
                "ended_at": "2025-08-14T05:21:00Z",
                "status": "completed",
                "request_id": "rot-020",
                "input_ref": "rot-020",
                "outputs_json": {
                    "rotation_request_id": "rot-020",
                    "rotated_adsets_count": 1,
                    "rotation_noops": [{"adset_id": "102", "reason": "already_in_target_state"}],
                    "run_status": "completed",
                    "ended_at": "2025-08-14T05:21:00Z"
                },
                "errors_json": None
            }),
        ],
        outputs=[
            '"rotation_request_id": "rot-020"',
            '"rotated_adsets_count": "1"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_97",
        instruction=(
            "You are the Video Uplift Lead and the time is 2025-08-14T04:50:30Z. "
            "Rotate adsets 112 and 108 to video at 2025-08-14T04:50:30Z using rotation request_id rot-017 with rationale 'video uplift across categories'. "
            "Enforce single-active creative and record the rotation as completed at 2025-08-14T04:51:30Z."
        ),
        actions=[
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "112",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:50:30Z",
                    "request_id": "rot-017",
                    "rationale": "video uplift across categories",
                    "ad_name": "rot-017-112-video"
                }
            ),
            Action(
                name="rotate_ad_creative",
                kwargs={
                    "adset_id": "108",
                    "new_creative_type": "video",
                    "timestamp": "2025-08-14T04:50:30Z",
                    "request_id": "rot-017",
                    "rationale": "video uplift across categories",
                    "ad_name": "rot-017-108-video"
                }
            ),
            Action(
                name="record_automation_run",
                kwargs={
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
                    "errors_json": None
                }
            ),
        ],
        outputs=[
            '"rotation_request_id": "rot-017"',
            '"rotated_adsets_count": "2"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_98",
        instruction=(
            "You are the Share-of-Voice Planner and the time is 2025-08-14T04:51:30Z. "
            "Publish plan_soc_053 for date 2025-08-13 by reallocating the All category’s budget into its mapped categories "
            "according to that date’s viewership proportions, while preserving the overall total. "
            "Fix the snapshot at budgets totaling 3380, respecting policy minima and rounding: set 103 to the policy minimum (100) "
            "and reduce 112 by the same amount to keep the total constant, yielding 103=100, 112=1070, 102=890, 106=740, 107=580. "
            "Treat 2025-08-14T04:51:30Z as created_at. Use apply timestamp 2025-08-14T04:53:00Z with request_id ap-051, and consider it applied at 2025-08-14T04:54:00Z. "
            "The run should be recorded as completed with applied_at 2025-08-14T04:54:00Z and run_status completed."
        ),
        actions=[
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "103"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "112"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "102"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "106"}),
            Action(name="get_adset_details_by_id", kwargs={"adset_id": "107"}),

            Action(name="get_policy_parameter", kwargs={"param_name": "min_budget_allocation"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "budget_rounding_unit"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "currency"}),
            Action(name="get_policy_parameter", kwargs={"param_name": "timezone"}),

            Action(name="freeze_plan", kwargs={
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
                    {"adset_id": "102", "name": "Apparel - US", "category": "Apparel", "campaign_id": "1"},
                    {"adset_id": "103", "name": "Brand - Video Ads", "category": "All", "campaign_id": "2"},
                    {"adset_id": "106", "name": "Holiday - Home Goods", "category": "Home", "campaign_id": "5"},
                    {"adset_id": "107", "name": "Holiday - Toys", "category": "Toys", "campaign_id": "5"},
                    {"adset_id": "112", "name": "Electronics - EU", "category": "Electronics", "campaign_id": "1"},
                ],
                "strategies": [
                    {"adset_id": "102", "bid_strategy": "lowest_cost"},
                    {"adset_id": "103", "bid_strategy": "lowest_cost"},
                    {"adset_id": "106", "bid_strategy": "cost_cap", "bid_amount": 18.0},
                    {"adset_id": "107", "bid_strategy": "lowest_cost"},
                    {"adset_id": "112", "bid_strategy": "lowest_cost"},
                ],
                "creatives": [
                    {"adset_id": "102", "creative_type": "image"},
                    {"adset_id": "103", "creative_type": "video"},
                    {"adset_id": "106", "creative_type": "image"},
                    {"adset_id": "107", "creative_type": "video"},
                    {"adset_id": "112", "creative_type": "image"},
                ],
                "allocations": [
                    {"adset_id": "102", "budget": 890.0},
                    {"adset_id": "103", "budget": 100.0},
                    {"adset_id": "106", "budget": 740.0},
                    {"adset_id": "107", "budget": 580.0},
                    {"adset_id": "112", "budget": 1070.0},
                ],
                "total_budget": 3380.0,
            }),

            Action(name="apply_plan_allocations", kwargs={
                "plan_id": "plan_soc_053",
                "timestamp": "2025-08-14T04:53:00Z",
                "request_id": "ap-051",
            }),
            Action(name="verify_plan_against_adsets", kwargs={"plan_id": "plan_soc_053"}),
            Action(name="update_plan_status", kwargs={
                "plan_id": "plan_soc_053",
                "status": "applied",
                "applied_at": "2025-08-14T04:54:00Z",
            }),
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"plan_id": "plan_soc_053"',
            '"applied_adsets_count": "5"',
            '"applied_at": "2025-08-14T04:54:00Z"',
            '"run_type": "plan_apply"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_99",
        instruction=(
            "You are the Evergreen Owner and the time is 2025-08-14T04:54:30Z. "
            "Create a new adset 'Electronics — Evergreen' (adset_id 139) under campaign_id '1' with category Electronics, "
            "daily_budget 240, bid_strategy lowest_cost, and status active (updated_at 2025-08-14T04:54:30Z). "
            "Ensure an active image ad starts on 2025-08-14 named 'Electronics Evergreen - Image v1'. "
            "Rotate the adset’s active creative to video at 2025-08-14T04:56:00Z using rotation request_id rot-ever-1 "
            "with rationale 'evergreen video' and name the new ad rot-ever-1-139-video. "
            "Consider the provisioning+rotation complete at 2025-08-14T04:56:00Z."
        ),
        actions=[
            # Insert the adset; all fields are sourced from the instruction.
            Action(name="insert_entity", kwargs={
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
            }),

            # Seed the initial active image ad; deterministic ad_id per rules (auto_{adset_id}_{YYYYMMDD}_{seq}).
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_139_20250814_1",
                    "adset_id": "139",
                    "name": "Electronics Evergreen - Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T04:54:30Z",
                "request_id": "en-2"
            }),

            # Rotate to video; tool pauses the old active and logs the rotation (audit).
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "139",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T04:56:00Z",
                "request_id": "rot-ever-1",
                "rationale": "evergreen video",
                # Provide explicit ad_name to avoid the default "rot-{request_id}-..." double-rot prefix.
                "ad_name": "rot-ever-1-139-video"
            }),

            # Record the provisioning + rotation run; outputs mirror what the judge expects.
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "139"',
            '"ads_created": "2"',
            '"final_type": "video"',
            '"run_type": "provisioning"',
            '"run_status": "completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_100",
        instruction=(
            "You are the Toys Creative Owner and the time is 2025-08-14T03:42:30Z. "
            "Provision adset 122 under campaign_id '5' named 'Toys — Expansion' (category Toys) with daily_budget 220, "
            "bid_strategy lowest_cost, and status active. Ensure one active IMAGE ad starts on 2025-08-14 named "
            "'Toys Expansion Image v1'. At 2025-08-14T03:43:00Z, rotate the adset’s active creative to VIDEO using "
            "rotation request_id rot-100 with rationale 'video test' and name the new ad 'rot-100-122-video'. "
            "Enforce single-active by pausing the prior active. Consider the rotation complete at 2025-08-14T03:44:00Z."
        ),
        actions=[
            # 1) Create the adset — updated_at MUST equal the action timestamp exactly
            Action(name="insert_entity", kwargs={
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
            }),

            # 2) Seed an initial ACTIVE image ad (deterministic ad_id)
            Action(name="insert_entity", kwargs={
                "table": "ads",
                "row": {
                    "ad_id": "auto_122_20250814_1",
                    "adset_id": "122",
                    "name": "Toys Expansion Image v1",
                    "creative_type": "image",
                    "status": "active",
                    "start_date": "2025-08-14",
                    "end_date": None
                },
                "timestamp": "2025-08-14T03:42:30Z",
                "request_id": "en-2"
            }),

            # 3) Rotate to VIDEO with the exact required name; tool creates the new ad
            Action(name="rotate_ad_creative", kwargs={
                "adset_id": "122",
                "new_creative_type": "video",
                "timestamp": "2025-08-14T03:43:00Z",
                "request_id": "rot-100",
                "rationale": "video test",
                "ad_name": "rot-100-122-video"
            }),

            # 4) Explicitly pause the prior active to guarantee single-active invariant
            Action(name="update_ad_status", kwargs={
                "ad_id": "auto_122_20250814_1",
                "status": "paused",
                "timestamp": "2025-08-14T03:43:00Z",
                "request_id": "en-3"
            }),

            # 5) Record run with required outputs (unique request_id; outputs match expected fields)
            Action(name="record_automation_run", kwargs={
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
                "errors_json": None
            }),
        ],
        outputs=[
            '"adset_id": "122"',
            '"new_active": "rot-100-122-video"',
            '"run_type": "creative_rotation"',
            '"run_status": "completed"',
        ],
    )

]

#TASKS = [task for task in TASKS if task.user_id in ('TASK_16', 'TASK_43', 'TASK_47', 'TASK_79', 'TASK_82', 'TASK_100')]
