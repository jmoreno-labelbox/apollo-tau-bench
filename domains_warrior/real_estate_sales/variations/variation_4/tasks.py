from domains.dto import Task, Action

TASKS = [
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_001",
    instruction=(
        "You need to execute client onboarding protocol for client 1 regarding property HTX001 (listing 1) at 1500000 with 5.847% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-20T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 1}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 5.847, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 1, "property_id": "HTX001", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 1, "broker_id": 1, "title": "Client onboarding session", "start_at": "2025-09-20T09:00:00Z", "end_at": "2025-09-20T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1684647.00"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_002",
    instruction=(
        "You need to execute client onboarding protocol for client 2 regarding property HTX002 (listing 2) at 3975000 with 6.395% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-21T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 2}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
        Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.395, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX002", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Client onboarding session", "start_at": "2025-09-21T09:00:00Z", "end_at": "2025-09-21T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["4971305.22"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_003",
    instruction=(
        "You need to execute client onboarding protocol for client 3 regarding property HTX003 (listing 3) at 591000 with 5.915% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-22T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 3}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
        Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 5.915, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX003", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 3, "broker_id": 1, "title": "Client onboarding session", "start_at": "2025-09-22T09:00:00Z", "end_at": "2025-09-22T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["673000.07"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_004",
    instruction=(
        "You need to execute client onboarding protocol for client 4 regarding property HTX004 (listing 4) at 705900 with 5.847% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-23T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 4}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
        Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 5.847, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 1, "property_id": "HTX004", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 4, "broker_id": 1, "title": "Client onboarding session", "start_at": "2025-09-23T09:00:00Z", "end_at": "2025-09-23T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["792794.88"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_005",
    instruction=(
        "You need to execute client onboarding protocol for client 5 regarding property HTX005 (listing 5) at 674900 with 6.395% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-24T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 5}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
        Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.395, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1, "property_id": "HTX005", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 5, "broker_id": 1, "title": "Client onboarding session", "start_at": "2025-09-24T09:00:00Z", "end_at": "2025-09-24T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["844058.84"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_006",
    instruction=(
        "You need to execute client onboarding protocol for client 6 regarding property HTX006 (listing 6) at 225700 with 5.915% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-25T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 6}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
        Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 5.915, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2, "property_id": "HTX006", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 6, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-25T09:00:00Z", "end_at": "2025-09-25T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["257015.43"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_007",
    instruction=(
        "You need to execute client onboarding protocol for client 7 regarding property HTX007 (listing 7) at 1490000 with 5.847% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-26T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 7}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 7}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX007"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1490000, "interest_rate": 5.847, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX007", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-26T09:00:00Z", "end_at": "2025-09-26T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1673416.02"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_008",
    instruction=(
        "You need to execute client onboarding protocol for client 8 regarding property HTX008 (listing 8) at 330000 with 6.395% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-27T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 8}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX008"}),
        Action(name="calculate_mortgage", kwargs={"principal": 330000, "interest_rate": 6.395, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX008", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-27T09:00:00Z", "end_at": "2025-09-27T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["412712.13"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_009",
    instruction=(
        "You need to execute client onboarding protocol for client 9 regarding property HTX011 (listing 11) at 495000 with 5.915% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-28T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 9}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 11}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX011"}),
        Action(name="calculate_mortgage", kwargs={"principal": 495000, "interest_rate": 5.915, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2, "property_id": "HTX011", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 9, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-28T09:00:00Z", "end_at": "2025-09-28T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["563680.26"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_010",
    instruction=(
        "You need to execute client onboarding protocol for client 10 regarding property HTX010 (listing 10) at 458500 with 5.847% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-29T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 10}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX010"}),
        Action(name="calculate_mortgage", kwargs={"principal": 458500, "interest_rate": 5.847, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2, "property_id": "HTX010", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 10, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-29T09:00:00Z", "end_at": "2025-09-29T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["514940.43"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_011",
    instruction=(
        "You need to execute client onboarding protocol for client 11 regarding property HTX011 (listing 11) at 899000 "
        "with 5.8% 30-year financing. Complete comprehensive client onboarding and schedule onboarding meeting on "
        "2025-09-21T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 11}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 11}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX011"}),
        Action(name="calculate_mortgage", kwargs={"principal": 899000, "interest_rate": 5.8, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX011", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 11, "broker_id": 3, "title": "Client onboarding session", "start_at": "2025-09-21T09:00:00Z", "end_at": "2025-09-21T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["999967.53"],
),
 Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_012",
        instruction=(
            "You need to execute property evaluation protocol for client 14 regarding property HTX002 (listing 2) at 3975000 with 6.8% 30-year financing. "
            "Deliver comprehensive property assessment with market valuation analysis. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 14}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX002", "doc_type": "evaluation_report"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Comprehensive Market Overview", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["5354049.44"]
    ),
Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_013",
    instruction=(
        "You need to onboard client 13 who is interested in property HTX013 (listing 13) priced at 591000 with a 6.8% 30-year mortgage. "
        "Prepare all onboarding materials and schedule a meeting on 2025-09-23T09:00:00Z–10:00:00Z at Office with notes 'Client onboarding session'. "
        "Make sure to report the total interest paid."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 13}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 13}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX013"}),
        Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.8, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 13, "broker_id": 3, "property_id": "HTX013", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 13, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 13,"broker_id": 3,"title": "Client onboarding session","start_at": "2025-09-23T09:00:00Z","end_at": "2025-09-23T10:00:00Z","location": "Office","notes": "Client onboarding session"})
    ],
    outputs=["796036.03"],
),
Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_014",
    instruction=(
        "You are to execute onboarding for client 14 purchasing HTX014 (listing 14) for 875000 with 6.2% 30-year loan. "
        "Setup a calendar event for 2025-09-24T09:00:00Z and report interest paid."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 14}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 14}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX014"}),
        Action(name="calculate_mortgage", kwargs={"principal": 875000, "interest_rate": 6.2, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX014", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 14, "broker_id": 3, "title": "Client onboarding session", "start_at": "2025-09-24T09:00:00Z", "end_at": "2025-09-24T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1054277.28"],
),
Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_015",
    instruction=(
        "Please onboard client 15 for HTX015 (listing 15) priced at 1380000 with 6.1% rate over 30 years. "
        "Prepare all onboarding material and arrange session at Office on 2025-09-25T09:00:00Z. Return total interest."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 15}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 15}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX015"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1380000, "interest_rate": 6.1, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 3, "property_id": "HTX015", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 15, "broker_id": 3, "title": "Client onboarding session", "start_at": "2025-09-25T09:00:00Z", "end_at": "2025-09-25T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1630582.09"],
),
Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_016",
    instruction=(
        "You need to execute client onboarding protocol for client 16 regarding property HTX009 (listing 9) at 1130000 with 6.1% 30-year financing. "
        "Schedule onboarding consultation on 2025-10-04T09:00:00Z–10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 16}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 9}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX009"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1130000, "interest_rate": 6.1, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 4, "property_id": "HTX009", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 16, "broker_id": 4, "title": "Client onboarding session", "start_at": "2025-10-04T09:00:00Z", "end_at": "2025-10-04T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1335186.79"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_017",
    instruction=(
        "You need to execute client onboarding protocol for client 17 regarding property HTX010 (listing 10) at 1580000 with 6.3% 30-year financing. "
        "Schedule onboarding consultation on 2025-10-05T09:00:00Z–10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 17}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX010"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1580000, "interest_rate": 6.3, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4, "property_id": "HTX010", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 17, "broker_id": 4, "title": "Client onboarding session", "start_at": "2025-10-05T09:00:00Z", "end_at": "2025-10-05T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1940717.23"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_018",
    instruction=(
        "You need to execute client onboarding protocol for client 18 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
        "Schedule onboarding consultation on 2025-10-06T09:00:00Z–10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 18}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 4, "property_id": "HTX001", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 18, "broker_id": 4, "title": "Client onboarding session", "start_at": "2025-10-06T09:00:00Z", "end_at": "2025-10-06T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1913167.33"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_019",
    instruction=(
        "You need to execute client onboarding protocol for client 19 regarding property HTX002 (listing 2) at 875000 with 6.4% 30-year financing. "
        "Schedule onboarding consultation on 2025-10-07T09:00:00Z–10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 19}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
        Action(name="calculate_mortgage", kwargs={"principal": 875000, "interest_rate": 6.4, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX002", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "Client onboarding session", "start_at": "2025-10-07T09:00:00Z", "end_at": "2025-10-07T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1095343.61"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_020",
    instruction=(
        "You need to execute client onboarding protocol for client 20 regarding property HTX003 (listing 3) at 591000 with 6.8% 30-year financing. "
        "Schedule onboarding consultation on 2025-10-08T09:00:00Z–10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 20}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
        Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.8, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 4, "property_id": "HTX003", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 20, "broker_id": 4, "title": "Client onboarding session", "start_at": "2025-10-08T09:00:00Z", "end_at": "2025-10-08T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["796036.03"]
),
 Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_021",
        instruction=(
            "You need to execute market intelligence protocol for client 11 regarding property HTX009 (listing 9) at 400000 with 7.3% 30-year financing. "
            "Deliver quarterly market intelligence and schedule intelligence meeting on 2025-10-30T16:00:00Z-17:00:00Z at Office with 'Market intelligence briefing' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 11}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 9}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX009"}),
            Action(name="calculate_mortgage", kwargs={"principal": 400000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_intelligence", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX009", "doc_type": "market_report"}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Comprehensive Market Intelligence", "template_code": "market_intelligence", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 11, "broker_id": 3, "title": "Market intelligence briefing", "start_at": "2025-10-30T16:00:00Z", "end_at": "2025-10-30T17:00:00Z", "location": "Office", "notes": "Market intelligence briefing"})
        ],
        outputs=["987222.14"]
    ),

Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_022",
    instruction=(
        "You should help client 5 understand their financing options for property HTX005 (listing 5). "
        "Use the listing’s current price as the principal for a 30-year mortgage at 6.5% interest, "
        "and summarize the mortgage interest for review. Include relevant property comparisons and prepare a purchase support package."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 5}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
        Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1, "property_id": "HTX005", "doc_type": "purchase_support"}),
        Action(name="send_email", kwargs={
            "client_id": 5,
            "broker_id": 1,
            "subject": "Comprehensive Purchase Analysis",
            "template_code": "purchase_support",
            "campaign_id": 101
        }),
    ],
    outputs=["860797.75"],
),

Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_023",
    instruction=(
        "You need to execute the PurchaseSupportProtocol for client 3 on property HTX013 (listing 13) using a $965,000 price. "
        "Include comparables, calculate total interest for a 6.1% 30-year mortgage, create campaign and briefing doc, "
        "send the purchase support email, and schedule a consultation at 2025‑09‑28T09:00:00Z–10:00:00Z at Office. "
        "Report the total interest."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 3}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 13}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX013"}),
        Action(name="calculate_mortgage", kwargs={"principal": 965000, "interest_rate": 6.1, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX013", "doc_type": "purchase_support"}),
        Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Comprehensive Purchase Analysis", "template_code": "purchase_support", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={
            "client_id": 3,
            "broker_id": 1,
            "title": "Purchase consultation",
            "start_at": "2025-09-28T09:00:00Z",
            "end_at": "2025-09-28T10:00:00Z",
            "location": "Office",
            "notes": "Purchase consultation"
        }),
    ],
    outputs=["1140225.88"],
),

Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_024",
    instruction=(
        "You need to execute the PurchaseSupportProtocol for client 4 on property HTX004 (listing 4) listed at $705,900. "
        "Include comparables, calculate total interest at a 6.3% 30-year mortgage, create campaign and briefing doc, "
        "send the purchase support email, and schedule a consult at 2025‑09‑29T09:00:00Z–10:00:00Z at Office. "
        "Report the total interest."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 4}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
        Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.3, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 1, "property_id": "HTX004", "doc_type": "purchase_support"}),
        Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Comprehensive Purchase Analysis", "template_code": "purchase_support", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={
            "client_id": 4,
            "broker_id": 1,
            "title": "Purchase consultation",
            "start_at": "2025-09-29T09:00:00Z",
            "end_at": "2025-09-29T10:00:00Z",
            "location": "Office",
            "notes": "Purchase consultation"
        }),
    ],
    outputs=["867058.41"],
),

Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_025",
    instruction=(
        "You should help client 5 evaluate property HTX005 (listing 5), currently listed at $674,900. "
        "Use this price for a 30-year mortgage calculation at 6.5% interest, and provide the total interest owed. "
        "Include comparable listings and generate the analysis report."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 5}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
        Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1, "property_id": "HTX005", "doc_type": "purchase_support"}),
        Action(name="send_email", kwargs={
            "client_id": 5,
            "broker_id": 1,
            "subject": "Comprehensive Purchase Analysis",
            "template_code": "purchase_support",
            "campaign_id": 101
        }),
    ],
    outputs=["860797.75"],
),
Task(
    annotator="Irfan", 
    user_id="RES_TASK_V4_026", 
    instruction=(
        "You need to execute client onboarding protocol for client 6 regarding property HTX006 (listing 6) at 1550000 with 6.7% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-26T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 6}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1550000, "interest_rate": 6.7, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2, "property_id": "HTX006", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 6, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-26T09:00:00Z", "end_at": "2025-09-26T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["2050651.12"],
),
Task(
    annotator="Irfan", 
    user_id="RES_TASK_V4_027", 
    instruction=(
        "You need to execute client onboarding protocol for client 7 regarding property HTX007 (listing 7) at 1490000 with 6.8% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-27T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 7}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 7}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX007"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1490000, "interest_rate": 6.8, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX007", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-27T09:00:00Z", "end_at": "2025-09-27T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["2006926.71"],
),
Task(
    annotator="Irfan", 
    user_id="RES_TASK_V4_028", 
    instruction=(
        "You need to execute client onboarding protocol for client 8 regarding property HTX008 (listing 8) at 1625000 with 6.5% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-28T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 8}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX008"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1625000, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX008", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-28T09:00:00Z", "end_at": "2025-09-28T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["2072597.94"],
),
Task(
    annotator="Irfan", 
    user_id="RES_TASK_V4_029", 
    instruction=(
        "You need to execute client onboarding protocol for client 9 regarding property HTX009 (listing 9) at 1400000 with 6.6% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-29T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 9}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 9}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX009"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1400000, "interest_rate": 6.6, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2, "property_id": "HTX009", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 9, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-29T09:00:00Z", "end_at": "2025-09-29T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1818840.44"],
),
Task(
    annotator="Irfan", 
    user_id="RES_TASK_V4_030", 
    instruction=(
        "You need to execute client onboarding protocol for client 10 regarding property HTX010 (listing 10) at 1295000 with 6.7% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-30T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 10}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX010"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1295000, "interest_rate": 6.7, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2, "property_id": "HTX010", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 10, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-30T09:00:00Z", "end_at": "2025-09-30T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1713285.93"],
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_031",
    instruction=(
        "You need to provide basic property analysis for client 11 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
        "Send Property Analysis Update communication using property_evaluation template with campaign_id 101. "
        "Report the monthly payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 11}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
        Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX001", "doc_type": "property_evaluation"}),
        Action(name="create_campaign", kwargs={"name": "Property Analysis for property_evaluation", "type": "property_evaluation", "created_by": 3}),
        Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Property Analysis Update", "template_code": "property_evaluation", "campaign_id": 101})
    ],
    outputs=["9481.02"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_032",
        instruction=(
            "You need to coordinate property showing for client 14 regarding property HTX003 (listing 3) at 591000 with 7.1% 30-year financing. "
            "Send Property Showing Invitation communication using showing_invitation template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 14}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Property Showing Invitation", "template_code": "showing_invitation", "campaign_id": 101})
        ],
        outputs=["838815.20"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_033",
        instruction=(
            "You need to deliver first-time buyer support to client 17 regarding property HTX005 (listing 5) at 674900 with 6.8% 30-year financing. "
            "Provide comprehensive first-time buyer education and schedule education session on 2025-03-10T14:00:00Z-15:00:00Z at Office with 'First-time buyer education session' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 17}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4, "property_id": "HTX005", "doc_type": "buyer_guide"}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 17, "broker_id": 4, "title": "First-time buyer education session", "start_at": "2025-03-10T14:00:00Z", "end_at": "2025-03-10T15:00:00Z", "location": "Office", "notes": "First-time buyer education session"})
        ],
        outputs=["1583943.51"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_034",
        instruction=(
            "You need to provide luxury marketing services to client 20 regarding property HTX002 (listing 2) at 3975000 with 6.3% 30-year financing. "
            "Send Exclusive Luxury Collection communication using luxury_marketing template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 20}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Exclusive Luxury Collection", "template_code": "luxury_marketing", "campaign_id": 101})
        ],
        outputs=["24604.17"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_035",
        instruction=(
            "You need to support investor outreach for client 3 regarding property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. "
            "Send Investment Opportunity Brief communication using investor_outreach template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 3}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX004", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Investment Opportunity Brief", "template_code": "investor_outreach", "campaign_id": 101})
        ],
                outputs=["1019063.75"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_036",
        instruction=(
            "You need to provide first-time buyer support to client 5 regarding property HTX002 (listing 2) at 3975000 with 6.9% 30-year financing. "
            "Send Welcome Package communication using first_time_buyer template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 5}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 1}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Welcome Package", "template_code": "first_time_buyer", "campaign_id": 101})
        ],
        outputs=["26179.36"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_037",
        instruction=(
            "You need to coordinate property showing for client 8 regarding property HTX001 (listing 1) at 1500000 with 7.0% 30-year financing. "
            "Schedule private property showing on 2025-03-15T15:00:00Z-16:00:00Z at HTX001 with 'Private property showing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 8}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX001", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "Private property showing", "start_at": "2025-03-15T15:00:00Z", "end_at": "2025-03-15T16:00:00Z", "location": "HTX001", "notes": "Private property showing"})
        ],
        outputs=["2092633.47"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_038",
        instruction=(
            "You need to provide luxury marketing services to client 13 regarding property HTX005 (listing 5) at 674900 with 6.6% 30-year financing. "
            "Send Exclusive VIP Access communication using luxury_marketing template with campaign_id 101. "
            "Schedule VIP consultation on 2025-05-05T14:00:00Z-15:00:00Z at Office with 'VIP client consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 13}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 3, "subject": "Exclusive VIP Access", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 13, "broker_id": 3, "title": "VIP client consultation", "start_at": "2025-05-05T14:00:00Z", "end_at": "2025-05-05T15:00:00Z", "location": "Office", "notes": "VIP client consultation"})
        ],
        outputs=["4310.31"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_039",
        instruction=(
            "You need to execute property evaluation protocol for client 18 regarding property HTX003 (listing 3) at 591000 with 7.3% 30-year financing. "
            "Send Property Evaluation Report communication using property_evaluation template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 18}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Property Evaluation Report", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["1458620.71"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_040",
        instruction=(
            "You need to support investor outreach for client 6 regarding property HTX006 (listing 6) at 225700 with 6.4% 30-year financing. "
            "Send Investment Opportunity Brief communication using investor_outreach template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 6}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Investment Opportunity Brief", "template_code": "investor_outreach", "campaign_id": 101})
        ],
                outputs=["282536.06"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_041",
        instruction=(
            "You need to execute relocation protocol for client 9 regarding property HTX001 (listing 1) at 1500000 with 6.8% 30-year financing. "
            "Send Relocation Guide communication using relocation template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 9}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Relocation Guide", "template_code": "relocation", "campaign_id": 101})
        ],
        outputs=["9778.88"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_042",
        instruction=(
            "You need to provide commercial sales services for client 14 regarding property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. "
            "Send Commercial Investment Opportunity communication using commercial_sales template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 14}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX002", "doc_type": "commercial_analysis"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101})
        ],
        outputs=["5641777.34"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_043",
    instruction=(
        "You need to execute estate management protocol for client 17 regarding property HTX003 (listing 3) at 591000 with 6.5% 30-year financing. "
        "Send Estate Services communication using estate_management template with campaign_id 101. "
        "Report the total payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 17}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
        Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 4}),
        Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "Luxury Estate Services", "template_code": "estate_management", "campaign_id": 101})
    ],
    outputs=["1344787.93"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_044",
        instruction=(
            "You need to execute investment consulting protocol for client 12 regarding property HTX004 (listing 4) at 705900 with 7.0% 30-year financing. "
            "Send Investment Strategy communication using investment_consulting template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 12}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "Investment Strategy", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["984793.31"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_045",
        instruction=(
            "You need to execute market analysis protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. "
            "Send Market Insights communication using market_analysis template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 7}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_analysis", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Market Insights", "template_code": "market_analysis", "campaign_id": 101})
        ],
                outputs=["4444.89"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_046",
        instruction=(
            "You need to execute portfolio review protocol for client 15 regarding property HTX002 (listing 2) at 3975000 with 7.2% 30-year financing. "
            "Send Portfolio Review communication using portfolio_review template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 15}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Portfolio Review", "type": "portfolio_review", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Comprehensive Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101})
        ],
        outputs=["5738459.28"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_047",
        instruction=(
            "You need to execute luxury marketing protocol for client 2 regarding property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. "
            "Deliver premium luxury marketing and schedule luxury consultation on 2025-09-25T14:00:00Z-15:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 2}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX002", "doc_type": "luxury_package"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Luxury property consultation", "start_at": "2025-09-25T14:00:00Z", "end_at": "2025-09-25T15:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["26713.27"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_048",
        instruction=(
            "You need to execute client onboarding protocol for client 4 regarding property HTX004 (listing 4) at 705900 with 6.6% 30-year financing. "
            "Send Welcome Package communication using client_onboarding template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 4}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Welcome Package", "template_code": "client_onboarding", "campaign_id": 101})
        ],
        outputs=["1622985.33"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_049",
    instruction=(
        "You need to execute purchase support protocol for client 16 regarding property HTX005 (listing 5) at 674900 with 7.4% 30-year financing. "
        "Send Purchase Support communication using purchase_support template with campaign_id 101. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 16}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
        Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.4, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 4}),
        Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Comprehensive Purchase Analysis", "template_code": "purchase_support", "campaign_id": 101})
    ],
    outputs=["1007333.66"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_050",
        instruction=(
            "You need to execute first time buyer protocol for client 1 regarding property HTX006 (listing 6) at 225700 with 6.3% 30-year financing. "
            "Send Welcome Package communication using first_time_buyer template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 1}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 1}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Welcome Package", "template_code": "first_time_buyer", "campaign_id": 101})
        ],
        outputs=["1397.02"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_051",
    instruction=(
        "You need to deliver comprehensive market intelligence for client 7 regarding property HTX001 (listing 1) at 1500000 with 6.9% 30-year financing. "
        "Schedule briefing on 2025-04-20T10:00:00Z-11:00:00Z at Office with 'Market intelligence consultation' notes and report the monthly payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 7}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
        Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.9, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_intelligence", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX001", "doc_type": "market_intelligence"}),
        Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Comprehensive Market Intelligence", "template_code": "market_intelligence", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "Market intelligence consultation", "start_at": "2025-04-20T10:00:00Z", "end_at": "2025-04-20T11:00:00Z", "location": "Office", "notes": "Market intelligence consultation"})
    ],
    outputs=["9879.0"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_052",
        instruction=(
            "You need to coordinate exclusive property showing for client 18 regarding property HTX004 (listing 4) at 705900 with 7.1% 30-year financing. "
            "Schedule private showing consultation on 2025-04-15T14:00:00Z-15:00:00Z at HTX004 with 'Private property showing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 18}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 18, "broker_id": 4, "title": "Private property showing", "start_at": "2025-04-15T14:00:00Z", "end_at": "2025-04-15T15:00:00Z", "location": "HTX004", "notes": "Private property showing"})
        ],
        outputs=["1001894.5"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_053",
        instruction=(
            "You need to execute investment consulting protocol for client 9 regarding property HTX005 (listing 5) at 674900 with 6.7% 30-year financing. "
            "Send Investment Strategy Analysis communication using investment_consulting template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 9}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Investment Strategy Analysis", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["1567793.19"]
    ),
 Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_054",
    instruction=(
        "You are to execute onboarding for client 14 purchasing HTX014 (listing 14) for 875000 with 6.2% 30-year loan. "
        "Setup a calendar event for 2025-09-24T09:00:00Z and report interest paid."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 14}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 14}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX014"}),
        Action(name="calculate_mortgage", kwargs={"principal": 875000, "interest_rate": 6.2, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX014", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 14, "broker_id": 3, "title": "Client onboarding session", "start_at": "2025-09-24T09:00:00Z", "end_at": "2025-09-24T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["1054277.28"],
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_055",
        instruction=(
            "You need to execute commercial sales protocol for client 20 regarding property HTX003 (listing 3) at 591000 with 7.3% 30-year financing. "
            "Send Commercial Investment Opportunity communication using commercial_sales template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 20}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 4, "property_id": "HTX003", "doc_type": "commercial_analysis"}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101})
        ],
        outputs=["4051.72"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_056",
    instruction=(
        "You need to execute relocation protocol for client 3 regarding property HTX005 (listing 5) at 674900 with 7.2% 30-year financing. "
        "Coordinate relocation consultation on 2025-05-01T09:00:00Z-10:00:00Z at Office with 'Executive relocation planning' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 3}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
        Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.2, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX005", "doc_type": "relocation_guide"}),
        Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 3, "broker_id": 1, "title": "Executive relocation planning", "start_at": "2025-05-01T09:00:00Z", "end_at": "2025-05-01T10:00:00Z", "location": "Office", "notes": "Executive relocation planning"})
    ],
    outputs=["974310.99"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_057",
        instruction=(
            "You need to execute luxury marketing protocol for client 10 regarding property HTX002 (listing 2) at 3975000 with 6.8% 30-year financing. "
            "Deliver exclusive luxury property briefing and schedule VIP consultation on 2025-05-05T15:00:00Z-16:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 10}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2, "property_id": "HTX002", "doc_type": "luxury_briefing"}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 10, "broker_id": 2, "title": "Luxury property consultation", "start_at": "2025-05-05T15:00:00Z", "end_at": "2025-05-05T16:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["25914.03"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_058",
        instruction=(
            "You need to execute client onboarding protocol for client 16 regarding property HTX003 (listing 3) at 591000 with 6.6% 30-year financing. "
            "Provide comprehensive onboarding package with welcome consultation on 2025-05-10T11:00:00Z-12:00:00Z at Office with 'New client onboarding session' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 16}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 4, "property_id": "HTX003", "doc_type": "onboarding_guide"}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 16, "broker_id": 4, "title": "New client onboarding session", "start_at": "2025-05-10T11:00:00Z", "end_at": "2025-05-10T12:00:00Z", "location": "Office", "notes": "New client onboarding session"})
        ],
        outputs=["1358810.50"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_059",
    instruction=(
        "You need to execute first time buyer protocol for client 2 regarding property HTX006 (listing 6) at 225700 with 7.0% 30-year financing. "
        "Provide first-time buyer education and schedule buyer consultation on 2025-05-15T14:00:00Z-15:00:00Z at Office with 'First-time buyer guidance' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 2}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
        Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 7.0, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX006", "doc_type": "buyer_guide"}),
        Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={
            "client_id": 2,
            "broker_id": 1,
            "title": "First-time buyer guidance",
            "start_at": "2025-05-15T14:00:00Z",
            "end_at": "2025-05-15T15:00:00Z",
            "location": "Office",
            "notes": "First-time buyer guidance"
        }),
    ],
    outputs=["314871.58"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_060",
    instruction=(
        "You need to execute investor outreach protocol for client 19 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
        "Schedule consultation on 2025-05-20T10:00:00Z-11:00:00Z at Office with 'Investment opportunity consultation' notes. "
        "Report the monthly payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 19}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
        Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX001", "doc_type": "investment_analysis"}),
        Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Investment Opportunities", "template_code": "investor_outreach", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "Investment opportunity consultation", "start_at": "2025-05-20T10:00:00Z", "end_at": "2025-05-20T11:00:00Z", "location": "Office", "notes": "Investment opportunity consultation"})
    ],
    outputs=["9481.02"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_061",
        instruction=(
            "You need to execute purchase support protocol for client 5 regarding property HTX001 (listing 1) at 1500000 with 6.3% 30-year financing. "
            "Deliver comprehensive purchase analysis and schedule purchase consultation on 2025-06-01T10:00:00Z-11:00:00Z at Office with 'Purchase strategy consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 5}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1, "property_id": "HTX001", "doc_type": "purchase_analysis"}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Comprehensive Purchase Analysis", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 5, "broker_id": 1, "title": "Purchase strategy consultation", "start_at": "2025-06-01T10:00:00Z", "end_at": "2025-06-01T11:00:00Z", "location": "Office", "notes": "Purchase strategy consultation"})
        ],
        outputs=["1842453.06"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_062",
        instruction=(
            "You need to execute property showing protocol for client 12 regarding property HTX005 (listing 5) at 674900 with 7.5% 30-year financing. "
            "Coordinate exclusive property showing and schedule showing appointment on 2025-06-05T15:00:00Z-16:00:00Z at HTX005 with 'Exclusive property viewing' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 12}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 3, "property_id": "HTX005", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 12, "broker_id": 3, "title": "Exclusive property viewing", "start_at": "2025-06-05T15:00:00Z", "end_at": "2025-06-05T16:00:00Z", "location": "HTX005", "notes": "Exclusive property viewing"})
        ],
        outputs=["4719.00"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_063",
        instruction=(
            "You need to execute VIP client protocol for client 8 regarding property HTX006 (listing 6) at 225700 with 6.8% 30-year financing. "
            "Provide exclusive VIP services and schedule VIP consultation on 2025-06-10T14:30:00Z-15:30:00Z at Office with 'VIP client consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 8}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX006", "doc_type": "vip_package"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "VIP Client Services", "template_code": "vip_client", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "VIP client consultation", "start_at": "2025-06-10T14:30:00Z", "end_at": "2025-06-10T15:30:00Z", "location": "Office", "notes": "VIP client consultation"})
        ],
        outputs=["529702.25"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_064",
        instruction=(
            "You need to execute property evaluation protocol for client 17 regarding property HTX004 (listing 4) at 705900 with 6.9% 30-year financing. "
            "Deliver comprehensive property assessment with comparable analysis. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 17}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4, "property_id": "HTX004", "doc_type": "evaluation_report"}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "Comprehensive Market Overview", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["967761.00"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_065",
    instruction=(
        "You need to execute commercial sales protocol for client 1 regarding property HTX002 (listing 2) at 3975000 with 7.0% 30-year financing. "
        "Deliver commercial investment analysis and schedule business meeting on 2025-06-15T09:00:00Z-10:00:00Z at Office with 'Commercial investment strategy' notes. "
        "Report the monthly payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 1}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
        Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.0, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 1}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 1, "property_id": "HTX002", "doc_type": "commercial_brief"}),
        Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Commercial Property Transaction", "template_code": "commercial_sales", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 1,"broker_id": 1,"title": "Commercial investment strategy","start_at": "2025-06-15T09:00:00Z","end_at": "2025-06-15T10:00:00Z","location": "Office","notes": "Commercial investment strategy"})
    ],
    outputs=["26445.77"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_066",
        instruction=(
            "You need to execute first time buyer protocol for client 12 regarding property HTX008 (listing 8) at 330000 with 6.6% 30-year financing. "
            "Provide first-time buyer education and schedule education meeting on 2025-10-25T10:30:00Z-11:30:00Z at Office with 'First-time buyer education' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 12}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX008"}),
            Action(name="calculate_mortgage", kwargs={"principal": 330000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 3, "property_id": "HTX008", "doc_type": "buyer_education"}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 12, "broker_id": 3, "title": "First-time buyer education", "start_at": "2025-10-25T10:30:00Z", "end_at": "2025-10-25T11:30:00Z", "location": "Office", "notes": "First-time buyer education"})
        ],
        outputs=["2107.57"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_067",
    instruction=(
        "You need to execute market intelligence protocol for client 15 regarding property HTX007 (listing 7) at 425600 with 6.5% 30-year financing. "
        "Schedule market review on 2025-06-25T11:00:00Z-12:00:00Z at Office with 'Market analysis review' notes. "
        "Report the monthly payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 15}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 7}),
        Action(name="calculate_mortgage", kwargs={"principal": 425600, "interest_rate": 6.5, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_intelligence", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 3, "property_id": "HTX007", "doc_type": "market_intelligence"}),
        Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Comprehensive Market Intelligence", "template_code": "market_intelligence", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 15, "broker_id": 3, "title": "Market analysis review", "start_at": "2025-06-25T11:00:00Z", "end_at": "2025-06-25T12:00:00Z", "location": "Office", "notes": "Market analysis review"})
    ],
    outputs=["2690.08"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_068",
        instruction=(
            "You need to execute relocation protocol for client 3 regarding property HTX008 (listing 8) at 1275000 with 6.7% 30-year financing. "
            "Deliver comprehensive relocation services and schedule relocation planning on 2025-06-30T16:00:00Z-17:00:00Z at Office with 'Relocation strategy session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 3}),
            Action(name="search_neighborhoods", kwargs={"neighborhood_name": "Downtown"}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
            Action(name="calculate_mortgage", kwargs={"principal": 1275000, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX008", "doc_type": "relocation_guide"}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 3, "broker_id": 1, "title": "Relocation strategy session", "start_at": "2025-06-30T16:00:00Z", "end_at": "2025-06-30T17:00:00Z", "location": "Office", "notes": "Relocation strategy session"})
        ],
        outputs=["1686825.92"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_069",
    instruction=(
        "You need to execute client onboarding protocol for client 9 regarding property HTX011 (listing 11) at 495000 with 5.915% 30-year financing. "
        "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-28T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
        "Report the total interest amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 9}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 11}),
        Action(name="get_comparable_properties", kwargs={"property_id": "HTX011"}),
        Action(name="calculate_mortgage", kwargs={"principal": 495000, "interest_rate": 5.915, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2, "property_id": "HTX011", "doc_type": "onboarding_package"}),
        Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 9, "broker_id": 2, "title": "Client onboarding session", "start_at": "2025-09-28T09:00:00Z", "end_at": "2025-09-28T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
    ],
    outputs=["563680.26"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_070",
        instruction=(
            "You need to execute luxury marketing protocol for client 6 regarding property HTX010 (listing 10) at 2850000 with 6.6% 30-year financing. "
            "Deliver exclusive luxury marketing services and schedule luxury consultation on 2025-07-10T14:00:00Z-15:00:00Z at Office with 'Luxury property strategy' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 6}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
            Action(name="calculate_mortgage", kwargs={"principal": 2850000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2, "property_id": "HTX010", "doc_type": "luxury_briefing"}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 6, "broker_id": 2, "title": "Luxury property strategy", "start_at": "2025-07-10T14:00:00Z", "end_at": "2025-07-10T15:00:00Z", "location": "Office", "notes": "Luxury property strategy"})
        ],
        outputs=["6552639.47"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_071",
        instruction=(
            "You need to execute client onboarding protocol for client 11 regarding property HTX001 (listing 1) at 1500000 with 6.4% 30-year financing. "
            "Deliver comprehensive onboarding package and schedule onboarding consultation on 2025-07-15T09:30:00Z-10:30:00Z at Office with 'Client onboarding session' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 11}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX001", "doc_type": "onboarding_package"}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 11, "broker_id": 3, "title": "Client onboarding session", "start_at": "2025-07-15T09:30:00Z", "end_at": "2025-07-15T10:30:00Z", "location": "Office", "notes": "Client onboarding session"})
        ],
        outputs=["9382.59"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_072",
        instruction=(
            "You need to execute property evaluation protocol for client 14 regarding property HTX002 (listing 2) at 3975000 with 6.8% 30-year financing. "
            "Deliver comprehensive property assessment with market valuation analysis. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 14}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX002", "doc_type": "evaluation_report"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Comprehensive Market Overview", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["5354049.44"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_073",
        instruction=(
            "You need to execute investment consulting protocol for client 19 regarding property HTX003 (listing 3) at 895700 with 7.3% 30-year financing. "
            "Deliver strategic investment guidance with financial modeling analysis. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 19}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 895700, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX003", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Strategic Investment Guidance", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["2210637.17"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_074",
        instruction=(
            "You need to execute commercial sales protocol for client 2 regarding property HTX004 (listing 4) at 705900 with 7.4% 30-year financing. "
            "Deliver commercial investment analysis and schedule commercial meeting on 2025-07-20T11:00:00Z-12:00:00Z at Office with 'Commercial sales strategy' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 2}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX004", "doc_type": "commercial_brief"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Commercial Investment Analysis", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Commercial sales strategy", "start_at": "2025-07-20T11:00:00Z", "end_at": "2025-07-20T12:00:00Z", "location": "Office", "notes": "Commercial sales strategy"})
        ],
        outputs=["4887.51"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_075",
        instruction=(
            "You need to execute VIP client protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. "
            "Provide exclusive VIP services and schedule VIP consultation on 2025-07-25T15:30:00Z-16:30:00Z at Office with 'VIP client strategy session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 7}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX005", "doc_type": "vip_package"}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "VIP Client Services", "template_code": "vip_client", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "VIP client strategy session", "start_at": "2025-07-25T15:30:00Z", "end_at": "2025-07-25T16:30:00Z", "location": "Office", "notes": "VIP client strategy session"})
        ],
        outputs=["925261.23"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_076",
        instruction=(
            "You need to execute portfolio review protocol for client 13 regarding property HTX001 (listing 1) at 1500000 with 6.2% 30-year financing. "
            "Deliver comprehensive portfolio assessment and schedule portfolio consultation on 2025-07-30T09:00:00Z-10:00:00Z at Office with 'Portfolio strategy review' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 13}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Portfolio Review", "type": "portfolio_review", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 13, "broker_id": 3, "property_id": "HTX001", "doc_type": "portfolio_analysis"}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 3, "subject": "Comprehensive Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 13, "broker_id": 3, "title": "Portfolio strategy review", "start_at": "2025-07-30T09:00:00Z", "end_at": "2025-07-30T10:00:00Z", "location": "Office", "notes": "Portfolio strategy review"})
        ],
        outputs=["9187.03"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_077",
        instruction=(
            "You need to execute estate management protocol for client 4 regarding property HTX002 (listing 2) at 3975000 with 6.6% 30-year financing. "
            "Deliver luxury estate services and schedule estate consultation on 2025-08-05T14:00:00Z-15:00:00Z at Office with 'Estate management strategy' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 4}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 1, "property_id": "HTX002", "doc_type": "estate_portfolio"}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Luxury Estate Services", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 4, "broker_id": 1, "title": "Estate management strategy", "start_at": "2025-08-05T14:00:00Z", "end_at": "2025-08-05T15:00:00Z", "location": "Office", "notes": "Estate management strategy"})
        ],
        outputs=["5164207.69"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_078",
    instruction=(
        "You need to execute market intelligence protocol for client 16 regarding property HTX004 (listing 4) at 705900 with 7.3% 30-year financing. "
        "Schedule market briefing on 2025-08-10T11:30:00Z-12:30:00Z at Office with 'Market intelligence consultation' notes. "
        "Report the total payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 16}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
        Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.3, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_intelligence", "created_by": 4}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 4, "property_id": "HTX004", "doc_type": "market_intelligence"}),
        Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Comprehensive Market Intelligence", "template_code": "market_intelligence", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 16, "broker_id": 4, "title": "Market intelligence consultation", "start_at": "2025-08-10T11:30:00Z", "end_at": "2025-08-10T12:30:00Z", "location": "Office", "notes": "Market intelligence consultation"})
    ],
    outputs=["1742200.27"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_079",
        instruction=(
            "You need to execute purchase support protocol for client 10 regarding property HTX003 (listing 3) at 591000 with 6.8% 30-year financing. "
            "Deliver comprehensive purchase analysis and schedule purchase meeting on 2025-08-15T10:00:00Z-11:00:00Z at Office with 'Purchase strategy consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 10}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2, "property_id": "HTX003", "doc_type": "purchase_analysis"}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Comprehensive Purchase Analysis", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 10, "broker_id": 2, "title": "Purchase strategy consultation", "start_at": "2025-08-15T10:00:00Z", "end_at": "2025-08-15T11:00:00Z", "location": "Office", "notes": "Purchase strategy consultation"})
        ],
        outputs=["3852.88"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_080",
        instruction=(
            "You need to execute property showing protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 7.1% 30-year financing. "
            "Coordinate exclusive property showing and schedule showing appointment on 2025-08-20T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 7}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX005", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "Private property viewing", "start_at": "2025-08-20T15:30:00Z", "end_at": "2025-08-20T16:30:00Z", "location": "HTX005", "notes": "Private property viewing"})
        ],
        outputs=["957895.73"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_081",
    instruction=(
        "You need to execute relocation protocol for client 11 regarding property HTX006 (listing 6) at 225700 with 6.9% 30-year financing. "
        "Deliver comprehensive relocation services and schedule relocation consultation on 2025-08-25T10:30:00Z-11:30:00Z at Office with 'Relocation planning session' notes. "
        "Report the total payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 11}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
        Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.9, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 3}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX006", "doc_type": "relocation_guide"}),
        Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 11, "broker_id": 3, "title": "Relocation planning session", "start_at": "2025-08-25T10:30:00Z", "end_at": "2025-08-25T11:30:00Z", "location": "Office", "notes": "Relocation planning session"})
    ],
    outputs=["535125.78"]
),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_082",
    instruction=(
        "You need to execute luxury marketing protocol for client 8 regarding property HTX007 (listing 7) at 425600 with 6.4% 30-year financing. "
        "Deliver premium luxury marketing and schedule luxury consultation on 2025-08-30T14:30:00Z-15:30:00Z at Office with 'Luxury property strategy' notes. "
        "Report the monthly payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 8}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 7}),
        Action(name="calculate_mortgage", kwargs={"principal": 425600, "interest_rate": 6.4, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX007", "doc_type": "luxury_briefing"}),
        Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "Luxury property strategy", "start_at": "2025-08-30T14:30:00Z", "end_at": "2025-08-30T15:30:00Z", "location": "Office", "notes": "Luxury property strategy"})
    ],
    outputs=["2662.15"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_083",
        instruction=(
            "You need to execute first time buyer protocol for client 19 regarding property HTX008 (listing 8) at 1275000 with 7.0% 30-year financing. "
            "Deliver comprehensive first-time buyer guidance and schedule buyer education session on 2025-09-05T09:30:00Z-10:30:00Z at Office with 'First-time buyer consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 19}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
            Action(name="calculate_mortgage", kwargs={"principal": 1275000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX008", "doc_type": "buyer_guide"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "First-time buyer consultation", "start_at": "2025-09-05T09:30:00Z", "end_at": "2025-09-05T10:30:00Z", "location": "Office", "notes": "First-time buyer consultation"})
        ],
        outputs=["1778738.45"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_084",
        instruction=(
            "You need to execute investor outreach protocol for client 2 regarding property HTX009 (listing 9) at 765300 with 6.8% 30-year financing. "
            "Deliver investment opportunity analysis and schedule investor meeting on 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Investment opportunity review' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 2}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 9}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX009"}),
            Action(name="calculate_mortgage", kwargs={"principal": 765300, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX009", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Investment Opportunity Analysis", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Investment opportunity review", "start_at": "2025-09-10T13:00:00Z", "end_at": "2025-09-10T14:00:00Z", "location": "Office", "notes": "Investment opportunity review"})
        ],
        outputs=["1796106.05"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_085",
        instruction=(
            "You need to execute client onboarding protocol for client 15 regarding property HTX010 (listing 10) at 2850000 with 6.5% 30-year financing. "
            "Provide comprehensive onboarding package and schedule onboarding consultation on 2025-09-15T11:00:00Z-12:00:00Z at Office with 'Client onboarding session' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 15}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX010"}),
            Action(name="calculate_mortgage", kwargs={"principal": 2850000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 3, "property_id": "HTX010", "doc_type": "onboarding_package"}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 15, "broker_id": 3, "title": "Client onboarding session", "start_at": "2025-09-15T11:00:00Z", "end_at": "2025-09-15T12:00:00Z", "location": "Office", "notes": "Client onboarding session"})
        ],
        outputs=["18013.94"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_086",
        instruction=(
            "You need to execute VIP client protocol for client 17 regarding property HTX006 (listing 6) at 225700 with 6.3% 30-year financing. "
            "Deliver white-glove VIP service and schedule VIP consultation on 2025-08-25T14:00:00Z-15:00:00Z at Office with 'VIP client consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 17}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4, "property_id": "HTX006", "doc_type": "vip_package"}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "VIP Client Services", "template_code": "vip_client", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 17, "broker_id": 4, "title": "VIP client consultation", "start_at": "2025-08-25T14:00:00Z", "end_at": "2025-08-25T15:00:00Z", "location": "Office", "notes": "VIP client consultation"})
        ],
        outputs=["1397.02"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_087",
        instruction=(
            "You need to execute estate management protocol for client 14 regarding property HTX007 (listing 7) at 1490000 with 6.9% 30-year financing. "
            "Deliver luxury estate services and schedule estate consultation on 2025-08-30T16:00:00Z-17:00:00Z at Office with 'Estate management strategy' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 14}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 7}),
            Action(name="calculate_mortgage", kwargs={"principal": 1490000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX007", "doc_type": "estate_portfolio"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Luxury Estate Services", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 14, "broker_id": 3, "title": "Estate management strategy", "start_at": "2025-08-30T16:00:00Z", "end_at": "2025-08-30T17:00:00Z", "location": "Office", "notes": "Estate management strategy"})
        ],
        outputs=["3532731.11"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_088",
        instruction=(
            "You need to execute first time buyer protocol for client 8 regarding property HTX008 (listing 8) at 330000 with 7.0% 30-year financing. "
            "Provide first-time buyer education and schedule education meeting on 2025-09-05T10:30:00Z-11:30:00Z at Office with 'First-time buyer education' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 8}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
            Action(name="calculate_mortgage", kwargs={"principal": 330000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX008", "doc_type": "buyer_education"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "First-time buyer education", "start_at": "2025-09-05T10:30:00Z", "end_at": "2025-09-05T11:30:00Z", "location": "Office", "notes": "First-time buyer education"})
        ],
        outputs=["460379.36"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_089",
        instruction=(
            "You need to execute luxury marketing protocol for client 19 regarding property HTX009 (listing 9) at 400000 with 6.4% 30-year financing. "
            "Deliver premium luxury marketing and schedule luxury consultation on 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 19}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 9}),
            Action(name="calculate_mortgage", kwargs={"principal": 400000, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX009", "doc_type": "luxury_package"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "Luxury property consultation", "start_at": "2025-09-10T13:00:00Z", "end_at": "2025-09-10T14:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["2502.02"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_090",
        instruction=(
            "You need to execute investment consulting protocol for client 15 regarding property HTX010 (listing 10) at 458500 with 6.7% 30-year financing. "
            "Deliver strategic investment guidance and schedule investment meeting on 2025-09-15T11:00:00Z-12:00:00Z at Office with 'Investment strategy consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 15}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX010"}),
            Action(name="calculate_mortgage", kwargs={"principal": 458500, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 3, "property_id": "HTX010", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Strategic Investment Guidance", "template_code": "investment_consulting", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 15, "broker_id": 3, "title": "Investment strategy consultation", "start_at": "2025-09-15T11:00:00Z", "end_at": "2025-09-15T12:00:00Z", "location": "Office", "notes": "Investment strategy consultation"})
        ],
        outputs=["1065095.83"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_091",
        instruction=(
            "You need to execute client onboarding protocol for client 1 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
            "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-20T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 1}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 1, "property_id": "HTX001", "doc_type": "onboarding_package"}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Comprehensive Client Onboarding", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 1, "broker_id": 1, "title": "Client onboarding session", "start_at": "2025-09-20T09:00:00Z", "end_at": "2025-09-20T10:00:00Z", "location": "Office", "notes": "Client onboarding session"})
        ],
        outputs=["1913167.33"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_092",
        instruction=(
            "You need to execute luxury marketing protocol for client 2 regarding property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. "
            "Deliver premium luxury marketing and schedule luxury consultation on 2025-09-25T14:00:00Z-15:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 2}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX002", "doc_type": "luxury_package"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Luxury property consultation", "start_at": "2025-09-25T14:00:00Z", "end_at": "2025-09-25T15:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["26713.27"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_093",
        instruction=(
            "You need to execute property evaluation protocol for client 3 regarding property HTX003 (listing 3) at 591000 with 6.6% 30-year financing. "
            "Provide comprehensive property analysis and schedule evaluation meeting on 2025-09-30T11:00:00Z-12:00:00Z at Office with 'Property evaluation consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 3}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX003", "doc_type": "evaluation_report"}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Comprehensive Market Overview", "template_code": "property_evaluation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 3, "broker_id": 1, "title": "Property evaluation consultation", "start_at": "2025-09-30T11:00:00Z", "end_at": "2025-09-30T12:00:00Z", "location": "Office", "notes": "Property evaluation consultation"})
        ],
        outputs=["1358810.5"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_094",
        instruction=(
            "You need to execute commercial sales protocol for client 18 regarding property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. "
            "Target commercial property transaction and schedule commercial meeting on 2025-10-05T16:00:00Z-17:00:00Z at Office with 'Commercial transaction consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 18}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 4, "property_id": "HTX004", "doc_type": "commercial_analysis"}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Commercial Property Transaction", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 18, "broker_id": 4, "title": "Commercial transaction consultation", "start_at": "2025-10-05T16:00:00Z", "end_at": "2025-10-05T17:00:00Z", "location": "Office", "notes": "Commercial transaction consultation"})
        ],
        outputs=["1019063.75"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_095",
        instruction=(
            "You need to execute property showing protocol for client 5 regarding property HTX005 (listing 5) at 674900 with 6.8% 30-year financing. "
            "Coordinate exclusive property showing and schedule showing appointment on 2025-10-10T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 5}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1, "property_id": "HTX005", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 5, "broker_id": 1, "title": "Private property viewing", "start_at": "2025-10-10T15:30:00Z", "end_at": "2025-10-10T16:30:00Z", "location": "HTX005", "notes": "Private property viewing"})
        ],
        outputs=["4399.84"]
    ),
    Task(
    annotator="Irfan",
    user_id="RES_TASK_V4_096",
    instruction=(
        "You need to execute relocation protocol for client 6 regarding property HTX006 (listing 6) at 225700 with 7.0% 30-year financing. "
        "Support client relocation and schedule relocation meeting on 2025-10-15T09:00:00Z-10:00:00Z at Office with 'Relocation consultation' notes. "
        "Report the total payment amount."
    ),
    actions=[
        Action(name="find_clients", kwargs={"client_id": 6}),
        Action(name="fetch_listing_details", kwargs={"listing_id": 6}),
        Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 7.0, "loan_term_years": 30}),
        Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 2}),
        Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2, "property_id": "HTX006", "doc_type": "relocation_guide"}),
        Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
        Action(name="create_calendar_event", kwargs={"client_id": 6, "broker_id": 2, "title": "Relocation consultation", "start_at": "2025-10-15T09:00:00Z", "end_at": "2025-10-15T10:00:00Z", "location": "Office", "notes": "Relocation consultation"})
    ],
    outputs=["540571.58"]
),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_097",
        instruction=(
            "You need to execute portfolio review protocol for client 9 regarding property HTX007 (listing 7) at 1490000 with 6.4% 30-year financing. "
            "Deliver comprehensive portfolio assessment and schedule portfolio consultation on 2025-10-20T14:00:00Z-15:00:00Z at Office with 'Portfolio strategy review' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 9}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 7}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX007"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1490000, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Portfolio Review", "type": "portfolio_review", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2, "property_id": "HTX007", "doc_type": "portfolio_analysis"}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Comprehensive Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 9, "broker_id": 2, "title": "Portfolio strategy review", "start_at": "2025-10-20T14:00:00Z", "end_at": "2025-10-20T15:00:00Z", "location": "Office", "notes": "Portfolio strategy review"})
        ],
        outputs=["1865213.7"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_098",
        instruction=(
            "You need to execute first time buyer protocol for client 12 regarding property HTX008 (listing 8) at 330000 with 6.6% 30-year financing. "
            "Provide first-time buyer education and schedule education meeting on 2025-10-25T10:30:00Z-11:30:00Z at Office with 'First-time buyer education' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 12}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 8}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX008"}),
            Action(name="calculate_mortgage", kwargs={"principal": 330000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 3, "property_id": "HTX008", "doc_type": "buyer_education"}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 12, "broker_id": 3, "title": "First-time buyer education", "start_at": "2025-10-25T10:30:00Z", "end_at": "2025-10-25T11:30:00Z", "location": "Office", "notes": "First-time buyer education"})
        ],
        outputs=["2107.57"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_099",
        instruction=(
            "You need to execute market intelligence protocol for client 11 regarding property HTX009 (listing 9) at 400000 with 7.3% 30-year financing. "
            "Deliver quarterly market intelligence and schedule intelligence meeting on 2025-10-30T16:00:00Z-17:00:00Z at Office with 'Market intelligence briefing' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 11}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 9}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX009"}),
            Action(name="calculate_mortgage", kwargs={"principal": 400000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_intelligence", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX009", "doc_type": "market_report"}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Comprehensive Market Intelligence", "template_code": "market_intelligence", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 11, "broker_id": 3, "title": "Market intelligence briefing", "start_at": "2025-10-30T16:00:00Z", "end_at": "2025-10-30T17:00:00Z", "location": "Office", "notes": "Market intelligence briefing"})
        ],
        outputs=["987222.14"]
    ),
    Task(
        annotator="Irfan",
        user_id="RES_TASK_V4_100",
        instruction=(
            "You need to execute purchase support protocol for client 20 regarding property HTX010 (listing 10) at 458500 with 6.5% 30-year financing. "
            "Deliver comprehensive purchase analysis and schedule purchase meeting on 2025-11-05T11:00:00Z-12:00:00Z at Office with 'Purchase strategy consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="find_clients", kwargs={"client_id": 20}),
            Action(name="fetch_listing_details", kwargs={"listing_id": 10}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX010"}),
            Action(name="calculate_mortgage", kwargs={"principal": 458500, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 4, "property_id": "HTX010", "doc_type": "purchase_analysis"}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Comprehensive Purchase Analysis", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 20, "broker_id": 4, "title": "Purchase strategy consultation", "start_at": "2025-11-05T11:00:00Z", "end_at": "2025-11-05T12:00:00Z", "location": "Office", "notes": "Purchase strategy consultation"})
        ],
        outputs=["584791.48"]
    )
]