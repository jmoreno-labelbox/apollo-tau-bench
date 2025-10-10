from domains.dto import Task, Action

TASKS = [
    # Task 1
    Task(
        annotator="faris",
        user_id="faris_001_comp_analysis_client13_htx025",
        instruction="You must create a comparable analysis for client 13 interested in property HTX025 with 1 comparable selection. Send an email to the client.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "13"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": ["7", "4", "5", "13"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "5"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "13",
                    "broker_id": "5",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 2
    Task(
        annotator="faris",
        user_id="faris_002_comp_client10_htx021_skip_review",
        instruction="You must generate a comparable report for client 10 interested in HTX021 with 1 comparable selection. Send an email to the client.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "10"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "10",
                    "created_by_broker_id": "11",
                    "subject_property_id": "HTX021",
                    "client_neighborhoods": ["13", "1", "12"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX030",
                            "similarity_score": 0.868,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "11"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "10",
                    "broker_id": "11",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 3
    Task(
        annotator="faris",
        user_id="faris_003_investment_comp_client12_htx044",
        instruction="You must verify mortgage rates for client 20, calculate their payment terms, create a mortgage audit entry, and send a general update email with the mortgage details.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 785, "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "1",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "20",
                    "metadata_json": {"mortgage_profile_id": "20"},
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "20",
                    "broker_id": "1",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 4
    Task(
        annotator="faris",
        user_id="faris_004_luxury_comp_client13_htx025_amenities",
        instruction="You must create a comp report for client 13 on HTX025",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "13"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": ["7", "4", "5", "13"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "5"},
            ),
        ],
        outputs=[],
    ),
    # Task 5
    Task(
        annotator="faris",
        user_id="faris_005_montrose_comp_client11_htx012",
        instruction="You must generate a comparable analysis for client 11 evaluating HTX012",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "11"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "11",
                    "created_by_broker_id": "6",
                    "subject_property_id": "HTX012",
                    "client_neighborhoods": ["7", "3", "11", "14"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.57,
                            "selection_reason": "Fair price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "6"},
            ),
        ],
        outputs=[],
    ),
    # Task 6
    Task(
        annotator="faris",
        user_id="faris_006_budget_comp_client7_htx036_400k",
        instruction="You must prepare a market comparison for client 3 looking at HTX021. Calculate property metrics and generate a comp report.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "3",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX021",
                    "client_neighborhoods": ["1", "12", "2", "4", "5"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX030",
                            "similarity_score": 0.868,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="calculate_property_metrics",
                kwargs={
                    "subject_property_id": "HTX021",
                    "comparable_properties": ["HTX030"],
                    "client_budget": {"client_id": "3", "price_max": 631914},
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    # Task 7
    Task(
        annotator="faris",
        user_id="faris_007_medical_center_comp_client8_htx049",
        instruction="You must find up to 4 open houses for client 5 near property HTX025 for the date 2025-08-30 and send an email summary.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX025"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX025",
                    "max_results": 4,
                    "status_filter": ["active", "for_sale"],
                },
            ),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035",
                    ],
                    "date": "2025-08-30",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "5",
                    "broker_id": "1",
                    "template_code": "open_house_summary",
                    "property_id": ["HTX025", "HTX032", "HTX017", "HTX038", "HTX035"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 8
    Task(
        annotator="faris",
        user_id="faris_008_first_time_buyer_client2_htx017",
        instruction="You must create a mortgage profile for client 17 with a loan of $548,318 and a down payment of $109,032, and then calculate their mortgage payment.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "17"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 699, "region": "TX"},
            ),
            Action(
                name="create_mortgage_profile",
                kwargs={
                    "client_id": "17",
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 699,
                    "region": "TX",
                    "annual_income": 78851,
                },
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 9
    Task(
        annotator="faris",
        user_id="faris_009_heights_analysis_client15_htx001",
        instruction="You must prepare a comp analysis for client 15 evaluating HTX001 in Heights neighborhood",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "15"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "Heights"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "15",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX001",
                    "client_neighborhoods": ["4"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX007",
                            "similarity_score": 0.918,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "8"},
            ),
        ],
        outputs=[],
    ),
    # Task 10
    Task(
        annotator="faris",
        user_id="faris_010_river_oaks_analysis_client16_htx007",
        instruction="You must create a comparable analysis for client 16 considering HTX007 in River Oaks",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "16"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "River Oaks"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "16",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX007",
                    "client_neighborhoods": ["5"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.918,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "8"},
            ),
        ],
        outputs=[],
    ),
    # Task 11
    Task(
        annotator="faris",
        user_id="faris_011_condo_analysis_client18_htx030",
        instruction="You must generate a comparable report for client 18 looking at HTX030",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "18"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "18",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": ["13", "9", "14", "15", "11"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "5"},
            ),
        ],
        outputs=[],
    ),
    # Task 12
    Task(
        annotator="faris",
        user_id="faris_012_comp_analysis_client9_htx024",
        instruction="You must prepare a comparable analysis for client 9 evaluating HTX024. You are broker 9.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "9"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "9",
                    "created_by_broker_id": "9",
                    "subject_property_id": "HTX024",
                    "client_neighborhoods": ["1", "12", "14", "3"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "9"},
            ),
        ],
        outputs=[],
    ),
    # Task 13
    Task(
        annotator="faris",
        user_id="faris_013_family_weekend_open_houses_client15_htx042",
        instruction="You are broker 8. Find up to 2 nearby open houses for client 15 near property HTX042 on 2025-08-23, schedule them as 'Weekend open houses schedule' on 2025-08-24 in Houston, TX, and email a summary to the client.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX042"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX042",
                    "max_results": 2,
                    "status_filter": ["active", "for_sale"],
                },
            ),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": ["HTX042", "HTX002", "HTX018"],
                    "date": "2025-08-23",
                },
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "8",
                    "client_id": "15",
                    "title": "Weekend open houses schedule",
                    "date": "2025-08-24",
                    "location": "Houston, TX",
                    "source": "viewing",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "15",
                    "broker_id": "8",
                    "template_code": "open_house_summary",
                    "property_id": ["HTX042", "HTX002", "HTX018"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 14
    Task(
        annotator="faris",
        user_id="faris_014_campaign_curation_client5_htx026",
        instruction="You are curating a 'Townhouse Spotlight' likely_buyer campaign (id: 3) for client 5; you want to summarize the listing data for HTX026, generate a briefing document, and send a briefing email to the client. You are broker 14.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "3"}),
            Action(name="fetch_listings_by_ids", kwargs={"property_ids": ["HTX026"]}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "5", "created_by": "14"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "5",
                    "broker_id": "14",
                    "template_code": "briefing",
                    "campaign_id": "3",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 15
    Task(
        annotator="faris",
        user_id="faris_015_client_comms_client4_briefing",
        instruction="You are preparing a client briefing for client 4; you want to review recent emails since 2025-07-01T00:00:00Z and send a follow-up. Return the client's mortgage id.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "4"}),
            Action(
                name="fetch_emails_for_client",
                kwargs={"client_id": "4", "since_date": "2025-07-01T00:00:00Z"},
            ),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "4", "created_by": "2"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "4",
                    "broker_id": "2",
                    "template_code": "briefing",
                },
            ),
        ],
        outputs=[{"mortgage_id": 4}],
    ),
    # Task 16
    Task(
        annotator="faris",
        user_id="faris_016_plan_route_client4_broker2",
        instruction="You are broker 2, planning a 3-stop viewing route for client 4 on 2025-09-20, starting from the client's commute address, with the first stop being HTX003. Hops should be under 25 minutes. Do not verify that the route was created or create a calendar event.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "4"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX003",
                    "max_results": 2,
                    "status_filter": ["active", "pending", "for_sale"],
                },
            ),
            Action(
                name="validate_drive_time_constraints",
                kwargs={
                    "property_list": ["HTX003", "HTX025", "HTX034"],
                    "max_hop_minutes": 25,
                },
            ),
            Action(
                name="calculate_route_optimization",
                kwargs={
                    "property_list": ["HTX003", "HTX025", "HTX034"],
                    "start_address": "201 Caroline St, Houston, TX",
                    "max_hop_minutes": 25,
                },
            ),
            Action(
                name="create_route_entry",
                kwargs={
                    "client_id": "4",
                    "route_date": "2025-09-20",
                    "stops_ordered_json": ["HTX003", "HTX025", "HTX034"],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "2",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 17
    Task(
        annotator="faris",
        user_id="faris_017_open_house_client11_broker6",
        instruction="You are broker 6, find 2 additional open houses using the date 2025-08-30 for client 11 at property HTX012. Schedule any you find as 'Montrose Open House Tour' in Montrose, Houston on 2025-08-31 and email a summary to the client.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX012"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX012",
                    "max_results": 2,
                    "status_filter": ["active", "for_sale"],
                },
            ),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": ["HTX012", "HTX038", "HTX017"],
                    "date": "2025-08-30",
                },
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "6",
                    "client_id": "11",
                    "title": "Montrose Open House Tour",
                    "date": "2025-08-31",
                    "location": "Montrose, Houston",
                    "source": "viewing",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "11",
                    "broker_id": "6",
                    "template_code": "open_house_summary",
                    "property_id": ["HTX012", "HTX038", "HTX017"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 18
    Task(
        annotator="faris",
        user_id="faris_018_campaign_update_broker1",
        instruction="You are broker 1, and you need to send a market intelligence briefing about property HTX015 to client 1 as part of the 'August 2025 Market Intelligence' campaign (ID 1).",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "1"}),
            Action(name="fetch_listings_by_ids", kwargs={"property_ids": ["HTX015"]}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "1", "created_by": "1"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "briefing",
                    "campaign_id": 1,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 19
    Task(
        annotator="faris",
        user_id="faris_019_client_followup_client3_broker3",
        instruction="You are broker 3. Fetch the client information for client 3, and their emails since 2025-08-01, and send a follow-up email about property HTX030 using the follow_up template.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(
                name="fetch_emails_for_client",
                kwargs={"client_id": "3", "date": "2025-08-01"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "3",
                    "broker_id": "3",
                    "template_code": "follow_up",
                    "property_id": "HTX030",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 20
    Task(
        annotator="faris",
        user_id="faris_020_mortgage_search_client6_broker6",
        instruction="You are broker 6. For client 6, create a comp report for property HTX030. Notify the client of the report.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "6"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "6",
                    "subject_property_id": "HTX030",
                    "max_selections": 1,
                    "created_by_broker_id": "6",
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "6"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "6",
                    "broker_id": "6",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 21
    Task(
        annotator="faris",
        user_id="faris_021_urgent_route_client9_broker9",
        instruction="You are broker 9, planning a 3-stop viewing route for client 9 on 2025-09-16, starting from the client's commute address, with the first stop being HTX029. Hops should be under 15 minutes. Do not verify that the route was created or create a calendar event.",
        actions=[
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX029",
                    "max_results": 2,
                    "status_filter": ["active", "pending", "for_sale"],
                },
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "9"}),
            Action(
                name="validate_drive_time_constraints",
                kwargs={
                    "property_list": ["HTX029", "HTX028", "HTX039"],
                    "max_hop_minutes": 15,
                },
            ),
            Action(
                name="calculate_route_optimization",
                kwargs={
                    "property_list": ["HTX029", "HTX028", "HTX039"],
                    "start_address": "201 Caroline St, Houston, TX",
                    "max_hop_minutes": 15,
                },
            ),
            Action(
                name="create_route_entry",
                kwargs={
                    "client_id": "9",
                    "route_date": "2025-09-16",
                    "stops_ordered_json": ["HTX029", "HTX028", "HTX039"],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "9",
                },
            ),

        ],
        outputs=[],
    ),
    # Task 22
    Task(
        annotator="faris",
        user_id="faris_022_new_campaign_broker10",
        instruction="You are broker 10. Create a new 'First-Time Buyer Education Series' likely_buyer campaign using HTX030 and HTX032, and prepare a briefing document for client 17 who is a good fit. Fetch their full context and send a first time buyer email to the client. Return the client's maximum price.",
        actions=[
            Action(
                name="create_campaign_entry",
                kwargs={
                    "campaign_name": "First-Time Buyer Education Series",
                    "campaign_type": "likely_buyer",
                    "created_by": "10",
                },
            ),
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX030", "HTX032"]},
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "17"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "17", "created_by": "10"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "17",
                    "broker_id": "10",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": ["HTX030", "HTX032"],
                },
            ),
        ],
        outputs=[{"MAX_PRICE":284669}],
    ),
    # Task 23
    Task(
        annotator="faris",
        user_id="faris_023_report_details_client4_broker2",
        instruction="You are broker 2. Fetch the details for comp report 1 and fetch client 4's full context, get details for the subject property, then generate a new briefing document and send a follow-up email. Return the client's mortgage id.",
        actions=[
            Action(name="fetch_comp_report_details", kwargs={"report_id": "1"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "4"}),
            Action(name="fetch_property_details", kwargs={"property_id": "HTX003"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "4", "created_by": "2"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "4",
                    "broker_id": "2",
                    "template_code": "follow_up",
                },
            ),
        ],
        outputs=[4],
    ),
    # Task 24
    Task(
        annotator="faris",
        user_id="faris_024_mortgage_check_client18_broker6",
        instruction="You are broker 6. Calculate client 18's potential mortgage payment on a 700000 loan, with a 10000 down payment at 3.99% with a 15 year term and email them the details using a general_update template. Add a calendar event titled 'Mortgage Check' for 2025-09-20 to discuss it with the location 'Phone Call' and source 'general_update'. Return the monthly payment.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "18"}),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 700000,
                    "down_payment": 10000,
                    "interest_rate": 3.99,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "6",
                    "client_id": "18",
                    "title": "Mortgage Check",
                    "date": "2025-09-20",
                    "location": "Phone Call",
                    "source": "general_update",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "18",
                    "broker_id": "6",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[{"MONTHLY_PAYMENT": 5174}],
    ),
    # Task 25
    Task(
        annotator="faris",
        user_id="faris_025_create_comp_report_with_metrics_client12_broker7",
        instruction="You are broker 7. Create a comparable analysis for client 12 on property HTX045, w/ up to 2 comparables, and generate the report document.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "12"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "12",
                    "created_by_broker_id": "7",
                    "subject_property_id": "HTX045",
                    "client_neighborhoods": ["11", "1", "13"],
                    "max_selections": 2,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX048",
                            "similarity_score": 0.923,
                            "selection_reason": "Strong price fit",
                        },
                        {
                            "comp_property_id": "HTX043",
                            "similarity_score": 0.897,
                            "selection_reason": "Strong price fit",
                        },
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "7"},
            ),
        ],
        outputs=[],
    ),
    # Task 26
    Task(
        annotator="faris",
        user_id="faris_026_comp_analysis_client9_htx024",
        instruction="You must prepare a comparable analysis for client 9 evaluating HTX024. You are broker 9.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "9"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "9",
                    "created_by_broker_id": "9",
                    "subject_property_id": "HTX024",
                    "client_neighborhoods": ["1", "12", "14", "3"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "9"},
            ),
        ],
        outputs=[],
    ),
    # Task 27
    Task(
        annotator="faris",
        user_id="faris_027_open_house_email_client5_broker6",
        instruction="You are broker 6. Find up to 4 additional open houses using the date 2025-08-30 for client 5 at property HTX025. Then, send an email summary of the houses.",
        actions=[
            Action(
                name="fetch_property_details",
                kwargs={"property_id": "HTX025"},
            ),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX025",
                    "max_results": 4,
                    "status_filter": ["active", "for_sale"],
                },
            ),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035",
                    ],
                    "date": "2025-08-30",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "5",
                    "broker_id": "6",
                    "template_code": "open_house_summary",
                    "property_id": ["HTX025", "HTX032", "HTX017", "HTX038", "HTX035"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 28
    Task(
        annotator="faris",
        user_id="faris_028_briefing_for_campaign_client_7_broker15",
        instruction="You are broker 15. First fetch the details for the 'Post-Closing Client Care' campaign (ID 4), then get client 7's full context. Use this information to generate a briefing document for client 7 and send them a post-closing check-in email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "4"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "7"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "7", "created_by": "15"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "7",
                    "broker_id": "15",
                    "template_code": "briefing",
                    "campaign_id": "4",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 29
    Task(
        annotator="faris",
        user_id="faris_029_review_client_comms_client_8_broker12",
        instruction="You are broker 12. Review all communications including calendar events and emails for client 8, generate a briefing document, and send a briefing email to schedule the next steps.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "8"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "8"}),
            Action(name="fetch_calendar_events_for_client", kwargs={"client_id": "8"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "8", "created_by": "12"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "8",
                    "broker_id": "12",
                    "template_code": "briefing",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 30
    Task(
        annotator="faris",
        user_id="faris_030_financial_check_client19_broker1",
        instruction="You are broker 1. Client 19 wants to know what they can afford. Fetch their mortgage profile, find the best rates, and email them a summary of their potential monthly payment.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "19"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": "702", "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 298612,
                    "down_payment": 26893,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "19",
                    "broker_id": "1",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 31
    Task(
        annotator="faris",
        user_id="faris_031_create_and_verify_route_client2_broker1",
        instruction="You are broker 1, planning a 3-stop viewing route for client 2 on 2025-09-25, starting from the client's commute address, with stops at HTX017, HTX026, and HTX040. Do not verify that the route was created or create a calendar event.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(
                name="validate_drive_time_constraints",
                kwargs={
                    "property_list": ["HTX017", "HTX026", "HTX040"],
                    "max_hop_minutes": 15,
                },
            ),
            Action(
                name="calculate_route_optimization",
                kwargs={
                    "property_list": ["HTX017", "HTX026", "HTX040"],
                    "start_address": "201 Caroline St, Houston, TX",
                    "max_hop_minutes": 15,
                },
            ),
            Action(
                name="create_route_entry",
                kwargs={
                    "client_id": "2",
                    "route_date": "2025-09-25",
                    "stops_ordered_json": ["HTX017", "HTX026", "HTX040"],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "1",
                },
            ),

        ],
        outputs=[],
    ),
    # Task 32
    Task(
        annotator="faris",
        user_id="faris_032_comp_report_for_client13_broker5",
        instruction="You are broker 5. Create a new comparable analysis for client 13 on property HTX025.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "13"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": ["7", "4", "5", "13"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "5"},
            ),
        ],
        outputs=[],
    ),
    # Task 34
    Task(
        annotator="faris",
        user_id="faris_034_neighborhood_and_comps_client15_broker8",
        instruction="You are broker 8. Your client 15 wants you to create a comp report for property HTX001 in neighborhood 4 w/ up to 3 comparables and email the client.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "15"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "15",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX001",
                    "client_neighborhoods": [4],
                    "max_selections": 3,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX007",
                            "similarity_score": 0.918,
                            "selection_reason": "Strong price fit",
                        },
                        {
                            "comp_property_id": "HTX050",
                            "similarity_score": 0.892,
                            "selection_reason": "Strong price fit",
                        },
                        {
                            "comp_property_id": "HTX019",
                            "similarity_score": 0.852,
                            "selection_reason": "Strong price fit",
                        },
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "8"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "15",
                    "broker_id": "8",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 35
    Task(
        annotator="faris",
        user_id="faris_035_create_mortgage_audit_client_17",
        instruction="You are broker 1. After creating a mortgage profile for client 17 with a loan amount of $548,318, and a down payment of $109,032, calculate their mortgage payment.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "17"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 699, "region": "TX"},
            ),
            Action(
                name="create_mortgage_profile",
                kwargs={
                    "client_id": "17",
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 699,
                    "region": "TX",
                    "annual_income": 78851,
                },
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 36
    Task(
        annotator="faris",
        user_id="faris_036_plan_route_with_inactive_broker_client5_broker1",
        instruction="You are broker 1 taking over for inactive broker 5, planning a viewing route for client 5 on 2025-09-23, starting from the client's commute address, visiting properties HTX030, HTX025, and HTX032. Do not verify that the route was created or create a calendar event.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "5"}),
            Action(
                name="validate_drive_time_constraints",
                kwargs={
                    "property_list": ["HTX030", "HTX025", "HTX032"],
                    "start_address": "1500 McKinney St, Houston, TX",
                    "max_hop_minutes": 30,
                },
            ),
            Action(
                name="calculate_route_optimization",
                kwargs={
                    "property_list": ["HTX030", "HTX025", "HTX032"],
                    "start_address": "1500 McKinney St, Houston, TX",
                    "max_hop_minutes": 30,
                },
            ),
            Action(
                name="create_route_entry",
                kwargs={
                    "client_id": "5",
                    "route_date": "2025-09-23",
                    "stops_ordered_json": ["HTX030", "HTX025", "HTX032"],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "1",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 37
    Task(
        annotator="faris",
        user_id="faris_037_generate_and_send_briefing_client_20_broker10",
        instruction="You are broker 10. For client 20, review their profile and communication history, generate a client briefing document, then email it to them using the briefing template.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "20"}),
            Action(name="fetch_calendar_events_for_client", kwargs={"client_id": "20"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "20", "created_by": "10"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "20",
                    "broker_id": "10",
                    "template_code": "briefing",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 38
    Task(
        annotator="faris",
        user_id="faris_038_find_investment_properties_client18_broker6",
        instruction="You are broker 6. Client 18 is an investor. Find up to 5 properties for them, and email them the list using campaign 8.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "18"}),
            Action(
                name="search_listings_by_criteria",
                kwargs={
                    "neighborhoods_json": [13, 9, 14, 15, 11],
                    "price_min": 273024,
                    "price_max": 868888,
                    "status_filter": ["active", "for_sale"],
                    "max_results": 5,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "18",
                    "broker_id": "6",
                    "template_code": "investment_alert",
                    "campaign_id": "8",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 39
    Task(
        annotator="faris",
        user_id="faris_039_sales_history_and_metrics_client3_broker3",
        instruction="You are broker 3. Client 3 needs a comprehensive property analysis for HTX021. Search for comparable properties and generate a complete analysis report with metrics calculation.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "3",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX021",
                    "client_neighborhoods": ["1", "12", "2", "4", "5"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX030",
                            "similarity_score": 0.868,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="calculate_property_metrics",
                kwargs={
                    "subject_property_id": "HTX021",
                    "comparable_properties": ["HTX030"],
                    "client_budget": {"client_id": "3", "price_max": 631914},
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "3"},
            ),
        ],
        outputs=[],
    ),
    # Task 40
    Task(
        annotator="faris",
        user_id="faris_040_send_client6_broker3",
        instruction="You are broker 3. Create a complete comparable analysis report for client 6 on property HTX044 including document generation and send the comp report delivery email.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "6"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "6",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX044",
                    "client_neighborhoods": [8, 12, 6, 5],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX027",
                            "similarity_score": 0.922,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "3"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "6",
                    "broker_id": "3",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 41
    Task(
        annotator="faris",
        user_id="faris_041_route_from_route_client_4_broker_2",
        instruction="You are broker 2. Fetch the latest route for client 4 and then create a new calendar event with location 'Phone Call' on 2025-09-21 titled 'Follow-up on Property Tour' to schedule a follow-up call about it and send an email to the client.",
        actions=[
            Action(name="fetch_route_details", kwargs={"client_id": "4"}),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "2",
                    "client_id": "4",
                    "title": "Follow-up on Property Tour",
                    "date": "2025-09-21",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "4",
                    "broker_id": "2",
                    "template_code": "follow_up",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 42
    Task(
        annotator="faris",
        user_id="faris_042_fetch_multiple_listings_and_email_client_10_broker11",
        instruction="You are broker 11. Fetch listings HTX021, HTX050, and HTX018 for client 10, check their preferences and recent (30 days) communication, then email them a listing summary.",
        actions=[
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX021", "HTX050", "HTX018"]},
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "10"}),
            Action(
                name="check_recent_email_history",
                kwargs={
                    "client_id": "10",
                    "template_code": "listing_summary",
                    "days_lookback": 30,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "10",
                    "broker_id": "11",
                    "template_code": "listing_summary",
                    "property_id": ["HTX021", "HTX050", "HTX018"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 43
    Task(
        annotator="faris",
        user_id="faris_043_update_report_status_and_notify_broker_report_2",
        instruction="You are broker 14. Update the status of comp report 2 to 'sent_to_broker'. After updating, fetch the report details, then create an audit event (report_status_update) for compliance tracking and send a report follow-up email to the client to notify them that the report has been sent.",
        actions=[
            Action(
                name="update_comp_report_status",
                kwargs={
                    "report_id": "2",
                    "new_status": "sent_to_broker",
                    "actor_id": "14",
                },
            ),
            Action(name="fetch_comp_report_details", kwargs={"report_id": "2"}),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "14",
                    "action": "report_status_update",
                    "entity_type": "comp_report",
                    "entity_id": "2",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "10",
                    "broker_id": "14",
                    "template_code": "report_followup",
                    "property_id": "HTX021",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 44
    Task(
        annotator="faris",
        user_id="faris_044_comp_report_inactive_broker_client_2_broker_1",
        instruction="You are broker 1. You must generate a comparable report for client 2 interested in HTX017, and check for the best mortgage rate.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": "716", "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 679753,
                    "down_payment": 49429,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "2",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX017",
                    "client_neighborhoods": ["11", "1"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX026",
                            "similarity_score": 0.879,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_045_generate_uri_and_update_report_3",
        instruction="You are broker 6. Generate the document for comp report ID 3, deliver it to the client via email using the comp_report_delivery template, then update the report status to 'sent_to_client'.",
        actions=[
            Action(name="fetch_comp_report_details", kwargs={"report_id": "3"}),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "3", "created_by": "6"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "11",
                    "broker_id": "6",
                    "template_code": "comp_report_delivery",
                },
            ),
            Action(
                name="update_comp_report_status",
                kwargs={
                    "report_id": "3",
                    "new_status": "sent_to_client",
                    "actor_id": "6",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 46
    Task(
        annotator="faris",
        user_id="faris_046_viewing_route_client20_broker2",
        instruction="You are broker 2, planning a 3-stop viewing route for client 20 on 2025-09-28, starting from the client's commute address, with the first stop being HTX042. Hops should be under 45 minutes. Do not verify that the route was created or create a calendar event.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX042",
                    "max_results": 2,
                    "status_filter": ["active", "pending", "for_sale"],
                },
            ),
            Action(
                name="validate_drive_time_constraints",
                kwargs={
                    "property_list": ["HTX042", "HTX002", "HTX018"],
                    "max_hop_minutes": 45,
                },
            ),
            Action(
                name="calculate_route_optimization",
                kwargs={
                    "property_list": ["HTX042", "HTX018", "HTX002"],
                    "start_address": "4 Riverway, Houston, TX",
                    "max_hop_minutes": 45,
                },
            ),
            Action(
                name="create_route_entry",
                kwargs={
                    "client_id": "20",
                    "route_date": "2025-09-28",
                    "stops_ordered_json": ["HTX042", "HTX018", "HTX002"],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "2",
                },
            ),

        ],
        outputs=[],
    ),
    # Task 47
    Task(
        annotator="faris",
        user_id="faris_047_open_house_search_client1_broker1",
        instruction="You are broker 1. Find up to 5 additional open houses (other than HTX001) for client 1 near property HTX001 for the weekend of 2025-08-25, and email a summary to the client.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX001"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX001",
                    "max_results": 5,
                    "status_filter": ["active", "for_sale"],
                },
            ),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": [
                        "HTX016",
                        "HTX023",
                        "HTX032",
                        "HTX017",
                        "HTX025",
                    ],
                    "date": "2025-08-25",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX016",
                        "HTX023",
                        "HTX032",
                        "HTX017",
                        "HTX025",
                    ],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 48
    Task(
        annotator="faris",
        user_id="faris_048_new_homeowner_campaign_client_3_broker3",
        instruction="You are broker 2. Find up to 4 additional open houses using the date 2025-08-30 for client 5 at property HTX025. Then, send an email summary of the houses.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX025"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX025",
                    "max_results": 4,
                    "status_filter": ["active", "for_sale"],
                },
            ),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035",
                    ],
                    "date": "2025-08-30",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "5",
                    "broker_id": "2",
                    "template_code": "open_house_summary",
                    "property_id": ["HTX025", "HTX032", "HTX017", "HTX038", "HTX035"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 49
    Task(
        annotator="faris",
        user_id="faris_049_review_calendar_client14_broker1",
        instruction="You are broker 1, taking over for broker 14. Review calendar events and email history for client 14, fetch their full context, generate a briefing document for your review, and then send a follow-up email to introduce yourself and schedule next steps.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "14"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "14"}),
            Action(name="fetch_calendar_events_for_client", kwargs={"client_id": "14"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "14", "created_by": "1"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "14",
                    "broker_id": "1",
                    "template_code": "briefing",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 50
    Task(
        annotator="faris",
        user_id="faris_050_mortgage_prequal_client1_broker1",
        instruction="You are broker 1. Client 1 needs a mortgage pre-qualification summary. Fetch their profile, find best rates for their credit score, calculate payment on a 750000 loan, and email the client.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": "647", "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 750000,
                    "down_payment": 41652,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 51
    Task(
        annotator="faris",
        user_id="faris_051_comp_analysis_client19_htx030_broker1",
        instruction="You are broker 1. Create a comparable analysis for client 19 interested in HTX030 with 1 comparable selection and document generation.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "19"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "19",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": ["10", "5"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    # Task 52
    Task(
        annotator="faris",
        user_id="faris_052_report_for_new_client_client11_broker6",
        instruction="You are broker 6. Create a comparable analysis for your new client 11 on property HTX012.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "11"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "11",
                    "created_by_broker_id": "6",
                    "subject_property_id": "HTX012",
                    "client_neighborhoods": ["7", "3", "11", "14"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.57,
                            "selection_reason": "Fair price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "6"},
            ),
        ],
        outputs=[],
    ),
    # Task 53
    Task(
        annotator="faris",
        user_id="faris_053_comp_analysis_email_client13_htx025",
        instruction="You must create a comp report for client 13 on HTX025 and email it to them.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "13"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": ["7", "4", "5", "13"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "5"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "13",
                    "broker_id": "5",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 54
    Task(
        annotator="faris",
        user_id="faris_054_neighborhood_comps_client_1_broker1",
        instruction="You are broker 1. Client 1 is interested in Downtown. Create a comp report for them on property HTX003 with 2 comparables and email it.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "Downtown"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "1",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX003",
                    "client_neighborhoods": [1],
                    "max_selections": 2,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX026",
                            "similarity_score": 0.908,
                            "selection_reason": "Strong price fit",
                        },
                        {
                            "comp_property_id": "HTX032",
                            "similarity_score": 0.905,
                            "selection_reason": "Strong price fit",
                        },
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "comp_report_delivery",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 55
    Task(
        annotator="faris",
        user_id="faris_055_audit_mortgage_creation_client20",
        instruction="You are broker 1. A mortgage profile was created for client 20. Verify their mortgage rates and calculate payment terms, create a mortgage audit entry for compliance, and send them a general update email with the mortgage details.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 785, "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "1",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "20",
                    "metadata_json": {"mortgage_profile_id": "20"},
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "20",
                    "broker_id": "1",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 56
    Task(
        annotator="faris",
        user_id="faris_056_route_planning_client10_broker11",
        instruction="You are broker 11, planning a 3-stop viewing route for client 10 on 2025-09-29, starting from the client's commute address, with the first stop being HTX021. Find the 2 nearest listings to HTX021 for the remaining stops. Hops should be under 30 minutes. Do not verify that the route was created or create a calendar event.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "10"}),
            Action(
                name="find_nearby_listings",
                kwargs={
                    "subject_property_id": "HTX021",
                    "max_results": 2,
                    "status_filter": ["active", "pending", "for_sale"],
                },
            ),
            Action(
                name="validate_drive_time_constraints",
                kwargs={
                    "property_list": ["HTX021", "HTX018", "HTX002"],
                    "max_hop_minutes": 30,
                },
            ),
            Action(
                name="calculate_route_optimization",
                kwargs={
                    "property_list": ["HTX021", "HTX018", "HTX002"],
                    "start_address": "1500 McKinney St, Houston, TX",
                    "max_hop_minutes": 30,
                },
            ),
            Action(
                name="create_route_entry",
                kwargs={
                    "client_id": "10",
                    "route_date": "2025-09-29",
                    "stops_ordered_json": ["HTX021", "HTX018", "HTX002"],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "11",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 57
    Task(
        annotator="faris",
        user_id="faris_057_briefing_and_email_client16_broker8",
        instruction="You are broker 8. Fetch the property details for HTX030, as well as the full context and email history for client 16. Generate a briefing document, schedule a follow-up Phone Call titled 'Discuss Briefing' for 2025-09-20 to discuss it, and then email the briefing to them using briefing template. Return the street view url for the property.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX030"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "16"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "16"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "16", "created_by": "8"},
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "8",
                    "client_id": "16",
                    "title": "Discuss Briefing",
                    "date": "2025-09-20",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "16",
                    "broker_id": "8",
                    "template_code": "briefing",
                },
            ),
        ],
        outputs=[{"STREET_VIEW_URL": "https://maps.google.com/?q=29.7377,-95.4017&layer=c"}],
    ),
    # Task 58
    Task(
        annotator="faris",
        user_id="faris_058_investor_search_client13_broker6",
        instruction="You are broker 6. Your investor client 13 is looking for a property. Search for 1 active listing in the neighborhoods 7, 4, 5, and 13 w/ price max 566116, create a calendar event titled 'Investor Search Follow-up' for 2025-09-23 with the location 'Phone Call' and source 'follow_up' and email them.",
        actions=[
            Action(
                name="search_listings_by_criteria",
                kwargs={
                    "neighborhoods_json": [7, 4, 5, 13],
                    "status_filter": "active",
                    "max_results": 1,
                    "price_max": 566116,
                },
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "6",
                    "client_id": "13",
                    "title": "Investor Search Follow-up",
                    "date": "2025-09-23",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "13",
                    "broker_id": "6",
                    "template_code": "investment_alert",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 59
    Task(
        annotator="faris",
        user_id="faris_059_sales_history_and_metrics_client_9_broker_9",
        instruction="You are broker 9. Create a comparable analysis for client 9 with HTX024 as the subject property.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "9"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "9",
                    "created_by_broker_id": "9",
                    "subject_property_id": "HTX024",
                    "client_neighborhoods": ["1", "12", "14", "3"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "9"},
            ),
        ],
        outputs=[],
    ),
    # Task 60
    Task(
        annotator="faris",
        user_id="faris_060_comp_analysis_metrics_client8_htx049",
        instruction="You must create a comp analysis for client 8 considering HTX049 with metrics.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "8"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "8",
                    "created_by_broker_id": "12",
                    "subject_property_id": "HTX049",
                    "client_neighborhoods": ["10", "2", "4"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX024",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="calculate_property_metrics",
                kwargs={
                    "subject_property_id": "HTX049",
                    "comparable_properties": ["HTX024"],
                    "client_budget": {"client_id": "8", "price_max": 434224},
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "12"},
            ),
        ],
        outputs=[],
    ),
    # Task 61
    Task(
        annotator="faris",
        user_id="faris_061_fetch_route_and_followup_client_10_broker11",
        instruction="You are broker 11. Fetch the client's full context and the latest route for client 10 and then create a calendar event to schedule a follow-up call about their tour on 2025-09-30 with the title 'Follow-up on Home Tour' with location 'Phone Call'. Return the listing price of each property in the route. Send an email to the client to confirm the follow-up.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "10"}),
            Action(name="fetch_route_details", kwargs={"client_id": "10"}),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "11",
                    "client_id": "10",
                    "title": "Follow-up on Home Tour",
                    "date": "2025-09-30",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(name="fetch_property_details", kwargs={"property_id": "HTX021"}),
            Action(name="fetch_property_details", kwargs={"property_id": "HTX050"}),
            Action(name="fetch_property_details", kwargs={"property_id": "HTX018"}),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "10",
                    "broker_id": "11",
                    "template_code": "follow_up",
                },
            ),
        ],
        outputs=[{"HTX021": 874000, "HTX050": 1549000, "HTX018": 4300000}],
    ),
    # Task 62
    Task(
        annotator="faris",
        user_id="faris_062_fetch_multiple_listings_client_1_broker1",
        instruction="You are broker 1. Fetch listings HTX001, HTX007, and HTX011 for client 1, review their profile and open house interests for the weekend of 2025-08-25, schedule a follow-up call w/location: Phone Call, titled 'Follow-up on River Oaks Listings' for 2025-09-23, and then email them a summary of these River Oaks properties.",
        actions=[
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX001", "HTX007", "HTX011"]},
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="fetch_open_house_opportunities",
                kwargs={
                    "property_candidates": ["HTX001", "HTX007", "HTX011"],
                    "date": "2025-08-25",
                },
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "1",
                    "client_id": "1",
                    "title": "Follow-up on River Oaks Listings",
                    "date": "2025-09-23",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "listing_summary",
                    "property_id": ["HTX001", "HTX007", "HTX011"],
                },
            ),
        ],
        outputs=[],
    ),
    # Task 63
    Task(
        annotator="faris",
        user_id="faris_063_update_report_status_report_7_broker1",
        instruction="You are broker 1. Fetch client 7's full context, update the status of comp report 7 to 'sent_to_client' and generate a briefing document for them.",
        actions=[
            Action(name="fetch_comp_report_details", kwargs={"report_id": "7"}),
            Action(
                name="update_comp_report_status",
                kwargs={
                    "report_id": "7",
                    "new_status": "sent_to_client",
                    "actor_id": "1",
                },
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "7"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "7", "created_by": "1"},
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "1",
                    "action": "created",
                    "entity_type": "briefing_document",
                    "entity_id": "21",
                    "metadata_json": {"briefing_document_id": "21"},
                },
            ),
        ],
        outputs=[],
    ),
    # Task 64
    Task(
        annotator="faris",
        user_id="faris_064_comp_report_inactive_broker_client_5_broker_1",
        instruction="You are broker 1, taking over for inactive broker 5. Check the property HTX030's sales history and create a comparable report for client 5 interested in HTX030 using 1 comparable selection.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "5"}),
            Action(name="fetch_property_sales_history", kwargs={"property_id": "HTX030"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "5",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": [6, 2, 4, 10],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    # Task 65
    Task(
        annotator="faris",
        user_id="faris_065_generate_uri_and_update_report_8_complex",
        instruction="You are broker 12. For comp report 8, you must generate the report document and update its status to 'sent_to_client'. Additionally, create a new 'general_update' campaign named 'Report 8 Follow-up Campaign' and send a 'report_followup' email to the client.",
        actions=[
            Action(name="fetch_comp_report_details", kwargs={"report_id": "8"}),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "8", "created_by": "12"},
            ),
            Action(
                name="update_comp_report_status",
                kwargs={
                    "report_id": "8",
                    "new_status": "sent_to_client",
                    "actor_id": 12,
                },
            ),
            Action(
                name="create_campaign_entry",
                kwargs={
                    "campaign_name": "Report 8 Follow-up Campaign",
                    "campaign_type": "general_update",
                    "created_by": "12",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "8",
                    "broker_id": "12",
                    "template_code": "report_followup",
                    "campaign_id": "9",
                    "property_id": "HTX049",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_066_briefing_for_campaign_client_1_broker1",
        instruction="You are broker 1. First fetch the details for the 'August 2025 Market Intelligence' campaign (ID 1), then get client 1's full context. Use this information to generate a briefing document for client 1 and send them a post-closing check-in email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "1"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "1", "created_by": "1"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "post_closing_checkin",
                    "campaign_id": "1",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_067_briefing_for_campaign_client_2_broker2",
        instruction="You are broker 2. First fetch the details for the 'New Client Onboarding Q3 2025' campaign (ID 2), then get client 2's full context. Use this information to generate a briefing document for client 2 and send them a post-closing check-in email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "2"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "2", "created_by": "2"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "2",
                    "broker_id": "2",
                    "template_code": "post_closing_checkin",
                    "campaign_id": "2",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_068_briefing_for_campaign_client_3_broker3",
        instruction="You are broker 3. First fetch the details for the 'Weekend Open House Circuit' campaign (ID 3), then get client 3's full context. Use this information to generate a briefing document for client 3 and send them a post-closing check-in email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "3"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "3", "created_by": "3"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "3",
                    "broker_id": "3",
                    "template_code": "post_closing_checkin",
                    "campaign_id": "3",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_069_montrose_comp_client12_htx013",
        instruction="You must generate a comparable analysis for client 12 evaluating HTX014",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "12"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "12",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX014",
                    "client_neighborhoods": ["11", "1", "13"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.914,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "3"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_070_montrose_comp_client14_htx015",
        instruction="You are broker 1. You must generate a comparable analysis for client 14 evaluating HTX019",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "14"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "14",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX019",
                    "client_neighborhoods": ["2", "9", "7", "14"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX007",
                            "similarity_score": 0.853,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_071_montrose_comp_client1_htx002",
        instruction="You must generate a comparable analysis for client 1 evaluating HTX002",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "1",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX002",
                    "client_neighborhoods": ["5", "9", "8", "10", "14"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX047",
                            "similarity_score": 0.85,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_072_luxury_comp_client14_htx026_amenities",
        instruction="You must create a comp report for client 14 on HTX026",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "14"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "14",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX026",
                    "client_neighborhoods": ["2", "9", "7", "14"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX003",
                            "similarity_score": 0.908,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_073_luxury_comp_client15_htx027_amenities",
        instruction="You must create a comp report for client 15 on HTX027",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "15"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "15",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX027",
                    "client_neighborhoods": ["5", "12", "1", "7"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX044",
                            "similarity_score": 0.922,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "8"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_074_luxury_comp_client16_htx028_amenities",
        instruction="You must create a comp report for client 16 on HTX028",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "16"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "16",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX028",
                    "client_neighborhoods": ["7", "11", "6", "13", "15"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX035",
                            "similarity_score": 0.9,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "8"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_075_audit_mortgage_creation_client1",
        instruction="You are broker 2. A mortgage profile was created for client 1. Verify their mortgage rates and calculate payment terms, create a mortgage audit entry for compliance, and send them a general update email with the mortgage details.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 647, "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 747819,
                    "down_payment": 41652,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "2",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "1",
                    "metadata_json": {"mortgage_profile_id": "1"},
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "2",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_076_audit_mortgage_creation_client2",
        instruction="You are broker 3. A mortgage profile was created for client 2. Verify their mortgage rates and calculate payment terms, create a mortgage audit entry for compliance, and send them a general update email with the mortgage details.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 716, "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 679753,
                    "down_payment": 49429,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "3",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "2",
                    "metadata_json": {"mortgage_profile_id": "2"},
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "2",
                    "broker_id": "3",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_077_audit_mortgage_creation_client3",
        instruction="You are broker 4. A mortgage profile was created for client 3. Verify their mortgage rates and calculate payment terms, create a mortgage audit entry for compliance, and send them a general update email with the mortgage details.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 698, "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 224492,
                    "down_payment": 72869,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "4",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "3",
                    "metadata_json": {"mortgage_profile_id": "3"},
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "3",
                    "broker_id": "4",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_078_new_homeowner_campaign_client_4_broker4",
        instruction="You are broker 4. For client 4, you are preparing for the 'Post-Closing Client Care' campaign (ID 4). You must fetch the campaign details, the client's context and email history, generate a briefing doc, schedule a Phone Call titled 'Post-Closing Call' for 2025-09-21, and then send them a briefing email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "4"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "4"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "4"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "4", "created_by": "4"},
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "4",
                    "client_id": "4",
                    "title": "Post-Closing Call",
                    "date": "2025-09-21",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "4",
                    "broker_id": "4",
                    "template_code": "briefing",
                    "campaign_id": "4",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_079_new_homeowner_campaign_client_5_broker5",
        instruction="You are broker 5. For client 5, you are preparing for the 'Fall Market Preparation' campaign (ID 5). You must fetch the campaign details, fetch listings for HTX017 and HTX028, get the client's context and email history, generate a briefing doc, schedule a Phone Call titled 'Fall Market Preparation Call' for 2025-09-22 with source 'follow_up', and then send them a briefing email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "5"}),
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX017", "HTX028"]},
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "5"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "5"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "5", "created_by": "5"},
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "5",
                    "client_id": "5",
                    "title": "Fall Market Preparation Call",
                    "date": "2025-09-22",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "5",
                    "broker_id": "5",
                    "template_code": "briefing",
                    "campaign_id": "5",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_080_new_homeowner_campaign_client_6_broker6",
        instruction="You are broker 6. For client 6, you are preparing for the 'First-Time Buyer Education Series' campaign (ID 6). You must fetch the campaign details, the client's context and email history, generate a briefing doc, schedule a welcome Phone Call titled 'First-Time Buyer Education Call' for 2025-09-23, and then send them a First-Time Buyer Education email.",
        actions=[
            Action(name="fetch_campaign_details", kwargs={"campaign_id": "6"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "6"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "6"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "6", "created_by": "6"},
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "6",
                    "client_id": "6",
                    "title": "First-Time Buyer Education Call",
                    "date": "2025-09-23",
                    "location": "Phone Call",
                    "source": "first_time_buyer",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "6",
                    "broker_id": "6",
                    "template_code": "first_time_buyer",
                    "campaign_id": "6",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_081_create_mortgage_audit_client_18",
        instruction="You are broker 2. Fetch the best rate for client 18 using their credit score and region, and using the best rate, create a new mortgage profile for client 18 with a loan amount of $685,266, and a down payment of $70,069, calculate their mortgage payment using the best_rate at 15 years.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "18"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 637, "region": "TX"},
            ),
            Action(
                name="create_mortgage_profile",
                kwargs={
                    "client_id": "18",
                    "loan_amount": 685266,
                    "down_payment": 70069,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 637,
                    "region": "TX",
                    "annual_income": 63042,
                },
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 685266,
                    "down_payment": 70069,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_082_create_mortgage_audit_client_19",
        instruction="You are broker 3. After creating a mortgage profile for client 19 with a loan amount of $298,612, and a down payment of $26,893, calculate their mortgage payment.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "19"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 702, "region": "TX"},
            ),
            Action(
                name="create_mortgage_profile",
                kwargs={
                    "client_id": "19",
                    "loan_amount": 298612,
                    "down_payment": 26893,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 702,
                    "region": "TX",
                    "annual_income": 114919,
                },
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 298612,
                    "down_payment": 26893,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_083_create_mortgage_audit_client_20",
        instruction="You are broker 4. After creating a mortgage profile for client 20 with a loan amount of $727,066, and a down payment of $86,396, calculate their mortgage payment. Don't send an email to the client.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 785, "region": "TX"},
            ),
            Action(
                name="create_mortgage_profile",
                kwargs={
                    "client_id": "20",
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 785,
                    "region": "TX",
                    "annual_income": 142452,
                },
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_084_midtown_analysis_client1_htx002",
        instruction="You must prepare a comp analysis for client 1 evaluating HTX002 in Midtown neighborhood",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "Midtown"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "1",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX002",
                    "client_neighborhoods": ["2"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX047",
                            "similarity_score": 0.85,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_085_downtown_analysis_client2_htx003",
        instruction="You must prepare a comp analysis for client 2 evaluating HTX003 in Downtown neighborhood.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "Downtown"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "2",
                    "created_by_broker_id": "14",
                    "subject_property_id": "HTX003",
                    "client_neighborhoods": ["1"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX026",
                            "similarity_score": 0.908,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "14"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_086_montrose_analysis_client3_htx004",
        instruction="You must prepare a comp analysis for client 3 evaluating HTX004 in Montrose neighborhood",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "Montrose"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "3",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX004",
                    "client_neighborhoods": ["3"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX005",
                            "similarity_score": 0.881,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_087_galleria_analysis_client4_htx008",
        instruction="You are broker 4. You must create a comparable analysis for client 4 considering HTX008 in Galleria/Uptown",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "4"}),
            Action(
                name="fetch_neighborhood_details", kwargs={"name": "Galleria/Uptown"}
            ),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "4",
                    "created_by_broker_id": "4",
                    "subject_property_id": "HTX008",
                    "client_neighborhoods": ["8"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX035",
                            "similarity_score": 0.916,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "4"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_088_eado_analysis_client5_htx009",
        instruction="You must create a comparable analysis for client 5 considering HTX009 in EaDo",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "5"}),
            Action(name="fetch_neighborhood_details", kwargs={"name": "EaDo"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "5",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX009",
                    "client_neighborhoods": ["9"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.57,
                            "selection_reason": "Fair price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_089_oak_forest_analysis_client6_htx010",
        instruction="You must create a comparable analysis for client 6 considering HTX010 in Oak Forest/Garden Oaks",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "6"}),
            Action(
                name="fetch_neighborhood_details",
                kwargs={"name": "Oak Forest/Garden Oaks"},
            ),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "6",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX010",
                    "client_neighborhoods": ["10"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX024",
                            "similarity_score": 0.889,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_090_new_campaign_broker11",
        instruction="You are broker 11. Create a new 'Luxury Market Updates' general_update campaign using HTX033 and HTX034, and prepare a briefing document for client 18 who is a good fit. Fetch their full context and send a first time buyer email to the client. Return the client's maximum price.",
        actions=[
            Action(
                name="create_campaign_entry",
                kwargs={
                    "campaign_name": "Luxury Market Updates",
                    "campaign_type": "general_update",
                    "created_by": "11",
                },
            ),
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX033", "HTX034"]},
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "18"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "18", "created_by": "11"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "18",
                    "broker_id": "11",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": ["HTX033", "HTX034"],
                },
            ),
        ],
        outputs=[{"MAX_PRICE": 868888}],
    ),
    Task(
        annotator="faris",
        user_id="faris_091_new_campaign_broker12",
        instruction="You are broker 12. Create a new 'Investment Property Alerts' likely_buyer campaign using HTX035 and HTX036, and prepare a briefing document for client 19 who is a good fit. Send a first time buyer email to the client. Fetch their full context at the end and return the client's MAX_PRICE.",
        actions=[
            Action(
                name="create_campaign_entry",
                kwargs={
                    "campaign_name": "Investment Property Alerts",
                    "campaign_type": "likely_buyer",
                    "created_by": "12",
                },
            ),
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX035", "HTX036"]},
            ),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "19", "created_by": "12"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "19",
                    "broker_id": "12",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": ["HTX035", "HTX036"],
                },
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "19"}),
        ],
        outputs=[{"MAX_PRICE": 617543}],
    ),
    Task(
        annotator="faris",
        user_id="faris_092_new_campaign_broker13",
        instruction="You are broker 13. Create a new 'August 2025 Market Intelligence' general_update campaign using HTX037 and HTX038, and prepare a briefing document for client 20 who is a good fit. Fetch their full context and send a first time buyer email to the client. Return the client's maximum price.",
        actions=[
            Action(
                name="create_campaign_entry",
                kwargs={
                    "campaign_name": "August 2025 Market Intelligence",
                    "campaign_type": "general_update",
                    "created_by": "13",
                },
            ),
            Action(
                name="fetch_listings_by_ids",
                kwargs={"property_ids": ["HTX037", "HTX038"]},
            ),
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "20", "created_by": "13"},
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "20",
                    "broker_id": "13",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": ["HTX037", "HTX038"],
                },
            ),
        ],
        outputs=[{"MAX_PRICE": 529693}],
    ),
    Task(
        annotator="faris",
        user_id="faris_093_find_investment_properties_client1_broker1",
        instruction="You are broker 1. Client 1 is an investor. Find up to 5 properties for them, and email them the list using campaign 1.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="search_listings_by_criteria",
                kwargs={
                    "neighborhoods_json": [5, 9, 8, 10, 14],
                    "price_min": 244685,
                    "price_max": 761571,
                    "status_filter": ["active", "for_sale"],
                    "max_results": 5,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "investment_alert",
                    "campaign_id": "1",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_094_find_investment_properties_client2_broker2",
        instruction="You are broker 2. Client 2 is an investor. Find up to 5 properties for them, and email them the list using campaign 2.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(
                name="search_listings_by_criteria",
                kwargs={
                    "neighborhoods_json": [11, 1],
                    "price_min": 158527,
                    "price_max": 603380,
                    "status_filter": ["active", "for_sale"],
                    "max_results": 5,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "2",
                    "broker_id": "2",
                    "template_code": "investment_alert",
                    "campaign_id": "2",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_095_find_investment_properties_client3_broker3",
        instruction="You are broker 3. Client 3 is an investor. Find up to 5 properties for them, and email them the list using campaign 3",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "3"}),
            Action(
                name="search_listings_by_criteria",
                kwargs={
                    "neighborhoods_json": [1, 12, 2, 4, 5],
                    "price_min": 200505,
                    "price_max": 631914,
                    "status_filter": ["active", "for_sale"],
                    "max_results": 5,
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "3",
                    "broker_id": "3",
                    "template_code": "investment_alert",
                    "campaign_id": "3",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_096_comp_analysis_client20_htx031_broker2",
        instruction="You are broker 2. Create a comparable analysis for client 20 interested in HTX031 with 1 comparable selection and document generation.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "20"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "20",
                    "created_by_broker_id": "2",
                    "subject_property_id": "HTX031",
                    "client_neighborhoods": ["12", "9", "1"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX028",
                            "similarity_score": 0.872,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "2"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_097_comp_analysis_client1_htx033_broker3",
        instruction="You are broker 3. Create a comparable analysis for client 1 interested in HTX033 with 1 comparable selection and document generation.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "1",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX033",
                    "client_neighborhoods": ["5", "9", "8", "10", "14"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX005",
                            "similarity_score": 0.856,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "3"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_098_comp_analysis_client2_htx035_broker4",
        instruction="You are broker 4. Create a comparable analysis for client 2 interested in HTX035 with 1 comparable selection and document generation.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "2"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "2",
                    "created_by_broker_id": "4",
                    "subject_property_id": "HTX035",
                    "client_neighborhoods": ["11", "1"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX008",
                            "similarity_score": 0.916,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "4"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_099_comp_analysis_client19_htx030_broker1",
        instruction="You are broker 1. You must prepare a comparable analysis for client 19, who is considering property HTX030.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "19"}),
            Action(
                name="search_comps_and_create_report",
                kwargs={
                    "client_id": "19",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": ["10", "5"],
                    "max_selections": 1,
                },
            ),
            Action(
                name="bulk_create_comparable_entries",
                kwargs={
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit",
                        }
                    ],
                },
            ),
            Action(
                name="generate_attach_comp_report_document",
                kwargs={"report_id": "9", "created_by": "1"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_100_client_briefing_client16_broker8",
        instruction="You are broker 8. Prepare a comprehensive briefing for client 16. Fetch property details for HTX030, get the client's full context and email history, generate a briefing document, schedule a follow-up call titled 'Discuss Briefing' for 2025-09-20 w/location 'Phone Call' and source 'follow_up', and send them a briefing email.",
        actions=[
            Action(name="fetch_property_details", kwargs={"property_id": "HTX030"}),
            Action(name="fetch_client_full_context", kwargs={"client_id": "16"}),
            Action(name="fetch_emails_for_client", kwargs={"client_id": "16"}),
            Action(
                name="generate_client_briefing_document",
                kwargs={"client_id": "16", "created_by": "8"},
            ),
            Action(
                name="create_calendar_event_entry",
                kwargs={
                    "broker_id": "8",
                    "client_id": "16",
                    "title": "Discuss Briefing",
                    "date": "2025-09-20",
                    "location": "Phone Call",
                    "source": "follow_up",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "16",
                    "broker_id": "8",
                    "template_code": "briefing",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_101_audit_mortgage_creation_client1",
        instruction="You are broker 2. A mortgage profile was created for client 1. Verify their mortgage rates and calculate payment terms, create a mortgage audit entry for compliance, and send them a general update email with the mortgage details.",
        actions=[
            Action(name="fetch_client_full_context", kwargs={"client_id": "1"}),
            Action(
                name="fetch_mortgage_rates_for_client",
                kwargs={"credit_score": 647, "region": "TX"},
            ),
            Action(
                name="calculate_mortgage_payment",
                kwargs={
                    "loan_amount": 747819,
                    "down_payment": 41652,
                    "interest_rate": 4.004,
                    "term_years": 15,
                },
            ),
            Action(
                name="create_audit_event_entry",
                kwargs={
                    "actor_id": "2",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "1",
                    "metadata_json": {"mortgage_profile_id": "1"},
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "client_id": "1",
                    "broker_id": "2",
                    "template_code": "general_update",
                },
            ),
        ],
        outputs=[],
    ),
]
