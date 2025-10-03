
tasks = [
    {
        "annotator": faris,
        "user_id": "faris_001_comp_analysis_client13_htx025",
        "instruction": "Develop a comparable analysis for client 13 who is interested in property HTX025, including 1 comparable selection. Dispatch an email to the client.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "13"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": [
                        "7",
                        "4",
                        "5",
                        "13"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "5"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "13",
                    "broker_id": "5",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_002_comp_client10_htx021_skip_review",
        "instruction": "Produce a comparable report for client 10, interested in HTX021, with 1 comparable selection. Forward an email to the client.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "10"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "10",
                    "created_by_broker_id": "11",
                    "subject_property_id": "HTX021",
                    "client_neighborhoods": [
                        "13",
                        "1",
                        "12"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX030",
                            "similarity_score": 0.868,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "11"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "10",
                    "broker_id": "11",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_003_investment_comp_client12_htx044",
        "instruction": "You need to confirm mortgage rates for client 20, determine their payment terms, generate a mortgage audit entry, and dispatch a general update email with the mortgage specifics.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 785,
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "1",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "20",
                    "metadata_json": {
                        "mortgage_profile_id": "20"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "20",
                    "broker_id": "1",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_004_luxury_comp_client13_htx025_amenities",
        "instruction": "It is necessary to prepare a comp report for client 13 on HTX025.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "13"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": [
                        "7",
                        "4",
                        "5",
                        "13"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "5"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_005_montrose_comp_client11_htx012",
        "instruction": "Ensure you create an analysis for client 11 assessing HTX012 for comparison purposes.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "11"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "11",
                    "created_by_broker_id": "6",
                    "subject_property_id": "HTX012",
                    "client_neighborhoods": [
                        "7",
                        "3",
                        "11",
                        "14"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.57,
                            "selection_reason": "Fair price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "6"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_006_budget_comp_client7_htx036_400k",
        "instruction": "Ensure you construct a market comparison for client 3 focusing on HTX021. Compute property metrics and produce a comp report.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "3",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX021",
                    "client_neighborhoods": [
                        "1",
                        "12",
                        "2",
                        "4",
                        "5"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX030",
                            "similarity_score": 0.868,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "CalculatePropertyMetrics",
                "arguments": {
                    "subject_property_id": "HTX021",
                    "comparable_properties": [
                        "HTX030"
                    ],
                    "client_budget": {
                        "client_id": "3",
                        "price_max": 631914
                    }
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_007_medical_center_comp_client8_htx049",
        "instruction": "Locate up to 4 open houses for client 5 near property HTX025 scheduled for 2025-08-30 and send a summary via email.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX025"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX025",
                    "max_results": 4,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035"
                    ],
                    "date": "2025-08-30"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "5",
                    "broker_id": "1",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_008_first_time_buyer_client2_htx017",
        "instruction": "Develop a mortgage profile for client 17, including a loan of $548,318 and a down payment of $109,032, then proceed to calculate their mortgage payment.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "17"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 699,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateMortgageProfile",
                "arguments": {
                    "client_id": "17",
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 699,
                    "region": "AZ",
                    "annual_income": 78851
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_009_heights_analysis_client15_htx001",
        "instruction": "Handle a comp analysis for client 15 evaluating HTX001 in The Hills neighborhood",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "15"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Heights"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "15",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX001",
                    "client_neighborhoods": [
                        "4"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX007",
                            "similarity_score": 0.918,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "8"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_010_river_oaks_analysis_client16_htx007",
        "instruction": "Coordinate a comparable analysis for client 16 considering HTX007 in Desert Ridge",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "16"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Desert Ridge"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "16",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX007",
                    "client_neighborhoods": [
                        "5"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.918,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "8"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_011_condo_analysis_client18_htx030",
        "instruction": "You are required to create a comparable report for client 18 assessing HTX030",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "18"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "18",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": [
                        "13",
                        "9",
                        "14",
                        "15",
                        "11"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "5"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_012_comp_analysis_client9_htx024",
        "instruction": "You need to compile a comparable analysis for client 9 reviewing HTX024. You are broker 9.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "9"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "9",
                    "created_by_broker_id": "9",
                    "subject_property_id": "HTX024",
                    "client_neighborhoods": [
                        "1",
                        "12",
                        "14",
                        "3"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "9"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_013_family_weekend_open_houses_client15_htx042",
        "instruction": "As broker 8, identify up to 2 open houses near property HTX042 for client 15 on 2025-08-23. Arrange them as 'Weekend open houses schedule' on 2025-08-24 in Phoenix, AZ, and dispatch a summary email to the client.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX042"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX042",
                    "max_results": 2,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX042",
                        "HTX002",
                        "HTX018"
                    ],
                    "date": "2025-08-23"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "8",
                    "client_id": "15",
                    "title": "Weekend open houses schedule",
                    "date": "2025-08-24",
                    "location": "Phoenix, AZ",
                    "source": "viewing"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "15",
                    "broker_id": "8",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX042",
                        "HTX002",
                        "HTX018"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_014_campaign_curation_client5_htx026",
        "instruction": "Tasked with curating a 'Townhouse Spotlight' likely_buyer campaign (id: 3) for client 5, your role is to collate the listing data for HTX026, formulate a briefing document, and send a briefing email to the client. You are broker 14.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX026"
                    ]
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "5",
                    "created_by": "14"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "5",
                    "broker_id": "14",
                    "template_code": "briefing",
                    "campaign_id": "3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_015_client_comms_client4_briefing",
        "instruction": "You are organizing a briefing for client 4; review recent emails from 2025-07-01T00:00:00Z onwards and send a follow-up. Return the client's mortgage id.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "4",
                    "since_date": "2025-07-01T00:00:00Z"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "4",
                    "created_by": "2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "4",
                    "broker_id": "2",
                    "template_code": "briefing"
                }
            }
        ],
        "outputs": [
                {
                    "mortgage_id": 4
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_016_plan_route_client4_broker2",
        "instruction": "As broker 2, organize a 3-stop viewing route for client 4 scheduled for 2025-09-20, beginning at the client's commute address, ensuring the first stop is HTX003. Hops should remain under 25 minutes. Avoid verifying the creation of the route WA setting a calendar event.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX003",
                    "max_results": 2,
                    "status_filter": [
                        "active",
                        "pending",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "ValidateDriveTimeConstraints",
                "arguments": {
                    "property_list": [
                        "HTX003",
                        "HTX025",
                        "HTX034"
                    ],
                    "max_hop_minutes": 25
                },
            },
            {
                "name": "CalculateRouteOptimization",
                "arguments": {
                    "property_list": [
                        "HTX003",
                        "HTX025",
                        "HTX034"
                    ],
                    "start_address": "201 Caroline St, Phoenix, AZ",
                    "max_hop_minutes": 25
                },
            },
            {
                "name": "CreateRouteEntry",
                "arguments": {
                    "client_id": "4",
                    "route_date": "2025-09-20",
                    "stops_ordered_json": [
                        "HTX003",
                        "HTX025",
                        "HTX034"
                    ],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "2"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_017_open_house_client11_broker6",
        "instruction": "Act as broker 6 and locate 2 more open houses with the date 2025-08-30 for client 11 at property HTX012. Arrange any located as 'Arcadia Open House Tour' CO Arcadia, Phoenix on 2025-08-31 and provide a summary via email to the client.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX012"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX012",
                    "max_results": 2,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX012",
                        "HTX038",
                        "HTX017"
                    ],
                    "date": "2025-08-30"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "6",
                    "client_id": "11",
                    "title": "Arcadia Open House Tour",
                    "date": "2025-08-31",
                    "location": "Arcadia, Phoenix",
                    "source": "viewing"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "11",
                    "broker_id": "6",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX012",
                        "HTX038",
                        "HTX017"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_018_campaign_update_broker1",
        "instruction": "Assume the role of broker 1 to deliver a market intelligence briefing on property HTX015 to client 1 as part of the 'August 2025 Market Intelligence' campaign (ID 1).",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX015"
                    ]
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "1",
                    "created_by": "1"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "briefing",
                    "campaign_id": 1
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_019_client_followup_client3_broker3",
        "instruction": "As broker 3, retrieve the details for client 3 along with their emails starting from 2025-08-01, and compose a follow-up email regarding property HTX030 using the follow_up template.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "3",
                    "date": "2025-08-01"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "3",
                    "broker_id": "3",
                    "template_code": "follow_up",
                    "property_id": "HTX030"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_020_mortgage_search_client6_broker6",
        "instruction": "Act as broker 6. Generate a comp report for client 6 concerning property HTX030 and inform the client about the completion of the report.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "6"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "6",
                    "subject_property_id": "HTX030",
                    "max_selections": 1,
                    "created_by_broker_id": "6"
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "6"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "6",
                    "broker_id": "6",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_021_urgent_route_client9_broker9",
        "instruction": "Act as broker 9 and devise a 3-stop viewing itinerary for client 9 on 2025-09-16. Begin at the client's commute address with HTX029 as the initial stop. Each hop should be less than 15 minutes. Avoid confirming route creation WA setting up a calendar appointment.",
        "actions": [
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX029",
                    "max_results": 2,
                    "status_filter": [
                        "active",
                        "pending",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "9"
                },
            },
            {
                "name": "ValidateDriveTimeConstraints",
                "arguments": {
                    "property_list": [
                        "HTX029",
                        "HTX028",
                        "HTX039"
                    ],
                    "max_hop_minutes": 15
                },
            },
            {
                "name": "CalculateRouteOptimization",
                "arguments": {
                    "property_list": [
                        "HTX029",
                        "HTX028",
                        "HTX039"
                    ],
                    "start_address": "201 Caroline St, Phoenix, AZ",
                    "max_hop_minutes": 15
                },
            },
            {
                "name": "CreateRouteEntry",
                "arguments": {
                    "client_id": "9",
                    "route_date": "2025-09-16",
                    "stops_ordered_json": [
                        "HTX029",
                        "HTX028",
                        "HTX039"
                    ],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "9"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_022_new_campaign_broker10",
        "instruction": "As broker 10, initiate a new 'First-Time Buyer Education Series' likely_buyer campaign utilizing HTX030 and HTX032. Compile a briefing document for client 17, who matches well. Gather their complete context and dispatch a first time buyer email to the client. Provide the client's maximum price.",
        "actions": [
            {
                "name": "CreateCampaignEntry",
                "arguments": {
                    "campaign_name": "First-Time Buyer Education Series",
                    "campaign_type": "likely_buyer",
                    "created_by": "10"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX030",
                        "HTX032"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "17"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "17",
                    "created_by": "10"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "17",
                    "broker_id": "10",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": [
                        "HTX030",
                        "HTX032"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "MAX_PRICE": 284669
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_023_report_details_client4_broker2",
        "instruction": "Acting as broker 2, retrieve the details for comp report 1 and obtain the comprehensive context for client 4. Acquire the details for the subject property and then produce a new briefing document, followed by sending a follow-up email. Provide the client's mortgage id.",
        "actions": [
            {
                "name": "FetchCompReportDetails",
                "arguments": {
                    "report_id": "1"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX003"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "4",
                    "created_by": "2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "4",
                    "broker_id": "2",
                    "template_code": "follow_up"
                }
            }
        ],
        "outputs": [
                4
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_024_mortgage_check_client18_broker6",
        "instruction": "As broker 6, compute client 18's potential mortgage installment on a 700000 loan, considering a 10000 down payment at a 3.99% interest rate over a 15-year term, and send them the information utilizing a general_update template. Schedule a calendar event named 'Mortgage Check' for 2025-09-20 to discuss it, with the location set to 'Phone Call' and source 'general_update'. Provide the monthly installment.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "18"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 700000,
                    "down_payment": 10000,
                    "interest_rate": 3.99,
                    "term_years": 15
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "6",
                    "client_id": "18",
                    "title": "Mortgage Check",
                    "date": "2025-09-20",
                    "location": "Phone Call",
                    "source": "general_update"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "18",
                    "broker_id": "6",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": [
                {
                    "MONTHLY_PAYMENT": 5174
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_025_create_comp_report_with_metrics_client12_broker7",
        "instruction": "As broker 7, handle a comparable analysis for client 12 concerning property HTX045, using up to 2 comparables, and produce the report document.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "12"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "12",
                    "created_by_broker_id": "7",
                    "subject_property_id": "HTX045",
                    "client_neighborhoods": [
                        "11",
                        "1",
                        "13"
                    ],
                    "max_selections": 2
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX048",
                            "similarity_score": 0.923,
                            "selection_reason": "Strong price fit"
                        },
                        {
                            "comp_property_id": "HTX043",
                            "similarity_score": 0.897,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "7"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_026_comp_analysis_client9_htx024",
        "instruction": "Coordinate a comparable analysis for client 9 focusing on HTX024. You are broker 9.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "9"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "9",
                    "created_by_broker_id": "9",
                    "subject_property_id": "HTX024",
                    "client_neighborhoods": [
                        "1",
                        "12",
                        "14",
                        "3"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "9"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_027_open_house_email_client5_broker6",
        "instruction": "As broker 6, locate up to 4 more open houses on the date 2025-08-30 for client 5 at property HTX025. Subsequently, prepare and dispatch an email summary of these houses.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX025"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX025",
                    "max_results": 4,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035"
                    ],
                    "date": "2025-08-30"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "5",
                    "broker_id": "6",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_028_briefing_for_campaign_client_7_broker15",
        "instruction": "Being broker 15, initially retrieve the specifics for the 'Post-Closing Client Care' campaign (ID 4) and then obtain the full context for client 7. Leverage this data to craft a briefing document for client 7 and forward a post-closing check-CO email.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "4"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "7"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "7",
                    "created_by": "15"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "7",
                    "broker_id": "15",
                    "template_code": "briefing",
                    "campaign_id": "4"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_029_review_client_comms_client_8_broker12",
        "instruction": "As broker 12, examine all communications such as calendar events and emails for client 8, create a briefing document, and dispatch a briefing email to arrange the next steps.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "8"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "8"
                },
            },
            {
                "name": "FetchCalendarEventsForClient",
                "arguments": {
                    "client_id": "8"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "8",
                    "created_by": "12"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "8",
                    "broker_id": "12",
                    "template_code": "briefing"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_030_financial_check_client19_broker1",
        "instruction": "Being broker 1, retrieve the mortgage profile for client 19 to inform them about their affordability. Identify the best rates and email a summary of their potential monthly payment.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "19"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": "702",
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 298612,
                    "down_payment": 26893,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "19",
                    "broker_id": "1",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_031_create_and_verify_route_client2_broker1",
        "instruction": "As broker 1, organize a 3-stop viewing route for client 2 on 2025-09-25, commencing from the client's commute address and including stops at HTX017, HTX026, and HTX040. Do not confirm the route's creation WA set up a calendar event.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "ValidateDriveTimeConstraints",
                "arguments": {
                    "property_list": [
                        "HTX017",
                        "HTX026",
                        "HTX040"
                    ],
                    "max_hop_minutes": 15
                },
            },
            {
                "name": "CalculateRouteOptimization",
                "arguments": {
                    "property_list": [
                        "HTX017",
                        "HTX026",
                        "HTX040"
                    ],
                    "start_address": "201 Caroline St, Phoenix, AZ",
                    "max_hop_minutes": 15
                },
            },
            {
                "name": "CreateRouteEntry",
                "arguments": {
                    "client_id": "2",
                    "route_date": "2025-09-25",
                    "stops_ordered_json": [
                        "HTX017",
                        "HTX026",
                        "HTX040"
                    ],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_032_comp_report_for_client13_broker5",
        "instruction": "Acting as broker 5, prepare a new comparable analysis for client 13 concerning property HTX025.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "13"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": [
                        "7",
                        "4",
                        "5",
                        "13"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "5"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_034_neighborhood_and_comps_client15_broker8",
        "instruction": "As broker 8, your task is to prepare a comp report for property HTX001 in neighborhood 4 with up to 3 comparables and send it via email to client 15.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "15"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "15",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX001",
                    "client_neighborhoods": [
                        4
                    ],
                    "max_selections": 3
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX007",
                            "similarity_score": 0.918,
                            "selection_reason": "Strong price fit"
                        },
                        {
                            "comp_property_id": "HTX050",
                            "similarity_score": 0.892,
                            "selection_reason": "Strong price fit"
                        },
                        {
                            "comp_property_id": "HTX019",
                            "similarity_score": 0.852,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "8"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "15",
                    "broker_id": "8",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_035_create_mortgage_audit_client_17",
        "instruction": "As broker 1, once you have developed a mortgage profile for client 17 with a loan of $548,318 and a down payment of $109,032, compute their mortgage payment.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "17"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 699,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateMortgageProfile",
                "arguments": {
                    "client_id": "17",
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 699,
                    "region": "AZ",
                    "annual_income": 78851
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 548318,
                    "down_payment": 109032,
                    "interest_rate": 4.004,
                    "term_years": 15
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_036_plan_route_with_inactive_broker_client5_broker1",
        "instruction": "Acting as broker 1, who is covering for inactive broker 5, organize a route for client 5's property viewing on 2025-09-23, beginning from their commute address and including properties HTX030, HTX025, and HTX032. Avoid confirming the route's creation WA setting up a calendar event.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "5"
                },
            },
            {
                "name": "ValidateDriveTimeConstraints",
                "arguments": {
                    "property_list": [
                        "HTX030",
                        "HTX025",
                        "HTX032"
                    ],
                    "start_address": "1500 McKinney St, Phoenix, AZ",
                    "max_hop_minutes": 30
                },
            },
            {
                "name": "CalculateRouteOptimization",
                "arguments": {
                    "property_list": [
                        "HTX030",
                        "HTX025",
                        "HTX032"
                    ],
                    "start_address": "1500 McKinney St, Phoenix, AZ",
                    "max_hop_minutes": 30
                },
            },
            {
                "name": "CreateRouteEntry",
                "arguments": {
                    "client_id": "5",
                    "route_date": "2025-09-23",
                    "stops_ordered_json": [
                        "HTX030",
                        "HTX025",
                        "HTX032"
                    ],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_037_generate_and_send_briefing_client_20_broker10",
        "instruction": "As broker 10, evaluate the profile and past communication of client 20, compile a client briefing document, and subsequently email it to them utilizing the briefing template.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "FetchCalendarEventsForClient",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "20",
                    "created_by": "10"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "20",
                    "broker_id": "10",
                    "template_code": "briefing"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_038_find_investment_properties_client18_broker6",
        "instruction": "As broker 6, locate up to 5 properties suitable for Client 18, an investor, and send them the listing through campaign 8.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "18"
                },
            },
            {
                "name": "SearchListingsByCriteria",
                "arguments": {
                    "neighborhoods_json": [
                        13,
                        9,
                        14,
                        15,
                        11
                    ],
                    "price_min": 273024,
                    "price_max": 868888,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ],
                    "max_results": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "18",
                    "broker_id": "6",
                    "template_code": "investment_alert",
                    "campaign_id": "8"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_039_sales_history_and_metrics_client3_broker3",
        "instruction": "Acting as broker 3, provide Client 3 with a comprehensive analysis of the property HTX021 by finding comparable properties and preparing a full report, including metrics calculation.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "3",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX021",
                    "client_neighborhoods": [
                        "1",
                        "12",
                        "2",
                        "4",
                        "5"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX030",
                            "similarity_score": 0.868,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "CalculatePropertyMetrics",
                "arguments": {
                    "subject_property_id": "HTX021",
                    "comparable_properties": [
                        "HTX030"
                    ],
                    "client_budget": {
                        "client_id": "3",
                        "price_max": 631914
                    }
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_040_send_client6_broker3",
        "instruction": "You are broker 3. Assemble a full comparable analysis report for client 6 on property HTX044, including generating documents, and dispatch the comp report delivery email.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "6"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "6",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX044",
                    "client_neighborhoods": [
                        8,
                        12,
                        6,
                        5
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX027",
                            "similarity_score": 0.922,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "3"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "6",
                    "broker_id": "3",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_041_route_from_route_client_4_broker_2",
        "instruction": "You are broker 2. Retrieve the latest route for client 4, then arrange a new calendar event with location 'Phone Call' on 2025-09-21 entitled 'Follow-up on Property Tour' to organize a follow-up call regarding it and send an email to the client.",
        "actions": [
            {
                "name": "FetchRouteDetails",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "2",
                    "client_id": "4",
                    "title": "Follow-up on Property Tour",
                    "date": "2025-09-21",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "4",
                    "broker_id": "2",
                    "template_code": "follow_up"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_042_fetch_multiple_listings_and_email_client_10_broker11",
        "instruction": "As broker 11, gather listings HTX021, HTX050, and HTX018 for client 10, review their preferences and the communication from the past 30 days, and subsequently send them an email with a summary of these listings.",
        "actions": [
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX021",
                        "HTX050",
                        "HTX018"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "10"
                },
            },
            {
                "name": "CheckRecentEmailHistory",
                "arguments": {
                    "client_id": "10",
                    "template_code": "listing_summary",
                    "days_lookback": 30
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "10",
                    "broker_id": "11",
                    "template_code": "listing_summary",
                    "property_id": [
                        "HTX021",
                        "HTX050",
                        "HTX018"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_043_update_report_status_and_notify_broker_report_2",
        "instruction": "As broker 14, update the status of comp report 2 to 'sent_to_broker'. Following this update, retrieve the report details, create an audit event (report_status_update) for compliance tracking, and then inform the client via email that the report has been sent.",
        "actions": [
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": "2",
                    "new_status": "sent_to_broker",
                    "actor_id": "14"
                },
            },
            {
                "name": "FetchCompReportDetails",
                "arguments": {
                    "report_id": "2"
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "14",
                    "action": "report_status_update",
                    "entity_type": "comp_report",
                    "entity_id": "2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "10",
                    "broker_id": "14",
                    "template_code": "report_followup",
                    "property_id": "HTX021"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_044_comp_report_inactive_broker_client_2_broker_1",
        "instruction": "Being broker 1, prepare a comparable report for client 2 who is interested in HTX017, and verify the most favorable mortgage rate.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": "716",
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 679753,
                    "down_payment": 49429,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "2",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX017",
                    "client_neighborhoods": [
                        "11",
                        "1"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX026",
                            "similarity_score": 0.879,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_045_generate_uri_and_update_report_3",
        "instruction": "As broker 6, prepare the document for comp report ID 3, send it to the client via email using the comp_report_delivery template, then change the report status to 'sent_to_client'.",
        "actions": [
            {
                "name": "FetchCompReportDetails",
                "arguments": {
                    "report_id": "3"
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "3",
                    "created_by": "6"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "11",
                    "broker_id": "6",
                    "template_code": "comp_report_delivery"
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": "3",
                    "new_status": "sent_to_client",
                    "actor_id": "6"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_046_viewing_route_client20_broker2",
        "instruction": "As broker 2, organize a 3-stop viewing itinerary for client 20 on 2025-09-28, commencing from the client's commuting address, with HTX042 as the first stop. Ensure hops are within 45 minutes. Avoid confirming route creation WA making a calendar appointment.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX042",
                    "max_results": 2,
                    "status_filter": [
                        "active",
                        "pending",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "ValidateDriveTimeConstraints",
                "arguments": {
                    "property_list": [
                        "HTX042",
                        "HTX002",
                        "HTX018"
                    ],
                    "max_hop_minutes": 45
                },
            },
            {
                "name": "CalculateRouteOptimization",
                "arguments": {
                    "property_list": [
                        "HTX042",
                        "HTX018",
                        "HTX002"
                    ],
                    "start_address": "4 Riverway, Phoenix, AZ",
                    "max_hop_minutes": 45
                },
            },
            {
                "name": "CreateRouteEntry",
                "arguments": {
                    "client_id": "20",
                    "route_date": "2025-09-28",
                    "stops_ordered_json": [
                        "HTX042",
                        "HTX018",
                        "HTX002"
                    ],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "2"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_047_open_house_search_client1_broker1",
        "instruction": "As broker 1, identify up to 5 more open houses (excluding HTX001) for client 1 in proximity to property HTX001 for the weekend of 2025-08-25, and send a summary via email to the client.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX001"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX001",
                    "max_results": 5,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX016",
                        "HTX023",
                        "HTX032",
                        "HTX017",
                        "HTX025"
                    ],
                    "date": "2025-08-25"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX016",
                        "HTX023",
                        "HTX032",
                        "HTX017",
                        "HTX025"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_048_new_homeowner_campaign_client_3_broker3",
        "instruction": "As broker 2, locate up to 4 more open houses on the date 2025-08-30 for client 5 at property HTX025. Afterward, prepare and send an email summarizing these houses.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX025"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX025",
                    "max_results": 4,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035"
                    ],
                    "date": "2025-08-30"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "5",
                    "broker_id": "2",
                    "template_code": "open_house_summary",
                    "property_id": [
                        "HTX025",
                        "HTX032",
                        "HTX017",
                        "HTX038",
                        "HTX035"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_049_review_calendar_client14_broker1",
        "instruction": "Acting as broker 1, now replacing broker 14, evaluate the calendar events and email history for client 14. Gather their comprehensive context, create a briefing document for your assessment, then dispatch a follow-up email to introduce yourself and arrange further actions.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "14"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "14"
                },
            },
            {
                "name": "FetchCalendarEventsForClient",
                "arguments": {
                    "client_id": "14"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "14",
                    "created_by": "1"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "14",
                    "broker_id": "1",
                    "template_code": "briefing"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_050_mortgage_prequal_client1_broker1",
        "instruction": "As broker 1, client 1 requires a mortgage pre-qualification summary. Gather their profile, identify optimal rates based on the credit score, determine payment details on a 750000 loan, and send an email to the client.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": "647",
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 750000,
                    "down_payment": 41652,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_051_comp_analysis_client19_htx030_broker1",
        "instruction": "As broker 1, develop a comparable analysis for client 19 who is interested in HTX030 with one comparable selection and prepare the necessary documentation.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "19"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "19",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": [
                        "10",
                        "5"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_052_report_for_new_client_client11_broker6",
        "instruction": "As broker 6, prepare a comparable analysis for your new client 11 regarding property HTX012.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "11"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "11",
                    "created_by_broker_id": "6",
                    "subject_property_id": "HTX012",
                    "client_neighborhoods": [
                        "7",
                        "3",
                        "11",
                        "14"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.57,
                            "selection_reason": "Fair price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "6"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_053_comp_analysis_email_client13_htx025",
        "instruction": "Develop a comp report for client 13 on HTX025 and send it via email.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "13"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "13",
                    "created_by_broker_id": "5",
                    "subject_property_id": "HTX025",
                    "client_neighborhoods": [
                        "7",
                        "4",
                        "5",
                        "13"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX023",
                            "similarity_score": 0.913,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "5"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "13",
                    "broker_id": "5",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_054_neighborhood_comps_client_1_broker1",
        "instruction": "You are broker 1. Client 1 has shown interest in Central City. Assemble a comp report for them on property HTX003 with 2 comparables and email it.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Central City"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "1",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX003",
                    "client_neighborhoods": [
                        1
                    ],
                    "max_selections": 2
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX026",
                            "similarity_score": 0.908,
                            "selection_reason": "Strong price fit"
                        },
                        {
                            "comp_property_id": "HTX032",
                            "similarity_score": 0.905,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "comp_report_delivery"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_055_audit_mortgage_creation_client20",
        "instruction": "You are broker 1. A mortgage profile was established for client 20. Confirm their mortgage rates and compute payment terms, prepare a mortgage audit entry for compliance, and forward them a general update email with the mortgage details.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 785,
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "1",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "20",
                    "metadata_json": {
                        "mortgage_profile_id": "20"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "20",
                    "broker_id": "1",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_056_route_planning_client10_broker11",
        "instruction": "As broker 11, organize a 3-stop viewing itinerary for client 10 on 2025-09-29, commencing from the client's commute address, with the initial visit at HTX021. Identify the 2 closest listings to HTX021 for the subsequent stops, ensuring transitions are under 30 minutes. Do not validate the route creation WA make a calendar entry.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "10"
                },
            },
            {
                "name": "FindNearbyListings",
                "arguments": {
                    "subject_property_id": "HTX021",
                    "max_results": 2,
                    "status_filter": [
                        "active",
                        "pending",
                        "for_sale"
                    ]
                },
            },
            {
                "name": "ValidateDriveTimeConstraints",
                "arguments": {
                    "property_list": [
                        "HTX021",
                        "HTX018",
                        "HTX002"
                    ],
                    "max_hop_minutes": 30
                },
            },
            {
                "name": "CalculateRouteOptimization",
                "arguments": {
                    "property_list": [
                        "HTX021",
                        "HTX018",
                        "HTX002"
                    ],
                    "start_address": "1500 McKinney St, Phoenix, AZ",
                    "max_hop_minutes": 30
                },
            },
            {
                "name": "CreateRouteEntry",
                "arguments": {
                    "client_id": "10",
                    "route_date": "2025-09-29",
                    "stops_ordered_json": [
                        "HTX021",
                        "HTX018",
                        "HTX002"
                    ],
                    "map_url": "https://maps.google.com/route/optimized_tour_001",
                    "created_by_broker_id": "11"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_057_briefing_and_email_client16_broker8",
        "instruction": "Acting as broker 8, retrieve the property details for HTX030, the complete context, and email correspondence associated with client 16. Compile a briefing document, arrange a follow-up Phone Call titled 'Discuss Briefing' for 2025-09-20 to review the briefing, and then send the briefing via email utilizing the briefing template. Provide the street view url for the property.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX030"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "16"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "16"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "16",
                    "created_by": "8"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "8",
                    "client_id": "16",
                    "title": "Discuss Briefing",
                    "date": "2025-09-20",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "16",
                    "broker_id": "8",
                    "template_code": "briefing"
                }
            }
        ],
        "outputs": [
                {
                    "STREET_VIEW_URL": "https://maps.google.com/?q=29.7377,-95.4017&layer=c"
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_058_investor_search_client13_broker6",
        "instruction": "As broker 6, assist investor client 13 in finding a property. Look up 1 active listing in neighborhoods 7, 4, 5, and 13 with a price cap of 566116, then schedule a calendar event titled 'Investor Search Follow-up' for 2025-09-23, setting the location as 'Phone Call' and source to 'follow_up', and send them an email.",
        "actions": [
            {
                "name": "SearchListingsByCriteria",
                "arguments": {
                    "neighborhoods_json": [
                        7,
                        4,
                        5,
                        13
                    ],
                    "status_filter": "active",
                    "max_results": 1,
                    "price_max": 566116
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "6",
                    "client_id": "13",
                    "title": "Investor Search Follow-up",
                    "date": "2025-09-23",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "13",
                    "broker_id": "6",
                    "template_code": "investment_alert"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_059_sales_history_and_metrics_client_9_broker_9",
        "instruction": "As broker 9, prepare a comparable analysis for client 9, using HTX024 as the subject property.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "9"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "9",
                    "created_by_broker_id": "9",
                    "subject_property_id": "HTX024",
                    "client_neighborhoods": [
                        "1",
                        "12",
                        "14",
                        "3"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "9"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_060_comp_analysis_metrics_client8_htx049",
        "instruction": "Craft a comp analysis for client 8 taking into account HTX049 along with relevant metrics.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "8"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "8",
                    "created_by_broker_id": "12",
                    "subject_property_id": "HTX049",
                    "client_neighborhoods": [
                        "10",
                        "2",
                        "4"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX024",
                            "similarity_score": 0.915,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "CalculatePropertyMetrics",
                "arguments": {
                    "subject_property_id": "HTX049",
                    "comparable_properties": [
                        "HTX024"
                    ],
                    "client_budget": {
                        "client_id": "8",
                        "price_max": 434224
                    }
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "12"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_061_fetch_route_and_followup_client_10_broker11",
        "instruction": "As broker 11, gather the complete context and the most recent route for client 10. Then, organize a calendar event to arrange a follow-up call regarding their tour on 2025-09-30. Use the title 'Follow-up on Home Tour' with location 'Phone Call'. Present the listing price of each property in the route. Email the client to confirm the follow-up.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "10"
                },
            },
            {
                "name": "FetchRouteDetails",
                "arguments": {
                    "client_id": "10"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "11",
                    "client_id": "10",
                    "title": "Follow-up on Home Tour",
                    "date": "2025-09-30",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX021"
                },
            },
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX050"
                },
            },
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX018"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "10",
                    "broker_id": "11",
                    "template_code": "follow_up"
                }
            }
        ],
        "outputs": [
                {
                    "HTX021": 874000,
                    "HTX050": 1549000,
                    "HTX018": 4300000
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_062_fetch_multiple_listings_client_1_broker1",
        "instruction": "Serve as broker 1. Obtain listings HTX001, HTX007, and HTX011 for client 1, assess their profile and interest in open houses for the weekend of 2025-08-25, set up a follow-up call with location: Phone Call, titled 'Follow-up on Desert Ridge Listings' for 2025-09-23, and subsequently send them an email summarizing these Desert Ridge properties.",
        "actions": [
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX001",
                        "HTX007",
                        "HTX011"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "FetchOpenHouseOpportunities",
                "arguments": {
                    "property_candidates": [
                        "HTX001",
                        "HTX007",
                        "HTX011"
                    ],
                    "date": "2025-08-25"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "1",
                    "client_id": "1",
                    "title": "Follow-up on Desert Ridge Listings",
                    "date": "2025-09-23",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "listing_summary",
                    "property_id": [
                        "HTX001",
                        "HTX007",
                        "HTX011"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_063_update_report_status_report_7_broker1",
        "instruction": "Act as broker 1. Retrieve the complete context for client 7, revise the status of comp report 7 to 'sent_to_client' and prepare a briefing document for them.",
        "actions": [
            {
                "name": "FetchCompReportDetails",
                "arguments": {
                    "report_id": "7"
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": "7",
                    "new_status": "sent_to_client",
                    "actor_id": "1"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "7"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "7",
                    "created_by": "1"
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "1",
                    "action": "created",
                    "entity_type": "briefing_document",
                    "entity_id": "21",
                    "metadata_json": {
                        "briefing_document_id": "21"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_064_comp_report_inactive_broker_client_5_broker_1",
        "instruction": "You are broker 1, assuming responsibility for inactive broker 5. Review the sales history of property HTX030 and prepare a comparable report for client 5 interested in HTX030 with 1 comparable selection.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "5"
                },
            },
            {
                "name": "FetchPropertySalesHistory",
                "arguments": {
                    "property_id": "HTX030"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "5",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": [
                        6,
                        2,
                        4,
                        10
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_065_generate_uri_and_update_report_8_complex",
        "instruction": "As broker 12, for comp report 8, you need to generate the report document and update its status to 'sent_to_client'. Furthermore, initiate a new 'general_update' campaign named 'Report 8 Follow-up Campaign' and dispatch a 'report_followup' email to the client.",
        "actions": [
            {
                "name": "FetchCompReportDetails",
                "arguments": {
                    "report_id": "8"
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "8",
                    "created_by": "12"
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": "8",
                    "new_status": "sent_to_client",
                    "actor_id": 12
                },
            },
            {
                "name": "CreateCampaignEntry",
                "arguments": {
                    "campaign_name": "Report 8 Follow-up Campaign",
                    "campaign_type": "general_update",
                    "created_by": "12"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "8",
                    "broker_id": "12",
                    "template_code": "report_followup",
                    "campaign_id": "9",
                    "property_id": "HTX049"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_066_briefing_for_campaign_client_1_broker1",
        "instruction": "As broker 1, begin by retrieving the details for the 'August 2025 Market Intelligence' campaign (ID 1). Subsequently, obtain complete context for client 1. Leverage this data to create a briefing document for client 1 and dispatch a post-closing check-CO email to them.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "1"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "1",
                    "created_by": "1"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "post_closing_checkin",
                    "campaign_id": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_067_briefing_for_campaign_client_2_broker2",
        "instruction": "Being broker 2, initiate by fetching the details for the 'New Client Onboarding Q3 2025' campaign (ID 2). Afterwards, acquire the full context for client 2. Utilize this information to compose a briefing document for client 2 and send them a post-closing check-CO email.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "2"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "2",
                    "created_by": "2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "2",
                    "broker_id": "2",
                    "template_code": "post_closing_checkin",
                    "campaign_id": "2"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_068_briefing_for_campaign_client_3_broker3",
        "instruction": "As broker 3, start by retrieving the particulars of the 'Weekend Open House Circuit' campaign (ID 3), then obtain the complete context for client 3. Using this data, compose a briefing document for client 3 and proceed to send them a post-closing check-CO email.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "3"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "3",
                    "created_by": "3"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "3",
                    "broker_id": "3",
                    "template_code": "post_closing_checkin",
                    "campaign_id": "3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_069_montrose_comp_client12_htx013",
        "instruction": "It is necessary to create a comparable analysis for client 12 by evaluating HTX014.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "12"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "12",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX014",
                    "client_neighborhoods": [
                        "11",
                        "1",
                        "13"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX049",
                            "similarity_score": 0.914,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_070_montrose_comp_client14_htx015",
        "instruction": "As broker 1, you need to create a comparable analysis for client 14 assessing HTX019",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "14"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "14",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX019",
                    "client_neighborhoods": [
                        "2",
                        "9",
                        "7",
                        "14"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX007",
                            "similarity_score": 0.853,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_071_montrose_comp_client1_htx002",
        "instruction": "Generate a comparable analysis for client 1 evaluating HTX002",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "1",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX002",
                    "client_neighborhoods": [
                        "5",
                        "9",
                        "8",
                        "10",
                        "14"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX047",
                            "similarity_score": 0.85,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_072_luxury_comp_client14_htx026_amenities",
        "instruction": "It is necessary to generate a comp report for client 14 on HTX026",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "14"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "14",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX026",
                    "client_neighborhoods": [
                        "2",
                        "9",
                        "7",
                        "14"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX003",
                            "similarity_score": 0.908,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_073_luxury_comp_client15_htx027_amenities",
        "instruction": "It is necessary to generate a comp report for client 15 on HTX027",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "15"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "15",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX027",
                    "client_neighborhoods": [
                        "5",
                        "12",
                        "1",
                        "7"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX044",
                            "similarity_score": 0.922,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "8"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_074_luxury_comp_client16_htx028_amenities",
        "instruction": "You need to develop a comp report for client 16 concerning HTX028.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "16"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "16",
                    "created_by_broker_id": "8",
                    "subject_property_id": "HTX028",
                    "client_neighborhoods": [
                        "7",
                        "11",
                        "6",
                        "13",
                        "15"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX035",
                            "similarity_score": 0.9,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "8"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_075_audit_mortgage_creation_client1",
        "instruction": "As broker 2, confirm the mortgage rates and determine payment terms for client 1 after a mortgage profile has been set up. Record a mortgage audit for compliance purposes and dispatch an email to them summarizing the mortgage information.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 647,
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 747819,
                    "down_payment": 41652,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "2",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "1",
                    "metadata_json": {
                        "mortgage_profile_id": "1"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "2",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_076_audit_mortgage_creation_client2",
        "instruction": "You function as broker 3. Inspect the mortgage profile set up for client 2 by confirming their mortgage rates and calculating payment terms. Generate a mortgage audit entry to satisfy compliance requirements, and dispatch a general update email that includes the mortgage details.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 716,
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 679753,
                    "down_payment": 49429,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "3",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "2",
                    "metadata_json": {
                        "mortgage_profile_id": "2"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "2",
                    "broker_id": "3",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_077_audit_mortgage_creation_client3",
        "instruction": "As broker 4, you are responsible for reviewing the mortgage profile created for client 3. Confirm their mortgage rates and work out the payment terms. Produce a mortgage audit entry for adherence to compliance, and send out a general update email containing the mortgage details.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 698,
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 224492,
                    "down_payment": 72869,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "4",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "3",
                    "metadata_json": {
                        "mortgage_profile_id": "3"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "3",
                    "broker_id": "4",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_078_new_homeowner_campaign_client_4_broker4",
        "instruction": "As broker 4, you need to organize the 'Post-Closing Client Care' campaign (ID 4) for client 4. Gather the campaign particulars, review the client's situation and email history, create a briefing document, arrange a Phone Call entitled 'Post-Closing Call' for 2025-09-21, and subsequently send them a briefing email.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "4"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "4",
                    "created_by": "4"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "4",
                    "client_id": "4",
                    "title": "Post-Closing Call",
                    "date": "2025-09-21",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "4",
                    "broker_id": "4",
                    "template_code": "briefing",
                    "campaign_id": "4"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_079_new_homeowner_campaign_client_5_broker5",
        "instruction": "As broker 5, it's necessary to arrange the 'Fall Market Preparation' campaign (ID 5) for client 5. Collect the campaign information, retrieve listings for HTX017 and HTX028, examine the client's background and email history, draft a briefing document, set up a Phone Call named 'Fall Market Preparation Call' for 2025-09-22 with source 'follow_up', and afterwards send them a briefing email.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "5"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX017",
                        "HTX028"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "5"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "5"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "5",
                    "created_by": "5"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "5",
                    "client_id": "5",
                    "title": "Fall Market Preparation Call",
                    "date": "2025-09-22",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "5",
                    "broker_id": "5",
                    "template_code": "briefing",
                    "campaign_id": "5"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_080_new_homeowner_campaign_client_6_broker6",
        "instruction": "As broker 6, prepare for the 'First-Time Buyer Education Series' campaign (ID 6) for client 6. Gather the campaign details, review the client\u2019s context and email history, create a briefing document, arrange a 'First-Time Buyer Education Call' on 2025-09-23, and subsequently send an email titled First-Time Buyer Education.",
        "actions": [
            {
                "name": "FetchCampaignDetails",
                "arguments": {
                    "campaign_id": "6"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "6"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "6"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "6",
                    "created_by": "6"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "6",
                    "client_id": "6",
                    "title": "First-Time Buyer Education Call",
                    "date": "2025-09-23",
                    "location": "Phone Call",
                    "source": "first_time_buyer"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "6",
                    "broker_id": "6",
                    "template_code": "first_time_buyer",
                    "campaign_id": "6"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_081_create_mortgage_audit_client_18",
        "instruction": "Act as broker 2. Retrieve the best rate for client 18 by considering their credit score and region, then establish a new mortgage profile for them. With a loan amount of $685,266 and a down payment of $70,069, compute their mortgage payment over 15 years using the best rate.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "18"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 637,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateMortgageProfile",
                "arguments": {
                    "client_id": "18",
                    "loan_amount": 685266,
                    "down_payment": 70069,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 637,
                    "region": "AZ",
                    "annual_income": 63042
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 685266,
                    "down_payment": 70069,
                    "interest_rate": 4.004,
                    "term_years": 15
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_082_create_mortgage_audit_client_19",
        "instruction": "You are broker 3. Once you establish a mortgage profile for client 19 with a loan amount of $298,612, and a down payment of $26,893, compute their mortgage payment.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "19"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 702,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateMortgageProfile",
                "arguments": {
                    "client_id": "19",
                    "loan_amount": 298612,
                    "down_payment": 26893,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 702,
                    "region": "AZ",
                    "annual_income": 114919
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 298612,
                    "down_payment": 26893,
                    "interest_rate": 4.004,
                    "term_years": 15
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_083_create_mortgage_audit_client_20",
        "instruction": "You are broker 4. Once you establish a mortgage profile for client 20 with a loan amount of $727,066, and a down payment of $86,396, compute their mortgage payment. Do not send an email to the client.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 785,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateMortgageProfile",
                "arguments": {
                    "client_id": "20",
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15,
                    "credit_score": 785,
                    "region": "AZ",
                    "annual_income": 142452
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 727066,
                    "down_payment": 86396,
                    "interest_rate": 4.004,
                    "term_years": 15
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_084_midtown_analysis_client1_htx002",
        "instruction": "Prepare a comparative analysis for client 1 assessing HTX002 in the Uptown neighborhood.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Uptown"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "1",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX002",
                    "client_neighborhoods": [
                        "2"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX047",
                            "similarity_score": 0.85,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_085_downtown_analysis_client2_htx003",
        "instruction": "Prepare a comparative analysis for client 2 assessing HTX003 in the Central City neighborhood.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Central City"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "2",
                    "created_by_broker_id": "14",
                    "subject_property_id": "HTX003",
                    "client_neighborhoods": [
                        "1"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX026",
                            "similarity_score": 0.908,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "14"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_086_montrose_analysis_client3_htx004",
        "instruction": "Handle the preparation of a comp analysis for client 3, evaluating HTX004 in the Arcadia neighborhood.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Arcadia"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "3",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX004",
                    "client_neighborhoods": [
                        "3"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX005",
                            "similarity_score": 0.881,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_087_galleria_analysis_client4_htx008",
        "instruction": "As broker 4, coordinate a comparable analysis for client 4, taking into account HTX008 in Fashion/Metro.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "4"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Fashion/Metro"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "4",
                    "created_by_broker_id": "4",
                    "subject_property_id": "HTX008",
                    "client_neighborhoods": [
                        "8"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX035",
                            "similarity_score": 0.916,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "4"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_088_eado_analysis_client5_htx009",
        "instruction": "Ensure to prepare a comparable analysis for client 5 accounting for HTX009 in SoDo",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "5"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "SoDo"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "5",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX009",
                    "client_neighborhoods": [
                        "9"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX001",
                            "similarity_score": 0.57,
                            "selection_reason": "Fair price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_089_oak_forest_analysis_client6_htx010",
        "instruction": "Ensure to prepare a comparable analysis for client 6 accounting for HTX010 in Pine Grove/Willow Gardens",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "6"
                },
            },
            {
                "name": "FetchNeighborhoodDetails",
                "arguments": {
                    "name": "Pine Grove/Willow Gardens"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "6",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX010",
                    "client_neighborhoods": [
                        "10"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX024",
                            "similarity_score": 0.889,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_090_new_campaign_broker11",
        "instruction": "You are broker 11. Construct a new 'Luxury Market Updates' general_update campaign using HTX033 and HTX034, and organize a briefing document for client 18 who is a suitable candidate. Acquire their complete context and dispatch a first time buyer email to the client. Return the client's maximum price.",
        "actions": [
            {
                "name": "CreateCampaignEntry",
                "arguments": {
                    "campaign_name": "Luxury Market Updates",
                    "campaign_type": "general_update",
                    "created_by": "11"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX033",
                        "HTX034"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "18"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "18",
                    "created_by": "11"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "18",
                    "broker_id": "11",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": [
                        "HTX033",
                        "HTX034"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "MAX_PRICE": 868888
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_091_new_campaign_broker12",
        "instruction": "You are broker 12. Develop a new 'Investment Property Alerts' likely_buyer campaign using HTX035 and HTX036, and compile a briefing document for client 19 who is a suitable candidate. Dispatch a first time buyer email to the client. Obtain their full context at the conclusion and return the client's MAX_PRICE.",
        "actions": [
            {
                "name": "CreateCampaignEntry",
                "arguments": {
                    "campaign_name": "Investment Property Alerts",
                    "campaign_type": "likely_buyer",
                    "created_by": "12"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX035",
                        "HTX036"
                    ]
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "19",
                    "created_by": "12"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "19",
                    "broker_id": "12",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": [
                        "HTX035",
                        "HTX036"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "19"
                }
            }
        ],
        "outputs": [
                {
                    "MAX_PRICE": 617543
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_092_new_campaign_broker13",
        "instruction": "You serve as broker 13. Set up a new campaign titled 'August 2025 Market Intelligence' under general_update using HTX037 and HTX038. Prepare a briefing document for client 20, who is deemed suitable. Obtain their complete context and dispatch a first time buyer email to the client. Provide the client's maximum price.",
        "actions": [
            {
                "name": "CreateCampaignEntry",
                "arguments": {
                    "campaign_name": "August 2025 Market Intelligence",
                    "campaign_type": "general_update",
                    "created_by": "13"
                },
            },
            {
                "name": "FetchListingsByIds",
                "arguments": {
                    "property_ids": [
                        "HTX037",
                        "HTX038"
                    ]
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "20",
                    "created_by": "13"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "20",
                    "broker_id": "13",
                    "template_code": "first_time_buyer",
                    "campaign_id": "9",
                    "property_id": [
                        "HTX037",
                        "HTX038"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "MAX_PRICE": 529693
                }
        ]
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_093_find_investment_properties_client1_broker1",
        "instruction": "You represent broker 1. Client 1 is seeking investment opportunities. Locate up to 5 properties for them and send the list via email using campaign 1.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "SearchListingsByCriteria",
                "arguments": {
                    "neighborhoods_json": [
                        5,
                        9,
                        8,
                        10,
                        14
                    ],
                    "price_min": 244685,
                    "price_max": 761571,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ],
                    "max_results": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "1",
                    "template_code": "investment_alert",
                    "campaign_id": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_094_find_investment_properties_client2_broker2",
        "instruction": "As broker 2, you need to assist Client 2, an investor, by locating up to 5 properties and sending them the list via campaign 2.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "SearchListingsByCriteria",
                "arguments": {
                    "neighborhoods_json": [
                        11,
                        1
                    ],
                    "price_min": 158527,
                    "price_max": 603380,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ],
                    "max_results": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "2",
                    "broker_id": "2",
                    "template_code": "investment_alert",
                    "campaign_id": "2"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_095_find_investment_properties_client3_broker3",
        "instruction": "Acting as broker 3, your task is to support Client 3, an investor, by identifying up to 5 properties and emailing them the list using campaign 3.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "3"
                },
            },
            {
                "name": "SearchListingsByCriteria",
                "arguments": {
                    "neighborhoods_json": [
                        1,
                        12,
                        2,
                        4,
                        5
                    ],
                    "price_min": 200505,
                    "price_max": 631914,
                    "status_filter": [
                        "active",
                        "for_sale"
                    ],
                    "max_results": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "3",
                    "broker_id": "3",
                    "template_code": "investment_alert",
                    "campaign_id": "3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_096_comp_analysis_client20_htx031_broker2",
        "instruction": "As broker 2, formulate a comparable analysis for client 20 considering HTX031 with a single comparable choice and generate the document.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "20"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "20",
                    "created_by_broker_id": "2",
                    "subject_property_id": "HTX031",
                    "client_neighborhoods": [
                        "12",
                        "9",
                        "1"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX028",
                            "similarity_score": 0.872,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "2"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_097_comp_analysis_client1_htx033_broker3",
        "instruction": "Serve as broker 3 to formulate a comparable analysis for client 1 interested in HTX033, ensuring one comparable selection and document creation.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "1",
                    "created_by_broker_id": "3",
                    "subject_property_id": "HTX033",
                    "client_neighborhoods": [
                        "5",
                        "9",
                        "8",
                        "10",
                        "14"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX005",
                            "similarity_score": 0.856,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_098_comp_analysis_client2_htx035_broker4",
        "instruction": "Your role is broker 4. Please craft a comparable analysis for client 2 interested in HTX035, including one comparable selection and document creation.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "2"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "2",
                    "created_by_broker_id": "4",
                    "subject_property_id": "HTX035",
                    "client_neighborhoods": [
                        "11",
                        "1"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX008",
                            "similarity_score": 0.916,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "4"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_099_comp_analysis_client19_htx030_broker1",
        "instruction": "As broker 1, you need to prepare a comparable analysis for client 19, who is looking into property HTX030.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "19"
                },
            },
            {
                "name": "SearchCompsAndCreateReport",
                "arguments": {
                    "client_id": "19",
                    "created_by_broker_id": "1",
                    "subject_property_id": "HTX030",
                    "client_neighborhoods": [
                        "10",
                        "5"
                    ],
                    "max_selections": 1
                },
            },
            {
                "name": "BulkCreateComparableEntries",
                "arguments": {
                    "report_id": "9",
                    "comparables": [
                        {
                            "comp_property_id": "HTX021",
                            "similarity_score": 0.864,
                            "selection_reason": "Strong price fit"
                        }
                    ]
                },
            },
            {
                "name": "GenerateAttachCompReportDocument",
                "arguments": {
                    "report_id": "9",
                    "created_by": "1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_100_client_briefing_client16_broker8",
        "instruction": "As broker 8, organize a thorough briefing for client 16. Retrieve HTX030 property details, gather the client's complete context and email history, produce a briefing document, arrange a follow-up call named 'Discuss Briefing' for 2025-09-20 with 'Phone Call' as the location and 'follow_up' as the source, and deliver a briefing email to them.",
        "actions": [
            {
                "name": "FetchPropertyDetails",
                "arguments": {
                    "property_id": "HTX030"
                },
            },
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "16"
                },
            },
            {
                "name": "FetchEmailsForClient",
                "arguments": {
                    "client_id": "16"
                },
            },
            {
                "name": "GenerateClientBriefingDocument",
                "arguments": {
                    "client_id": "16",
                    "created_by": "8"
                },
            },
            {
                "name": "CreateCalendarEventEntry",
                "arguments": {
                    "broker_id": "8",
                    "client_id": "16",
                    "title": "Discuss Briefing",
                    "date": "2025-09-20",
                    "location": "Phone Call",
                    "source": "follow_up"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "16",
                    "broker_id": "8",
                    "template_code": "briefing"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": faris,
        "user_id": "faris_101_audit_mortgage_creation_client1",
        "instruction": "As broker 2, a mortgage profile has been created for client 1. Confirm their mortgage rates and determine payment terms, log a mortgage audit entry for compliance, and provide them with a general update email encompassing the mortgage details.",
        "actions": [
            {
                "name": "FetchClientFullContext",
                "arguments": {
                    "client_id": "1"
                },
            },
            {
                "name": "FetchMortgageRatesForClient",
                "arguments": {
                    "credit_score": 647,
                    "region": "AZ"
                },
            },
            {
                "name": "CalculateMortgagePayment",
                "arguments": {
                    "loan_amount": 747819,
                    "down_payment": 41652,
                    "interest_rate": 4.004,
                    "term_years": 15
                },
            },
            {
                "name": "CreateAuditEventEntry",
                "arguments": {
                    "actor_id": "2",
                    "action": "created",
                    "entity_type": "mortgage_profile",
                    "entity_id": "1",
                    "metadata_json": {
                        "mortgage_profile_id": "1"
                    }
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": "1",
                    "broker_id": "2",
                    "template_code": "general_update"
                }
            }
        ],
        "outputs": []
    }
]
