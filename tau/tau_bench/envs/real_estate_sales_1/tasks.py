
tasks = [
    {
        "annotator": 0,
        "user_id": "task_001",
        "instruction": "Handle onboarding for new clients 4, 5, and 6 via broker 1 for property HTX003 (listing 3) at 591000 with 6.8% 30-year financing. Deliver comprehensive onboarding services with Premium Client Onboarding \u2014 Elite Segment campaign client_onboarding type by broker 1. Issue Welcome to Premium Real Estate Services communications using client_onboarding template with campaign_id 101. Organize consultations for clients 4 and 6 exclusively on 2024-11-20T10:00:00Z-11:00:00Z and 2024-11-20T14:00:00Z-15:00:00Z at Office with 'Premium client onboarding consultation' notes. Report the monthly payment figure.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Premium Client Onboarding — Elite Segment",
                    "type": "client_onboarding",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "subject": "Welcome to Premium Real Estate Services",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Welcome to Premium Real Estate Services",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 1,
                    "subject": "Welcome to Premium Real Estate Services",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 4,
                    "title": "Premium client onboarding consultation",
                    "start_at": "2024-11-20T10:00:00Z",
                    "end_at": "2024-11-20T11:00:00Z",
                    "location": "Office",
                    "notes": "Premium client onboarding consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 6,
                    "title": "Premium client onboarding consultation",
                    "start_at": "2024-11-20T14:00:00Z",
                    "end_at": "2024-11-20T15:00:00Z",
                    "location": "Office",
                    "notes": "Premium client onboarding consultation"
                }
            }
        ],
        "outputs": [
                "3852.88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_002",
        "instruction": "Coordinate LuxuryMarketingProtocol for clients 1, 2, and 3 via broker 2 targeting property HTX002 (listing 2) at 3975000 with 6.5% 30-year financing. Use campaign 'December Luxury Properties Showcase' luxury_marketing type by broker 2. Dispatch 'Exclusive Luxury Properties Available' emails using luxury_marketing template with campaign_id 101. Arrange consultations for clients 1 and 3 exclusively on 2024-12-02T14:00:00Z-15:00:00Z and 2024-12-02T15:30:00Z-16:30:00Z at Office with 'Luxury property investment consultation' notes. Report the total payment figure.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "December Luxury Properties Showcase",
                    "type": "luxury_marketing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 2,
                    "subject": "Exclusive Luxury Properties Available",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 2,
                    "subject": "Exclusive Luxury Properties Available",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 2,
                    "subject": "Exclusive Luxury Properties Available",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 1,
                    "title": "Luxury property investment consultation",
                    "start_at": "2024-12-02T14:00:00Z",
                    "end_at": "2024-12-02T15:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property investment consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 3,
                    "title": "Luxury property investment consultation",
                    "start_at": "2024-12-02T15:30:00Z",
                    "end_at": "2024-12-02T16:30:00Z",
                    "location": "Office",
                    "notes": "Luxury property investment consultation"
                }
            }
        ],
        "outputs": [
                "9044893.42"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_003",
        "instruction": "Handle PurchaseSupportProtocol for clients 7, 8, and 9 via broker 2, focusing on property HTX004 (listing 4) priced at 705900 with 7.0% 30-year financing. Utilize the campaign 'HTX004 Purchase Analysis \u2014 Premium Buyers' purchase_support type as facilitated by broker 2. Dispatch 'HTX004 Purchase Analysis Ready' emails applying the purchase_support template with campaign_id 101. Arrange consultations for clients 7 and 9 exclusively on 2024-12-01T10:00:00Z-11:00:00Z and 2024-12-01T14:00:00Z-15:00:00Z at Office accompanied by 'Review purchase analysis and financing' notes. Confirm the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "HTX004 Purchase Analysis — Premium Buyers",
                    "type": "purchase_support",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "HTX004 Purchase Analysis Ready",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "HTX004 Purchase Analysis Ready",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "HTX004 Purchase Analysis Ready",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 7,
                    "title": "Review purchase analysis and financing",
                    "start_at": "2024-12-01T10:00:00Z",
                    "end_at": "2024-12-01T11:00:00Z",
                    "location": "Office",
                    "notes": "Review purchase analysis and financing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 9,
                    "title": "Review purchase analysis and financing",
                    "start_at": "2024-12-01T14:00:00Z",
                    "end_at": "2024-12-01T15:00:00Z",
                    "location": "Office",
                    "notes": "Review purchase analysis and financing"
                }
            }
        ],
        "outputs": [
                "4696.37"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_004",
        "instruction": "Coordinate PropertyShowingProtocol for clients 10, 11, and 12 with broker 2, aiming at property HTX002 (listing 2) valued at 3975000 with 6.5% 30-year financing. Engage campaign 'HTX002 Elite Private Showings' property_showing type managed by broker 2. Issue 'Exclusive Property Showing Invitation' emails using the showing_invitation template with campaign_id 101. Plan showings for clients 10 and 12 alone on 2024-11-22T15:00:00Z-16:00:00Z and 2024-11-22T17:00:00Z-18:00:00Z at HTX002 with 'Private property showing' notes. Verify the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "HTX002 Elite Private Showings",
                    "type": "property_showing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "subject": "Exclusive Property Showing Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 2,
                    "subject": "Exclusive Property Showing Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 2,
                    "subject": "Exclusive Property Showing Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 10,
                    "title": "Private property showing",
                    "start_at": "2024-11-22T15:00:00Z",
                    "end_at": "2024-11-22T16:00:00Z",
                    "location": "HTX002",
                    "notes": "Private property showing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 12,
                    "title": "Private property showing",
                    "start_at": "2024-11-22T17:00:00Z",
                    "end_at": "2024-11-22T18:00:00Z",
                    "location": "HTX002",
                    "notes": "Private property showing"
                }
            }
        ],
        "outputs": [
                "5069893.42"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_005",
        "instruction": "Handle the distribution of quarterly market intelligence to clients 13, 14, and 15 via broker 1 concerning property HTX006 (listing 6) priced at 890000 with 6.9% financing over 30 years. Implement MarketIntelligenceProtocol using the November Market Intelligence Brief \u2014 Elite Segment and Q4 Market Intelligence Update communications. Organize strategic briefings for clients 13 and 15 on 2024-11-25 from 09:00-10:00 and 14:00-15:00. Summarize the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX006"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 890000,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "November Market Intelligence Brief — Elite Segment",
                    "type": "market_update",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 1,
                    "subject": "Q4 Market Intelligence Update",
                    "template_code": "market_update",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 1,
                    "subject": "Q4 Market Intelligence Update",
                    "template_code": "market_update",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 1,
                    "subject": "Q4 Market Intelligence Update",
                    "template_code": "market_update",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 13,
                    "title": "Market intelligence briefing",
                    "start_at": "2024-11-25T09:00:00Z",
                    "end_at": "2024-11-25T10:00:00Z",
                    "location": "Office",
                    "notes": "Market intelligence briefing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 15,
                    "title": "Market intelligence briefing",
                    "start_at": "2024-11-25T14:00:00Z",
                    "end_at": "2024-11-25T15:00:00Z",
                    "location": "Office",
                    "notes": "Market intelligence briefing"
                }
            }
        ],
        "outputs": [
                "2110154.82"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_006",
        "instruction": "Establish connections with investor clients 16, 17, and 18 via broker 3 focusing on property HTX005 (listing 5) valued at 1200000 with 7.2% 30-year financing. Conduct the Strategic Investment Opportunities \u2014 Q4 Edition campaign of investor_outreach type through broker 3. Deliver Investment Opportunity Analysis communications using the investor_outreach template associated with campaign_id 101. Arrange investment consultations for clients 16 and 18 exclusively on 2024-12-15T11:00:00Z-12:00:00Z and 2024-12-15T15:00:00Z-16:00:00Z at Office, including 'Investment opportunity consultation' notes. Calculate the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1200000,
                    "interest_rate": 7.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Strategic Investment Opportunities — Q4 Edition",
                    "type": "investor_outreach",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 3,
                    "subject": "Investment Opportunity Analysis",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 3,
                    "subject": "Investment Opportunity Analysis",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 3,
                    "subject": "Investment Opportunity Analysis",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 16,
                    "title": "Investment opportunity consultation",
                    "start_at": "2024-12-15T11:00:00Z",
                    "end_at": "2024-12-15T12:00:00Z",
                    "location": "Office",
                    "notes": "Investment opportunity consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 18,
                    "title": "Investment opportunity consultation",
                    "start_at": "2024-12-15T15:00:00Z",
                    "end_at": "2024-12-15T16:00:00Z",
                    "location": "Office",
                    "notes": "Investment opportunity consultation"
                }
            }
        ],
        "outputs": [
                "8145.46"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_007",
        "instruction": "Handle FirstTimeBuyerProtocol for clients 19, 20, and 1 via broker 4 targeting property HTX001 (listing 1) at 1500000 with 6.75% 30-year financing. Utilize campaign 'First Time Buyer Education Series', first_time_buyer type by broker 4. Dispatch 'Your First Home Purchase Guide' emails using first_time_buyer template with campaign_id 101. Plan education sessions for clients 19 and 1 only on 2024-12-10T09:30:00Z-10:30:00Z and 2024-12-10T14:30:00Z-15:30:00Z at Office including 'First-time buyer education session' notes. Document the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.75,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Time Buyer Education Series",
                    "type": "first_time_buyer",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "subject": "Your First Home Purchase Guide",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "subject": "Your First Home Purchase Guide",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 4,
                    "subject": "Your First Home Purchase Guide",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 19,
                    "title": "First-time buyer education session",
                    "start_at": "2024-12-10T09:30:00Z",
                    "end_at": "2024-12-10T10:30:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education session"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 1,
                    "title": "First-time buyer education session",
                    "start_at": "2024-12-10T14:30:00Z",
                    "end_at": "2024-12-10T15:30:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education session"
                }
            }
        ],
        "outputs": [
                "2002429.72"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_008",
        "instruction": "Coordinate PropertyEvaluationProtocol for clients 2, 3, and 4 with broker 5 targeting property HTX003 (listing 3) at 591000 with 6.8% financing over 30 years. Provide comprehensive market analysis through campaign Property Market Evaluation \u2014 December 2024 and Property Valuation Assessment communications. Calculate the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Market Evaluation — December 2024",
                    "type": "property_evaluation",
                    "created_by": 5
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 5
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 5
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 5,
                    "subject": "Property Valuation Assessment",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 5,
                    "subject": "Property Valuation Assessment",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 5,
                    "subject": "Property Valuation Assessment",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1387036.03"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_009",
        "instruction": "Handle VIP concierge services for clients 6, 7, and 8 through broker 2, focusing on property HTX002 (listing 2) priced at 3975000 with 6.5% 30-year financing. Initiate a 'VIP Concierge Services \u2014 Exclusive Properties' campaign and distribute 'Exclusive VIP Property Access' communications. Arrange VIP consultations with clients 6 and 8 exclusively on 2024-12-20T10:00:00Z-11:00:00Z and 2024-12-20T16:00:00Z-17:00:00Z at Office, including 'VIP property consultation' notes. Provide a report on the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "VIP Concierge Services — Exclusive Properties",
                    "type": "vip_service",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Exclusive VIP Property Access",
                    "template_code": "vip_service",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Exclusive VIP Property Access",
                    "template_code": "vip_service",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "Exclusive VIP Property Access",
                    "template_code": "vip_service",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "VIP property consultation",
                    "start_at": "2024-12-20T10:00:00Z",
                    "end_at": "2024-12-20T11:00:00Z",
                    "location": "Office",
                    "notes": "VIP property consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 8,
                    "title": "VIP property consultation",
                    "start_at": "2024-12-20T16:00:00Z",
                    "end_at": "2024-12-20T17:00:00Z",
                    "location": "Office",
                    "notes": "VIP property consultation"
                }
            }
        ],
        "outputs": [
                "25124.7"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_010",
        "instruction": "Conduct comprehensive market research delivery for clients 8, 9, and 10 via broker 7 with emphasis on Phoenix neighborhoods, particularly on property HTX004 (listing 4) costing 705900 with 7.0% financing over 30 years. Launch the Comprehensive Market Research \u2014 Phoenix Focus campaign and dispatch Regional Market Analysis communications. Schedule research consultations for clients 8 and 10 only on 2024-12-22T09:00:00Z-10:00:00Z and 2024-12-22T14:00:00Z-15:00:00Z at Office, accompanied by 'Market research consultation' notes. Deliver a report on the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "city": "Phoenix"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Comprehensive Market Research — Phoenix Focus",
                    "type": "market_analysis",
                    "created_by": 7
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 7
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 7
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 7
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 7,
                    "subject": "Regional Market Analysis",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 7,
                    "subject": "Regional Market Analysis",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 7,
                    "subject": "Regional Market Analysis",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 8,
                    "title": "Market research consultation",
                    "start_at": "2024-12-22T09:00:00Z",
                    "end_at": "2024-12-22T10:00:00Z",
                    "location": "Office",
                    "notes": "Market research consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 10,
                    "title": "Market research consultation",
                    "start_at": "2024-12-22T14:00:00Z",
                    "end_at": "2024-12-22T15:00:00Z",
                    "location": "Office",
                    "notes": "Market research consultation"
                }
            }
        ],
        "outputs": [
                "984793.31"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_011",
        "instruction": "Handle PortfolioReviewProtocol for clients 11, 12, and 13 via broker 8 targeting property HTX006 (listing 6) valued at 890000 with 6.6% 30-year financing. Utilize campaign 'Quarterly Portfolio Analysis \u2014 Q4 Review' portfolio_review type by broker 8. Dispatch 'Portfolio Performance Update' emails using portfolio_review template with campaign_id 101. Plan portfolio consultations for clients 11 and 13 exclusively on 2024-12-28T10:30:00Z-11:30:00Z and 2024-12-28T15:30:00Z-16:30:00Z at Office with 'Portfolio performance consultation' notes. Provide a report on the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX006"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 890000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Quarterly Portfolio Analysis — Q4 Review",
                    "type": "portfolio_review",
                    "created_by": 8
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 8
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 8
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 8
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 8,
                    "subject": "Portfolio Performance Update",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 8,
                    "subject": "Portfolio Performance Update",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 8,
                    "subject": "Portfolio Performance Update",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 11,
                    "title": "Portfolio performance consultation",
                    "start_at": "2024-12-28T10:30:00Z",
                    "end_at": "2024-12-28T11:30:00Z",
                    "location": "Office",
                    "notes": "Portfolio performance consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 13,
                    "title": "Portfolio performance consultation",
                    "start_at": "2024-12-28T15:30:00Z",
                    "end_at": "2024-12-28T16:30:00Z",
                    "location": "Office",
                    "notes": "Portfolio performance consultation"
                }
            }
        ],
        "outputs": [
                "5684.06"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_012",
        "instruction": "Conduct CommercialSalesProtocol for clients 14, 15, and 16 via broker 9 targeting property HTX002 (listing 2) priced at 3975000 with 7.1% 30-year financing. Employ campaign 'Commercial Property Specialists \u2014 Elite Division' commercial_sales type by broker 9. Send out 'Commercial Investment Opportunity' emails using commercial_sales template with campaign_id 101. Arrange commercial consultations for clients 14 and 16 exclusively on 2025-01-05T09:15:00Z-10:15:00Z and 2025-01-05T14:15:00Z-15:15:00Z at Office with 'Commercial property consultation' notes. Communicate the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Property Specialists — Elite Division",
                    "type": "commercial_sales",
                    "created_by": 9
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 9
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 9
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 9,
                    "subject": "Commercial Investment Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 9,
                    "subject": "Commercial Investment Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 9,
                    "subject": "Commercial Investment Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 14,
                    "title": "Commercial property consultation",
                    "start_at": "2025-01-05T09:15:00Z",
                    "end_at": "2025-01-05T10:15:00Z",
                    "location": "Office",
                    "notes": "Commercial property consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 16,
                    "title": "Commercial property consultation",
                    "start_at": "2025-01-05T14:15:00Z",
                    "end_at": "2025-01-05T15:15:00Z",
                    "location": "Office",
                    "notes": "Commercial property consultation"
                }
            }
        ],
        "outputs": [
                "26713.27"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_013",
        "instruction": "Handle RelocationProtocol for clients 17, 18, and 19 through broker 10, focusing on Phoenix neighborhoods and property HTX001 (listing 1) at 1500000 with 6.9% financing over 30 years. Utilize the campaign 'Executive Relocation Services \u2014 Phoenix Gateway' for relocation type as facilitated by broker 10. Dispatch 'Phoenix Relocation Guide' emails using the relocation template with campaign_id 101. Arrange relocation consultations exclusively for clients 17 and 19 on 2025-01-10T11:00:00Z-12:00:00Z and 2025-01-10T16:00:00Z-17:00:00Z at Office, annotating 'Executive relocation consultation' notes. Summarize the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "city": "Phoenix"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Executive Relocation Services — Phoenix Gateway",
                    "type": "relocation",
                    "created_by": 10
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 10
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 10
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 10
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "Phoenix Relocation Guide",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 10,
                    "subject": "Phoenix Relocation Guide",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 10,
                    "subject": "Phoenix Relocation Guide",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 10,
                    "client_id": 17,
                    "title": "Executive relocation consultation",
                    "start_at": "2025-01-10T11:00:00Z",
                    "end_at": "2025-01-10T12:00:00Z",
                    "location": "Office",
                    "notes": "Executive relocation consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 10,
                    "client_id": 19,
                    "title": "Executive relocation consultation",
                    "start_at": "2025-01-10T16:00:00Z",
                    "end_at": "2025-01-10T17:00:00Z",
                    "location": "Office",
                    "notes": "Executive relocation consultation"
                }
            }
        ],
        "outputs": [
                "2056440.72"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_014",
        "instruction": "Coordinate InvestmentConsultingProtocol for clients 20, 1, and 2 through broker 11, concentrating on property HTX004 (listing 4) at 705900 with 6.7% financing over 30 years. Implement the campaign 'Strategic Investment Advisory \u2014 Premium Services' for investment_consulting type conducted by broker 11. Forward 'Investment Strategy Analysis' emails using the investment_consulting template with campaign_id 101. Detail the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Strategic Investment Advisory — Premium Services",
                    "type": "investment_consulting",
                    "created_by": 11
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 11
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 11
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 11
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Investment Strategy Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 11,
                    "subject": "Investment Strategy Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 11,
                    "subject": "Investment Strategy Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1639806.21"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_015",
        "instruction": "Handle EstateManagementProtocol for clients 3, 4, and 5 via broker 12, focusing on property HTX005 (listing 5) priced at 1200000 with 6.8% 30-year financing. Utilize the 'Luxury Estate Management \u2014 Concierge Collection' estate_management strategy by broker 12. Dispatch 'Estate Portfolio Review' emails using the estate_management template associated with campaign_id 101. Arrange estate consultations for clients 3 and 5 exclusively on 2025-01-15T10:00:00Z-11:00:00Z and 2025-01-15T15:00:00Z-16:00:00Z at Office with notes on 'Luxury estate consultation'. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1200000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Estate Management — Concierge Collection",
                    "type": "estate_management",
                    "created_by": 12
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 12
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 12
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 12
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 12,
                    "subject": "Estate Portfolio Review",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 12,
                    "subject": "Estate Portfolio Review",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 12,
                    "subject": "Estate Portfolio Review",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 3,
                    "title": "Luxury estate consultation",
                    "start_at": "2025-01-15T10:00:00Z",
                    "end_at": "2025-01-15T11:00:00Z",
                    "location": "Office",
                    "notes": "Luxury estate consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 5,
                    "title": "Luxury estate consultation",
                    "start_at": "2025-01-15T15:00:00Z",
                    "end_at": "2025-01-15T16:00:00Z",
                    "location": "Office",
                    "notes": "Luxury estate consultation"
                }
            }
        ],
        "outputs": [
                "7823.1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_016",
        "instruction": "You are required to bring new clients 6, 7, and 8 onboard through broker 1 for property HTX001 (listing 1) valued at 1500000 with 6.4% 30-year financing. Deliver comprehensive onboarding services utilizing the Elite Client Onboarding \u2014 Winter Collection campaign client_onboarding type by broker 1. Provide Welcome to Elite Real Estate Services communications using the client_onboarding template linked to campaign_id 101. Schedule onboarding consultations for clients 6 and 8 exclusively on 2025-01-20T09:00:00Z-10:00:00Z and 2025-01-20T14:00:00Z-15:00:00Z at Office with notes on 'Elite client onboarding session'. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Elite Client Onboarding — Winter Collection",
                    "type": "client_onboarding",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 1,
                    "subject": "Welcome to Elite Real Estate Services",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 1,
                    "subject": "Welcome to Elite Real Estate Services",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 1,
                    "subject": "Welcome to Elite Real Estate Services",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 6,
                    "title": "Elite client onboarding session",
                    "start_at": "2025-01-20T09:00:00Z",
                    "end_at": "2025-01-20T10:00:00Z",
                    "location": "Office",
                    "notes": "Elite client onboarding session"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 8,
                    "title": "Elite client onboarding session",
                    "start_at": "2025-01-20T14:00:00Z",
                    "end_at": "2025-01-20T15:00:00Z",
                    "location": "Office",
                    "notes": "Elite client onboarding session"
                }
            }
        ],
        "outputs": [
                "9382.59"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_017",
        "instruction": "Handle the delivery of luxury marketing services to clients 9, 10, and 11 via broker 2, focusing on property HTX006 (listing 6) priced at 890000 with 6.3% 30-year financing. Develop the Luxury Properties \u2014 Exclusive Winter Showcase campaign under the luxury_marketing category by broker 2. Dispatch Exclusive Winter Property Collection communications utilizing the luxury_marketing template with campaign_id 101. Organize luxury consultations for clients 9 and 11 exclusively on 2025-01-22T11:00:00Z-12:00:00Z and 2025-01-22T16:00:00Z-17:00:00Z at the Office including 'Luxury property showcase consultation' notes. Submit a report detailing the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 890000,
                    "interest_rate": 6.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Properties — Exclusive Winter Showcase",
                    "type": "luxury_marketing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Exclusive Winter Property Collection",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "subject": "Exclusive Winter Property Collection",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 2,
                    "subject": "Exclusive Winter Property Collection",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 9,
                    "title": "Luxury property showcase consultation",
                    "start_at": "2025-01-22T11:00:00Z",
                    "end_at": "2025-01-22T12:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property showcase consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 11,
                    "title": "Luxury property showcase consultation",
                    "start_at": "2025-01-22T16:00:00Z",
                    "end_at": "2025-01-22T17:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property showcase consultation"
                }
            }
        ],
        "outputs": [
                "1983188.82"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_018",
        "instruction": "Arrange purchase support for clients 12, 13, and 14 via broker 3 concerning property HTX005 (listing 5) priced at 1200000 with 6.6% 30-year financing. Initiate the HTX005 Purchase Analysis \u2014 Strategic Buyers campaign and issue HTX005 Purchase Support Ready communications. Schedule purchase consultations for clients 12 and 14 exclusively on 2025-01-25T10:00:00Z-11:00:00Z and 2025-01-25T15:00:00Z-16:00:00Z at the Office incorporating 'Purchase analysis consultation' notes. Document the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1200000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "HTX005 Purchase Analysis — Strategic Buyers",
                    "type": "purchase_support",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "HTX005 Purchase Support Ready",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "subject": "HTX005 Purchase Support Ready",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "HTX005 Purchase Support Ready",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Purchase analysis consultation",
                    "start_at": "2025-01-25T10:00:00Z",
                    "end_at": "2025-01-25T11:00:00Z",
                    "location": "Office",
                    "notes": "Purchase analysis consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 14,
                    "title": "Purchase analysis consultation",
                    "start_at": "2025-01-25T15:00:00Z",
                    "end_at": "2025-01-25T16:00:00Z",
                    "location": "Office",
                    "notes": "Purchase analysis consultation"
                }
            }
        ],
        "outputs": [
                "7663.91"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_019",
        "instruction": "Coordinate exclusive property showings for clients 15, 16, and 17 through broker 4 for property HTX003 (listing 3) priced at 591000 with 6.7% 30-year financing. Initiate the HTX003 Elite Property Showings campaign and distribute Exclusive Property Access Invitation communications. Arrange property showings for clients 15 and 17 exclusively on 2025-01-28T13:00:00Z-14:00:00Z and 2025-01-28T16:00:00Z-17:00:00Z at HTX003, including 'Exclusive property showcase' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "HTX003 Elite Property Showings",
                    "type": "property_showing",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 4,
                    "subject": "Exclusive Property Access Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "subject": "Exclusive Property Access Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "subject": "Exclusive Property Access Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 15,
                    "title": "Exclusive property showcase",
                    "start_at": "2025-01-28T13:00:00Z",
                    "end_at": "2025-01-28T14:00:00Z",
                    "location": "HTX003",
                    "notes": "Exclusive property showcase"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 17,
                    "title": "Exclusive property showcase",
                    "start_at": "2025-01-28T16:00:00Z",
                    "end_at": "2025-01-28T17:00:00Z",
                    "location": "HTX003",
                    "notes": "Exclusive property showcase"
                }
            }
        ],
        "outputs": [
                "781893.43"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_020",
        "instruction": "Deliver quarterly market intelligence to clients 18, 19, and 20 via broker 5 concerning property HTX004 (listing 4) priced at 705900 with 6.5% 30-year financing. Launch the Q1 Market Intelligence \u2014 Strategic Insights campaign and issue Q1 Market Intelligence Brief communications. Plan market briefings for clients 18 and 20 exclusively on 2025-01-30T09:30:00Z-10:30:00Z and 2025-01-30T14:30:00Z-15:30:00Z at Office with 'Strategic market intelligence briefing' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Q1 Market Intelligence — Strategic Insights",
                    "type": "market_update",
                    "created_by": 5
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 5
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 5
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Q1 Market Intelligence Brief",
                    "template_code": "market_update",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 5,
                    "subject": "Q1 Market Intelligence Brief",
                    "template_code": "market_update",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 5,
                    "subject": "Q1 Market Intelligence Brief",
                    "template_code": "market_update",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Strategic market intelligence briefing",
                    "start_at": "2025-01-30T09:30:00Z",
                    "end_at": "2025-01-30T10:30:00Z",
                    "location": "Office",
                    "notes": "Strategic market intelligence briefing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 20,
                    "title": "Strategic market intelligence briefing",
                    "start_at": "2025-01-30T14:30:00Z",
                    "end_at": "2025-01-30T15:30:00Z",
                    "location": "Office",
                    "notes": "Strategic market intelligence briefing"
                }
            }
        ],
        "outputs": [
                "1606236.54"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_021",
        "instruction": "Handle support for high-value investor clients 1, 2, and 3 via broker 1 concerning property HTX002 (listing 2) at 2500000 with 6.1% 30-year financing. Provide comprehensive investor outreach services with Elite Investor Outreach \u2014 Q1 Initiative and Exclusive Investment Opportunity communications. Coordinate investment consultations exclusively for clients 1 and 3 on 2025-02-05T10:00:00Z-11:00:00Z and 2025-02-05T15:00:00Z-16:00:00Z at Office with 'High-value investment consultation' notes. Share the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX002"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 2500000,
                    "interest_rate": 6.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Elite Investor Outreach — Q1 Initiative",
                    "type": "investor_outreach",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "Exclusive Investment Opportunity",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "Exclusive Investment Opportunity",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Exclusive Investment Opportunity",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 1,
                    "title": "High-value investment consultation",
                    "start_at": "2025-02-05T10:00:00Z",
                    "end_at": "2025-02-05T11:00:00Z",
                    "location": "Office",
                    "notes": "High-value investment consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "High-value investment consultation",
                    "start_at": "2025-02-05T15:00:00Z",
                    "end_at": "2025-02-05T16:00:00Z",
                    "location": "Office",
                    "notes": "High-value investment consultation"
                }
            }
        ],
        "outputs": [
                "15149.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_022",
        "instruction": "Handle first-time buyer education for clients 4, 5, and 6 via broker 7 with a focus on property HTX004 (listing 4) at 650000 with 6.8% 30-year financing. Offer First-Time Buyer Education \u2014 Spring Series campaign and Your Home Buying Journey communications. Organize education sessions solely for clients 4 and 6 on 2025-02-08T09:00:00Z-10:00:00Z and 2025-02-08T14:00:00Z-15:00:00Z at Office with 'First-time buyer education session' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 650000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First-Time Buyer Education — Spring Series",
                    "type": "first_time_buyer",
                    "created_by": 7
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 7
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 7
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 7
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 7,
                    "subject": "Your Home Buying Journey",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 7,
                    "subject": "Your Home Buying Journey",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 7,
                    "subject": "Your Home Buying Journey",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 4,
                    "title": "First-time buyer education session",
                    "start_at": "2025-02-08T09:00:00Z",
                    "end_at": "2025-02-08T10:00:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education session"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 6,
                    "title": "First-time buyer education session",
                    "start_at": "2025-02-08T14:00:00Z",
                    "end_at": "2025-02-08T15:00:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education session"
                }
            }
        ],
        "outputs": [
                "1525504.94"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_023",
        "instruction": "Handle the delivery of comprehensive property evaluations for clients 7, 8, and 9 via broker 8 for property HTX006 (listing 6) priced at 980000 with a 6.9% 30-year financing option. Develop the HTX006 Market Evaluation \u2014 Professional Assessment campaign and the Property Analysis Report communications. Arrange evaluation consultations for clients 7 and 9 only on 2025-02-12T11:00:00Z-12:00:00Z and 2025-02-12T16:00:00Z-17:00:00Z at Office, including 'Property evaluation consultation' notes. Determine the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX006"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 980000,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "HTX006 Market Evaluation — Professional Assessment",
                    "type": "property_evaluation",
                    "created_by": 8
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 8
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 8
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 8
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 8,
                    "subject": "Property Analysis Report",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 8,
                    "subject": "Property Analysis Report",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 8,
                    "subject": "Property Analysis Report",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 7,
                    "title": "Property evaluation consultation",
                    "start_at": "2025-02-12T11:00:00Z",
                    "end_at": "2025-02-12T12:00:00Z",
                    "location": "Office",
                    "notes": "Property evaluation consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 9,
                    "title": "Property evaluation consultation",
                    "start_at": "2025-02-12T16:00:00Z",
                    "end_at": "2025-02-12T17:00:00Z",
                    "location": "Office",
                    "notes": "Property evaluation consultation"
                }
            }
        ],
        "outputs": [
                "6454.28"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_024",
        "instruction": "Coordinate the provision of VIP concierge services to clients 10, 11, and 12 through broker 9, focusing on property HTX001 (listing 1) valued at 1800000 with a 6.2% 30-year financing arrangement. Establish the VIP Concierge Services \u2014 Elite Experience campaign and the Exclusive VIP Property Services communications. Plan VIP consultations for clients 10 and 12 only on 2025-02-15T13:00:00Z-14:00:00Z and 2025-02-15T17:00:00Z-18:00:00Z at Office, accompanied by 'VIP concierge consultation' notes. Calculate the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1800000,
                    "interest_rate": 6.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "VIP Concierge Services — Elite Experience",
                    "type": "vip_service",
                    "created_by": 9
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 9
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 9
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 9,
                    "subject": "Exclusive VIP Property Services",
                    "template_code": "vip_service",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 9,
                    "subject": "Exclusive VIP Property Services",
                    "template_code": "vip_service",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 9,
                    "subject": "Exclusive VIP Property Services",
                    "template_code": "vip_service",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 10,
                    "title": "VIP concierge consultation",
                    "start_at": "2025-02-15T13:00:00Z",
                    "end_at": "2025-02-15T14:00:00Z",
                    "location": "Office",
                    "notes": "VIP concierge consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 12,
                    "title": "VIP concierge consultation",
                    "start_at": "2025-02-15T17:00:00Z",
                    "end_at": "2025-02-15T18:00:00Z",
                    "location": "Office",
                    "notes": "VIP concierge consultation"
                }
            }
        ],
        "outputs": [
                "2168798.97"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_025",
        "instruction": "Handle the provision of comprehensive market analysis for clients 13, 14, and 15 through broker 3 concerning Phoenix neighborhoods, concentrating on property HTX005 (listing 5) valued at 550000 with a financing option of 7.0% over 30 years. Present Phoenix Market Analysis \u2014 Q1 Comprehensive Study campaign along with Regional Market Intelligence communications. Coordinate analysis briefings specifically for clients 13 and 15 on 2025-02-18T10:30:00Z-11:30:00Z and 2025-02-18T15:30:00Z-16:30:00Z at Office including 'Market analysis briefing' notes. Calculate and report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "city": "Phoenix"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 550000,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Phoenix Market Analysis — Q1 Comprehensive Study",
                    "type": "market_analysis",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "subject": "Regional Market Intelligence",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Regional Market Intelligence",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "subject": "Regional Market Intelligence",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 13,
                    "title": "Market analysis briefing",
                    "start_at": "2025-02-18T10:30:00Z",
                    "end_at": "2025-02-18T11:30:00Z",
                    "location": "Office",
                    "notes": "Market analysis briefing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 15,
                    "title": "Market analysis briefing",
                    "start_at": "2025-02-18T15:30:00Z",
                    "end_at": "2025-02-18T16:30:00Z",
                    "location": "Office",
                    "notes": "Market analysis briefing"
                }
            }
        ],
        "outputs": [
                "1317298.94"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_026",
        "instruction": "Handle comprehensive relocation services for clients 16, 17, and 18 through broker 11 focusing on property HTX003 (listing 3) priced at 591000 with 7.3% financing over 30 years. Deliver the Executive Relocation \u2014 Phoenix Elite Program campaign relocation type with the assistance of broker 11. Send out Phoenix Relocation Package communications to all three clients utilizing the relocation template tagged with campaign_id 101. Schedule relocation meetings exclusively for clients 16 and 18 on 2025-03-01T09:30:00Z-10:30:00Z and 2025-03-01T15:30:00Z-16:30:00Z at Office, incorporating 'Executive relocation planning' notes. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 7.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Executive Relocation — Phoenix Elite Program",
                    "type": "relocation",
                    "created_by": 11
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 11
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 11
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 11
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 11,
                    "subject": "Phoenix Relocation Package",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 11,
                    "subject": "Phoenix Relocation Package",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 11,
                    "subject": "Phoenix Relocation Package",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 16,
                    "title": "Executive relocation planning",
                    "start_at": "2025-03-01T09:30:00Z",
                    "end_at": "2025-03-01T10:30:00Z",
                    "location": "Office",
                    "notes": "Executive relocation planning"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 18,
                    "title": "Executive relocation planning",
                    "start_at": "2025-03-01T15:30:00Z",
                    "end_at": "2025-03-01T16:30:00Z",
                    "location": "Office",
                    "notes": "Executive relocation planning"
                }
            }
        ],
        "outputs": [
                "4051.72"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_027",
        "instruction": "Handle the provision of investment consulting services to clients 19, 20, and 1 via broker 12, focusing on property HTX006 (listing 6) at 890000 with 7.4% 30-year financing. Coordinate the creation of the Strategic Investment Portfolio \u2014 Premium Advisory campaign, investment_consulting type, by broker 12. Dispatch Investment Portfolio Analysis communications utilizing the investment_consulting template with campaign_id 101. Arrange investment reviews for clients 19 and 1 exclusively on 2025-03-05T11:00:00Z-12:00:00Z and 2025-03-05T16:00:00Z-17:00:00Z at Office, including 'Investment portfolio consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX006"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 890000,
                    "interest_rate": 7.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Strategic Investment Portfolio — Premium Advisory",
                    "type": "investment_consulting",
                    "created_by": 12
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 12
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 12
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 12
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 12,
                    "subject": "Investment Portfolio Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 12,
                    "subject": "Investment Portfolio Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 12,
                    "subject": "Investment Portfolio Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 19,
                    "title": "Investment portfolio consultation",
                    "start_at": "2025-03-05T11:00:00Z",
                    "end_at": "2025-03-05T12:00:00Z",
                    "location": "Office",
                    "notes": "Investment portfolio consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 1,
                    "title": "Investment portfolio consultation",
                    "start_at": "2025-03-05T16:00:00Z",
                    "end_at": "2025-03-05T17:00:00Z",
                    "location": "Office",
                    "notes": "Investment portfolio consultation"
                }
            }
        ],
        "outputs": [
                "1328384.88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_028",
        "instruction": "Handle support for commercial property acquisition for clients 2, 3, and 4 through broker 1 concerning property HTX004 (listing 4) at 705900 with 7.5% 30-year financing. Coordinate the delivery of the Commercial Real Estate \u2014 Elite Business Division campaign, commercial_sales type, by broker 1. Dispatch Commercial Property Opportunity communications using the commercial_sales template with campaign_id 101. Schedule business meetings for clients 2 and 4 exclusively on 2025-03-08T10:15:00Z-11:15:00Z and 2025-03-08T14:15:00Z-15:15:00Z at Office, including 'Commercial property strategy meeting' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Real Estate — Elite Business Division",
                    "type": "commercial_sales",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "Commercial Property Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Commercial Property Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "subject": "Commercial Property Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 2,
                    "title": "Commercial property strategy meeting",
                    "start_at": "2025-03-08T10:15:00Z",
                    "end_at": "2025-03-08T11:15:00Z",
                    "location": "Office",
                    "notes": "Commercial property strategy meeting"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 4,
                    "title": "Commercial property strategy meeting",
                    "start_at": "2025-03-08T14:15:00Z",
                    "end_at": "2025-03-08T15:15:00Z",
                    "location": "Office",
                    "notes": "Commercial property strategy meeting"
                }
            }
        ],
        "outputs": [
                "1776871.88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_029",
        "instruction": "Handle the provision of portfolio review services for clients 5, 6, and 7 through broker 2 related to property HTX002 (listing 2) at 2500000 with 7.6% 30-year financing. Establish Elite Portfolio Management \u2014 Q1 Review campaign of portfolio_review type via broker 2. Dispatch Quarterly Portfolio Assessment communications utilizing the portfolio_review template with campaign_id 101. Schedule the portfolio reviews exclusively for clients 5 and 7 on 2025-03-12T09:45:00Z-10:45:00Z and 2025-03-12T15:45:00Z-16:45:00Z at Office, incorporating 'Portfolio performance review' notes. Report on the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX002"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 2500000,
                    "interest_rate": 7.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Elite Portfolio Management — Q1 Review",
                    "type": "portfolio_review",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 2,
                    "subject": "Quarterly Portfolio Assessment",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Quarterly Portfolio Assessment",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Quarterly Portfolio Assessment",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 5,
                    "title": "Portfolio performance review",
                    "start_at": "2025-03-12T09:45:00Z",
                    "end_at": "2025-03-12T10:45:00Z",
                    "location": "Office",
                    "notes": "Portfolio performance review"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 7,
                    "title": "Portfolio performance review",
                    "start_at": "2025-03-12T15:45:00Z",
                    "end_at": "2025-03-12T16:45:00Z",
                    "location": "Office",
                    "notes": "Portfolio performance review"
                }
            }
        ],
        "outputs": [
                "17651.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_030",
        "instruction": "Handle estate management services for clients 8, 9, and 10 through broker 3, concentrating on property HTX001 (listing 1) at 1500000 with 7.7% 30-year financing. Initiate Luxury Estate Services \u2014 Premium Collection campaign of estate_management type conducted by broker 3. Dispatch Estate Management Portfolio communications through estate_management template with campaign_id 101. Arrange estate consultations for clients 8 and 10 only on 2025-03-15T08:30:00Z-09:30:00Z and 2025-03-15T13:30:00Z-14:30:00Z at Office, including 'Estate management consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 7.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Estate Services — Premium Collection",
                    "type": "estate_management",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 3,
                    "subject": "Estate Management Portfolio",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 3,
                    "subject": "Estate Management Portfolio",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 3,
                    "subject": "Estate Management Portfolio",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 8,
                    "title": "Estate management consultation",
                    "start_at": "2025-03-15T08:30:00Z",
                    "end_at": "2025-03-15T09:30:00Z",
                    "location": "Office",
                    "notes": "Estate management consultation"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 10,
                    "title": "Estate management consultation",
                    "start_at": "2025-03-15T13:30:00Z",
                    "end_at": "2025-03-15T14:30:00Z",
                    "location": "Office",
                    "notes": "Estate management consultation"
                }
            }
        ],
        "outputs": [
                "2349984.94"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_031",
        "instruction": "Handle the basic property analysis for client 11 concerning property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. Dispatch the Property Analysis Update communication using the property_evaluation template with campaign_id 101. Indicate the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Analysis",
                    "type": "property_evaluation",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "subject": "Property Analysis Update",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "9481.02"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_032",
        "instruction": "Organize the property showing for client 14 related to property HTX003 (listing 3) at 591000 with 7.1% 30-year financing. Send out the Property Showing Invitation communication utilizing the showing_invitation template with campaign_id 101. Specify the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Showings",
                    "type": "property_showing",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Property Showing Invitation",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "838815.20"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_033",
        "instruction": "Handle initial buyer assistance for client 17 concerning property HTX005 (listing 5) priced at 674900 with 6.8% 30-year financing. Offer thorough first-time buyer education and arrange the educational session on 2025-03-10T14:00:00Z-15:00:00Z at Office, including 'First-time buyer education session' notes. Summarize the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "property_id": "HTX005",
                    "doc_type": "buyer_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "subject": "First-Time Buyer Support",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "title": "First-time buyer education session",
                    "start_at": "2025-03-10T14:00:00Z",
                    "end_at": "2025-03-10T15:00:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education session"
                }
            }
        ],
        "outputs": [
                "1583943.51"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_034",
        "instruction": "Coordinate luxury marketing services for client 20 in relation to property HTX002 (listing 2) costing 3975000 with 6.3% 30-year financing. Dispatch Exclusive Luxury Collection communication using the luxury_marketing template with campaign_id 101. Calculate the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "subject": "Exclusive Luxury Collection",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "24604.17"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_035",
        "instruction": "Handle investor engagement for client 3 concerning property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. Dispatch Investment Opportunity Brief communication using the investor_outreach template with campaign_id 101. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Opportunities",
                    "type": "investor_outreach",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX004",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Investment Opportunity Brief",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1019063.75"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_036",
        "instruction": "Assist client 5 with first-time buyer support concerning property HTX002 (listing 2) at 3975000 with 6.9% 30-year financing. Send out the Welcome Package communication using the first_time_buyer template with campaign_id 101. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Welcome Package",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "26179.36"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_037",
        "instruction": "Coordinate a property viewing for client 8 related to property HTX001 (listing 1) priced at 1500000 with 7.0% 30-year financing. Arrange a private property viewing on 2025-03-15T15:00:00Z-16:00:00Z at HTX001 with notes 'Private property showing'. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Showings",
                    "type": "property_showing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "property_id": "HTX001",
                    "doc_type": "showing_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "Exclusive Property Showing",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "title": "Private property showing",
                    "start_at": "2025-03-15T15:00:00Z",
                    "end_at": "2025-03-15T16:00:00Z",
                    "location": "HTX001",
                    "notes": "Private property showing"
                }
            }
        ],
        "outputs": [
                "2092633.47"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_038",
        "instruction": "Handle the provision of luxury marketing services for client 13 concerning property HTX005 (listing 5) valued at 674900 with 6.6% 30-year financing. Dispatch Exclusive VIP Access communication utilizing the luxury_marketing template with campaign_id 101. Organize a VIP consultation on 2025-05-05T14:00:00Z-15:00:00Z at Office with notes 'VIP client consultation'. Determine and report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "subject": "Exclusive VIP Access",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "title": "VIP client consultation",
                    "start_at": "2025-05-05T14:00:00Z",
                    "end_at": "2025-05-05T15:00:00Z",
                    "location": "Office",
                    "notes": "VIP client consultation"
                }
            }
        ],
        "outputs": [
                "4310.31"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_039",
        "instruction": "Handle the property evaluation protocol for client 18 related to property HTX003 (listing 3) priced at 591000 with a 7.3% 30-year financing option. Use the property_evaluation template to send the Property Evaluation Report communication with campaign_id 101. Report on the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 7.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Analysis",
                    "type": "property_evaluation",
                    "created_by": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "subject": "Property Evaluation Report",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1458620.71"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_040",
        "instruction": "Assist with investor outreach for client 6 concerning property HTX006 (listing 6) valued at 225700 with a 6.4% 30-year financing rate. Utilize the investor_outreach template to send the Investment Opportunity Brief communication with campaign_id 101. Provide details on the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX006"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Opportunities",
                    "type": "investor_outreach",
                    "created_by": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Investment Opportunity Brief",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "282536.06"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_041",
        "instruction": "Handle the relocation protocol for client 9 concerning property HTX001 (listing 1) priced at 1500000 with a 6.8% 30-year mortgage. Dispatch the Relocation Guide communication utilizing the relocation template with campaign_id 101. Provide the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Relocation Services",
                    "type": "relocation",
                    "created_by": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Relocation Guide",
                    "template_code": "relocation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "9778.88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_042",
        "instruction": "Coordinate commercial sales services for client 14 relevant to property HTX002 (listing 2) priced at 3975000 with a 7.1% 30-year mortgage. Issue the Commercial Investment Opportunity communication using the commercial_sales template with campaign_id 101. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Sales",
                    "type": "commercial_sales",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "property_id": "HTX002",
                    "doc_type": "commercial_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Commercial Investment Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "5641777.34"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_043",
        "instruction": "Handle the estate management protocol for client 17 concerning property HTX003 (listing 3) at 591000 with 6.5% 30-year financing. Utilize the estate_management template to send Estate Services communication with campaign_id 101. Compute the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Estate Management",
                    "type": "estate_management",
                    "created_by": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "subject": "Estate Services",
                    "template_code": "estate_management",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1344787.93"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_044",
        "instruction": "Coordinate the investment consulting protocol for client 12 regarding property HTX004 (listing 4) at 705900 with 7.0% 30-year financing. Employ the investment_consulting template to send Investment Strategy communication with campaign_id 101. Calculate the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Consulting",
                    "type": "investment_consulting",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Investment Strategy",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "984793.31"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_045",
        "instruction": "Handle the market analysis protocol for client 7 regarding property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. Dispatch the Market Insights communication using the market_analysis template with campaign_id 101. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Market Intelligence",
                    "type": "market_analysis",
                    "created_by": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Market Insights",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "4444.89"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_046",
        "instruction": "Coordinate the portfolio review protocol for client 15 regarding property HTX002 (listing 2) at 3975000 with 7.2% 30-year financing. Send the Portfolio Review communication using the portfolio_review template with campaign_id 101. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX002"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 7.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Portfolio Review",
                    "type": "portfolio_review",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "subject": "Comprehensive Portfolio Assessment",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "5738459.28"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_047",
        "instruction": "Handle the VIP client protocol for client 11 concerning property HTX003 (listing 3) priced at 591000 with 6.7% 30-year financing. Dispatch VIP Services communication utilizing the vip_client template with campaign_id 101. Detail the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "VIP Client Services",
                    "type": "vip_client",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "subject": "VIP Services",
                    "template_code": "vip_client",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "3813.59"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_048",
        "instruction": "Coordinate the client onboarding protocol for client 4 in relation to property HTX004 (listing 4) valued at 705900 with 6.6% 30-year financing. Forward the Welcome Package communication using the client_onboarding template with campaign_id 101. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "subject": "Welcome Package",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1622985.33"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_049",
        "instruction": "Handle the purchase support protocol for client 16 concerning property HTX005 (listing 5) at 674900 with 7.4% 30-year financing. Use the purchase_support template to send Purchase Support communication, referencing campaign_id 101. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 7.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Purchase Support",
                    "type": "purchase_support",
                    "created_by": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "subject": "Purchase Support",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1007333.66"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_050",
        "instruction": "Initiate the first time buyer protocol for client 1 related to property HTX006 (listing 6) at 225700 with 6.3% 30-year financing. Dispatch the Welcome Package communication using the first_time_buyer template, associated with campaign_id 101. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 6.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "Welcome Package",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1397.02"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_051",
        "instruction": "Ensure the preparation of a detailed market analysis for client 7 concerning property HTX001 (listing 1) priced at 1500000 with 6.9% 30-year financing. Compile a Market Intelligence Report that includes a comparative analysis of similar properties, and arrange a market intelligence briefing on 2025-04-20T10:00:00Z-11:00:00Z at the Office with 'Market intelligence consultation' notes. Calculate and provide the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Market Intelligence",
                    "type": "market_analysis",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "property_id": "HTX001",
                    "doc_type": "market_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Market Intelligence Report",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "title": "Market intelligence consultation",
                    "start_at": "2025-04-20T10:00:00Z",
                    "end_at": "2025-04-20T11:00:00Z",
                    "location": "Office",
                    "notes": "Market intelligence consultation"
                }
            }
        ],
        "outputs": [
                "9879.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_052",
        "instruction": "Coordinate an exclusive property showing for client 18 concerning property HTX004 (listing 4) valued at 705900 with 7.1% 30-year financing. Organize a private showing consultation on 2025-04-15T14:00:00Z-15:00:00Z at HTX004, ensuring 'Private property showing' notes are included. Compute and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Showings",
                    "type": "property_showing",
                    "created_by": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "subject": "Exclusive Property Showing",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "title": "Private property showing",
                    "start_at": "2025-04-15T14:00:00Z",
                    "end_at": "2025-04-15T15:00:00Z",
                    "location": "HTX004",
                    "notes": "Private property showing"
                }
            }
        ],
        "outputs": [
                "1001894.5"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_053",
        "instruction": "Handle investment consulting procedures for client 9 concerning property HTX005 (listing 5) at 674900 with 6.7% 30-year financing. Dispatch Investment Strategy Analysis communication using investment_consulting template with campaign_id 101. Provide the report on the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX005"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Consulting",
                    "type": "investment_consulting",
                    "created_by": 2
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Investment Strategy Analysis",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "1567793.19"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_054",
        "instruction": "Coordinate estate management procedures for client 14 regarding property HTX002 (listing 2) at 3975000 with 6.4% 30-year financing. Transmit Estate Portfolio Review communication using estate_management template with campaign_id 101. Offer a report on the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Estate Management",
                    "type": "estate_management",
                    "created_by": 3
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Estate Portfolio Review",
                    "template_code": "estate_management",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "4975989.56"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_055",
        "instruction": "Handle commercial sales protocol for client 20 pertinent to property HTX003 (listing 3) at 591000 with 7.3% 30-year financing. Send the Commercial Investment Opportunity communication using the commercial_sales template with campaign_id 101. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 7.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Sales",
                    "type": "commercial_sales",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "property_id": "HTX003",
                    "doc_type": "commercial_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "subject": "Commercial Investment Opportunity",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "4051.72"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_056",
        "instruction": "Handle relocation protocol for client 3 concerning property HTX005 (listing 5) at 674900 with 7.2% 30-year financing. Provide the Phoenix relocation guide along with neighborhood analysis and schedule a relocation consultation on 2025-05-01T09:00:00Z-10:00:00Z at Office with 'Executive relocation planning' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "city": "Phoenix"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 7.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Relocation Services",
                    "type": "relocation",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX005",
                    "doc_type": "relocation_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Phoenix Relocation Guide",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "title": "Executive relocation planning",
                    "start_at": "2025-05-01T09:00:00Z",
                    "end_at": "2025-05-01T10:00:00Z",
                    "location": "Office",
                    "notes": "Executive relocation planning"
                }
            }
        ],
        "outputs": [
                "974310.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_057",
        "instruction": "Handle the luxury marketing protocol for client 10 concerning property HTX002 (listing 2) priced at 3975000 with 6.8% 30-year financing. Provide the exclusive luxury property briefing and arrange a VIP consultation on 2025-05-05T15:00:00Z-16:00:00Z at Office with 'Luxury property consultation' notes documented. Please share the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "property_id": "HTX002",
                    "doc_type": "luxury_briefing"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "subject": "Premium Luxury Marketing",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "title": "Luxury property consultation",
                    "start_at": "2025-05-05T15:00:00Z",
                    "end_at": "2025-05-05T16:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property consultation"
                }
            }
        ],
        "outputs": [
                "25914.03"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_058",
        "instruction": "Manage the client onboarding protocol for client 16 related to property HTX003 (listing 3) valued at 591000 with 6.6% 30-year financing. Present a comprehensive onboarding package and organize the welcome consultation on 2025-05-10T11:00:00Z-12:00:00Z at Office with 'New client onboarding session' notes. Provide the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "property_id": "HTX003",
                    "doc_type": "onboarding_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "title": "New client onboarding session",
                    "start_at": "2025-05-10T11:00:00Z",
                    "end_at": "2025-05-10T12:00:00Z",
                    "location": "Office",
                    "notes": "New client onboarding session"
                }
            }
        ],
        "outputs": [
                "1358810.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_059",
        "instruction": "Handle the first time buyer protocol for client 2 concerning property HTX006 (listing 6) at 225700 with 7.0% 30-year financing. Offer first-time buyer education and arrange a buyer consultation on 2025-05-15T14:00:00Z-15:00:00Z at Office with 'First-time buyer guidance' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "property_id": "HTX006",
                    "doc_type": "buyer_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "First Home Purchase Guide",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "title": "First-time buyer guidance",
                    "start_at": "2025-05-15T14:00:00Z",
                    "end_at": "2025-05-15T15:00:00Z",
                    "location": "Office",
                    "notes": "First-time buyer guidance"
                }
            }
        ],
        "outputs": [
                "314871.58"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_060",
        "instruction": "Handle the investor outreach protocol for client 19 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. Present investment opportunity analysis along with a consultation scheduled for 2025-05-20T10:00:00Z-11:00:00Z at Office with 'Investment opportunity consultation' notes. Determine and report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Opportunities",
                    "type": "investor_outreach",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "property_id": "HTX001",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "subject": "Investment Opportunity Analysis",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "title": "Investment opportunity consultation",
                    "start_at": "2025-05-20T10:00:00Z",
                    "end_at": "2025-05-20T11:00:00Z",
                    "location": "Office",
                    "notes": "Investment opportunity consultation"
                }
            }
        ],
        "outputs": [
                "9481.02"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_061",
        "instruction": "Handle the purchase support protocol for client 5 concerning property HTX001 (listing 1) priced at 1500000 with 6.3% 30-year financing. Prepare a detailed purchase analysis and arrange a purchase consultation for 2025-06-01T10:00:00Z-11:00:00Z at Office, including 'Purchase strategy consultation' notes. Provide a report on the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Purchase Support",
                    "type": "purchase_support",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "property_id": "HTX001",
                    "doc_type": "purchase_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Comprehensive Purchase Analysis",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "title": "Purchase strategy consultation",
                    "start_at": "2025-06-01T10:00:00Z",
                    "end_at": "2025-06-01T11:00:00Z",
                    "location": "Office",
                    "notes": "Purchase strategy consultation"
                }
            }
        ],
        "outputs": [
                "1842453.06"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_062",
        "instruction": "Facilitate the property showing protocol for client 12 related to property HTX005 (listing 5) with a price of 674900 and 7.5% 30-year financing. Manage an exclusive property showing and set the showing appointment for 2025-06-05T15:00:00Z-16:00:00Z at HTX005, including 'Exclusive property viewing' notes. Deliver a report on the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 7.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Showings",
                    "type": "property_showing",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "property_id": "HTX005",
                    "doc_type": "showing_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Exclusive Property Showing",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "title": "Exclusive property viewing",
                    "start_at": "2025-06-05T15:00:00Z",
                    "end_at": "2025-06-05T16:00:00Z",
                    "location": "HTX005",
                    "notes": "Exclusive property viewing"
                }
            }
        ],
        "outputs": [
                "4719.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_063",
        "instruction": "Handle the VIP client protocol for client 8 concerning property HTX006 (listing 6) at 225700 with 6.8% 30-year financing. Provide exclusive VIP services and arrange a VIP consultation on 2025-06-10T14:30:00Z-15:30:00Z at Office, including 'VIP client consultation' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "VIP Client Services",
                    "type": "vip_client",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "property_id": "HTX006",
                    "doc_type": "vip_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "VIP Client Services",
                    "template_code": "vip_client",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "title": "VIP client consultation",
                    "start_at": "2025-06-10T14:30:00Z",
                    "end_at": "2025-06-10T15:30:00Z",
                    "location": "Office",
                    "notes": "VIP client consultation"
                }
            }
        ],
        "outputs": [
                "529702.25"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_064",
        "instruction": "Coordinate property evaluation protocol for client 17 in relation to property HTX004 (listing 4) at 705900 with 6.9% 30-year financing. Deliver a comprehensive property assessment with comparable analysis. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Analysis",
                    "type": "property_evaluation",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "property_id": "HTX004",
                    "doc_type": "evaluation_report"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "subject": "Comprehensive Market Overview",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "967761.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_065",
        "instruction": "Handle the implementation of the commercial sales protocol for client 1 concerning property HTX002 (listing 2) priced at 3975000 with 7.0% 30-year financing. Present the commercial investment analysis and arrange a business meeting on 2025-06-15T09:00:00Z-10:00:00Z at Office, accompanied by 'Commercial investment strategy' notes. Provide the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Sales",
                    "type": "commercial_sales",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "commercial_brief"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "Commercial Property Transaction",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "title": "Commercial investment strategy",
                    "start_at": "2025-06-15T09:00:00Z",
                    "end_at": "2025-06-15T10:00:00Z",
                    "location": "Office",
                    "notes": "Commercial investment strategy"
                }
            }
        ],
        "outputs": [
                "26445.77"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_066",
        "instruction": "Coordinate the first-time buyer protocol execution for client 9 related to property HTX003 (listing 3) valued at 895700 with 7.2% 30-year financing. Deliver detailed first-time buyer guidance and organize a buyer education session on 2025-06-20T13:00:00Z-14:00:00Z at Office, including 'First-time buyer consultation' notes. Relay the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 895700,
                    "interest_rate": 7.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "property_id": "HTX003",
                    "doc_type": "buyer_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Comprehensive First-Time Buyer Guidance",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "title": "First-time buyer consultation",
                    "start_at": "2025-06-20T13:00:00Z",
                    "end_at": "2025-06-20T14:00:00Z",
                    "location": "Office",
                    "notes": "First-time buyer consultation"
                }
            }
        ],
        "outputs": [
                "2188766.16"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_067",
        "instruction": "Handle the execution of market analysis protocol for client 15 in neighborhood Uptown concerning property HTX007 (listing 7) at 425600 with 6.5% 30-year financing. Deliver comprehensive market intelligence and arrange a market review on 2025-06-25T11:00:00Z-12:00:00Z at Office with 'Market analysis review' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 7
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "neighborhood_name": "Uptown"
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX007"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 425600,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Market Analysis",
                    "type": "market_analysis",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "property_id": "HTX007",
                    "doc_type": "market_report"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "subject": "Comprehensive Market Intelligence",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "title": "Market analysis review",
                    "start_at": "2025-06-25T11:00:00Z",
                    "end_at": "2025-06-25T12:00:00Z",
                    "location": "Office",
                    "notes": "Market analysis review"
                }
            }
        ],
        "outputs": [
                "2690.08"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_068",
        "instruction": "Handle the execution of relocation protocol for client 3 concerning property HTX008 (listing 8) at 1275000 with 6.7% 30-year financing. Coordinate comprehensive relocation services and plan a relocation planning on 2025-06-30T16:00:00Z-17:00:00Z at Office with 'Relocation strategy session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "neighborhood_name": "Central City"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 8
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1275000,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Relocation Services",
                    "type": "relocation",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX008",
                    "doc_type": "relocation_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Comprehensive Relocation Services",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "title": "Relocation strategy session",
                    "start_at": "2025-06-30T16:00:00Z",
                    "end_at": "2025-06-30T17:00:00Z",
                    "location": "Office",
                    "notes": "Relocation strategy session"
                }
            }
        ],
        "outputs": [
                "1686825.92"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_069",
        "instruction": "Handle the investor outreach protocol for client 18 concerning property HTX009 (listing 9) at 765300 with 7.1% 30-year financing. Provide the investment opportunity analysis and arrange an investor meeting on 2025-07-05T10:30:00Z-11:30:00Z at Office with 'Investment opportunity review' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 9
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 765300,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Opportunities",
                    "type": "investor_outreach",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "property_id": "HTX009",
                    "doc_type": "investment_brief"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "subject": "Investment Opportunity Analysis",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "title": "Investment opportunity review",
                    "start_at": "2025-07-05T10:30:00Z",
                    "end_at": "2025-07-05T11:30:00Z",
                    "location": "Office",
                    "notes": "Investment opportunity review"
                }
            }
        ],
        "outputs": [
                "5143.06"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_070",
        "instruction": "Coordinate the luxury marketing protocol for client 6 with respect to property HTX010 (listing 10) at 2850000 with 6.6% 30-year financing. Present exclusive luxury marketing services and set up a luxury consultation on 2025-07-10T14:00:00Z-15:00:00Z at Office with 'Luxury property strategy' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 10
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 2850000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "property_id": "HTX010",
                    "doc_type": "luxury_briefing"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Premium Luxury Marketing",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "title": "Luxury property strategy",
                    "start_at": "2025-07-10T14:00:00Z",
                    "end_at": "2025-07-10T15:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property strategy"
                }
            }
        ],
        "outputs": [
                "6552639.47"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_071",
        "instruction": "Handle the client onboarding protocol for client 11 concerning property HTX001 (listing 1) valued at 1500000 with a 6.4% 30-year financing plan. Provide a comprehensive onboarding package and arrange an onboarding consultation for 2025-07-15T09:30:00Z-10:30:00Z at Office, including 'Client onboarding session' notes. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "property_id": "HTX001",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "title": "Client onboarding session",
                    "start_at": "2025-07-15T09:30:00Z",
                    "end_at": "2025-07-15T10:30:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "9382.59"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_072",
        "instruction": "Coordinate the property evaluation protocol for client 14 related to property HTX002 (listing 2) priced at 3975000 with 6.8% 30-year financing. Furnish a thorough property assessment along with a market valuation analysis. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX002"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Analysis",
                    "type": "property_evaluation",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "property_id": "HTX002",
                    "doc_type": "evaluation_report"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Comprehensive Market Overview",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "5354049.44"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_073",
        "instruction": "Handle the investment consulting protocol for client 19 with respect to property HTX003 (listing 3) at 895700, utilizing 7.3% financing over 30 years. Provide strategic investment guidance along with a financial modeling analysis. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 895700,
                    "interest_rate": 7.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Consulting",
                    "type": "investment_consulting",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "property_id": "HTX003",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "subject": "Strategic Investment Guidance",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                }
            }
        ],
        "outputs": [
                "2210637.17"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_074",
        "instruction": "Coordinate the commercial sales protocol for client 2 concerning property HTX004 (listing 4) with a price of 705900 using 7.4% 30-year financing. Provide a commercial investment analysis and arrange a commercial meeting on 2025-07-20T11:00:00Z-12:00:00Z at Office, including 'Commercial sales strategy' notes. Present the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Sales",
                    "type": "commercial_sales",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "property_id": "HTX004",
                    "doc_type": "commercial_brief"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "Commercial Investment Analysis",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "title": "Commercial sales strategy",
                    "start_at": "2025-07-20T11:00:00Z",
                    "end_at": "2025-07-20T12:00:00Z",
                    "location": "Office",
                    "notes": "Commercial sales strategy"
                }
            }
        ],
        "outputs": [
                "4887.51"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_075",
        "instruction": "Handle the VIP client protocol for client 7 concerning property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. Offer exclusive VIP services and arrange a VIP consultation on 2025-07-25T15:30:00Z-16:30:00Z at Office with 'VIP client strategy session' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "VIP Client Services",
                    "type": "vip_client",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "property_id": "HTX005",
                    "doc_type": "vip_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "VIP Client Services",
                    "template_code": "vip_client",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "title": "VIP client strategy session",
                    "start_at": "2025-07-25T15:30:00Z",
                    "end_at": "2025-07-25T16:30:00Z",
                    "location": "Office",
                    "notes": "VIP client strategy session"
                }
            }
        ],
        "outputs": [
                "925261.23"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_076",
        "instruction": "Handle the portfolio review protocol for client 13 concerning property HTX001 (listing 1) at 1500000 with 6.2% 30-year financing. Provide a comprehensive portfolio assessment and organize a portfolio consultation on 2025-07-30T09:00:00Z-10:00:00Z at Office with 'Portfolio strategy review' notes. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Portfolio Review",
                    "type": "portfolio_review",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "property_id": "HTX001",
                    "doc_type": "portfolio_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "subject": "Comprehensive Portfolio Assessment",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "title": "Portfolio strategy review",
                    "start_at": "2025-07-30T09:00:00Z",
                    "end_at": "2025-07-30T10:00:00Z",
                    "location": "Office",
                    "notes": "Portfolio strategy review"
                }
            }
        ],
        "outputs": [
                "9187.03"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_077",
        "instruction": "Coordinate the estate management procedure for client 4 concerning property HTX002 (listing 2) priced at 3975000 with 6.6% 30-year financing. Offer luxury estate services and arrange an estate consultation on 2025-08-05T14:00:00Z-15:00:00Z at Office with 'Estate management strategy' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Estate Management",
                    "type": "estate_management",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "estate_portfolio"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "subject": "Luxury Estate Services",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "title": "Estate management strategy",
                    "start_at": "2025-08-05T14:00:00Z",
                    "end_at": "2025-08-05T15:00:00Z",
                    "location": "Office",
                    "notes": "Estate management strategy"
                }
            }
        ],
        "outputs": [
                "5164207.69"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_078",
        "instruction": "Handle the market analysis procedure for client 16 in the Westside neighborhood related to property HTX004 (listing 4) valued at 705900 with 7.3% 30-year financing. Deliver a comprehensive market analysis and organize a market briefing on 2025-08-10T11:30:00Z-12:30:00Z at Office with 'Market intelligence consultation' notes. Provide a report on the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "neighborhood_name": "Westside"
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX004"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Market Intelligence",
                    "type": "market_analysis",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "property_id": "HTX004",
                    "doc_type": "market_report"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "subject": "Comprehensive Market Intelligence",
                    "template_code": "market_analysis",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "title": "Market intelligence consultation",
                    "start_at": "2025-08-10T11:30:00Z",
                    "end_at": "2025-08-10T12:30:00Z",
                    "location": "Office",
                    "notes": "Market intelligence consultation"
                }
            }
        ],
        "outputs": [
                "1742200.27"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_079",
        "instruction": "Handle the purchase support procedure for client 10 concerning property HTX003 (listing 3) valued at 591000 utilizing 6.8% 30-year financing. Provide a detailed purchase analysis and arrange a purchase meeting on 2025-08-15T10:00:00Z-11:00:00Z at Office while including 'Purchase strategy consultation' notes. Report on the monthly payment figure.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Purchase Support",
                    "type": "purchase_support",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "property_id": "HTX003",
                    "doc_type": "purchase_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "subject": "Comprehensive Purchase Analysis",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "title": "Purchase strategy consultation",
                    "start_at": "2025-08-15T10:00:00Z",
                    "end_at": "2025-08-15T11:00:00Z",
                    "location": "Office",
                    "notes": "Purchase strategy consultation"
                }
            }
        ],
        "outputs": [
                "3852.88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_080",
        "instruction": "Manage the property showing procedure for client 7 related to property HTX005 (listing 5) priced at 674900 with 7.1% 30-year financing. Arrange an exclusive property showing and set up a showing session on 2025-08-20T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. Provide the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Showings",
                    "type": "property_showing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "property_id": "HTX005",
                    "doc_type": "showing_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Exclusive Property Showing",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "title": "Private property viewing",
                    "start_at": "2025-08-20T15:30:00Z",
                    "end_at": "2025-08-20T16:30:00Z",
                    "location": "HTX005",
                    "notes": "Private property viewing"
                }
            }
        ],
        "outputs": [
                "957895.73"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_081",
        "instruction": "Handle the relocation protocol for client 11 in neighborhood Central City concerning property HTX006 (listing 6) at 225700 with 6.9% 30-year financing. Provide comprehensive relocation services and arrange a relocation consultation on 2025-08-25T10:30:00Z-11:30:00Z at Office with 'Relocation planning session' notes. Calculate the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "neighborhood_name": "Central City"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Relocation Services",
                    "type": "relocation",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "property_id": "HTX006",
                    "doc_type": "relocation_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "subject": "Comprehensive Relocation Services",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "title": "Relocation planning session",
                    "start_at": "2025-08-25T10:30:00Z",
                    "end_at": "2025-08-25T11:30:00Z",
                    "location": "Office",
                    "notes": "Relocation planning session"
                }
            }
        ],
        "outputs": [
                "535125.78"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_082",
        "instruction": "Coordinate the luxury marketing protocol for client 8 concerning property HTX007 (listing 7) at 425600 with 6.4% 30-year financing. Offer exclusive luxury marketing services and arrange a luxury consultation on 2025-08-30T14:30:00Z-15:30:00Z at Office with 'Luxury property strategy' notes. Determine the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 7
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 425600,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "property_id": "HTX007",
                    "doc_type": "luxury_briefing"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "Exclusive Luxury Marketing Services",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "title": "Luxury property strategy",
                    "start_at": "2025-08-30T14:30:00Z",
                    "end_at": "2025-08-30T15:30:00Z",
                    "location": "Office",
                    "notes": "Luxury property strategy"
                }
            }
        ],
        "outputs": [
                "2662.15"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_083",
        "instruction": "Handle the first time buyer protocol for client 19 concerning property HTX008 (listing 8) listed at 1275000 with 7.0% 30-year financing. Provide comprehensive first-time buyer guidance and arrange a buyer education session on 2025-09-05T09:30:00Z-10:30:00Z at Office with 'First-time buyer consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 8
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1275000,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "property_id": "HTX008",
                    "doc_type": "buyer_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "subject": "First-Time Buyer Support",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "title": "First-time buyer consultation",
                    "start_at": "2025-09-05T09:30:00Z",
                    "end_at": "2025-09-05T10:30:00Z",
                    "location": "Office",
                    "notes": "First-time buyer consultation"
                }
            }
        ],
        "outputs": [
                "1778738.45"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_084",
        "instruction": "Coordinate the investor outreach protocol for client 2 related to property HTX009 (listing 9) priced at 765300 with 6.8% 30-year financing. Offer investment opportunity analysis and organize an investor meeting on 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Investment opportunity review' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 9
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX009"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 765300,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Opportunities",
                    "type": "investor_outreach",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "property_id": "HTX009",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "Investment Opportunity Analysis",
                    "template_code": "investor_outreach",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "title": "Investment opportunity review",
                    "start_at": "2025-09-10T13:00:00Z",
                    "end_at": "2025-09-10T14:00:00Z",
                    "location": "Office",
                    "notes": "Investment opportunity review"
                }
            }
        ],
        "outputs": [
                "1796106.05"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_085",
        "instruction": "Handle the client onboarding protocol for client 15 concerning property HTX010 (listing 10) valued at 2850000 with 6.5% 30-year financing. Present a thorough onboarding package and arrange an onboarding consultation on 2025-09-15T11:00:00Z-12:00:00Z at Office with 'Client onboarding session' notes. Submit the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 10
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX010"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 2850000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "property_id": "HTX010",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-15T11:00:00Z",
                    "end_at": "2025-09-15T12:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "18013.94"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_086",
        "instruction": "Initiate the VIP client protocol for client 17 concerning property HTX006 (listing 6) priced at 225700 with 6.3% 30-year financing. Provide premium VIP service and set up a VIP consultation on 2025-08-25T14:00:00Z-15:00:00Z at Office with 'VIP client consultation' notes. Submit the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 6.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "VIP Client Services",
                    "type": "vip_client",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "property_id": "HTX006",
                    "doc_type": "vip_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "subject": "VIP Client Services",
                    "template_code": "vip_client",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "title": "VIP client consultation",
                    "start_at": "2025-08-25T14:00:00Z",
                    "end_at": "2025-08-25T15:00:00Z",
                    "location": "Office",
                    "notes": "VIP client consultation"
                }
            }
        ],
        "outputs": [
                "1397.02"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_087",
        "instruction": "Handle estate management protocol for client 14 concerning property HTX007 (listing 7) at 1490000 with 6.9% 30-year financing. Coordinate luxury estate services and arrange an estate consultation on 2025-08-30T16:00:00Z-17:00:00Z at Office, using 'Estate management strategy' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 7
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1490000,
                    "interest_rate": 6.9,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Estate Management",
                    "type": "estate_management",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "property_id": "HTX007",
                    "doc_type": "estate_portfolio"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Luxury Estate Services",
                    "template_code": "estate_management",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "title": "Estate management strategy",
                    "start_at": "2025-08-30T16:00:00Z",
                    "end_at": "2025-08-30T17:00:00Z",
                    "location": "Office",
                    "notes": "Estate management strategy"
                }
            }
        ],
        "outputs": [
                "3532731.11"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_088",
        "instruction": "Handle first time buyer protocol for client 8 concerning property HTX008 (listing 8) at 330000 with 7.0% 30-year financing. Coordinate first-time buyer education and arrange an education meeting on 2025-09-05T10:30:00Z-11:30:00Z at Office, using 'First-time buyer education' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 8
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 330000,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "property_id": "HTX008",
                    "doc_type": "buyer_education"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "First-Time Buyer Support",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "title": "First-time buyer education",
                    "start_at": "2025-09-05T10:30:00Z",
                    "end_at": "2025-09-05T11:30:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education"
                }
            }
        ],
        "outputs": [
                "460379.36"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_089",
        "instruction": "Handle the luxury marketing protocol for client 19 with respect to property HTX009 (listing 9) priced at 400000 using 6.4% 30-year financing. Provide premium luxury marketing and arrange a luxury consultation on 2025-09-10T13:00:00Z-14:00:00Z at Office, including 'Luxury property consultation' notes. Provide the monthly payment amount in your report.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 9
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 400000,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "property_id": "HTX009",
                    "doc_type": "luxury_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "subject": "Premium Luxury Marketing",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "title": "Luxury property consultation",
                    "start_at": "2025-09-10T13:00:00Z",
                    "end_at": "2025-09-10T14:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property consultation"
                }
            }
        ],
        "outputs": [
                "2502.02"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_090",
        "instruction": "Coordinate the investment consulting protocol for client 15 concerning property HTX010 (listing 10) valued at 458500 with 6.7% 30-year financing. Offer strategic investment guidance and organize an investment meeting on 2025-09-15T11:00:00Z-12:00:00Z at Office, using 'Investment strategy consultation' notes. Supply the total payment amount in the report.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 10
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX010"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 458500,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Investment Consulting",
                    "type": "investment_consulting",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "property_id": "HTX010",
                    "doc_type": "investment_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "subject": "Strategic Investment Guidance",
                    "template_code": "investment_consulting",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "title": "Investment strategy consultation",
                    "start_at": "2025-09-15T11:00:00Z",
                    "end_at": "2025-09-15T12:00:00Z",
                    "location": "Office",
                    "notes": "Investment strategy consultation"
                }
            }
        ],
        "outputs": [
                "1065095.83"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_091",
        "instruction": "Handle the client onboarding protocol for client 1 related to property HTX001 (listing 1) priced at 1500000 with 6.5% for a 30-year financing plan. Coordinate comprehensive client onboarding and arrange the onboarding meeting on 2025-09-20T09:00:00Z-10:00:00Z in the Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 1
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1500000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "property_id": "HTX001",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-20T09:00:00Z",
                    "end_at": "2025-09-20T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1913167.33"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_092",
        "instruction": "Handle the luxury marketing protocol for client 2 concerning property HTX002 (listing 2) at the value of 3975000 with a 7.1% 30-year financing. Facilitate premium luxury marketing and arrange the luxury consultation on 2025-09-25T14:00:00Z-15:00:00Z in the Office with 'Luxury property consultation' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 2
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 3975000,
                    "interest_rate": 7.1,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Luxury Collection",
                    "type": "luxury_marketing",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "luxury_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "Premium Luxury Marketing",
                    "template_code": "luxury_marketing",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "title": "Luxury property consultation",
                    "start_at": "2025-09-25T14:00:00Z",
                    "end_at": "2025-09-25T15:00:00Z",
                    "location": "Office",
                    "notes": "Luxury property consultation"
                }
            }
        ],
        "outputs": [
                "26713.27"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_093",
        "instruction": "Handle the property evaluation protocol for client 3 concerning property HTX003 (listing 3) valued at 591000 with 6.6% 30-year financing. Provide a detailed property analysis and arrange an evaluation meeting on 2025-09-30T11:00:00Z-12:00:00Z at Office with 'Property evaluation consultation' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 3
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 591000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Analysis",
                    "type": "property_evaluation",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX003",
                    "doc_type": "evaluation_report"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Comprehensive Market Overview",
                    "template_code": "property_evaluation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "title": "Property evaluation consultation",
                    "start_at": "2025-09-30T11:00:00Z",
                    "end_at": "2025-09-30T12:00:00Z",
                    "location": "Office",
                    "notes": "Property evaluation consultation"
                }
            }
        ],
        "outputs": [
                "1358810.5"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_094",
        "instruction": "Conduct the commercial sales protocol for client 18 in relation to property HTX004 (listing 4) priced at 705900 with 7.2% 30-year financing. Focus on the commercial property transaction and set up a commercial meeting on 2025-10-05T16:00:00Z-17:00:00Z at Office with 'Commercial transaction consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 4
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 705900,
                    "interest_rate": 7.2,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Commercial Sales",
                    "type": "commercial_sales",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "property_id": "HTX004",
                    "doc_type": "commercial_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "subject": "Commercial Property Transaction",
                    "template_code": "commercial_sales",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "title": "Commercial transaction consultation",
                    "start_at": "2025-10-05T16:00:00Z",
                    "end_at": "2025-10-05T17:00:00Z",
                    "location": "Office",
                    "notes": "Commercial transaction consultation"
                }
            }
        ],
        "outputs": [
                "1019063.75"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_095",
        "instruction": "Handle the property showing protocol for client 5 concerning property HTX005 (listing 5) priced at 674900 with a 6.8% 30-year financing plan. Arrange an exclusive property showing and set the appointment for 2025-10-10T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. Provide the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 5
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 674900,
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Showings",
                    "type": "property_showing",
                    "created_by": 1
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "property_id": "HTX005",
                    "doc_type": "showing_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Exclusive Property Showing",
                    "template_code": "showing_invitation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "title": "Private property viewing",
                    "start_at": "2025-10-10T15:30:00Z",
                    "end_at": "2025-10-10T16:30:00Z",
                    "location": "HTX005",
                    "notes": "Private property viewing"
                }
            }
        ],
        "outputs": [
                "4399.84"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_096",
        "instruction": "Handle the relocation protocol for client 6 related to property HTX006 (listing 6) priced at 225700 with a 7.0% 30-year financing plan.Support client's relocation by providing an area analysis and set up a relocation meeting on 2025-10-15T09:00:00Z-10:00:00Z at Office with 'Relocation consultation' notes. Provide the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "SearchNeighborhoods",
                "arguments": {
                    "city": "Phoenix"
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 6
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 225700,
                    "interest_rate": 7.0,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Relocation Services",
                    "type": "relocation",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "property_id": "HTX006",
                    "doc_type": "relocation_guide"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Comprehensive Relocation Services",
                    "template_code": "relocation",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "title": "Relocation consultation",
                    "start_at": "2025-10-15T09:00:00Z",
                    "end_at": "2025-10-15T10:00:00Z",
                    "location": "Office",
                    "notes": "Relocation consultation"
                }
            }
        ],
        "outputs": [
                "540571.58"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_097",
        "instruction": "Handle the portfolio review protocol for client 9 concerning property HTX007 (listing 7) at 1490000 with 6.4% 30-year financing. Deliver a comprehensive portfolio assessment and schedule a portfolio consultation on 2025-10-20T14:00:00Z-15:00:00Z at the Office with 'Portfolio strategy review' notes. Provide a report on the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 7
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX007"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1490000,
                    "interest_rate": 6.4,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Portfolio Review",
                    "type": "portfolio_review",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "property_id": "HTX007",
                    "doc_type": "portfolio_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Comprehensive Portfolio Assessment",
                    "template_code": "portfolio_review",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "title": "Portfolio strategy review",
                    "start_at": "2025-10-20T14:00:00Z",
                    "end_at": "2025-10-20T15:00:00Z",
                    "location": "Office",
                    "notes": "Portfolio strategy review"
                }
            }
        ],
        "outputs": [
                "1865213.7"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_098",
        "instruction": "Handle the first-time buyer protocol for client 12 regarding property HTX008 (listing 8) at 330000 with 6.6% 30-year financing. Offer first-time buyer education and arrange an education meeting on 2025-10-25T10:30:00Z-11:30:00Z at the Office with 'First-time buyer education' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 8
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX008"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 330000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "First Home Purchase",
                    "type": "first_time_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "property_id": "HTX008",
                    "doc_type": "buyer_education"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "First-Time Buyer Support",
                    "template_code": "first_time_buyer",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "title": "First-time buyer education",
                    "start_at": "2025-10-25T10:30:00Z",
                    "end_at": "2025-10-25T11:30:00Z",
                    "location": "Office",
                    "notes": "First-time buyer education"
                }
            }
        ],
        "outputs": [
                "2107.57"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_099",
        "instruction": "Handle the market intelligence protocol for client 11 concerning property HTX009 (listing 9) priced at 400000 with a 7.3% 30-year financing option. Provide quarterly market intelligence and arrange a meeting on 2025-10-30T16:00:00Z-17:00:00Z at Office, accompanied by 'Market intelligence briefing' notes. Calculate and report the total payment amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 9
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX009"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 400000,
                    "interest_rate": 7.3,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Market Intelligence",
                    "type": "market_intelligence",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "property_id": "HTX009",
                    "doc_type": "market_report"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "subject": "Comprehensive Market Intelligence",
                    "template_code": "market_intelligence",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "title": "Market intelligence briefing",
                    "start_at": "2025-10-30T16:00:00Z",
                    "end_at": "2025-10-30T17:00:00Z",
                    "location": "Office",
                    "notes": "Market intelligence briefing"
                }
            }
        ],
        "outputs": [
                "987222.14"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "Coordinate purchase support protocol for client 20 related to property HTX010 (listing 10) valued at 458500 with a 6.5% 30-year financing plan. Supply a complete purchase analysis and set up a meeting on 2025-11-05T11:00:00Z-12:00:00Z at Office with 'Purchase strategy consultation' notes. Compute and report the total interest amount.",
        "actions": [
            {
                "name": "SearchClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "GetListingDetails",
                "arguments": {
                    "listing_id": 10
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX010"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 458500,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Purchase Support",
                    "type": "purchase_support",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "property_id": "HTX010",
                    "doc_type": "purchase_analysis"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "subject": "Comprehensive Purchase Analysis",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "title": "Purchase strategy consultation",
                    "start_at": "2025-11-05T11:00:00Z",
                    "end_at": "2025-11-05T12:00:00Z",
                    "location": "Office",
                    "notes": "Purchase strategy consultation"
                }
            }
        ],
        "outputs": [
                "584791.48"
        ]
    }
]
