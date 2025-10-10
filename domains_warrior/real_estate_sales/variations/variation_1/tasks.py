from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "You need to onboard new clients 4, 5, and 6 through broker 1 for property HTX003 (listing 3) at 591000 with 6.8% 30-year financing. "
            "Deliver comprehensive onboarding services with Premium Client Onboarding — Elite Segment campaign client_onboarding type by broker 1. "
            "Provide Welcome to Premium Real Estate Services communications using client_onboarding template with campaign_id 101. "
            "Coordinate consultations for clients 4 and 6 only on 2024-11-20T10:00:00Z-11:00:00Z and 2024-11-20T14:00:00Z-15:00:00Z at Office with 'Premium client onboarding consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Premium Client Onboarding — Elite Segment", "type": "client_onboarding", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 1}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Welcome to Premium Real Estate Services", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Welcome to Premium Real Estate Services", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 1, "subject": "Welcome to Premium Real Estate Services", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 4, "title": "Premium client onboarding consultation", "start_at": "2024-11-20T10:00:00Z", "end_at": "2024-11-20T11:00:00Z", "location": "Office", "notes": "Premium client onboarding consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 6, "title": "Premium client onboarding consultation", "start_at": "2024-11-20T14:00:00Z", "end_at": "2024-11-20T15:00:00Z", "location": "Office", "notes": "Premium client onboarding consultation"})
        ],
        outputs=["3852.88"]
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction=(
            "You execute LuxuryMarketingProtocol for clients 1, 2, and 3 through broker 2 targeting property HTX002 (listing 2) at 3975000 with 6.5% 30-year financing. "
            "Use campaign 'December Luxury Properties Showcase' luxury_marketing type by broker 2. "
            "Send 'Exclusive Luxury Properties Available' emails using luxury_marketing template with campaign_id 101. "
            "Schedule consultations for clients 1 and 3 only on 2024-12-02T14:00:00Z-15:00:00Z and 2024-12-02T15:30:00Z-16:30:00Z at Office with 'Luxury property investment consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "December Luxury Properties Showcase", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 2}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 2, "subject": "Exclusive Luxury Properties Available", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 2, "subject": "Exclusive Luxury Properties Available", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 2, "subject": "Exclusive Luxury Properties Available", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 1, "title": "Luxury property investment consultation", "start_at": "2024-12-02T14:00:00Z", "end_at": "2024-12-02T15:00:00Z", "location": "Office", "notes": "Luxury property investment consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 3, "title": "Luxury property investment consultation", "start_at": "2024-12-02T15:30:00Z", "end_at": "2024-12-02T16:30:00Z", "location": "Office", "notes": "Luxury property investment consultation"})
        ],
        outputs=["9044893.42"]
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "You execute PurchaseSupportProtocol for clients 7, 8, and 9 through broker 2 targeting property HTX004 (listing 4) at 705900 with 7.0% 30-year financing. "
            "Use campaign 'HTX004 Purchase Analysis — Premium Buyers' purchase_support type by broker 2. "
            "Send 'HTX004 Purchase Analysis Ready' emails using purchase_support template with campaign_id 101. "
            "Schedule consultations for clients 7 and 9 only on 2024-12-01T10:00:00Z-11:00:00Z and 2024-12-01T14:00:00Z-15:00:00Z at Office with 'Review purchase analysis and financing' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "HTX004 Purchase Analysis — Premium Buyers", "type": "purchase_support", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "HTX004 Purchase Analysis Ready", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "HTX004 Purchase Analysis Ready", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "HTX004 Purchase Analysis Ready", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 7, "title": "Review purchase analysis and financing", "start_at": "2024-12-01T10:00:00Z", "end_at": "2024-12-01T11:00:00Z", "location": "Office", "notes": "Review purchase analysis and financing"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 9, "title": "Review purchase analysis and financing", "start_at": "2024-12-01T14:00:00Z", "end_at": "2024-12-01T15:00:00Z", "location": "Office", "notes": "Review purchase analysis and financing"})
        ],
        outputs=["4696.37"]
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction=(
            "You execute PropertyShowingProtocol for clients 10, 11, and 12 through broker 2 targeting property HTX002 (listing 2) at 3975000 with 6.5% 30-year financing. "
            "Use campaign 'HTX002 Elite Private Showings' property_showing type by broker 2. "
            "Send 'Exclusive Property Showing Invitation' emails using showing_invitation template with campaign_id 101. "
            "Schedule showings for clients 10 and 12 only on 2024-11-22T15:00:00Z-16:00:00Z and 2024-11-22T17:00:00Z-18:00:00Z at HTX002 with 'Private property showing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "HTX002 Elite Private Showings", "type": "property_showing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 2}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Exclusive Property Showing Invitation", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 2, "subject": "Exclusive Property Showing Invitation", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 2, "subject": "Exclusive Property Showing Invitation", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 10, "title": "Private property showing", "start_at": "2024-11-22T15:00:00Z", "end_at": "2024-11-22T16:00:00Z", "location": "HTX002", "notes": "Private property showing"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 12, "title": "Private property showing", "start_at": "2024-11-22T17:00:00Z", "end_at": "2024-11-22T18:00:00Z", "location": "HTX002", "notes": "Private property showing"})
        ],
        outputs=["5069893.42"]
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "You deliver quarterly market intelligence to clients 13, 14, and 15 through broker 1 regarding property HTX006 (listing 6) at 890000 with 6.9% financing over 30 years. "
            "Execute MarketIntelligenceProtocol with campaign November Market Intelligence Brief — Elite Segment and Q4 Market Intelligence Update communications. "
            "Coordinate strategic briefings for clients 13 and 15 on 2024-11-25 at 09:00-10:00 and 14:00-15:00. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 13}),
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
            Action(name="calculate_mortgage", kwargs={"principal": 890000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "November Market Intelligence Brief — Elite Segment", "type": "market_update", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 13, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 1}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 1, "subject": "Q4 Market Intelligence Update", "template_code": "market_update", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 1, "subject": "Q4 Market Intelligence Update", "template_code": "market_update", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 1, "subject": "Q4 Market Intelligence Update", "template_code": "market_update", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 13, "title": "Market intelligence briefing", "start_at": "2024-11-25T09:00:00Z", "end_at": "2024-11-25T10:00:00Z", "location": "Office", "notes": "Market intelligence briefing"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 15, "title": "Market intelligence briefing", "start_at": "2024-11-25T14:00:00Z", "end_at": "2024-11-25T15:00:00Z", "location": "Office", "notes": "Market intelligence briefing"})
        ],
        outputs=["2110154.82"]
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction=(
            "You need to connect with investor clients 16, 17, and 18 through broker 3 regarding property HTX005 (listing 5) at 1200000 with 7.2% 30-year financing. "
            "Deliver Strategic Investment Opportunities — Q4 Edition campaign investor_outreach type by broker 3. "
            "Provide Investment Opportunity Analysis communications using investor_outreach template with campaign_id 101. "
            "Coordinate investment consultations for clients 16 and 18 only on 2024-12-15T11:00:00Z-12:00:00Z and 2024-12-15T15:00:00Z-16:00:00Z at Office with 'Investment opportunity consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1200000, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Strategic Investment Opportunities — Q4 Edition", "type": "investor_outreach", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 3}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 3, "subject": "Investment Opportunity Analysis", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 3, "subject": "Investment Opportunity Analysis", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 3, "subject": "Investment Opportunity Analysis", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 16, "title": "Investment opportunity consultation", "start_at": "2024-12-15T11:00:00Z", "end_at": "2024-12-15T12:00:00Z", "location": "Office", "notes": "Investment opportunity consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 18, "title": "Investment opportunity consultation", "start_at": "2024-12-15T15:00:00Z", "end_at": "2024-12-15T16:00:00Z", "location": "Office", "notes": "Investment opportunity consultation"})
        ],
        outputs=["8145.46"]
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction=(
            "You execute FirstTimeBuyerProtocol for clients 19, 20, and 1 through broker 4 targeting property HTX001 (listing 1) at 1500000 with 6.75% 30-year financing. "
            "Use campaign 'First Time Buyer Education Series' first_time_buyer type by broker 4. "
            "Send 'Your First Home Purchase Guide' emails using first_time_buyer template with campaign_id 101. "
            "Schedule education sessions for clients 19 and 1 only on 2024-12-10T09:30:00Z-10:30:00Z and 2024-12-10T14:30:00Z-15:30:00Z at Office with 'First-time buyer education session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.75, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Time Buyer Education Series", "type": "first_time_buyer", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 4}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Your First Home Purchase Guide", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Your First Home Purchase Guide", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 4, "subject": "Your First Home Purchase Guide", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 4, "client_id": 19, "title": "First-time buyer education session", "start_at": "2024-12-10T09:30:00Z", "end_at": "2024-12-10T10:30:00Z", "location": "Office", "notes": "First-time buyer education session"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 4, "client_id": 1, "title": "First-time buyer education session", "start_at": "2024-12-10T14:30:00Z", "end_at": "2024-12-10T15:30:00Z", "location": "Office", "notes": "First-time buyer education session"})
        ],
        outputs=["2002429.72"]
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction=(
            "You execute PropertyEvaluationProtocol for clients 2, 3, and 4 through broker 5 targeting property HTX003 (listing 3) at 591000 with 6.8% financing over 30 years. "
            "Deliver comprehensive market analysis with campaign Property Market Evaluation — December 2024 and Property Valuation Assessment communications. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Market Evaluation — December 2024", "type": "property_evaluation", "created_by": 5}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 5}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 5}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 5}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 5, "subject": "Property Valuation Assessment", "template_code": "property_evaluation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 5, "subject": "Property Valuation Assessment", "template_code": "property_evaluation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 5, "subject": "Property Valuation Assessment", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["1387036.03"]
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "You need to provide VIP concierge services to clients 6, 7, and 8 through broker 2 targeting property HTX002 (listing 2) at 3975000 with 6.5% 30-year financing. "
            "Create 'VIP Concierge Services — Exclusive Properties' campaign and provide 'Exclusive VIP Property Access' communications. "
            "Coordinate VIP consultations for clients 6 and 8 only on 2024-12-20T10:00:00Z-11:00:00Z and 2024-12-20T16:00:00Z-17:00:00Z at Office with 'VIP property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Concierge Services — Exclusive Properties", "type": "vip_service", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Exclusive VIP Property Access", "template_code": "vip_service", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Exclusive VIP Property Access", "template_code": "vip_service", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Exclusive VIP Property Access", "template_code": "vip_service", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 6, "title": "VIP property consultation", "start_at": "2024-12-20T10:00:00Z", "end_at": "2024-12-20T11:00:00Z", "location": "Office", "notes": "VIP property consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 8, "title": "VIP property consultation", "start_at": "2024-12-20T16:00:00Z", "end_at": "2024-12-20T17:00:00Z", "location": "Office", "notes": "VIP property consultation"})
        ],
        outputs=["25124.7"]
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "You need to deliver comprehensive market research for clients 8, 9, and 10 through broker 7 regarding Houston neighborhoods with focus on property HTX004 (listing 4) at 705900 with 7.0% financing over 30 years. "
            "Provide Comprehensive Market Research — Houston Focus campaign and Regional Market Analysis communications. "
            "Coordinate research consultations for clients 8 and 10 only on 2024-12-22T09:00:00Z-10:00:00Z and 2024-12-22T14:00:00Z-15:00:00Z at Office with 'Market research consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="search_neighborhoods", kwargs={"city": "Houston"}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Comprehensive Market Research — Houston Focus", "type": "market_analysis", "created_by": 7}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 7}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 7}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 7}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 7, "subject": "Regional Market Analysis", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 7, "subject": "Regional Market Analysis", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 7, "subject": "Regional Market Analysis", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 7, "client_id": 8, "title": "Market research consultation", "start_at": "2024-12-22T09:00:00Z", "end_at": "2024-12-22T10:00:00Z", "location": "Office", "notes": "Market research consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 7, "client_id": 10, "title": "Market research consultation", "start_at": "2024-12-22T14:00:00Z", "end_at": "2024-12-22T15:00:00Z", "location": "Office", "notes": "Market research consultation"})
        ],
        outputs=["984793.31"]
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "You execute PortfolioReviewProtocol for clients 11, 12, and 13 through broker 8 targeting property HTX006 (listing 6) at 890000 with 6.6% 30-year financing. "
            "Use campaign 'Quarterly Portfolio Analysis — Q4 Review' portfolio_review type by broker 8. "
            "Send 'Portfolio Performance Update' emails using portfolio_review template with campaign_id 101. "
            "Schedule portfolio consultations for clients 11 and 13 only on 2024-12-28T10:30:00Z-11:30:00Z and 2024-12-28T15:30:00Z-16:30:00Z at Office with 'Portfolio performance consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="search_clients", kwargs={"client_id": 13}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
            Action(name="calculate_mortgage", kwargs={"principal": 890000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Quarterly Portfolio Analysis — Q4 Review", "type": "portfolio_review", "created_by": 8}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 8}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 8}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 13, "broker_id": 8}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 8, "subject": "Portfolio Performance Update", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 8, "subject": "Portfolio Performance Update", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 8, "subject": "Portfolio Performance Update", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 8, "client_id": 11, "title": "Portfolio performance consultation", "start_at": "2024-12-28T10:30:00Z", "end_at": "2024-12-28T11:30:00Z", "location": "Office", "notes": "Portfolio performance consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 8, "client_id": 13, "title": "Portfolio performance consultation", "start_at": "2024-12-28T15:30:00Z", "end_at": "2024-12-28T16:30:00Z", "location": "Office", "notes": "Portfolio performance consultation"})
        ],
        outputs=["5684.06"]
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "You execute CommercialSalesProtocol for clients 14, 15, and 16 through broker 9 targeting property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. "
            "Use campaign 'Commercial Property Specialists — Elite Division' commercial_sales type by broker 9. "
            "Send 'Commercial Investment Opportunity' emails using commercial_sales template with campaign_id 101. "
            "Schedule commercial consultations for clients 14 and 16 only on 2025-01-05T09:15:00Z-10:15:00Z and 2025-01-05T14:15:00Z-15:15:00Z at Office with 'Commercial property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Property Specialists — Elite Division", "type": "commercial_sales", "created_by": 9}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 9}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 9}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 9}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 9, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 9, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 9, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 9, "client_id": 14, "title": "Commercial property consultation", "start_at": "2025-01-05T09:15:00Z", "end_at": "2025-01-05T10:15:00Z", "location": "Office", "notes": "Commercial property consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 9, "client_id": 16, "title": "Commercial property consultation", "start_at": "2025-01-05T14:15:00Z", "end_at": "2025-01-05T15:15:00Z", "location": "Office", "notes": "Commercial property consultation"})
        ],
        outputs=["26713.27"]
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "You execute RelocationProtocol for clients 17, 18, and 19 through broker 10 targeting Houston neighborhoods with focus on property HTX001 (listing 1) at 1500000 with 6.9% financing over 30 years. "
            "Use campaign 'Executive Relocation Services — Houston Gateway' relocation type by broker 10. "
            "Send 'Houston Relocation Guide' emails using relocation template with campaign_id 101. "
            "Schedule relocation consultations for clients 17 and 19 only on 2025-01-10T11:00:00Z-12:00:00Z and 2025-01-10T16:00:00Z-17:00:00Z at Office with 'Executive relocation consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="search_neighborhoods", kwargs={"city": "Houston"}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Executive Relocation Services — Houston Gateway", "type": "relocation", "created_by": 10}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 10}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 10}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 10}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 10, "subject": "Houston Relocation Guide", "template_code": "relocation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 10, "subject": "Houston Relocation Guide", "template_code": "relocation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 10, "subject": "Houston Relocation Guide", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 10, "client_id": 17, "title": "Executive relocation consultation", "start_at": "2025-01-10T11:00:00Z", "end_at": "2025-01-10T12:00:00Z", "location": "Office", "notes": "Executive relocation consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 10, "client_id": 19, "title": "Executive relocation consultation", "start_at": "2025-01-10T16:00:00Z", "end_at": "2025-01-10T17:00:00Z", "location": "Office", "notes": "Executive relocation consultation"})
        ],
        outputs=["2056440.72"]
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "You execute InvestmentConsultingProtocol for clients 20, 1, and 2 through broker 11 targeting property HTX004 (listing 4) at 705900 with 6.7% financing over 30 years. "
            "Use campaign 'Strategic Investment Advisory — Premium Services' investment_consulting type by broker 11. "
            "Send 'Investment Strategy Analysis' emails using investment_consulting template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Strategic Investment Advisory — Premium Services", "type": "investment_consulting", "created_by": 11}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 11}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 11}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 11}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 11, "subject": "Investment Strategy Analysis", "template_code": "investment_consulting", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 11, "subject": "Investment Strategy Analysis", "template_code": "investment_consulting", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 11, "subject": "Investment Strategy Analysis", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["1639806.21"]
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "You execute EstateManagementProtocol for clients 3, 4, and 5 through broker 12 targeting property HTX005 (listing 5) at 1200000 with 6.8% 30-year financing. "
            "Use campaign 'Luxury Estate Management — Concierge Collection' estate_management type by broker 12. "
            "Send 'Estate Portfolio Review' emails using estate_management template with campaign_id 101. "
            "Schedule estate consultations for clients 3 and 5 only on 2025-01-15T10:00:00Z-11:00:00Z and 2025-01-15T15:00:00Z-16:00:00Z at Office with 'Luxury estate consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 1200000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Estate Management — Concierge Collection", "type": "estate_management", "created_by": 12}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 12}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 12}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 12}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 12, "subject": "Estate Portfolio Review", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 12, "subject": "Estate Portfolio Review", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 12, "subject": "Estate Portfolio Review", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 12, "client_id": 3, "title": "Luxury estate consultation", "start_at": "2025-01-15T10:00:00Z", "end_at": "2025-01-15T11:00:00Z", "location": "Office", "notes": "Luxury estate consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 12, "client_id": 5, "title": "Luxury estate consultation", "start_at": "2025-01-15T15:00:00Z", "end_at": "2025-01-15T16:00:00Z", "location": "Office", "notes": "Luxury estate consultation"})
        ],
        outputs=["7823.1"]
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "You need to onboard new clients 6, 7, and 8 through broker 1 for property HTX001 (listing 1) at 1500000 with 6.4% 30-year financing. "
            "Deliver comprehensive onboarding services with Elite Client Onboarding — Winter Collection campaign client_onboarding type by broker 1. "
            "Provide Welcome to Elite Real Estate Services communications using client_onboarding template with campaign_id 101. "
            "Coordinate onboarding consultations for clients 6 and 8 only on 2025-01-20T09:00:00Z-10:00:00Z and 2025-01-20T14:00:00Z-15:00:00Z at Office with 'Elite client onboarding session' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Elite Client Onboarding — Winter Collection", "type": "client_onboarding", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 1}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 1, "subject": "Welcome to Elite Real Estate Services", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 1, "subject": "Welcome to Elite Real Estate Services", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 1, "subject": "Welcome to Elite Real Estate Services", "template_code": "client_onboarding", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 6, "title": "Elite client onboarding session", "start_at": "2025-01-20T09:00:00Z", "end_at": "2025-01-20T10:00:00Z", "location": "Office", "notes": "Elite client onboarding session"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 8, "title": "Elite client onboarding session", "start_at": "2025-01-20T14:00:00Z", "end_at": "2025-01-20T15:00:00Z", "location": "Office", "notes": "Elite client onboarding session"})
        ],
        outputs=["9382.59"]
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "You need to deliver luxury marketing services to clients 9, 10, and 11 through broker 2 targeting property HTX006 (listing 6) at 890000 with 6.3% 30-year financing. "
            "Create Luxury Properties — Exclusive Winter Showcase campaign luxury_marketing type by broker 2. "
            "Send Exclusive Winter Property Collection communications using luxury_marketing template with campaign_id 101. "
            "Schedule luxury consultations for clients 9 and 11 only on 2025-01-22T11:00:00Z-12:00:00Z and 2025-01-22T16:00:00Z-17:00:00Z at Office with 'Luxury property showcase consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 890000, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Properties — Exclusive Winter Showcase", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 2}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Exclusive Winter Property Collection", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Exclusive Winter Property Collection", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 2, "subject": "Exclusive Winter Property Collection", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 9, "title": "Luxury property showcase consultation", "start_at": "2025-01-22T11:00:00Z", "end_at": "2025-01-22T12:00:00Z", "location": "Office", "notes": "Luxury property showcase consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 11, "title": "Luxury property showcase consultation", "start_at": "2025-01-22T16:00:00Z", "end_at": "2025-01-22T17:00:00Z", "location": "Office", "notes": "Luxury property showcase consultation"})
        ],
        outputs=["1983188.82"]
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "You need to provide purchase support for clients 12, 13, and 14 through broker 3 regarding property HTX005 (listing 5) at 1200000 with 6.6% 30-year financing. "
            "Deliver HTX005 Purchase Analysis — Strategic Buyers campaign and HTX005 Purchase Support Ready communications. "
            "Coordinate purchase consultations for clients 12 and 14 only on 2025-01-25T10:00:00Z-11:00:00Z and 2025-01-25T15:00:00Z-16:00:00Z at Office with 'Purchase analysis consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="search_clients", kwargs={"client_id": 13}),
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1200000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "HTX005 Purchase Analysis — Strategic Buyers", "type": "purchase_support", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 13, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "HTX005 Purchase Support Ready", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 3, "subject": "HTX005 Purchase Support Ready", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "HTX005 Purchase Support Ready", "template_code": "purchase_support", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 12, "title": "Purchase analysis consultation", "start_at": "2025-01-25T10:00:00Z", "end_at": "2025-01-25T11:00:00Z", "location": "Office", "notes": "Purchase analysis consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 14, "title": "Purchase analysis consultation", "start_at": "2025-01-25T15:00:00Z", "end_at": "2025-01-25T16:00:00Z", "location": "Office", "notes": "Purchase analysis consultation"})
        ],
        outputs=["7663.91"]
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "You need to coordinate exclusive property showings for clients 15, 16, and 17 through broker 4 regarding property HTX003 (listing 3) at 591000 with 6.7% 30-year financing. "
            "Create HTX003 Elite Property Showings campaign and send Exclusive Property Access Invitation communications. "
            "Schedule property showings for clients 15 and 17 only on 2025-01-28T13:00:00Z-14:00:00Z and 2025-01-28T16:00:00Z-17:00:00Z at HTX003 with 'Exclusive property showcase' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "HTX003 Elite Property Showings", "type": "property_showing", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 4, "subject": "Exclusive Property Access Invitation", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Exclusive Property Access Invitation", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "Exclusive Property Access Invitation", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 4, "client_id": 15, "title": "Exclusive property showcase", "start_at": "2025-01-28T13:00:00Z", "end_at": "2025-01-28T14:00:00Z", "location": "HTX003", "notes": "Exclusive property showcase"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 4, "client_id": 17, "title": "Exclusive property showcase", "start_at": "2025-01-28T16:00:00Z", "end_at": "2025-01-28T17:00:00Z", "location": "HTX003", "notes": "Exclusive property showcase"})
        ],
        outputs=["781893.43"]
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction=(
            "You need to deliver quarterly market intelligence to clients 18, 19, and 20 through broker 5 regarding property HTX004 (listing 4) at 705900 with 6.5% 30-year financing. "
            "Provide Q1 Market Intelligence — Strategic Insights campaign and Q1 Market Intelligence Brief communications. "
            "Coordinate market briefings for clients 18 and 20 only on 2025-01-30T09:30:00Z-10:30:00Z and 2025-01-30T14:30:00Z-15:30:00Z at Office with 'Strategic market intelligence briefing' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Q1 Market Intelligence — Strategic Insights", "type": "market_update", "created_by": 5}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 5}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 5}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 5}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 5, "subject": "Q1 Market Intelligence Brief", "template_code": "market_update", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 5, "subject": "Q1 Market Intelligence Brief", "template_code": "market_update", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 5, "subject": "Q1 Market Intelligence Brief", "template_code": "market_update", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 5, "client_id": 18, "title": "Strategic market intelligence briefing", "start_at": "2025-01-30T09:30:00Z", "end_at": "2025-01-30T10:30:00Z", "location": "Office", "notes": "Strategic market intelligence briefing"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 5, "client_id": 20, "title": "Strategic market intelligence briefing", "start_at": "2025-01-30T14:30:00Z", "end_at": "2025-01-30T15:30:00Z", "location": "Office", "notes": "Strategic market intelligence briefing"})
        ],
        outputs=["1606236.54"]
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction=(
            "You need to support high-value investor clients 1, 2, and 3 through broker 1 regarding property HTX002 (listing 2) at 2500000 with 6.1% 30-year financing. "
            "Deliver comprehensive investor outreach services with Elite Investor Outreach — Q1 Initiative and Exclusive Investment Opportunity communications. "
            "Coordinate investment consultations for clients 1 and 3 only on 2025-02-05T10:00:00Z-11:00:00Z and 2025-02-05T15:00:00Z-16:00:00Z at Office with 'High-value investment consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 2500000, "interest_rate": 6.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Elite Investor Outreach — Q1 Initiative", "type": "investor_outreach", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 1, "property_id": "HTX002", "doc_type": "investment_analysis"}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX002", "doc_type": "investment_analysis"}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX002", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Exclusive Investment Opportunity", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Exclusive Investment Opportunity", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Exclusive Investment Opportunity", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 1, "title": "High-value investment consultation", "start_at": "2025-02-05T10:00:00Z", "end_at": "2025-02-05T11:00:00Z", "location": "Office", "notes": "High-value investment consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 3, "title": "High-value investment consultation", "start_at": "2025-02-05T15:00:00Z", "end_at": "2025-02-05T16:00:00Z", "location": "Office", "notes": "High-value investment consultation"})
        ],
        outputs=["15149.87"]
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction=(
            "You need to provide first-time buyer education to clients 4, 5, and 6 through broker 7 targeting property HTX004 (listing 4) at 650000 with 6.8% 30-year financing. "
            "Deliver First-Time Buyer Education — Spring Series campaign and Your Home Buying Journey communications. "
            "Coordinate education sessions for clients 4 and 6 only on 2025-02-08T09:00:00Z-10:00:00Z and 2025-02-08T14:00:00Z-15:00:00Z at Office with 'First-time buyer education session' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 650000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First-Time Buyer Education — Spring Series", "type": "first_time_buyer", "created_by": 7}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 7}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 7}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 7}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 7, "subject": "Your Home Buying Journey", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 7, "subject": "Your Home Buying Journey", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 7, "subject": "Your Home Buying Journey", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 7, "client_id": 4, "title": "First-time buyer education session", "start_at": "2025-02-08T09:00:00Z", "end_at": "2025-02-08T10:00:00Z", "location": "Office", "notes": "First-time buyer education session"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 7, "client_id": 6, "title": "First-time buyer education session", "start_at": "2025-02-08T14:00:00Z", "end_at": "2025-02-08T15:00:00Z", "location": "Office", "notes": "First-time buyer education session"})
        ],
        outputs=["1525504.94"]
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction=(
            "You need to deliver comprehensive property evaluation for clients 7, 8, and 9 through broker 8 regarding property HTX006 (listing 6) at 980000 with 6.9% 30-year financing. "
            "Create HTX006 Market Evaluation — Professional Assessment campaign and Property Analysis Report communications. "
            "Coordinate evaluation consultations for clients 7 and 9 only on 2025-02-12T11:00:00Z-12:00:00Z and 2025-02-12T16:00:00Z-17:00:00Z at Office with 'Property evaluation consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
            Action(name="calculate_mortgage", kwargs={"principal": 980000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "HTX006 Market Evaluation — Professional Assessment", "type": "property_evaluation", "created_by": 8}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 8}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 8}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 8}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 8, "subject": "Property Analysis Report", "template_code": "property_evaluation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 8, "subject": "Property Analysis Report", "template_code": "property_evaluation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 8, "subject": "Property Analysis Report", "template_code": "property_evaluation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 8, "client_id": 7, "title": "Property evaluation consultation", "start_at": "2025-02-12T11:00:00Z", "end_at": "2025-02-12T12:00:00Z", "location": "Office", "notes": "Property evaluation consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 8, "client_id": 9, "title": "Property evaluation consultation", "start_at": "2025-02-12T16:00:00Z", "end_at": "2025-02-12T17:00:00Z", "location": "Office", "notes": "Property evaluation consultation"})
        ],
        outputs=["6454.28"]
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction=(
            "You need to provide VIP concierge services to clients 10, 11, and 12 through broker 9 targeting property HTX001 (listing 1) at 1800000 with 6.2% 30-year financing. "
            "Create VIP Concierge Services — Elite Experience campaign and Exclusive VIP Property Services communications. "
            "Schedule VIP consultations for clients 10 and 12 only on 2025-02-15T13:00:00Z-14:00:00Z and 2025-02-15T17:00:00Z-18:00:00Z at Office with 'VIP concierge consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1800000, "interest_rate": 6.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Concierge Services — Elite Experience", "type": "vip_service", "created_by": 9}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 9}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 9}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 9}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 9, "subject": "Exclusive VIP Property Services", "template_code": "vip_service", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 9, "subject": "Exclusive VIP Property Services", "template_code": "vip_service", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 9, "subject": "Exclusive VIP Property Services", "template_code": "vip_service", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 9, "client_id": 10, "title": "VIP concierge consultation", "start_at": "2025-02-15T13:00:00Z", "end_at": "2025-02-15T14:00:00Z", "location": "Office", "notes": "VIP concierge consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 9, "client_id": 12, "title": "VIP concierge consultation", "start_at": "2025-02-15T17:00:00Z", "end_at": "2025-02-15T18:00:00Z", "location": "Office", "notes": "VIP concierge consultation"})
        ],
        outputs=["2168798.97"]
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction=(
            "You need to provide comprehensive market analysis for clients 13, 14, and 15 through broker 3 regarding Houston neighborhoods with focus on property HTX005 (listing 5) at 550000 with 7.0% financing over 30 years. "
            "Deliver Houston Market Analysis — Q1 Comprehensive Study campaign and Regional Market Intelligence communications. "
            "Coordinate analysis briefings for clients 13 and 15 only on 2025-02-18T10:30:00Z-11:30:00Z and 2025-02-18T15:30:00Z-16:30:00Z at Office with 'Market analysis briefing' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 13}),
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="search_neighborhoods", kwargs={"city": "Houston"}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 550000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Houston Market Analysis — Q1 Comprehensive Study", "type": "market_analysis", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 13, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 3}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 3, "subject": "Regional Market Intelligence", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Regional Market Intelligence", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Regional Market Intelligence", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 13, "title": "Market analysis briefing", "start_at": "2025-02-18T10:30:00Z", "end_at": "2025-02-18T11:30:00Z", "location": "Office", "notes": "Market analysis briefing"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 15, "title": "Market analysis briefing", "start_at": "2025-02-18T15:30:00Z", "end_at": "2025-02-18T16:30:00Z", "location": "Office", "notes": "Market analysis briefing"})
        ],
        outputs=["1317298.94"]
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "You need to provide comprehensive relocation services to clients 16, 17, and 18 through broker 11 regarding property HTX003 (listing 3) at 591000 with 7.3% 30-year financing. "
            "Deliver Executive Relocation — Houston Elite Program campaign relocation type by broker 11. "
            "Send Houston Relocation Package communications to all three clients using relocation template with campaign_id 101. "
            "Coordinate relocation meetings for clients 16 and 18 only on 2025-03-01T09:30:00Z-10:30:00Z and 2025-03-01T15:30:00Z-16:30:00Z at Office with 'Executive relocation planning' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Executive Relocation — Houston Elite Program", "type": "relocation", "created_by": 11}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 11}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 11}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 11}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 11, "subject": "Houston Relocation Package", "template_code": "relocation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 11, "subject": "Houston Relocation Package", "template_code": "relocation", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 11, "subject": "Houston Relocation Package", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 11, "client_id": 16, "title": "Executive relocation planning", "start_at": "2025-03-01T09:30:00Z", "end_at": "2025-03-01T10:30:00Z", "location": "Office", "notes": "Executive relocation planning"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 11, "client_id": 18, "title": "Executive relocation planning", "start_at": "2025-03-01T15:30:00Z", "end_at": "2025-03-01T16:30:00Z", "location": "Office", "notes": "Executive relocation planning"})
        ],
        outputs=["4051.72"]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction=(
            "You need to deliver investment consulting services to clients 19, 20, and 1 through broker 12 targeting property HTX006 (listing 6) at 890000 with 7.4% 30-year financing. "
            "Create Strategic Investment Portfolio — Premium Advisory campaign investment_consulting type by broker 12. "
            "Send Investment Portfolio Analysis communications using investment_consulting template with campaign_id 101. "
            "Schedule investment reviews for clients 19 and 1 only on 2025-03-05T11:00:00Z-12:00:00Z and 2025-03-05T16:00:00Z-17:00:00Z at Office with 'Investment portfolio consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
            Action(name="calculate_mortgage", kwargs={"principal": 890000, "interest_rate": 7.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Strategic Investment Portfolio — Premium Advisory", "type": "investment_consulting", "created_by": 12}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 12}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 12}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 12}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 12, "subject": "Investment Portfolio Analysis", "template_code": "investment_consulting", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 12, "subject": "Investment Portfolio Analysis", "template_code": "investment_consulting", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 12, "subject": "Investment Portfolio Analysis", "template_code": "investment_consulting", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 12, "client_id": 19, "title": "Investment portfolio consultation", "start_at": "2025-03-05T11:00:00Z", "end_at": "2025-03-05T12:00:00Z", "location": "Office", "notes": "Investment portfolio consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 12, "client_id": 1, "title": "Investment portfolio consultation", "start_at": "2025-03-05T16:00:00Z", "end_at": "2025-03-05T17:00:00Z", "location": "Office", "notes": "Investment portfolio consultation"})
        ],
        outputs=["1328384.88"]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction=(
            "You need to support commercial property acquisition for clients 2, 3, and 4 through broker 1 regarding property HTX004 (listing 4) at 705900 with 7.5% 30-year financing. "
            "Deliver Commercial Real Estate — Elite Business Division campaign commercial_sales type by broker 1. "
            "Send Commercial Property Opportunity communications using commercial_sales template with campaign_id 101. "
            "Schedule business meetings for clients 2 and 4 only on 2025-03-08T10:15:00Z-11:15:00Z and 2025-03-08T14:15:00Z-15:15:00Z at Office with 'Commercial property strategy meeting' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Real Estate — Elite Business Division", "type": "commercial_sales", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 1}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Commercial Property Opportunity", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Commercial Property Opportunity", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Commercial Property Opportunity", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 2, "title": "Commercial property strategy meeting", "start_at": "2025-03-08T10:15:00Z", "end_at": "2025-03-08T11:15:00Z", "location": "Office", "notes": "Commercial property strategy meeting"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 1, "client_id": 4, "title": "Commercial property strategy meeting", "start_at": "2025-03-08T14:15:00Z", "end_at": "2025-03-08T15:15:00Z", "location": "Office", "notes": "Commercial property strategy meeting"})
        ],
        outputs=["1776871.88"]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "You need to provide portfolio review services to clients 5, 6, and 7 through broker 2 regarding property HTX002 (listing 2) at 2500000 with 7.6% 30-year financing. "
            "Create Elite Portfolio Management — Q1 Review campaign portfolio_review type by broker 2. "
            "Send Quarterly Portfolio Assessment communications using portfolio_review template with campaign_id 101. "
            "Schedule portfolio reviews for clients 5 and 7 only on 2025-03-12T09:45:00Z-10:45:00Z and 2025-03-12T15:45:00Z-16:45:00Z at Office with 'Portfolio performance review' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 2500000, "interest_rate": 7.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Elite Portfolio Management — Q1 Review", "type": "portfolio_review", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 2, "subject": "Quarterly Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Quarterly Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Quarterly Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 5, "title": "Portfolio performance review", "start_at": "2025-03-12T09:45:00Z", "end_at": "2025-03-12T10:45:00Z", "location": "Office", "notes": "Portfolio performance review"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 2, "client_id": 7, "title": "Portfolio performance review", "start_at": "2025-03-12T15:45:00Z", "end_at": "2025-03-12T16:45:00Z", "location": "Office", "notes": "Portfolio performance review"})
        ],
        outputs=["17651.87"]
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "You need to deliver estate management services to clients 8, 9, and 10 through broker 3 targeting property HTX001 (listing 1) at 1500000 with 7.7% 30-year financing. "
            "Create Luxury Estate Services — Premium Collection campaign estate_management type by broker 3. "
            "Send Estate Management Portfolio communications using estate_management template with campaign_id 101. "
            "Coordinate estate consultations for clients 8 and 10 only on 2025-03-15T08:30:00Z-09:30:00Z and 2025-03-15T13:30:00Z-14:30:00Z at Office with 'Estate management consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 7.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Estate Services — Premium Collection", "type": "estate_management", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 3}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 3, "subject": "Estate Management Portfolio", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 3, "subject": "Estate Management Portfolio", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 3, "subject": "Estate Management Portfolio", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 8, "title": "Estate management consultation", "start_at": "2025-03-15T08:30:00Z", "end_at": "2025-03-15T09:30:00Z", "location": "Office", "notes": "Estate management consultation"}),
            Action(name="create_calendar_event", kwargs={"broker_id": 3, "client_id": 10, "title": "Estate management consultation", "start_at": "2025-03-15T13:30:00Z", "end_at": "2025-03-15T14:30:00Z", "location": "Office", "notes": "Estate management consultation"})
        ],
        outputs=["2349984.94"]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "You need to provide basic property analysis for client 11 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
            "Send Property Analysis Update communication using property_evaluation template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Property Analysis Update", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["9481.02"]
    ),
    Task(
        annotator="0",
        user_id="task_032",
        instruction=(
            "You need to coordinate property showing for client 14 regarding property HTX003 (listing 3) at 591000 with 7.1% 30-year financing. "
            "Send Property Showing Invitation communication using showing_invitation template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Property Showing Invitation", "template_code": "showing_invitation", "campaign_id": 101})
        ],
        outputs=["838815.20"]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction=(
            "You need to deliver first-time buyer support to client 17 regarding property HTX005 (listing 5) at 674900 with 6.8% 30-year financing. "
            "Provide comprehensive first-time buyer education and schedule education session on 2025-03-10T14:00:00Z-15:00:00Z at Office with 'First-time buyer education session' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
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
        annotator="0",
        user_id="task_034",
        instruction=(
            "You need to provide luxury marketing services to client 20 regarding property HTX002 (listing 2) at 3975000 with 6.3% 30-year financing. "
            "Send Exclusive Luxury Collection communication using luxury_marketing template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Exclusive Luxury Collection", "template_code": "luxury_marketing", "campaign_id": 101})
        ],
        outputs=["24604.17"]
    ),
    Task(
        annotator="0",
        user_id="task_035",
        instruction=(
            "You need to support investor outreach for client 3 regarding property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. "
            "Send Investment Opportunity Brief communication using investor_outreach template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX004", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Investment Opportunity Brief", "template_code": "investor_outreach", "campaign_id": 101})
        ],
                outputs=["1019063.75"]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction=(
            "You need to provide first-time buyer support to client 5 regarding property HTX002 (listing 2) at 3975000 with 6.9% 30-year financing. "
            "Send Welcome Package communication using first_time_buyer template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 1}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Welcome Package", "template_code": "first_time_buyer", "campaign_id": 101})
        ],
        outputs=["26179.36"]
    ),
    Task(
        annotator="0",
        user_id="task_037",
        instruction=(
            "You need to coordinate property showing for client 8 regarding property HTX001 (listing 1) at 1500000 with 7.0% 30-year financing. "
            "Schedule private property showing on 2025-03-15T15:00:00Z-16:00:00Z at HTX001 with 'Private property showing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX001", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "Private property showing", "start_at": "2025-03-15T15:00:00Z", "end_at": "2025-03-15T16:00:00Z", "location": "HTX001", "notes": "Private property showing"})
        ],
        outputs=["2092633.47"]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "You need to provide luxury marketing services to client 13 regarding property HTX005 (listing 5) at 674900 with 6.6% 30-year financing. "
            "Send Exclusive VIP Access communication using luxury_marketing template with campaign_id 101. "
            "Schedule VIP consultation on 2025-05-05T14:00:00Z-15:00:00Z at Office with 'VIP client consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 13}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 13, "broker_id": 3, "subject": "Exclusive VIP Access", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 13, "broker_id": 3, "title": "VIP client consultation", "start_at": "2025-05-05T14:00:00Z", "end_at": "2025-05-05T15:00:00Z", "location": "Office", "notes": "VIP client consultation"})
        ],
        outputs=["4310.31"]
    ),
    Task(
        annotator="0",
        user_id="task_039",
        instruction=(
            "You need to execute property evaluation protocol for client 18 regarding property HTX003 (listing 3) at 591000 with 7.3% 30-year financing. "
            "Send Property Evaluation Report communication using property_evaluation template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Property Evaluation Report", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["1458620.71"]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction=(
            "You need to support investor outreach for client 6 regarding property HTX006 (listing 6) at 225700 with 6.4% 30-year financing. "
            "Send Investment Opportunity Brief communication using investor_outreach template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX006"}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Investment Opportunity Brief", "template_code": "investor_outreach", "campaign_id": 101})
        ],
                outputs=["282536.06"]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction=(
            "You need to execute relocation protocol for client 9 regarding property HTX001 (listing 1) at 1500000 with 6.8% 30-year financing. "
            "Send Relocation Guide communication using relocation template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Relocation Guide", "template_code": "relocation", "campaign_id": 101})
        ],
        outputs=["9778.88"]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction=(
            "You need to provide commercial sales services for client 14 regarding property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. "
            "Send Commercial Investment Opportunity communication using commercial_sales template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX002", "doc_type": "commercial_analysis"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101})
        ],
        outputs=["5641777.34"]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction=(
            "You need to execute estate management protocol for client 17 regarding property HTX003 (listing 3) at 591000 with 6.5% 30-year financing. "
            "Send Estate Services communication using estate_management template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "Estate Services", "template_code": "estate_management", "campaign_id": 101})
        ],
        outputs=["1344787.93"]
    ),
    Task(
        annotator="0",
        user_id="task_044",
        instruction=(
            "You need to execute investment consulting protocol for client 12 regarding property HTX004 (listing 4) at 705900 with 7.0% 30-year financing. "
            "Send Investment Strategy communication using investment_consulting template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "Investment Strategy", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["984793.31"]
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction=(
            "You need to execute market analysis protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. "
            "Send Market Insights communication using market_analysis template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_analysis", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Market Insights", "template_code": "market_analysis", "campaign_id": 101})
        ],
                outputs=["4444.89"]
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "You need to execute portfolio review protocol for client 15 regarding property HTX002 (listing 2) at 3975000 with 7.2% 30-year financing. "
            "Send Portfolio Review communication using portfolio_review template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Portfolio Review", "type": "portfolio_review", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Comprehensive Portfolio Assessment", "template_code": "portfolio_review", "campaign_id": 101})
        ],
        outputs=["5738459.28"]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "You need to execute VIP client protocol for client 11 regarding property HTX003 (listing 3) at 591000 with 6.7% 30-year financing. "
            "Send VIP Services communication using vip_client template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "VIP Services", "template_code": "vip_client", "campaign_id": 101})
        ],
        outputs=["3813.59"]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction=(
            "You need to execute client onboarding protocol for client 4 regarding property HTX004 (listing 4) at 705900 with 6.6% 30-year financing. "
            "Send Welcome Package communication using client_onboarding template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Client Onboarding", "type": "client_onboarding", "created_by": 1}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Welcome Package", "template_code": "client_onboarding", "campaign_id": 101})
        ],
        outputs=["1622985.33"]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "You need to execute purchase support protocol for client 16 regarding property HTX005 (listing 5) at 674900 with 7.4% 30-year financing. "
            "Send Purchase Support communication using purchase_support template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Purchase Support", "type": "purchase_support", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Purchase Support", "template_code": "purchase_support", "campaign_id": 101})
        ],
        outputs=["1007333.66"]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "You need to execute first time buyer protocol for client 1 regarding property HTX006 (listing 6) at 225700 with 6.3% 30-year financing. "
            "Send Welcome Package communication using first_time_buyer template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 1}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Welcome Package", "template_code": "first_time_buyer", "campaign_id": 101})
        ],
        outputs=["1397.02"]
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction=(
            "You need to deliver comprehensive market analysis for client 7 regarding property HTX001 (listing 1) at 1500000 with 6.9% 30-year financing. "
            "Provide Market Intelligence Report with comparable properties analysis and schedule market intelligence briefing on 2025-04-20T10:00:00Z-11:00:00Z at Office with 'Market intelligence consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_analysis", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX001", "doc_type": "market_analysis"}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Market Intelligence Report", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "Market intelligence consultation", "start_at": "2025-04-20T10:00:00Z", "end_at": "2025-04-20T11:00:00Z", "location": "Office", "notes": "Market intelligence consultation"})
        ],
        outputs=["9879.0"]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction=(
            "You need to coordinate exclusive property showing for client 18 regarding property HTX004 (listing 4) at 705900 with 7.1% 30-year financing. "
            "Schedule private showing consultation on 2025-04-15T14:00:00Z-15:00:00Z at HTX004 with 'Private property showing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 4}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 18, "broker_id": 4, "title": "Private property showing", "start_at": "2025-04-15T14:00:00Z", "end_at": "2025-04-15T15:00:00Z", "location": "HTX004", "notes": "Private property showing"})
        ],
        outputs=["1001894.5"]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction=(
            "You need to execute investment consulting protocol for client 9 regarding property HTX005 (listing 5) at 674900 with 6.7% 30-year financing. "
            "Send Investment Strategy Analysis communication using investment_consulting template with campaign_id 101. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX005"}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 2}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Investment Strategy Analysis", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["1567793.19"]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction=(
            "You need to execute estate management protocol for client 14 regarding property HTX002 (listing 2) at 3975000 with 6.4% 30-year financing. "
            "Send Estate Portfolio Review communication using estate_management template with campaign_id 101. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 3}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Estate Portfolio Review", "template_code": "estate_management", "campaign_id": 101})
        ],
        outputs=["4975989.56"]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction=(
            "You need to execute commercial sales protocol for client 20 regarding property HTX003 (listing 3) at 591000 with 7.3% 30-year financing. "
            "Send Commercial Investment Opportunity communication using commercial_sales template with campaign_id 101. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="calculate_mortgage", kwargs={"principal": 591000, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 20, "broker_id": 4, "property_id": "HTX003", "doc_type": "commercial_analysis"}),
            Action(name="send_email", kwargs={"client_id": 20, "broker_id": 4, "subject": "Commercial Investment Opportunity", "template_code": "commercial_sales", "campaign_id": 101})
        ],
        outputs=["4051.72"]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "You need to execute relocation protocol for client 3 regarding property HTX005 (listing 5) at 674900 with 7.2% 30-year financing. "
            "Provide Houston relocation guide with neighborhood analysis and coordinate relocation consultation on 2025-05-01T09:00:00Z-10:00:00Z at Office with 'Executive relocation planning' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="search_neighborhoods", kwargs={"city": "Houston"}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX005", "doc_type": "relocation_guide"}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Houston Relocation Guide", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 3, "broker_id": 1, "title": "Executive relocation planning", "start_at": "2025-05-01T09:00:00Z", "end_at": "2025-05-01T10:00:00Z", "location": "Office", "notes": "Executive relocation planning"})
        ],
        outputs=["974310.99"]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "You need to execute luxury marketing protocol for client 10 regarding property HTX002 (listing 2) at 3975000 with 6.8% 30-year financing. "
            "Deliver exclusive luxury property briefing and schedule VIP consultation on 2025-05-05T15:00:00Z-16:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 10, "broker_id": 2, "property_id": "HTX002", "doc_type": "luxury_briefing"}),
            Action(name="send_email", kwargs={"client_id": 10, "broker_id": 2, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 10, "broker_id": 2, "title": "Luxury property consultation", "start_at": "2025-05-05T15:00:00Z", "end_at": "2025-05-05T16:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["25914.03"]
    ),
    Task(
        annotator="0",
        user_id="task_058",
        instruction=(
            "You need to execute client onboarding protocol for client 16 regarding property HTX003 (listing 3) at 591000 with 6.6% 30-year financing. "
            "Provide comprehensive onboarding package with welcome consultation on 2025-05-10T11:00:00Z-12:00:00Z at Office with 'New client onboarding session' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
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
        annotator="0",
        user_id="task_059",
        instruction=(
            "You need to execute first time buyer protocol for client 2 regarding property HTX006 (listing 6) at 225700 with 7.0% 30-year financing. "
            "Provide first-time buyer education and schedule buyer consultation on 2025-05-15T14:00:00Z-15:00:00Z at Office with 'First-time buyer guidance' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX006", "doc_type": "buyer_guide"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "First Home Purchase Guide", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "First-time buyer guidance", "start_at": "2025-05-15T14:00:00Z", "end_at": "2025-05-15T15:00:00Z", "location": "Office", "notes": "First-time buyer guidance"})
        ],
        outputs=["314871.58"]
    ),
    Task(
        annotator="0",
        user_id="task_060",
        instruction=(
            "You need to execute investor outreach protocol for client 19 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
            "Deliver investment opportunity analysis with consultation on 2025-05-20T10:00:00Z-11:00:00Z at Office with 'Investment opportunity consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX001"}),
            Action(name="calculate_mortgage", kwargs={"principal": 1500000, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX001", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Investment Opportunity Analysis", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "Investment opportunity consultation", "start_at": "2025-05-20T10:00:00Z", "end_at": "2025-05-20T11:00:00Z", "location": "Office", "notes": "Investment opportunity consultation"})
        ],
        outputs=["9481.02"]
    ),
    Task(
        annotator="0",
        user_id="task_061",
        instruction=(
            "You need to execute purchase support protocol for client 5 regarding property HTX001 (listing 1) at 1500000 with 6.3% 30-year financing. "
            "Deliver comprehensive purchase analysis and schedule purchase consultation on 2025-06-01T10:00:00Z-11:00:00Z at Office with 'Purchase strategy consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
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
        annotator="0",
        user_id="task_062",
        instruction=(
            "You need to execute property showing protocol for client 12 regarding property HTX005 (listing 5) at 674900 with 7.5% 30-year financing. "
            "Coordinate exclusive property showing and schedule showing appointment on 2025-06-05T15:00:00Z-16:00:00Z at HTX005 with 'Exclusive property viewing' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 12, "broker_id": 3, "property_id": "HTX005", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 12, "broker_id": 3, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 12, "broker_id": 3, "title": "Exclusive property viewing", "start_at": "2025-06-05T15:00:00Z", "end_at": "2025-06-05T16:00:00Z", "location": "HTX005", "notes": "Exclusive property viewing"})
        ],
        outputs=["4719.00"]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction=(
            "You need to execute VIP client protocol for client 8 regarding property HTX006 (listing 6) at 225700 with 6.8% 30-year financing. "
            "Provide exclusive VIP services and schedule VIP consultation on 2025-06-10T14:30:00Z-15:30:00Z at Office with 'VIP client consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX006", "doc_type": "vip_package"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "VIP Client Services", "template_code": "vip_client", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "VIP client consultation", "start_at": "2025-06-10T14:30:00Z", "end_at": "2025-06-10T15:30:00Z", "location": "Office", "notes": "VIP client consultation"})
        ],
        outputs=["529702.25"]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "You need to execute property evaluation protocol for client 17 regarding property HTX004 (listing 4) at 705900 with 6.9% 30-year financing. "
            "Deliver comprehensive property assessment with comparable analysis. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4, "property_id": "HTX004", "doc_type": "evaluation_report"}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "Comprehensive Market Overview", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["967761.00"]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "You need to execute commercial sales protocol for client 1 regarding property HTX002 (listing 2) at 3975000 with 7.0% 30-year financing. "
            "Deliver commercial investment analysis and schedule business meeting on 2025-06-15T09:00:00Z-10:00:00Z at Office with 'Commercial investment strategy' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 1, "broker_id": 1, "property_id": "HTX002", "doc_type": "commercial_brief"}),
            Action(name="send_email", kwargs={"client_id": 1, "broker_id": 1, "subject": "Commercial Property Transaction", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 1, "broker_id": 1, "title": "Commercial investment strategy", "start_at": "2025-06-15T09:00:00Z", "end_at": "2025-06-15T10:00:00Z", "location": "Office", "notes": "Commercial investment strategy"})
        ],
        outputs=["26445.77"]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "You need to execute first time buyer protocol for client 9 regarding property HTX003 (listing 3) at 895700 with 7.2% 30-year financing. "
            "Deliver comprehensive first-time buyer guidance and schedule buyer education session on 2025-06-20T13:00:00Z-14:00:00Z at Office with 'First-time buyer consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 895700, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 9, "broker_id": 2, "property_id": "HTX003", "doc_type": "buyer_guide"}),
            Action(name="send_email", kwargs={"client_id": 9, "broker_id": 2, "subject": "Comprehensive First-Time Buyer Guidance", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 9, "broker_id": 2, "title": "First-time buyer consultation", "start_at": "2025-06-20T13:00:00Z", "end_at": "2025-06-20T14:00:00Z", "location": "Office", "notes": "First-time buyer consultation"})
        ],
        outputs=["2188766.16"]
    ),
    Task(
        annotator="0",
        user_id="task_067",
        instruction=(
            "You need to execute market analysis protocol for client 15 in neighborhood Midtown regarding property HTX007 (listing 7) at 425600 with 6.5% 30-year financing. "
            "Provide comprehensive market intelligence and schedule market review on 2025-06-25T11:00:00Z-12:00:00Z at Office with 'Market analysis review' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="get_listing_details", kwargs={"listing_id": 7}),
            Action(name="search_neighborhoods", kwargs={"neighborhood_name": "Midtown"}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX007"}),
            Action(name="calculate_mortgage", kwargs={"principal": 425600, "interest_rate": 6.5, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Analysis", "type": "market_analysis", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 15, "broker_id": 3, "property_id": "HTX007", "doc_type": "market_report"}),
            Action(name="send_email", kwargs={"client_id": 15, "broker_id": 3, "subject": "Comprehensive Market Intelligence", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 15, "broker_id": 3, "title": "Market analysis review", "start_at": "2025-06-25T11:00:00Z", "end_at": "2025-06-25T12:00:00Z", "location": "Office", "notes": "Market analysis review"})
        ],
        outputs=["2690.08"]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "You need to execute relocation protocol for client 3 regarding property HTX008 (listing 8) at 1275000 with 6.7% 30-year financing. "
            "Deliver comprehensive relocation services and schedule relocation planning on 2025-06-30T16:00:00Z-17:00:00Z at Office with 'Relocation strategy session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="search_neighborhoods", kwargs={"neighborhood_name": "Downtown"}),
            Action(name="get_listing_details", kwargs={"listing_id": 8}),
            Action(name="calculate_mortgage", kwargs={"principal": 1275000, "interest_rate": 6.7, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 3, "broker_id": 1, "property_id": "HTX008", "doc_type": "relocation_guide"}),
            Action(name="send_email", kwargs={"client_id": 3, "broker_id": 1, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 3, "broker_id": 1, "title": "Relocation strategy session", "start_at": "2025-06-30T16:00:00Z", "end_at": "2025-06-30T17:00:00Z", "location": "Office", "notes": "Relocation strategy session"})
        ],
        outputs=["1686825.92"]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "You need to execute investor outreach protocol for client 18 regarding property HTX009 (listing 9) at 765300 with 7.1% 30-year financing. "
            "Deliver investment opportunity analysis and schedule investor meeting on 2025-07-05T10:30:00Z-11:30:00Z at Office with 'Investment opportunity review' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="get_listing_details", kwargs={"listing_id": 9}),
            Action(name="calculate_mortgage", kwargs={"principal": 765300, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Opportunities", "type": "investor_outreach", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 4, "property_id": "HTX009", "doc_type": "investment_brief"}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Investment Opportunity Analysis", "template_code": "investor_outreach", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 18, "broker_id": 4, "title": "Investment opportunity review", "start_at": "2025-07-05T10:30:00Z", "end_at": "2025-07-05T11:30:00Z", "location": "Office", "notes": "Investment opportunity review"})
        ],
        outputs=["5143.06"]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "You need to execute luxury marketing protocol for client 6 regarding property HTX010 (listing 10) at 2850000 with 6.6% 30-year financing. "
            "Deliver exclusive luxury marketing services and schedule luxury consultation on 2025-07-10T14:00:00Z-15:00:00Z at Office with 'Luxury property strategy' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="get_listing_details", kwargs={"listing_id": 10}),
            Action(name="calculate_mortgage", kwargs={"principal": 2850000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2, "property_id": "HTX010", "doc_type": "luxury_briefing"}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 6, "broker_id": 2, "title": "Luxury property strategy", "start_at": "2025-07-10T14:00:00Z", "end_at": "2025-07-10T15:00:00Z", "location": "Office", "notes": "Luxury property strategy"})
        ],
        outputs=["6552639.47"]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "You need to execute client onboarding protocol for client 11 regarding property HTX001 (listing 1) at 1500000 with 6.4% 30-year financing. "
            "Deliver comprehensive onboarding package and schedule onboarding consultation on 2025-07-15T09:30:00Z-10:30:00Z at Office with 'Client onboarding session' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
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
        annotator="0",
        user_id="task_072",
        instruction=(
            "You need to execute property evaluation protocol for client 14 regarding property HTX002 (listing 2) at 3975000 with 6.8% 30-year financing. "
            "Deliver comprehensive property assessment with market valuation analysis. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX002"}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Analysis", "type": "property_evaluation", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX002", "doc_type": "evaluation_report"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Comprehensive Market Overview", "template_code": "property_evaluation", "campaign_id": 101})
        ],
        outputs=["5354049.44"]
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
            "You need to execute investment consulting protocol for client 19 regarding property HTX003 (listing 3) at 895700 with 7.3% 30-year financing. "
            "Deliver strategic investment guidance with financial modeling analysis. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX003"}),
            Action(name="calculate_mortgage", kwargs={"principal": 895700, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Investment Consulting", "type": "investment_consulting", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX003", "doc_type": "investment_analysis"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Strategic Investment Guidance", "template_code": "investment_consulting", "campaign_id": 101})
        ],
        outputs=["2210637.17"]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction=(
            "You need to execute commercial sales protocol for client 2 regarding property HTX004 (listing 4) at 705900 with 7.4% 30-year financing. "
            "Deliver commercial investment analysis and schedule commercial meeting on 2025-07-20T11:00:00Z-12:00:00Z at Office with 'Commercial sales strategy' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX004", "doc_type": "commercial_brief"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Commercial Investment Analysis", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Commercial sales strategy", "start_at": "2025-07-20T11:00:00Z", "end_at": "2025-07-20T12:00:00Z", "location": "Office", "notes": "Commercial sales strategy"})
        ],
        outputs=["4887.51"]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction=(
            "You need to execute VIP client protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. "
            "Provide exclusive VIP services and schedule VIP consultation on 2025-07-25T15:30:00Z-16:30:00Z at Office with 'VIP client strategy session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX005", "doc_type": "vip_package"}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "VIP Client Services", "template_code": "vip_client", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "VIP client strategy session", "start_at": "2025-07-25T15:30:00Z", "end_at": "2025-07-25T16:30:00Z", "location": "Office", "notes": "VIP client strategy session"})
        ],
        outputs=["925261.23"]
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction=(
            "You need to execute portfolio review protocol for client 13 regarding property HTX001 (listing 1) at 1500000 with 6.2% 30-year financing. "
            "Deliver comprehensive portfolio assessment and schedule portfolio consultation on 2025-07-30T09:00:00Z-10:00:00Z at Office with 'Portfolio strategy review' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 13}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
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
        annotator="0",
        user_id="task_077",
        instruction=(
            "You need to execute estate management protocol for client 4 regarding property HTX002 (listing 2) at 3975000 with 6.6% 30-year financing. "
            "Deliver luxury estate services and schedule estate consultation on 2025-08-05T14:00:00Z-15:00:00Z at Office with 'Estate management strategy' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 4}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 6.6, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 4, "broker_id": 1, "property_id": "HTX002", "doc_type": "estate_portfolio"}),
            Action(name="send_email", kwargs={"client_id": 4, "broker_id": 1, "subject": "Luxury Estate Services", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 4, "broker_id": 1, "title": "Estate management strategy", "start_at": "2025-08-05T14:00:00Z", "end_at": "2025-08-05T15:00:00Z", "location": "Office", "notes": "Estate management strategy"})
        ],
        outputs=["5164207.69"]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction=(
            "You need to execute market analysis protocol for client 16 in neighborhood Westside regarding property HTX004 (listing 4) at 705900 with 7.3% 30-year financing. "
            "Provide comprehensive market intelligence and schedule market briefing on 2025-08-10T11:30:00Z-12:30:00Z at Office with 'Market intelligence consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 16}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="search_neighborhoods", kwargs={"neighborhood_name": "Westside"}),
            Action(name="get_comparable_properties", kwargs={"property_id": "HTX004"}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Market Intelligence", "type": "market_analysis", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 16, "broker_id": 4, "property_id": "HTX004", "doc_type": "market_report"}),
            Action(name="send_email", kwargs={"client_id": 16, "broker_id": 4, "subject": "Comprehensive Market Intelligence", "template_code": "market_analysis", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 16, "broker_id": 4, "title": "Market intelligence consultation", "start_at": "2025-08-10T11:30:00Z", "end_at": "2025-08-10T12:30:00Z", "location": "Office", "notes": "Market intelligence consultation"})
        ],
        outputs=["1742200.27"]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
            "You need to execute purchase support protocol for client 10 regarding property HTX003 (listing 3) at 591000 with 6.8% 30-year financing. "
            "Deliver comprehensive purchase analysis and schedule purchase meeting on 2025-08-15T10:00:00Z-11:00:00Z at Office with 'Purchase strategy consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 10}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
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
        annotator="0",
        user_id="task_080",
        instruction=(
            "You need to execute property showing protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 7.1% 30-year financing. "
            "Coordinate exclusive property showing and schedule showing appointment on 2025-08-20T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 7}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 7, "broker_id": 2, "property_id": "HTX005", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 7, "broker_id": 2, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 7, "broker_id": 2, "title": "Private property viewing", "start_at": "2025-08-20T15:30:00Z", "end_at": "2025-08-20T16:30:00Z", "location": "HTX005", "notes": "Private property viewing"})
        ],
        outputs=["957895.73"]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction=(
            "You need to execute relocation protocol for client 11 in neighborhood Downtown regarding property HTX006 (listing 6) at 225700 with 6.9% 30-year financing. "
            "Deliver comprehensive relocation services and schedule relocation consultation on 2025-08-25T10:30:00Z-11:30:00Z at Office with 'Relocation planning session' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="search_neighborhoods", kwargs={"neighborhood_name": "Downtown"}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 11, "broker_id": 3, "property_id": "HTX006", "doc_type": "relocation_guide"}),
            Action(name="send_email", kwargs={"client_id": 11, "broker_id": 3, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 11, "broker_id": 3, "title": "Relocation planning session", "start_at": "2025-08-25T10:30:00Z", "end_at": "2025-08-25T11:30:00Z", "location": "Office", "notes": "Relocation planning session"})
        ],
        outputs=["535125.78"]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction=(
            "You need to execute luxury marketing protocol for client 8 regarding property HTX007 (listing 7) at 425600 with 6.4% 30-year financing. "
            "Deliver exclusive luxury marketing services and schedule luxury consultation on 2025-08-30T14:30:00Z-15:30:00Z at Office with 'Luxury property strategy' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="get_listing_details", kwargs={"listing_id": 7}),
            Action(name="calculate_mortgage", kwargs={"principal": 425600, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX007", "doc_type": "luxury_briefing"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "Exclusive Luxury Marketing Services", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "Luxury property strategy", "start_at": "2025-08-30T14:30:00Z", "end_at": "2025-08-30T15:30:00Z", "location": "Office", "notes": "Luxury property strategy"})
        ],
        outputs=["2662.15"]
    ),
    Task(
        annotator="0",
        user_id="task_083",
        instruction=(
            "You need to execute first time buyer protocol for client 19 regarding property HTX008 (listing 8) at 1275000 with 7.0% 30-year financing. "
            "Deliver comprehensive first-time buyer guidance and schedule buyer education session on 2025-09-05T09:30:00Z-10:30:00Z at Office with 'First-time buyer consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="get_listing_details", kwargs={"listing_id": 8}),
            Action(name="calculate_mortgage", kwargs={"principal": 1275000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX008", "doc_type": "buyer_guide"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "First-time buyer consultation", "start_at": "2025-09-05T09:30:00Z", "end_at": "2025-09-05T10:30:00Z", "location": "Office", "notes": "First-time buyer consultation"})
        ],
        outputs=["1778738.45"]
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction=(
            "You need to execute investor outreach protocol for client 2 regarding property HTX009 (listing 9) at 765300 with 6.8% 30-year financing. "
            "Deliver investment opportunity analysis and schedule investor meeting on 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Investment opportunity review' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="get_listing_details", kwargs={"listing_id": 9}),
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
        annotator="0",
        user_id="task_085",
        instruction=(
            "You need to execute client onboarding protocol for client 15 regarding property HTX010 (listing 10) at 2850000 with 6.5% 30-year financing. "
            "Provide comprehensive onboarding package and schedule onboarding consultation on 2025-09-15T11:00:00Z-12:00:00Z at Office with 'Client onboarding session' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="get_listing_details", kwargs={"listing_id": 10}),
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
        annotator="0",
        user_id="task_086",
        instruction=(
            "You need to execute VIP client protocol for client 17 regarding property HTX006 (listing 6) at 225700 with 6.3% 30-year financing. "
            "Deliver white-glove VIP service and schedule VIP consultation on 2025-08-25T14:00:00Z-15:00:00Z at Office with 'VIP client consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 17}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 6.3, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "VIP Client Services", "type": "vip_client", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 17, "broker_id": 4, "property_id": "HTX006", "doc_type": "vip_package"}),
            Action(name="send_email", kwargs={"client_id": 17, "broker_id": 4, "subject": "VIP Client Services", "template_code": "vip_client", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 17, "broker_id": 4, "title": "VIP client consultation", "start_at": "2025-08-25T14:00:00Z", "end_at": "2025-08-25T15:00:00Z", "location": "Office", "notes": "VIP client consultation"})
        ],
        outputs=["1397.02"]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "You need to execute estate management protocol for client 14 regarding property HTX007 (listing 7) at 1490000 with 6.9% 30-year financing. "
            "Deliver luxury estate services and schedule estate consultation on 2025-08-30T16:00:00Z-17:00:00Z at Office with 'Estate management strategy' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 14}),
            Action(name="get_listing_details", kwargs={"listing_id": 7}),
            Action(name="calculate_mortgage", kwargs={"principal": 1490000, "interest_rate": 6.9, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Estate Management", "type": "estate_management", "created_by": 3}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 14, "broker_id": 3, "property_id": "HTX007", "doc_type": "estate_portfolio"}),
            Action(name="send_email", kwargs={"client_id": 14, "broker_id": 3, "subject": "Luxury Estate Services", "template_code": "estate_management", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 14, "broker_id": 3, "title": "Estate management strategy", "start_at": "2025-08-30T16:00:00Z", "end_at": "2025-08-30T17:00:00Z", "location": "Office", "notes": "Estate management strategy"})
        ],
        outputs=["3532731.11"]
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "You need to execute first time buyer protocol for client 8 regarding property HTX008 (listing 8) at 330000 with 7.0% 30-year financing. "
            "Provide first-time buyer education and schedule education meeting on 2025-09-05T10:30:00Z-11:30:00Z at Office with 'First-time buyer education' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 8}),
            Action(name="get_listing_details", kwargs={"listing_id": 8}),
            Action(name="calculate_mortgage", kwargs={"principal": 330000, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "First Home Purchase", "type": "first_time_buyer", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 8, "broker_id": 2, "property_id": "HTX008", "doc_type": "buyer_education"}),
            Action(name="send_email", kwargs={"client_id": 8, "broker_id": 2, "subject": "First-Time Buyer Support", "template_code": "first_time_buyer", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 8, "broker_id": 2, "title": "First-time buyer education", "start_at": "2025-09-05T10:30:00Z", "end_at": "2025-09-05T11:30:00Z", "location": "Office", "notes": "First-time buyer education"})
        ],
        outputs=["460379.36"]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "You need to execute luxury marketing protocol for client 19 regarding property HTX009 (listing 9) at 400000 with 6.4% 30-year financing. "
            "Deliver premium luxury marketing and schedule luxury consultation on 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 19}),
            Action(name="get_listing_details", kwargs={"listing_id": 9}),
            Action(name="calculate_mortgage", kwargs={"principal": 400000, "interest_rate": 6.4, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 19, "broker_id": 4, "property_id": "HTX009", "doc_type": "luxury_package"}),
            Action(name="send_email", kwargs={"client_id": 19, "broker_id": 4, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 19, "broker_id": 4, "title": "Luxury property consultation", "start_at": "2025-09-10T13:00:00Z", "end_at": "2025-09-10T14:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["2502.02"]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "You need to execute investment consulting protocol for client 15 regarding property HTX010 (listing 10) at 458500 with 6.7% 30-year financing. "
            "Deliver strategic investment guidance and schedule investment meeting on 2025-09-15T11:00:00Z-12:00:00Z at Office with 'Investment strategy consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 15}),
            Action(name="get_listing_details", kwargs={"listing_id": 10}),
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
        annotator="0",
        user_id="task_091",
        instruction=(
            "You need to execute client onboarding protocol for client 1 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. "
            "Complete comprehensive client onboarding and schedule onboarding meeting on 2025-09-20T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 1}),
            Action(name="get_listing_details", kwargs={"listing_id": 1}),
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
        annotator="0",
        user_id="task_092",
        instruction=(
            "You need to execute luxury marketing protocol for client 2 regarding property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. "
            "Deliver premium luxury marketing and schedule luxury consultation on 2025-09-25T14:00:00Z-15:00:00Z at Office with 'Luxury property consultation' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 2}),
            Action(name="get_listing_details", kwargs={"listing_id": 2}),
            Action(name="calculate_mortgage", kwargs={"principal": 3975000, "interest_rate": 7.1, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Luxury Collection", "type": "luxury_marketing", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 2, "broker_id": 1, "property_id": "HTX002", "doc_type": "luxury_package"}),
            Action(name="send_email", kwargs={"client_id": 2, "broker_id": 1, "subject": "Premium Luxury Marketing", "template_code": "luxury_marketing", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 2, "broker_id": 1, "title": "Luxury property consultation", "start_at": "2025-09-25T14:00:00Z", "end_at": "2025-09-25T15:00:00Z", "location": "Office", "notes": "Luxury property consultation"})
        ],
        outputs=["26713.27"]
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction=(
            "You need to execute property evaluation protocol for client 3 regarding property HTX003 (listing 3) at 591000 with 6.6% 30-year financing. "
            "Provide comprehensive property analysis and schedule evaluation meeting on 2025-09-30T11:00:00Z-12:00:00Z at Office with 'Property evaluation consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 3}),
            Action(name="get_listing_details", kwargs={"listing_id": 3}),
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
        annotator="0",
        user_id="task_094",
        instruction=(
            "You need to execute commercial sales protocol for client 18 regarding property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. "
            "Target commercial property transaction and schedule commercial meeting on 2025-10-05T16:00:00Z-17:00:00Z at Office with 'Commercial transaction consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 18}),
            Action(name="get_listing_details", kwargs={"listing_id": 4}),
            Action(name="calculate_mortgage", kwargs={"principal": 705900, "interest_rate": 7.2, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Commercial Sales", "type": "commercial_sales", "created_by": 4}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 18, "broker_id": 4, "property_id": "HTX004", "doc_type": "commercial_analysis"}),
            Action(name="send_email", kwargs={"client_id": 18, "broker_id": 4, "subject": "Commercial Property Transaction", "template_code": "commercial_sales", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 18, "broker_id": 4, "title": "Commercial transaction consultation", "start_at": "2025-10-05T16:00:00Z", "end_at": "2025-10-05T17:00:00Z", "location": "Office", "notes": "Commercial transaction consultation"})
        ],
        outputs=["1019063.75"]
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction=(
            "You need to execute property showing protocol for client 5 regarding property HTX005 (listing 5) at 674900 with 6.8% 30-year financing. "
            "Coordinate exclusive property showing and schedule showing appointment on 2025-10-10T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 5}),
            Action(name="get_listing_details", kwargs={"listing_id": 5}),
            Action(name="calculate_mortgage", kwargs={"principal": 674900, "interest_rate": 6.8, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Property Showings", "type": "property_showing", "created_by": 1}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 5, "broker_id": 1, "property_id": "HTX005", "doc_type": "showing_package"}),
            Action(name="send_email", kwargs={"client_id": 5, "broker_id": 1, "subject": "Exclusive Property Showing", "template_code": "showing_invitation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 5, "broker_id": 1, "title": "Private property viewing", "start_at": "2025-10-10T15:30:00Z", "end_at": "2025-10-10T16:30:00Z", "location": "HTX005", "notes": "Private property viewing"})
        ],
        outputs=["4399.84"]
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
            "You need to execute relocation protocol for client 6 regarding property HTX006 (listing 6) at 225700 with 7.0% 30-year financing. "
            "Support client relocation with area analysis and schedule relocation meeting on 2025-10-15T09:00:00Z-10:00:00Z at Office with 'Relocation consultation' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 6}),
            Action(name="search_neighborhoods", kwargs={"city": "Houston"}),
            Action(name="get_listing_details", kwargs={"listing_id": 6}),
            Action(name="calculate_mortgage", kwargs={"principal": 225700, "interest_rate": 7.0, "loan_term_years": 30}),
            Action(name="create_campaign", kwargs={"name": "Relocation Services", "type": "relocation", "created_by": 2}),
            Action(name="generate_briefing_doc", kwargs={"client_id": 6, "broker_id": 2, "property_id": "HTX006", "doc_type": "relocation_guide"}),
            Action(name="send_email", kwargs={"client_id": 6, "broker_id": 2, "subject": "Comprehensive Relocation Services", "template_code": "relocation", "campaign_id": 101}),
            Action(name="create_calendar_event", kwargs={"client_id": 6, "broker_id": 2, "title": "Relocation consultation", "start_at": "2025-10-15T09:00:00Z", "end_at": "2025-10-15T10:00:00Z", "location": "Office", "notes": "Relocation consultation"})
        ],
        outputs=["540571.58"]
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
            "You need to execute portfolio review protocol for client 9 regarding property HTX007 (listing 7) at 1490000 with 6.4% 30-year financing. "
            "Deliver comprehensive portfolio assessment and schedule portfolio consultation on 2025-10-20T14:00:00Z-15:00:00Z at Office with 'Portfolio strategy review' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 9}),
            Action(name="get_listing_details", kwargs={"listing_id": 7}),
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
        annotator="0",
        user_id="task_098",
        instruction=(
            "You need to execute first time buyer protocol for client 12 regarding property HTX008 (listing 8) at 330000 with 6.6% 30-year financing. "
            "Provide first-time buyer education and schedule education meeting on 2025-10-25T10:30:00Z-11:30:00Z at Office with 'First-time buyer education' notes. "
            "Report the monthly payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 12}),
            Action(name="get_listing_details", kwargs={"listing_id": 8}),
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
        annotator="0",
        user_id="task_099",
        instruction=(
            "You need to execute market intelligence protocol for client 11 regarding property HTX009 (listing 9) at 400000 with 7.3% 30-year financing. "
            "Deliver quarterly market intelligence and schedule intelligence meeting on 2025-10-30T16:00:00Z-17:00:00Z at Office with 'Market intelligence briefing' notes. "
            "Report the total payment amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 11}),
            Action(name="get_listing_details", kwargs={"listing_id": 9}),
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
        annotator="0",
        user_id="task_100",
        instruction=(
            "You need to execute purchase support protocol for client 20 regarding property HTX010 (listing 10) at 458500 with 6.5% 30-year financing. "
            "Deliver comprehensive purchase analysis and schedule purchase meeting on 2025-11-05T11:00:00Z-12:00:00Z at Office with 'Purchase strategy consultation' notes. "
            "Report the total interest amount."
        ),
        actions=[
            Action(name="search_clients", kwargs={"client_id": 20}),
            Action(name="get_listing_details", kwargs={"listing_id": 10}),
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