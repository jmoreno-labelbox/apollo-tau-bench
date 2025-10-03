from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="v2",
        user_id="task_01",
        instruction=(
            "Handle the preparation of a first-time buyer packet for client 16 under broker 8. Desired outcome: a briefing document for client 16 (defaults to 'v1') is created and stored at 'https://test.storage.com/details/client_briefing_016_v1.pdf'; a 'general_update' campaign titled 'First-Time Buyer Packet -Client 16 - Aug 2025' is established; an email to client 16 using template_code 'general_update' with the subject 'Here’s Your Starter Packet' and body_uri 'https://test.storage.com/details/client_briefing_016_v1.pdf' is logged in the campaign; and a reminder hold is scheduled for 2025-08-21 23:00-23:10Z, titled 'Packet follow-up' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc", kwargs={"client_id": 16, "broker_id": 8}
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "First‑Time Buyer Packet -Client 16 - Aug 2025",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Here’s Your Starter Packet",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_016_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 16}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 8,
                    "client_id": 16,
                    "title": "Packet follow-up",
                    "start_at": "2025-08-21T23:00:00Z",
                    "end_at": "2025-08-21T23:10:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 16}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_02",
        instruction=(
            "Coordinate the assembly of seller-outreach drafts for client 19 under broker 7. Final state: a collection of drafts is produced for property_ids ['HTX070','HTX071','HTX072','HTX073'] (contextual), stored at 'https://test.storage.com/drafts/client_19_props_4.pdf'; a 'general_update' campaign called 'Seller Outreach — Client 19- Aug 2025 ' is created; an email to client 19 using template_code 'general_update' with the subject 'Seller Outreach Drafts' and body_uri 'https://test.storage.com/drafts/client_19_props_4.pdf' is recorded within the campaign; and a hold is placed on 2025-08-23 12:00-12:20Z, titled 'Select which drafts to send' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="DraftSellerBrokerBatch",
                kwargs={
                    "client_id": 19,
                    "property_ids": ["HTX070", "HTX071", "HTX072", "HTX073"],
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Seller Outreach — Client 19- Aug 2025 ",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Seller Outreach Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_19_props_4.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 19}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 19,
                    "title": "Select which drafts to send",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 19}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_03",
        instruction=(
            "Handle the preparation of a 3-bed Uptown/Galleria shortlist for client 22 under broker 9. End state: a draft comp report is available and readable for subject 'UPTOWN_3BEDS_C22_AUG25'; a campaign named 'Aug 2025 3-Bed Uptown — Client 22' exists and dispatches one email with the subject '3-Bed Options' (template 'likely_buyer') and body URI 'https://test.storage.com/emails/three_bed_uptown_c22.html'; and a viewing kickoff on 2025-08-27 from 12:10Z to 12:40Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') is on the calendar. Confirm via comp report read, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 22,
                    "subject_property_id": "UPTOWN_3BEDS_C22_AUG25",
                    "created_by_broker_id": 9,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 3‑Bed Uptown — Client 22",
                    "type": "likely_buyer",
                    "created_by": 9,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 22,
                    "broker_id": 9,
                    "subject": "3‑Bed Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/three_bed_uptown_c22.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 22}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 9,
                    "client_id": 22,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-27T12:10:00Z",
                    "end_at": "2025-08-27T12:40:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 22}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_04",
        instruction=(
            "Coordinate the creation of a comps report draft for client 19 under broker 7 and ensure it's shared. End state: a comp report is saved with subject_property_id 'HTX044' marked as 'draft' and is readable; a 'general_update' campaign titled 'Aug 2025 CMA Draft — Client 19' is present and utilized for one email with the subject 'Your Market Analysis is Ready Draft' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/cma_draft_c19.html'; a consult hold is set on 2025-08-23 12:40–13:00Z labeled 'CMA Draft consult' at 'Phone' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 19,
                    "subject_property_id": "HTX044",
                    "created_by_broker_id": 7,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 CMA Draft — Client 19",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Your Market Analysis is Ready Draft",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/cma_draft_c19.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 19}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 19,
                    "title": "CMA Draft consult",
                    "start_at": "2025-08-23T12:40:00Z",
                    "end_at": "2025-08-23T13:00:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 19}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_05",
        instruction=(
            "Handle a premium-area update for client 5 under broker 5. Final state: there is a documented snapshot available for subject property ID 'ROX_PREM_C5_AUG25' in draft status which is readable; a succinct inventory view displays up to six active matches across neighborhoods [6,2,4,10] within 147268-644740 for context; one outreach is attached to a campaign titled 'Desert Ridge Premium - Client 5- Aug 2025 ' with subject 'Premium Area Update' using body URI 'https://test.storage.com/emails/riveroaks_premium_c5.html' and the general-update template; and a follow-up phone hold scheduled for 2025-08-23 from 12:00Z to 12:20Z titled 'Discuss premium options' (source 'follow_up') appears on the calendar. Verify through the preserved snapshot, the campaign record, the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 5,
                    "subject_property_id": "ROX_PREM_C5_AUG25",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [6, 2, 4, 10],
                    "price_min": 147268,
                    "price_max": 644740,
                    "limit": 6,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Desert Ridge Premium - Client 5- Aug 2025 ",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Premium Area Update",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/riveroaks_premium_c5.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "Discuss premium options",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_06",
        instruction=(
            "Coordinate the finalization of a comparative market analysis for client 11 under broker 6. End state: the record for subject property 'HTX012' includes a document link and a status of 'sent_to_client', with session activity showing that it began as a draft in this workflow. Attach one client-facing outreach to a campaign titled 'CMA Results Shared – Client 11', comprising a single message to client 11 with subject 'Your Market Analysis is Ready' utilizing body URI 'https://test.storage.com/emails/cma_c11.html' and the likely-buyer template. Demonstrate completion by retrieving the report's details and the client’s campaign/email records."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 11,
                    "subject_property_id": "HTX012",
                    "created_by_broker_id": 6,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "CMA Results Shared – Client 11",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Your Market Analysis is Ready",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/cma_c11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_07",
        instruction=(
            "Handle a two-segment likely-buyer outreach for clients 5 and 6 under broker 2. Set up a campaign called 'Aug 2025 Likely Buyers — Segment A' of type 'likely_buyer' and use the ID from the creation step in all emails. Use each client's neighborhoods exactly as listed to retrieve context listings (capped at 6 each): client 5 → [6, 2, 4, 10]; client 6 → [8, 12, 6, 5]. Dispatch an email to both clients with the subject 'August Listings Shortlist' and body_uri 'https://test.storage.com/emails/likely_buyer_aug_2025.html'. Schedule a calendar hold for each client titled 'Intro call about shortlist' on 2025-08-22, with client 5 from 16:00-16:30Z and client 6 from 17:00-17:30Z, location 'Phone', notes 'Segment A outreach', source 'follow_up'. Desired outcome: the campaign is created; two emails are documented (clients 5 and 6); and both calendar holds are established at the designated times."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Likely Buyers — Segment A",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={"neighborhood_ids": [6, 2, 4, 10], "limit": 6},
            ),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={"neighborhood_ids": [8, 12, 6, 5], "limit": 6},
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 2,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/likely_buyer_aug_2025.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/likely_buyer_aug_2025.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(name="ListClientEmails", kwargs={"client_id": 6}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 5,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-22T16:00:00Z",
                    "end_at": "2025-08-22T16:30:00Z",
                    "location": "Phone",
                    "notes": "Segment A outreach",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-22T17:00:00Z",
                    "end_at": "2025-08-22T17:30:00Z",
                    "location": "Phone",
                    "notes": "Segment A outreach",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 6}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_08",
        instruction=(
            "Coordinate a Saturday multi-stop tour for client 9 under broker 6. Desired outcome: a route dated 2025-08-23 is set for client 9 with stops ordered as ['HTX221','HTX187','HTX204'] and the map link 'https://maps.example.com/route/c9_aug23' is stored without modifications; the route is accessible; drive-time feasibility is validated between those stops with a maximum of 25 minutes between each; a campaign named 'Aug 2025 Saturday Tour — Client 9' is established and is utilized to send one email with the subject 'Tour Map & Plan' (using the 'general_update' template) and body URI 'https://test.storage.com/emails/tour_plan_c9.html'; and an initial viewing hold on 2025-08-23 from 09:20Z to 09:40Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') is reflected on the calendar. Confirm via the route details, the drive-time verification, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX221", "HTX187", "HTX204"],
                    "map_url": "https://maps.example.com/route/c9_aug23",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX221", "HTX187", "HTX204"],
                    "max_minutes": 25,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Saturday Tour — Client 9",
                    "type": "general_update",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 6,
                    "subject": "Tour Map & Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/tour_plan_c9.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 9,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-23T09:20:00Z",
                    "end_at": "2025-08-23T09:40:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_09",
        instruction=(
            "Handle off-route viewing requests for client 10, coordinated through broker 11. Final outcome: a drafts bundle is generated for properties ['HTX040','HTX042','HTX043'] (context); a 'general_update' campaign titled 'Aug 2025 Off-Route Viewings - Client 10' is established; an internal email sent to client 10 under this campaign features the subject 'Viewing Requests To Send' and body_uri 'https://test.storage.com/emails/offroute_c10.html'; and a follow-up hold is scheduled for client 10 on 2025-08-25 16:00-16:20Z named 'Follow up on viewing requests' via 'Video - Teams' (source 'follow_up'). Confirm by reviewing the campaign, the email, and the events in the client's calendar."
        ),
        actions=[
            Action(
                name="DraftSellerBrokerBatch",
                kwargs={
                    "client_id": 10,
                    "property_ids": ["HTX040", "HTX042", "HTX043"],
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Off-Route Viewings - Client 10",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 10,
                    "subject": "Viewing Requests To Send",
                    "slug": "offroute_c10",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Viewing Requests To Send",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/offroute_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 10}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 11,
                    "client_id": 10,
                    "title": "Follow up on viewing requests",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:20:00Z",
                    "location": "Video - Teams",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 10}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_10",
        instruction=(
            "Distribute a Uptown condo briefing for client 2 under broker 14. Final outcome: a draft comp report document is present for the subject property ID 'MDTN_CONDO_C2_AUG25' and is accessible; a client update relates to a campaign titled 'Aug 2025 Uptown Condos - Client 2' with the subject line 'Uptown Condo Picks' and body URI 'https://test.storage.com/emails/midtown_condos_c2.html' utilizing the general-update template; and a debrief hold on 2025-08-27 from 18:00Z to 18:20Z titled 'Uptown options debrief' at 'Office' (source 'follow_up') appears on the calendar. Validate by accessing the comp report and obtaining the campaign record, client's email log, and the calendar entry."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MDTN_CONDO_C2_AUG25",
                    "created_by_broker_id": 14,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Uptown Condos - Client 2",
                    "type": "general_update",
                    "created_by": 14,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Uptown Condo Picks",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/midtown_condos_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Uptown options debrief",
                    "start_at": "2025-08-27T18:00:00Z",
                    "end_at": "2025-08-27T18:20:00Z",
                    "location": "Office",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_11",
        instruction=(
            "Conduct a comparison of Uptown versus Central City for client 2 handled by broker 3. Desired outcome: create two draft comp report documents that are accessible—'MID_VS_DT_AUG25_A' showing Uptown+Central City context and 'MID_VS_DT_AUG25_B' displaying Central City-only; initiate a client update linked to a campaign called 'Aug 2025 Uptown vs Central City - Client 2' with subject 'Uptown vs Central City' using body URI 'https://test.storage.com/emails/mid_vs_dt_c2.html' alongside the general-update template; schedule a Zoom discussion titled 'Compare neighborhoods' occurring on 2025-08-24 from 16:30Z to 17:00Z on the calendar with source 'follow_up'. Confirm by reviewing both comp reports and accessing the campaign, the client’s email log, and the calendar entry."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MID_VS_DT_AUG25_A",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MID_VS_DT_AUG25_B",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 10}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Uptown vs Central City - Client 2",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Uptown vs Central City",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/mid_vs_dt_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Compare neighborhoods",
                    "start_at": "2025-08-24T16:30:00Z",
                    "end_at": "2025-08-24T17:00:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_12",
        instruction=(
            "Craft a neighborhood preview for client 4 handled by broker 2. Outcome required: a campaign of type 'general_update' named 'Aug 2025 Neighborhood Preview - Client 4' should be available and utilized by the outbound message; obtain a listings snapshot for neighborhood 1 filtered to price range 250000–700000 with beds=2 and baths=2 (context only); ensure one email exists for client 4 with subject 'Neighborhood Preview' and body_uri 'https://test.storage.com/emails/preview_c4.html' connected to that campaign; arrange a calendar hold for client 4 on 2025-08-22 from 15:00–15:30Z with title 'Pre-tour call' at 'Video - Zoom' and source 'follow_up'."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Neighborhood Preview - Client 4",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [1],
                    "price_min": 250000,
                    "price_max": 700000,
                    "beds": 2,
                    "baths": 2,
                },
            ),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 4,
                    "subject": "Neighborhood Preview",
                    "slug": "preview_c4",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Neighborhood Preview",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/preview_c4.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 4}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 4,
                    "title": "Pre-tour call",
                    "start_at": "2025-08-22T15:00:00Z",
                    "end_at": "2025-08-22T15:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 4}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_13",
        instruction=(
            "Manage a Westbury CMA + follow-up process for client 21 under broker 4. Final outcome: a comp report for subject 'WESTBURY_CMA_C21_AUG25' is prepared in draft and is accessible, then its status is revised to 'sent_to_client' and reviewed; a campaign titled 'Aug 2025 Westbury CMA — Client 21' (type 'general_update') exists and is used to deliver one email to client 21 with subject 'Your Westbury CMA' using template 'general_update' and body URI 'https://test.storage.com/emails/westbury_cma_c21.html'; and a follow-up hold scheduled for 2025-08-23 from 15:30Z to 15:50Z titled 'CMA Q&A' at 'Video — Zoom' (source 'follow_up') shows on the calendar. Confirm by reviewing the comp report, the campaign, the client’s email log, and the client’s calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 21,
                    "subject_property_id": "WESTBURY_CMA_C21_AUG25",
                    "created_by_broker_id": 4,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Westbury CMA — Client 21",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 21,
                    "broker_id": 4,
                    "subject": "Your Westbury CMA",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/westbury_cma_c21.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 21}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 21,
                    "title": "CMA Q&A",
                    "start_at": "2025-08-23T15:30:00Z",
                    "end_at": "2025-08-23T15:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 21}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_14",
        instruction=(
            "Coordinate a weekend open-house overview for client 10 under broker 11. Final state: open-house windows are retrieved for neighborhoods [13,1,12] (context); a 'general_update' campaign named 'Aug 2025 Weekend OH — Client 10' exists; one email to client 10 with subject 'Weekend Open Houses' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/weekend_oh_c10.html' is documented; a planning hold exists for 2025-08-23 13:00–13:20Z titled 'Plan weekend open houses' at 'Phone' (source 'follow_up'). Confirm with inspections."
        ),
        actions=[
            Action(
                name="OpenHouseWindowsByNeighborhoods",
                kwargs={"neighborhood_ids": [13, 1, 12]},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Weekend OH — Client 10",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Weekend Open Houses",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_oh_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 10}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 11,
                    "client_id": 10,
                    "title": "Plan weekend open houses",
                    "start_at": "2025-08-23T13:00:00Z",
                    "end_at": "2025-08-23T13:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 10}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_15",
        instruction=(
            "Handle a price-alert follow-up for client 13 under broker 5. End state: recent sales for 'HTX043' (limit 3) have been checked (context); a 'general_update' campaign titled 'Aug 2025 Price Alert Follow-Up — Client 13' is available and used for one email with subject 'Price Move & Local Sales' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/price_move_sales_c13.html'; a 2025-08-23 10:00–10:20Z 'Price-move debrief' hold at 'USNV Strickland, FPO AP 98640' (source 'client_meeting') is set. Confirm by performing reads."
        ),
        actions=[
            Action(
                name="RecentSalesForProperty",
                kwargs={"property_id": "HTX043", "limit": 3},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Price Alert Follow-Up — Client 13",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "Price Move & Local Sales",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/price_move_sales_c13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 13}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 13,
                    "title": "Price-move debrief",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:20:00Z",
                    "location": "USNV Strickland, FPO AP 98640",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 13}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_16",
        instruction=(
            "Coordinate an investor packet for client 20 under broker 11. End state: a briefing document is created for client 20 (defaults to 'v1'); a 'general_update' campaign named 'Aug 2025 Investor Packet — Client 20' exists; an email to client 20 using template_code 'general_update' with subject 'Investor Packet' and body_uri 'https://test.storage.com/guides/investor_packet_c20.pdf' is logged under the campaign; and there is a review hold on 2025‑08‑22 20:00–20:25Z titled 'Investor packet review' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc", kwargs={"client_id": 20, "broker_id": 11}
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Investor Packet — Client 20",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Investor Packet",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/guides/investor_packet_c20.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 20}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 11,
                    "client_id": 20,
                    "title": "Investor packet review",
                    "start_at": "2025-08-22T20:00:00Z",
                    "end_at": "2025-08-22T20:25:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 20}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_17",
        instruction=(
            "Handle the preparation of an investor-focused condo snapshot for client 15 under broker 8. Final outcome: make sure a listings context for neighborhoods [5,12,1,7] with property_type 'condo' and price range 246399–420408 (limit 6) is documented; compute a mortgage estimate for client 15 at list_price 400000; ensure a 'general_update' campaign titled 'Aug 2025 Investor Snapshot — Client 15' is established and utilized for one email to client 15 with subject 'Condo Investor Snapshot' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/investor_snapshot_c15.html'; set a consultation appointment on 2025-08-24 20:30–21:00Z named 'Investor consult' using 'Video — Zoom' (source 'follow_up'). Validate the entries by verifying the campaign, the client’s emails, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [5, 12, 1, 7],
                    "property_type": "condo",
                    "price_min": 246399,
                    "price_max": 420408,
                    "limit": 6,
                },
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 15, "list_price": 400000},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Investor Snapshot — Client 15",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Condo Investor Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/investor_snapshot_c15.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 15}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Investor consult",
                    "start_at": "2025-08-24T20:30:00Z",
                    "end_at": "2025-08-24T21:00:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 15}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_18",
        instruction=(
            "Coordinate the preparation of a financing brief for client 18 under broker 6. Outcome: verify the client’s mortgage profile; compute a 30‑year AZ estimate for a list price of 540000; generate a briefing document (version 'aug25') and cite it in one email under a campaign named 'Aug 2025 Financing Brief — Client 18' with subject 'Your Financing Brief' (template 'general_update') and body URI 'https://test.storage.com/details/client_briefing_018_aug25.pdf'; schedule a follow‑up phone meeting on 2025-08-24 from 19:00Z to 19:20Z titled 'Financing Q&A' (source 'follow_up') on the calendar. Confirm via the campaign/email and calendar."
        ),
        actions=[
            Action(name="RetrieveMortgageProfile", kwargs={"client_id": 18}),
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 18,
                    "list_price": 540000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="CreateBriefingDoc",
                kwargs={"client_id": 18, "broker_id": 6, "version_tag": "aug25"},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Financing Brief — Client 18",
                    "type": "general_update",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 18,
                    "broker_id": 6,
                    "subject": "Your Financing Brief",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_018_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 18}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 18,
                    "title": "Financing Q&A",
                    "start_at": "2025-08-24T19:00:00Z",
                    "end_at": "2025-08-24T19:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 18}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_19",
        instruction=(
            "Handle the delivery of a loan-sizing snapshot for client 10 with broker 11. Final status: calculate a mortgage estimate at list_price 600000 (region 'AZ', term_years 30) as context; a 'general_update' campaign labeled 'Aug 2025 Loan Sizing — Client 10' exists; an email to client 10 with subject 'Loan Sizing Snapshot' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/loan_sizing_c10.html' is documented; a 2025-08-23 13:20–13:40Z 'Sizing consult' hold at 'Phone' (source 'follow_up'). Confirm via reads."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 10,
                    "list_price": 600000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Loan Sizing — Client 10",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Loan Sizing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/loan_sizing_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 10}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 11,
                    "client_id": 10,
                    "title": "Sizing consult",
                    "start_at": "2025-08-23T13:20:00Z",
                    "end_at": "2025-08-23T13:40:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 10}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_20",
        instruction=(
            "Coordinate the creation of a Sunday route plan for client 2 under broker 3 using neighborhood context. The final state should show: open-house windows for neighborhood [1] were utilized as context; a route dated 2025-08-24 is saved with ordered stops ['HTX001','HTX004','HTX005'] and map URL 'https://maps.google.com/route/sun_c2_20250824'; a 30-minute hop check is met; a 'likely_buyer' campaign titled 'Aug 2025 Sunday Route — Client 2' exists; an email to client 2 using template_code 'likely_buyer' with subject 'Sunday Route — 2025-08-24' and the same map URL as body_uri is recorded under the campaign; and two holds exist — 09:55–10:05Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10–13:25Z titled 'Post-route debrief' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="OpenHouseWindowsByNeighborhoods",
                kwargs={"neighborhood_ids": [1]},
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/sun_c2_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Sunday Route — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Sunday Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/sun_c2_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T09:55:00Z",
                    "end_at": "2025-08-24T10:05:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Post-route debrief",
                    "start_at": "2025-08-24T13:10:00Z",
                    "end_at": "2025-08-24T13:25:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_21",
        instruction=(
            "Prepare drafts for viewing requests for client 11 under broker 4. in the final state: a drafts bundle is available for property_ids ['HTX055','HTX057','HTX060'] (context) at 'https://test.storage.com/drafts/client_11_props_3.pdf'; this file is linked to client 11; a 'general_update' campaign titled 'Aug 2025 Viewing Requests — Client 11' is created; one email to client 11 with the subject 'Viewing Requests Drafts' and body_uri 'https://test.storage.com/drafts/client_11_props_3.pdf' is recorded within the campaign; and a confirmation hold is set for 2025-08-22 17:00-17:20Z with the title 'Confirm viewing requests' via 'Phone' (source 'follow_up'). Validate by reviewing the campaign, the email for client 11, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="DraftSellerBrokerBatch",
                kwargs={
                    "client_id": 11,
                    "property_ids": ["HTX055", "HTX057", "HTX060"],
                },
            ),
            Action(
                name="LinkDocumentToClient",
                kwargs={
                    "client_id": 11,
                    "file_uri": "https://test.storage.com/drafts/client_11_props_3.pdf",
                    "created_by": 4,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Viewing Requests — Client 11",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 11,
                    "broker_id": 4,
                    "subject": "Viewing Requests Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_11_props_3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 11}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 11,
                    "title": "Confirm viewing requests",
                    "start_at": "2025-08-22T17:00:00Z",
                    "end_at": "2025-08-22T17:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_22",
        instruction=(
            "Dispatch a welcome packet to client 20 under broker 7. Finalize by ensuring: a 'general_update' campaign named 'Aug 2025 Welcome - Client 20' is established; an email to client 20 is logged under the campaign with the subject 'Welcome & Next Steps' and body_uri 'https://test.storage.com/emails/welcome_c20.html'; along with two holds — one for 2025-08-22 18:00-18:20Z titled 'Welcome call' via 'Phone' (source 'follow_up'), and another for 2025-08-23 18:00-18:30Z titled 'Next-steps planning' via 'Video - Zoom' (source 'follow_up'). Verify by reading back the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Welcome - Client 20",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 20,
                    "subject": "Welcome & Next Steps",
                    "slug": "welcome_c20",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 20,
                    "broker_id": 7,
                    "subject": "Welcome & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/welcome_c20.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 20}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Welcome call",
                    "start_at": "2025-08-22T18:00:00Z",
                    "end_at": "2025-08-22T18:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Next-steps planning",
                    "start_at": "2025-08-23T18:00:00Z",
                    "end_at": "2025-08-23T18:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 20}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_23",
        instruction=(
            "Coordinate a concise compensation package for client 2 under broker 3. Finalize with a comp report saved for subject_property_id 'HTX049' (created_by_broker_id 3) marked as 'draft' and confirmed through reading; ensure a 'likely_buyer' campaign titled 'Aug 2025 Quick Comps — Client 2' is in place; send one email to client 2 with the subject 'Quick Comps Pack' and body_uri 'https://test.storage.com/emails/quick_comps_c2.html' recorded in the campaign; and place a follow-up hold on 2025–08–23 14:00–14:20Z labeled 'Comps review' via 'Phone' (source 'follow_up'). Confirm by retrieving the comp report details, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "HTX049",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Quick Comps — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Quick Comps Pack",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/quick_comps_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Comps review",
                    "start_at": "2025-08-23T14:00:00Z",
                    "end_at": "2025-08-23T14:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_24",
        instruction=(
            "Handle a three-home seller outreach packet for client 8 under broker 5. Ensure completion with an outreach drafts bundle for ['HTX401','HTX402','HTX403']; a campaign titled 'Aug 2025 Seller Inquiries — Client 8' should exist and manage sending an email with the subject 'Owner Inquiry Drafts' (template 'general_update') and body URI 'https://test.storage.com/drafts/client_8_props_3.pdf'; document an audit event 'drafts_prepped' on the campaign and re-read the campaign; and have a follow-up phone hold on 2025-08-25 from 13:30Z to 13:50Z titled 'Seller outreach debrief' (source 'follow_up') shown on the calendar. Confirm this through campaign retrievals, email logs, and calendar checks."
        ),
        actions=[
            Action(
                name="DraftSellerBrokerBatch",
                kwargs={"client_id": 8, "property_ids": ["HTX401", "HTX402", "HTX403"]},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Seller Inquiries — Client 8",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 8,
                    "broker_id": 5,
                    "subject": "Owner Inquiry Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_8_props_3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 8}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 5,
                    "action": "drafts_prepped",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 8,
                    "title": "Seller outreach debrief",
                    "start_at": "2025-08-25T13:30:00Z",
                    "end_at": "2025-08-25T13:50:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 8}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_25",
        instruction=(
            "Coordinate the creation of a Arcadia first-time buyer briefing for client 7 under broker 5. End state: a briefing document (version 'aug25') is produced and included in one email under a campaign titled 'Aug 2025 Buyer Brief — Client 7' with subject 'Your Buyer Brief' (template 'general_update') and body URI 'https://test.storage.com/details/client_briefing_007_aug25.pdf'; and a follow-up phone appointment on 2025-08-24 from 17:10Z to 17:30Z titled 'Brief Q&A' (source 'follow_up') is placed on the calendar. Confirm by reviewing the campaign, the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc",
                kwargs={"client_id": 7, "broker_id": 5, "version_tag": "aug25"},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Buyer Brief — Client 7",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 7,
                    "broker_id": 5,
                    "subject": "Your Buyer Brief",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_007_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 7}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 7,
                    "title": "Brief Q&A",
                    "start_at": "2025-08-24T17:10:00Z",
                    "end_at": "2025-08-24T17:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 7}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_26",
        instruction=(
            "Arrange a bordering-area Sunday tour for client 2 with broker 3. End state: neighborhood 1 details along with its bordering list are accessed (context); a route for 2025-08-24 is recorded with ordered stops ['HTX001','HTX004','HTX005'] and map 'https://maps.google.com/route/dt_mid_c2_20250824'; hops satisfy a ≤30-minute check; a 'likely_buyer' campaign named 'Aug 2025 Bordering Tour — Client 2' is present; an email to client 2 with subject 'Bordering Tour — 2025-08-24' (template_code 'likely_buyer') using that map URL as body_uri is documented; two holds are scheduled: 09:55–10:05Z 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10–13:25Z 'Post-tour debrief' at 'Phone' (source 'follow_up'); register an audit 'open_house_route_built' on the route and then inspect the route again to verify state."
        ),
        actions=[
            Action(name="FetchNeighborhood", kwargs={"neighborhood_id": 1}),
            Action(name="ListAdjacentNeighborhoods", kwargs={"neighborhood_id": 1}),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/dt_mid_c2_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Bordering Tour — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Tour — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/dt_mid_c2_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T09:55:00Z",
                    "end_at": "2025-08-24T10:05:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Post-tour debrief",
                    "start_at": "2025-08-24T13:10:00Z",
                    "end_at": "2025-08-24T13:25:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 3,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {"stops": ["HTX001", "HTX004", "HTX005"]},
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_27",
        instruction=(
            "Handle outreach to sellers and brokers for client 5, under broker 5, regarding properties ['HTX201','HTX205','HTX207']. The final result should be an outreach drafts bundle; a campaign named 'Aug 2025 Seller Outreach — Client 5' is to be created, sending an email with the subject 'Seller Outreach Drafts' (using template 'general_update') featuring a body URI of 'https://test.storage.com/drafts/client_5_props_3.pdf'; and a follow-up event titled 'Review outreach drafts' should be scheduled on 2025-08-22 from 21:10Z to 21:30Z as a 'Phone' meeting (source 'follow_up') in the calendar. Verify all details through the campaign record, email log, and calendar."
        ),
        actions=[
            Action(
                name="DraftSellerBrokerBatch",
                kwargs={"client_id": 5, "property_ids": ["HTX201", "HTX205", "HTX207"]},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Seller Outreach — Client 5",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Seller Outreach Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_5_props_3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "Review outreach drafts",
                    "start_at": "2025-08-22T21:10:00Z",
                    "end_at": "2025-08-22T21:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_28",
        instruction=(
            "Coordinate the production and delivery of a comparable report for client 10 under broker 4. Achieve a state where a comp report is saved for subject_property_id 'HTX072' (created_by_broker_id 4) marked as 'draft', then progressed to 'sent_to_client'; confirm the report and its associated comparables/documents are accessible; a 'likely_buyer' campaign titled 'Aug 2025 Comp Report — Client 10' should be active; ensure there is one email to client 10 with the subject 'Comp Report Delivered' and body_uri 'https://test.storage.com/emails/comp_report_c10.html' documented in the campaign; and make sure a follow-up hold on 2025-08-22 from 18:00 to 18:20Z under the title 'Comp report debrief' takes place as a 'Video — Zoom' session (source 'follow_up', notes 'CMA review & Q&A'). Validate by reading back the comp report details post-save and status update, alongside the campaign, the email, and calendar events."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 10,
                    "subject_property_id": "HTX072",
                    "created_by_broker_id": 4,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Comp Report — Client 10",
                    "type": "likely_buyer",
                    "created_by": 4,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Comp Report Delivered",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comp_report_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 10}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 10,
                    "title": "Comp report debrief",
                    "start_at": "2025-08-22T18:00:00Z",
                    "end_at": "2025-08-22T18:20:00Z",
                    "location": "Video — Zoom",
                    "notes": "CMA review & Q&A",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 10}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_29",
        instruction=(
            "Arrange a Sugar Land tour for client 11 with broker 6 on 2025-08-25. Objective: client 11's route includes ordered stops ['SL_501','SL_512','SL_498'] and the map link 'https://maps.example.com/route/c11_aug25' is stored exactly; ensure the route is accessible; validate drive-time feasibility, ensuring a maximum of 25 minutes between stops; establish a campaign titled 'Aug 2025 Sugar Land Tour — Client 11' sending a single email 'Your Sugar Land Tour' (template 'general_update') using 'https://test.storage.com/emails/sl_tour_c11.html'; and a pre-tour client meeting on 2025-08-25 from 08:30Z to 08:50Z titled 'Pre-tour brief' at 'Video — Zoom' is shown on the calendar. Confirm via route details, drive-time check, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 11,
                    "date": "2025-08-25",
                    "stops_ordered_json": ["SL_501", "SL_512", "SL_498"],
                    "map_url": "https://maps.example.com/route/c11_aug25",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["SL_501", "SL_512", "SL_498"],
                    "max_minutes": 25,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Sugar Land Tour — Client 11",
                    "type": "general_update",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Your Sugar Land Tour",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/sl_tour_c11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 11}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Pre-tour brief",
                    "start_at": "2025-08-25T08:30:00Z",
                    "end_at": "2025-08-25T08:50:00Z",
                    "location": "Video — Zoom",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_30",
        instruction=(
            "Coordinate a Saturday route for client 12 with broker 6. Endpoint: a route dated 2025-08-23 with ordered stops ['HTX032','HTX036','HTX049'] is recorded using map URL 'https://maps.google.com/route/weekend_c12_20250823' and complies with a 30-minute hop test; a 'likely_buyer' campaign titled 'Aug 2025 Saturday Tour — Client 12' is active; an email to client 12 with subject 'Saturday Route — 2025-08-23' and body_uri 'https://maps.google.com/route/weekend_c12_20250823' is documented; and two holds are present — 09:40-09:50Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10-13:30Z titled 'Tour debrief' at 'Video — Zoom' (source 'follow_up', notes 'Next steps & offers'). Verify by reviewing the route details, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 12,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX032", "HTX036", "HTX049"],
                    "map_url": "https://maps.google.com/route/weekend_c12_20250823",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX032", "HTX036", "HTX049"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Saturday Tour — Client 12",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 12,
                    "broker_id": 6,
                    "subject": "Saturday Route — 2025-08-23",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/weekend_c12_20250823",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 12}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 12,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-23T09:40:00Z",
                    "end_at": "2025-08-23T09:50:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 12,
                    "title": "Tour debrief",
                    "start_at": "2025-08-23T13:10:00Z",
                    "end_at": "2025-08-23T13:30:00Z",
                    "location": "Video — Zoom",
                    "notes": "Next steps & offers",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 12}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_31",
        instruction=(
            "Coordinate the creation of a concise shortlist for client 11 alongside broker 6. Ensure the final setup includes: a 'likely_buyer' campaign named 'Aug 2025 Compact Shortlist — Client 11'; a context search executed in neighborhoods [1, 2] with price_min 200000, price_max 900000, beds 1, baths 1, sqft_min 800, sqft_max 2200, limit 8; a single email to client 11 categorized under the established campaign, subject 'Shortlist & Saturday Route', template_code 'likely_buyer', and body_uri 'https://test.storage.com/emails/compact_shortlist_11.html'; a Saturday (2025‑08‑23) route documented with ordered stops ['HTX036','HTX032','HTX049'] at map URL 'https://maps.google.com/route/htx_011_20250823'; and two Saturday holds for client 11: 11:00–11:30Z titled 'Shortlist review' (location 'Video — Zoom', notes 'Review shortlist & route', source 'follow_up') and 12:00–12:30Z titled 'Saturday Schedule Check-CO' (location 'Phone', notes 'Confirm times & transport', source 'follow_up'). Verify the entries by reviewing back the campaign, the email, the route details, and the calendar events."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Compact Shortlist — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={
                    "neighborhood_ids": [1, 2],
                    "price_min": 200000,
                    "price_max": 900000,
                    "beds": 1,
                    "baths": 1,
                    "sqft_min": 800,
                    "sqft_max": 2200,
                    "limit": 8,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Shortlist & Saturday Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/compact_shortlist_11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 11}),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 11,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX036", "HTX032", "HTX049"],
                    "map_url": "https://maps.google.com/route/htx_011_20250823",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Shortlist review",
                    "start_at": "2025-08-23T11:00:00Z",
                    "end_at": "2025-08-23T11:30:00Z",
                    "location": "Video — Zoom",
                    "notes": "Review shortlist & route",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Saturday Schedule Check-CO",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:30:00Z",
                    "location": "Phone",
                    "notes": "Confirm times & transport",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 11}),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_32",
        instruction=(
            "Arrange for a combined comps-and-tour plan for client 2 under broker 3. Ensure the end configuration includes: a comp report for subject_property_id 'HTX041' (created_by_broker_id 3) saved with status 'draft' and confirmed; a Saturday route on the date 2025-08-23 recorded with ordered stops ['HTX041','HTX032','HTX036'] and map URL 'https://maps.google.com/route/comp_tour_c2_20250823' adhering to a ≤30-minute hop limit; a 'likely_buyer' campaign named 'Aug 2025 Comp + Tour — Client 2' in place; two emails documented under the campaign for client 2 — one with template_code 'likely_buyer', subject 'Comps Overview' and body_uri 'https://test.storage.com/emails/comps_overview_c2.html', and another with template_code 'likely_buyer', subject 'Saturday Tour Plan' and body_uri 'https://maps.google.com/route/comp_tour_c2_20250823'; two holds scheduled — 2025-08-22 18:00–18:20Z titled 'Comps review' at 'Phone' (source 'follow_up') and 2025-08-23 09:40–09:50Z titled 'Depart for tour' at 'Client Home' (source 'viewing'). Register an audit 'routes_shared_and_viewings_set' on the route."
        ),
        actions=[

            Action(
                name="CreateOrUpdateCompReport",
                kwargs={"client_id": 2, "subject_property_id": "HTX041", "created_by_broker_id": 3,
                        "final_status": "draft"}
            ),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 1, "status": "confirmed"}
            ),

            Action(
                name="ValidateDriveTimeHops",
                kwargs={"property_ids": ["HTX041", "HTX032", "HTX036"], "max_minutes": 30}
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX041", "HTX032", "HTX036"],
                    "map_url": "https://maps.google.com/route/comp_tour_c2_20250823",
                    "created_by_broker_id": 3
                }
            ),

            Action(
                name="NewCampaignCreator",
                kwargs={"name": "Aug 2025 Comp + Tour — Client 2", "type": "likely_buyer", "created_by": 3}
            ),

            Action(
                name="ComposeClientEmail",
                kwargs={"template_code": "likely_buyer", "client_id": 2, "subject": "Comps Overview"}
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Comps Overview",
                    "body_uri": "https://test.storage.com/emails/comps_overview_c2.html",
                    "template_code": "likely_buyer",
                    "campaign_id": None
                }
            ),
            Action(
                name="ComposeClientEmail",
                kwargs={"template_code": "likely_buyer", "client_id": 2, "subject": "Saturday Tour Plan"}
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Saturday Tour Plan",
                    "body_uri": "https://maps.google.com/route/comp_tour_c2_20250823",
                    "template_code": "likely_buyer",
                    "campaign_id": None
                }
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Comps review",
                    "start_at": "2025-08-22T18:00:00Z",
                    "end_at": "2025-08-22T18:20:00Z",
                    "location": "Phone",
                    "notes": "Review comps snapshot",
                    "source": "follow_up"
                }
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Depart for tour",
                    "start_at": "2025-08-23T09:40:00Z",
                    "end_at": "2025-08-23T09:50:00Z",
                    "location": "Client Home",
                    "notes": "Leave buffer for transit",
                    "source": "viewing"
                }
            ),

            Action(
                name="AppendAuditEvent",
                kwargs={"actor_id": 3, "action": "routes_shared_and_viewings_set", "entity_type": "routes",
                        "entity_id": "c2_2025-08-23"}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="v2",
        user_id="task_33",
        instruction=(
            "Handle the creation of a comps report draft for client 19 under broker 7 and ensure it is shared. End state: a comp report is saved for subject_property_id 'HTX044' with status 'draft' and read; a 'general_update' campaign named 'Aug 2025 CMA Draft — Client 19' exists and is used for one email with subject 'Your Market Analysis is Ready Draft' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/cma_draft_c19.html'; a consult hold is scheduled on 2025-08-23 12:40–13:00Z titled 'CMA Draft consult' at 'Phone' (source 'follow_up'). Confirm by reviewing reads."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 19,
                    "subject_property_id": "HTX044",
                    "created_by_broker_id": 7,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 CMA Draft — Client 19",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Your Market Analysis is Ready Draft",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/cma_draft_c19.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 19}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 19,
                    "title": "CMA Draft consult",
                    "start_at": "2025-08-23T12:40:00Z",
                    "end_at": "2025-08-23T13:00:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 19}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_34",
        instruction=(
            "Coordinate the creation of a townhouse seeker brief for client 12 with broker 3. End state: neighborhood 11 details and its bordering IDs are retrieved; listings are explored within [11,1,13] for property_type 'townhouse' and price 128758–279350 (limit 6) as context; a 'likely_buyer' campaign named 'Aug 2025 Townhouse Path — Client 12' exists; an email to client 12 with subject 'Townhouse Options' (template_code 'likely_buyer') and body_uri 'https://test.storage.com/emails/townhouse_path_c12.html' is documented; a 2025-08-25 14:30–14:50Z hold titled 'Townhouse plan' at 'Phone' (source 'follow_up') is scheduled. Verify through reads."
        ),
        actions=[
            Action(name="FetchNeighborhood", kwargs={"neighborhood_id": 11}),
            Action(name="ListAdjacentNeighborhoods", kwargs={"neighborhood_id": 11}),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={
                    "neighborhood_ids": [11, 1, 13],
                    "property_type": "townhouse",
                    "price_min": 128758,
                    "price_max": 279350,
                    "limit": 6,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Townhouse Path — Client 12",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/townhouse_path_c12.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 12}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Townhouse plan",
                    "start_at": "2025-08-25T14:30:00Z",
                    "end_at": "2025-08-25T14:50:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 12}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_35",
        instruction=(
            "Handle the sending of a Heights historic shortlist for client 15 under broker 8. End state: a draft comp report document for subject property ID 'HGTS_HIST_C15_AUG25' should exist and be readable; an outbound update must be linked to a campaign titled 'Aug 2025 Heights Historic - Client 15' with the subject 'Heights Historic Picks' using body URI 'https://test.storage.com/emails/heights_historic_c15.html' and the general-update template; a hold for a viewing-plan on 2025-08-30 from 14:00Z to 14:20Z titled 'Heights tour plan' at '1234 Heights Boulevard, Phoenix, AZ 77008' (source 'viewing') should appear on the calendar. Validate by checking the comp report, the campaign record, the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 15,
                    "subject_property_id": "HGTS_HIST_C15_AUG25",
                    "created_by_broker_id": 8,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Heights Historic - Client 15",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Heights Historic Picks",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/heights_historic_c15.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 15}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Heights tour plan",
                    "start_at": "2025-08-30T14:00:00Z",
                    "end_at": "2025-08-30T14:20:00Z",
                    "location": "1234 Heights Boulevard, Phoenix, AZ 77008",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 15}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_36",
        instruction=(
            "Coordinate the assembly of a Northside Sunday tour for client 20 under broker 11. Final state: a route for 2025‑08‑24 must be saved with ordered stops ['HTX066','HTX067','HTX068'] and map URL 'https://maps.google.com/route/northside_c20_20250824'; a hop check should confirm ≤30 minutes between stops; a 'likely_buyer' campaign named 'Aug 2025 Northside Tour — Client 20' must exist; an email to client 20 with subject 'Northside Route — 2025‑08‑24' and the map URL as body_uri should be recorded; and two holds must exist — 09:15–09:25Z titled 'Pre‑drive check' at 'Phone' (source 'follow_up') and 12:45–13:05Z titled 'Debrief call' at 'Phone' (source 'follow_up'). Prove by examining the route details, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 20,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX066", "HTX067", "HTX068"],
                    "map_url": "https://maps.google.com/route/northside_c20_20250824",
                    "created_by_broker_id": 11,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX066", "HTX067", "HTX068"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Northside Tour — Client 20",
                    "type": "likely_buyer",
                    "created_by": 11,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Northside Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/northside_c20_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 20}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 11,
                    "client_id": 20,
                    "title": "Pre-drive check",
                    "start_at": "2025-08-24T09:15:00Z",
                    "end_at": "2025-08-24T09:25:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 11,
                    "client_id": 20,
                    "title": "Debrief call",
                    "start_at": "2025-08-24T12:45:00Z",
                    "end_at": "2025-08-24T13:05:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 20}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_37",
        instruction=(
            "Handle the sending of a Garden Oaks CMA with financing for client 17 under broker 7. End state: a draft comp report is created and viewable for subject 'GARDEN_OAKS_CMA_C17_AUG25'; a 30-year AZ mortgage estimate is calculated for list price 680000; a campaign with the title 'Aug 2025 Garden Oaks CMA — Client 17' is established and dispatches one email with subject 'CMA + Payment Estimate' (template 'likely_buyer') and body URI 'https://test.storage.com/emails/go_cma_finance_c17.html'; a Zoom CMA review scheduled on 2025-08-28 from 17:00Z to 17:30Z titled 'CMA review' at 'Video — Zoom' (source 'client_meeting') is placed on the calendar. Confirm via comp report read, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 17,
                    "subject_property_id": "GARDEN_OAKS_CMA_C17_AUG25",
                    "created_by_broker_id": 7,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 17,
                    "list_price": 680000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Garden Oaks CMA — Client 17",
                    "type": "likely_buyer",
                    "created_by": 7,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 17,
                    "broker_id": 7,
                    "subject": "CMA + Payment Estimate",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/go_cma_finance_c17.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 17}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 17,
                    "title": "CMA review",
                    "start_at": "2025-08-28T17:00:00Z",
                    "end_at": "2025-08-28T17:30:00Z",
                    "location": "Video — Zoom",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 17}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_38",
        instruction=(
            "Coordinate the preparation of a sales-context financing snapshot for client 8 under broker 12, concentrating on Medical Center condos. End state: recent sales are retrieved for property_id 'HTX049' (limit 3) as context; a mortgage estimate is calculated for client 8 at list_price 550000; a 'general_update' campaign titled 'Aug 2025 Med Center Finance — Client 8' is set up and used for one email with subject 'Medical Center Finance Snapshot' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/medcenter_finance_c8.html'; a consult hold is placed 2025-08-26 09:00–09:30Z titled 'Financing consult' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="RecentSalesForProperty",
                kwargs={"property_id": "HTX049", "limit": 3},
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 8, "list_price": 550000},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Med Center Finance — Client 8",
                    "type": "general_update",
                    "created_by": 12,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Medical Center Finance Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/medcenter_finance_c8.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 8}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Financing consult",
                    "start_at": "2025-08-26T09:00:00Z",
                    "end_at": "2025-08-26T09:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 8}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_39",
        instruction=(
            "Handle a neighborhood open‑house sweep for client 20 under broker 7 throughout neighborhoods [11,6,13] during the 2025‑08‑23 weekend. Desired outcome: the neighborhood open‑house windows are inspected; a campaign named 'Aug 2025 Open House Sweep — Client 20' is registered, dispatching one email 'Open House Sweep' (template 'general_update') with body URI 'https://test.storage.com/emails/oh_sweep_c20.html'; and a buffer hold on 2025-08-24 from 12:40Z to 13:00Z titled 'Open House Sweep Q&A' at 'Cafe — Arcadia' (source 'follow_up') listed on the calendar. Confirm through the campaign/email and the calendar."
        ),
        actions=[
            Action(
                name="OpenHouseWindowsByNeighborhoods",
                kwargs={"neighborhood_ids": [11, 6, 13]},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Open House Sweep — Client 20",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 20,
                    "broker_id": 7,
                    "subject": "Open House Sweep",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/oh_sweep_c20.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 20}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Open House Sweep Q&A",
                    "start_at": "2025-08-24T12:40:00Z",
                    "end_at": "2025-08-24T13:00:00Z",
                    "location": "Cafe — Arcadia",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 20}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_40",
        instruction=(
            "Organize weekend logistics for clients 6 and 7 under broker 4. Needed outcome: a 'general_update' campaign titled 'Aug 2025 Weekend Logistics - C6 & C7' is established; emails are documented under that campaign with subject 'Weekend Logistics' and body_uris 'https://test.storage.com/emails/weekend_c6.html' (client 6) and 'https://test.storage.com/emails/weekend_c7.html' (client 7); and two holds are in place — client 6 at 2025-08-23 13:00-13:20Z titled 'Prep call' at 'Video - Zoom' (source 'follow_up') and client 7 at 2025-08-23 13:30-13:50Z titled 'Prep call' at 'Video - Zoom' (source 'follow_up'). Validate by reviewing the campaign, emails for both clients, and calendar events for both clients."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Weekend Logistics - C6 & C7",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 6,
                    "subject": "Weekend Logistics",
                    "slug": "weekend_c6",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 6,
                    "broker_id": 4,
                    "subject": "Weekend Logistics",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 6}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 7,
                    "subject": "Weekend Logistics",
                    "slug": "weekend_c7",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 7,
                    "broker_id": 4,
                    "subject": "Weekend Logistics",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_c7.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 7}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 6,
                    "title": "Prep call",
                    "start_at": "2025-08-23T13:00:00Z",
                    "end_at": "2025-08-23T13:20:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 7,
                    "title": "Prep call",
                    "start_at": "2025-08-23T13:30:00Z",
                    "end_at": "2025-08-23T13:50:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 6}),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 7}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_41",
        instruction=(
            "Handle the delivery of a v2 briefing for client 3 facilitated by broker 1. Final state: ensure a briefing document is produced with version_tag 'v2' and subsequently stored at 'https://test.storage.com/details/client_briefing_003_v2.pdf'; there should be a 'general_update' campaign titled 'Aug 2025 Briefing v2 — Client 3'; log an email to client 3 using template_code 'general_update' with the subject 'Updated Briefing (v2)' and body_uri 'https://test.storage.com/details/client_briefing_003_v2.pdf' as part of that campaign; additionally, place a review hold dated 2025‑08‑22 16:30–16:50Z, titled 'Briefing v2 review' at 'Video — Zoom' (from source 'follow_up')."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc",
                kwargs={"client_id": 3, "broker_id": 1, "version_tag": "v2"},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Briefing v2 — Client 3",
                    "type": "general_update",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Updated Briefing (v2)",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_003_v2.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 3}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Briefing v2 review",
                    "start_at": "2025-08-22T16:30:00Z",
                    "end_at": "2025-08-22T16:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 3}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_42",
        instruction=(
            "Coordinate preparation of a pre-approval and tour plan for client 1 alongside broker 3. Final outcome: calculate a mortgage estimate based on a list_price of 600000 (contextual information); establish a 'general_update' campaign named 'Aug 2025 Pre-approval & Tour - Client 1'; ensure an email to client 1 with the subject 'Pre-approval & Tour Plan' and body_uri 'https://test.storage.com/emails/preapprove_tour_c1.html' is filed under the campaign; moreover, set two holds: 2025-08-22 09:00-09:30Z titled 'Lender pre-approval' at 'Phone' (sourced from 'follow_up') and 2025-08-24 15:00-16:30Z titled 'Tour window' at 'TBD' (sourced from 'viewing'). Confirm this by reviewing the campaign, the email, and the calendar entries."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 1, "list_price": 600000},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Pre-approval & Tour - Client 1",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Pre-approval & Tour Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/preapprove_tour_c1.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 1}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Lender pre-approval",
                    "start_at": "2025-08-22T09:00:00Z",
                    "end_at": "2025-08-22T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Tour window",
                    "start_at": "2025-08-24T15:00:00Z",
                    "end_at": "2025-08-24T16:30:00Z",
                    "location": "TBD",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 1}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_43",
        instruction=(
            "Handle a four-stop tour arrangement for client 1 associated with broker 3. Final state: a route for 2025-08-24 is recorded with stops ordered as ['HTX021','HTX025','HTX029','HTX030'] and a map URL 'https://maps.google.com/route/four_stop_c1_20250824'; it successfully meets a 30-minute hop check; a 'likely_buyer' campaign titled 'Aug 2025 Four-Stop Tour — Client 1' is created; an email to client 1 with subject 'Four-Stop Tour — 2025-08-24' and the map URL in the body_uri is documented; and two holds are noted — 09:20-09:30Z titled 'Pre-drive sync' at 'Phone' (source 'follow_up', notes 'Confirm sequence & parking') and 14:00-14:20Z titled 'Tour debrief' at 'Video — Zoom' (source 'follow_up'). Verify by reviewing the route details, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 1,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX021", "HTX025", "HTX029", "HTX030"],
                    "map_url": "https://maps.google.com/route/four_stop_c1_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX021", "HTX025", "HTX029", "HTX030"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Four‑Stop Tour — Client 1",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Four-Stop Tour — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/four_stop_c1_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 1}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:20:00Z",
                    "end_at": "2025-08-24T09:30:00Z",
                    "location": "Phone",
                    "notes": "Confirm sequence & parking",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Tour debrief",
                    "start_at": "2025-08-24T14:00:00Z",
                    "end_at": "2025-08-24T14:20:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 1}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_44",
        instruction=(
            "Organize and send comps for client 14 under the guidance of broker 5. Final state: a comp report is filed for the subject_property_id 'HTX060' (created_by_broker_id 5) with an initial status 'draft', verified through reading, then updated to 'sent_to_client' and re-confirmed; a follow-up hold is scheduled for 2025-08-22 18:30-18:50Z titled 'Discuss comp findings' at 'Phone' (source 'follow_up'). Confirm by reviewing the comp report details after both the save and status update, and by checking the client's calendar events."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 14,
                    "subject_property_id": "HTX060",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "Discuss comp findings",
                    "start_at": "2025-08-22T18:30:00Z",
                    "end_at": "2025-08-22T18:50:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 14}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_45",
        instruction=(
            "Arrange a route day for client 2 under broker 3. Desired outcome: a route for 2025-08-24 is documented with sequential stops ['HTX015','HTX016','HTX017'] and map URL 'https://maps.google.com/route/htx_plan_c2_20250824'; hops adhere to a 30-minute constraint; a 'likely_buyer' campaign called 'Aug 2025 Route Day - Client 2' is active; an email to client 2 with subject 'Route Day Plan - 2025-08-24' and body_uri 'https://test.storage.com/emails/routeday_c2.html' is logged within the campaign; and two reservations exist for client 2 — 08:30-08:45Z labeled 'Kickoff call' at 'Phone' (source 'follow_up') and 13:00-13:20Z labeled 'Post-route debrief' at 'Video - Zoom' (source 'follow_up'). Confirm by reviewing the route details, campaign, email, and calendar events."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX015", "HTX016", "HTX017"],
                    "map_url": "https://maps.google.com/route/htx_plan_c2_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX015", "HTX016", "HTX017"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Route Day - Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "likely_buyer",
                    "client_id": 2,
                    "subject": "Route Day Plan - 2025-08-24",
                    "slug": "routeday_c2",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Route Day Plan - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/routeday_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Kickoff call",
                    "start_at": "2025-08-24T08:30:00Z",
                    "end_at": "2025-08-24T08:45:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Post-route debrief",
                    "start_at": "2025-08-24T13:00:00Z",
                    "end_at": "2025-08-24T13:20:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_46",
        instruction=(
            "Coordinate a Central City two-bed single-family briefing for client 3 with broker 1. Final condition: a draft comp report document exists for subject property ID 'DT_SF2B2B_C3_AUG25' and is accessible; one client update is associated with a campaign titled 'Aug 2025 Central City Fit - Client 3' with subject 'Central City Options' using body URI 'https://test.storage.com/emails/dt_fit_c3.html' and the likely-buyer template; and two calendar holds for 2025-08-24 are established: 10:30-10:50Z 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:20-13:40Z 'Post-tour buffer' at 'Phone' (source 'follow_up'). Ensure by reviewing the comp report, the campaign, the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 3,
                    "subject_property_id": "DT_SF2B2B_C3_AUG25",
                    "created_by_broker_id": 1,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Central City Fit - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Central City Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/dt_fit_c3.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 3}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T10:30:00Z",
                    "end_at": "2025-08-24T10:50:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Post-tour buffer",
                    "start_at": "2025-08-24T13:20:00Z",
                    "end_at": "2025-08-24T13:40:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 3}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_47",
        instruction=(
            "Handle a Medical Center luxury snapshot delivery for client 8 through broker 5. Final result: an inventory overview succinctly displays up to six active listings in neighborhoods [13,9,14,15,11] within the 273024–8688888 price bracket; generate a finance estimate for client 8 using an 800000 target price spread over 30 years in AZ; ensure one client update is linked to a campaign named 'Aug 2025 Med Center Luxury — Client 8' with the subject 'Luxury Snapshot' utilizing 'https://test.storage.com/emails/medcenter_luxury_c8.html' as the body along with the likely-buyer template; and ensure a Zoom consultation on 2025-08-26 from 10:00Z to 10:30Z titled 'Luxury plan consult' is scheduled. Confirm completion by logging the outreach in the email record, the campaign registry, the calendar entry, and the finance estimate."
        ),
        actions=[
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [13, 9, 14, 15, 11],
                    "price_min": 273024,
                    "price_max": 868888,
                    "limit": 6,
                },
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 8,
                    "list_price": 800000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Med Center Luxury — Client 8",
                    "type": "likely_buyer",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 8,
                    "broker_id": 5,
                    "subject": "Luxury Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/medcenter_luxury_c8.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 8}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 8,
                    "title": "Luxury plan consult",
                    "start_at": "2025-08-26T10:00:00Z",
                    "end_at": "2025-08-26T10:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 8}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_48",
        instruction=(
            "Coordinate an expansion of client 4’s condo search under broker 2. Final result: acquire neighborhood 15 details along with neighboring IDs (context); search listings within the precise bordering set provided for property_type 'apartment' and price range 201911–507035 (limit 6) for context; a 'general_update' campaign titled 'Aug 2025 Bordering Apartment Picks — Client 4' should exist and be utilized for sending an email with the subject 'Bordering Options' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/border_apts_c4.html'; schedule a 2025-08-22 15:00–15:30Z hold named 'Pre-tour call' via 'Video — Zoom' (source 'follow_up'). Confirm by reading the records."
        ),
        actions=[
            Action(name="FetchNeighborhood", kwargs={"neighborhood_id": 15}),
            Action(name="ListAdjacentNeighborhoods", kwargs={"neighborhood_id": 15}),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={
                    "neighborhood_ids": [14],
                    "property_type": "apartment",
                    "price_min": 201911,
                    "price_max": 507035,
                    "limit": 6,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Bordering Apartment Picks — Client 4",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Bordering Options",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/border_apts_c4.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 4}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 4,
                    "title": "Pre-tour call",
                    "start_at": "2025-08-22T15:00:00Z",
                    "end_at": "2025-08-22T15:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 4}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_49",
        instruction=(
            "Organize a post-tour follow-up for client 10 together with broker 4. End state: a briefing document is produced; a 'likely_buyer' campaign titled 'Aug 2025 Tour Follow-Ups — Client 10' is created; and an email to client 10 is stored under the new campaign with subject 'Your Tour Follow-Up Packet', template_code 'likely_buyer', and body_uri 'https://test.storage.com/details/client_briefing_010_v1.pdf'. A follow-up calendar hold is secured for client 10 on Saturday 2025-08-23 from 11:30 to 12:00Z, bearing the exact title 'Tour recap', located 'Phone', notes 'Recap post-tour', and labeled 'follow_up'. Verify the writes by reviewing the campaign, the email for client 10, and the calendar event."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc", kwargs={"client_id": 10, "broker_id": 4}
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Tour Follow‑Ups — Client 10",
                    "type": "likely_buyer",
                    "created_by": 4,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Your Tour Follow‑Up Packet",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/details/client_briefing_010_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 10}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 10,
                    "title": "Tour recap",
                    "start_at": "2025-08-23T11:30:00Z",
                    "end_at": "2025-08-23T12:00:00Z",
                    "location": "Phone",
                    "notes": "Recap post‑tour",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 10}),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_50",
        instruction=(
            "Prepare a weekend open-house snapshot for client 4 under broker 2. Final state: open-house windows are retrieved for properties ['HTX030','HTX031'] during 2025-08-23 through 2025-08-24 (context); a 'general_update' campaign titled 'Aug 2025 Weekend Open Houses — Client 4' is in place; an email to client 4 with subject 'Weekend Open Houses' and body_uri 'https://test.storage.com/emails/weekend_open_c4.html' is logged under the campaign; and a planning hold is arranged at 2025-08-23 from 08:30 to 08:45Z with the title 'Plan the route' using 'Phone' (source 'follow_up'). Confirm by reviewing the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="OpenHousesForProperties",
                kwargs={
                    "property_ids": ["HTX030", "HTX031"],
                    "date_from": "2025-08-23",
                    "date_to": "2025-08-24",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Weekend Open Houses — Client 4",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Weekend Open Houses",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_open_c4.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 4}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 4,
                    "title": "Plan the route",
                    "start_at": "2025-08-23T08:30:00Z",
                    "end_at": "2025-08-23T08:45:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 4}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_51",
        instruction=(
            "Handle the post-tour recap delivery for client 3 under broker 1. Final requirement: generate a briefing document (version 'aug25') and reference it in an email under the campaign called 'Aug 2025 Tour Recap — Client 3' with the subject 'Tour Recap & Next Steps' (template 'general_update') and access body URI 'https://test.storage.com/details/client_briefing_003_aug25.pdf'; ensure a draft comp report for 'TOUR_RECAP_C3_AUG25' is saved and accessible; notate an audit event 'recap_sent' on that comp report and confirm it has been viewed; and schedule a follow-up phone meeting on 2025-08-29 from 09:10Z to 09:30Z titled 'Recap call' (source 'follow_up') on the calendar. Confirm all through comp report checking, campaign/email, and calendar entries."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc",
                kwargs={"client_id": 3, "broker_id": 1, "version_tag": "aug25"},
            ),
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 3,
                    "subject_property_id": "TOUR_RECAP_C3_AUG25",
                    "created_by_broker_id": 1,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Tour Recap — Client 3",
                    "type": "general_update",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Tour Recap & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_003_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 3}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 1,
                    "action": "recap_sent",
                    "entity_type": "comp_reports",
                    "entity_id": 9,
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Recap call",
                    "start_at": "2025-08-29T09:10:00Z",
                    "end_at": "2025-08-29T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 3}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_52",
        instruction=(
            "Coordinate the delivery of a comps-and-status package for client 6 under broker 2. Desired outcome: a comp report for subject_property_id 'HTX058' (created_by_broker_id 2) is saved with a 'draft' status and verified; its status then changes to 'sent_to_client' and is re-verified; a 'likely_buyer' campaign titled 'Aug 2025 Comps Sent — Client 6' is in place; there is an email to client 6 using the template_code 'likely_buyer' with the subject 'Comps Sent' and body_uri 'https://test.storage.com/emails/comps_sent_c6.html' recorded under this campaign; and a meeting hold on 2025-08-22 from 18:40 to 19:00Z titled 'Comps debrief' via 'Phone' (source 'follow_up') is prepared."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 6,
                    "subject_property_id": "HTX058",
                    "created_by_broker_id": 2,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Comps Sent — Client 6",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Comps Sent",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comps_sent_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 6}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Comps debrief",
                    "start_at": "2025-08-22T18:40:00Z",
                    "end_at": "2025-08-22T19:00:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 6}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_53",
        instruction=(
            "Arrange an open-house tour for client 3 with broker 1. Desired outcome: a 'likely_buyer' campaign is established with the name 'Aug 2025 Open House — Client 3'; the route scheduled for 2025-08-24 is documented with the precise sequence of stops ['HTX001','HTX004','HTX005'] and the map URL 'https://maps.google.com/route/htx_003_20250824'; ensure drive-time feasibility does not exceed 30 minutes per segment. Register one email for client 3 from broker 1 under the newly created campaign featuring the subject 'Open House Route — 2025-08-24' and body_uri 'https://maps.google.com/route/htx_003_20250824'. Facilitate two calendar reservations for client 3 on 2025-08-24: 10:00-10:30Z marked 'Depart for first stop' (location 'Client Home', notes 'Open-house tour', source 'viewing') and 13:00-13:30Z marked 'Broker follow-up' (location 'Office', notes 'Post-tour recap', source 'follow_up'). Confirm the entries by reviewing the campaign, stored route specifics, the email, and calendar appointments; additionally, log audits for both the campaign initiation and the saved route."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Open House — Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 3,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/htx_003_20250824",
                    "created_by_broker_id": 1,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Open House Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/htx_003_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 3}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-24T10:00:00Z",
                    "end_at": "2025-08-24T10:30:00Z",
                    "location": "Client Home",
                    "notes": "Open-house tour",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Broker follow-up",
                    "start_at": "2025-08-24T13:00:00Z",
                    "end_at": "2025-08-24T13:30:00Z",
                    "location": "Office",
                    "notes": "Post-tour recap",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 3}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 1,
                    "action": "campaign_created",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                    "metadata_json": {
                        "name": "Aug 2025 Open House — Client 3",
                        "type": "likely_buyer",
                    },
                },
            ),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 1,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": ["HTX001", "HTX004", "HTX005"],
                        "map_url": "https://maps.google.com/route/htx_003_20250824",
                    },
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_54",
        instruction=(
            "Coordinate paired likely-buyer updates for clients 1 and 2 with broker 3. Target state: search_listings align with each client’s preferred neighborhoods (client 1: [5,9,8,10,14], client 2: [11,1]) each capped at 6 for context; a 'likely_buyer' campaign titled 'Aug 2025 Paired Likely Buyers — C1 & C2' is present and serves two emails (subject 'August Listings Shortlist', template_code 'likely_buyer', body_uri 'https://test.storage.com/emails/aug_shortlist.html'); schedule two holds on 2025-08-23 titled 'Intro call about shortlist' over 'Phone' (source 'follow_up'): client 1 at 15:00-15:30Z and client 2 at 16:00-16:20Z. Verify through reviewing campaign details, emails, and both calendar entries."
        ),
        actions=[
            Action(
                name="QueryActiveListings",
                kwargs={"neighborhood_ids": [5, 9, 8, 10, 14], "limit": 6},
            ),
            Action(
                name="QueryActiveListings",
                kwargs={"neighborhood_ids": [11, 1], "limit": 6},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Paired Likely Buyers — C1 & C2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/aug_shortlist.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/aug_shortlist.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 1}),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-23T15:00:00Z",
                    "end_at": "2025-08-23T15:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Intro call about shortlist",
                    "start_at": "2025-08-23T16:00:00Z",
                    "end_at": "2025-08-23T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 1}),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_55",
        instruction=(
            "Handle a preference-targeted notification for client 3 overseen by broker 1. Final state: client 3's stored preferences have been referred to and the property search matches those filters precisely—neighborhoods [1,12,2,4,5], price 200505–631914, beds=2, baths=2 (context); a 'likely_buyer' campaign titled 'Aug 2025 Targeted Listings - Client 3' is active and the outbound message is cataloged under it; one email is present for client 3 with subject 'Tailored Listings Update' and body_uri 'https://test.storage.com/emails/prefs_c3.html'; and a follow-up hold is scheduled for 2025-08-23 17:00–17:20Z titled 'Listings check-CO' via 'Phone' with source 'follow_up'."
        ),
        actions=[
            Action(name="FetchClientPrefs", kwargs={"client_id": 3}),
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [1, 12, 2, 4, 5],
                    "price_min": 200505,
                    "price_max": 631914,
                    "beds": 2,
                    "baths": 2,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Targeted Listings - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Tailored Listings Update",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/prefs_c3.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 3}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Listings check-CO",
                    "start_at": "2025-08-23T17:00:00Z",
                    "end_at": "2025-08-23T17:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 3}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_56",
        instruction=(
            "Coordinate a dual-client general briefing for clients 13 and 14 within the jurisdiction of broker 5. Final state: a listings context inquiry executes for neighborhoods [2,3,4], with a maximum of 6 results (limit 6); a 'general_update' campaign titled 'Aug 2025 Multi-Client Update — C13 & C14' exists; two emails are logged — each with subject 'August Market & Listings' and body_uri 'https://test.storage.com/emails/aug_market_multi.html' — one for client 13 and the other for client 14, both linked to the same campaign; and two holds are established on 2025-08-22: client 13 at 16:00–16:20Z and client 14 at 16:30–16:50Z, both marked 'Discuss August update' via 'Phone' (source 'follow_up'). Verify by reviewing the campaign, the emails for both clients, and the calendar events for both clients."
        ),
        actions=[
            Action(
                name="QueryActiveListings",
                kwargs={"neighborhood_ids": [2, 3, 4], "limit": 6},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Multi‑Client Update — C13 & C14",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "August Market & Listings",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/aug_market_multi.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "August Market & Listings",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/aug_market_multi.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 13}),
            Action(name="ListClientEmails", kwargs={"client_id": 14}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 13,
                    "title": "Discuss August update",
                    "start_at": "2025-08-22T16:00:00Z",
                    "end_at": "2025-08-22T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "Discuss August update",
                    "start_at": "2025-08-22T16:30:00Z",
                    "end_at": "2025-08-22T16:50:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 13}),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 14}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_57",
        instruction=(
            "Handle a Central City/Uptown statistics update for client 1 under broker 1. Final outcome: a 'general_update' campaign titled 'Aug 2025 DT/Uptown Stats — Client 1' is established and utilized for a single email to client 1 with subject 'DT/Uptown Q3 Snapshot' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/dt_mid_q3_c1.html'; a follow-up hold is scheduled on 2025-08-25 09:00–09:30Z with the title 'Follow-up Check-CO — DT/Uptown' via 'Phone' (source 'follow_up'); an audit 'campaign_sent' is recorded on the campaign and the campaign is examined to confirm state."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 DT/Uptown Stats — Client 1",
                    "type": "general_update",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "DT/Uptown Q3 Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/dt_mid_q3_c1.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 1}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 1,
                    "title": "Follow-up Check-CO — DT/Uptown",
                    "start_at": "2025-08-25T09:00:00Z",
                    "end_at": "2025-08-25T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 1}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 1,
                    "action": "campaign_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_58",
        instruction=(
            "Coordinate the creation of an evening Uptown route for client 9 under broker 2. Final situation: a route dated 2025-08-24 with organized stops ['HTX021','HTX025','HTX030'] and map 'https://maps.google.com/route/midtown_evening_c9_20250824' is stored and checked; hops do not exceed 30 minutes; a 'likely_buyer' campaign named 'Aug 2025 Uptown Evening — Client 9' is devised and used for a single email with subject 'Evening Route — Uptown' (template_code 'likely_buyer') with that map URL as body_uri; a 09:30–09:45Z pre-drive sync hold via 'Phone' (source 'follow_up') is set up; audit 'routes_shared_and_viewings_set' is documented and route re-evaluated."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX021", "HTX025", "HTX030"],
                    "map_url": "https://maps.google.com/route/midtown_evening_c9_20250824",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX021", "HTX025", "HTX030"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Uptown Evening — Client 9",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Evening Route — Uptown",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/midtown_evening_c9_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 9,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:30:00Z",
                    "end_at": "2025-08-24T09:45:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 9}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 2,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_59",
        instruction=(
            "Coordinate a Sunday drive for client 3 under broker 1 using open-house windows (context) for properties HTX001, HTX004, and HTX005 spanning 2025-08-22 to 2025-08-25. By the end, ensure a route dated 2025-08-24 for these three properties is documented with a shareable map link and that it complies with the 30-minute hop limit. An active 'likely_buyer' campaign titled 'Aug 2025 Sunday Drive - Client 3' is required, along with a single notification email to client 3 with the subject 'Sunday Drive Plan - 2025-08-24' which includes the map link. Schedule a brief pre-drive check-CO to occur that morning on the calendar (source 'follow_up'). Ensure the resulting state can be validated via ensuing reads."
        ),
        actions=[
            Action(
                name="OpenHousesForProperties",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "date_from": "2025-08-22",
                    "date_to": "2025-08-25",
                },
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 3,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/htx_c3_sunday_20250824",
                    "created_by_broker_id": 1,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Sunday Drive - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "likely_buyer",
                    "client_id": 3,
                    "subject": "Sunday Drive Plan - 2025-08-24",
                    "slug": "sunday_c3",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Sunday Drive Plan - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/sunday_c3.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 3}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Pre-drive check-CO",
                    "start_at": "2025-08-24T09:45:00Z",
                    "end_at": "2025-08-24T10:00:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 3}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_60",
        instruction=(
            "Handle the creation of a curated shortlist by ID for client 11 under broker 6. Final state: listings [15,16,17] are accessed with property details (context); ensure a 'likely_buyer' campaign named 'Aug 2025 Curated Picks — Client 11' is established and used for a single email titled 'Handpicked Listings' (template_code 'likely_buyer') with body_uri 'https://test.storage.com/emails/curated_picks_c11.html'; schedule a hold for 2025-08-24, 11:10–11:30Z, titled 'Curated picks debrief' via 'Phone' (source 'follow_up'). Confirm by reads."
        ),
        actions=[
            Action(
                name="GatherListingsWithProperties",
                kwargs={"listing_ids": [15, 16, 17]},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Curated Picks — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Handpicked Listings",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/curated_picks_c11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 11}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Curated picks debrief",
                    "start_at": "2025-08-24T11:10:00Z",
                    "end_at": "2025-08-24T11:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_61",
        instruction=(
            "Expand search guidance for client 2 under broker 3 using areas adjacent to neighborhood 1. Upon completion: neighborhood 1 and its adjacent neighborhood IDs are documented; the context of listings reflects results derived solely from these adjacent IDs with a price range of 300000–650000, beds=2, baths=2, and a limit of 6; a 'general_update' campaign named 'Aug 2025 Bordering Preview — Client 2' is recorded; one message to client 2 exists with the subject 'Bordering Area Shortlist' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/border_prev_c2.html'; and a follow-up calendar hold is set for 2025-08-22 16:00–16:20Z titled 'Bordering shortlist review' at 'Phone' (source 'follow_up'). The outcome is verifiable in campaign, email, and client calendar records."
        ),
        actions=[
            Action(name="FetchNeighborhood", kwargs={"neighborhood_id": 1}),
            Action(name="ListAdjacentNeighborhoods", kwargs={"neighborhood_id": 1}),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={
                    "neighborhood_ids": [2],
                    "price_min": 300000,
                    "price_max": 650000,
                    "beds": 2,
                    "baths": 2,
                    "limit": 6,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Bordering Preview — Client 2",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Area Shortlist",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/border_prev_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Bordering shortlist review",
                    "start_at": "2025-08-22T16:00:00Z",
                    "end_at": "2025-08-22T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_62",
        instruction=(
            "Dispatch a general market update to clients 1 and 2 from broker 3. Ensure the final result includes: a 'general_update' campaign named 'Aug 2025 General Update — Central City & Uptown' which is utilized for both emails; a context listing pull of up to 8 active listings with no further filters (limit 8); two emails dispatched to clients 1 and 2 with the subject 'Q3 Stats & Listings — Central City & Uptown' and body_uri 'https://test.storage.com/emails/q3_stats_dt_midtown.html'; and two follow-up holds on 2025-08-23 titled 'Discuss Q3 market update' at 'Video — Zoom' with notes 'Market update follow-up' (client 1 at 15:00–15:30Z, client 2 at 16:30–17:00Z)."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 General Update — Central City & Uptown",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="QueryActiveListings", kwargs={"limit": 8}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Q3 Stats & Listings — Central City & Uptown",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/q3_stats_dt_midtown.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Q3 Stats & Listings — Central City & Uptown",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/q3_stats_dt_midtown.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 1}),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 1,
                    "title": "Discuss Q3 market update",
                    "start_at": "2025-08-23T15:00:00Z",
                    "end_at": "2025-08-23T15:30:00Z",
                    "location": "Video — Zoom",
                    "notes": "Market update follow‑up",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Discuss Q3 market update",
                    "start_at": "2025-08-23T16:30:00Z",
                    "end_at": "2025-08-23T17:00:00Z",
                    "location": "Video — Zoom",
                    "notes": "Market update follow‑up",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 1}),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_63",
        instruction=(
            "Handle the creation of a finance-first briefing for client 13 in collaboration with broker 7. Ensure the system displays: retrieval of the client's mortgage profile; extraction of three recent sales for context concerning property_id 'HTX003' (limit 3); an expansive active search conducted (limit 6); and a 'likely_buyer' campaign titled 'Aug 2025 Finance-First — Client 13' is active with an email to client 13 having the subject 'Finance-First Plan & Options', template_code 'likely_buyer', and body_uri 'https://test.storage.com/emails/finance_first_client_13.html'. A consultation hold is in place for client 13 on 2025-08-26 18:00-18:30Z with the explicit title 'Financing consult', location 'Video — Teams', notes 'Finance-first plan', and source 'client_meeting'."
        ),
        actions=[
            Action(name="RetrieveMortgageProfile", kwargs={"client_id": 13}),
            Action(
                name="RecentSalesForProperty",
                kwargs={"property_id": "HTX003", "limit": 3},
            ),
            Action(name="QueryActiveListings", kwargs={"limit": 6}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Finance‑First — Client 13",
                    "type": "likely_buyer",
                    "created_by": 7,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 13,
                    "broker_id": 7,
                    "subject": "Finance‑First Plan & Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/finance_first_client_13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 13}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 7,
                    "client_id": 13,
                    "title": "Financing consult",
                    "start_at": "2025-08-26T18:00:00Z",
                    "end_at": "2025-08-26T18:30:00Z",
                    "location": "Video — Teams",
                    "notes": "Finance-first plan",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 13}),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_64",
        instruction=(
            "Coordinate the finalization and dispatch of a comps report for client 13 working with broker 5. Completion requirements: save a comps report for 'HTX025' as 'draft' and review it; update status to 'sent_to_client' and review again; initiate a 'general_update' campaign named 'Aug 2025 Comps Final — Client 13' involving one email with the subject 'Your Comps Report' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/comps_final_c13.html'; a debrief hold is scheduled for 2025-08-26 09:00-09:20Z titled 'Comps debrief' at 'USNV Strickland, FPO AP 98640' (source 'client_meeting'). Confirm through reads."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 13,
                    "subject_property_id": "HTX025",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Comps Final — Client 13",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "Your Comps Report",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/comps_final_c13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 13}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 13,
                    "title": "Comps debrief",
                    "start_at": "2025-08-26T09:00:00Z",
                    "end_at": "2025-08-26T09:20:00Z",
                    "location": "USNV Strickland, FPO AP 98640",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 13}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_65",
        instruction=(
            "Coordinate the finalization of a weekend open‑house plan for client 12 under broker 3 using properties ['HTX310','HTX318'] for 2025‑08‑23 to 2025‑08‑24. Finalize by ensuring the window set is reviewed; a campaign titled 'Aug 2025 Open‑House Weekend — Client 12' is created and used to send one email with subject 'Your Open House Plan' (template 'general_update') and body URI 'https://test.storage.com/emails/openhouse_plan_c12.html'; and schedule an 'Open‑house kickoff' hold on 2025-08-23 from 10:00Z to 10:20Z at 'Client Home' (source 'viewing') on the calendar. Validate through the campaign/email and the calendar."
        ),
        actions=[
            Action(
                name="OpenHousesForProperties",
                kwargs={
                    "property_ids": ["HTX310", "HTX318"],
                    "date_from": "2025-08-23",
                    "date_to": "2025-08-24",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Open‑House Weekend — Client 12",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Your Open House Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/openhouse_plan_c12.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 12}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Open-house kickoff",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:20:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 12}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_66",
        instruction=(
            "Conduct a new-homeowner touch for client 14 under broker 5. Required outcome: a 'new_homeowner' campaign titled 'Aug 2025 New Homeowner - Client 14' is established; log an email to client 14 under the campaign with subject 'Congrats & Checklist' and body_uri 'https://test.storage.com/emails/newhome_c14.html'; and arrange a check-CO hold for 2025-08-25 16:00-16:20Z called 'New homeowner check-CO' at 'Phone' (source 'follow_up'). Confirm by verifying the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 New Homeowner - Client 14",
                    "type": "new_homeowner",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "new_homeowner",
                    "client_id": 14,
                    "subject": "Congrats & Checklist",
                    "slug": "newhome_c14",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "Congrats & Checklist",
                    "template_code": "new_homeowner",
                    "body_uri": "https://test.storage.com/emails/newhome_c14.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 14}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "New homeowner check-CO",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 14}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_67",
        instruction=(
            "Handle finalizing a Central City luxury finance and confirm the route for client 9 under broker 9. End state: calculate a mortgage estimate for client 9 at list_price 750000 (term_years 30, region 'AZ') as context; a route dated 2025-08-24 with stops ['HTX036','HTX032','HTX049'] and map 'https://maps.google.com/route/dt_lux_finance_c9_20250824' is retained and passes a ≤30-minute hop check; establish a 'general_update' campaign named 'Aug 2025 DT Luxury Finance — Client 9' to send two emails under that campaign: one to client 9 with subject 'Luxury Finance Snapshot' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/dt_lux_finance_c9.html', and another to client 9 with subject 'Route Confirm — 2025-08-24' (template_code 'general_update') using the map URL as body_uri; log audit 'routes_shared_and_viewings_set' on the route and check the route again. Verify with reads."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 9,
                    "list_price": 750000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX036", "HTX032", "HTX049"],
                    "map_url": "https://maps.google.com/route/dt_lux_finance_c9_20250824",
                    "created_by_broker_id": 9,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX036", "HTX032", "HTX049"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 DT Luxury Finance — Client 9",
                    "type": "general_update",
                    "created_by": 9,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Luxury Finance Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/dt_lux_finance_c9.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Route Confirm — 2025-08-24",
                    "template_code": "general_update",
                    "body_uri": "https://maps.google.com/route/dt_lux_finance_c9_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 9}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 9,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_68",
        instruction=(
            "Coordinate the provision of regional financing guidance for client 17 under broker 10. End state: calculate a mortgage estimate for client 17 at list_price 650000 with term_years 30 and region 'CA-SF' (context); ensure a 'general_update' campaign named 'Aug 2025 SF Financing — Client 17' is in place; document an email to client 17 using template_code 'general_update' with subject 'San Francisco Financing Snapshot' and body_uri 'https://test.storage.com/emails/finance_sf_c17.html' under the campaign; and set a consult hold for 2025‑08‑22 22:00–22:30Z titled 'Financing consult (SF)' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 17,
                    "list_price": 650000,
                    "term_years": 30,
                    "region": "CA-SF",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 SF Financing — Client 17",
                    "type": "general_update",
                    "created_by": 10,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "San Francisco Financing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_sf_c17.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 17}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 10,
                    "client_id": 17,
                    "title": "Financing consult (SF)",
                    "start_at": "2025-08-22T22:00:00Z",
                    "end_at": "2025-08-22T22:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 17}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_69",
        instruction=(
            "Handle the preparation and dispatch of a Heights CMA to client 5 under broker 5. Final outcome: a draft comp report for subject 'HEIGHTS_HTX012_C5_AUG25' is saved, readable, updated to 'sent_to_client,' and reviewed again; a campaign titled 'Aug 2025 Heights Listing CMA — Client 5' exists, dispatching an email with subject 'CMA for HTX012' (template 'general_update') and body URI 'https://test.storage.com/emails/cma_htx012_c5.html'; and a follow-up hold scheduled on 2025-08-24 from 15:00Z to 15:20Z titled 'CMA questions' at 'Phone' (source 'follow_up') is marked on the calendar. Confirm with the comp report reads, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 5,
                    "subject_property_id": "HEIGHTS_HTX012_C5_AUG25",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="SetCompReportStatus",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Heights Listing CMA — Client 5",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "CMA for HTX012",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/cma_htx012_c5.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "CMA questions",
                    "start_at": "2025-08-24T15:00:00Z",
                    "end_at": "2025-08-24T15:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_70",
        instruction=(
            "Coordinate the delivery of investor options to client 18 under broker 5. The end result: condos in neighborhoods [3,4] priced between 300000 and 650000 have been investigated (context); a mortgage estimate for client 18 is calculated at list_price 400000 (context); a 'general_update' campaign titled 'Aug 2025 Investor Picks - Client 18' is set up; a single email for client 18 exists with subject 'Investor Picks & Financing' and body_uri 'https://test.storage.com/emails/investor_c18.html' linked to that campaign; and a review hold is in place for 2025-08-24 19:00 to 19:30Z titled 'Investor review' at 'Video - Zoom' with source 'follow_up'."
        ),
        actions=[
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [3, 4],
                    "property_type": "condo",
                    "price_min": 300000,
                    "price_max": 650000,
                },
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 18, "list_price": 400000},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Investor Picks - Client 18",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 18,
                    "subject": "Investor Picks & Financing",
                    "slug": "investor_c18",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Investor Picks & Financing",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/investor_c18.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 18}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Investor review",
                    "start_at": "2025-08-24T19:00:00Z",
                    "end_at": "2025-08-24T19:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 18}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_71",
        instruction=(
            "Manage client 9 with broker 9. The desired system outcome should be as follows: a 'likely_buyer' campaign labeled 'Aug 2025 Likely Buyer — Client 9 Comp Pack' is present, and every email sent for this task is registered under the ID generated during creation (do not assume a fixed ID). Utilizing the client's areas [1, 12, 14, 3] and the price range 276667–628429, retrieve up to 6 current context listings for reference (maximum 6). Document two emails for client 9 from broker 9 within that campaign using template_code 'likely_buyer' and body_uri 'https://test.storage.com/emails/comp_pack_client_9.html', with the exact subject lines 'Comp Pack Draft — Client 9' and 'Your Comparable & Payment Plan'. Furthermore, a calendar appointment is scheduled for client 9 with the title 'Review comparable & payment plan' on 2025‑08‑21 from 15:00–15:30Z, located at 'Video — Teams', containing notes '30‑min review of comp pack', and originating from 'client_meeting'. Validate the entries by rechecking the campaign, emails, and the calendar event for client 9."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Likely Buyer — Client 9 Comp Pack",
                    "type": "likely_buyer",
                    "created_by": 9,
                },
            ),
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [1, 12, 14, 3],
                    "price_min": 276667,
                    "price_max": 628429,
                    "limit": 6,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Comp Pack Draft — Client 9",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comp_pack_client_9.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Your Comparable & Payment Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comp_pack_client_9.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 9,
                    "client_id": 9,
                    "title": "Review comparable & payment plan",
                    "start_at": "2025-08-21T15:00:00Z",
                    "end_at": "2025-08-21T15:30:00Z",
                    "location": "Video — Teams",
                    "notes": "30‑min review of comp pack",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 9}),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_72",
        instruction=(
            "Facilitate the distribution of seller disclosures to client 5 through broker 5. Final outcome: a briefing document (version 'disclosures_aug25') is created and referenced; a campaign named 'Aug 2025 Disclosures — Client 5' is available and dispatches an email with subject 'Seller Disclosures' (template 'general_update') using the briefing URI; and a follow‑up call scheduled for 2025-08-23 from 12:10Z to 12:30Z titled 'Disclosure Q&A' at 'Phone' (source 'follow_up') is registered on the calendar. Confirm through campaign verification, email log, and calendar review."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "version_tag": "disclosures_aug25",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Disclosures — Client 5",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Seller Disclosures",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_005_disclosures_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 5,
                    "title": "Disclosure Q&A",
                    "start_at": "2025-08-23T12:10:00Z",
                    "end_at": "2025-08-23T12:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_73",
        instruction=(
            "Handle the preparation and distribution of a duplex shortlist for client 6 with the involvement of broker 2. End state: a documented snapshot for property ID 'DPLX_C6_AUG25' is saved in draft status and remains accessible; a maximum of six listings view depicts active duplex options across neighborhoods [8,12,6,5] within 147021-402736 for contextual purposes; a single client interaction is recorded under the campaign 'Aug 2025 Duplex Shortlist - Client 6' with the subject 'Duplexes That Fit' incorporating body URI 'https://test.storage.com/emails/duplex_shortlist_c6.html' and the likely-buyer template; along with a phone follow-up scheduled for 2025-08-23 from 18:40Z to 19:00Z titled 'Shortlist debrief' (source 'follow_up') entered in the client’s calendar. Validate through the saved snapshot, campaign record, client’s email entry, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 6,
                    "subject_property_id": "DPLX_C6_AUG25",
                    "created_by_broker_id": 2,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [8, 12, 6, 5],
                    "property_type": "duplex",
                    "price_min": 147021,
                    "price_max": 402736,
                    "limit": 6,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Duplex Shortlist - Client 6",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Duplexes That Fit",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/duplex_shortlist_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 6}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Shortlist debrief",
                    "start_at": "2025-08-23T18:40:00Z",
                    "end_at": "2025-08-23T19:00:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 6}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_74",
        instruction=(
            "Coordinate an Inner Loop viewing day for client 16 in collaboration with broker 8. End state: review of open-house times in neighborhoods [7,11,6] is completed; a three-stop itinerary for client 16 set on 2025-08-31 listing stops ['HTX716','HTX722','HTX731'] with map link 'https://maps.example.com/route/c16_aug31' stored as stated; the itinerary is legible; drive-time feasibility holds within a 30-minute limit; a campaign 'Aug 2025 Viewing Day — Client 16' is established sending a single email 'Route & Open House Plan' (template 'general_update') using 'https://test.storage.com/emails/viewing_day_c16.html'; plus, an initial viewing hold arranged on 2025-08-31 from 09:15Z to 09:35Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') is listed in the calendar. Confirm through route specifics, drive-time validation, associated campaign/email, and calendar synchronization."
        ),
        actions=[
            Action(
                name="OpenHouseWindowsByNeighborhoods",
                kwargs={"neighborhood_ids": [7, 11, 6]},
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 16,
                    "date": "2025-08-31",
                    "stops_ordered_json": ["HTX716", "HTX722", "HTX731"],
                    "map_url": "https://maps.example.com/route/c16_aug31",
                    "created_by_broker_id": 8,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX716", "HTX722", "HTX731"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Viewing Day — Client 16",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Route & Open House Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/viewing_day_c16.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 16}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 8,
                    "client_id": 16,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-31T09:15:00Z",
                    "end_at": "2025-08-31T09:35:00Z",
                    "location": "Client Home",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 16}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_75",
        instruction=(
            "Coordinate the completion of a museum-area townhouse tour for client 12 with broker 3, ensuring seller-broker drafts are prepared. End state: a route for 2025-08-25 with ordered stops ['HTX044','HTX036','HTX032'] and map 'https://maps.google.com/route/museum_townhouse_c12_20250825' is saved and checked; the drive-time feasibility is validated at ≤30 minutes; drafts bundle is created for property_ids ['HTX044','HTX036','HTX032']; a 'likely_buyer' campaign named 'Aug 2025 Townhouse Tour — Client 12' is established and used to send one email to client 12 with subject 'Townhouse Tour Plan' (template_code 'likely_buyer') and body_uri 'https://maps.google.com/route/museum_townhouse_c12_20250825'; schedule a same-day hold from 13:30–13:45Z titled 'Pre-tour sync' at 'Phone' (source 'follow_up'); ensure audit 'routes_shared_and_viewings_set' is posted on the route and reread the route."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 12,
                    "date": "2025-08-25",
                    "stops_ordered_json": ["HTX044", "HTX036", "HTX032"],
                    "map_url": "https://maps.google.com/route/museum_townhouse_c12_20250825",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX044", "HTX036", "HTX032"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="DraftSellerBrokerBatch",
                kwargs={
                    "client_id": 12,
                    "property_ids": ["HTX044", "HTX036", "HTX032"],
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Townhouse Tour — Client 12",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/museum_townhouse_c12_20250825",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 12}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Pre-tour sync",
                    "start_at": "2025-08-25T13:30:00Z",
                    "end_at": "2025-08-25T13:45:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 12}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 3,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_76",
        instruction=(
            "Handle the presentation of financing scenarios for client 10 through broker 4 at target prices of 650000 and 820000 (30‑year AZ). End state: both calculations are completed; a campaign titled 'Aug 2025 Financing Scenarios — Client 10' is active and dispatches one email with subject 'Two Financing Scenarios' (template 'general_update') and body URI 'https://test.storage.com/emails/finance_scenarios_c10.html'; a client‑meeting hold on 2025-08-25 from 20:10Z to 20:40Z titled 'Financing consult' at 'Video — Zoom' (source 'client_meeting') is recorded on the calendar. Confirm via the campaign/email and the calendar."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 10,
                    "list_price": 650000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 10,
                    "list_price": 820000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Financing Scenarios — Client 10",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Two Financing Scenarios",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_scenarios_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 10}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 4,
                    "client_id": 10,
                    "title": "Financing consult",
                    "start_at": "2025-08-25T20:10:00Z",
                    "end_at": "2025-08-25T20:40:00Z",
                    "location": "Video — Zoom",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 10}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_77",
        instruction=(
            "Handle a Saturday open-house drive for client 5 under broker 1. Final state: Retrieve open-house windows for properties ['HTX021','HTX024','HTX025'] from 2025‑08‑22 to 2025‑08‑24 (context); Record a route dated 2025‑08‑23 with ordered stops ['HTX021','HTX024','HTX025'] and map URL 'https://maps.google.com/route/oh_c5_20250823'; Confirm drive-time feasibility does not exceed 30 minutes per hop; Ensure a 'likely_buyer' campaign named 'Aug 2025 Open Houses — Client 5' is available; Document one email to client 5 with the subject 'Saturday Open-House Route' using the map URL as body_uri under the campaign; Schedule two holds for 2025‑08‑23 — 09:50–10:00Z titled 'Depart for first stop' at 'Client Home' (source 'viewing', notes 'Leave buffer for parking') and 13:30–13:50Z titled 'Post-tour recap' at 'Phone' (source 'follow_up', notes 'Discuss favorites & next steps'). Validate by reviewing the campaign, the stored route, the email, and calendar events; also log an audit for the constructed route."
        ),
        actions=[
            Action(
                name="OpenHousesForProperties",
                kwargs={
                    "property_ids": ["HTX021", "HTX024", "HTX025"],
                    "date_from": "2025-08-22",
                    "date_to": "2025-08-24",
                },
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 5,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX021", "HTX024", "HTX025"],
                    "map_url": "https://maps.google.com/route/oh_c5_20250823",
                    "created_by_broker_id": 1,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX021", "HTX024", "HTX025"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Open Houses — Client 5",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Saturday Open-House Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/oh_c5_20250823",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 5,
                    "title": "Depart for first stop",
                    "start_at": "2025-08-23T09:50:00Z",
                    "end_at": "2025-08-23T10:00:00Z",
                    "location": "Client Home",
                    "notes": "Leave buffer for parking",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 1,
                    "client_id": 5,
                    "title": "Post-tour recap",
                    "start_at": "2025-08-23T13:30:00Z",
                    "end_at": "2025-08-23T13:50:00Z",
                    "location": "Phone",
                    "notes": "Discuss favorites & next steps",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 1,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": ["HTX021", "HTX024", "HTX025"],
                        "map_url": "https://maps.google.com/route/oh_c5_20250823",
                    },
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_78",
        instruction=(
            "Coordinate a Desert Ridge luxury route for client 18 with broker 5. End state: Save and review a route dated 2025-08-24 with stops ['HTX018','HTX032','HTX025'] and map 'https://maps.google.com/route/riveroaks_lux_c18_20250824'; Confirm hop feasibility within 30 minutes; Ensure a 'likely_buyer' campaign named 'Aug 2025 Desert Ridge Luxury — Client 18' is available and used for one email with subject 'Luxury Viewing Route' (template_code 'likely_buyer') and the map URL as body_uri; Establish an 11:10–11:20Z 'Pre-drive sync' hold at 'Phone' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 18,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX018", "HTX032", "HTX025"],
                    "map_url": "https://maps.google.com/route/riveroaks_lux_c18_20250824",
                    "created_by_broker_id": 5,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX018", "HTX032", "HTX025"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Desert Ridge Luxury — Client 18",
                    "type": "likely_buyer",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Luxury Viewing Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/riveroaks_lux_c18_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 18}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T11:10:00Z",
                    "end_at": "2025-08-24T11:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 18}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_79",
        instruction=(
            "Handle the delivery of two contrast CMAs for client 22 under broker 9. End state: two draft comp reports should exist and be readable—subjects 'RICE_MIL_C22_AUG25_A' and 'MIDTOWN_C22_AUG25_B'; a campaign titled 'Aug 2025 Two-CMA Contrast — Client 22' should be available and utilized to send one email with subject 'Two CMA Snapshots' (template 'general_update') and body URI 'https://test.storage.com/emails/two_cma_c22.html'; and a follow-up Zoom hold on 2025-08-26 from 11:30Z to 11:50Z titled 'CMA contrast debrief' (source 'follow_up') should appear on the calendar. Validate by both comp report reads, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 22,
                    "subject_property_id": "RICE_MIL_C22_AUG25_A",
                    "created_by_broker_id": 9,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 22,
                    "subject_property_id": "MIDTOWN_C22_AUG25_B",
                    "created_by_broker_id": 9,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 10}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Two‑CMA Contrast — Client 22",
                    "type": "general_update",
                    "created_by": 9,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 22,
                    "broker_id": 9,
                    "subject": "Two CMA Snapshots",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/two_cma_c22.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 22}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 9,
                    "client_id": 22,
                    "title": "CMA contrast debrief",
                    "start_at": "2025-08-26T11:30:00Z",
                    "end_at": "2025-08-26T11:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 22}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_80",
        instruction=(
            "Coordinate a micro-tour setup for client 7 under broker 15. End state: a route for 2025-08-28 with stops ['HTX036','HTX035'] and map 'https://maps.google.com/route/eado_microtour_c7_20250828' should be saved/read; hops should not exceed 30 minutes; a 'likely_buyer' campaign named 'Aug 2025 SoDo Micro-Tour — Client 7' should exist and be used for one email with subject 'Micro-Tour Plan' (template_code 'likely_buyer') and body_uri 'https://maps.google.com/route/eado_microtour_c7_20250828'; a 16:00–17:00Z 'Contract Review - Mr. Sean Hardy' hold at '5033 Parker Keys Suite 325, Old Williamsburg, VT 03979' (source 'client_meeting') should be on the calendar. Confirm via reads."
        ),
        actions=[
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 7,
                    "date": "2025-08-28",
                    "stops_ordered_json": ["HTX036", "HTX035"],
                    "map_url": "https://maps.google.com/route/eado_microtour_c7_20250828",
                    "created_by_broker_id": 15,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={"property_ids": ["HTX036", "HTX035"], "max_minutes": 30},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 SoDo Micro-Tour — Client 7",
                    "type": "likely_buyer",
                    "created_by": 15,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 7,
                    "broker_id": 15,
                    "subject": "Micro-Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/eado_microtour_c7_20250828",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 7}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 15,
                    "client_id": 7,
                    "title": "Contract Review - Mr. Sean Hardy",
                    "start_at": "2025-08-28T16:00:00Z",
                    "end_at": "2025-08-28T17:00:00Z",
                    "location": "5033 Parker Keys Suite 325, Old Williamsburg, VT 03979",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 7}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_81",
        instruction=(
            "Handle the preparation of a comps draft for client 2 under broker 14 and incorporate an internal broker debrief. End state to achieve: save and read a comp report for subject_property_id 'HTX017' CO 'draft' status; create a 'likely_buyer' campaign titled 'Aug 2025 Comps Draft — Client 2'; record one email sent to client 2 with the subject 'Comps Draft' (template_code 'likely_buyer') and body_uri 'https://test.storage.com/emails/comps_draft_c2.html'; ensure two holds are placed: 2025-08-27 15:00–15:30Z 'Urban Living Property Tour' at '2222 Smith Street Unit 405, Phoenix, AZ 77002' (source 'viewing') and 2025-08-27 18:10–18:30Z 'Broker internal debrief' at 'Office' (source 'follow_up'). Confirm through reads."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "HTX017",
                    "created_by_broker_id": 14,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Comps Draft — Client 2",
                    "type": "likely_buyer",
                    "created_by": 14,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Comps Draft",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comps_draft_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Urban Living Property Tour",
                    "start_at": "2025-08-27T15:00:00Z",
                    "end_at": "2025-08-27T15:30:00Z",
                    "location": "2222 Smith Street Unit 405, Phoenix, AZ 77002",
                    "source": "viewing",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Broker internal debrief",
                    "start_at": "2025-08-27T18:10:00Z",
                    "end_at": "2025-08-27T18:30:00Z",
                    "location": "Office",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_82",
        instruction=(
            "Coordinate a Sunday open‑house circuit for client 12 with broker 6. Achieve the final state: confirm neighborhoods [4,5] were reviewed for open‑house timing (context only); ensure a route dated 2025‑08‑24 is created with ordered stops ['HTX041','HTX040','HTX048'] and map URL 'https://maps.google.com/route/oh_plan_c12_20250824', confirming hops are feasible within ≤30 minutes each; establish a 'likely_buyer' campaign titled 'Aug 2025 Sunday Open Houses — Client 12' for outbound email use; document one email to client 12 with the subject 'Open House Plan — 2025‑08‑24' and body_uri 'https://maps.google.com/route/oh_plan_c12_20250824'; ensure a same‑day hold is present on 2025‑08‑24 09:20–09:30Z 'Pre-drive sync' at 'Phone' with source 'follow_up'; and capture an audit event for the route building. Validate your actions by reviewing the campaign, saved route, email, and client’s calendar events."
        ),
        actions=[
            Action(
                name="OpenHouseWindowsByNeighborhoods",
                kwargs={"neighborhood_ids": [4, 5]},
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 12,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX041", "HTX040", "HTX048"],
                    "map_url": "https://maps.google.com/route/oh_plan_c12_20250824",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX041", "HTX040", "HTX048"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Sunday Open Houses — Client 12",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 12,
                    "broker_id": 6,
                    "subject": "Open House Plan — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/oh_plan_c12_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 12}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 12,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:20:00Z",
                    "end_at": "2025-08-24T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 12}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 6,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {
                        "stops": ["HTX041", "HTX040", "HTX048"],
                        "map_url": "https://maps.google.com/route/oh_plan_c12_20250824",
                    },
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_83",
        instruction=(
            "Coordinate a 15‑year financing plan for client 6 under broker 2. Final outcome: gather the mortgage profile (context) and determine a mortgage estimate for client 6 with list_price 480000, term_years 15, and region 'AZ-HOU'; a 'general_update' campaign named 'Aug 2025 Financing Plan — Client 6' exists; an email to client 6 with the subject 'Financing Options — 15‑year plan' and body_uri 'https://test.storage.com/emails/finance_c6_15yr.html' is recorded in the campaign; a consult hold is scheduled on 2025‑08‑22 from 21:00‑21:30Z titled 'Financing consult' at 'Video — Zoom' (source 'follow_up'). Confirm by reviewing the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(name="RetrieveMortgageProfile", kwargs={"client_id": 6}),
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 6,
                    "list_price": 480000,
                    "term_years": 15,
                    "region": "AZ-HOU",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Financing Plan — Client 6",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Financing Options — 15-year plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_c6_15yr.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 6}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Financing consult",
                    "start_at": "2025-08-22T21:00:00Z",
                    "end_at": "2025-08-22T21:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 6}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_84",
        instruction=(
            "Organize a Uptown CMA snapshot for client 2 under broker 14. Final state: a draft comp report is accessible with the subject 'MDTN_CMA_C2_AUG25'; a campaign called 'Aug 2025 Uptown CMA — Client 2' exists and sends one email with the subject 'Uptown CMA Snapshot' (template 'likely_buyer') and body URI 'https://test.storage.com/emails/midtown_cma_c2.html'; a follow‑up phone hold on 2025-08-23 from 18:20Z to 18:40Z titled 'CMA debrief' (source 'follow_up') is noted on the calendar. Validate through the comp report, campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MDTN_CMA_C2_AUG25",
                    "created_by_broker_id": 14,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Uptown CMA — Client 2",
                    "type": "likely_buyer",
                    "created_by": 14,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Uptown CMA Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/midtown_cma_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "CMA debrief",
                    "start_at": "2025-08-23T18:20:00Z",
                    "end_at": "2025-08-23T18:40:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_85",
        instruction=(
            "Set up a Cypress commute test for client 6 under broker 2. Final state: drive-time feasibility is verified for ['HTX551','HTX562','HTX574'] within a 25-minute limit; there's a route dated 2025-08-27 for those stops, and the map link 'https://maps.example.com/route/c6_aug27' is stored precisely and is accessible; a campaign titled 'Aug 2025 Commute Test — Client 6' exists and dispatches one email 'Commute Test Plan' (template 'general_update') using 'https://test.storage.com/emails/commute_test_c6.html'; and a pre-commute client-meeting call on 2025-08-27 from 07:40Z to 08:00Z entitled 'Pre-commute check-CO' at 'Phone' (source 'client_meeting') is listed on the calendar. Confirm via the drive-time verification, route specifics, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX551", "HTX562", "HTX574"],
                    "max_minutes": 25,
                },
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 6,
                    "date": "2025-08-27",
                    "stops_ordered_json": ["HTX551", "HTX562", "HTX574"],
                    "map_url": "https://maps.example.com/route/c6_aug27",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Commute Test — Client 6",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Commute Test Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/commute_test_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 6}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Pre-commute check-CO",
                    "start_at": "2025-08-27T07:40:00Z",
                    "end_at": "2025-08-27T08:00:00Z",
                    "location": "Phone",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 6}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_86",
        instruction=(
            "Prepare a concise market progress update for client 14 with broker 7. Final state: a 'general_update' campaign named 'Aug 2025 Uptown Market Update — Client 14' is established; current comps are accessed using listing_ids [4, 5, 6]; a showing route for 2025-08-25 with ordered stops ['HTX012','HTX027','HTX044'] is saved at map URL 'https://maps.google.com/route/htx_014_20250825'; and one email to client 14 is registered under the established campaign with subject 'Uptown Market Update & Showing Plan', template_code 'general_update', and body_uri 'https://maps.google.com/route/htx_014_20250825'. Validate the entries by reviewing the campaign, email, and route."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Uptown Market Update — Client 14",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(
                name="GatherListingsWithProperties",
                kwargs={"listing_ids": [4, 5, 6]},
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 14,
                    "date": "2025-08-25",
                    "stops_ordered_json": ["HTX012", "HTX027", "HTX044"],
                    "map_url": "https://maps.google.com/route/htx_014_20250825",
                    "created_by_broker_id": 7,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 14,
                    "broker_id": 7,
                    "subject": "Uptown Market Update & Showing Plan",
                    "template_code": "general_update",
                    "body_uri": "https://maps.google.com/route/htx_014_20250825",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 14}),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_87",
        instruction=(
            "Handle a v3 client briefing for client 16 under broker 8. End state: a briefing document is produced with version_tag 'v3' and stored at 'https://test.storage.com/details/client_briefing_016_v3.pdf'; initiate a 'general_update' campaign labeled 'Aug 2025 Briefing v3 — Client 16' which is utilized for one email featuring subject 'Briefing v3' (template_code 'general_update') employing the specified file URI as body_uri; arrange a reminder scheduled on 2025-08-31 12:30–12:50Z titled 'Briefing v3 review' at 'Video — Zoom' (source 'follow_up'). Validate by checking campaign, emails, and calendar."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc",
                kwargs={"client_id": 16, "broker_id": 8, "version_tag": "v3"},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Briefing v3 — Client 16",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Briefing v3",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_016_v3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 16}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 8,
                    "client_id": 16,
                    "title": "Briefing v3 review",
                    "start_at": "2025-08-31T12:30:00Z",
                    "end_at": "2025-08-31T12:50:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 16}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_88",
        instruction=(
            "Coordinate sharing of a Arts Quarter vs SoDo townhouse comparison for client 12 under broker 3. End state: a documented snapshot for subject property ID 'MD_VS_EADO_TH_C12_AUG25' is available in draft status and can be read; context includes up to six active townhouses across neighborhoods [13,9]; attach a quick finance estimate to the update using a target price of 530000 over 30 years in region AZ; connect one client message to a campaign titled 'Aug 2025 Museum vs SoDo - Client 12' with subject 'Townhouse Compare: Museum vs SoDo' using body URI 'https://test.storage.com/emails/museum_vs_eado_c12.html' and the likely-buyer template; also, place a viewing hold on 2025-08-25 from 14:00Z to 14:20Z titled 'Compare plan' at '3030 Caroline Street, Phoenix, AZ 77004' (source 'viewing') on the calendar. Confirm by checking the saved snapshot, retrieving the campaign and email records, verifying the calendar entry, and obtaining the finance estimate."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 12,
                    "subject_property_id": "MD_VS_EADO_TH_C12_AUG25",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [13, 9],
                    "property_type": "townhouse",
                    "limit": 6,
                },
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 12,
                    "list_price": 530000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Museum vs SoDo - Client 12",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Compare: Museum vs SoDo",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/museum_vs_eado_c12.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 12}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Compare plan",
                    "start_at": "2025-08-25T14:00:00Z",
                    "end_at": "2025-08-25T14:20:00Z",
                    "location": "3030 Caroline Street, Phoenix, AZ 77004",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 12}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_89",
        instruction=(
            "You arrange a Saturday open-house route for client 5 under broker 2. Final state: a 'likely_buyer' campaign named 'Aug 2025 Saturday Open Houses - Client 5' is established; a route for 2025-08-23 is recorded with ordered stops ['HTX012','HTX009','HTX020'] and the map URL 'https://maps.google.com/route/htx_012_20250823'; drive-time feasibility is satisfactory at no more than 30 minutes per hop; and an email to client 5 is documented under that campaign with the subject 'Open House Route - 2025-08-23' and body_uri 'https://maps.google.com/route/htx_012_20250823'. Additionally, place a same-day hold from 10:00-10:15Z titled 'Day-of check-CO' at 'Phone' (source 'follow_up'). Confirm by reviewing the campaign, the route particulars, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Saturday Open Houses - Client 5",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 5,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX012", "HTX009", "HTX020"],
                    "map_url": "https://maps.google.com/route/htx_012_20250823",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX012", "HTX009", "HTX020"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 5,
                    "broker_id": 2,
                    "subject": "Open House Route - 2025-08-23",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/htx_012_20250823",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 5}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 5,
                    "title": "Day-of check-CO",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:15:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 5}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_90",
        instruction=(
            "You deliver a first-time buyer education pack to client 17 under broker 10. End state: calculate a mortgage estimate at list_price 450000 with region 'AZ' (term_years 30) for context; a 'likely_buyer' campaign named 'Aug 2025 First-Time Buyer — Client 17' is established and is utilized for an email with the subject 'First-Time Buyer Guide' (template_code 'likely_buyer') and body_uri 'https://test.storage.com/emails/ftb_guide_c17.html'; a consult hold is scheduled for 2025-08-22 22:00–22:30Z titled 'Financing consult (SF)' at 'Video — Zoom' (source 'follow_up'). Confirm with readings."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 17,
                    "list_price": 450000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 First-Time Buyer — Client 17",
                    "type": "likely_buyer",
                    "created_by": 10,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "First-Time Buyer Guide",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/ftb_guide_c17.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 17}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 10,
                    "client_id": 17,
                    "title": "Financing consult (SF)",
                    "start_at": "2025-08-22T22:00:00Z",
                    "end_at": "2025-08-22T22:30:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 17}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_91",
        instruction=(
            "Coordinate an inspection summary for client 14, managed by broker 5. Desired outcome: a briefing document (version 'inspection_aug25') is created and referenced; a campaign called 'Aug 2025 Inspection Delivered — Client 14' is in place and dispatches a single email with the subject 'Inspection Report' (template 'general_update') using the briefing URI as the body content; and a follow‑up phone hold for 2025-08-22 from 19:15Z to 19:35Z labeled 'Inspection Q&A' (source 'follow_up') is displayed on the calendar. Confirm through campaign review, email log, and calendar check."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "version_tag": "inspection_aug25",
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Inspection Delivered — Client 14",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "Inspection Report",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_014_inspection_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 14}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "Inspection Q&A",
                    "start_at": "2025-08-22T19:15:00Z",
                    "end_at": "2025-08-22T19:35:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 14}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_92",
        instruction=(
            "Oversee the preparation of mortgage guidance and subsequent steps for client 8, coordinated by broker 12. Required result: a mortgage estimate is determined for client 8 at a listing price of 550000 (context); a concise comps package is documented as a comp report for subject_property_id 'HTX088' (authored by broker_id 12) and its specifics are verified; a 'general_update' campaign named 'Aug 2025 Mortgage & Viewing - Client 8' is established; an email directed to client 8 with the subject 'Mortgage & Viewing Plan' and having body_uri 'https://test.storage.com/emails/mortgage_viewing_c8.html' is filed under that campaign; and two calendar holds are set — 2025-08-22 14:00–14:30Z titled 'Mortgage consult' at 'Office' (source 'follow_up') and 2025-08-24 18:00–19:00Z titled 'Placeholder viewing window' at 'TBD' (source 'viewing')."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 8, "list_price": 550000},
            ),
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 8,
                    "subject_property_id": "HTX088",
                    "created_by_broker_id": 12,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Mortgage & Viewing - Client 8",
                    "type": "general_update",
                    "created_by": 12,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Mortgage & Viewing Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/mortgage_viewing_c8.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 8}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Mortgage consult",
                    "start_at": "2025-08-22T14:00:00Z",
                    "end_at": "2025-08-22T14:30:00Z",
                    "location": "Office",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Placeholder viewing window",
                    "start_at": "2025-08-24T18:00:00Z",
                    "end_at": "2025-08-24T19:00:00Z",
                    "location": "TBD",
                    "source": "viewing",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 8}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_93",
        instruction=(
            "Broaden the search guidance for client 2 working with broker 3 by exclusively considering the actual adjacent neighborhoods of neighborhood 1. Final state: details for neighborhood 1 and its adjacent IDs are read; listings are searched strictly within those adjacent neighborhoods using beds=2 and baths=2 (context); a 'general_update' campaign titled 'Aug 2025 Bordering Areas - Client 2' is established; there is an email for client 2 with the subject 'Bordering Area Options' and body_uri 'https://test.storage.com/emails/border_c2.html' within that campaign; and a consultation hold for 2025-08-23 16:00–16:30Z is arranged, titled 'Bordering areas consult' at 'Video - Zoom', marked as 'follow_up'."
        ),
        actions=[
            Action(name="FetchNeighborhood", kwargs={"neighborhood_id": 1}),
            Action(name="ListAdjacentNeighborhoods", kwargs={"neighborhood_id": 1}),
            Action(
                name="QueryListingsByNeighborhoods",
                kwargs={"neighborhood_ids": [2], "beds": 2, "baths": 2},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Bordering Areas - Client 2",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="ComposeClientEmail",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 2,
                    "subject": "Bordering Area Options",
                    "slug": "border_c2",
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Area Options",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/border_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 2}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 3,
                    "client_id": 2,
                    "title": "Bordering areas consult",
                    "start_at": "2025-08-23T16:00:00Z",
                    "end_at": "2025-08-23T16:30:00Z",
                    "location": "Video - Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_94",
        instruction=(
            "Coordinate the preparation of a briefing packet for client 7 under broker 5. Final state: a briefing document is created for client 7 (version_tag defaults to 'v1'), so the file exists at 'https://test.storage.com/details/client_briefing_007_v1.pdf'; an external next‑steps checklist is attached to the client with file_uri 'https://test.storage.com/checklists/next_steps_c7.pdf' (created_by 5); a 'general_update' campaign named 'Aug 2025 Briefing & Next Steps — Client 7' is active; an email to client 7 with the subject 'Briefing Packet & Next Steps' and body_uri 'https://test.storage.com/details/client_briefing_007_v1.pdf' is recorded under the campaign; a review hold is scheduled for 2025‑08‑22 20:00–20:20Z titled 'Briefing review' at 'Video — Teams' (source 'follow_up'); and an audit log 'briefing_sent' is entered referencing the campaign. Validate by reviewing the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(name="CreateBriefingDoc", kwargs={"client_id": 7, "broker_id": 5}),
            Action(
                name="LinkDocumentToClient",
                kwargs={
                    "client_id": 7,
                    "file_uri": "https://test.storage.com/checklists/next_steps_c7.pdf",
                    "created_by": 5,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Briefing & Next Steps — Client 7",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 7,
                    "broker_id": 5,
                    "subject": "Briefing Packet & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_007_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 7,
                    "title": "Briefing review",
                    "start_at": "2025-08-22T20:00:00Z",
                    "end_at": "2025-08-22T20:20:00Z",
                    "location": "Video — Teams",
                    "source": "follow_up",
                },
            ),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 5,
                    "action": "briefing_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                    "metadata_json": {
                        "doc_uri": "https://test.storage.com/details/client_briefing_007_v1.pdf"
                    },
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(name="ListClientEmails", kwargs={"client_id": 7}),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 7}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_95",
        instruction=(
            "Coordinate the assembly of a condo investment package for client 15 under broker 8. Achieve the final state by conducting a listings search for neighborhoods [5,7], property_type 'condo', price range 350000–600000, limit 6; calculate a mortgage estimate for client 15 using list_price 500000 (for context); store a comps snapshot as a comp report for subject_property_id 'HTX057' (created_by_broker_id 8) with status 'draft' and ensure the report is verified; confirm the presence of a 'general_update' campaign called 'Aug 2025 Condo Picks — Client 15' for outbound emails; ensure an email to client 15 is documented with subject 'Condo Investment Picks' and body_uri 'https://test.storage.com/emails/condo_invest_c15.html'; verify that a consult hold for 2025‑08‑24 20:30–21:00Z titled 'Investment consult' at 'Video — Zoom' with source 'follow_up' is set; and that an audit event logs the campaign send. Validate your work by reviewing the comp report details, the campaign, the email to client 15, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="QueryActiveListings",
                kwargs={
                    "neighborhood_ids": [5, 7],
                    "property_type": "condo",
                    "price_min": 350000,
                    "price_max": 600000,
                    "limit": 6,
                },
            ),
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 15, "list_price": 500000},
            ),
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 15,
                    "subject_property_id": "HTX057",
                    "created_by_broker_id": 8,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Condo Picks — Client 15",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Condo Investment Picks",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/condo_invest_c15.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 15}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Investment consult",
                    "start_at": "2025-08-24T20:30:00Z",
                    "end_at": "2025-08-24T21:00:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 15}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 8,
                    "action": "campaign_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_96",
        instruction=(
            "Handle the preparation of an investor financing check-CO for client 18 under broker 5. Reach the final state by calculating a mortgage estimate for client 18 at list_price 500000 (for context); ensure a 'general_update' campaign named 'Aug 2025 Investor Financing — Client 18' is in existence; record an email to client 18 with subject 'Investor Financing Snapshot' and body_uri 'https://test.storage.com/emails/finance_investor_c18.html' under the campaign; and verify the existence of two holds — on 2025‑08‑22 19:00–19:20Z titled 'Lender Q&A' at 'Video — Zoom' (source 'follow_up') and on 2025‑08‑24 17:00–17:30Z titled 'Docs review' at 'Office' (source 'client_meeting'). Confirm by reviewing the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={"client_id": 18, "list_price": 500000},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Investor Financing — Client 18",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Investor Financing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_investor_c18.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 18}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Lender Q&A",
                    "start_at": "2025-08-22T19:00:00Z",
                    "end_at": "2025-08-22T19:20:00Z",
                    "location": "Video — Zoom",
                    "source": "follow_up",
                },
            ),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 5,
                    "client_id": 18,
                    "title": "Docs review",
                    "start_at": "2025-08-24T17:00:00Z",
                    "end_at": "2025-08-24T17:30:00Z",
                    "location": "Office",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 18}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_97",
        instruction=(
            "Handle the delivery of a Autumn Creek CMA for client 13 under broker 2 ensuring an audit trail is maintained. End state: confirm a draft comp report for 'SPRBR_CMA_C13_AUG25' is safely saved and readable; establish a campaign titled 'Aug 2025 Autumn Creek CMA — Client 13' which dispatches one email with the subject 'Your Market Analysis is Ready' using the template 'likely_buyer' and the body URI 'https://test.storage.com/emails/sprbr_cma_c13.html'; log an audit event 'client_notified' linked to the comp report and ensure the report is re-read; include a follow-up phone hold scheduled on 2025-08-26 from 18:10Z to 18:30Z titled 'CMA debrief' (source 'follow_up') in the calendar. Verify results by reviewing comp report reads, the campaign/email, and the calendar entry."
        ),
        actions=[
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 13,
                    "subject_property_id": "SPRBR_CMA_C13_AUG25",
                    "created_by_broker_id": 2,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Autumn Creek CMA — Client 13",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 13,
                    "broker_id": 2,
                    "subject": "Your Market Analysis is Ready",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/sprbr_cma_c13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 13}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 2,
                    "action": "client_notified",
                    "entity_type": "comp_reports",
                    "entity_id": 9,
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 13,
                    "title": "CMA debrief",
                    "start_at": "2025-08-26T18:10:00Z",
                    "end_at": "2025-08-26T18:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 13}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_98",
        instruction=(
            "Coordinate the preparation of a briefing update for client 8 under broker 12. Required end state: ensure a briefing document is generated and linked to client 8; confirm the existence of a 'general_update' campaign named 'Aug 2025 Briefings — Client 8'; record the broker-authored email to client 8 filed under that campaign with subject 'Client Briefing Packet', template_code 'briefing_broker', and body_uri 'https://test.storage.com/details/client_briefing_008_v1.pdf'; and place a review hold for client 8 on 2025‑08‑22 from 14:00 to 14:30Z titled 'Briefing review' at 'Office', with notes 'Review briefing packet', source 'client_meeting'. Confirm the writes by checking the campaign, the email for client 8, and the calendar event; document an audit noting the briefing was dispatched."
        ),
        actions=[
            Action(
                name="CreateBriefingDoc", kwargs={"client_id": 8, "broker_id": 12}
            ),
            Action(
                name="LinkDocumentToClient",
                kwargs={"client_id": 8, "document_id": 21},
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Briefings — Client 8",
                    "type": "general_update",
                    "created_by": 12,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Client Briefing Packet",
                    "template_code": "briefing_broker",
                    "body_uri": "https://test.storage.com/details/client_briefing_008_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 8}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 12,
                    "client_id": 8,
                    "title": "Briefing review",
                    "start_at": "2025-08-22T14:00:00Z",
                    "end_at": "2025-08-22T14:30:00Z",
                    "location": "Office",
                    "notes": "Review briefing packet",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 8}),
            Action(
                name="AppendAuditEvent",
                kwargs={
                    "actor_id": 12,
                    "action": "briefing_sent",
                    "entity_type": "documents",
                    "entity_id": 21,
                    "metadata_json": {"client_id": 8, "campaign_id": 9},
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_99",
        instruction=(
            "Handle the preparation of an open-house plan for client 9 under broker 2. The verifiable end state should comprise: open-house windows gathered for neighborhoods [2,3] (context); a stored route scheduled for 2025-08-24 with ordered stops ['HTX021','HTX025','HTX030'] using map URL 'https://maps.google.com/route/htx_plan_c9_20250824' that adheres to a ≤30-minute hop constraint; a 'likely_buyer' campaign named 'Aug 2025 Open House Plan - Client 9' which includes one email sent to client 9 with the subject 'Sunday Route - 2025-08-24' and the body_uri 'https://test.storage.com/emails/sunday_route_c9.html'; and a same-day hold from 09:30 to 09:45Z titled 'Pre-drive sync' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="OpenHouseWindowsByNeighborhoods",
                kwargs={"neighborhood_ids": [2, 3]},
            ),
            Action(
                name="PersistViewingRoute",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX021", "HTX025", "HTX030"],
                    "map_url": "https://maps.google.com/route/htx_plan_c9_20250824",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="ReadRoute", kwargs={"route_id": 11}),
            Action(
                name="ValidateDriveTimeHops",
                kwargs={
                    "property_ids": ["HTX021", "HTX025", "HTX030"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Open House Plan - Client 9",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Sunday Route - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/sunday_route_c9.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 9}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 2,
                    "client_id": 9,
                    "title": "Pre-drive sync",
                    "start_at": "2025-08-24T09:30:00Z",
                    "end_at": "2025-08-24T09:45:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 9}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v2",
        user_id="task_100",
        instruction=(
            "Coordinate a financing-ready update for client 18 under broker 6 targeting a price of 720000. End state: calculate a 30-year AZ mortgage estimate; save a comp report for subject 'BRAESWOOD_TARGET_C18_AUG25' in draft and make it readable; ensure a campaign titled 'Aug 2025 Financing + CMA — Client 18' is in place and used to send an email with subject 'Financing & CMA' (template 'likely_buyer') and body URI 'https://test.storage.com/emails/financing_cma_c18.html'; and schedule a client meeting on 2025-08-25 from 16:00Z to 16:30Z titled 'Financing plan' at 'Office' (source 'client_meeting'). Confirm completion via the comp report read, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="EstimateMortgagePayment",
                kwargs={
                    "client_id": 18,
                    "list_price": 720000,
                    "term_years": 30,
                    "region": "AZ",
                },
            ),
            Action(
                name="CreateOrUpdateCompReport",
                kwargs={
                    "client_id": 18,
                    "subject_property_id": "BRAESWOOD_TARGET_C18_AUG25",
                    "created_by_broker_id": 6,
                    "final_status": "draft",
                },
            ),
            Action(name="ReadCompReportBundle", kwargs={"report_id": 9}),
            Action(
                name="NewCampaignCreator",
                kwargs={
                    "name": "Aug 2025 Financing + CMA — Client 18",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="ReadCampaign", kwargs={"campaign_id": 9}),
            Action(
                name="PersistOutboundEmail",
                kwargs={
                    "client_id": 18,
                    "broker_id": 6,
                    "subject": "Financing & CMA",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/financing_cma_c18.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="ListClientEmails", kwargs={"client_id": 18}),
            Action(
                name="InsertCalendarEvent",
                kwargs={
                    "broker_id": 6,
                    "client_id": 18,
                    "title": "Financing plan",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:30:00Z",
                    "location": "Office",
                    "source": "client_meeting",
                },
            ),
            Action(name="ListClientCalendarEvents", kwargs={"client_id": 18}),
        ],
        outputs=[]
    ),
]