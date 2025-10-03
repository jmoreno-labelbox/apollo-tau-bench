
tasks = [
    {
        "annotator": 0,
        "user_id": "res_v3_001",
        "instruction": "Take charge of client 9 with broker 9. The system needs to achieve the following result: a 'likely_buyer' campaign titled 'Aug 2025 Likely Buyer \u2014 Client 9 Comp Pack' should exist, and all associated email sends should be filed under the ID obtained during the creation step (do not presume a constant ID). Using the specified neighborhoods for the client [1, 12, 14, 3] and a price range of 276667\u2013628429, retrieve up to 6 active context listings for reference purposes. Record two emails for client 9 from broker 9 under this campaign employing the template_code 'likely_buyer' and body_uri 'https://storage.example.com/emails/comp_pack_client_9.html' with the precise subjects 'Comp Pack Draft \u2014 Client 9' and 'Your Comparable & Payment Plan'. Additionally, ensure there is a calendar event for client 9 with the exact title 'Review comparable & payment plan' scheduled on 2025\u201108\u201121 from 15:00\u201315:30Z, located at 'Video \u2014 Teams', with notes '30\u2011min review of comp pack', and source 'client_meeting'. Verify the entries by checking the campaign, emails, and calendar event for client 9.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Likely Buyer — Client 9 Comp Pack",
                    "type": "likely_buyer",
                    "created_by": 9
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        1,
                        12,
                        14,
                        3
                    ],
                    "price_min": 276667,
                    "price_max": 628429,
                    "limit": 6
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Comp Pack Draft — Client 9",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/comp_pack_client_9.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Your Comparable & Payment Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/comp_pack_client_9.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 9,
                    "title": "Review comparable & payment plan",
                    "start_at": "2025-08-21T15:00:00Z",
                    "end_at": "2025-08-21T15:30:00Z",
                    "location": "Video — Teams",
                    "notes": "30‑min review of comp pack",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Campaign exists; two emails recorded for client 9 under that campaign; review event present at 2025‑08‑21T15:00:00Z."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_002",
        "instruction": "Conduct a two\u2011segment likely\u2011buyer outreach for clients 5 and 6 under broker 2. Initiate a campaign called 'Aug 2025 Likely Buyers \u2014 Segment A' of type 'likely_buyer', and ensure to use the ID from the creation step for all emails. Fetch context listings (limit 6 each) using each client\u2019s neighborhoods precisely as mentioned: client 5 \u2192 [6, 2, 4, 10]; client 6 \u2192 [8, 12, 6, 5]. Dispatch an email to both clients with the subject 'August Listings Shortlist' and body_uri 'https://storage.example.com/emails/likely_buyer_aug_2025.html'. Schedule one calendar hold per client titled 'Intro call about shortlist' for 2025\u201108\u201122, with client 5 at 16:00\u201316:30Z and client 6 at 17:00\u201317:30Z, location 'Phone', notes 'Segment A outreach', source 'follow_up'. The final state should show that the campaign exists, two emails are recorded (for clients 5 and 6), and both calendar holds are set at the specified times.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Likely Buyers — Segment A",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        6,
                        2,
                        4,
                        10
                    ],
                    "limit": 6
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        8,
                        12,
                        6,
                        5
                    ],
                    "limit": 6
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 2,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/likely_buyer_aug_2025.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/likely_buyer_aug_2025.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 5,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-22T16:00:00Z",
                    "end_at": "2025-08-22T16:30:00Z",
                    "location": "Phone",
                    "notes": "Segment A outreach",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-22T17:00:00Z",
                    "end_at": "2025-08-22T17:30:00Z",
                    "location": "Phone",
                    "notes": "Segment A outreach",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Two emails recorded under the created campaign; two client holds exist on 2025‑08‑22 (16:00 and 17:00 Z)."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_003",
        "instruction": "Coordinate an open-house tour for client 3 alongside broker 1. Required outcome: a 'likely_buyer' campaign labeled 'Aug 2025 Open House \u2014 Client 3' must exist; the itinerary for 2025-08-24 should be saved with the exact sequence of stops ['HTX001','HTX004','HTX005'] and map URL 'https://maps.google.com/route/htx_003_20250824'; confirm the drive-time feasibility with a maximum of 30 minutes per segment. An email from broker 1 to client 3 associated with the created campaign should be present with the subject 'Open House Route \u2014 2025-08-24' and body_uri 'https://maps.google.com/route/htx_003_20250824'. Ensure two calendar entries for client 3 on 2025-08-24: from 10:00-10:30Z, titled 'Depart for first stop' (location 'Client Home', notes 'Open-house tour', source 'viewing') and from 13:00-13:30Z, titled 'Broker follow-up' (location 'Office', notes 'Post-tour recap', source 'follow_up'). Validate the actions by retrieving the campaign, recorded itinerary, email, and calendar entries; additionally, log audits for the campaign initiation and route preservation.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Open House — Client 3",
                    "type": "likely_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 3,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "map_url": "https://maps.google.com/route/htx_003_20250824",
                    "created_by_broker_id": 1
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Open House Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/htx_003_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T10:00:00Z",
                    "end_at": "2025-08-24T10:30:00Z",
                    "location": "Client Home",
                    "notes": "Open-house tour",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Broker follow-up",
                    "start_at": "2025-08-24T13:00:00Z",
                    "end_at": "2025-08-24T13:30:00Z",
                    "location": "Office",
                    "notes": "Post-tour recap",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 1,
                    "action": "campaign_created",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                    "metadata_json": {
                        "name": "Aug 2025 Open House — Client 3",
                        "type": "likely_buyer"
                    }
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 1,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": [
                            "HTX001",
                            "HTX004",
                            "HTX005"
                        ],
                        "map_url": "https://maps.google.com/route/htx_003_20250824"
                    }
                }
            }
        ],
        "outputs": [
                "Route persisted with specified map_url; one email recorded under created campaign; two calendar holds confirmed; audits saved."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_004",
        "instruction": "Handle the preparation of a briefing update for client 8 under broker 12. Desired outcome: a briefing document is created and linked to client 8; a 'general_update' campaign titled 'Aug 2025 Briefings \u2014 Client 8' is available; the broker-crafted email to client 8 is categorized under this campaign with subject 'Client Briefing Packet', template_code 'briefing_broker', and body_uri 'https://storage.example.com/briefings/client_briefing_008_v1.pdf'; and a review appointment is scheduled for client 8 on 2025-08-22 from 14:00-14:30Z titled 'Briefing review' with the location 'Office', notes 'Review briefing packet', source 'client_meeting'. Confirm the operations by retrieving the campaign, email related to client 8, and the calendar event; document an audit trail indicating the dispatch of the briefing.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 12
                },
            },
            {
                "name": "AttachDocumentToClient",
                "arguments": {
                    "client_id": 8,
                    "document_id": 21
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Briefings — Client 8",
                    "type": "general_update",
                    "created_by": 12
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Client Briefing Packet",
                    "template_code": "briefing_broker",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_008_v1.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Briefing review",
                    "start_at": "2025-08-22T14:00:00Z",
                    "end_at": "2025-08-22T14:30:00Z",
                    "location": "Office",
                    "notes": "Review briefing packet",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 12,
                    "action": "briefing_sent",
                    "entity_type": "documents",
                    "entity_id": 21,
                    "metadata_json": {
                        "client_id": 8,
                        "campaign_id": 9
                    }
                }
            }
        ],
        "outputs": [
                "Briefing generated/attached; broker email filed under created campaign; review reminder present; audit logged."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_005",
        "instruction": "Handle the creation of a succinct market progress report for client 14 collaborating with broker 7. Expected outcome: a 'general_update' campaign titled 'Aug 2025 Uptown Market Update \u2014 Client 14' is created; current comps are accessed using listing_ids [4, 5, 6]; a showing itinerary for 2025\u201108\u201125 with arranged stops ['HTX012','HTX027','HTX044'] is saved at the map URL 'https://maps.google.com/route/htx_014_20250825'; and one email to client 14 is recorded under the new campaign with subject 'Uptown Market Update & Showing Plan', template_code 'general_update', and body_uri 'https://maps.google.com/route/htx_014_20250825'. Confirm the entries by verifying the campaign, email, and route.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Uptown Market Update — Client 14",
                    "type": "general_update",
                    "created_by": 7
                },
            },
            {
                "name": "ListListingsByIds",
                "arguments": {
                    "listing_ids": [
                        4,
                        5,
                        6
                    ]
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 14,
                    "date": "2025-08-25",
                    "stops_ordered_json": [
                        "HTX012",
                        "HTX027",
                        "HTX044"
                    ],
                    "map_url": "https://maps.google.com/route/htx_014_20250825",
                    "created_by_broker_id": 7
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 7,
                    "subject": "Uptown Market Update & Showing Plan",
                    "template_code": "general_update",
                    "body_uri": "https://maps.google.com/route/htx_014_20250825",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Comps [4,5,6] retrieved; route saved with provided map; email filed under created campaign."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_006",
        "instruction": "Coordinate the distribution of a general market update to clients 1 and 2 on behalf of broker 3. Make sure the resulting state has: a 'general_update' campaign called 'Aug 2025 General Update \u2014 Central City & Uptown' used for both emails; a collection of up to 8 active listings without extra filters (limit 8); two emails sent to clients 1 and 2 with subject 'Q3 Stats & Listings \u2014 Central City & Uptown' and body_uri 'https://storage.example.com/emails/q3_stats_dt_midtown.html'; and schedule two follow\u2011up meetings on 2025\u201108\u201123 titled 'Discuss Q3 market update' over 'Video \u2014 Zoom' with notes 'Market update follow\u2011up' (client 1 at 15:00\u201315:30Z, client 2 at 16:30\u201317:00Z).",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 General Update — Central City & Uptown",
                    "type": "general_update",
                    "created_by": 3
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "limit": 8
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Q3 Stats & Listings — Central City & Uptown",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/q3_stats_dt_midtown.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Q3 Stats & Listings — Central City & Uptown",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/q3_stats_dt_midtown.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Discuss Q3 market update",
                    "start_at": "2025-08-23T15:00:00Z",
                    "end_at": "2025-08-23T15:30:00Z",
                    "location": "Video — Zoom",
                    "notes": "Market update follow‑up",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Discuss Q3 market update",
                    "start_at": "2025-08-23T16:30:00Z",
                    "end_at": "2025-08-23T17:00:00Z",
                    "location": "Video — Zoom",
                    "notes": "Market update follow‑up",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Two general update emails filed under created campaign; follow‑ups scheduled for 2025‑08‑23 and confirmed via reads."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_007",
        "instruction": "Handle the creation of a finance-first brief for client 13 in collaboration with broker 7. Ensure the system displays: the retrieval of the client's mortgage profile; three recent sales fetched for context against property_id 'HTX003' (limit 3); a general active search was conducted (limit 6); and a 'likely_buyer' campaign entitled 'Aug 2025 Finance-First \u2014 Client 13' is present with one email to client 13 logged under the established campaign using subject 'Finance-First Plan & Options', template_code 'likely_buyer', and body_uri 'https://storage.example.com/emails/finance_first_client_13.html'. A consultation hold is scheduled for client 13 on 2025-08-26 18:00-18:30Z with the specific title 'Financing consult', location 'Video \u2014 Teams', notes 'Finance-first plan', and source 'client_meeting'. Confirm the entries by reading back the campaign, the email, and the calendar event.",
        "actions": [
            {
                "name": "GetMortgageProfile",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "FetchRecentSalesByProperty",
                "arguments": {
                    "property_id": "HTX003",
                    "limit": 3
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Finance‑First — Client 13",
                    "type": "likely_buyer",
                    "created_by": 7
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 7,
                    "subject": "Finance‑First Plan & Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/finance_first_client_13.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 13,
                    "title": "Financing consult",
                    "start_at": "2025-08-26T18:00:00Z",
                    "end_at": "2025-08-26T18:30:00Z",
                    "location": "Video — Teams",
                    "notes": "Finance-first plan",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Finance-first context prepared; one email filed under created campaign; consultation hold present for 2025‑08‑26T18:00:00Z."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_008",
        "instruction": "Coordinate a post-tour follow-up for client 10 with broker 4. Target state: a briefing document is completed; a 'likely_buyer' campaign titled 'Aug 2025 Tour Follow-Ups \u2014 Client 10' is in place; an email to client 10 is cataloged under the created campaign with subject 'Your Tour Follow-Up Packet', template_code 'likely_buyer', and body_uri 'https://storage.example.com/briefings/client_briefing_010_v1.pdf'. A follow-up calendar hold is arranged for client 10 on Saturday 2025-08-23 11:30-12:00Z, bearing the exact title 'Tour recap', location 'Phone', notes 'Recap post-tour', and source 'follow_up'. Certify the entries by reading back the campaign, the email for client 10, and the calendar event.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 4
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Tour Follow‑Ups — Client 10",
                    "type": "likely_buyer",
                    "created_by": 4
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Your Tour Follow‑Up Packet",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_010_v1.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 10,
                    "title": "Tour recap",
                    "start_at": "2025-08-23T11:30:00Z",
                    "end_at": "2025-08-23T12:00:00Z",
                    "location": "Phone",
                    "notes": "Recap post‑tour",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Briefing generated; follow‑up email filed under created campaign; 2025‑08‑23 recap hold present."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_009",
        "instruction": "Handle a compact shortlist for client 11 alongside broker 6, ensuring the final outcome contains: a 'likely_buyer' campaign identified as 'Aug 2025 Compact Shortlist \u2014 Client 11'; a context search conducted in neighborhoods [1, 2] with parameters price_min 200000, price_max 900000, beds 1, baths 1, sqft_min 800, sqft_max 2200, limit 8; an email directed to client 11 categorized under the established campaign with the subject 'Shortlist & Saturday Route', template_code 'likely_buyer', and body_uri 'https://storage.example.com/emails/compact_shortlist_11.html'; a Saturday (2025\u201108\u201123) itinerary recorded with stops in sequence ['HTX036','HTX032','HTX049'] available at map URL 'https://maps.google.com/route/htx_011_20250823'; and two Saturday reservations for client 11: 11:00\u201311:30Z named 'Shortlist review' (location 'Video \u2014 Zoom', notes 'Review shortlist & route', source 'follow_up') and 12:00\u201312:30Z titled 'Confirm Saturday logistics' (location 'Phone', notes 'Confirm times & transport', source 'follow_up'). Verify the documentation by retrieving the campaign, the email, the route specifics, and the scheduling events.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Compact Shortlist — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        1,
                        2
                    ],
                    "price_min": 200000,
                    "price_max": 900000,
                    "beds": 1,
                    "baths": 1,
                    "sqft_min": 800,
                    "sqft_max": 2200,
                    "limit": 8
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Shortlist & Saturday Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/compact_shortlist_11.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 11,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX036",
                        "HTX032",
                        "HTX049"
                    ],
                    "map_url": "https://maps.google.com/route/htx_011_20250823",
                    "created_by_broker_id": 6
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Shortlist review",
                    "start_at": "2025-08-23T11:00:00Z",
                    "end_at": "2025-08-23T11:30:00Z",
                    "location": "Video — Zoom",
                    "notes": "Review shortlist & route",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Confirm Saturday logistics",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:30:00Z",
                    "location": "Phone",
                    "notes": "Confirm times & transport",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Campaign exists; shortlist email filed; route saved with provided map; both Saturday holds confirmed."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_v3_010",
        "instruction": "Coordinate a combined Saturday showing agenda for clients 1 and 2 along with broker 3. Ensure the final setup comprises the following: \u2022 A 'likely_buyer' campaign titled 'Aug 2025 Saturday Showings \u2014 Clients 1 & 2' utilized for both outbound emails. \u2022 A documented route for client 1 on 2025\u201108\u201123 featuring the ordered stops ['HTX036','HTX032','HTX049'] and map URL 'https://maps.google.com/route/htx_011_20250823', with a driving time feasible at a maximum of 30 minutes per leg. \u2022 Two emails archived with the subject 'Saturday: Route & Mortgage Snapshot' and HTML content at 'https://storage.example.com/emails/sat_show_c1.html' (client 1) and 'https://storage.example.com/emails/sat_show_c2.html' (client 2), both aligned with the campaign you formed. \u2022 Two Saturday appointments: for client 1 at 11:00\u201311:30Z labeled 'Shortlist review' (location 'Video - Zoom', source 'follow_up') and for client 2 at 12:00\u201312:30Z titled 'Confirm Saturday logistics' (location 'Phone', source 'follow_up'). Include a brief mortgage analysis for client 1 targeting $550,000 with the usual 30\u2011year term. Confirm the campaign, the viable route, the two emails, and both scheduled holds as outcomes.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Saturday Showings — Clients 1 & 2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 1,
                    "list_price": 550000,
                    "term_years": 30
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "likely_buyer",
                    "client_id": 1,
                    "subject": "Saturday: Route & Mortgage Snapshot",
                    "slug": "sat_show_c1"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Saturday: Route & Mortgage Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/sat_show_c1.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "likely_buyer",
                    "client_id": 2,
                    "subject": "Saturday: Route & Mortgage Snapshot",
                    "slug": "sat_show_c2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Saturday: Route & Mortgage Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/sat_show_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 1,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX036",
                        "HTX032",
                        "HTX049"
                    ],
                    "map_url": "https://maps.google.com/route/htx_011_20250823",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX036",
                        "HTX032",
                        "HTX049"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Shortlist review",
                    "start_at": "2025-08-23T11:00:00Z",
                    "end_at": "2025-08-23T11:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Confirm Saturday logistics",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Campaign created and verified; mortgage snapshot computed for client 1; route saved with the given URL and stops and is drive‑time feasible (≤30 minutes per hop); two emails recorded under the campaign; and both Saturday calendar holds exist."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_011",
        "instruction": "Coordinate a neighborhood preview for client 4 under broker 2. Final state should have a 'general_update' campaign named 'Aug 2025 Neighborhood Preview - Client 4', which is utilized by the outbound message; obtain a listings snapshot for neighborhood 1 filtered to price 250000\u2013700000 with beds=2 and baths=2 (context only); ensure one email for client 4 with subject 'Neighborhood Preview' and body_uri 'https://storage.example.com/emails/preview_c4.html' is linked to that campaign; and secure a calendar hold for client 4 on 2025-08-22 from 15:00\u201315:30Z titled 'Pre-tour call' at 'Video - Zoom' with source 'follow_up'.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Neighborhood Preview - Client 4",
                    "type": "general_update",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        1
                    ],
                    "price_min": 250000,
                    "price_max": 700000,
                    "beds": 2,
                    "baths": 2
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 4,
                    "subject": "Neighborhood Preview",
                    "slug": "preview_c4"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Neighborhood Preview",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/preview_c4.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 4,
                    "title": "Pre-tour call",
                    "start_at": "2025-08-22T15:00:00Z",
                    "end_at": "2025-08-22T15:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 4
                }
            }
        ],
        "outputs": [
                "Campaign exists and is referenced by the email; listings snapshot retrieved; email recorded; calendar hold present for 2025-08-22T15:00Z."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_012",
        "instruction": "Handle the setup of a Saturday open-house route for client 5 under broker 2. Ensure a 'likely_buyer' campaign named 'Aug 2025 Saturday Open Houses - Client 5' is created; log a route for 2025-08-23 with ordered stops ['HTX012','HTX009','HTX020'] and map URL 'https://maps.google.com/route/htx_012_20250823'; drive-time feasibility should be checked and confirmed as OK at a maximum of 30 minutes per hop; and verify one email to client 5 is documented under that campaign with the subject 'Open House Route - 2025-08-23' and body_uri 'https://maps.google.com/route/htx_012_20250823'. Additionally, set a same-day hold from 10:00-10:15Z titled 'Day-of check-CO' at 'Phone' (source 'follow_up'). Confirm by reading back the campaign, route details, email, and calendar events.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Saturday Open Houses - Client 5",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 5,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX012",
                        "HTX009",
                        "HTX020"
                    ],
                    "map_url": "https://maps.google.com/route/htx_012_20250823",
                    "created_by_broker_id": 2
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX012",
                        "HTX009",
                        "HTX020"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 2,
                    "subject": "Open House Route - 2025-08-23",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/htx_012_20250823",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 5,
                    "title": "Day-of check-CO",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:15:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                }
            }
        ],
        "outputs": [
                "Campaign exists; route saved and feasible; email recorded; calendar hold present for 2025-08-23."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_013",
        "instruction": "Manage weekend logistics for clients 6 and 7 under broker 4. Targeted end state: a 'general_update' campaign with the title 'Aug 2025 Weekend Logistics - C6 & C7' should be present; emails associated with that campaign must be on file with the subject 'Weekend Logistics' and body_uris 'https://storage.example.com/emails/weekend_c6.html' (client 6) and 'https://storage.example.com/emails/weekend_c7.html' (client 7); and there should be two holds \u2014 for client 6 at 2025-08-23 13:00-13:20Z titled 'Prep call' at 'Video - Zoom' (source 'follow_up') and for client 7 at 2025-08-23 13:30-13:50Z titled 'Prep call' at 'Video - Zoom' (source 'follow_up'). Confirm by reviewing the campaign, both clients\u2019 emails, and both clients\u2019 calendar events.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Weekend Logistics - C6 & C7",
                    "type": "general_update",
                    "created_by": 4
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 6,
                    "subject": "Weekend Logistics",
                    "slug": "weekend_c6"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 4,
                    "subject": "Weekend Logistics",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/weekend_c6.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 7,
                    "subject": "Weekend Logistics",
                    "slug": "weekend_c7"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 4,
                    "subject": "Weekend Logistics",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/weekend_c7.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 6,
                    "title": "Prep call",
                    "start_at": "2025-08-23T13:00:00Z",
                    "end_at": "2025-08-23T13:20:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 7,
                    "title": "Prep call",
                    "start_at": "2025-08-23T13:30:00Z",
                    "end_at": "2025-08-23T13:50:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 7
                }
            }
        ],
        "outputs": [
                "Campaign verified; two emails filed; two prep-call holds present on 2025-08-23."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_014",
        "instruction": "Organize mortgage guidance and subsequent actions for client 8 under broker 12. Required final outcome: a mortgage estimate must be calculated for client 8 at list_price 550000 (context); a concise comps package should be documented as a comp report for subject_property_id 'HTX088' (created_by_broker_id 12) and its details confirmed; a 'general_update' campaign titled 'Aug 2025 Mortgage & Viewing - Client 8' should exist; an email to client 8 with the subject 'Mortgage & Viewing Plan' and body_uri 'https://storage.example.com/emails/mortgage_viewing_c8.html' should be logged under that campaign; and two calendar holds should be present \u2014 on 2025-08-22 14:00\u201314:30Z titled 'Mortgage consult' at 'Office' (source 'follow_up') and on 2025-08-24 18:00\u201319:00Z titled 'Placeholder viewing window' at 'TBD' (source 'viewing').",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 8,
                    "list_price": 550000
                },
            },
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 8,
                    "subject_property_id": "HTX088",
                    "created_by_broker_id": 12,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Mortgage & Viewing - Client 8",
                    "type": "general_update",
                    "created_by": 12
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Mortgage & Viewing Plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/mortgage_viewing_c8.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Mortgage consult",
                    "start_at": "2025-08-22T14:00:00Z",
                    "end_at": "2025-08-22T14:30:00Z",
                    "location": "Office",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Placeholder viewing window",
                    "start_at": "2025-08-24T18:00:00Z",
                    "end_at": "2025-08-24T19:00:00Z",
                    "location": "TBD",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 8
                }
            }
        ],
        "outputs": [
                "Mortgage estimate computed; comp report saved and verified; campaign verified; email filed; two calendar holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_015",
        "instruction": "Ensure the creation of an open-house plan for client 9 managed by broker 2. The required outcome should comprise: open-house windows obtained for neighborhoods [2,3] (context); a stored route dated 2025-08-24 with sequential stops ['HTX021','HTX025','HTX030'] using map URL 'https://maps.google.com/route/htx_plan_c9_20250824' that adheres to a \u226430-minute hop constraint; a 'likely_buyer' campaign titled 'Aug 2025 Open House Plan - Client 9' featuring one email to client 9 with subject 'Sunday Route - 2025-08-24' and body_uri 'https://storage.example.com/emails/sunday_route_c9.html'; as well as a same-day hold from 09:30-09:45Z named 'Pre-drive sync' at 'Phone' (source 'follow_up').",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        2,
                        3
                    ]
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX021",
                        "HTX025",
                        "HTX030"
                    ],
                    "map_url": "https://maps.google.com/route/htx_plan_c9_20250824",
                    "created_by_broker_id": 2
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX021",
                        "HTX025",
                        "HTX030"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Open House Plan - Client 9",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Sunday Route - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/sunday_route_c9.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 9,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:30:00Z",
                    "end_at": "2025-08-24T09:45:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 9
                }
            }
        ],
        "outputs": [
                "Open-house windows fetched; route saved and feasible; campaign verified; email recorded; pre-drive hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_016",
        "instruction": "Manage all off-route viewing requests for client 10 overseen by broker 11. Desired outcome includes: a drafts bundle prepared for properties ['HTX040','HTX042','HTX043'] (context); a 'general_update' campaign titled 'Aug 2025 Off-Route Viewings - Client 10' is set up; an internal email to client 10 (for documentation under the campaign) with subject 'Viewing Requests To Send' and body_uri 'https://storage.example.com/emails/offroute_c10.html'; and a follow-up hold arranged for client 10 on 2025-08-25 from 16:00-16:20Z named 'Follow up on viewing requests' at 'Video - Teams' (source 'follow_up'). Validate by reviewing the campaign, the email, and the client's scheduled events.",
        "actions": [
            {
                "name": "DraftSellerBrokerEmails",
                "arguments": {
                    "client_id": 10,
                    "property_ids": [
                        "HTX040",
                        "HTX042",
                        "HTX043"
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Off-Route Viewings - Client 10",
                    "type": "general_update",
                    "created_by": 11
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 10,
                    "subject": "Viewing Requests To Send",
                    "slug": "offroute_c10"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Viewing Requests To Send",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/offroute_c10.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 10,
                    "title": "Follow up on viewing requests",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:20:00Z",
                    "location": "Video - Teams",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 10
                }
            }
        ],
        "outputs": [
                "Drafts produced; campaign verified; internal email stored; follow-up hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_017",
        "instruction": "Handle the sending of a preference-focused update to client 3, represented by broker 1. Final state: client 3's stored preferences have been reviewed, and the listings search precisely aligns with these criteria\u2014neighborhoods [1,12,2,4,5], price 200505\u2013631914, beds=2, baths=2 (context); a campaign named 'Aug 2025 Targeted Listings - Client 3' categorized as 'likely_buyer' is active, and the outgoing message is stored within it; an email exists for client 3 with subject 'Tailored Listings Update' and body_uri 'https://storage.example.com/emails/prefs_c3.html'; and a check-CO hold for 2025-08-23 17:00\u201317:20Z titled 'Listings check-CO' at 'Phone' is prepared with origin 'follow_up'.",
        "actions": [
            {
                "name": "GetClientPreferences",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        1,
                        12,
                        2,
                        4,
                        5
                    ],
                    "price_min": 200505,
                    "price_max": 631914,
                    "beds": 2,
                    "baths": 2
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Targeted Listings - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Tailored Listings Update",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/prefs_c3.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Listings check-CO",
                    "start_at": "2025-08-23T17:00:00Z",
                    "end_at": "2025-08-23T17:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 3
                }
            }
        ],
        "outputs": [
                "Preferences referenced and mirrored in search; campaign exists; email recorded; check-CO hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_018",
        "instruction": "Coordinate the broadening of search guidance for client 2 under broker 3 by exclusively considering the actual adjacent neighborhoods to neighborhood 1. Final state: the details for neighborhood 1 along with its bordering IDs are reviewed; listings searches are confined strictly within these adjoining neighborhoods using beds=2 and baths=2 (context); there is a 'general_update' campaign named 'Aug 2025 Bordering Areas - Client 2'; one email is prepared for client 2 with subject 'Bordering Area Options' and body_uri 'https://storage.example.com/emails/border_c2.html' linked to that campaign; and a consult hold for 2025-08-23 16:00\u201316:30Z titled 'Bordering areas consult' at 'Video - Zoom' is organized with origin 'follow_up'.",
        "actions": [
            {
                "name": "GetNeighborhoodDetails",
                "arguments": {
                    "neighborhood_id": 1
                },
            },
            {
                "name": "GetBorderingNeighborhoods",
                "arguments": {
                    "neighborhood_id": 1
                },
            },
            {
                "name": "SearchListingsInNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        2
                    ],
                    "beds": 2,
                    "baths": 2
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Bordering Areas - Client 2",
                    "type": "general_update",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 2,
                    "subject": "Bordering Area Options",
                    "slug": "border_c2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Area Options",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/border_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Bordering areas consult",
                    "start_at": "2025-08-23T16:00:00Z",
                    "end_at": "2025-08-23T16:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Neighborhood context gathered; bordering-only search performed; campaign exists; email recorded; consult hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_019",
        "instruction": "Organize a route day for client 2 under broker 3. Desired outcome: a route for 2025-08-24 is stored with ordered stops ['HTX015','HTX016','HTX017'] and map URL 'https://maps.google.com/route/htx_plan_c2_20250824'; hops comply with a 30-minute time frame; a 'likely_buyer' campaign titled 'Aug 2025 Route Day - Client 2' is set up; an email is sent to client 2 with subject 'Route Day Plan - 2025-08-24' and body_uri 'https://storage.example.com/emails/routeday_c2.html' noted under the campaign; and two holds are scheduled for client 2 \u2014 08:30-08:45Z with the title 'Kickoff call' at 'Phone' (source 'follow_up') and 13:00-13:20Z with title 'Post-route debrief' at 'Video - Zoom' (source 'follow_up'). Confirm by reviewing the route details, campaign, email, and calendar events.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX015",
                        "HTX016",
                        "HTX017"
                    ],
                    "map_url": "https://maps.google.com/route/htx_plan_c2_20250824",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX015",
                        "HTX016",
                        "HTX017"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Route Day - Client 2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "likely_buyer",
                    "client_id": 2,
                    "subject": "Route Day Plan - 2025-08-24",
                    "slug": "routeday_c2"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Route Day Plan - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/routeday_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Kickoff call",
                    "start_at": "2025-08-24T08:30:00Z",
                    "end_at": "2025-08-24T08:45:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Post-route debrief",
                    "start_at": "2025-08-24T13:00:00Z",
                    "end_at": "2025-08-24T13:20:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Route saved and feasible; campaign verified; email recorded; two holds present for kickoff and debrief."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_020",
        "instruction": "Coordinate a new-homeowner touch for client 14 under broker 5. Targeted outcome: a 'new_homeowner' campaign titled 'Aug 2025 New Homeowner - Client 14' is established; an email to client 14 is documented under the campaign with subject 'Congrats & Checklist' and body_uri 'https://storage.example.com/emails/newhome_c14.html'; and a check-CO hold is arranged for 2025-08-25 16:00-16:20Z titled 'New homeowner check-CO' at 'Phone' (source 'follow_up'). Validate by reviewing the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 New Homeowner - Client 14",
                    "type": "new_homeowner",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "new_homeowner",
                    "client_id": 14,
                    "subject": "Congrats & Checklist",
                    "slug": "newhome_c14"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "Congrats & Checklist",
                    "template_code": "new_homeowner",
                    "body_uri": "https://storage.example.com/emails/newhome_c14.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "New homeowner check-CO",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 14
                }
            }
        ],
        "outputs": [
                "Campaign verified; email recorded; check-CO hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_021",
        "instruction": "Handle the sending of investor options to client 18, managed by broker 5. The final situation: condos in neighborhoods [3,4] priced 300000\u2013650000 have been searched (context); a mortgage estimate for client 18 is calculated at list_price 400000 (context); a 'general_update' campaign called 'Aug 2025 Investor Picks - Client 18' is present; there is one email for client 18 with the subject 'Investor Picks & Financing' and body_uri 'https://storage.example.com/emails/investor_c18.html' linked to that campaign; and a review hold is scheduled for 2025-08-24 19:00\u201319:30Z titled 'Investor review' at 'Video - Zoom' with the source 'follow_up'.",
        "actions": [
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        3,
                        4
                    ],
                    "property_type": "condo",
                    "price_min": 300000,
                    "price_max": 650000
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 18,
                    "list_price": 400000
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Investor Picks - Client 18",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 18,
                    "subject": "Investor Picks & Financing",
                    "slug": "investor_c18"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Investor Picks & Financing",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/investor_c18.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Investor review",
                    "start_at": "2025-08-24T19:00:00Z",
                    "end_at": "2025-08-24T19:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 18
                }
            }
        ],
        "outputs": [
                "Search and estimate computed as context; campaign exists; email recorded; review hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_022",
        "instruction": "Handle the dispatching of a welcome packet to client 20, under the responsibility of broker 7. Final outcome: a 'general_update' campaign titled 'Aug 2025 Welcome - Client 20' is established; an email to client 20 is documented under the campaign with the subject 'Welcome & Next Steps' and body_uri 'https://storage.example.com/emails/welcome_c20.html'; and two holds are set: 2025-08-22 18:00-18:20Z titled 'Welcome call' at 'Phone' (source 'follow_up') and 2025-08-23 18:00-18:30Z titled 'Next-steps planning' at 'Video - Zoom' (source 'follow_up'). Confirm by reviewing the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Welcome - Client 20",
                    "type": "general_update",
                    "created_by": 7
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "general_update",
                    "client_id": 20,
                    "subject": "Welcome & Next Steps",
                    "slug": "welcome_c20"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 7,
                    "subject": "Welcome & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/welcome_c20.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Welcome call",
                    "start_at": "2025-08-22T18:00:00Z",
                    "end_at": "2025-08-22T18:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Next-steps planning",
                    "start_at": "2025-08-23T18:00:00Z",
                    "end_at": "2025-08-23T18:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 20
                }
            }
        ],
        "outputs": [
                "Campaign verified; welcome email recorded; two planning holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_023",
        "instruction": "Handle the creation of a Sunday drive plan for client 3 under broker 1 by reviewing open-house times for properties ['HTX001','HTX004','HTX005'] for 2025-08-22 to 2025-08-25 (context). Final outcome: a route scheduled for 2025-08-24 with stops arranged in order ['HTX001','HTX004','HTX005'] is recorded using the map URL 'https://maps.google.com/route/htx_c3_sunday_20250824' and successfully meets a 30-minute hop check; a 'likely_buyer' campaign named 'Aug 2025 Sunday Drive - Client 3' is in place; an email addressed to client 3 with the subject 'Sunday Drive Plan - 2025-08-24' and body_uri 'https://storage.example.com/emails/sunday_c3.html' is logged under that campaign; and a check-CO hold for 2025-08-24 09:45-10:00Z titled 'Pre-drive check-CO' at 'Phone' (source 'follow_up') is established. Verify by reviewing the route details, campaign, email, and calendar events.",
        "actions": [
            {
                "name": "FetchOpenHousesByProperties",
                "arguments": {
                    "property_ids": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "date_from": "2025-08-22",
                    "date_to": "2025-08-25"
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 3,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "map_url": "https://maps.google.com/route/htx_c3_sunday_20250824",
                    "created_by_broker_id": 1
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Sunday Drive - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "RenderClientEmail",
                "arguments": {
                    "template_code": "likely_buyer",
                    "client_id": 3,
                    "subject": "Sunday Drive Plan - 2025-08-24",
                    "slug": "sunday_c3"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Sunday Drive Plan - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/sunday_c3.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Pre-drive check-CO",
                    "start_at": "2025-08-24T09:45:00Z",
                    "end_at": "2025-08-24T10:00:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 3
                }
            }
        ],
        "outputs": [
                "Open-house windows fetched; route saved and feasible; campaign verified; email recorded; check-CO hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_024",
        "instruction": "Coordinate a pre-approval and tour plan for client 1 under broker 3. Final outcome: a mortgage estimate is determined at list_price 600000 (context); a 'general_update' campaign titled 'Aug 2025 Pre-approval & Tour - Client 1' is set up; an email directed to client 1 with the subject 'Pre-approval & Tour Plan' and body_uri 'https://storage.example.com/emails/preapprove_tour_c1.html' is documented under the campaign; and two holds are established - 2025-08-22 09:00-09:30Z titled 'Lender pre-approval' at 'Phone' (source 'follow_up') and 2025-08-24 15:00-16:30Z titled 'Tour window' at 'TBD' (source 'viewing'). Validate by reviewing the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 1,
                    "list_price": 600000
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Pre-approval & Tour - Client 1",
                    "type": "general_update",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Pre-approval & Tour Plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/preapprove_tour_c1.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Lender pre-approval",
                    "start_at": "2025-08-22T09:00:00Z",
                    "end_at": "2025-08-22T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Tour window",
                    "start_at": "2025-08-24T15:00:00Z",
                    "end_at": "2025-08-24T16:30:00Z",
                    "location": "TBD",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 1
                }
            }
        ],
        "outputs": [
                "Estimate computed; campaign verified; email recorded; two holds present for lender and tour."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_025",
        "instruction": "Handle the expansion of search guidance for client 2 under broker 3 by exclusively utilizing the adjoining neighborhoods of neighborhood 1. Final condition: you review details for neighborhood 1 and its surrounding IDs (context); then initiate a listings search solely within those surrounding IDs with price 300000\u2013650000, beds=2, baths=2, limiting to 6 results (limit 6) for context; a 'general_update' campaign titled 'Aug 2025 Bordering Preview \u2014 Client 2' is in place; log an email to client 2 with subject 'Bordering Area Shortlist' and body_uri 'https://storage.example.com/emails/border_prev_c2.html' within the campaign; and a follow-up hold is scheduled for 2025\u201108\u201122 16:00\u201316:20Z titled 'Bordering shortlist review' at 'Phone' (source 'follow_up'). Confirm by reviewing the campaign, the email sent to client 2, and the client's calendar events.",
        "actions": [
            {
                "name": "GetNeighborhoodDetails",
                "arguments": {
                    "neighborhood_id": 1
                },
            },
            {
                "name": "GetBorderingNeighborhoods",
                "arguments": {
                    "neighborhood_id": 1
                },
            },
            {
                "name": "SearchListingsInNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        2
                    ],
                    "price_min": 300000,
                    "price_max": 650000,
                    "beds": 2,
                    "baths": 2,
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Bordering Preview — Client 2",
                    "type": "general_update",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Area Shortlist",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/border_prev_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Bordering shortlist review",
                    "start_at": "2025-08-22T16:00:00Z",
                    "end_at": "2025-08-22T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Neighborhood and borders read; campaign verified; email recorded; follow‑up hold present on 2025‑08‑22T16:00Z."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_026",
        "instruction": "Coordinate a Saturday open-house tour for client 5 under broker 1. End condition: open-house windows are retrieved for properties ['HTX021','HTX024','HTX025'] between 2025\u201108\u201122 and 2025\u201108\u201124 (context); save a route dated 2025\u201108\u201123 with ordered stops ['HTX021','HTX024','HTX025'] and map URL 'https://maps.google.com/route/oh_c5_20250823'; ensure drive-time feasibility at \u226430 minutes per segment; a 'likely_buyer' campaign named 'Aug 2025 Open Houses \u2014 Client 5' is created; send an email to client 5 with subject 'Saturday Open-House Route' using the map URL as body_uri, recorded within the campaign; set two holds for 2025\u201108\u201123 \u2014 09:50\u201310:00Z titled 'Depart for first stop' at 'Client Home' (source 'viewing', notes 'Leave buffer for parking') and 13:30\u201313:50Z titled 'Post-tour recap' at 'Phone' (source 'follow_up', notes 'Discuss favorites & next steps'). Validate by reviewing the campaign, the stored route, the email, and calendar events; also log an audit for the developed route.",
        "actions": [
            {
                "name": "FetchOpenHousesByProperties",
                "arguments": {
                    "property_ids": [
                        "HTX021",
                        "HTX024",
                        "HTX025"
                    ],
                    "date_from": "2025-08-22",
                    "date_to": "2025-08-24"
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 5,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX021",
                        "HTX024",
                        "HTX025"
                    ],
                    "map_url": "https://maps.google.com/route/oh_c5_20250823",
                    "created_by_broker_id": 1
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX021",
                        "HTX024",
                        "HTX025"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Open Houses — Client 5",
                    "type": "likely_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Saturday Open-House Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/oh_c5_20250823",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 5,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-23T09:50:00Z",
                    "end_at": "2025-08-23T10:00:00Z",
                    "location": "Client Home",
                    "notes": "Leave buffer for parking",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 5,
                    "title": "Post-tour recap",
                    "start_at": "2025-08-23T13:30:00Z",
                    "end_at": "2025-08-23T13:50:00Z",
                    "location": "Phone",
                    "notes": "Discuss favorites & next steps",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 1,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": [
                            "HTX021",
                            "HTX024",
                            "HTX025"
                        ],
                        "map_url": "https://maps.google.com/route/oh_c5_20250823"
                    }
                }
            }
        ],
        "outputs": [
                "Route saved and feasible; campaign verified; email recorded; two holds present; audit logged for the route."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_027",
        "instruction": "Handle the creation and delivery of a comparable report for client 10 under broker 4. The end result should be a comp report saved for subject_property_id 'HTX072' (created_by_broker_id 4) with status 'draft', which is then updated to 'sent_to_client'; ensure verification reads display the report and its comparables/documents; a 'likely_buyer' campaign titled 'Aug 2025 Comp Report \u2014 Client 10' is active; record one email to client 10 with subject 'Comp Report Delivered' and body_uri 'https://storage.example.com/emails/comp_report_c10.html' within the campaign; and schedule a follow-up hold for 2025\u201108\u201122 18:00\u201318:20Z named 'Comp report debrief' at 'Video \u2014 Zoom' (source 'follow_up', notes 'CMA review & Q&A'). Verify by reviewing the details of the comp report after saving and status update, the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 10,
                    "subject_property_id": "HTX072",
                    "created_by_broker_id": 4,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Comp Report — Client 10",
                    "type": "likely_buyer",
                    "created_by": 4
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Comp Report Delivered",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/comp_report_c10.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 10,
                    "title": "Comp report debrief",
                    "start_at": "2025-08-22T18:00:00Z",
                    "end_at": "2025-08-22T18:20:00Z",
                    "location": "Video — Zoom",
                    "notes": "CMA review & Q&A",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 10
                }
            }
        ],
        "outputs": [
                "Comp report saved and updated; campaign verified; email recorded; debrief hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_028",
        "instruction": "Coordinate the preparation of a 15\u2011year financing plan for client 6 under broker 2. The final state involves retrieving the mortgage profile (context) and calculating a mortgage estimate for client 6 at list_price 480000 with term_years 15 and region 'AZ-HOU'; ensure a 'general_update' campaign titled 'Aug 2025 Financing Plan \u2014 Client 6' is available; record one email to client 6 with subject 'Financing Options \u2014 15\u2011year plan' and body_uri 'https://storage.example.com/emails/finance_c6_15yr.html' within the campaign; and arrange a consult hold on 2025\u201108\u201122 21:00\u201321:30Z named 'Financing consult' at 'Video \u2014 Zoom' (source 'follow_up'). Confirm by reviewing the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "GetMortgageProfile",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 6,
                    "list_price": 480000,
                    "term_years": 15,
                    "region": "AZ-HOU"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Financing Plan — Client 6",
                    "type": "general_update",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Financing Options — 15-year plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/finance_c6_15yr.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Financing consult",
                    "start_at": "2025-08-22T21:00:00Z",
                    "end_at": "2025-08-22T21:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 6
                }
            }
        ],
        "outputs": [
                "Mortgage profile referenced; estimate computed; campaign verified; email recorded; consult hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_029",
        "instruction": "Handle the preparation of a briefing packet for client 7 via broker 5. Ensure the final condition is met: a briefing document must be created for client 7 (version_tag defaults to 'v1'), thus the file should be available at 'https://storage.example.com/briefings/client_briefing_007_v1.pdf'; accompany this with an external next\u2011steps checklist attached to the client using file_uri 'https://storage.example.com/checklists/next_steps_c7.pdf' (created_by 5); the existence of a 'general_update' campaign entitled 'Aug 2025 Briefing & Next Steps \u2014 Client 7' is necessary; ensure an email to client 7 with subject 'Briefing Packet & Next Steps' and body_uri 'https://storage.example.com/briefings/client_briefing_007_v1.pdf' is recorded under the campaign; a review hold should be placed for 2025\u201108\u201122 20:00\u201320:20Z, titled 'Briefing review' at 'Video \u2014 Teams' (source 'follow_up'); and post an audit 'briefing_sent' linked to the campaign. Confirm by checking the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 5
                },
            },
            {
                "name": "AttachDocumentToClient",
                "arguments": {
                    "client_id": 7,
                    "file_uri": "https://storage.example.com/checklists/next_steps_c7.pdf",
                    "created_by": 5
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Briefing & Next Steps — Client 7",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 5,
                    "subject": "Briefing Packet & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_007_v1.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 7,
                    "title": "Briefing review",
                    "start_at": "2025-08-22T20:00:00Z",
                    "end_at": "2025-08-22T20:20:00Z",
                    "location": "Video — Teams",
                    "source": "follow_up"
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 5,
                    "action": "briefing_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                    "metadata_json": {
                        "doc_uri": "https://storage.example.com/briefings/client_briefing_007_v1.pdf"
                    }
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 7
                }
            }
        ],
        "outputs": [
                "Briefing generated and referenced; campaign verified; email recorded; review hold present; audit logged."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_030",
        "instruction": "Coordinate a Sunday open\u2011house circuit plan for client 12 with the help of broker 6. Achieve the final state: ensure the system accounts for neighborhoods [4,5] reviewed for open\u2011house timing (context only); a planned route on 2025\u201108\u201124 should be set with the ordered stops ['HTX041','HTX040','HTX048'] and map URL found at 'https://maps.google.com/route/oh_plan_c12_20250824', ensuring that each hop remains feasible within \u226430 minutes; a 'likely_buyer' campaign titled 'Aug 2025 Sunday Open Houses \u2014 Client 12' should be initiated and leveraged for outbound email; confirm one email to client 12, logged with subject 'Open House Plan \u2014 2025\u201108\u201124' and body_uri 'https://maps.google.com/route/oh_plan_c12_20250824'; a same\u2011day hold is to exist for 2025\u201108\u201124 09:20\u201309:30Z under the title 'Pre-drive sync' scheduled at 'Phone' with source 'follow_up'; and an audit event must document the constructed route. Validate your entries by reviewing the campaign, the stored route, the email, and the client\u2019s calendar events.",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        4,
                        5
                    ]
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 12,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX041",
                        "HTX040",
                        "HTX048"
                    ],
                    "map_url": "https://maps.google.com/route/oh_plan_c12_20250824",
                    "created_by_broker_id": 6
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX041",
                        "HTX040",
                        "HTX048"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Sunday Open Houses — Client 12",
                    "type": "likely_buyer",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 6,
                    "subject": "Open House Plan — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/oh_plan_c12_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 12,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:20:00Z",
                    "end_at": "2025-08-24T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 6,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": [
                            "HTX041",
                            "HTX040",
                            "HTX048"
                        ],
                        "map_url": "https://maps.google.com/route/oh_plan_c12_20250824"
                    }
                }
            }
        ],
        "outputs": [
                "Open‑house context confirmed; route saved and hop check OK; campaign exists; email recorded under that campaign; calendar hold present; and the route build is audited."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_031",
        "instruction": "Handle a Heights viewing day setup for client 11 with broker 4. Final outcome: neighborhood open-house windows for a Heights/Galleria mix ([11,6]) must be reviewed; a planned three-stop route for client 11 on 2025-08-22 with designated stops ['HTX055','HTX057','HTX060'] and map link 'https://maps.example.com/route/c11_aug22' needs to be stored unchanged; ensure the route is legible; verify drive-time feasibility does not exceed a 30-minute limit; anchor a campaign named 'Aug 2025 Viewing Requests \u2014 Client 11' with type 'general_update' includes one email featuring the subject 'Viewing Requests Drafts' and body URI 'https://storage.example.com/drafts/client_11_props_3.pdf'; and hold confirmation on 2025-08-22 from 17:00Z to 17:20Z, titled 'Confirm viewing requests' at 'Phone' (origin 'follow_up') should be present on the calendar. Confirm through the open-house review, route particulars, drive-time validation, campaign/email, and the calendar.",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        11,
                        6
                    ]
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 11,
                    "date": "2025-08-22",
                    "stops_ordered_json": [
                        "HTX055",
                        "HTX057",
                        "HTX060"
                    ],
                    "map_url": "https://maps.example.com/route/c11_aug22",
                    "created_by_broker_id": 4
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX055",
                        "HTX057",
                        "HTX060"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Viewing Requests — Client 11",
                    "type": "general_update",
                    "created_by": 4
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 4,
                    "subject": "Viewing Requests Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/drafts/client_11_props_3.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 11,
                    "title": "Confirm viewing requests",
                    "start_at": "2025-08-22T17:00:00Z",
                    "end_at": "2025-08-22T17:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 11
                }
            }
        ],
        "outputs": [
                "Open‑house windows reviewed; route stored and feasible; campaign/email verified; confirmation hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_032",
        "instruction": "Coordinate the assembly of a condo investment package for client 15 under broker 8. The finalized state should include: capturing a clear context view via a draft comps snapshot for subject_property_id 'HTX057' (up to six condo options) that is easy to read; generating a finance estimate for client 15 at a target price of 500000; anchoring a campaign titled 'Aug 2025 Condo Picks \u2014 Client 15' of type 'general_update' which includes one email with the subject 'Condo Investment Picks' and body URI 'https://storage.example.com/emails/condo_invest_c15.html'; and scheduling a consult hold on 2025-08-24 from 20:30Z to 21:00Z titled 'Investment consult' at 'Video \u2014 Zoom' (source 'follow_up') on the calendar. Confirm by checking the comp report, the campaign, the client's email records, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 15,
                    "subject_property_id": "HTX057",
                    "created_by_broker_id": 8,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 15,
                    "list_price": 500000
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Condo Picks — Client 15",
                    "type": "general_update",
                    "created_by": 8
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Condo Investment Picks",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/condo_invest_c15.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Investment consult",
                    "start_at": "2025-08-24T20:30:00Z",
                    "end_at": "2025-08-24T21:00:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 15
                }
            }
        ],
        "outputs": [
                "Snapshot saved and read; finance estimate produced; campaign/email verified; consult hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_033",
        "instruction": "Compile a brief compensation package for client 2 associated with broker 3. Final state: a compensation report is saved for subject_property_id 'HTX049' (created_by_broker_id 3) with status 'draft' and confirmed by read; a 'likely_buyer' campaign titled 'Aug 2025 Quick Comps \u2014 Client 2' is present; an email to client 2 with subject 'Quick Comps Pack' and body_uri 'https://storage.example.com/emails/quick_comps_c2.html' is documented within the campaign; and a follow\u2011up hold is set for 2025\u201108\u201123 14:00\u201314:20Z with the title 'Comps review' at 'Phone' (source 'follow_up'). Verify by reviewing the details of the comp report, the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "HTX049",
                    "created_by_broker_id": 3,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Quick Comps — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Quick Comps Pack",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/quick_comps_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Comps review",
                    "start_at": "2025-08-23T14:00:00Z",
                    "end_at": "2025-08-23T14:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Comp report saved and verified; campaign verified; email recorded; review hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_034",
        "instruction": "Arrange a Saturday route for client 12 with broker 6. Final state: a route for 2025\u201108\u201123 with ordered stops ['HTX032','HTX036','HTX049'] is saved using map URL 'https://maps.google.com/route/weekend_c12_20250823' and passes a 30\u2011minute hop check; a 'likely_buyer' campaign identified as 'Aug 2025 Saturday Tour \u2014 Client 12' is in place; an email to client 12 with subject 'Saturday Route \u2014 2025\u201108\u201123' and body_uri 'https://maps.google.com/route/weekend_c12_20250823' is noted; and two holds are present \u2014 09:40\u201309:50Z named 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10\u201313:30Z labeled 'Tour debrief' at 'Video \u2014 Zoom' (source 'follow_up', notes 'Next steps & offers'). Confirm by checking the route details, the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 12,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX032",
                        "HTX036",
                        "HTX049"
                    ],
                    "map_url": "https://maps.google.com/route/weekend_c12_20250823",
                    "created_by_broker_id": 6
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX032",
                        "HTX036",
                        "HTX049"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Saturday Tour — Client 12",
                    "type": "likely_buyer",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 6,
                    "subject": "Saturday Route — 2025-08-23",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/weekend_c12_20250823",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 12,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-23T09:40:00Z",
                    "end_at": "2025-08-23T09:50:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 12,
                    "title": "Tour debrief",
                    "start_at": "2025-08-23T13:10:00Z",
                    "end_at": "2025-08-23T13:30:00Z",
                    "location": "Video — Zoom",
                    "notes": "Next steps & offers",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 12
                }
            }
        ],
        "outputs": [
                "Route saved and feasible; campaign verified; email recorded; two holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_035",
        "instruction": "Handle the creation of a weekend open-house snapshot for client 4 under broker 2. Final state: ensure that open-house windows are retrieved for properties ['HTX030','HTX031'] for 2025\u201108\u201123 through 2025\u201108\u201124 (context); verify that a 'general_update' campaign named 'Aug 2025 Weekend Open Houses \u2014 Client 4' is established; record an email to client 4 with subject 'Weekend Open Houses' and body_uri 'https://storage.example.com/emails/weekend_open_c4.html' under the campaign; and maintain a planning hold at 2025\u201108\u201123 08:30\u201308:45Z titled 'Plan the route' at 'Phone' (source 'follow_up'). Confirm by reviewing the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "FetchOpenHousesByProperties",
                "arguments": {
                    "property_ids": [
                        "HTX030",
                        "HTX031"
                    ],
                    "date_from": "2025-08-23",
                    "date_to": "2025-08-24"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Weekend Open Houses — Client 4",
                    "type": "general_update",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Weekend Open Houses",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/weekend_open_c4.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 4,
                    "title": "Plan the route",
                    "start_at": "2025-08-23T08:30:00Z",
                    "end_at": "2025-08-23T08:45:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 4
                }
            }
        ],
        "outputs": [
                "Open‑house windows retrieved; campaign verified; email recorded; planning hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_036",
        "instruction": "Coordinate an investor financing check-CO for client 18 under broker 5. Final state: calculate a mortgage estimate for client 18 at list_price 500000 (context); ensure that a 'general_update' campaign named 'Aug 2025 Investor Financing \u2014 Client 18' is in place; log one email to client 18 with subject 'Investor Financing Snapshot' and body_uri 'https://storage.example.com/emails/finance_investor_c18.html' under the campaign; and manage two holds \u2014 2025\u201108\u201122 19:00\u201319:20Z titled 'Lender Q&A' at 'Video \u2014 Zoom' (source 'follow_up') and 2025\u201108\u201124 17:00\u201317:30Z titled 'Docs review' at 'Office' (source 'client_meeting'). Validate by checking the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 18,
                    "list_price": 500000
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Investor Financing — Client 18",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Investor Financing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/finance_investor_c18.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Lender Q&A",
                    "start_at": "2025-08-22T19:00:00Z",
                    "end_at": "2025-08-22T19:20:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Docs review",
                    "start_at": "2025-08-24T17:00:00Z",
                    "end_at": "2025-08-24T17:30:00Z",
                    "location": "Office",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 18
                }
            }
        ],
        "outputs": [
                "Estimate computed; campaign verified; email recorded; two holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_037",
        "instruction": "Handle a v2 briefing for client 3 via broker 1. Final result: a briefing document is produced with version_tag 'v2' and stored at 'https://storage.example.com/briefings/client_briefing_003_v2.pdf'; a 'general_update' campaign titled 'Aug 2025 Briefing v2 \u2014 Client 3' is set up; one email directed to client 3 using template_code 'general_update' with the subject 'Updated Briefing (v2)' and body_uri 'https://storage.example.com/briefings/client_briefing_003_v2.pdf' is documented under that campaign; and a review hold scheduled for 2025\u201108\u201122 16:30\u201316:50Z named 'Briefing v2 review' takes place at 'Video \u2014 Zoom' (source 'follow_up').",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "version_tag": "v2"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Briefing v2 — Client 3",
                    "type": "general_update",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Updated Briefing (v2)",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_003_v2.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Briefing v2 review",
                    "start_at": "2025-08-22T16:30:00Z",
                    "end_at": "2025-08-22T16:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 3
                }
            }
        ],
        "outputs": [
                "Briefing v2 generated; campaign verified; email recorded under the campaign; review hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_038",
        "instruction": "Coordinate a Sunday route plan for client 2 collaborating with broker 3 using neighborhood context. The end goal should detail: open\u2011house windows for neighborhood [1] were utilized as context; a route dated 2025\u201108\u201124 is recorded with sequential stops ['HTX001','HTX004','HTX005'] and map URL 'https://maps.google.com/route/sun_c2_20250824'; a 30\u2011minute hop check is approved; a 'likely_buyer' campaign named 'Aug 2025 Sunday Route \u2014 Client 2' is present; one email sent to client 2 using template_code 'likely_buyer' with subject 'Sunday Route \u2014 2025\u201108\u201124' and the same map URL as body_uri is logged under the campaign; and two holds are scheduled \u2014 09:55\u201310:05Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10\u201313:25Z titled 'Post\u2011route debrief' at 'Phone' (source 'follow_up'). Record an audit of the route.",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        1
                    ]
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "map_url": "https://maps.google.com/route/sun_c2_20250824",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Sunday Route — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Sunday Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/sun_c2_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T09:55:00Z",
                    "end_at": "2025-08-24T10:05:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Post-route debrief",
                    "start_at": "2025-08-24T13:10:00Z",
                    "end_at": "2025-08-24T13:25:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 3,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                }
            }
        ],
        "outputs": [
                "Route saved and feasible; campaign verified; email recorded; two holds present; route audit logged and proven."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_039",
        "instruction": "Handle a general update for both clients 13 and 14 under broker 5. Final state: a listings context search occurs for neighborhoods [2,3,4], allowing up to 6 results (limit 6); a 'general_update' campaign titled 'Aug 2025 Multi\u2011Client Update \u2014 C13 & C14' is in place; two emails are logged \u2014 both with subject 'August Market & Listings' and body_uri 'https://storage.example.com/emails/aug_market_multi.html' \u2014 one for each client under the same campaign; and two holds are scheduled on 2025\u201108\u201122: client 13 from 16:00\u201316:20Z and client 14 from 16:30\u201316:50Z, both labeled 'Discuss August update' at 'Phone' (source 'follow_up'). Confirm by reviewing the campaign, emails for both clients, and their calendar events.",
        "actions": [
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        2,
                        3,
                        4
                    ],
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Multi‑Client Update — C13 & C14",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "August Market & Listings",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/aug_market_multi.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "August Market & Listings",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/aug_market_multi.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 13,
                    "title": "Discuss August update",
                    "start_at": "2025-08-22T16:00:00Z",
                    "end_at": "2025-08-22T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "Discuss August update",
                    "start_at": "2025-08-22T16:30:00Z",
                    "end_at": "2025-08-22T16:50:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 14
                }
            }
        ],
        "outputs": [
                "Context search run; campaign verified; two emails recorded; two follow‑up holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_040",
        "instruction": "Coordinate a four\u2011stop tour for client 1 under broker 3. Final state: a route for 2025\u201108\u201124 is documented with stops in order ['HTX021','HTX025','HTX029','HTX030'] and map URL 'https://maps.google.com/route/four_stop_c1_20250824'; the route successfully passes a 30\u2011minute hop check; a 'likely_buyer' campaign titled 'Aug 2025 Four\u2011Stop Tour \u2014 Client 1' is established; an email to client 1, which includes the subject 'Four\u2011Stop Tour \u2014 2025\u201108\u201124' and the map URL as body_uri, is logged; and two holds are in place \u2014 09:20\u201309:30Z labeled 'Pre\u2011drive sync' at 'Phone' (source 'follow_up', notes 'Confirm sequence & parking') and 14:00\u201314:20Z labeled 'Tour debrief' at 'Video \u2014 Zoom' (source 'follow_up'). Verify by reviewing the route details, the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 1,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX021",
                        "HTX025",
                        "HTX029",
                        "HTX030"
                    ],
                    "map_url": "https://maps.google.com/route/four_stop_c1_20250824",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX021",
                        "HTX025",
                        "HTX029",
                        "HTX030"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Four‑Stop Tour — Client 1",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Four-Stop Tour — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/four_stop_c1_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:20:00Z",
                    "end_at": "2025-08-24T09:30:00Z",
                    "location": "Phone",
                    "notes": "Confirm sequence & parking",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Tour debrief",
                    "start_at": "2025-08-24T14:00:00Z",
                    "end_at": "2025-08-24T14:20:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 1
                }
            }
        ],
        "outputs": [
                "Route saved and feasible; campaign verified; email recorded; two holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_041",
        "instruction": "Handle the preparation and delivery of comps for client 14 under broker 5. The final condition: a comp report is saved with status 'draft' for subject_property_id 'HTX060' (created_by_broker_id 5), verified through reading, then modified to 'sent_to_client' and re-verified; a follow-up hold is scheduled for 2025-08-22 18:30-18:50Z with the title 'Discuss comp findings' via 'Phone' (source 'follow_up'). Confirm by reviewing the comp report details after saving and status updating, along with the client\u2019s calendar events.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 14,
                    "subject_property_id": "HTX060",
                    "created_by_broker_id": 5,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "Discuss comp findings",
                    "start_at": "2025-08-22T18:30:00Z",
                    "end_at": "2025-08-22T18:50:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 14
                }
            }
        ],
        "outputs": [
                "Comp report saved and updated; follow‑up hold present and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_042",
        "instruction": "Coordinate the assembly of seller-outreach drafts for client 19 under broker 7. The end result: a bundle of drafts is compiled for property_ids ['HTX070','HTX071','HTX072','HTX073'] (context), stored at 'https://storage.example.com/drafts/client_19_props_4.pdf'; a 'general_update' campaign titled 'Aug 2025 Seller Outreach \u2014 Client 19' is set up; a single email to client 19 using template_code 'general_update' with the subject 'Seller Outreach Drafts' and body_uri 'https://storage.example.com/drafts/client_19_props_4.pdf' is documented under the campaign; and a hold is placed for 2025-08-23 12:00-12:20Z titled 'Select which drafts to send' via 'Phone' (source 'follow_up').",
        "actions": [
            {
                "name": "DraftSellerBrokerEmails",
                "arguments": {
                    "client_id": 19,
                    "property_ids": [
                        "HTX070",
                        "HTX071",
                        "HTX072",
                        "HTX073"
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Seller Outreach — Client 19",
                    "type": "general_update",
                    "created_by": 7
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Seller Outreach Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/drafts/client_19_props_4.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 19,
                    "title": "Select which drafts to send",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 19
                }
            }
        ],
        "outputs": [
                "Drafts generated; campaign verified; email recorded referencing the drafts URI; selection hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_043",
        "instruction": "Handle the creation of a first-time buyer packet for client 16 under the guidance of broker 8. End state: a briefing document is prepared for client 16 (defaults to 'v1') and saved at 'https://storage.example.com/briefings/client_briefing_016_v1.pdf'; a 'general_update' campaign titled 'Aug 2025 First-Time Buyer Packet \u2014 Client 16' is established; an email directed to client 16 using the template_code 'general_update' with the subject 'Your First-Time Buyer Packet' and body_uri 'https://storage.example.com/briefings/client_briefing_016_v1.pdf' is logged within the campaign; and a reminder hold is scheduled for 2025-08-21 23:00-23:10Z titled 'Packet follow-up' via 'Phone' (source 'follow_up').",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 8
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 First‑Time Buyer Packet — Client 16",
                    "type": "general_update",
                    "created_by": 8
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Your First-Time Buyer Packet",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_016_v1.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 16,
                    "title": "Packet follow-up",
                    "start_at": "2025-08-21T23:00:00Z",
                    "end_at": "2025-08-21T23:10:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 16
                }
            }
        ],
        "outputs": [
                "Briefing doc generated; campaign verified; email recorded using the generated doc URI; reminder hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_044",
        "instruction": "Coordinate the provision of regional financing guidance for client 17 under broker 10's directive. End state: a mortgage estimate is calculated for client 17 at list_price 650000 with term_years 30 and region 'CA-SF' (context provided); a 'general_update' campaign named 'Aug 2025 SF Financing \u2014 Client 17' is created; an email to client 17 using template_code 'general_update' with the subject 'San Francisco Financing Snapshot' and body_uri 'https://storage.example.com/emails/finance_sf_c17.html' is documented under the campaign; and a consult hold is arranged for 2025-08-22 22:00-22:30Z titled 'Financing consult (SF)' via 'Video \u2014 Zoom' (source 'follow_up').",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 17,
                    "list_price": 650000,
                    "term_years": 30,
                    "region": "CA-SF"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 SF Financing — Client 17",
                    "type": "general_update",
                    "created_by": 10
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "San Francisco Financing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/finance_sf_c17.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 10,
                    "client_id": 17,
                    "title": "Financing consult (SF)",
                    "start_at": "2025-08-22T22:00:00Z",
                    "end_at": "2025-08-22T22:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 17
                }
            }
        ],
        "outputs": [
                "Estimate computed; campaign verified; email recorded under the campaign; SF consult hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_045",
        "instruction": "Coordinate a Northside Sunday tour for client 20 under broker 11. Resulting state: a route for 2025\u201108\u201124 is recorded with ordered stops ['HTX066','HTX067','HTX068'] and the map URL 'https://maps.google.com/route/northside_c20_20250824'; ensure a hop check confirms \u226430 minutes between stops; a 'likely_buyer' campaign titled 'Aug 2025 Northside Tour \u2014 Client 20' is established; an email to client 20 with the subject 'Northside Route \u2014 2025\u201108\u201124' and the map URL as body_uri is logged; and two holds are placed \u2014 09:15\u201309:25Z named 'Pre\u2011drive check' at 'Phone' (source 'follow_up') and 12:45\u201313:05Z named 'Debrief call' at 'Phone' (source 'follow_up'). Confirm by reviewing the route details, the campaign, the email, and the calendar events.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 20,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX066",
                        "HTX067",
                        "HTX068"
                    ],
                    "map_url": "https://maps.google.com/route/northside_c20_20250824",
                    "created_by_broker_id": 11
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX066",
                        "HTX067",
                        "HTX068"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Northside Tour — Client 20",
                    "type": "likely_buyer",
                    "created_by": 11
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Northside Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/northside_c20_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 20,
                    "title": "Pre-drive check",
                    "start_at": "2025-08-24T09:15:00Z",
                    "end_at": "2025-08-24T09:25:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 20,
                    "title": "Debrief call",
                    "start_at": "2025-08-24T12:45:00Z",
                    "end_at": "2025-08-24T13:05:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 20
                }
            }
        ],
        "outputs": [
                "Route saved and feasible; campaign verified; email recorded; two follow‑up holds present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_046",
        "instruction": "Handle the assembly of an investor packet for client 20 under broker 11. Final state: a client briefing document (default version) is created; the campaign titled 'Aug 2025 Investor Packet \u2014 Client 20' is of type 'general_update' is in place; an email to client 20 with subject 'Investor Packet' contains the generated briefing link as the body; and a review hold on 2025\u201108\u201122 from 20:00Z to 20:25Z titled 'Investor packet review' at 'Video \u2014 Zoom' (source 'follow_up') is scheduled in the calendar. Confirm through the campaign read, the client\u2019s email log, and the calendar.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 11
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Investor Packet — Client 20",
                    "type": "general_update",
                    "created_by": 11
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Investor Packet",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_020_v1.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 20,
                    "title": "Investor packet review",
                    "start_at": "2025-08-22T20:00:00Z",
                    "end_at": "2025-08-22T20:25:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 20
                }
            }
        ],
        "outputs": [
                "Briefing generated and referenced via email; campaign verified; review hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_047",
        "instruction": "Handle the delivery of a comps\u2011and\u2011status package for client 6 under broker 2. Final condition: a comp report for subject_property_id 'HTX058' (created_by_broker_id 2) is saved with status 'draft' and verified; subsequently, its status is changed to 'sent_to_client' and re\u2011verified; a 'likely_buyer' campaign titled 'Aug 2025 Comps Sent \u2014 Client 6' exists; an email to client 6 using template_code 'likely_buyer' with subject 'Comps Sent' and body_uri 'https://storage.example.com/emails/comps_sent_c6.html' is recorded in the campaign; and a debrief hold is noted on 2025\u201108\u201122 18:40\u201319:00Z titled 'Comps debrief' at 'Phone' (source 'follow_up').",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 6,
                    "subject_property_id": "HTX058",
                    "created_by_broker_id": 2,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Comps Sent — Client 6",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Comps Sent",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/comps_sent_c6.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Comps debrief",
                    "start_at": "2025-08-22T18:40:00Z",
                    "end_at": "2025-08-22T19:00:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 6
                }
            }
        ],
        "outputs": [
                "Comp report saved and updated; campaign verified; email recorded under the campaign; debrief hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_048",
        "instruction": "Coordinate the delivery of a combined comps\u2011and\u2011tour plan for client 2 under broker 3. End result: a comp report for subject_property_id 'HTX041' (created_by_broker_id 3) is saved with status 'draft' and verified; a Saturday route dated 2025\u201108\u201123 is saved with ordered stops ['HTX041','HTX032','HTX036'] and map URL 'https://maps.google.com/route/comp_tour_c2_20250823', adhering to a \u226430\u2011minute hop constraint; a 'likely_buyer' campaign named 'Aug 2025 Comp + Tour \u2014 Client 2' exists; two emails are cataloged under the campaign for client 2 \u2014 one with template_code 'likely_buyer' having subject 'Comps Overview' and body_uri 'https://storage.example.com/emails/comps_overview_c2.html', and another using template_code 'likely_buyer' with subject 'Saturday Tour Plan' and body_uri 'https://maps.google.com/route/comp_tour_c2_20250823'; and two holds are established \u2014 2025\u201108\u201122 18:00\u201318:20Z titled 'Comps review' at 'Phone' (source 'follow_up') and 2025\u201108\u201123 09:40\u201309:50Z titled 'Depart for tour' at 'Client Home' (source 'viewing'). Document an audit 'routes_shared_and_viewings_set' on the route.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "HTX041",
                    "created_by_broker_id": 3,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 2,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX041",
                        "HTX032",
                        "HTX036"
                    ],
                    "map_url": "https://maps.google.com/route/comp_tour_c2_20250823",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX041",
                        "HTX032",
                        "HTX036"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Comp + Tour — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Comps Overview",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/comps_overview_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Saturday Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/comp_tour_c2_20250823",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Comps review",
                    "start_at": "2025-08-22T18:00:00Z",
                    "end_at": "2025-08-22T18:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Depart for tour",
                    "start_at": "2025-08-23T09:40:00Z",
                    "end_at": "2025-08-23T09:50:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 3,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                }
            }
        ],
        "outputs": [
                "Comp report verified; route saved and feasible; campaign verified; two emails recorded; two holds present; route audit logged and proven."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_049",
        "instruction": "Handle the preparation of an investor-focused condo snapshot for client 15 under broker 8. End state: ensure a listings context run for neighborhoods [5,12,1,7] with property_type 'condo' and price 246399\u2013420408 (limit 6) is on record; calculate a mortgage estimate for client 15 at list_price 400000; a 'general_update' campaign titled 'Aug 2025 Investor Snapshot \u2014 Client 15' is created and used for one email to client 15 with subject 'Condo Investor Snapshot' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/investor_snapshot_c15.html'; schedule a consult hold on 2025-08-24 20:30\u201321:00Z called 'Investor consult' at 'Video \u2014 Zoom' (source 'follow_up'). Verify the records by reading back the campaign, the client\u2019s emails, and the client\u2019s calendar events.",
        "actions": [
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        5,
                        12,
                        1,
                        7
                    ],
                    "property_type": "condo",
                    "price_min": 246399,
                    "price_max": 420408,
                    "limit": 6
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 15,
                    "list_price": 400000
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Investor Snapshot — Client 15",
                    "type": "general_update",
                    "created_by": 8
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Condo Investor Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/investor_snapshot_c15.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Investor consult",
                    "start_at": "2025-08-24T20:30:00Z",
                    "end_at": "2025-08-24T21:00:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 15
                }
            }
        ],
        "outputs": [
                "Campaign 9 verified; email recorded for client 15; consult scheduled 2025-08-24 20:30Z."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_050",
        "instruction": "Coordinate the creation of a bordering-area Sunday tour for client 2 with broker 3. End state: obtain neighborhood 1 details and its bordering list (context); save a route for 2025-08-24 with ordered stops ['HTX001','HTX004','HTX005'] and map 'https://maps.google.com/route/dt_mid_c2_20250824'; verify that hops pass a \u226430-minute check; a 'likely_buyer' campaign titled 'Aug 2025 Bordering Tour \u2014 Client 2' is established; record one email to client 2 with subject 'Bordering Tour \u2014 2025-08-24' (template_code 'likely_buyer') utilizing that map URL as body_uri; create two holds: 09:55\u201310:05Z 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10\u201313:25Z 'Post-tour debrief' at 'Phone' (source 'follow_up'); document an audit 'open_house_route_built' on the route and reread the route to confirm the state.",
        "actions": [
            {
                "name": "GetNeighborhoodDetails",
                "arguments": {
                    "neighborhood_id": 1
                },
            },
            {
                "name": "GetBorderingNeighborhoods",
                "arguments": {
                    "neighborhood_id": 1
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "map_url": "https://maps.google.com/route/dt_mid_c2_20250824",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX001",
                        "HTX004",
                        "HTX005"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Bordering Tour — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Tour — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/dt_mid_c2_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T09:55:00Z",
                    "end_at": "2025-08-24T10:05:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Post-tour debrief",
                    "start_at": "2025-08-24T13:10:00Z",
                    "end_at": "2025-08-24T13:25:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 3,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": [
                            "HTX001",
                            "HTX004",
                            "HTX005"
                        ]
                    }
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                }
            }
        ],
        "outputs": [
                "Route 11 feasible; campaign 9 verified; email present; both holds present; audit logged & route re-read."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_051",
        "instruction": "Complete a comparative market analysis for client 11 under broker 6. End state: the record for subject property 'HTX012' contains a document link and a final status of 'sent_to_client', with the session's activity indicating it originated as a draft during this workflow. Initiate one client-facing outreach under a campaign titled 'Aug 2025 CMA Delivered \u2014 Client 11' with a single message to client 11, titled 'Your CMA', using the body URI 'https://storage.example.com/emails/cma_c11.html' and the likely-buyer template. Confirm completion by retrieving the report\u2019s details and the client's campaign/email records.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 11,
                    "subject_property_id": "HTX012",
                    "created_by_broker_id": 6,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 CMA Delivered — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Your CMA",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/cma_c11.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 11
                }
            }
        ],
        "outputs": [
                "Report 9 saved then sent_to_client; campaign verified; email recorded."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_052",
        "instruction": "Conduct paired likely-buyer updates for clients 1 and 2 from broker 3. End state: one campaign titled 'Aug 2025 Paired Likely Buyers \u2014 C1 & C2' of type 'likely_buyer' facilitates two emails with subject 'August Listings Shortlist' and body URI 'https://storage.example.com/emails/aug_shortlist.html'; and two phone holds on 2025-08-23 titled 'Intro call about shortlist' are scheduled for client 1 (15:00\u201315:30Z) and client 2 (16:00\u201316:20Z), both sourced from 'follow_up'. Validate via the campaign read, each client\u2019s email log, and both calendars.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Paired Likely Buyers — C1 & C2",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/aug_shortlist.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/aug_shortlist.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-23T15:00:00Z",
                    "end_at": "2025-08-23T15:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-23T16:00:00Z",
                    "end_at": "2025-08-23T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Campaign verified; both emails present; both phone holds present for 2025-08-23."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_053",
        "instruction": "Handle the preparation of a sales-context financing snapshot for client 8, under broker 12, with a focus on Medical Center condos. The final outcome should include: acquiring recent sales data for property_id 'HTX049' (limited to 3) as context; computing a mortgage estimate for client 8 at a list_price of 550000; the existence and utilization of a 'general_update' campaign called 'Aug 2025 Med Center Finance \u2014 Client 8' for sending one email with the subject 'Medical Center Finance Snapshot' (template_code 'general_update') and using body_uri 'https://storage.example.com/emails/medcenter_finance_c8.html'; the scheduling of a consult hold for 2025-08-26 from 09:00 to 09:30Z entitled 'Financing consult' located at 'Video \u2014 Zoom' (origin 'follow_up'). Confirm via campaign, emails, and calendar reads.",
        "actions": [
            {
                "name": "FetchRecentSalesByProperty",
                "arguments": {
                    "property_id": "HTX049",
                    "limit": 3
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 8,
                    "list_price": 550000
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Med Center Finance — Client 8",
                    "type": "general_update",
                    "created_by": 12
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Medical Center Finance Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/medcenter_finance_c8.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Financing consult",
                    "start_at": "2025-08-26T09:00:00Z",
                    "end_at": "2025-08-26T09:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 8
                }
            }
        ],
        "outputs": [
                "Campaign 9 verified; email for client 8 present; consult hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_054",
        "instruction": "Coordinate the completion of a museum-area townhouse tour for client 12, operating under broker 3, and incorporate seller\u2011broker outreach drafts. The desired end state is: establishing a route for 2025-08-25 with arranged stops ['HTX044','HTX036','HTX032'] and saving the map 'https://maps.google.com/route/museum_townhouse_c12_20250825' for reading; confirming drive-time feasibility within \u226430 minutes; ensuring an outreach drafts bundle for these stops is available with its link included in the client email body; creating a campaign named 'Aug 2025 Townhouse Tour \u2014 Client 12' of type 'likely_buyer' and sending one email with the subject 'Townhouse Tour Plan'; setting a same-day hold from 13:30 to 13:45Z titled 'Pre-tour sync' at 'Phone' (origin 'follow_up') on the calendar; and auditing the route as shared before rereading. Validate through route details, drive-time verification, campaign/email, and calendar checks.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 12,
                    "date": "2025-08-25",
                    "stops_ordered_json": [
                        "HTX044",
                        "HTX036",
                        "HTX032"
                    ],
                    "map_url": "https://maps.google.com/route/museum_townhouse_c12_20250825",
                    "created_by_broker_id": 3
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX044",
                        "HTX036",
                        "HTX032"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "DraftSellerBrokerEmails",
                "arguments": {
                    "client_id": 12,
                    "property_ids": [
                        "HTX044",
                        "HTX036",
                        "HTX032"
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Townhouse Tour — Client 12",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/drafts/client_12_props_3.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Pre-tour sync",
                    "start_at": "2025-08-25T13:30:00Z",
                    "end_at": "2025-08-25T13:45:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 3,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                }
            }
        ],
        "outputs": [
                "Route 11 saved and feasible; drafts referenced via email; campaign verified; email and hold present; audit logged & route re-read."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_055",
        "instruction": "Coordinate a v3 client briefing delivery for client 16 under broker 8. Final result: a briefing document is created with version_tag 'v3' and stored at 'https://storage.example.com/briefings/client_briefing_016_v3.pdf'; a 'general_update' campaign named 'Aug 2025 Briefing v3 \u2014 Client 16' is set up and utilized for an email with the subject 'Briefing v3' (template_code 'general_update') using the provided file URI as body_uri; a reminder hold is scheduled for 2025-08-31 12:30\u201312:50Z with the title 'Briefing v3 review' at 'Video \u2014 Zoom' (source 'follow_up'). Confirm by reviewing the campaign, emails, and calendar.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 8,
                    "version_tag": "v3"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Briefing v3 — Client 16",
                    "type": "general_update",
                    "created_by": 8
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Briefing v3",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_016_v3.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 16,
                    "title": "Briefing v3 review",
                    "start_at": "2025-08-31T12:30:00Z",
                    "end_at": "2025-08-31T12:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 16
                }
            }
        ],
        "outputs": [
                "Briefing v3 email recorded; review reminder present; campaign verified."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_056",
        "instruction": "Handle the completion of a Westbury CMA + follow-up workflow for client 21 under broker 4. Desired outcome: save a draft of the comp report for subject 'WESTBURY_CMA_C21_AUG25' and ensure it is readable, then change its status to 'sent_to_client' and verify it again; a campaign titled 'Aug 2025 Westbury CMA \u2014 Client 21' (type 'general_update') is established to send an email to client 21 with the subject 'Your Westbury CMA' using the 'general_update' template and body URI 'https://storage.example.com/emails/westbury_cma_c21.html'; additionally, a follow-up hold for 2025-08-23 from 15:30Z to 15:50Z titled 'CMA Q&A' at 'Video \u2014 Zoom' (source 'follow_up') should be present on the calendar. Validate by checking the comp report, campaign, client's email log, and client's calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 21,
                    "subject_property_id": "WESTBURY_CMA_C21_AUG25",
                    "created_by_broker_id": 4,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Westbury CMA — Client 21",
                    "type": "general_update",
                    "created_by": 4
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 21,
                    "broker_id": 4,
                    "subject": "Your Westbury CMA",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/westbury_cma_c21.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 21
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 21,
                    "title": "CMA Q&A",
                    "start_at": "2025-08-23T15:30:00Z",
                    "end_at": "2025-08-23T15:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 21
                }
            }
        ],
        "outputs": [
                "Report saved then sent_to_client; campaign/email verified; follow-up scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_057",
        "instruction": "Handle the creation of a weekend open-house summary for client 10 under broker 11. Final state: open-house windows are retrieved for neighborhoods [13,1,12] (context); a 'general_update' campaign entitled 'Aug 2025 Weekend OH \u2014 Client 10' is in place; an email sent to client 10 with the subject 'Weekend Open Houses' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/weekend_oh_c10.html' is documented; a planning hold is scheduled for 2025-08-23 13:00\u201313:20Z named 'Plan weekend open houses' using 'Phone' (source 'follow_up'). Confirm with required reads.",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        13,
                        1,
                        12
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Weekend OH — Client 10",
                    "type": "general_update",
                    "created_by": 11
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Weekend Open Houses",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/weekend_oh_c10.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 10,
                    "title": "Plan weekend open houses",
                    "start_at": "2025-08-23T13:00:00Z",
                    "end_at": "2025-08-23T13:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 10
                }
            }
        ],
        "outputs": [
                "Campaign 9 verified; open-house overview sent; planning hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_058",
        "instruction": "Coordinate and distribute a duplex shortlist for client 6 under broker 2. Final state: a recorded snapshot is available for subject property ID 'DPLX_C6_AUG25' in draft status and accessible; a listing view, limited to six entries, displays active duplex options in neighborhoods [8,12,6,5] within 147021-402736 for context; a single client interaction is noted under a campaign named 'Aug 2025 Duplex Shortlist - Client 6' with the subject 'Duplexes That Fit' using body URI 'https://storage.example.com/emails/duplex_shortlist_c6.html' and the likely-buyer template; and a follow-up phone hold on 2025-08-23 from 18:40Z to 19:00Z titled 'Shortlist debrief' (source 'follow_up') is on the client\u2019s calendar. Confirm by reviewing the saved snapshot, the campaign record, the client\u2019s email log, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 6,
                    "subject_property_id": "DPLX_C6_AUG25",
                    "created_by_broker_id": 2,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        8,
                        12,
                        6,
                        5
                    ],
                    "property_type": "duplex",
                    "price_min": 147021,
                    "price_max": 402736,
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Duplex Shortlist - Client 6",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Duplexes That Fit",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/duplex_shortlist_c6.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Shortlist debrief",
                    "start_at": "2025-08-23T18:40:00Z",
                    "end_at": "2025-08-23T19:00:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 6
                }
            }
        ],
        "outputs": [
                "Snapshot saved and verified; campaign/email verified; debrief call scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_059",
        "instruction": "Handle a stats update for Central City/Uptown regarding client 1 under broker 1. The desired outcome: there should be a 'general_update' campaign titled 'Aug 2025 DT/Uptown Stats \u2014 Client 1', which is utilized for one email to client 1 with the subject 'DT/Uptown Q3 Snapshot' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/dt_mid_q3_c1.html'; a follow-up hold is scheduled for 2025-08-25 09:00\u201309:30Z named 'Follow-up Check-CO \u2014 DT/Uptown' occurring via 'Phone' (source 'follow_up'); an audit entry 'campaign_sent' is recorded on the campaign and the campaign is reviewed to verify the state.",
        "actions": [
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 DT/Uptown Stats — Client 1",
                    "type": "general_update",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "DT/Uptown Q3 Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/dt_mid_q3_c1.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 1,
                    "title": "Follow-up Check-CO — DT/Uptown",
                    "start_at": "2025-08-25T09:00:00Z",
                    "end_at": "2025-08-25T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 1
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 1,
                    "action": "campaign_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                }
            }
        ],
        "outputs": [
                "Campaign/email/hold verified; audit logged and campaign re-read."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_060",
        "instruction": "Coordinate the creation of a comps report draft for client 19 under broker 7 and proceed to share it. The required outcome: a comps report is saved for subject_property_id 'HTX044' with the status 'draft' and verified through reading; a 'general_update' campaign titled 'Aug 2025 CMA Draft \u2014 Client 19' is present and utilized for a single email with the subject 'Your CMA Draft' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/cma_draft_c19.html'; a consultation hold is placed on 2025-08-23 12:40\u201313:00Z titled 'CMA Draft consult' to take place via 'Phone' (source 'follow_up'). Confirm through verification by reading.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 19,
                    "subject_property_id": "HTX044",
                    "created_by_broker_id": 7,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 CMA Draft — Client 19",
                    "type": "general_update",
                    "created_by": 7
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Your CMA Draft",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/cma_draft_c19.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 19
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 19,
                    "title": "CMA Draft consult",
                    "start_at": "2025-08-23T12:40:00Z",
                    "end_at": "2025-08-23T13:00:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 19
                }
            }
        ],
        "outputs": [
                "Report 9 verified; campaign/email/consult present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_061",
        "instruction": "Handle an expansion of client 4\u2019s condo search under broker 2. End state: neighborhood 15 details along with bordering IDs are obtained (context); listings are investigated within the exact bordering set returned for property_type 'apartment' and price 201911\u2013507035 (limit 6) for context; a 'general_update' campaign named 'Aug 2025 Bordering Apartment Picks \u2014 Client 4' is in place and is utilized for one email with subject 'Bordering Options' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/border_apts_c4.html'; arrange a 2025-08-22 15:00\u201315:30Z hold titled 'Pre-tour call' at 'Video \u2014 Zoom' (source 'follow_up'). Confirm with reads.",
        "actions": [
            {
                "name": "GetNeighborhoodDetails",
                "arguments": {
                    "neighborhood_id": 15
                },
            },
            {
                "name": "GetBorderingNeighborhoods",
                "arguments": {
                    "neighborhood_id": 15
                },
            },
            {
                "name": "SearchListingsInNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        14
                    ],
                    "property_type": "apartment",
                    "price_min": 201911,
                    "price_max": 507035,
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Bordering Apartment Picks — Client 4",
                    "type": "general_update",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Bordering Options",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/border_apts_c4.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 4
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 4,
                    "title": "Pre-tour call",
                    "start_at": "2025-08-22T15:00:00Z",
                    "end_at": "2025-08-22T15:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 4
                }
            }
        ],
        "outputs": [
                "Bordering set used → listings context; campaign/email verified; pre-tour call present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_062",
        "instruction": "Coordinate a delivery of a Medical Center luxury snapshot for client 8 under broker 5. End state: a compact inventory view captures up to six active listings across neighborhoods [13,9,14,15,11] within the 273024\u2013868888 price range; a finance estimate for client 8 is generated using a target price of 800000 over 30 years in region AZ; one client update is linked to a campaign titled 'Aug 2025 Med Center Luxury \u2014 Client 8' with subject 'Luxury Snapshot' that uses 'https://storage.example.com/emails/medcenter_luxury_c8.html' as the body and the likely-buyer template; and a Zoom consult on 2025-08-26 from 10:00Z to 10:30Z titled 'Luxury plan consult' is scheduled on the calendar. Validate completion by presenting the outreach in the email log, the campaign record, the calendar entry, and the finance estimate.",
        "actions": [
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        13,
                        9,
                        14,
                        15,
                        11
                    ],
                    "price_min": 273024,
                    "price_max": 868888,
                    "limit": 6
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 8,
                    "list_price": 800000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Med Center Luxury — Client 8",
                    "type": "likely_buyer",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 5,
                    "subject": "Luxury Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/medcenter_luxury_c8.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 8,
                    "title": "Luxury plan consult",
                    "start_at": "2025-08-26T10:00:00Z",
                    "end_at": "2025-08-26T10:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 8
                }
            }
        ],
        "outputs": [
                "Campaign/email verified; mortgage estimate saved; consult scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_063",
        "instruction": "Coordinate the creation of a curated shortlist by ID for client 11 under broker 6. End state: listings [15,16,17] are consulted with property details (context); a 'likely_buyer' campaign named 'Aug 2025 Curated Picks \u2014 Client 11' is available and utilized for one email with subject 'Handpicked Listings' (template_code 'likely_buyer') and body_uri 'https://storage.example.com/emails/curated_picks_c11.html'; schedule a 2025-08-24 11:10\u201311:30Z hold titled 'Curated picks debrief' at 'Phone' (source 'follow_up'). Confirm by reads.",
        "actions": [
            {
                "name": "ListListingsByIds",
                "arguments": {
                    "listing_ids": [
                        15,
                        16,
                        17
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Curated Picks — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Handpicked Listings",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/curated_picks_c11.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Curated picks debrief",
                    "start_at": "2025-08-24T11:10:00Z",
                    "end_at": "2025-08-24T11:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 11
                }
            }
        ],
        "outputs": [
                "Curated items read; campaign/email verified; debrief hold present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_064",
        "instruction": "Handle the preparation of a townhouse seeker brief for client 12 with broker 3. End state: retrieve neighborhood 11 details along with its neighboring IDs; conduct searches within [11,1,13] for property_type 'townhouse' and price 128758\u2013279350 (limit 6) as context; ensure a 'likely_buyer' campaign named 'Aug 2025 Townhouse Path \u2014 Client 12' is in place; record one email to client 12 with subject 'Townhouse Options' (template_code 'likely_buyer') and body_uri 'https://storage.example.com/emails/townhouse_path_c12.html'; set a 2025-08-25 14:30\u201314:50Z hold titled 'Townhouse plan' at 'Phone' (source 'follow_up'). Verify via reads.",
        "actions": [
            {
                "name": "GetNeighborhoodDetails",
                "arguments": {
                    "neighborhood_id": 11
                },
            },
            {
                "name": "GetBorderingNeighborhoods",
                "arguments": {
                    "neighborhood_id": 11
                },
            },
            {
                "name": "SearchListingsInNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        11,
                        1,
                        13
                    ],
                    "property_type": "townhouse",
                    "price_min": 128758,
                    "price_max": 279350,
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Townhouse Path — Client 12",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/townhouse_path_c12.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Townhouse plan",
                    "start_at": "2025-08-25T14:30:00Z",
                    "end_at": "2025-08-25T14:50:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 12
                }
            }
        ],
        "outputs": [
                "Neighborhood & borders loaded; context search saved; campaign/email/hold verified."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_065",
        "instruction": "Handle drafting a comps report for client 2 under broker 14 and incorporate an internal broker debrief. Desired outcome: the comp report for subject_property_id 'HTX017' is stored as 'draft' and accessible; a 'likely_buyer' campaign titled 'Aug 2025 Comps Draft \u2014 Client 2' is created; one email to client 2 with subject 'Comps Draft' (template_code 'likely_buyer') and body_uri 'https://storage.example.com/emails/comps_draft_c2.html' is logged; two appointments are noted \u2014 2025-08-27 15:00\u201315:30Z labeled 'Urban Living Property Tour' at '2222 Smith Street Unit 405, Phoenix, AZ 77002' (source 'viewing'), and 2025-08-27 18:10\u201318:30Z titled 'Broker internal debrief' at 'Office' (source 'follow_up'). Confirm through reads.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "HTX017",
                    "created_by_broker_id": 14,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Comps Draft — Client 2",
                    "type": "likely_buyer",
                    "created_by": 14
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Comps Draft",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/comps_draft_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Urban Living Property Tour",
                    "start_at": "2025-08-27T15:00:00Z",
                    "end_at": "2025-08-27T15:30:00Z",
                    "location": "2222 Smith Street Unit 405, Phoenix, AZ 77002",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Broker internal debrief",
                    "start_at": "2025-08-27T18:10:00Z",
                    "end_at": "2025-08-27T18:30:00Z",
                    "location": "Office",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "CMA draft verified; campaign/email recorded; both events present."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_066",
        "instruction": "Coordinate sending a premium-area update for client 5 under broker 5. Target outcome: a snapshot for subject property ID 'ROX_PREM_C5_AUG25' is documented in draft mode and is accessible; the inventory view shows up to six active matches across neighborhoods [6,2,4,10] within 147268-644740 for context; a campaign titled 'Aug 2025 Desert Ridge Premium - Client 5' with subject 'Premium Area Update' using body URI 'https://storage.example.com/emails/riveroaks_premium_c5.html' and the general-update template is linked; and a follow-up phone appointment on 2025-08-23 from 12:00Z to 12:20Z labeled 'Discuss premium options' (source 'follow_up') is recorded on the calendar. Validate through the saved snapshot, the campaign log, the client\u2019s email records, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 5,
                    "subject_property_id": "ROX_PREM_C5_AUG25",
                    "created_by_broker_id": 5,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "SearchListings",
                "arguments": {
                    "neighborhood_ids": [
                        6,
                        2,
                        4,
                        10
                    ],
                    "price_min": 147268,
                    "price_max": 644740,
                    "limit": 6
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Desert Ridge Premium - Client 5",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Premium Area Update",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/riveroaks_premium_c5.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "Discuss premium options",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                }
            }
        ],
        "outputs": [
                "Snapshot saved and verified; campaign/email verified; follow-up hold scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_067",
        "instruction": "Coordinate the delivery of a Central City two-bed single-family briefing for client 3 under broker 1. Final outcome: a draft comp report document is available for subject property ID 'DT_SF2B2B_C3_AUG25' and is accessible; one client update is connected to a campaign titled 'Aug 2025 Central City Fit - Client 3' with subject 'Central City Options' using body URI 'https://storage.example.com/emails/dt_fit_c3.html' and the likely-buyer template; and two calendar holds are set for 2025-08-24: 10:30-10:50Z 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:20-13:40Z 'Post-tour buffer' at 'Phone' (source 'follow_up'). Confirm this by reviewing the comp report, the campaign, the client\u2019s email log, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 3,
                    "subject_property_id": "DT_SF2B2B_C3_AUG25",
                    "created_by_broker_id": 1,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Central City Fit - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Central City Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/dt_fit_c3.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T10:30:00Z",
                    "end_at": "2025-08-24T10:50:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Post-tour buffer",
                    "start_at": "2025-08-24T13:20:00Z",
                    "end_at": "2025-08-24T13:40:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 3
                }
            }
        ],
        "outputs": [
                "Comp report saved and verified; campaign/email present; viewing and buffer holds scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_068",
        "instruction": "Complete and dispatch a comps report for client 13 with broker 5. Final outcome: a comp report for 'HTX025' is recorded as 'draft' and checked; status is updated to 'sent_to_client' and verified; a 'general_update' campaign titled 'Aug 2025 Comps Final \u2014 Client 13' exists for one email with subject 'Your Comps Report' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/comps_final_c13.html'; a debrief hold is scheduled for 2025-08-26 09:00\u201309:20Z named 'Comps debrief' at 'USNV Strickland, FPO AP 98640' (source 'client_meeting'). Confirm by reviewing.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 13,
                    "subject_property_id": "HTX025",
                    "created_by_broker_id": 5,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Comps Final — Client 13",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "Your Comps Report",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/comps_final_c13.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 13,
                    "title": "Comps debrief",
                    "start_at": "2025-08-26T09:00:00Z",
                    "end_at": "2025-08-26T09:20:00Z",
                    "location": "USNV Strickland, FPO AP 98640",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 13
                }
            }
        ],
        "outputs": [
                "CMA 9 saved/sent; campaign/email verified; debrief created."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_069",
        "instruction": "Organize an evening Uptown route for client 9 under broker 2. The final outcome should be a route dated 2025-08-24 with sequenced stops ['HTX021','HTX025','HTX030'] and the map 'https://maps.google.com/route/midtown_evening_c9_20250824' saved and examined; hops remain within \u226430 minutes; a 'likely_buyer' campaign titled 'Aug 2025 Uptown Evening \u2014 Client 9' should be available and utilized for one email with the subject 'Evening Route \u2014 Uptown' (template_code 'likely_buyer') including the map URL as body_uri; a pre-drive sync hold from 09:30\u201309:45Z at 'Phone' (source 'follow_up') should be set; the audit 'routes_shared_and_viewings_set' must be submitted and the route reviewed.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX021",
                        "HTX025",
                        "HTX030"
                    ],
                    "map_url": "https://maps.google.com/route/midtown_evening_c9_20250824",
                    "created_by_broker_id": 2
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX021",
                        "HTX025",
                        "HTX030"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Uptown Evening — Client 9",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Evening Route — Uptown",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/midtown_evening_c9_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 9,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:30:00Z",
                    "end_at": "2025-08-24T09:45:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 2,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                }
            }
        ],
        "outputs": [
                "Route 11 feasible; campaign/email/hold verified; audit posted & route re-read."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_070",
        "instruction": "Dispatch a first-time buyer education pack to client 17 under broker 10. The intended state: calculate a mortgage estimate at list_price 450000 within region 'AZ' (term_years 30) for context; ensure a 'likely_buyer' campaign called 'Aug 2025 First-Time Buyer \u2014 Client 17' is available and applied for an email with the subject 'First-Time Buyer Guide' (template_code 'likely_buyer') and body_uri 'https://storage.example.com/emails/ftb_guide_c17.html'; schedule a consult hold on 2025-08-22 from 22:00\u201322:30Z labeled 'Financing consult (SF)' at 'Video \u2014 Zoom' (source 'follow_up'). Confirm with reading.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 17,
                    "list_price": 450000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 First-Time Buyer — Client 17",
                    "type": "likely_buyer",
                    "created_by": 10
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "First-Time Buyer Guide",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/ftb_guide_c17.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 10,
                    "client_id": 17,
                    "title": "Financing consult (SF)",
                    "start_at": "2025-08-22T22:00:00Z",
                    "end_at": "2025-08-22T22:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 17
                }
            }
        ],
        "outputs": [
                "Education email recorded; consult slot verified; campaign 9 ok."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_071",
        "instruction": "Coordinate a Saturday multi-stop tour for client 9 represented by broker 6. End state: ensure a route dated 2025-08-23 is created for client 9 with stops ordered as ['HTX221','HTX187','HTX204'] and the exact map link 'https://maps.example.com/route/c9_aug23' is stored; the route should be comprehensible; verify the drive-time feasibility with a maximum of 25 minutes between stops; ensure a campaign titled 'Aug 2025 Saturday Tour \u2014 Client 9' is set up to dispatch one email featuring the subject 'Tour Map & Plan' (template 'general_update') and body URI 'https://storage.example.com/emails/tour_plan_c9.html'; and arrange for a kickoff viewing hold on 2025-08-23 from 09:20Z to 09:40Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') to appear on the calendar. Confirm through the route details, the drive-time verification, the campaign/email, and the calendar.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 9,
                    "date": "2025-08-23",
                    "stops_ordered_json": [
                        "HTX221",
                        "HTX187",
                        "HTX204"
                    ],
                    "map_url": "https://maps.example.com/route/c9_aug23",
                    "created_by_broker_id": 6
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX221",
                        "HTX187",
                        "HTX204"
                    ],
                    "max_minutes": 25
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Saturday Tour — Client 9",
                    "type": "general_update",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 6,
                    "subject": "Tour Map & Plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/tour_plan_c9.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 9,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-23T09:20:00Z",
                    "end_at": "2025-08-23T09:40:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 9
                }
            }
        ],
        "outputs": [
                "Route stored and verified; drive-time OK; campaign/email present; kickoff hold scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_072",
        "instruction": "Organize a Desert Ridge luxury route for client 18 in collaboration with broker 5. End state: confirm that a route dated 2025-08-24 with stops ['HTX018','HTX032','HTX025'] and the map 'https://maps.google.com/route/riveroaks_lux_c18_20250824' is recorded and understandable; check that hop feasibility is \u226430 minutes; a campaign labeled 'likely_buyer' named 'Aug 2025 Desert Ridge Luxury \u2014 Client 18' is operational for sending an email including the subject 'Luxury Viewing Route' (template_code 'likely_buyer') and the map URL as body_uri; arrange a 'Pre-drive sync' hold from 11:10-11:20Z at 'Phone' (source 'follow_up'). Confirm through reads.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 18,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX018",
                        "HTX032",
                        "HTX025"
                    ],
                    "map_url": "https://maps.google.com/route/riveroaks_lux_c18_20250824",
                    "created_by_broker_id": 5
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX018",
                        "HTX032",
                        "HTX025"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Desert Ridge Luxury — Client 18",
                    "type": "likely_buyer",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Luxury Viewing Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/riveroaks_lux_c18_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T11:10:00Z",
                    "end_at": "2025-08-24T11:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 18
                }
            }
        ],
        "outputs": [
                "Route/email/hold verified; campaign 9 ok."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_073",
        "instruction": "Handle the sending of a price-alert follow-up for client 13 under broker 5. End state: recent sales for 'HTX043' (limit 3) are checked (context); a 'general_update' campaign titled 'Aug 2025 Price Alert Follow-Up \u2014 Client 13' is created and utilized for an email with subject 'Price Move & Local Sales' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/price_move_sales_c13.html'; a 2025-08-23 10:00\u201310:20Z 'Price-move debrief' appointment is scheduled at 'USNV Strickland, FPO AP 98640' (source 'client_meeting'). Validate through reads.",
        "actions": [
            {
                "name": "FetchRecentSalesByProperty",
                "arguments": {
                    "property_id": "HTX043",
                    "limit": 3
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Price Alert Follow-Up — Client 13",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "Price Move & Local Sales",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/price_move_sales_c13.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 13,
                    "title": "Price-move debrief",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:20:00Z",
                    "location": "USNV Strickland, FPO AP 98640",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 13
                }
            }
        ],
        "outputs": [
                "Sales context used; campaign/email verified; debrief set."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_074",
        "instruction": "Coordinate a Uptown vs Central City comparison for client 2 under broker 3. End state: two draft comp report documents are generated and accessible\u2014'MID_VS_DT_AUG25_A' reflecting Uptown+Central City context and 'MID_VS_DT_AUG25_B' representing Central City-only; a single client update is linked to a campaign titled 'Aug 2025 Uptown vs Central City - Client 2' with the subject 'Uptown vs Central City' using body URI 'https://storage.example.com/emails/mid_vs_dt_c2.html' and the general-update template; and a Zoom discussion dated 2025-08-24 from 16:30Z to 17:00Z titled 'Compare neighborhoods' (source 'follow_up') is recorded on the calendar. Confirm by reading both comp reports and accessing the campaign, the client\u2019s email log, and the calendar entry.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "MID_VS_DT_AUG25_A",
                    "created_by_broker_id": 3,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "MID_VS_DT_AUG25_B",
                    "created_by_broker_id": 3,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 10
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Uptown vs Central City - Client 2",
                    "type": "general_update",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Uptown vs Central City",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/mid_vs_dt_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Compare neighborhoods",
                    "start_at": "2025-08-24T16:30:00Z",
                    "end_at": "2025-08-24T17:00:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Both comp reports saved and verified; campaign/email verified; Zoom hold scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_075",
        "instruction": "Handle sending a Heights historic shortlist for client 15 under broker 8. End state: a draft comp report document for subject property ID 'HGTS_HIST_C15_AUG25' is available and readable; an outbound update is included in a campaign titled 'Aug 2025 Heights Historic - Client 15' with subject 'Heights Historic Picks' using body URI 'https://storage.example.com/emails/heights_historic_c15.html' and the general-update template; and a viewing-plan hold on 2025-08-30 from 14:00Z to 14:20Z titled 'Heights tour plan' at '1234 Heights Boulevard, Phoenix, AZ 77008' (source 'viewing') is present on the calendar. Verify by checking the comp report, the campaign record, the client\u2019s email log, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 15,
                    "subject_property_id": "HGTS_HIST_C15_AUG25",
                    "created_by_broker_id": 8,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Heights Historic - Client 15",
                    "type": "general_update",
                    "created_by": 8
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Heights Historic Picks",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/heights_historic_c15.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 15
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Heights tour plan",
                    "start_at": "2025-08-30T14:00:00Z",
                    "end_at": "2025-08-30T14:20:00Z",
                    "location": "1234 Heights Boulevard, Phoenix, AZ 77008",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 15
                }
            }
        ],
        "outputs": [
                "Comp report saved and verified; campaign/email verified; viewing plan scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_076",
        "instruction": "Coordinate the sharing of a Arts Quarter vs SoDo townhouse comparison for client 12 under broker 3. End state: a documented snapshot for subject property ID 'MD_VS_EADO_TH_C12_AUG25' is available in draft status and is readable; alongside the update, a quick finance estimate with a target price of 530000 over 30 years in region AZ is provided; an associated client message is connected to a campaign titled 'Aug 2025 Museum vs SoDo - Client 12' with subject 'Townhouse Compare: Museum vs SoDo' using body URI 'https://storage.example.com/emails/museum_vs_eado_c12.html' and the likely-buyer template; and a viewing hold on 2025-08-25 from 14:00Z to 14:20Z titled 'Compare plan' at '3030 Caroline Street, Phoenix, AZ 77004' (source 'viewing') is visible on the calendar. Verify by reviewing the saved snapshot, retrieving the campaign and email records, checking the calendar entry, and confirming the finance estimate.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 12,
                    "subject_property_id": "MD_VS_EADO_TH_C12_AUG25",
                    "created_by_broker_id": 3,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 12,
                    "list_price": 530000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Museum vs SoDo - Client 12",
                    "type": "likely_buyer",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Compare: Museum vs SoDo",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/museum_vs_eado_c12.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Compare plan",
                    "start_at": "2025-08-25T14:00:00Z",
                    "end_at": "2025-08-25T14:20:00Z",
                    "location": "3030 Caroline Street, Phoenix, AZ 77004",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 12
                }
            }
        ],
        "outputs": [
                "Snapshot saved and verified; finance estimate returned; campaign/email verified; viewing hold scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_077",
        "instruction": "Handle the delivery of a loan-sizing snapshot for client 10 in collaboration with broker 11. Final state: determine a mortgage estimate at list_price 600000 (region 'AZ', term_years 30) for context; a 'general_update' campaign titled 'Aug 2025 Loan Sizing \u2014 Client 10' is in place; ensure one email to client 10 with the subject 'Loan Sizing Snapshot' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/loan_sizing_c10.html' is documented; record a 2025-08-23 13:20\u201313:40Z 'Sizing consult' hold via 'Phone' (source 'follow_up'). Confirm through reads.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 10,
                    "list_price": 600000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Loan Sizing — Client 10",
                    "type": "general_update",
                    "created_by": 11
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Loan Sizing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/loan_sizing_c10.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 11,
                    "client_id": 10,
                    "title": "Sizing consult",
                    "start_at": "2025-08-23T13:20:00Z",
                    "end_at": "2025-08-23T13:40:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 10
                }
            }
        ],
        "outputs": [
                "Loan estimate + campaign/email verified; consult set."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_078",
        "instruction": "Coordinate a micro-tour arrangement for client 7 with the involvement of broker 15. Final state: secure and read a route for 2025-08-28 with stops ['HTX036','HTX035'] and map 'https://maps.google.com/route/eado_microtour_c7_20250828'; hops do not exceed 30 minutes; a 'likely_buyer' campaign titled 'Aug 2025 SoDo Micro-Tour \u2014 Client 7' is established and supports one email with the subject 'Micro-Tour Plan' (template_code 'likely_buyer') and body_uri 'https://maps.google.com/route/eado_microtour_c7_20250828'; log a 16:00\u201317:00Z 'Contract Review - Mr. Sean Hardy' hold at '5033 Parker Keys Suite 325, Old Williamsburg, VT 03979' (source 'client_meeting'). Confirm through reads.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 7,
                    "date": "2025-08-28",
                    "stops_ordered_json": [
                        "HTX036",
                        "HTX035"
                    ],
                    "map_url": "https://maps.google.com/route/eado_microtour_c7_20250828",
                    "created_by_broker_id": 15
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX036",
                        "HTX035"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 SoDo Micro-Tour — Client 7",
                    "type": "likely_buyer",
                    "created_by": 15
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 15,
                    "subject": "Micro-Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/eado_microtour_c7_20250828",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 15,
                    "client_id": 7,
                    "title": "Contract Review - Mr. Sean Hardy",
                    "start_at": "2025-08-28T16:00:00Z",
                    "end_at": "2025-08-28T17:00:00Z",
                    "location": "5033 Parker Keys Suite 325, Old Williamsburg, VT 03979",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 7
                }
            }
        ],
        "outputs": [
                "Route/email/meeting present; campaign verified."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_079",
        "instruction": "Handle a Uptown condo briefing for client 2 under broker 14. End state: a draft comp report document is created for subject property ID 'MDTN_CONDO_C2_AUG25' and remains readable; one client update is linked with a campaign titled 'Aug 2025 Uptown Condos - Client 2' utilizing the subject 'Uptown Condo Picks' and body URI 'https://storage.example.com/emails/midtown_condos_c2.html' with the general-update template; and a debrief scheduled for 2025-08-27 from 18:00Z to 18:20Z titled 'Uptown options debrief' at 'Office' (source 'follow_up') is seen on the calendar. Verify by reviewing the comp report and retrieving the campaign record, the client\u2019s email log, and the calendar entry.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "MDTN_CONDO_C2_AUG25",
                    "created_by_broker_id": 14,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Uptown Condos - Client 2",
                    "type": "general_update",
                    "created_by": 14
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Uptown Condo Picks",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/midtown_condos_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Uptown options debrief",
                    "start_at": "2025-08-27T18:00:00Z",
                    "end_at": "2025-08-27T18:20:00Z",
                    "location": "Office",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Comp report saved and verified; campaign/email present; debrief scheduled and confirmed."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_080",
        "instruction": "Coordinate a Central City luxury finance & route confirmation for client 9 under broker 9. End state: calculate a mortgage estimate for client 9 at list_price 750000 (term_years 30, region 'AZ') as context; a route dated 2025-08-24 with stops ['HTX036','HTX032','HTX049'] and map 'https://maps.google.com/route/dt_lux_finance_c9_20250824' is saved/read and complies with a \u226430-minute hop check; a 'general_update' campaign called 'Aug 2025 DT Luxury Finance \u2014 Client 9' exists and is used for sending two emails under that campaign: one to client 9 with subject 'Luxury Finance Snapshot' (template_code 'general_update') and body_uri 'https://storage.example.com/emails/dt_lux_finance_c9.html', and another to client 9 with subject 'Route Confirm \u2014 2025-08-24' (template_code 'general_update') employing the map URL as body_uri; log audit 'routes_shared_and_viewings_set' on the route and review the route again. Verify with readings.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 9,
                    "list_price": 750000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": [
                        "HTX036",
                        "HTX032",
                        "HTX049"
                    ],
                    "map_url": "https://maps.google.com/route/dt_lux_finance_c9_20250824",
                    "created_by_broker_id": 9
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX036",
                        "HTX032",
                        "HTX049"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 DT Luxury Finance — Client 9",
                    "type": "general_update",
                    "created_by": 9
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Luxury Finance Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/dt_lux_finance_c9.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Route Confirm — 2025-08-24",
                    "template_code": "general_update",
                    "body_uri": "https://maps.google.com/route/dt_lux_finance_c9_20250824",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 9
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 9,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                }
            }
        ],
        "outputs": [
                "Finance+route context present; two emails filed; audit posted; route re-read and feasible."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_081",
        "instruction": "Handle the assembly of a Arcadia first\u2011time buyer briefing for client 7 under broker 5. Final state: a briefing document (version 'aug25') is produced and linked in one email within a campaign named 'Aug 2025 Buyer Brief \u2014 Client 7' with the subject 'Your Buyer Brief' (template 'general_update') and body URI 'https://storage.example.com/briefings/client_briefing_007_aug25.pdf'; also, a follow\u2011up phone hold on 2025-08-24 from 17:10Z to 17:30Z titled 'Brief Q&A' (source 'follow_up') shows up on the calendar. Confirm by reviewing the campaign, the client\u2019s email log, and the calendar.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 5,
                    "version_tag": "aug25"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Buyer Brief — Client 7",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 7,
                    "broker_id": 5,
                    "subject": "Your Buyer Brief",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_007_aug25.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 7
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 7,
                    "title": "Brief Q&A",
                    "start_at": "2025-08-24T17:10:00Z",
                    "end_at": "2025-08-24T17:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 7
                }
            }
        ],
        "outputs": [
                "Briefing referenced in email; campaign verified; follow-up scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_082",
        "instruction": "Coordinate the assembly of a financing\u2011ready update for client 18 under broker 6 targeting a price of 720000. Final state: a 30\u2011year AZ mortgage estimate is calculated; a comp report titled 'BRAESWOOD_TARGET_C18_AUG25' is saved in draft and accessible; a campaign named 'Aug 2025 Financing + CMA \u2014 Client 18' is set up and used to distribute an email with the subject 'Financing & CMA' (template 'likely_buyer') and body URI 'https://storage.example.com/emails/financing_cma_c18.html'; and a client meeting on 2025-08-25 from 16:00Z to 16:30Z titled 'Financing plan' at 'Office' (source 'client_meeting') is noted on the calendar. Verify through the comp report read, the campaign/email, and the calendar.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 18,
                    "list_price": 720000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 18,
                    "subject_property_id": "BRAESWOOD_TARGET_C18_AUG25",
                    "created_by_broker_id": 6,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Financing + CMA — Client 18",
                    "type": "likely_buyer",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 6,
                    "subject": "Financing & CMA",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/financing_cma_c18.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 18,
                    "title": "Financing plan",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:30:00Z",
                    "location": "Office",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 18
                }
            }
        ],
        "outputs": [
                "Estimate computed; draft CMA saved; campaign/email verified; consult scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_083",
        "instruction": "Handle the completion of a weekend open-house plan for client 12 under broker 3 utilizing properties ['HTX310','HTX318'] for 2025-08-23 to 2025-08-24. Finalize the window set review; ensure a campaign titled 'Aug 2025 Open-House Weekend \u2014 Client 12' is available and employed to transmit a single email with subject 'Your Open House Plan' (template 'general_update') and body URI 'https://storage.example.com/emails/openhouse_plan_c12.html'; and ensure an 'Open-house kickoff' hold on 2025-08-23 from 10:00Z to 10:20Z at 'Client Home' (source 'viewing') is visible on the calendar. Verify accuracy through the campaign/email and the calendar.",
        "actions": [
            {
                "name": "FetchOpenHousesByProperties",
                "arguments": {
                    "property_ids": [
                        "HTX310",
                        "HTX318"
                    ],
                    "date_from": "2025-08-23",
                    "date_to": "2025-08-24"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Open‑House Weekend — Client 12",
                    "type": "general_update",
                    "created_by": 3
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Your Open House Plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/openhouse_plan_c12.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 12
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Open-house kickoff",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:20:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 12
                }
            }
        ],
        "outputs": [
                "Open-house plan shared; campaign/email verified; kickoff scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_084",
        "instruction": "Coordinate seller-broker outreach for client 5 under broker 5, encompassing properties ['HTX201','HTX205','HTX207']. Ensure an outreach drafts bundle is prepared; confirm the existence of a campaign titled 'Aug 2025 Seller Outreach \u2014 Client 5', which dispatches one email with the subject 'Seller Outreach Drafts' (template 'general_update') and body URI 'https://storage.example.com/drafts/client_5_props_3.pdf'; and make sure a follow-up hold on 2025-08-22 from 21:10Z to 21:30Z named 'Review outreach drafts' at 'Phone' (source 'follow_up') is present on the calendar. Validate through the campaign record, email log, and calendar.",
        "actions": [
            {
                "name": "DraftSellerBrokerEmails",
                "arguments": {
                    "client_id": 5,
                    "property_ids": [
                        "HTX201",
                        "HTX205",
                        "HTX207"
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Seller Outreach — Client 5",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Seller Outreach Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/drafts/client_5_props_3.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "Review outreach drafts",
                    "start_at": "2025-08-22T21:10:00Z",
                    "end_at": "2025-08-22T21:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                }
            }
        ],
        "outputs": [
                "Drafts bundle referenced in email; campaign verified; follow-up logged."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_085",
        "instruction": "Handle the delivery of two contrast CMAs for client 22 managed by broker 9. Final outcome: Two draft comp reports should be present and accessible\u2014titles 'RICE_MIL_C22_AUG25_A' and 'MIDTOWN_C22_AUG25_B'; there should be an existing campaign named 'Aug 2025 Two-CMA Contrast \u2014 Client 22' which is utilized to dispatch one email with the subject 'Two CMA Snapshots' (template 'general_update') and the body link 'https://storage.example.com/emails/two_cma_c22.html'. Additionally, ensure a follow-up Zoom meeting on 2025-08-26 from 11:30Z to 11:50Z titled 'CMA contrast debrief' (source 'follow_up') is scheduled in the calendar. Confirm by checking both comp report reads, the campaign/email, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 22,
                    "subject_property_id": "RICE_MIL_C22_AUG25_A",
                    "created_by_broker_id": 9,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 22,
                    "subject_property_id": "MIDTOWN_C22_AUG25_B",
                    "created_by_broker_id": 9,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 10
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Two‑CMA Contrast — Client 22",
                    "type": "general_update",
                    "created_by": 9
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 22,
                    "broker_id": 9,
                    "subject": "Two CMA Snapshots",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/two_cma_c22.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 22
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 22,
                    "title": "CMA contrast debrief",
                    "start_at": "2025-08-26T11:30:00Z",
                    "end_at": "2025-08-26T11:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 22
                }
            }
        ],
        "outputs": [
                "Both CMAs saved; campaign/email verified; debrief scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_086",
        "instruction": "Coordinate a neighborhood open-house sweep for client 20 guided by broker 7 across neighborhoods [11,6,13] during the 2025-08-23 weekend. Final outcome: neighborhood open-house windows should be evaluated; a campaign titled 'Aug 2025 Open House Sweep \u2014 Client 20' should exist and send out one email 'Open House Sweep' (template 'general_update') with the body link 'https://storage.example.com/emails/oh_sweep_c20.html'. Also, ensure a buffer hold on 2025-08-24 from 12:40Z to 13:00Z titled 'Open House Sweep Q&A' at 'Cafe \u2014 Arcadia' (source 'follow_up') is present in the calendar. Verify through the campaign/email and the calendar.",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        11,
                        6,
                        13
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Open House Sweep — Client 20",
                    "type": "general_update",
                    "created_by": 7
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 20,
                    "broker_id": 7,
                    "subject": "Open House Sweep",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/oh_sweep_c20.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 20
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Open House Sweep Q&A",
                    "start_at": "2025-08-24T12:40:00Z",
                    "end_at": "2025-08-24T13:00:00Z",
                    "location": "Cafe — Arcadia",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 20
                }
            }
        ],
        "outputs": [
                "Neighborhood windows reviewed; campaign/email sent; buffer hold set."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_087",
        "instruction": "Handle the delivery of an inspection recap to client 14 under broker 5. End state: generate and reference a briefing document (version 'inspection_aug25'); ensure that a campaign titled 'Aug 2025 Inspection Delivered \u2014 Client 14' is created, which dispatches one email with the subject 'Inspection Report' (template 'general_update'), using the briefing URI as the body; and make sure a follow-up phone hold on 2025-08-22 from 19:15Z to 19:35Z titled 'Inspection Q&A' (source 'follow_up') appears on the calendar. Confirm through campaign read, email log, and calendar.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 5,
                    "version_tag": "inspection_aug25"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Inspection Delivered — Client 14",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "Inspection Report",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_014_inspection_aug25.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 14
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "Inspection Q&A",
                    "start_at": "2025-08-22T19:15:00Z",
                    "end_at": "2025-08-22T19:35:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 14
                }
            }
        ],
        "outputs": [
                "Briefing generated and referenced; campaign/email verified; Q&A scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_088",
        "instruction": "Coordinate a Sugar Land tour for client 11 under broker 6 on 2025\u201108\u201125. End state: establish a route for client 11 with the specified ordered stops ['SL_501','SL_512','SL_498'] and store the map link 'https://maps.example.com/route/c11_aug25' verbatim; ensure the route is readable; confirm the drive-time feasibility with a maximum of 25 minutes between stops; verify the creation of a campaign titled 'Aug 2025 Sugar Land Tour \u2014 Client 11' that sends one email 'Your Sugar Land Tour' (template 'general_update') utilizing 'https://storage.example.com/emails/sl_tour_c11.html'; and schedule a pre-tour client meeting on 2025-08-25 from 08:30Z to 08:50Z titled 'Pre-tour brief' at 'Video \u2014 Zoom' to appear on the calendar. Validate through route details, drive-time check, campaign/email, and calendar.",
        "actions": [
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 11,
                    "date": "2025-08-25",
                    "stops_ordered_json": [
                        "SL_501",
                        "SL_512",
                        "SL_498"
                    ],
                    "map_url": "https://maps.example.com/route/c11_aug25",
                    "created_by_broker_id": 6
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "SL_501",
                        "SL_512",
                        "SL_498"
                    ],
                    "max_minutes": 25
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Sugar Land Tour — Client 11",
                    "type": "general_update",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Your Sugar Land Tour",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/sl_tour_c11.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 11
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Pre-tour brief",
                    "start_at": "2025-08-25T08:30:00Z",
                    "end_at": "2025-08-25T08:50:00Z",
                    "location": "Video — Zoom",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 11
                }
            }
        ],
        "outputs": [
                "Route verified; drive-time OK; campaign/email present; pre-tour hold set."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_089",
        "instruction": "Handle the sending of a Uptown CMA snapshot for client 2 under broker 14. Desired outcome: a draft comp report is available and can be read for subject 'MDTN_CMA_C2_AUG25'; a campaign entitled 'Aug 2025 Uptown CMA \u2014 Client 2' is present and dispatches an email with subject 'Uptown CMA Snapshot' (template 'likely_buyer') and body URI 'https://storage.example.com/emails/midtown_cma_c2.html'; and a follow-up phone hold on 2025-08-23 from 18:20Z to 18:40Z named 'CMA debrief' (source 'follow_up') is listed on the calendar. Confirm through the comp report read, the campaign/email, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 2,
                    "subject_property_id": "MDTN_CMA_C2_AUG25",
                    "created_by_broker_id": 14,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Uptown CMA — Client 2",
                    "type": "likely_buyer",
                    "created_by": 14
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Uptown CMA Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/midtown_cma_c2.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 2
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "CMA debrief",
                    "start_at": "2025-08-23T18:20:00Z",
                    "end_at": "2025-08-23T18:40:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 2
                }
            }
        ],
        "outputs": [
                "Draft CMA saved; campaign/email verified; debrief set."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_090",
        "instruction": "Coordinate the presentation of financing scenarios for client 10 under broker 4 at two target prices: 650000 and 820000 (30-year AZ). Intended result: both calculations are completed; a campaign called 'Aug 2025 Financing Scenarios \u2014 Client 10' is set up and dispatches an email with subject 'Two Financing Scenarios' (template 'general_update') and body URI 'https://storage.example.com/emails/finance_scenarios_c10.html'; and a client-meeting hold on 2025-08-25 from 20:10Z to 20:40Z titled 'Financing consult' at 'Video \u2014 Zoom' (source 'client_meeting') is scheduled on the calendar. Verify via the campaign/email and the calendar.",
        "actions": [
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 10,
                    "list_price": 650000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 10,
                    "list_price": 820000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Financing Scenarios — Client 10",
                    "type": "general_update",
                    "created_by": 4
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Two Financing Scenarios",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/finance_scenarios_c10.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 10
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 4,
                    "client_id": 10,
                    "title": "Financing consult",
                    "start_at": "2025-08-25T20:10:00Z",
                    "end_at": "2025-08-25T20:40:00Z",
                    "location": "Video — Zoom",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 10
                }
            }
        ],
        "outputs": [
                "Scenarios computed; campaign/email verified; consult scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_091",
        "instruction": "Handle the preparation and dispatch of a Heights CMA to client 5, working under broker 5. End state: ensure that a draft comp report for subject 'HEIGHTS_HTX012_C5_AUG25' is stored and viewable, subsequently updating it to 'sent_to_client' and re-reading it; ensure the existence of a campaign named 'Aug 2025 Heights Listing CMA \u2014 Client 5' that sends an email with subject 'CMA for HTX012' (template 'general_update') and body URI 'https://storage.example.com/emails/cma_htx012_c5.html'; and ensure a follow-up scheduled on 2025-08-24 from 15:00Z to 15:20Z titled 'CMA questions' at 'Phone' (source 'follow_up') is noted on the calendar. Confirm through the comp report, the campaign/email, and the calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 5,
                    "subject_property_id": "HEIGHTS_HTX012_C5_AUG25",
                    "created_by_broker_id": 5,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "UpdateCompReportStatus",
                "arguments": {
                    "report_id": 9,
                    "status": "sent_to_client"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Heights Listing CMA — Client 5",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "CMA for HTX012",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/cma_htx012_c5.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "CMA questions",
                    "start_at": "2025-08-24T15:00:00Z",
                    "end_at": "2025-08-24T15:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                }
            }
        ],
        "outputs": [
                "CMA saved then sent; campaign/email verified; follow‑up scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_092",
        "instruction": "Coordinate the creation of a 3-bed Uptown/Galleria shortlist for client 22 operating under broker 9. End state: confirm that a draft comp report is available and accessible for subject 'UPTOWN_3BEDS_C22_AUG25'; ensure the presence of a campaign called 'Aug 2025 3-Bed Uptown \u2014 Client 22' which sends one email with subject '3-Bed Options' (template 'likely_buyer') and body URI 'https://storage.example.com/emails/three_bed_uptown_c22.html'; and make sure a viewing kickoff on 2025-08-27 from 12:10Z to 12:40Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') is entered on the calendar. Validate through comp report read, campaign/email, and calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 22,
                    "subject_property_id": "UPTOWN_3BEDS_C22_AUG25",
                    "created_by_broker_id": 9,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 3‑Bed Uptown — Client 22",
                    "type": "likely_buyer",
                    "created_by": 9
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 22,
                    "broker_id": 9,
                    "subject": "3‑Bed Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/three_bed_uptown_c22.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 22
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 9,
                    "client_id": 22,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-27T12:10:00Z",
                    "end_at": "2025-08-27T12:40:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 22
                }
            }
        ],
        "outputs": [
                "Draft shortlist CMA saved; campaign/email verified; kickoff scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_093",
        "instruction": "Handle the preparation of a financing brief for client 18 under broker 6. End state: the client\u2019s mortgage profile gets verified; a 30\u2011year AZ estimate is calculated for list price 540000; a briefing document (version 'aug25') is compiled and linked in one email under a campaign titled 'Aug 2025 Financing Brief \u2014 Client 18' with subject 'Your Financing Brief' (template 'general_update') and body URI 'https://storage.example.com/briefings/client_briefing_018_aug25.pdf'; and a follow\u2011up phone hold on 2025-08-24 from 19:00Z to 19:20Z titled 'Financing Q&A' (source 'follow_up') is set on the calendar. Confirm via the campaign/email and calendar.",
        "actions": [
            {
                "name": "GetMortgageProfile",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 18,
                    "list_price": 540000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 6,
                    "version_tag": "aug25"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Financing Brief — Client 18",
                    "type": "general_update",
                    "created_by": 6
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 18,
                    "broker_id": 6,
                    "subject": "Your Financing Brief",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_018_aug25.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 18
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 6,
                    "client_id": 18,
                    "title": "Financing Q&A",
                    "start_at": "2025-08-24T19:00:00Z",
                    "end_at": "2025-08-24T19:20:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 18
                }
            }
        ],
        "outputs": [
                "Profile checked; estimate computed; briefing mailed; Q&A scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_094",
        "instruction": "Coordinate an Inner Loop viewing day for client 16 under broker 8. End state: open\u2011house windows for neighborhoods [7,11,6] are evaluated; a three\u2011stop route dated 2025-08-31 is organized for client 16 with stops ['HTX716','HTX722','HTX731'] and map link 'https://maps.example.com/route/c16_aug31' retained precisely; the route is clear; drive\u2011time feasibility is validated with a 30\u2011minute limit; a campaign titled 'Aug 2025 Viewing Day \u2014 Client 16' is available and dispatches one email 'Route & Open House Plan' (template 'general_update') using 'https://storage.example.com/emails/viewing_day_c16.html'; and a kickoff viewing hold on 2025-08-31 from 09:15Z to 09:35Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') is scheduled on the calendar. Validate via route specifics, drive\u2011time verification, campaign/email, and calendar.",
        "actions": [
            {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "arguments": {
                    "neighborhood_ids": [
                        7,
                        11,
                        6
                    ]
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 16,
                    "date": "2025-08-31",
                    "stops_ordered_json": [
                        "HTX716",
                        "HTX722",
                        "HTX731"
                    ],
                    "map_url": "https://maps.example.com/route/c16_aug31",
                    "created_by_broker_id": 8
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX716",
                        "HTX722",
                        "HTX731"
                    ],
                    "max_minutes": 30
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Viewing Day — Client 16",
                    "type": "general_update",
                    "created_by": 8
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Route & Open House Plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/viewing_day_c16.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 16
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 8,
                    "client_id": 16,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-31T09:15:00Z",
                    "end_at": "2025-08-31T09:35:00Z",
                    "location": "Client Home",
                    "source": "viewing"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 16
                }
            }
        ],
        "outputs": [
                "Route stored; drive-time OK; campaign/email verified; kickoff scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_095",
        "instruction": "Handle the delivery of a Autumn Creek CMA for client 13 under broker 2, ensuring an audit trail. Desired outcome: a draft comp report labeled 'SPRBR_CMA_C13_AUG25' is stored and accessible; a campaign named 'Aug 2025 Autumn Creek CMA \u2014 Client 13' is active and sends out one email with the subject 'Your CMA' (template 'likely_buyer') and body link 'https://storage.example.com/emails/sprbr_cma_c13.html'; an audit event 'client_notified' is logged with the comp report and it is reviewed again; and a follow-up call is scheduled on 2025-08-26 from 18:10Z to 18:30Z titled 'CMA debrief' (source 'follow_up') on the calendar. Confirm through comp report reads, campaign/email, and calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 13,
                    "subject_property_id": "SPRBR_CMA_C13_AUG25",
                    "created_by_broker_id": 2,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Autumn Creek CMA — Client 13",
                    "type": "likely_buyer",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 13,
                    "broker_id": 2,
                    "subject": "Your CMA",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/sprbr_cma_c13.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 13
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 2,
                    "action": "client_notified",
                    "entity_type": "comp_reports",
                    "entity_id": 9
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 13,
                    "title": "CMA debrief",
                    "start_at": "2025-08-26T18:10:00Z",
                    "end_at": "2025-08-26T18:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 13
                }
            }
        ],
        "outputs": [
                "CMA saved; client notified; report re-read; debrief scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_096",
        "instruction": "Coordinate the distribution of seller disclosures to client 5 under broker 5. Desired result: a briefing document (version 'disclosures_aug25') is created and referenced; a campaign titled 'Aug 2025 Disclosures \u2014 Client 5' is set up and sends one email with subject 'Seller Disclosures' (template 'general_update') utilizing that briefing URI; and a follow-up phone call on 2025-08-23 from 12:10Z to 12:30Z titled 'Disclosure Q&A' at 'Phone' (source 'follow_up') is on the calendar. Validate through campaign review, email record, and calendar.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 5,
                    "version_tag": "disclosures_aug25"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Disclosures — Client 5",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Seller Disclosures",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_005_disclosures_aug25.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 5
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "Disclosure Q&A",
                    "start_at": "2025-08-23T12:10:00Z",
                    "end_at": "2025-08-23T12:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 5
                }
            }
        ],
        "outputs": [
                "Briefing generated; campaign verified; disclosures emailed; Q&A scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_097",
        "instruction": "Handle the preparation of a three-home seller outreach packet for client 8 under the supervision of broker 5. Final outcome: an outreach drafts bundle is established for ['HTX401','HTX402','HTX403']; a campaign labeled 'Aug 2025 Seller Inquiries \u2014 Client 8' is created and utilized to dispatch one email with the subject 'Owner Inquiry Drafts' (template 'general_update') and the body URI 'https://storage.example.com/drafts/client_8_props_3.pdf'; an audit event 'drafts_prepped' is logged on the campaign, and the campaign is reviewed again; and a follow-up phone hold scheduled for 2025-08-25 from 13:30Z to 13:50Z titled 'Seller outreach debrief' (source 'follow_up') appears in the calendar. Confirm via campaign readings, email log, and calendar entry.",
        "actions": [
            {
                "name": "DraftSellerBrokerEmails",
                "arguments": {
                    "client_id": 8,
                    "property_ids": [
                        "HTX401",
                        "HTX402",
                        "HTX403"
                    ]
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Seller Inquiries — Client 8",
                    "type": "general_update",
                    "created_by": 5
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 8,
                    "broker_id": 5,
                    "subject": "Owner Inquiry Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/drafts/client_8_props_3.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 8
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 5,
                    "action": "drafts_prepped",
                    "entity_type": "campaigns",
                    "entity_id": 9
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 5,
                    "client_id": 8,
                    "title": "Seller outreach debrief",
                    "start_at": "2025-08-25T13:30:00Z",
                    "end_at": "2025-08-25T13:50:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 8
                }
            }
        ],
        "outputs": [
                "Drafts referenced; campaign audited; debrief scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_098",
        "instruction": "Coordinate the setup of a Cypress commute test for client 6 with broker 2. Final outcome: drive-time feasibility is verified for ['HTX551','HTX562','HTX574'] within a 25-minute limit; a route dated 2025-08-27 is established for these stops with a map link 'https://maps.example.com/route/c6_aug27' stored verbatim and accessible; a campaign named 'Aug 2025 Commute Test \u2014 Client 6' exists and issues one email 'Commute Test Plan' (template 'general_update') utilizing 'https://storage.example.com/emails/commute_test_c6.html'; and a pre-commute client-meeting call on 2025-08-27 from 07:40Z to 08:00Z titled 'Pre-commute check-CO' at 'Phone' (source 'client_meeting') is listed in the calendar. Confirm via the drive-time verification, route information, campaign/email, and calendar.",
        "actions": [
            {
                "name": "CheckDriveTimeConstraints",
                "arguments": {
                    "property_ids": [
                        "HTX551",
                        "HTX562",
                        "HTX574"
                    ],
                    "max_minutes": 25
                },
            },
            {
                "name": "BuildRoute",
                "arguments": {
                    "client_id": 6,
                    "date": "2025-08-27",
                    "stops_ordered_json": [
                        "HTX551",
                        "HTX562",
                        "HTX574"
                    ],
                    "map_url": "https://maps.example.com/route/c6_aug27",
                    "created_by_broker_id": 2
                },
            },
            {
                "name": "GetRouteDetails",
                "arguments": {
                    "route_id": 11
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Commute Test — Client 6",
                    "type": "general_update",
                    "created_by": 2
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Commute Test Plan",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/emails/commute_test_c6.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 6
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Pre-commute check-CO",
                    "start_at": "2025-08-27T07:40:00Z",
                    "end_at": "2025-08-27T08:00:00Z",
                    "location": "Phone",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 6
                }
            }
        ],
        "outputs": [
                "Drive-time checked; route verified; campaign/email present; meeting scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_099",
        "instruction": "Handle sending a Garden Oaks CMA with financing for client 17 under broker 7. Desired outcome: a draft comp report is generated and accessible for subject 'GARDEN_OAKS_CMA_C17_AUG25'; a 30\u2011year AZ mortgage estimate should be calculated for list price 680000; create a campaign named 'Aug 2025 Garden Oaks CMA \u2014 Client 17', which sends an email with the subject 'CMA + Payment Estimate' (template 'likely_buyer') and body URI 'https://storage.example.com/emails/go_cma_finance_c17.html'; and schedule a Zoom CMA review on 2025-08-28 from 17:00Z to 17:30Z titled 'CMA review' at 'Video \u2014 Zoom' (source 'client_meeting') on the calendar. Confirm through comp report availability, campaign/email, and calendar.",
        "actions": [
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 17,
                    "subject_property_id": "GARDEN_OAKS_CMA_C17_AUG25",
                    "created_by_broker_id": 7,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "ComputeMortgageEstimate",
                "arguments": {
                    "client_id": 17,
                    "list_price": 680000,
                    "term_years": 30,
                    "region": "AZ"
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Garden Oaks CMA — Client 17",
                    "type": "likely_buyer",
                    "created_by": 7
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 17,
                    "broker_id": 7,
                    "subject": "CMA + Payment Estimate",
                    "template_code": "likely_buyer",
                    "body_uri": "https://storage.example.com/emails/go_cma_finance_c17.html",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 17
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 7,
                    "client_id": 17,
                    "title": "CMA review",
                    "start_at": "2025-08-28T17:00:00Z",
                    "end_at": "2025-08-28T17:30:00Z",
                    "location": "Video — Zoom",
                    "source": "client_meeting"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 17
                }
            }
        ],
        "outputs": [
                "CMA saved; estimate computed; campaign/email verified; review scheduled."
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "res_v3_100",
        "instruction": "Coordinate the delivery of a post\u2011tour recap for client 3 under broker 1. Required outcomes: generate a briefing document (version 'aug25') and include it in an email within a campaign titled 'Aug 2025 Tour Recap \u2014 Client 3' with the subject 'Tour Recap & Next Steps' (template 'general_update') and body URI 'https://storage.example.com/briefings/client_briefing_003_aug25.pdf'; ensure a draft comp report for 'TOUR_RECAP_C3_AUG25' is stored and accessible; log an audit event 'recap_sent' on that comp report and re\u2011review the report; and a follow\u2011up phone call scheduled on 2025-08-29 from 09:10Z to 09:30Z titled 'Recap call' (source 'follow_up') should appear on the calendar. Confirm by checking comp report availability, campaign/email, and calendar.",
        "actions": [
            {
                "name": "GenerateBriefingDoc",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "version_tag": "aug25"
                },
            },
            {
                "name": "SaveCompReport",
                "arguments": {
                    "client_id": 3,
                    "subject_property_id": "TOUR_RECAP_C3_AUG25",
                    "created_by_broker_id": 1,
                    "final_status": "draft"
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCampaign",
                "arguments": {
                    "name": "Aug 2025 Tour Recap — Client 3",
                    "type": "general_update",
                    "created_by": 1
                },
            },
            {
                "name": "GetCampaignDetails",
                "arguments": {
                    "campaign_id": 9
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Tour Recap & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://storage.example.com/briefings/client_briefing_003_aug25.pdf",
                    "campaign_id": 9
                },
            },
            {
                "name": "GetEmailsForClient",
                "arguments": {
                    "client_id": 3
                },
            },
            {
                "name": "PostAuditEvent",
                "arguments": {
                    "actor_id": 1,
                    "action": "recap_sent",
                    "entity_type": "comp_reports",
                    "entity_id": 9
                },
            },
            {
                "name": "GetCompReportDetails",
                "arguments": {
                    "report_id": 9
                },
            },
            {
                "name": "CreateCalendarEvent",
                "arguments": {
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Recap call",
                    "start_at": "2025-08-29T09:10:00Z",
                    "end_at": "2025-08-29T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up"
                },
            },
            {
                "name": "GetCalendarEventsForClient",
                "arguments": {
                    "client_id": 3
                }
            }
        ],
        "outputs": [
                "Briefing mailed; CMA saved; audit logged via report re-read; recap call scheduled."
        ]
    }
]
