
tasks = [
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_001",
        "instruction": "Handle client onboarding protocol for client 1 regarding property HTX001 (listing 1) at 1500000 with 5.847% 30-year financing. Conduct a comprehensive client onboarding and arrange an onboarding meeting on 2025-09-20T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 5.847,
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
                "1684647.00"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_002",
        "instruction": "Handle client onboarding protocol for client 2 regarding property HTX002 (listing 2) at 3975000 with 6.395% 30-year financing. Conduct a comprehensive client onboarding and arrange an onboarding meeting on 2025-09-21T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 6.395,
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
                    "client_id": 2,
                    "broker_id": 1,
                    "property_id": "HTX002",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 1,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-21T09:00:00Z",
                    "end_at": "2025-09-21T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "4971305.22"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_003",
        "instruction": "Handle the client onboarding procedure for client 3 concerning property HTX003 (listing 3) at 591000 with a 5.915% 30-year financing option. Coordinate a detailed client onboarding and plan the onboarding meeting for 2025-09-22T09:00:00Z-10:00:00Z at Office, including 'Client onboarding session' notes. Calculate the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 5.915,
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
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX003",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-22T09:00:00Z",
                    "end_at": "2025-09-22T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "673000.07"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_004",
        "instruction": "Handle the client onboarding procedure for client 4 in relation to property HTX004 (listing 4) at 705900 with a 5.847% 30-year financing option. Coordinate a detailed client onboarding and plan the onboarding meeting for 2025-09-23T09:00:00Z-10:00:00Z at Office, including 'Client onboarding session' notes. Calculate the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 5.847,
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
                    "client_id": 4,
                    "broker_id": 1,
                    "property_id": "HTX004",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-23T09:00:00Z",
                    "end_at": "2025-09-23T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "792794.88"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_005",
        "instruction": "Handle the client onboarding protocol for client 5 pertaining to property HTX005 (listing 5) at 674900 with 6.395% 30-year financing. Coordinate a comprehensive client onboarding process and organize an onboarding meeting on 2025-09-24T09:00:00Z-10:00:00Z at the Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 6.395,
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
                    "client_id": 5,
                    "broker_id": 1,
                    "property_id": "HTX005",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-24T09:00:00Z",
                    "end_at": "2025-09-24T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "844058.84"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_006",
        "instruction": "Handle the client onboarding protocol for client 6 pertaining to property HTX006 (listing 6) at 225700 with 5.915% 30-year financing. Coordinate a comprehensive client onboarding process and organize an onboarding meeting on 2025-09-25T09:00:00Z-10:00:00Z at the Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 5.915,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "property_id": "HTX006",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-25T09:00:00Z",
                    "end_at": "2025-09-25T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "257015.43"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_007",
        "instruction": "Handle the client onboarding protocol for client 7 concerning property HTX007 (listing 7) at 1490000 with 5.847% 30-year financing. Conduct a thorough client onboarding and arrange an onboarding meeting on 2025-09-26T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 5.847,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "property_id": "HTX007",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-26T09:00:00Z",
                    "end_at": "2025-09-26T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1673416.02"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_008",
        "instruction": "Handle the client onboarding protocol for client 8 concerning property HTX008 (listing 8) at 330000 with 6.395% 30-year financing. Conduct a thorough client onboarding and arrange an onboarding meeting on 2025-09-27T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 6.395,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "property_id": "HTX008",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-27T09:00:00Z",
                    "end_at": "2025-09-27T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "412712.13"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_009",
        "instruction": "Handle the client onboarding protocol for client 9 associated with property HTX011 (listing 11) valued at 495000 using 5.915% 30-year financing. Carry out a thorough client onboarding and arrange the onboarding meeting for 2025-09-28T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Summarize the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 11
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX011"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 495000,
                    "interest_rate": 5.915,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "property_id": "HTX011",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-28T09:00:00Z",
                    "end_at": "2025-09-28T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "563680.26"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_010",
        "instruction": "Handle the client onboarding protocol for client 10 related to property HTX010 (listing 10) valued at 458500 with 5.847% 30-year financing. Conduct a detailed client onboarding and organize the onboarding meeting for 2025-09-29T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Summarize the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 5.847,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "property_id": "HTX010",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-29T09:00:00Z",
                    "end_at": "2025-09-29T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "514940.43"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_011",
        "instruction": "Handle the client onboarding protocol for client 11 concerning property HTX011 (listing 11) valued at 899000 with 5.8% 30-year financing. Organize a detailed client onboarding and schedule the onboarding meeting for 2025-09-21T09:00:00Z-10:00:00Z at Office, including 'Client onboarding session' notes. Present the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 11
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX011"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 899000,
                    "interest_rate": 5.8,
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
                    "property_id": "HTX011",
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
                    "start_at": "2025-09-21T09:00:00Z",
                    "end_at": "2025-09-21T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "999967.53"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_012",
        "instruction": "Execute the property evaluation protocol for client 14 related to property HTX002 (listing 2) priced at 3975000 with 6.8% 30-year financing. Prepare a comprehensive property assessment including market valuation analysis. Provide the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_013",
        "instruction": "Handle the onboarding process for client 13 who is interested in property HTX013 (listing 13) valued at 591000 with a 6.8% 30-year mortgage. Organize all necessary onboarding materials and arrange a meeting on 2025-09-23T09:00:00Z\u201310:00:00Z at the Office with notes 'Client onboarding session'. Be certain to report the total interest paid.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 13
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX013"
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
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "property_id": "HTX013",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 3,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-23T09:00:00Z",
                    "end_at": "2025-09-23T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "796036.03"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_014",
        "instruction": "Coordinate onboarding for client 14 who is purchasing HTX014 (listing 14) at a price of 875000 with a 6.2% 30-year loan. Set up an event on the calendar for 2025-09-24T09:00:00Z and ensure the interest paid is reported.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 14
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX014"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 875000,
                    "interest_rate": 6.2,
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
                    "client_id": 14,
                    "broker_id": 3,
                    "property_id": "HTX014",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-24T09:00:00Z",
                    "end_at": "2025-09-24T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1054277.28"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_015",
        "instruction": "Handle the client onboarding for client 15 for HTX015 (listing 15) with a price of 1380000 at a 6.1% rate over 30 years. Coordinate all onboarding materials and set up a session at the Office on 2025-09-25T09:00:00Z. Provide the total interest figure.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 15
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX015"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 1380000,
                    "interest_rate": 6.1,
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
                    "property_id": "HTX015",
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
                    "start_at": "2025-09-25T09:00:00Z",
                    "end_at": "2025-09-25T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1630582.09"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_016",
        "instruction": "Coordinate the execution of the client onboarding protocol for client 16 concerning property HTX009 (listing 9) priced at 1130000 with a 6.1% 30-year plan. Organize an onboarding consultation on 2025-10-04T09:00:00Z\u201310:00:00Z at the Office with notes titled 'Client onboarding session'. Deliver the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 1130000,
                    "interest_rate": 6.1,
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
                    "property_id": "HTX009",
                    "doc_type": "onboarding_package"
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
                    "title": "Client onboarding session",
                    "start_at": "2025-10-04T09:00:00Z",
                    "end_at": "2025-10-04T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1335186.79"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_017",
        "instruction": "Handle the client onboarding protocol for client 17 concerning property HTX010 (listing 10) priced at 1580000 with 6.3% for 30-year financing. Arrange the onboarding consultation on 2025-10-05T09:00:00Z\u201310:00:00Z at Office with 'Client onboarding session' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 1580000,
                    "interest_rate": 6.3,
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
                    "client_id": 17,
                    "broker_id": 4,
                    "property_id": "HTX010",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 4,
                    "title": "Client onboarding session",
                    "start_at": "2025-10-05T09:00:00Z",
                    "end_at": "2025-10-05T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1940717.23"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_018",
        "instruction": "Handle the client onboarding protocol for client 18 concerning property HTX001 (listing 1) priced at 1500000 with 6.5% for 30-year financing. Arrange the onboarding consultation on 2025-10-06T09:00:00Z\u201310:00:00Z at Office with 'Client onboarding session' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "property_id": "HTX001",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 4,
                    "title": "Client onboarding session",
                    "start_at": "2025-10-06T09:00:00Z",
                    "end_at": "2025-10-06T10:00:00Z",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_019",
        "instruction": "Handle the client onboarding protocol for client 19 concerning property HTX002 (listing 2) valued at 875000 with 6.4% 30-year financing. Arrange the onboarding consultation for 2025-10-07T09:00:00Z\u201310:00:00Z at Office, including 'Client onboarding session' notes. Provide a report on the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 875000,
                    "interest_rate": 6.4,
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
                    "client_id": 19,
                    "broker_id": 4,
                    "property_id": "HTX002",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 4,
                    "title": "Client onboarding session",
                    "start_at": "2025-10-07T09:00:00Z",
                    "end_at": "2025-10-07T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1095343.61"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_020",
        "instruction": "Handle the client onboarding protocol for client 20 concerning property HTX003 (listing 3) valued at 591000 with 6.8% 30-year financing. Arrange the onboarding consultation for 2025-10-08T09:00:00Z\u201310:00:00Z at Office, including 'Client onboarding session' notes. Provide a report on the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "property_id": "HTX003",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 4,
                    "title": "Client onboarding session",
                    "start_at": "2025-10-08T09:00:00Z",
                    "end_at": "2025-10-08T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "796036.03"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_021",
        "instruction": "Handle the market intelligence protocol for client 11 related to property HTX009 (listing 9) at 400000 with 7.3% 30-year financing. Coordinate the delivery of quarterly market intelligence and arrange an intelligence meeting on 2025-10-30T16:00:00Z-17:00:00Z at the Office with 'Market intelligence briefing' notes. Provide a report on the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_022",
        "instruction": "Assist client 5 in understanding their financing options for property HTX005 (listing 5). Use the listing's current price as the principal for a 30-year mortgage at 6.5% interest, and present a summary of the mortgage interest for review. Include relevant property comparisons and compile a purchase support package.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 6.5,
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
                    "property_id": "HTX005",
                    "doc_type": "purchase_support"
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
                }
            }
        ],
        "outputs": [
                "860797.75"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_023",
        "instruction": "Handle the PurchaseSupportProtocol for client 3 concerning property HTX013 (listing 13) with a price of $965,000. Incorporate comparables, compute the overall interest for a 6.1% 30-year mortgage, develop the campaign and briefing documentation, dispatch the purchase support email, and arrange a consultation on 2025\u201109\u201128T09:00:00Z\u201310:00:00Z at Office. Compile a report on the total interest.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 13
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX013"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 965000,
                    "interest_rate": 6.1,
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
                    "client_id": 3,
                    "broker_id": 1,
                    "property_id": "HTX013",
                    "doc_type": "purchase_support"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Comprehensive Purchase Analysis",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "title": "Purchase consultation",
                    "start_at": "2025-09-28T09:00:00Z",
                    "end_at": "2025-09-28T10:00:00Z",
                    "location": "Office",
                    "notes": "Purchase consultation"
                }
            }
        ],
        "outputs": [
                "1140225.88"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_024",
        "instruction": "Coordinate the PurchaseSupportProtocol for client 4 related to property HTX004 (listing 4) priced at $705,900. Include comparables, determine the total interest at a 6.3% 30-year mortgage, prepare the campaign and briefing documentation, send the purchase support email, and organize a consultation on 2025\u201109\u201129T09:00:00Z\u201310:00:00Z at Office. Document the total interest.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "client_id": 4,
                    "broker_id": 1,
                    "property_id": "HTX004",
                    "doc_type": "purchase_support"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "subject": "Comprehensive Purchase Analysis",
                    "template_code": "purchase_support",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 1,
                    "title": "Purchase consultation",
                    "start_at": "2025-09-29T09:00:00Z",
                    "end_at": "2025-09-29T10:00:00Z",
                    "location": "Office",
                    "notes": "Purchase consultation"
                }
            }
        ],
        "outputs": [
                "867058.41"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_025",
        "instruction": "Assist client 5 in assessing property HTX005 (listing 5), currently offered at $674,900. Use this price for computing a 30-year mortgage at 6.5% interest, and identify the total interest payable. Incorporate comparable listings and prepare the analysis report.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 6.5,
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
                    "property_id": "HTX005",
                    "doc_type": "purchase_support"
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
                }
            }
        ],
        "outputs": [
                "860797.75"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_026",
        "instruction": "Manage the client onboarding process for client 6 regarding property HTX006 (listing 6) priced at 1550000 with 6.7% 30-year financing. Complete full client onboarding and arrange the onboarding meeting on 2025-09-26T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 1550000,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "property_id": "HTX006",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-26T09:00:00Z",
                    "end_at": "2025-09-26T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "2050651.12"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_027",
        "instruction": "Handle the client onboarding protocol for client 7 concerning property HTX007 (listing 7) valued at 1490000 with 6.8% 30-year financing. Coordinate comprehensive client onboarding and arrange the onboarding meeting on 2025-09-27T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Document the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "interest_rate": 6.8,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "property_id": "HTX007",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-27T09:00:00Z",
                    "end_at": "2025-09-27T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "2006926.71"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_028",
        "instruction": "Handle the client onboarding protocol for client 8 concerning property HTX008 (listing 8) valued at 1625000 with 6.5% 30-year financing. Coordinate comprehensive client onboarding and arrange the onboarding meeting on 2025-09-28T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Document the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 1625000,
                    "interest_rate": 6.5,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "property_id": "HTX008",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-28T09:00:00Z",
                    "end_at": "2025-09-28T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "2072597.94"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_029",
        "instruction": "Handle the client onboarding protocol for client 9 involving property HTX009 (listing 9) priced at 1400000 with a 6.6% 30-year loan. Conduct a thorough client onboarding and organize an onboarding meeting on 2025-09-29T09:00:00Z-10:00:00Z at Office with notes titled 'Client onboarding session'. Provide the total interest amount in your report.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 1400000,
                    "interest_rate": 6.6,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "property_id": "HTX009",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-29T09:00:00Z",
                    "end_at": "2025-09-29T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1818840.44"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_030",
        "instruction": "Coordinate the client onboarding protocol for client 10 regarding property HTX010 (listing 10) valued at 1295000 with a 6.7% 30-year mortgage. Execute a comprehensive client onboarding and arrange an onboarding meeting on 2025-09-30T09:00:00Z-10:00:00Z at Office, including notes marked 'Client onboarding session'. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "principal": 1295000,
                    "interest_rate": 6.7,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "property_id": "HTX010",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-30T09:00:00Z",
                    "end_at": "2025-09-30T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1713285.93"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_031",
        "instruction": "Handle the basic property analysis for client 11 concerning property HTX001 (listing 1) valued at 1500000 with a 6.5% 30-year financing option. Dispatch the Property Analysis Update communication utilizing the property_evaluation template associated with campaign_id 101. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "FetchListingDetails",
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
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 3,
                    "property_id": "HTX001",
                    "doc_type": "property_evaluation"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Property Analysis for property_evaluation",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_032",
        "instruction": "Coordinate the property showing for client 14 related to property HTX003 (listing 3) priced at 591000 with 7.1% 30-year financing. Issue the Property Showing Invitation communication using the showing_invitation template linked to campaign_id 101. Summarize and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_033",
        "instruction": "Handle initial buyer support for client 17 concerning property HTX005 (listing 5) priced at 674900 with 6.8% 30-year financing. Deliver thorough first-time buyer education and arrange an education session on 2025-03-10T14:00:00Z-15:00:00Z at Office with 'First-time buyer education session' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_034",
        "instruction": "Coordinate luxury marketing services for client 20 related to property HTX002 (listing 2) valued at 3975000 with 6.3% 30-year financing. Dispatch Exclusive Luxury Collection communication utilizing luxury_marketing template with campaign_id 101. Report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_035",
        "instruction": "Handle investor outreach assistance for client 3 concerning property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. Dispatch the Investment Opportunity Brief using the investor_outreach template with campaign_id 101. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_036",
        "instruction": "Coordinate first-time buyer assistance for client 5 about property HTX002 (listing 2) at 3975000 with 6.9% 30-year financing. Deliver the Welcome Package using the first_time_buyer template with campaign_id 101. Report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_037",
        "instruction": "Arrange a property viewing for client 8 for property HTX001 (listing 1) valued at 1500000 with 7.0% 30-year financing. Set up a private property showing on 2025-03-15T15:00:00Z-16:00:00Z at HTX001, including 'Private property showing' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_038",
        "instruction": "Deliver luxury marketing services to client 13 for property HTX005 (listing 5) priced at 674900 with 6.6% 30-year financing. Utilize the luxury_marketing template to send Exclusive VIP Access communication with campaign_id 101. Arrange a VIP consultation on 2025-05-05T14:00:00Z-15:00:00Z at the Office with 'VIP client consultation' notes. Determine and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_039",
        "instruction": "Handle the property evaluation protocol for client 18 concerning property HTX003 (listing 3) priced at 591000 with 7.3% 30-year financing. Dispatch the Property Evaluation Report using the property_evaluation template associated with campaign_id 101. Provide the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_040",
        "instruction": "Coordinate investor outreach support for client 6 regarding property HTX006 (listing 6) valued at 225700 with 6.4% 30-year financing. Distribute the Investment Opportunity Brief using the investor_outreach template linked to campaign_id 101. Indicate the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_041",
        "instruction": "Handle the relocation protocol for client 9 concerning property HTX001 (listing 1) priced at 1500000 with 6.8% 30-year financing. Dispatch the Relocation Guide communication using the relocation template with campaign_id 101. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_042",
        "instruction": "Coordinate commercial sales services for client 14 relating to property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. Deliver the Commercial Investment Opportunity communication using the commercial_sales template with campaign_id 101. Determine and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_043",
        "instruction": "Handle the estate management protocol for client 17 concerning property HTX003 (listing 3) at 591000 with 6.5% 30-year financing. Dispatch Estate Services communication employing the estate_management template with campaign_id 101. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "subject": "Luxury Estate Services",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_044",
        "instruction": "Coordinate the investment consulting protocol for client 12 in relation to property HTX004 (listing 4) at 705900 with 7.0% 30-year financing. Utilize Investment Strategy communication using the investment_consulting template with campaign_id 101. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_045",
        "instruction": "Handle market analysis protocol for client 7 concerning property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. Utilize the market_analysis template to send Market Insights communication with campaign_id 101. Determine and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_046",
        "instruction": "Conduct portfolio review protocol for client 15 focusing on property HTX002 (listing 2) at 3975000 with 7.2% 30-year financing. Use the portfolio_review template to dispatch Portfolio Review communication with campaign_id 101. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_047",
        "instruction": "Handle the execution of the luxury marketing protocol for client 2 related to property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. Coordinate the delivery of premium luxury marketing and plan a luxury consultation on 2025-09-25T14:00:00Z-15:00:00Z at Office with 'Luxury property consultation' notes. Provide a report on the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_048",
        "instruction": "Coordinate the execution of client onboarding protocol for client 4 concerning property HTX004 (listing 4) at 705900 with 6.6% 30-year financing. Dispatch the Welcome Package communication utilizing the client_onboarding template with campaign_id 101. Provide a report on the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_049",
        "instruction": "Handle the purchase support protocol for client 16 in relation to property HTX005 (listing 5) priced at 674900 with 7.4% 30-year financing. Dispatch Purchase Support communication using purchase_support template with campaign_id 101. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "subject": "Comprehensive Purchase Analysis",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_050",
        "instruction": "Coordinate the first time buyer protocol for client 1 concerning property HTX006 (listing 6) valued at 225700 with 6.3% 30-year financing. Issue Welcome Package communication utilizing the first_time_buyer template with campaign_id 101. Determine and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_051",
        "instruction": "Handle the delivery of detailed market intelligence for client 7 concerning property HTX001 (listing 1) valued at 1500000 with 6.9% 30-year financing. Arrange a briefing on 2025-04-20T10:00:00Z-11:00:00Z at Office with 'Market intelligence consultation' notes, and calculate the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "name": "Market Intelligence",
                    "type": "market_intelligence",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "property_id": "HTX001",
                    "doc_type": "market_intelligence"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 2,
                    "subject": "Comprehensive Market Intelligence",
                    "template_code": "market_intelligence",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_052",
        "instruction": "Coordinate an exclusive property showing for client 18 concerning property HTX004 (listing 4) priced at 705900 with 7.1% 30-year financing. Organize a private showing consultation on 2025-04-15T14:00:00Z-15:00:00Z at HTX004 with 'Private property showing' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_053",
        "instruction": "Handle the investment consulting protocol for client 9 concerning property HTX005 (listing 5) at 674900 with 6.7% 30-year financing. Utilize the investment_consulting template with campaign_id 101 to send the Investment Strategy Analysis communication. Report on the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_054",
        "instruction": "Coordinate onboarding for client 14 purchasing HTX014 (listing 14) for 875000 with a 6.2% 30-year loan. Schedule a calendar event for 2025-09-24T09:00:00Z and provide a report on the interest paid.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 14
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX014"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 875000,
                    "interest_rate": 6.2,
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
                    "client_id": 14,
                    "broker_id": 3,
                    "property_id": "HTX014",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 3,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-24T09:00:00Z",
                    "end_at": "2025-09-24T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "1054277.28"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_055",
        "instruction": "Handle commercial sales protocol for client 20 concerning property HTX003 (listing 3) priced at 591000 with 7.3% financing over 30 years. Dispatch the Commercial Investment Opportunity communication utilizing the commercial_sales template with campaign_id 101. Provide a report on the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_056",
        "instruction": "Manage relocation protocol for client 3 in relation to property HTX005 (listing 5) valued at 674900 with 7.2% financing for 30 years. Arrange a relocation consultation on 2025-05-01T09:00:00Z-10:00:00Z at the Office including 'Executive relocation planning' notes. Submit a report on the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_057",
        "instruction": "Handle the luxury marketing protocol for client 10 concerning property HTX002 (listing 2) valued at 3975000 with 6.8% 30-year financing. Present an exclusive luxury property briefing and arrange a VIP consultation on 2025-05-05T15:00:00Z-16:00:00Z at Office, including 'Luxury property consultation' notes. Compute the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_058",
        "instruction": "Coordinate client onboarding protocol for client 16 related to property HTX003 (listing 3), priced at 591000 with 6.6% 30-year financing. Supply a comprehensive onboarding package along with a welcome consultation on 2025-05-10T11:00:00Z-12:00:00Z at Office, accompanied by 'New client onboarding session' notes. Calculate the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_059",
        "instruction": "Handle the first time buyer protocol for client 2 concerning property HTX006 (listing 6) valued at 225700 with 7.0% 30-year financing. Provide education for first-time buyers and arrange a buyer consultation on 2025-05-15T14:00:00Z-15:00:00Z at Office with 'First-time buyer guidance' notes. Calculate the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "subject": "First-Time Buyer Support",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_060",
        "instruction": "Carry out the investor outreach protocol for client 19 related to property HTX001 (listing 1) priced at 1500000 with 6.5% 30-year financing. Arrange a consultation on 2025-05-20T10:00:00Z-11:00:00Z at Office with 'Investment opportunity consultation' notes. Determine the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "subject": "Investment Opportunities",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_061",
        "instruction": "Handle purchase support protocol for client 5 concerning property HTX001 (listing 1) priced at 1500000 with 6.3% 30-year financing. Provide a thorough purchase analysis and arrange a purchase consultation on 2025-06-01T10:00:00Z-11:00:00Z at Office with notes 'Purchase strategy consultation'. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_062",
        "instruction": "Handle property showing protocol for client 12 related to property HTX005 (listing 5) valued at 674900 with 7.5% 30-year financing. Organize an exclusive property showing and set up the showing appointment on 2025-06-05T15:00:00Z-16:00:00Z at HTX005, including notes 'Exclusive property viewing'. Determine and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_063",
        "instruction": "Handle the VIP client protocol for client 8 concerning property HTX006 (listing 6) priced at 225700 with 6.8% 30-year financing. Offer exclusive VIP services and arrange the VIP consultation on 2025-06-10T14:30:00Z-15:30:00Z at Office, including 'VIP client consultation' notes. Provide the total payment amount report.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_064",
        "instruction": "Coordinate the property evaluation protocol for client 17 concerning property HTX004 (listing 4) valued at 705900 with 6.9% 30-year financing. Conduct a comprehensive property assessment along with a comparable analysis. Present the total interest amount report.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_065",
        "instruction": "Handle the commercial sales protocol for client 1 related to property HTX002 (listing 2) priced at 3975000 with 7.0% 30-year financing. Deliver a commercial investment analysis and coordinate a business meeting on 2025-06-15T09:00:00Z-10:00:00Z at the Office, including the 'Commercial investment strategy' notes. Report the amount for the monthly payment.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_066",
        "instruction": "Handle the first time buyer protocol for client 12 concerning property HTX008 (listing 8) priced at 330000 with 6.6% 30-year financing. Provide education for first-time buyers and arrange an educational meeting on 2025-10-25T10:30:00Z-11:30:00Z at the Office, accompanying it with 'First-time buyer education' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_067",
        "instruction": "Handle market intelligence protocol for client 15 concerning property HTX007 (listing 7) valued at 425600 with 6.5% 30-year financing. Arrange market review on 2025-06-25T11:00:00Z-12:00:00Z at Office with 'Market analysis review' notes. State the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 7
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
                    "name": "Market Intelligence",
                    "type": "market_intelligence",
                    "created_by": 3
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "property_id": "HTX007",
                    "doc_type": "market_intelligence"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 3,
                    "subject": "Comprehensive Market Intelligence",
                    "template_code": "market_intelligence",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_068",
        "instruction": "Manage relocation protocol for client 3 related to property HTX008 (listing 8) valued at 1275000 with 6.7% 30-year financing. Coordinate comprehensive relocation services and set up relocation planning on 2025-06-30T16:00:00Z-17:00:00Z at Office with 'Relocation strategy session' notes. Indicate the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
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
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_069",
        "instruction": "Handle client onboarding protocol for client 9 concerning property HTX011 (listing 11) at 495000 with 5.915% 30-year financing. Arrange comprehensive client onboarding and set up the onboarding meeting on 2025-09-28T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Determine the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 11
                },
            },
            {
                "name": "GetComparableProperties",
                "arguments": {
                    "property_id": "HTX011"
                },
            },
            {
                "name": "CalculateMortgage",
                "arguments": {
                    "principal": 495000,
                    "interest_rate": 5.915,
                    "loan_term_years": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Client Onboarding",
                    "type": "client_onboarding",
                    "created_by": 2
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "property_id": "HTX011",
                    "doc_type": "onboarding_package"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Comprehensive Client Onboarding",
                    "template_code": "client_onboarding",
                    "campaign_id": 101
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "title": "Client onboarding session",
                    "start_at": "2025-09-28T09:00:00Z",
                    "end_at": "2025-09-28T10:00:00Z",
                    "location": "Office",
                    "notes": "Client onboarding session"
                }
            }
        ],
        "outputs": [
                "563680.26"
        ]
    }
    ,
    {
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_070",
        "instruction": "Handle luxury marketing protocol for client 6 involving property HTX010 (listing 10) at 2850000 with 6.6% 30-year financing. Coordinate exclusive luxury marketing services and organize the luxury consultation on 2025-07-10T14:00:00Z-15:00:00Z at Office with 'Luxury property strategy' notes. Calculate the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_071",
        "instruction": "Handle client onboarding protocol for client 11 concerning property HTX001 (listing 1) at 1500000 with 6.4% 30-year financing. Provide a comprehensive onboarding package and arrange onboarding consultation on 2025-07-15T09:30:00Z-10:30:00Z at Office with 'Client onboarding session' notes. Specify the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_072",
        "instruction": "Coordinate property evaluation protocol for client 14 concerning property HTX002 (listing 2) at 3975000 with 6.8% 30-year financing. Provide a comprehensive property assessment with market valuation analysis. Specify the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_073",
        "instruction": "You are required to handle the investment consulting protocol for client 19 concerning property HTX003 (listing 3) at 895700 with 7.3% 30-year financing. Provide strategic investment guidance alongside financial modeling analysis. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_074",
        "instruction": "You are required to manage the commercial sales protocol for client 2 concerning property HTX004 (listing 4) at 705900 with 7.4% 30-year financing. Provide commercial investment analysis and schedule a commercial meeting on 2025-07-20T11:00:00Z-12:00:00Z at Office with 'Commercial sales strategy' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_075",
        "instruction": "Handle the VIP client protocol for client 7 concerning property HTX005 (listing 5) at 674900 with 6.9% 30-year financing. Ensure the provision of exclusive VIP services and coordinate a VIP consultation on 2025-07-25T15:30:00Z-16:30:00Z at Office with 'VIP client strategy session' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_076",
        "instruction": "Coordinate the portfolio review protocol for client 13 concerning property HTX001 (listing 1) at 1500000 with 6.2% 30-year financing. Provide a comprehensive portfolio assessment and arrange a portfolio consultation on 2025-07-30T09:00:00Z-10:00:00Z at Office with 'Portfolio strategy review' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_077",
        "instruction": "Handle estate management protocol for client 4 concerning property HTX002 (listing 2) at 3975000 with 6.6% 30-year financing. Provide luxury estate services and arrange an estate consultation on 2025-08-05T14:00:00Z-15:00:00Z at Office with 'Estate management strategy' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_078",
        "instruction": "Handle market intelligence protocol for client 16 related to property HTX004 (listing 4) at 705900 with 7.3% 30-year financing. Organize a market briefing on 2025-08-10T11:30:00Z-12:30:00Z at Office with 'Market intelligence consultation' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "FetchListingDetails",
                "arguments": {
                    "listing_id": 4
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
                    "type": "market_intelligence",
                    "created_by": 4
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "property_id": "HTX004",
                    "doc_type": "market_intelligence"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 4,
                    "subject": "Comprehensive Market Intelligence",
                    "template_code": "market_intelligence",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_079",
        "instruction": "Handle purchase support protocol for client 10 concerning property HTX003 (listing 3) at 591000 with 6.8% 30-year financing. Provide a comprehensive purchase analysis and arrange a purchase meeting on 2025-08-15T10:00:00Z-11:00:00Z at Office with 'Purchase strategy consultation' notes. Determine the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_080",
        "instruction": "Handle property showing protocol for client 7 concerning property HTX005 (listing 5) at 674900 with 7.1% 30-year financing. Organize an exclusive property showing and set a showing appointment on 2025-08-20T15:30:00Z-16:30:00Z at HTX005 with 'Private property viewing' notes. Calculate the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_081",
        "instruction": "Ensure the relocation protocol is handled for client 11 concerning property HTX006 (listing 6) at 225700 with 6.9% 30-year financing. Provide comprehensive relocation services and arrange a relocation consultation on 2025-08-25T10:30:00Z-11:30:00Z at Office with 'Relocation planning session' notes. Communicate the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_082",
        "instruction": "Manage the execution of luxury marketing protocol for client 8 in relation to property HTX007 (listing 7) at 425600 with 6.4% 30-year financing. Submit premium luxury marketing and set up a luxury consultation on 2025-08-30T14:30:00Z-15:30:00Z at Office with 'Luxury property strategy' notes. Convey the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "FetchListingDetails",
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
                    "subject": "Premium Luxury Marketing",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_083",
        "instruction": "Handle the first-time buyer protocol for client 19 concerning property HTX008 (listing 8) at 1275000 with 7.0% 30-year financing. Provide comprehensive first-time buyer guidance and arrange a buyer education session on 2025-09-05T09:30:00Z-10:30:00Z at Office with 'First-time buyer consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_084",
        "instruction": "Coordinate the investor outreach protocol for client 2 in relation to property HTX009 (listing 9) at 765300 with 6.8% 30-year financing. Supply an investment opportunity analysis and organize an investor meeting on 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Investment opportunity review' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_085",
        "instruction": "Handle the client onboarding protocol for client 15 related to property HTX010 (listing 10) at 2850000 with 6.5% 30-year financing. Prep a comprehensive onboarding package and organize the onboarding consultation on 2025-09-15T11:00:00Z-12:00:00Z at Office, including 'Client onboarding session' notes. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_086",
        "instruction": "Handle the VIP client protocol for client 17 concerning property HTX006 (listing 6) at 225700 with 6.3% 30-year financing. Provide an exemplary VIP service and arrange the VIP consultation on 2025-08-25T14:00:00Z-15:00:00Z at Office, with 'VIP client consultation' notes. Calculate and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_087",
        "instruction": "Handle the estate management protocol for client 14 for property HTX007 (listing 7) priced at 1490000 with a 6.9% 30-year financing plan. Provide luxury estate services and arrange an estate consultation on 2025-08-30T16:00:00Z-17:00:00Z at the Office with 'Estate management strategy' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_088",
        "instruction": "Handle the first time buyer protocol for client 8 for property HTX008 (listing 8) priced at 330000 with a 7.0% 30-year financing plan. Offer first-time buyer education and arrange an education meeting on 2025-09-05T10:30:00Z-11:30:00Z at the Office with 'First-time buyer education' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_089",
        "instruction": "Handle luxury marketing protocol for client 19 concerning property HTX009 (listing 9) priced at 400000 with 6.4% 30-year financing. Provide premium luxury marketing and arrange a luxury consultation for 2025-09-10T13:00:00Z-14:00:00Z at Office with 'Luxury property consultation' notes. Report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_090",
        "instruction": "Handle investment consulting protocol for client 15 concerning property HTX010 (listing 10) priced at 458500 with 6.7% 30-year financing. Provide strategic investment guidance and arrange an investment meeting on 2025-09-15T11:00:00Z-12:00:00Z at Office with 'Investment strategy consultation' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_091",
        "instruction": "Handle client onboarding protocol for client 1 regarding property HTX001 (listing 1) at 1500000 with 6.5% 30-year financing. Coordinate comprehensive client onboarding and set up the onboarding meeting on 2025-09-20T09:00:00Z-10:00:00Z at Office with 'Client onboarding session' notes. Provide the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_092",
        "instruction": "Conduct the luxury marketing protocol for client 2 concerning property HTX002 (listing 2) at 3975000 with 7.1% 30-year financing. Arrange premium luxury marketing and organize the luxury consultation on 2025-09-25T14:00:00Z-15:00:00Z at Office with 'Luxury property consultation' notes. Offer the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_093",
        "instruction": "Handle property evaluation protocol for client 3 concerning property HTX003 (listing 3) at 591000 with 6.6% 30-year financing. Deliver a comprehensive property analysis and arrange the evaluation meeting on 2025-09-30T11:00:00Z-12:00:00Z at Office with 'Property evaluation consultation' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_094",
        "instruction": "Handle the commercial sales protocol for client 18 in reference to property HTX004 (listing 4) at 705900 with 7.2% 30-year financing. Target the commercial property transaction and set up the commercial meeting on 2025-10-05T16:00:00Z-17:00:00Z at Office with 'Commercial transaction consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_095",
        "instruction": "Handle the property showing protocol for client 5 concerning property HTX005 (listing 5) priced at 674900 with 6.8% 30-year financing. Arrange for an exclusive property viewing and set the showing appointment on 2025-10-10T15:30:00Z-16:30:00Z at HTX005, including 'Private property viewing' notes. Provide the monthly payment amount report.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_096",
        "instruction": "Handle the relocation protocol for client 6 pertaining to property HTX006 (listing 6) valued at 225700 with 7.0% 30-year financing. Assist with client relocation activities and organize the relocation meeting on 2025-10-15T09:00:00Z-10:00:00Z at Office with 'Relocation consultation' noted. Convey the total payment amount report.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_097",
        "instruction": "Handle the portfolio review protocol for client 9 concerning property HTX007 (listing 7) valued at 1490000 with 6.4% 30-year financing. Deliver a comprehensive portfolio assessment and arrange a portfolio consultation scheduled for 2025-10-20T14:00:00Z-15:00:00Z at the Office, including 'Portfolio strategy review' notes. Calculate and report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_098",
        "instruction": "Coordinate the first time buyer protocol for client 12 related to property HTX008 (listing 8) priced at 330000 with 6.6% 30-year financing. Offer first-time buyer education and set up an education meeting on 2025-10-25T10:30:00Z-11:30:00Z at the Office, annotating 'First-time buyer education' notes. Compute and report the monthly payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_099",
        "instruction": "You are required to handle market intelligence protocol for client 11 concerning property HTX009 (listing 9) priced at 400000 with 7.3% 30-year financing. Provide quarterly market intelligence and arrange an intelligence meeting on 2025-10-30T16:00:00Z-17:00:00Z at Office complete with 'Market intelligence briefing' notes. Report the total payment amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "FetchListingDetails",
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
        "annotator": Irfan,
        "user_id": "RES_TASK_V4_100",
        "instruction": "You are required to handle purchase support protocol for client 20 related to property HTX010 (listing 10) valued at 458500 with 6.5% 30-year financing. Conduct a comprehensive purchase analysis and set up a purchase meeting on 2025-11-05T11:00:00Z-12:00:00Z at Office with 'Purchase strategy consultation' notes. Report the total interest amount.",
        "actions": [
            {
                "name": "FindClients",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "FetchListingDetails",
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
