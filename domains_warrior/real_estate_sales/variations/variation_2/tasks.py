from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="v2",
        user_id="task_01",
        instruction=(
            "You prepare a first‑time buyer packet for client 16 under broker 8. End state: a briefing document is generated "
            "for client 16 (defaults to 'v1') and stored at 'https://test.storage.com/details/client_briefing_016_v1.pdf'; "
            "a 'general_update' campaign named 'First‑Time Buyer Packet -Client 16 - Aug 2025' exists; an email to client 16 "
            "using template_code 'general_update' with subject 'Here’s Your Starter Packet' and body_uri "
            "'https://test.storage.com/details/client_briefing_016_v1.pdf' is recorded under the campaign; and a reminder "
            "hold exists at 2025‑08‑21 23:00–23:10Z titled 'Packet follow‑up' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="create_briefing_doc", kwargs={"client_id": 16, "broker_id": 8}
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "First‑Time Buyer Packet -Client 16 - Aug 2025",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Here’s Your Starter Packet",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_016_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 16}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 16}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_02",
        instruction=(
            "You assemble seller‑outreach drafts for client 19 under broker 7. End state: a drafts bundle is generated for "
            "property_ids ['HTX070','HTX071','HTX072','HTX073'] (context), stored at "
            "'https://test.storage.com/drafts/client_19_props_4.pdf'; a 'general_update' campaign named "
            "'Seller Outreach — Client 19- Aug 2025 ' exists; one email to client 19 using template_code 'general_update' with "
            "subject 'Seller Outreach Drafts' and body_uri 'https://test.storage.com/drafts/client_19_props_4.pdf' is "
            "recorded under the campaign; and a hold exists on 2025‑08‑23 12:00–12:20Z titled 'Select which drafts to send' "
            "at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="draft_seller_broker_batch",
                kwargs={
                    "client_id": 19,
                    "property_ids": ["HTX070", "HTX071", "HTX072", "HTX073"],
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Seller Outreach — Client 19- Aug 2025 ",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Seller Outreach Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_19_props_4.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 19}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 19}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_03",
        instruction=(
            "You prepare a 3‑bed Uptown/Galleria shortlist for client 22 under broker 9. End state: a draft comp report exists and is readable for subject 'UPTOWN_3BEDS_C22_AUG25'; "
            "a campaign titled 'Aug 2025 3‑Bed Uptown — Client 22' exists and sends one email with subject '3‑Bed Options' (template 'likely_buyer') and body URI "
            "'https://test.storage.com/emails/three_bed_uptown_c22.html'; and a viewing kickoff on 2025-08-27 from 12:10Z to 12:40Z titled 'Depart for first stop' at 'Client Home' "
            "(source 'viewing') appears on the calendar. Verify via comp report read, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 22,
                    "subject_property_id": "UPTOWN_3BEDS_C22_AUG25",
                    "created_by_broker_id": 9,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 3‑Bed Uptown — Client 22",
                    "type": "likely_buyer",
                    "created_by": 9,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 22,
                    "broker_id": 9,
                    "subject": "3‑Bed Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/three_bed_uptown_c22.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 22}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 22}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_04",
        instruction=(
            "You create a comps report draft for client 19 under broker 7 and share it. End state: "
            "a comp report is saved for subject_property_id 'HTX044' with status 'draft' and read; "
            "a 'general_update' campaign named 'Aug 2025 CMA Draft — Client 19' exists and is used for one email "
            "with subject 'Your Market Analysis is Ready Draft' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/cma_draft_c19.html'; "
            "a consult hold exists on 2025-08-23 12:40–13:00Z titled 'CMA Draft consult' at 'Phone' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 19,
                    "subject_property_id": "HTX044",
                    "created_by_broker_id": 7,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 CMA Draft — Client 19",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Your Market Analysis is Ready Draft",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/cma_draft_c19.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 19}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 19}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_05",
        instruction=(
            "You send a premium-area update for client 5 under broker 5. End state: a "
            "documented snapshot exists for subject property ID 'ROX_PREM_C5_AUG25' in "
            "draft status and is readable; a concise inventory view reflects up to six "
            "active matches across neighborhoods [6,2,4,10] within 147268-644740 for context; "
            "one outreach is attached to a campaign titled 'River Oaks Premium - Client 5- Aug 2025 ' "
            "with subject 'Premium Area Update' using body URI "
            "'https://test.storage.com/emails/riveroaks_premium_c5.html' and the "
            "general-update template; and a follow-up phone hold on 2025-08-23 from 12:00Z "
            "to 12:20Z titled 'Discuss premium options' (source 'follow_up') appears on the calendar. "
            "Verify through the saved snapshot, the campaign record, the client’s email log, "
            "and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 5,
                    "subject_property_id": "ROX_PREM_C5_AUG25",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [6, 2, 4, 10],
                    "price_min": 147268,
                    "price_max": 644740,
                    "limit": 6,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "River Oaks Premium - Client 5- Aug 2025 ",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Premium Area Update",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/riveroaks_premium_c5.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_06",
        instruction=(
            "You finalize a comparative market analysis for client 11 under broker 6. End state: the record for subject property 'HTX012' shows a document link and a final status of 'sent_to_client', with the session’s activity reflecting that it originated as a draft during this workflow. Anchor one client-facing outreach under a campaign titled 'CMA Results Shared – Client 11' consisting of a single message to client 11 with subject 'Your Market Analysis is Ready' that uses the body URI 'https://test.storage.com/emails/cma_c11.html' and the likely-buyer template. Demonstrate completion by retrieving the report’s details and the client’s campaign/email records."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 11,
                    "subject_property_id": "HTX012",
                    "created_by_broker_id": 6,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "CMA Results Shared – Client 11",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Your Market Analysis is Ready",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/cma_c11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 11}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_07",
        instruction=(
            "You run a two‑segment likely‑buyer outreach for clients 5 and 6 under broker 2. "
            "Create a campaign named 'Aug 2025 Likely Buyers — Segment A' of type 'likely_buyer' and use the ID returned by the create step for all emails. "
            "Use each client’s neighborhoods exactly as listed here to fetch context listings (limit 6 each): client 5 → [6, 2, 4, 10]; client 6 → [8, 12, 6, 5]. "
            "Send both clients an email with subject 'August Listings Shortlist' and body_uri "
            "'https://test.storage.com/emails/likely_buyer_aug_2025.html'. "
            "Create one calendar hold per client titled 'Intro call about shortlist' on 2025‑08‑22, with client 5 at 16:00–16:30Z and client 6 at 17:00–17:30Z, "
            "location 'Phone', notes 'Segment A outreach', source 'follow_up'. "
            "End state: the campaign exists; two emails are recorded (clients 5 and 6); and both calendar holds exist at the specified times."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Likely Buyers — Segment A",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(
                name="query_listings_by_neighborhoods",
                kwargs={"neighborhood_ids": [6, 2, 4, 10], "limit": 6},
            ),
            Action(
                name="query_listings_by_neighborhoods",
                kwargs={"neighborhood_ids": [8, 12, 6, 5], "limit": 6},
            ),
            Action(
                name="persist_outbound_email",
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
                name="persist_outbound_email",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/likely_buyer_aug_2025.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(name="list_client_emails", kwargs={"client_id": 6}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
            Action(name="list_client_calendar_events", kwargs={"client_id": 6}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_08",
        instruction=(
            "You stage a Saturday multi‑stop tour for client 9 under broker 6. End state: a route dated 2025-08-23 exists for client 9 with ordered stops "
            "['HTX221','HTX187','HTX204'] and the map link 'https://maps.example.com/route/c9_aug23' stored verbatim; the route is readable; "
            "drive‑time feasibility is confirmed for those stops with a 25‑minute max between hops; a campaign titled 'Aug 2025 Saturday Tour — Client 9' exists and is used to send one email "
            "with subject 'Tour Map & Plan' (template 'general_update') and body URI 'https://test.storage.com/emails/tour_plan_c9.html'; "
            "and a kickoff viewing hold on 2025-08-23 from 09:20Z to 09:40Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') appears on the calendar. "
            "Verify via the route details, the drive‑time check, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX221", "HTX187", "HTX204"],
                    "map_url": "https://maps.example.com/route/c9_aug23",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX221", "HTX187", "HTX204"],
                    "max_minutes": 25,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Saturday Tour — Client 9",
                    "type": "general_update",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 9,
                    "broker_id": 6,
                    "subject": "Tour Map & Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/tour_plan_c9.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 9}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_09",
        instruction=(
            "You coordinate off-route viewing requests for client 10 under broker 11. End state: a drafts bundle is produced for properties "
            "['HTX040','HTX042','HTX043'] (context); a 'general_update' campaign named 'Aug 2025 Off-Route Viewings - Client 10' exists; "
            "an internal email to client 10 (for record under the campaign) has subject 'Viewing Requests To Send' and body_uri "
            "'https://test.storage.com/emails/offroute_c10.html'; and a follow-up hold exists for client 10 on 2025-08-25 16:00-16:20Z "
            "titled 'Follow up on viewing requests' at 'Video - Teams' (source 'follow_up'). Prove by reading back the campaign, "
            "the email, and the client's calendar events."
        ),
        actions=[
            Action(
                name="draft_seller_broker_batch",
                kwargs={
                    "client_id": 10,
                    "property_ids": ["HTX040", "HTX042", "HTX043"],
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Off-Route Viewings - Client 10",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 10,
                    "subject": "Viewing Requests To Send",
                    "slug": "offroute_c10",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Viewing Requests To Send",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/offroute_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 10}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 10}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_10",
        instruction=(
            "You share a Midtown condo briefing for client 2 under broker 14. End state: "
            "a draft comp report document exists for subject property ID 'MDTN_CONDO_C2_AUG25' "
            "and is readable; one client update is associated with a campaign titled "
            "'Aug 2025 Midtown Condos - Client 2' using subject 'Midtown Condo Picks' "
            "and body URI 'https://test.storage.com/emails/midtown_condos_c2.html' with the "
            "general-update template; and a debrief hold on 2025-08-27 from 18:00Z to 18:20Z "
            "titled 'Midtown options debrief' at 'Office' (source 'follow_up') appears on the calendar. "
            "Verify by reading the comp report and retrieving the campaign record, the client’s "
            "email log, and the calendar entry."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MDTN_CONDO_C2_AUG25",
                    "created_by_broker_id": 14,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Midtown Condos - Client 2",
                    "type": "general_update",
                    "created_by": 14,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Midtown Condo Picks",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/midtown_condos_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Midtown options debrief",
                    "start_at": "2025-08-27T18:00:00Z",
                    "end_at": "2025-08-27T18:20:00Z",
                    "location": "Office",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_11",
        instruction=(
            "You provide a Midtown vs Downtown comparison for client 2 under broker 3. "
            "End state: two draft comp report documents are created and readable—'MID_VS_DT_AUG25_A' "
            "representing Midtown+Downtown context and 'MID_VS_DT_AUG25_B' representing "
            "Downtown-only; a single client update is anchored to a campaign titled "
            "'Aug 2025 Midtown vs Downtown - Client 2' with subject 'Midtown vs Downtown' "
            "using body URI 'https://test.storage.com/emails/mid_vs_dt_c2.html' and the "
            "general-update template; and a Zoom discussion on 2025-08-24 from 16:30Z to "
            "17:00Z titled 'Compare neighborhoods' (source 'follow_up') appears on the "
            "calendar. Prove by reading both comp reports and retrieving the campaign, "
            "the client’s email log, and the calendar entry."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MID_VS_DT_AUG25_A",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MID_VS_DT_AUG25_B",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 10}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Midtown vs Downtown - Client 2",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Midtown vs Downtown",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/mid_vs_dt_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_12",
        instruction=(
            "You prepare a neighborhood preview for client 4 under broker 2. Final state: a campaign of type "
            "'general_update' named 'Aug 2025 Neighborhood Preview - Client 4' exists and is used by the outbound "
            "message; a listings snapshot has been retrieved for neighborhood 1 filtered to price 250000–700000 with "
            "beds=2 and baths=2 (context only); one email exists for client 4 with subject 'Neighborhood Preview' and "
            "body_uri 'https://test.storage.com/emails/preview_c4.html' associated to that campaign; and a calendar "
            "hold exists for client 4 on 2025-08-22 from 15:00–15:30Z titled 'Pre-tour call' at 'Video - Zoom' with "
            "source 'follow_up'."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Neighborhood Preview - Client 4",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [1],
                    "price_min": 250000,
                    "price_max": 700000,
                    "beds": 2,
                    "baths": 2,
                },
            ),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 4,
                    "subject": "Neighborhood Preview",
                    "slug": "preview_c4",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Neighborhood Preview",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/preview_c4.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 4}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 4}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_13",
        instruction=(
            "You complete a Westbury CMA + follow‑up workflow for client 21 under broker 4. End state: "
            "a comp report for subject 'WESTBURY_CMA_C21_AUG25' is saved in draft and readable, then its status is updated to 'sent_to_client' and re‑read; "
            "a campaign titled 'Aug 2025 Westbury CMA — Client 21' (type 'general_update') exists and is used to send one email to client 21 with subject 'Your Westbury CMA' "
            "using template 'general_update' and body URI 'https://test.storage.com/emails/westbury_cma_c21.html'; "
            "and a follow‑up hold for 2025-08-23 from 15:30Z to 15:50Z titled 'CMA Q&A' at 'Video — Zoom' (source 'follow_up') appears on the calendar. "
            "Verify by reading the comp report, the campaign, the client’s email log, and the client’s calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 21,
                    "subject_property_id": "WESTBURY_CMA_C21_AUG25",
                    "created_by_broker_id": 4,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Westbury CMA — Client 21",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 21,
                    "broker_id": 4,
                    "subject": "Your Westbury CMA",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/westbury_cma_c21.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 21}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 21}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_14",
        instruction=(
            "You prepare a weekend open-house overview for client 10 under broker 11. End state: "
            "open-house windows are fetched for neighborhoods [13,1,12] (context); "
            "a 'general_update' campaign named 'Aug 2025 Weekend OH — Client 10' exists; "
            "one email to client 10 with subject 'Weekend Open Houses' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/weekend_oh_c10.html' is recorded; "
            "a planning hold exists 2025-08-23 13:00–13:20Z titled 'Plan weekend open houses' at 'Phone' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="open_house_windows_by_neighborhoods",
                kwargs={"neighborhood_ids": [13, 1, 12]},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Weekend OH — Client 10",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Weekend Open Houses",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_oh_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 10}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 10}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_15",
        instruction=(
            "You send a price-alert follow-up for client 13 under broker 5. End state: "
            "recent sales for 'HTX043' (limit 3) are read (context); "
            "a 'general_update' campaign named 'Aug 2025 Price Alert Follow-Up — Client 13' exists and is used for one email "
            "with subject 'Price Move & Local Sales' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/price_move_sales_c13.html'; "
            "a 2025-08-23 10:00–10:20Z 'Price-move debrief' hold at 'USNV Strickland, FPO AP 98640' (source 'client_meeting') exists. Verify via reads."
        ),
        actions=[
            Action(
                name="recent_sales_for_property",
                kwargs={"property_id": "HTX043", "limit": 3},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Price Alert Follow-Up — Client 13",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "Price Move & Local Sales",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/price_move_sales_c13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 13}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 13}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_16",
        instruction=(
            "You assemble an investor packet for client 20 under broker 11. End state: a briefing document is generated for client 20 "
            "(defaults to 'v1'); a 'general_update' campaign named 'Aug 2025 Investor Packet — Client 20' exists; an email to client 20 using "
            "template_code 'general_update' with subject 'Investor Packet' and body_uri "
            "'https://test.storage.com/guides/investor_packet_c20.pdf' is recorded under the campaign; and a review hold exists "
            "for 2025‑08‑22 20:00–20:25Z titled 'Investor packet review' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="create_briefing_doc", kwargs={"client_id": 20, "broker_id": 11}
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Investor Packet — Client 20",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Investor Packet",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/guides/investor_packet_c20.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 20}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 20}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_17",
        instruction=(
            "You prepare an investor-leaning condo snapshot for client 15 under broker 8. End state: "
            "a listings context run for neighborhoods [5,12,1,7] with property_type 'condo' and price 246399–420408 (limit 6) is on record; "
            "a mortgage estimate for client 15 at list_price 400000 is computed; "
            "a 'general_update' campaign named 'Aug 2025 Investor Snapshot — Client 15' exists and is used for one email to client 15 "
            "with subject 'Condo Investor Snapshot' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/investor_snapshot_c15.html'; "
            "place a consult hold on 2025-08-24 20:30–21:00Z titled 'Investor consult' at 'Video — Zoom' (source 'follow_up'). "
            "Prove the writes by reading back the campaign, the client’s emails, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [5, 12, 1, 7],
                    "property_type": "condo",
                    "price_min": 246399,
                    "price_max": 420408,
                    "limit": 6,
                },
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 15, "list_price": 400000},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Investor Snapshot — Client 15",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Condo Investor Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/investor_snapshot_c15.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 15}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 15}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_18",
        instruction=(
            "You ready a financing brief for client 18 under broker 6. End state: the client’s mortgage profile is checked; a 30‑year TX estimate is computed for list price 540000; "
            "a briefing document (version 'aug25') is generated and referenced in one email under a campaign titled 'Aug 2025 Financing Brief — Client 18' with subject 'Your Financing Brief' "
            "(template 'general_update') and body URI 'https://test.storage.com/details/client_briefing_018_aug25.pdf'; and a follow‑up phone hold on 2025-08-24 from 19:00Z to 19:20Z "
            "titled 'Financing Q&A' (source 'follow_up') is on the calendar. Verify via the campaign/email and calendar."
        ),
        actions=[
            Action(name="retrieve_mortgage_profile", kwargs={"client_id": 18}),
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 18,
                    "list_price": 540000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="create_briefing_doc",
                kwargs={"client_id": 18, "broker_id": 6, "version_tag": "aug25"},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Financing Brief — Client 18",
                    "type": "general_update",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 18,
                    "broker_id": 6,
                    "subject": "Your Financing Brief",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_018_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 18}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 18}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_19",
        instruction=(
            "You deliver a loan-sizing snapshot for client 10 with broker 11. End state: "
            "compute a mortgage estimate at list_price 600000 (region 'TX', term_years 30) as context; "
            "a 'general_update' campaign named 'Aug 2025 Loan Sizing — Client 10' exists; "
            "one email to client 10 with subject 'Loan Sizing Snapshot' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/loan_sizing_c10.html' is recorded; "
            "a 2025-08-23 13:20–13:40Z 'Sizing consult' hold at 'Phone' (source 'follow_up'). Verify via reads."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 10,
                    "list_price": 600000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Loan Sizing — Client 10",
                    "type": "general_update",
                    "created_by": 11,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 10,
                    "broker_id": 11,
                    "subject": "Loan Sizing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/loan_sizing_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 10}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 10}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_20",
        instruction=(
            "You create a Sunday route plan for client 2 under broker 3 using neighborhood context. End state must reflect: "
            "open‑house windows for neighborhood [1] were used as context; a route dated 2025‑08‑24 is saved with ordered stops "
            "['HTX001','HTX004','HTX005'] and map URL 'https://maps.google.com/route/sun_c2_20250824'; a 30‑minute hop check passes; "
            "a 'likely_buyer' campaign named 'Aug 2025 Sunday Route — Client 2' exists; one email to client 2 using template_code "
            "'likely_buyer' with subject 'Sunday Route — 2025‑08‑24' and that same map URL as body_uri is on record under the campaign; "
            "and two holds exist — 09:55–10:05Z titled 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10–13:25Z "
            "titled 'Post‑route debrief' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="open_house_windows_by_neighborhoods",
                kwargs={"neighborhood_ids": [1]},
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/sun_c2_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Sunday Route — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Sunday Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/sun_c2_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_21",
        instruction=(
            "You prepare viewing‑request drafts for client 11 under broker 4. Final state: a drafts bundle is generated for property_ids "
            "['HTX055','HTX057','HTX060'] (context), which deterministically lives at "
            "'https://test.storage.com/drafts/client_11_props_3.pdf'; that file is attached to client 11; a 'general_update' campaign "
            "named 'Aug 2025 Viewing Requests — Client 11' exists; one email to client 11 with subject 'Viewing Requests Drafts' and body_uri "
            "'https://test.storage.com/drafts/client_11_props_3.pdf' is recorded under the campaign; and a confirmation hold exists for "
            "2025‑08‑22 17:00–17:20Z titled 'Confirm viewing requests' at 'Phone' (source 'follow_up'). Prove by reading back the campaign, the "
            "email for client 11, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="draft_seller_broker_batch",
                kwargs={
                    "client_id": 11,
                    "property_ids": ["HTX055", "HTX057", "HTX060"],
                },
            ),
            Action(
                name="link_document_to_client",
                kwargs={
                    "client_id": 11,
                    "file_uri": "https://test.storage.com/drafts/client_11_props_3.pdf",
                    "created_by": 4,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Viewing Requests — Client 11",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 11,
                    "broker_id": 4,
                    "subject": "Viewing Requests Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_11_props_3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 11}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 11}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_22",
        instruction=(
            "You send a welcome packet to client 20 under broker 7. End state: a 'general_update' campaign named 'Aug 2025 Welcome - Client 20' exists; "
            "an email to client 20 is recorded under the campaign with subject 'Welcome & Next Steps' and body_uri "
            "'https://test.storage.com/emails/welcome_c20.html'; and two holds exist — 2025-08-22 18:00-18:20Z titled 'Welcome call' "
            "at 'Phone' (source 'follow_up') and 2025-08-23 18:00-18:30Z titled 'Next-steps planning' at 'Video - Zoom' (source 'follow_up'). "
            "Prove by reading back the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Welcome - Client 20",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 20,
                    "subject": "Welcome & Next Steps",
                    "slug": "welcome_c20",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 20,
                    "broker_id": 7,
                    "subject": "Welcome & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/welcome_c20.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 20}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 20}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_23",
        instruction=(
            "You prepare a concise comp package for client 2 under broker 3. Final state: a comp report is saved for "
            "subject_property_id 'HTX049' (created_by_broker_id 3) with status 'draft' and verified via read; a 'likely_buyer' campaign named "
            "'Aug 2025 Quick Comps — Client 2' exists; one email to client 2 with subject 'Quick Comps Pack' and body_uri "
            "'https://test.storage.com/emails/quick_comps_c2.html' is recorded under the campaign; and a follow‑up hold exists on "
            "2025‑08‑23 14:00–14:20Z titled 'Comps review' at 'Phone' (source 'follow_up'). Prove by reading back the comp report details, "
            "the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "HTX049",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Quick Comps — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Quick Comps Pack",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/quick_comps_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_24",
        instruction=(
            "You prepare a three‑home seller outreach packet for client 8 under broker 5. End state: an outreach drafts bundle exists for ['HTX401','HTX402','HTX403']; "
            "a campaign titled 'Aug 2025 Seller Inquiries — Client 8' exists and is used to send one email with subject 'Owner Inquiry Drafts' (template 'general_update') and body URI "
            "'https://test.storage.com/drafts/client_8_props_3.pdf'; an audit event 'drafts_prepped' is recorded on the campaign and the campaign is re‑read; "
            "and a follow‑up phone hold on 2025-08-25 from 13:30Z to 13:50Z titled 'Seller outreach debrief' (source 'follow_up') appears on the calendar. Verify via campaign reads, email log, and calendar."
        ),
        actions=[
            Action(
                name="draft_seller_broker_batch",
                kwargs={"client_id": 8, "property_ids": ["HTX401", "HTX402", "HTX403"]},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Seller Inquiries — Client 8",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 8,
                    "broker_id": 5,
                    "subject": "Owner Inquiry Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_8_props_3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 8}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 5,
                    "action": "drafts_prepped",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 8}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_25",
        instruction=(
            "You compile a Montrose first‑time buyer briefing for client 7 under broker 5. End state: a briefing document (version 'aug25') is generated and referenced in one email under "
            "a campaign titled 'Aug 2025 Buyer Brief — Client 7' with subject 'Your Buyer Brief' (template 'general_update') and body URI "
            "'https://test.storage.com/details/client_briefing_007_aug25.pdf'; and a follow‑up phone hold on 2025-08-24 from 17:10Z to 17:30Z titled 'Brief Q&A' (source 'follow_up') "
            "appears on the calendar. Verify by reading the campaign, the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="create_briefing_doc",
                kwargs={"client_id": 7, "broker_id": 5, "version_tag": "aug25"},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Buyer Brief — Client 7",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 7,
                    "broker_id": 5,
                    "subject": "Your Buyer Brief",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_007_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 7}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 7}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_26",
        instruction=(
            "You design a bordering-area Sunday tour for client 2 with broker 3. End state: "
            "neighborhood 1 details and its bordering list are retrieved (context); "
            "a route for 2025-08-24 is saved with ordered stops ['HTX001','HTX004','HTX005'] and map "
            "'https://maps.google.com/route/dt_mid_c2_20250824'; hops pass a ≤30-minute check; "
            "a 'likely_buyer' campaign named 'Aug 2025 Bordering Tour — Client 2' exists; "
            "one email to client 2 with subject 'Bordering Tour — 2025-08-24' (template_code 'likely_buyer') using that map URL as body_uri is on record; "
            "two holds exist: 09:55–10:05Z 'Depart for first stop' at 'Client Home' (source 'viewing') and 13:10–13:25Z 'Post-tour debrief' at 'Phone' (source 'follow_up'); "
            "log an audit 'open_house_route_built' on the route and then read the route again to prove state."
        ),
        actions=[
            Action(name="fetch_neighborhood", kwargs={"neighborhood_id": 1}),
            Action(name="list_adjacent_neighborhoods", kwargs={"neighborhood_id": 1}),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/dt_mid_c2_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Bordering Tour — Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Tour — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/dt_mid_c2_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 3,
                    "action": "open_house_route_built",
                    "entity_type": "routes",
                    "entity_id": 11,
                    "metadata_json": {"stops": ["HTX001", "HTX004", "HTX005"]},
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
        ],
        outputs=[
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_27",
        instruction=(
            "You prepare seller‑broker outreach for client 5 under broker 5 covering properties ['HTX201','HTX205','HTX207']. End state: an outreach drafts bundle exists; "
            "a campaign titled 'Aug 2025 Seller Outreach — Client 5' exists and sends one email with subject 'Seller Outreach Drafts' (template 'general_update') and body URI "
            "'https://test.storage.com/drafts/client_5_props_3.pdf'; and a follow‑up hold on 2025-08-22 from 21:10Z to 21:30Z titled 'Review outreach drafts' at 'Phone' (source 'follow_up') "
            "appears on the calendar. Verify via the campaign record, email log, and calendar."
        ),
        actions=[
            Action(
                name="draft_seller_broker_batch",
                kwargs={"client_id": 5, "property_ids": ["HTX201", "HTX205", "HTX207"]},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Seller Outreach — Client 5",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Seller Outreach Drafts",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/drafts/client_5_props_3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_28",
        instruction=(
            "You produce and deliver a comparable report for client 10 under broker 4. End state: a comp report is saved for "
            "subject_property_id 'HTX072' (created_by_broker_id 4) with status 'draft', then updated to 'sent_to_client'; "
            "verification reads show the report and its comparables/documents; a 'likely_buyer' campaign named "
            "'Aug 2025 Comp Report — Client 10' exists; one email to client 10 with subject 'Comp Report Delivered' and body_uri "
            "'https://test.storage.com/emails/comp_report_c10.html' is recorded under the campaign; and a follow‑up hold exists "
            "for 2025‑08‑22 18:00–18:20Z titled 'Comp report debrief' at 'Video — Zoom' (source 'follow_up', notes 'CMA review & Q&A'). "
            "Prove by reading back the comp report details after both save and status update, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 10,
                    "subject_property_id": "HTX072",
                    "created_by_broker_id": 4,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Comp Report — Client 10",
                    "type": "likely_buyer",
                    "created_by": 4,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Comp Report Delivered",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comp_report_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 10}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 10}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_29",
        instruction=(
            "You stage a Sugar Land tour for client 11 under broker 6 on 2025‑08‑25. End state: a route exists for client 11 with ordered stops ['SL_501','SL_512','SL_498'] and map link "
            "'https://maps.example.com/route/c11_aug25' stored verbatim; the route is readable; drive‑time feasibility is confirmed with max 25 minutes between hops; "
            "a campaign titled 'Aug 2025 Sugar Land Tour — Client 11' exists and sends one email 'Your Sugar Land Tour' (template 'general_update') using "
            "'https://test.storage.com/emails/sl_tour_c11.html'; and a pre‑tour client meeting on 2025-08-25 from 08:30Z to 08:50Z titled 'Pre-tour brief' at 'Video — Zoom' appears on the calendar. "
            "Verify via route details, drive‑time check, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 11,
                    "date": "2025-08-25",
                    "stops_ordered_json": ["SL_501", "SL_512", "SL_498"],
                    "map_url": "https://maps.example.com/route/c11_aug25",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["SL_501", "SL_512", "SL_498"],
                    "max_minutes": 25,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Sugar Land Tour — Client 11",
                    "type": "general_update",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Your Sugar Land Tour",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/sl_tour_c11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 11}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 11}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_30",
        instruction=(
            "You create a Saturday route for client 12 under broker 6. Final state: a route dated 2025‑08‑23 with ordered stops "
            "['HTX032','HTX036','HTX049'] is saved using map URL 'https://maps.google.com/route/weekend_c12_20250823' and passes a 30‑minute hop check; "
            "a 'likely_buyer' campaign named 'Aug 2025 Saturday Tour — Client 12' exists; an email to client 12 with subject 'Saturday Route — 2025‑08‑23' "
            "and body_uri 'https://maps.google.com/route/weekend_c12_20250823' is recorded; and two holds exist — 09:40–09:50Z titled 'Depart for first stop' "
            "at 'Client Home' (source 'viewing') and 13:10–13:30Z titled 'Tour debrief' at 'Video — Zoom' (source 'follow_up', notes 'Next steps & offers'). "
            "Prove by reading the route details, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 12,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX032", "HTX036", "HTX049"],
                    "map_url": "https://maps.google.com/route/weekend_c12_20250823",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX032", "HTX036", "HTX049"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Saturday Tour — Client 12",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 12,
                    "broker_id": 6,
                    "subject": "Saturday Route — 2025-08-23",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/weekend_c12_20250823",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 12}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 12}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_31",
        instruction=(
            "You prepare a compact shortlist for client 11 with broker 6. The final state must include: a 'likely_buyer' campaign named "
            "'Aug 2025 Compact Shortlist — Client 11'; a context search run in neighborhoods [1, 2] with price_min 200000, price_max 900000, "
            "beds 1, baths 1, sqft_min 800, sqft_max 2200, limit 8; one email to client 11 filed under the created campaign with subject "
            "'Shortlist & Saturday Route', template_code 'likely_buyer', and body_uri "
            "'https://test.storage.com/emails/compact_shortlist_11.html'; a Saturday (2025‑08‑23) route stored with ordered stops "
            "['HTX036','HTX032','HTX049'] at map URL 'https://maps.google.com/route/htx_011_20250823'; and two Saturday holds for client 11: "
            "11:00–11:30Z titled 'Shortlist review' (location 'Video — Zoom', notes 'Review shortlist & route', source 'follow_up') and "
            "12:00–12:30Z titled 'Saturday Schedule Check-In' (location 'Phone', notes 'Confirm times & transport', source 'follow_up'). "
            "Prove the writes by reading back the campaign, the email, the route details, and the calendar events."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Compact Shortlist — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(
                name="query_listings_by_neighborhoods",
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
                name="persist_outbound_email",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Shortlist & Saturday Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/compact_shortlist_11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 11}),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 11,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX036", "HTX032", "HTX049"],
                    "map_url": "https://maps.google.com/route/htx_011_20250823",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 6,
                    "client_id": 11,
                    "title": "Saturday Schedule Check-In",
                    "start_at": "2025-08-23T12:00:00Z",
                    "end_at": "2025-08-23T12:30:00Z",
                    "location": "Phone",
                    "notes": "Confirm times & transport",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 11}),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_32",
        instruction=(
            "You deliver a combined comps-and-tour plan for client 2 under broker 3. End state: a comp report for subject_property_id 'HTX041' "
            "(created_by_broker_id 3) is saved with status 'draft' and confirmed; a Saturday route dated 2025-08-23 is saved with ordered stops "
            "['HTX041','HTX032','HTX036'] and map URL 'https://maps.google.com/route/comp_tour_c2_20250823' and meets a ≤30-minute hop constraint; "
            "a 'likely_buyer' campaign named 'Aug 2025 Comp + Tour — Client 2' exists; two emails are recorded under the campaign for client 2 — one using "
            "template_code 'likely_buyer' with subject 'Comps Overview' and body_uri 'https://test.storage.com/emails/comps_overview_c2.html', and "
            "another using template_code 'likely_buyer' with subject 'Saturday Tour Plan' and body_uri "
            "'https://maps.google.com/route/comp_tour_c2_20250823'; and two holds exist — 2025-08-22 18:00–18:20Z titled 'Comps review' at 'Phone' "
            "(source 'follow_up') and 2025-08-23 09:40–09:50Z titled 'Depart for tour' at 'Client Home' (source 'viewing'). Log an audit "
            "'routes_shared_and_viewings_set' on the route."
        ),
        actions=[

            Action(
                name="create_or_update_comp_report",
                kwargs={"client_id": 2, "subject_property_id": "HTX041", "created_by_broker_id": 3,
                        "final_status": "draft"}
            ),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 1, "status": "confirmed"}
            ),

            Action(
                name="validate_drive_time_hops",
                kwargs={"property_ids": ["HTX041", "HTX032", "HTX036"], "max_minutes": 30}
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX041", "HTX032", "HTX036"],
                    "map_url": "https://maps.google.com/route/comp_tour_c2_20250823",
                    "created_by_broker_id": 3
                }
            ),

            Action(
                name="new_campaign_creator",
                kwargs={"name": "Aug 2025 Comp + Tour — Client 2", "type": "likely_buyer", "created_by": 3}
            ),

            Action(
                name="compose_client_email",
                kwargs={"template_code": "likely_buyer", "client_id": 2, "subject": "Comps Overview"}
            ),
            Action(
                name="persist_outbound_email",
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
                name="compose_client_email",
                kwargs={"template_code": "likely_buyer", "client_id": 2, "subject": "Saturday Tour Plan"}
            ),
            Action(
                name="persist_outbound_email",
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
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
                name="append_audit_event",
                kwargs={"actor_id": 3, "action": "routes_shared_and_viewings_set", "entity_type": "routes",
                        "entity_id": "c2_2025-08-23"}
            ),
        ],
        outputs=[
            "comp_report_status=confirmed",
            "hops_valid<=30",
            "route_date=2025-08-23",
            "campaign_name=Aug 2025 Comp + Tour — Client 2",
            "email_persisted=Comps Overview",
            "email_persisted=Saturday Tour Plan",
            "event_title=Comps review",
            "event_title=Depart for tour",
            "audit=routes_shared_and_viewings_set"
        ]
    ),

    Task(
        annotator="v2",
        user_id="task_33",
        instruction=(
            "You create a comps report draft for client 19 under broker 7 and share it. End state: "
            "a comp report is saved for subject_property_id 'HTX044' with status 'draft' and read; "
            "a 'general_update' campaign named 'Aug 2025 CMA Draft — Client 19' exists and is used for one email "
            "with subject 'Your Market Analysis is Ready Draft' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/cma_draft_c19.html'; "
            "a consult hold exists on 2025-08-23 12:40–13:00Z titled 'CMA Draft consult' at 'Phone' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 19,
                    "subject_property_id": "HTX044",
                    "created_by_broker_id": 7,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 CMA Draft — Client 19",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 19,
                    "broker_id": 7,
                    "subject": "Your Market Analysis is Ready Draft",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/cma_draft_c19.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 19}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 19}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_34",
        instruction=(
            "You create a townhouse seeker brief for client 12 with broker 3. End state: "
            "neighborhood 11 details and its bordering IDs are fetched; "
            "listings are searched within [11,1,13] for property_type 'townhouse' and price 128758–279350 (limit 6) as context; "
            "a 'likely_buyer' campaign named 'Aug 2025 Townhouse Path — Client 12' exists; "
            "one email to client 12 with subject 'Townhouse Options' (template_code 'likely_buyer') and body_uri "
            "'https://test.storage.com/emails/townhouse_path_c12.html' is recorded; "
            "a 2025-08-25 14:30–14:50Z hold titled 'Townhouse plan' at 'Phone' (source 'follow_up'). Verify via reads."
        ),
        actions=[
            Action(name="fetch_neighborhood", kwargs={"neighborhood_id": 11}),
            Action(name="list_adjacent_neighborhoods", kwargs={"neighborhood_id": 11}),
            Action(
                name="query_listings_by_neighborhoods",
                kwargs={
                    "neighborhood_ids": [11, 1, 13],
                    "property_type": "townhouse",
                    "price_min": 128758,
                    "price_max": 279350,
                    "limit": 6,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Townhouse Path — Client 12",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/townhouse_path_c12.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 12}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 12}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_35",
        instruction=(
            "You send a Heights historic shortlist for client 15 under broker 8. "
            "End state: a draft comp report document for subject property ID "
            "'HGTS_HIST_C15_AUG25' exists and is readable; one outbound update is "
            "associated with a campaign titled 'Aug 2025 Heights Historic - Client 15' "
            "with subject 'Heights Historic Picks' using body URI "
            "'https://test.storage.com/emails/heights_historic_c15.html' and the "
            "general-update template; and a viewing-plan hold on 2025-08-30 from 14:00Z to "
            "14:20Z titled 'Heights tour plan' at '1234 Heights Boulevard, Houston, TX 77008' "
            "(source 'viewing') appears on the calendar. Verify through the comp report, "
            "the campaign record, the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 15,
                    "subject_property_id": "HGTS_HIST_C15_AUG25",
                    "created_by_broker_id": 8,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Heights Historic - Client 15",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Heights Historic Picks",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/heights_historic_c15.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 15}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 8,
                    "client_id": 15,
                    "title": "Heights tour plan",
                    "start_at": "2025-08-30T14:00:00Z",
                    "end_at": "2025-08-30T14:20:00Z",
                    "location": "1234 Heights Boulevard, Houston, TX 77008",
                    "source": "viewing",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 15}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_36",
        instruction=(
            "You assemble a Northside Sunday tour for client 20 under broker 11. Final state: a route for 2025‑08‑24 is saved with ordered stops "
            "['HTX066','HTX067','HTX068'] and map URL 'https://maps.google.com/route/northside_c20_20250824'; a hop check confirms ≤30 minutes between stops; "
            "a 'likely_buyer' campaign named 'Aug 2025 Northside Tour — Client 20' exists; an email to client 20 with subject 'Northside Route — 2025‑08‑24' "
            "and the map URL as body_uri is recorded; and two holds exist — 09:15–09:25Z titled 'Pre‑drive check' at 'Phone' (source 'follow_up') and "
            "12:45–13:05Z titled 'Debrief call' at 'Phone' (source 'follow_up'). Prove by reading the route details, the campaign, the email, and the "
            "calendar events."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 20,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX066", "HTX067", "HTX068"],
                    "map_url": "https://maps.google.com/route/northside_c20_20250824",
                    "created_by_broker_id": 11,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX066", "HTX067", "HTX068"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Northside Tour — Client 20",
                    "type": "likely_buyer",
                    "created_by": 11,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 20,
                    "broker_id": 11,
                    "subject": "Northside Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/northside_c20_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 20}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 20}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_37",
        instruction=(
            "You send a Garden Oaks CMA with financing for client 17 under broker 7. End state: a draft comp report exists and is readable for subject 'GARDEN_OAKS_CMA_C17_AUG25'; "
            "a 30‑year TX mortgage estimate is computed for list price 680000; a campaign titled 'Aug 2025 Garden Oaks CMA — Client 17' exists and sends one email "
            "with subject 'CMA + Payment Estimate' (template 'likely_buyer') and body URI 'https://test.storage.com/emails/go_cma_finance_c17.html'; "
            "and a Zoom CMA review on 2025-08-28 from 17:00Z to 17:30Z titled 'CMA review' at 'Video — Zoom' (source 'client_meeting') is on the calendar. "
            "Verify via comp report read, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 17,
                    "subject_property_id": "GARDEN_OAKS_CMA_C17_AUG25",
                    "created_by_broker_id": 7,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 17,
                    "list_price": 680000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Garden Oaks CMA — Client 17",
                    "type": "likely_buyer",
                    "created_by": 7,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 17,
                    "broker_id": 7,
                    "subject": "CMA + Payment Estimate",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/go_cma_finance_c17.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 17}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 17}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_38",
        instruction=(
            "You prepare a sales-context financing snapshot for client 8 under broker 12 focused on Medical Center condos. End state: "
            "recent sales are fetched for property_id 'HTX049' (limit 3) as context; "
            "a mortgage estimate for client 8 at list_price 550000 is computed; "
            "a 'general_update' campaign named 'Aug 2025 Med Center Finance — Client 8' exists and is used for one email "
            "with subject 'Medical Center Finance Snapshot' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/medcenter_finance_c8.html'; "
            "a consult hold exists 2025-08-26 09:00–09:30Z titled 'Financing consult' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="recent_sales_for_property",
                kwargs={"property_id": "HTX049", "limit": 3},
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 8, "list_price": 550000},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Med Center Finance — Client 8",
                    "type": "general_update",
                    "created_by": 12,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Medical Center Finance Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/medcenter_finance_c8.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 8}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 8}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_39",
        instruction=(
            "You prep a neighborhood open‑house sweep for client 20 under broker 7 across neighborhoods [11,6,13] for the 2025‑08‑23 weekend. End state: the neighborhood open‑house windows are reviewed; "
            "a campaign titled 'Aug 2025 Open House Sweep — Client 20' exists and sends one email 'Open House Sweep' (template 'general_update') with body URI 'https://test.storage.com/emails/oh_sweep_c20.html'; "
            "and a buffer hold on 2025-08-24 from 12:40Z to 13:00Z titled 'Open House Sweep Q&A' at 'Cafe — Montrose' (source 'follow_up') appears on the calendar. Verify via the campaign/email and the calendar."
        ),
        actions=[
            Action(
                name="open_house_windows_by_neighborhoods",
                kwargs={"neighborhood_ids": [11, 6, 13]},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Open House Sweep — Client 20",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 20,
                    "broker_id": 7,
                    "subject": "Open House Sweep",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/oh_sweep_c20.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 20}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 7,
                    "client_id": 20,
                    "title": "Open House Sweep Q&A",
                    "start_at": "2025-08-24T12:40:00Z",
                    "end_at": "2025-08-24T13:00:00Z",
                    "location": "Cafe — Montrose",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 20}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_40",
        instruction=(
            "You coordinate weekend logistics for clients 6 and 7 under broker 4. Required end state: a 'general_update' campaign named "
            "'Aug 2025 Weekend Logistics - C6 & C7' exists; emails are on record under that campaign with subject 'Weekend Logistics' "
            "and body_uris 'https://test.storage.com/emails/weekend_c6.html' (client 6) and 'https://test.storage.com/emails/weekend_c7.html' (client 7); "
            "and two holds exist — client 6 at 2025-08-23 13:00-13:20Z titled 'Prep call' at 'Video - Zoom' (source 'follow_up') "
            "and client 7 at 2025-08-23 13:30-13:50Z titled 'Prep call' at 'Video - Zoom' (source 'follow_up'). Prove by reading back the campaign, "
            "both clients’ emails, and both clients’ calendar events."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Weekend Logistics - C6 & C7",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 6,
                    "subject": "Weekend Logistics",
                    "slug": "weekend_c6",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 6,
                    "broker_id": 4,
                    "subject": "Weekend Logistics",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 6}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 7,
                    "subject": "Weekend Logistics",
                    "slug": "weekend_c7",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 7,
                    "broker_id": 4,
                    "subject": "Weekend Logistics",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_c7.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 7}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 6}),
            Action(name="list_client_calendar_events", kwargs={"client_id": 7}),
        ],
        outputs=[
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_41",
        instruction=(
            "You deliver a v2 briefing for client 3 under broker 1. End state: a briefing document is generated with "
            "version_tag 'v2' so it is stored at 'https://test.storage.com/details/client_briefing_003_v2.pdf'; a "
            "'general_update' campaign named 'Aug 2025 Briefing v2 — Client 3' exists; one email to client 3 using "
            "template_code 'general_update' with subject 'Updated Briefing (v2)' and body_uri "
            "'https://test.storage.com/details/client_briefing_003_v2.pdf' is on record under that campaign; and a "
            "review hold exists on 2025‑08‑22 16:30–16:50Z titled 'Briefing v2 review' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="create_briefing_doc",
                kwargs={"client_id": 3, "broker_id": 1, "version_tag": "v2"},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Briefing v2 — Client 3",
                    "type": "general_update",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Updated Briefing (v2)",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_003_v2.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 3}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 3}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_42",
        instruction=(
            "You prepare a pre-approval and tour plan for client 1 under broker 3. End state: a mortgage estimate is computed at list_price 600000 (context); "
            "a 'general_update' campaign named 'Aug 2025 Pre-approval & Tour - Client 1' exists; an email to client 1 with subject "
            "'Pre-approval & Tour Plan' and body_uri 'https://test.storage.com/emails/preapprove_tour_c1.html' is recorded under the campaign; "
            "and two holds exist — 2025-08-22 09:00-09:30Z titled 'Lender pre-approval' at 'Phone' (source 'follow_up') and "
            "2025-08-24 15:00-16:30Z titled 'Tour window' at 'TBD' (source 'viewing'). Prove by reading back the campaign, the email, "
            "and the calendar events."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 1, "list_price": 600000},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Pre-approval & Tour - Client 1",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Pre-approval & Tour Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/preapprove_tour_c1.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 1}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 1}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_43",
        instruction=(
            "You coordinate a four‑stop tour for client 1 under broker 3. Final state: a route for 2025‑08‑24 is saved with ordered stops "
            "['HTX021','HTX025','HTX029','HTX030'] and map URL 'https://maps.google.com/route/four_stop_c1_20250824'; the route passes a 30‑minute hop check; "
            "a 'likely_buyer' campaign named 'Aug 2025 Four‑Stop Tour — Client 1' exists; an email to client 1 with subject 'Four‑Stop Tour — 2025‑08‑24' "
            "and the map URL as body_uri is recorded; and two holds exist — 09:20–09:30Z titled 'Pre‑drive sync' at 'Phone' (source 'follow_up', "
            "notes 'Confirm sequence & parking') and 14:00–14:20Z titled 'Tour debrief' at 'Video — Zoom' (source 'follow_up'). Prove by reading the route "
            "details, the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 1,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX021", "HTX025", "HTX029", "HTX030"],
                    "map_url": "https://maps.google.com/route/four_stop_c1_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX021", "HTX025", "HTX029", "HTX030"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Four‑Stop Tour — Client 1",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Four-Stop Tour — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/four_stop_c1_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 1}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 1}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_44",
        instruction=(
            "You prepare and deliver comps for client 14 under broker 5. Final state: a comp report is saved for subject_property_id 'HTX060' "
            "(created_by_broker_id 5) with status 'draft', verified via read, then updated to 'sent_to_client' and re‑confirmed; a follow‑up hold exists "
            "for 2025‑08‑22 18:30–18:50Z titled 'Discuss comp findings' at 'Phone' (source 'follow_up'). Prove by reading back the comp report details "
            "after both save and status update, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 14,
                    "subject_property_id": "HTX060",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 14}),
        ],
        outputs=[
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_45",
        instruction=(
            "You plan a route day for client 2 under broker 3. End state: a route for 2025-08-24 is stored with ordered stops "
            "['HTX015','HTX016','HTX017'] and map URL 'https://maps.google.com/route/htx_plan_c2_20250824'; hops meet a 30-minute limit; "
            "a 'likely_buyer' campaign named 'Aug 2025 Route Day - Client 2' exists; an email to client 2 with subject 'Route Day Plan - 2025-08-24' "
            "and body_uri 'https://test.storage.com/emails/routeday_c2.html' is recorded under the campaign; and two holds exist for client 2 — "
            "08:30-08:45Z titled 'Kickoff call' at 'Phone' (source 'follow_up') and 13:00-13:20Z titled 'Post-route debrief' at 'Video - Zoom' "
            "(source 'follow_up'). Prove by reading back the route details, campaign, email, and calendar events."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 2,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX015", "HTX016", "HTX017"],
                    "map_url": "https://maps.google.com/route/htx_plan_c2_20250824",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX015", "HTX016", "HTX017"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Route Day - Client 2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "likely_buyer",
                    "client_id": 2,
                    "subject": "Route Day Plan - 2025-08-24",
                    "slug": "routeday_c2",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Route Day Plan - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/routeday_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_46",
        instruction=(
            "You deliver a Downtown two-bed single-family briefing for client 3 under "
            "broker 1. End state: a draft comp report document exists for subject "
            "property ID 'DT_SF2B2B_C3_AUG25' and is readable; one client update is tied "
            "to a campaign titled 'Aug 2025 Downtown Fit - Client 3' with subject "
            "'Downtown Options' using body URI 'https://test.storage.com/emails/dt_fit_c3.html' "
            "and the likely-buyer template; and two calendar holds for 2025-08-24 are "
            "present: 10:30-10:50Z 'Depart for first stop' at 'Client Home' (source 'viewing') "
            "and 13:20-13:40Z 'Post-tour buffer' at 'Phone' (source 'follow_up'). "
            "Verify by reading the comp report, the campaign, the client’s email log, "
            "and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 3,
                    "subject_property_id": "DT_SF2B2B_C3_AUG25",
                    "created_by_broker_id": 1,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Downtown Fit - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Downtown Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/dt_fit_c3.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 3}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 3}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_47",
        instruction=(
            "You deliver a Medical Center luxury snapshot for client 8 under broker 5. End state: a concise inventory view captures up to six active listings across neighborhoods [13,9,14,15,11] within the 273024–868888 price band; a finance estimate for client 8 is produced using a target price of 800000 over 30 years in region TX; one client update is anchored to a campaign titled 'Aug 2025 Med Center Luxury — Client 8' with subject 'Luxury Snapshot' that uses 'https://test.storage.com/emails/medcenter_luxury_c8.html' as the body and the likely-buyer template; and a Zoom consult on 2025-08-26 from 10:00Z to 10:30Z titled 'Luxury plan consult' is on the calendar. Prove completion by showing the outreach in the email log, the campaign record, the calendar entry, and the finance estimate."
        ),
        actions=[
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [13, 9, 14, 15, 11],
                    "price_min": 273024,
                    "price_max": 868888,
                    "limit": 6,
                },
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 8,
                    "list_price": 800000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Med Center Luxury — Client 8",
                    "type": "likely_buyer",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 8,
                    "broker_id": 5,
                    "subject": "Luxury Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/medcenter_luxury_c8.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 8}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 8}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_48",
        instruction=(
            "You broaden client 4’s condo search under broker 2. End state: "
            "neighborhood 15 details and bordering IDs are fetched (context); "
            "listings are searched within the exact bordering set returned for property_type 'apartment' and price 201911–507035 (limit 6) for context; "
            "a 'general_update' campaign named 'Aug 2025 Bordering Apartment Picks — Client 4' exists and is used for one email "
            "with subject 'Bordering Options' (template_code 'general_update') and body_uri 'https://test.storage.com/emails/border_apts_c4.html'; "
            "create a 2025-08-22 15:00–15:30Z hold titled 'Pre-tour call' at 'Video — Zoom' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(name="fetch_neighborhood", kwargs={"neighborhood_id": 15}),
            Action(name="list_adjacent_neighborhoods", kwargs={"neighborhood_id": 15}),
            Action(
                name="query_listings_by_neighborhoods",
                kwargs={
                    "neighborhood_ids": [14],
                    "property_type": "apartment",
                    "price_min": 201911,
                    "price_max": 507035,
                    "limit": 6,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Bordering Apartment Picks — Client 4",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Bordering Options",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/border_apts_c4.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 4}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 4}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_49",
        instruction=(
            "You assemble a post‑tour follow‑up for client 10 with broker 4. End state: a briefing document is generated; a "
            "'likely_buyer' campaign named 'Aug 2025 Tour Follow‑Ups — Client 10' exists; and one email to client 10 is filed under "
            "the created campaign with subject 'Your Tour Follow‑Up Packet', template_code 'likely_buyer', and body_uri "
            "'https://test.storage.com/details/client_briefing_010_v1.pdf'. A follow‑up calendar hold exists for client 10 on "
            "Saturday 2025‑08‑23 11:30–12:00Z with the exact title 'Tour recap', location 'Phone', notes 'Recap post‑tour', and "
            "source 'follow_up'. Prove the writes by reading back the campaign, the email for client 10, and the calendar event."
        ),
        actions=[
            Action(
                name="create_briefing_doc", kwargs={"client_id": 10, "broker_id": 4}
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Tour Follow‑Ups — Client 10",
                    "type": "likely_buyer",
                    "created_by": 4,
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Your Tour Follow‑Up Packet",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/details/client_briefing_010_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 10}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 10}),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_50",
        instruction=(
            "You prep a weekend open‑house snapshot for client 4 under broker 2. Final state: open‑house windows are fetched for properties "
            "['HTX030','HTX031'] for 2025‑08‑23 through 2025‑08‑24 (context); a 'general_update' campaign named 'Aug 2025 Weekend Open Houses — Client 4' "
            "exists; an email to client 4 with subject 'Weekend Open Houses' and body_uri 'https://test.storage.com/emails/weekend_open_c4.html' is "
            "recorded under the campaign; and a planning hold exists at 2025‑08‑23 08:30–08:45Z titled 'Plan the route' at 'Phone' (source 'follow_up'). "
            "Prove by reading back the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="open_houses_for_properties",
                kwargs={
                    "property_ids": ["HTX030", "HTX031"],
                    "date_from": "2025-08-23",
                    "date_to": "2025-08-24",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Weekend Open Houses — Client 4",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 4,
                    "broker_id": 2,
                    "subject": "Weekend Open Houses",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/weekend_open_c4.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 4}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 4}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_51",
        instruction=(
            "You deliver a post‑tour recap for client 3 under broker 1. End state: a briefing document (version 'aug25') is generated and referenced in one email under "
            "a campaign titled 'Aug 2025 Tour Recap — Client 3' with subject 'Tour Recap & Next Steps' (template 'general_update') and body URI "
            "'https://test.storage.com/details/client_briefing_003_aug25.pdf'; a draft comp report for 'TOUR_RECAP_C3_AUG25' is saved and readable; "
            "an audit event 'recap_sent' is recorded on that comp report and the report is re‑read; and a follow‑up phone hold on 2025-08-29 from 09:10Z to 09:30Z titled 'Recap call' "
            "(source 'follow_up') appears on the calendar. Verify via comp report reads, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="create_briefing_doc",
                kwargs={"client_id": 3, "broker_id": 1, "version_tag": "aug25"},
            ),
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 3,
                    "subject_property_id": "TOUR_RECAP_C3_AUG25",
                    "created_by_broker_id": 1,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Tour Recap — Client 3",
                    "type": "general_update",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Tour Recap & Next Steps",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_003_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 3}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 1,
                    "action": "recap_sent",
                    "entity_type": "comp_reports",
                    "entity_id": 9,
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 3}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_52",
        instruction=(
            "You deliver a comps‑and‑status package for client 6 under broker 2. End state: a comp report for subject_property_id 'HTX058' "
            "(created_by_broker_id 2) is saved with status 'draft' and confirmed; then its status is updated to 'sent_to_client' and re‑confirmed; "
            "a 'likely_buyer' campaign named 'Aug 2025 Comps Sent — Client 6' exists; one email to client 6 using template_code 'likely_buyer' with "
            "subject 'Comps Sent' and body_uri 'https://test.storage.com/emails/comps_sent_c6.html' is recorded under the campaign; and a debrief hold "
            "exists on 2025‑08‑22 18:40–19:00Z titled 'Comps debrief' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 6,
                    "subject_property_id": "HTX058",
                    "created_by_broker_id": 2,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Comps Sent — Client 6",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Comps Sent",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comps_sent_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 6}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 6}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_53",
        instruction=(
            "You plan an open‑house tour for client 3 with broker 1. End state required: there exists a 'likely_buyer' "
            "campaign named 'Aug 2025 Open House — Client 3'; the route for 2025‑08‑24 is saved with the exact ordered "
            "stops ['HTX001','HTX004','HTX005'] and map URL 'https://maps.google.com/route/htx_003_20250824'; drive‑time "
            "feasibility is confirmed at a maximum of 30 minutes per hop. One email is recorded for client 3 from broker 1 "
            "under the created campaign with subject 'Open House Route — 2025‑08‑24' and body_uri "
            "'https://maps.google.com/route/htx_003_20250824'. Two calendar holds exist for client 3 on 2025‑08‑24: "
            "10:00–10:30Z titled 'Depart for first stop' (location 'Client Home', notes 'Open-house tour', source 'viewing') "
            "and 13:00–13:30Z titled 'Broker follow‑up' (location 'Office', notes 'Post-tour recap', source 'follow_up'). "
            "Prove the writes by reading back the campaign, the stored route details, the email, and the calendar events; "
            "also record audits for the campaign creation and for the saved route."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Open House — Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 3,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/htx_003_20250824",
                    "created_by_broker_id": 1,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Open House Route — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/htx_003_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 3}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 3}),
            Action(
                name="append_audit_event",
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
                name="append_audit_event",
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
        outputs=[
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_54",
        instruction=(
            "You run paired likely-buyer updates for clients 1 and 2 from broker 3. End state: "
            "search_listings matches each client’s neighborhoods (client 1: [5,9,8,10,14], client 2: [11,1]) with limit 6 each for context; "
            "a 'likely_buyer' campaign named 'Aug 2025 Paired Likely Buyers — C1 & C2' exists and is used for two emails "
            "(subject 'August Listings Shortlist', template_code 'likely_buyer', body_uri 'https://test.storage.com/emails/aug_shortlist.html'); "
            "create two holds on 2025-08-23 titled 'Intro call about shortlist' at 'Phone' (source 'follow_up'): "
            "client 1 at 15:00–15:30Z and client 2 at 16:00–16:20Z. Verify by reading campaign, emails, and both calendars."
        ),
        actions=[
            Action(
                name="query_active_listings",
                kwargs={"neighborhood_ids": [5, 9, 8, 10, 14], "limit": 6},
            ),
            Action(
                name="query_active_listings",
                kwargs={"neighborhood_ids": [11, 1], "limit": 6},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Paired Likely Buyers — C1 & C2",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
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
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "August Listings Shortlist",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/aug_shortlist.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 1}),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 1}),
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_55",
        instruction=(
            "You send a preference-targeted update to client 3 under broker 1. Final state: client 3's stored "
            "preferences have been consulted and the listings search exactly reflects those constraints—neighborhoods "
            "[1,12,2,4,5], price 200505–631914, beds=2, baths=2 (context); a 'likely_buyer' campaign named "
            "'Aug 2025 Targeted Listings - Client 3' exists and the outbound message is filed under it; one email exists "
            "for client 3 with subject 'Tailored Listings Update' and body_uri 'https://test.storage.com/emails/prefs_c3.html'; "
            "and a check-in hold exists for 2025-08-23 17:00–17:20Z titled 'Listings check-in' at 'Phone' with source 'follow_up'."
        ),
        actions=[
            Action(name="fetch_client_prefs", kwargs={"client_id": 3}),
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [1, 12, 2, 4, 5],
                    "price_min": 200505,
                    "price_max": 631914,
                    "beds": 2,
                    "baths": 2,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Targeted Listings - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Tailored Listings Update",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/prefs_c3.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 3}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Listings check-in",
                    "start_at": "2025-08-23T17:00:00Z",
                    "end_at": "2025-08-23T17:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 3}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_56",
        instruction=(
            "You run a two‑client general update for clients 13 and 14 under broker 5. Final state: a listings context search runs for "
            "neighborhoods [2,3,4], up to 6 results (limit 6); a 'general_update' campaign named 'Aug 2025 Multi‑Client Update — C13 & C14' exists; "
            "two emails are recorded — both with subject 'August Market & Listings' and body_uri "
            "'https://test.storage.com/emails/aug_market_multi.html' — one for client 13 and one for client 14 under the same campaign; "
            "and two holds exist on 2025‑08‑22: client 13 at 16:00–16:20Z and client 14 at 16:30–16:50Z, both titled 'Discuss August update' "
            "at 'Phone' (source 'follow_up'). Prove by reading back the campaign, both clients’ emails, and both clients’ calendar events."
        ),
        actions=[
            Action(
                name="query_active_listings",
                kwargs={"neighborhood_ids": [2, 3, 4], "limit": 6},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Multi‑Client Update — C13 & C14",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
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
                name="persist_outbound_email",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "August Market & Listings",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/aug_market_multi.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 13}),
            Action(name="list_client_emails", kwargs={"client_id": 14}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 13}),
            Action(name="list_client_calendar_events", kwargs={"client_id": 14}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_57",
        instruction=(
            "You launch a Downtown/Midtown stats update for client 1 under broker 1. End state: "
            "a 'general_update' campaign named 'Aug 2025 DT/Midtown Stats — Client 1' exists and is used for one email to client 1 "
            "with subject 'DT/Midtown Q3 Snapshot' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/dt_mid_q3_c1.html'; "
            "a follow-up hold exists 2025-08-25 09:00–09:30Z titled 'Follow-up Check-in — DT/Midtown' at 'Phone' (source 'follow_up'); "
            "an audit 'campaign_sent' is posted on the campaign and the campaign is read to prove state."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 DT/Midtown Stats — Client 1",
                    "type": "general_update",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 1,
                    "broker_id": 1,
                    "subject": "DT/Midtown Q3 Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/dt_mid_q3_c1.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 1}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 1,
                    "client_id": 1,
                    "title": "Follow-up Check-in — DT/Midtown",
                    "start_at": "2025-08-25T09:00:00Z",
                    "end_at": "2025-08-25T09:30:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 1}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 1,
                    "action": "campaign_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_58",
        instruction=(
            "You create an evening Midtown route for client 9 under broker 2. End state: "
            "a route dated 2025-08-24 with ordered stops ['HTX021','HTX025','HTX030'] and map "
            "'https://maps.google.com/route/midtown_evening_c9_20250824' is saved and read; hops pass ≤30 minutes; "
            "a 'likely_buyer' campaign named 'Aug 2025 Midtown Evening — Client 9' exists and is used for one email "
            "with subject 'Evening Route — Midtown' (template_code 'likely_buyer') and that map URL as body_uri; "
            "a 09:30–09:45Z pre-drive sync hold at 'Phone' (source 'follow_up') exists; "
            "audit 'routes_shared_and_viewings_set' is posted and route re-read."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX021", "HTX025", "HTX030"],
                    "map_url": "https://maps.google.com/route/midtown_evening_c9_20250824",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX021", "HTX025", "HTX030"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Midtown Evening — Client 9",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Evening Route — Midtown",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/midtown_evening_c9_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 9}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 2,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_59",
        instruction=(
            "You plan a Sunday drive for client 3 under broker 1 using open-house windows (context) for properties "
            "HTX001, HTX004, and HTX005 across 2025-08-22 to 2025-08-25. By completion, a route dated 2025-08-24 covering those "
            "three properties is saved with a shareable map link and confirmed to meet the 30-minute hop limit. A 'likely_buyer' "
            "campaign titled 'Aug 2025 Sunday Drive - Client 3' is active, and exactly one notification email to client 3 exists "
            "with subject 'Sunday Drive Plan - 2025-08-24' that includes the map link. A brief pre-drive check-in is scheduled that "
            "morning on the calendar (source 'follow_up'). The resulting state should be verifiable via subsequent reads."
        ),
        actions=[
            Action(
                name="open_houses_for_properties",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "date_from": "2025-08-22",
                    "date_to": "2025-08-25",
                },
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 3,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX001", "HTX004", "HTX005"],
                    "map_url": "https://maps.google.com/route/htx_c3_sunday_20250824",
                    "created_by_broker_id": 1,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX001", "HTX004", "HTX005"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Sunday Drive - Client 3",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "likely_buyer",
                    "client_id": 3,
                    "subject": "Sunday Drive Plan - 2025-08-24",
                    "slug": "sunday_c3",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 3,
                    "broker_id": 1,
                    "subject": "Sunday Drive Plan - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/sunday_c3.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 3}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 1,
                    "client_id": 3,
                    "title": "Pre-drive check-in",
                    "start_at": "2025-08-24T09:45:00Z",
                    "end_at": "2025-08-24T10:00:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 3}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_60",
        instruction=(
            "You assemble a curated shortlist by ID for client 11 under broker 6. End state: "
            "listings [15,16,17] are read with property details (context); "
            "a 'likely_buyer' campaign named 'Aug 2025 Curated Picks — Client 11' exists and is used for one email "
            "with subject 'Handpicked Listings' (template_code 'likely_buyer') and body_uri "
            "'https://test.storage.com/emails/curated_picks_c11.html'; "
            "place a 2025-08-24 11:10–11:30Z hold titled 'Curated picks debrief' at 'Phone' (source 'follow_up'). Verify by reads."
        ),
        actions=[
            Action(
                name="gather_listings_with_properties",
                kwargs={"listing_ids": [15, 16, 17]},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Curated Picks — Client 11",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 11,
                    "broker_id": 6,
                    "subject": "Handpicked Listings",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/curated_picks_c11.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 11}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 11}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_61",
        instruction=(
            "You expand search guidance for client 2 under broker 3 using only areas bordering neighborhood 1. "
            "By completion: neighborhood 1 is documented together with its bordering neighborhood IDs; listings context reflects results drawn "
            "strictly from those bordering IDs with price 300000–650000, beds=2, baths=2, limit 6; a 'general_update' campaign titled "
            "'Aug 2025 Bordering Preview — Client 2' is on record; exactly one message to client 2 exists with subject 'Bordering Area Shortlist' "
            "(template_code 'general_update') and body_uri 'https://test.storage.com/emails/border_prev_c2.html'; and a follow-up calendar hold is scheduled "
            "for 2025-08-22 16:00–16:20Z titled 'Bordering shortlist review' at 'Phone' (source 'follow_up'). The resulting state is verifiable in campaign, "
            "email, and client calendar records."
        ),
        actions=[
            Action(name="fetch_neighborhood", kwargs={"neighborhood_id": 1}),
            Action(name="list_adjacent_neighborhoods", kwargs={"neighborhood_id": 1}),
            Action(
                name="query_listings_by_neighborhoods",
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
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Bordering Preview — Client 2",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Area Shortlist",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/border_prev_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_62",
        instruction=(
            "You send a general market update to clients 1 and 2 from broker 3. "
            "Ensure the final state includes: a 'general_update' campaign named 'Aug 2025 General Update — Downtown & Midtown' "
            "that is used for both emails; a context listing pull of up to 8 active listings with no additional filters (limit 8); "
            "two emails to clients 1 and 2 with subject 'Q3 Stats & Listings — Downtown & Midtown' and body_uri "
            "'https://test.storage.com/emails/q3_stats_dt_midtown.html'; and two follow‑up holds on 2025‑08‑23 titled "
            "'Discuss Q3 market update' at 'Video — Zoom' with notes 'Market update follow‑up' (client 1 at 15:00–15:30Z, "
            "client 2 at 16:30–17:00Z)."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 General Update — Downtown & Midtown",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="query_active_listings", kwargs={"limit": 8}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 1,
                    "broker_id": 3,
                    "subject": "Q3 Stats & Listings — Downtown & Midtown",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/q3_stats_dt_midtown.html",
                    "campaign_id": 9,
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Q3 Stats & Listings — Downtown & Midtown",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/q3_stats_dt_midtown.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 1}),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 1}),
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_63",
        instruction=(
            "You craft a finance‑first brief for client 13 with broker 7. The system must show: the client's mortgage profile was "
            "retrieved; pull three recent sale for context against property_id 'HTX003' (limit 3); a general active search was "
            "run (limit 6); and a 'likely_buyer' campaign named 'Aug 2025 Finance‑First — Client 13' exists with one email to client 13 "
            "subject 'Finance‑First Plan & Options', template_code 'likely_buyer', and body_uri "
            "'https://test.storage.com/emails/finance_first_client_13.html'. A consultation hold exists for client 13 on 2025‑08‑26 "
            "18:00–18:30Z with the exact title 'Financing consult', location 'Video — Teams', notes 'Finance-first plan', and source "
            "'client_meeting'"
        ),
        actions=[
            Action(name="retrieve_mortgage_profile", kwargs={"client_id": 13}),
            Action(
                name="recent_sales_for_property",
                kwargs={"property_id": "HTX003", "limit": 3},
            ),
            Action(name="query_active_listings", kwargs={"limit": 6}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Finance‑First — Client 13",
                    "type": "likely_buyer",
                    "created_by": 7,
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 13,
                    "broker_id": 7,
                    "subject": "Finance‑First Plan & Options",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/finance_first_client_13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 13}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 13}),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_64",
        instruction=(
            "You finalize and send a comps report for client 13 with broker 5. End state: "
            "a comp report is saved for 'HTX025' as 'draft' and read; "
            "status is set to 'sent_to_client' and read again; "
            "a 'general_update' campaign named 'Aug 2025 Comps Final — Client 13' exists for one email with subject 'Your Comps Report' "
            "(template_code 'general_update') and body_uri 'https://test.storage.com/emails/comps_final_c13.html'; "
            "a debrief hold exists 2025-08-26 09:00–09:20Z titled 'Comps debrief' at 'USNV Strickland, FPO AP 98640' (source 'client_meeting'). Verify via reads."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 13,
                    "subject_property_id": "HTX025",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Comps Final — Client 13",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 13,
                    "broker_id": 5,
                    "subject": "Your Comps Report",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/comps_final_c13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 13}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 13}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_65",
        instruction=(
            "You finalize a weekend open‑house plan for client 12 under broker 3 using properties ['HTX310','HTX318'] for 2025‑08‑23 to 2025‑08‑24. End state: the window set is reviewed; "
            "a campaign titled 'Aug 2025 Open‑House Weekend — Client 12' exists and is used to send one email with subject 'Your Open House Plan' (template 'general_update') and body URI "
            "'https://test.storage.com/emails/openhouse_plan_c12.html'; and an opening 'Open‑house kickoff' hold on 2025-08-23 from 10:00Z to 10:20Z at 'Client Home' (source 'viewing') "
            "appears on the calendar. Verify via the campaign/email and the calendar."
        ),
        actions=[
            Action(
                name="open_houses_for_properties",
                kwargs={
                    "property_ids": ["HTX310", "HTX318"],
                    "date_from": "2025-08-23",
                    "date_to": "2025-08-24",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Open‑House Weekend — Client 12",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Your Open House Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/openhouse_plan_c12.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 12}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 12}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_66",
        instruction=(
            "You send a new-homeowner touch for client 14 under broker 5. Final state: a 'new_homeowner' campaign named "
            "'Aug 2025 New Homeowner - Client 14' exists; an email to client 14 is recorded under the campaign with subject 'Congrats & Checklist' "
            "and body_uri 'https://test.storage.com/emails/newhome_c14.html'; and a check-in hold is present for 2025-08-25 16:00-16:20Z "
            "titled 'New homeowner check-in' at 'Phone' (source 'follow_up'). Prove by reading back the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 New Homeowner - Client 14",
                    "type": "new_homeowner",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "new_homeowner",
                    "client_id": 14,
                    "subject": "Congrats & Checklist",
                    "slug": "newhome_c14",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "Congrats & Checklist",
                    "template_code": "new_homeowner",
                    "body_uri": "https://test.storage.com/emails/newhome_c14.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 14}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 5,
                    "client_id": 14,
                    "title": "New homeowner check-in",
                    "start_at": "2025-08-25T16:00:00Z",
                    "end_at": "2025-08-25T16:20:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 14}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_67",
        instruction=(
            "You finalize a Downtown luxury finance & route confirm for client 9 under broker 9. End state: "
            "compute a mortgage estimate for client 9 at list_price 750000 (term_years 30, region 'TX') as context; "
            "a route dated 2025-08-24 with stops ['HTX036','HTX032','HTX049'] and map "
            "'https://maps.google.com/route/dt_lux_finance_c9_20250824' is saved/read and passes a ≤30-minute hop check; "
            "a 'general_update' campaign named 'Aug 2025 DT Luxury Finance — Client 9' exists and is used for two emails under that campaign: "
            "one to client 9 with subject 'Luxury Finance Snapshot' (template_code 'general_update') and body_uri "
            "'https://test.storage.com/emails/dt_lux_finance_c9.html', and another to client 9 with subject 'Route Confirm — 2025-08-24' "
            "(template_code 'general_update') using the map URL as body_uri; "
            "log audit 'routes_shared_and_viewings_set' on the route and re-read the route. Verify with reads."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 9,
                    "list_price": 750000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX036", "HTX032", "HTX049"],
                    "map_url": "https://maps.google.com/route/dt_lux_finance_c9_20250824",
                    "created_by_broker_id": 9,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX036", "HTX032", "HTX049"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 DT Luxury Finance — Client 9",
                    "type": "general_update",
                    "created_by": 9,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
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
                name="persist_outbound_email",
                kwargs={
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Route Confirm — 2025-08-24",
                    "template_code": "general_update",
                    "body_uri": "https://maps.google.com/route/dt_lux_finance_c9_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 9}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 9,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
        ],
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_68",
        instruction=(
            "You provide regional financing guidance for client 17 under broker 10. End state: a mortgage estimate is computed for client 17 "
            "at list_price 650000 with term_years 30 and region 'CA-SF' (context); a 'general_update' campaign named 'Aug 2025 SF Financing — Client 17' "
            "exists; an email to client 17 using template_code 'general_update' with subject 'San Francisco Financing Snapshot' and body_uri "
            "'https://test.storage.com/emails/finance_sf_c17.html' is recorded under the campaign; and a consult hold exists for 2025‑08‑22 "
            "22:00–22:30Z titled 'Financing consult (SF)' at 'Video — Zoom' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 17,
                    "list_price": 650000,
                    "term_years": 30,
                    "region": "CA-SF",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 SF Financing — Client 17",
                    "type": "general_update",
                    "created_by": 10,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "San Francisco Financing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_sf_c17.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 17}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 17}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_69",
        instruction=(
            "You prepare and send a Heights CMA to client 5 under broker 5. End state: a draft comp report for subject "
            "'HEIGHTS_HTX012_C5_AUG25' is saved and readable, then updated to 'sent_to_client' and re‑read; a campaign titled "
            "'Aug 2025 Heights Listing CMA — Client 5' exists and sends one email with subject 'CMA for HTX012' (template "
            "'general_update') and body URI 'https://test.storage.com/emails/cma_htx012_c5.html'; and a follow‑up hold on "
            "2025-08-24 from 15:00Z to 15:20Z titled 'CMA questions' at 'Phone' (source 'follow_up') appears on the calendar. "
            "Verify via the comp report reads, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 5,
                    "subject_property_id": "HEIGHTS_HTX012_C5_AUG25",
                    "created_by_broker_id": 5,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="set_comp_report_status",
                kwargs={"report_id": 9, "status": "sent_to_client"},
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Heights Listing CMA — Client 5",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "CMA for HTX012",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/cma_htx012_c5.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_70",
        instruction=(
            "You send investor options to client 18 under broker 5. Final state: condos in neighborhoods [3,4] priced "
            "300000–650000 have been searched (context); a mortgage estimate for client 18 is computed at list_price "
            "400000 (context); a 'general_update' campaign named 'Aug 2025 Investor Picks - Client 18' exists; one email "
            "exists for client 18 with subject 'Investor Picks & Financing' and body_uri "
            "'https://test.storage.com/emails/investor_c18.html' associated to that campaign; and a review hold exists "
            "for 2025-08-24 19:00–19:30Z titled 'Investor review' at 'Video - Zoom' with source 'follow_up'."
        ),
        actions=[
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [3, 4],
                    "property_type": "condo",
                    "price_min": 300000,
                    "price_max": 650000,
                },
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 18, "list_price": 400000},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Investor Picks - Client 18",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 18,
                    "subject": "Investor Picks & Financing",
                    "slug": "investor_c18",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Investor Picks & Financing",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/investor_c18.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 18}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 18}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_71",
        instruction=(
            "You are responsible for client 9 with broker 9. The system must reflect the following end state: "
            "there exists a 'likely_buyer' campaign named 'Aug 2025 Likely Buyer — Client 9 Comp Pack' and all email sends for this task are "
            "filed under the ID returned by that create step (do not assume a constant ID). Using the client's neighborhoods [1, 12, 14, 3] "
            "and price band 276667–628429, up to 6 active context listings (limit 6) are retrieved for reference. Two emails are recorded "
            "for client 9 from broker 9 under that campaign using template_code 'likely_buyer' and body_uri "
            "'https://test.storage.com/emails/comp_pack_client_9.html' with the exact subjects 'Comp Pack Draft — Client 9' and "
            "'Your Comparable & Payment Plan'. In addition, a calendar event exists for client 9 with the exact title "
            "'Review comparable & payment plan' on 2025‑08‑21 15:00–15:30Z, location 'Video — Teams', notes "
            "'30‑min review of comp pack', and source 'client_meeting'. Prove the writes by reading back the campaign, emails, "
            "and the calendar event for client 9."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Likely Buyer — Client 9 Comp Pack",
                    "type": "likely_buyer",
                    "created_by": 9,
                },
            ),
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [1, 12, 14, 3],
                    "price_min": 276667,
                    "price_max": 628429,
                    "limit": 6,
                },
            ),
            Action(
                name="persist_outbound_email",
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
                name="persist_outbound_email",
                kwargs={
                    "client_id": 9,
                    "broker_id": 9,
                    "subject": "Your Comparable & Payment Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comp_pack_client_9.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 9}),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_72",
        instruction=(
            "You distribute seller disclosures to client 5 under broker 5. End state: a briefing document (version 'disclosures_aug25') is generated and referenced; "
            "a campaign titled 'Aug 2025 Disclosures — Client 5' exists and sends one email with subject 'Seller Disclosures' (template 'general_update') using that briefing URI; "
            "and a follow‑up call on 2025-08-23 from 12:10Z to 12:30Z titled 'Disclosure Q&A' at 'Phone' (source 'follow_up') appears on the calendar. Verify via campaign read, email log, and calendar."
        ),
        actions=[
            Action(
                name="create_briefing_doc",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "version_tag": "disclosures_aug25",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Disclosures — Client 5",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 5,
                    "broker_id": 5,
                    "subject": "Seller Disclosures",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_005_disclosures_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_73",
        instruction=(
            "You prepare and share a duplex shortlist for client 6 under broker 2. "
            "End state: a documented snapshot exists for subject property ID 'DPLX_C6_AUG25' "
            "in draft status and is readable; an at-most-six listing view reflects "
            "active duplex options across neighborhoods [8,12,6,5] within 147021-402736 for "
            "context; a single client touch is logged under a campaign titled "
            "'Aug 2025 Duplex Shortlist - Client 6' with subject 'Duplexes That Fit' "
            "using body URI 'https://test.storage.com/emails/duplex_shortlist_c6.html' "
            "and the likely-buyer template; and a follow-up phone hold on 2025-08-23 from "
            "18:40Z to 19:00Z titled 'Shortlist debrief' (source 'follow_up') is on the "
            "client’s calendar. Verify via the saved snapshot, the campaign record, "
            "the client’s email log, and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 6,
                    "subject_property_id": "DPLX_C6_AUG25",
                    "created_by_broker_id": 2,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [8, 12, 6, 5],
                    "property_type": "duplex",
                    "price_min": 147021,
                    "price_max": 402736,
                    "limit": 6,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Duplex Shortlist - Client 6",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Duplexes That Fit",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/duplex_shortlist_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 6}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 6}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_74",
        instruction=(
            "You plan an Inner Loop viewing day for client 16 under broker 8. End state: open‑house windows for neighborhoods [7,11,6] are reviewed; "
            "a three‑stop route dated 2025-08-31 exists for client 16 with stops ['HTX716','HTX722','HTX731'] and map link 'https://maps.example.com/route/c16_aug31' stored verbatim; the route is readable; "
            "drive‑time feasibility is confirmed with a 30‑minute cap; a campaign titled 'Aug 2025 Viewing Day — Client 16' exists and sends one email 'Route & Open House Plan' "
            "(template 'general_update') using 'https://test.storage.com/emails/viewing_day_c16.html'; and a kickoff viewing hold on 2025-08-31 from 09:15Z to 09:35Z titled 'Depart for first stop' "
            "at 'Client Home' (source 'viewing') is on the calendar. Verify via route details, drive‑time check, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="open_house_windows_by_neighborhoods",
                kwargs={"neighborhood_ids": [7, 11, 6]},
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 16,
                    "date": "2025-08-31",
                    "stops_ordered_json": ["HTX716", "HTX722", "HTX731"],
                    "map_url": "https://maps.example.com/route/c16_aug31",
                    "created_by_broker_id": 8,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX716", "HTX722", "HTX731"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Viewing Day — Client 16",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Route & Open House Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/viewing_day_c16.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 16}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 16}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_75",
        instruction=(
            "You finalize a museum-area townhouse tour for client 12 under broker 3 and prep seller-broker drafts. End state: "
            "a route for 2025-08-25 with ordered stops ['HTX044','HTX036','HTX032'] and map "
            "'https://maps.google.com/route/museum_townhouse_c12_20250825' is saved and read; "
            "drive-time feasibility passes at ≤30 minutes; "
            "a drafts bundle is generated for property_ids ['HTX044','HTX036','HTX032']; "
            "a 'likely_buyer' campaign named 'Aug 2025 Townhouse Tour — Client 12' exists and is used for one email to client 12 "
            "with subject 'Townhouse Tour Plan' (template_code 'likely_buyer') and body_uri "
            "'https://maps.google.com/route/museum_townhouse_c12_20250825'; "
            "a same-day hold 13:30–13:45Z titled 'Pre-tour sync' at 'Phone' (source 'follow_up'); "
            "audit 'routes_shared_and_viewings_set' is posted on the route and the route is read again."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 12,
                    "date": "2025-08-25",
                    "stops_ordered_json": ["HTX044", "HTX036", "HTX032"],
                    "map_url": "https://maps.google.com/route/museum_townhouse_c12_20250825",
                    "created_by_broker_id": 3,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX044", "HTX036", "HTX032"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="draft_seller_broker_batch",
                kwargs={
                    "client_id": 12,
                    "property_ids": ["HTX044", "HTX036", "HTX032"],
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Townhouse Tour — Client 12",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/museum_townhouse_c12_20250825",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 12}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 12}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 3,
                    "action": "routes_shared_and_viewings_set",
                    "entity_type": "routes",
                    "entity_id": 11,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
        ],
        outputs=[
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_76",
        instruction=(
            "You present financing scenarios for client 10 under broker 4 at two target prices: 650000 and 820000 (30‑year TX). End state: both estimates are computed; "
            "a campaign titled 'Aug 2025 Financing Scenarios — Client 10' exists and sends one email with subject 'Two Financing Scenarios' (template 'general_update') and body URI "
            "'https://test.storage.com/emails/finance_scenarios_c10.html'; and a client‑meeting hold on 2025-08-25 from 20:10Z to 20:40Z titled 'Financing consult' at 'Video — Zoom' (source 'client_meeting') "
            "appears on the calendar. Verify via the campaign/email and the calendar."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 10,
                    "list_price": 650000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 10,
                    "list_price": 820000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Financing Scenarios — Client 10",
                    "type": "general_update",
                    "created_by": 4,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 10,
                    "broker_id": 4,
                    "subject": "Two Financing Scenarios",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_scenarios_c10.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 10}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 10}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_77",
        instruction=(
            "You coordinate a Saturday open‑house drive for client 5 under broker 1. Final state: open‑house windows are fetched for "
            "properties ['HTX021','HTX024','HTX025'] within 2025‑08‑22 to 2025‑08‑24 (context); a route dated 2025‑08‑23 is saved with "
            "ordered stops ['HTX021','HTX024','HTX025'] and map URL 'https://maps.google.com/route/oh_c5_20250823'; drive‑time feasibility "
            "is confirmed at ≤30 minutes per hop; a 'likely_buyer' campaign named 'Aug 2025 Open Houses — Client 5' exists; one email to client 5 "
            "with subject 'Saturday Open-House Route' using the map URL as body_uri is recorded under the campaign; two holds exist for 2025‑08‑23 — "
            "09:50–10:00Z titled 'Depart for first stop' at 'Client Home' (source 'viewing', notes 'Leave buffer for parking') and "
            "13:30–13:50Z titled 'Post-tour recap' at 'Phone' (source 'follow_up', notes 'Discuss favorites & next steps'). "
            "Prove by reading back the campaign, the stored route, the email, and calendar events; also record an audit for the built route."
        ),
        actions=[
            Action(
                name="open_houses_for_properties",
                kwargs={
                    "property_ids": ["HTX021", "HTX024", "HTX025"],
                    "date_from": "2025-08-22",
                    "date_to": "2025-08-24",
                },
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 5,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX021", "HTX024", "HTX025"],
                    "map_url": "https://maps.google.com/route/oh_c5_20250823",
                    "created_by_broker_id": 1,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX021", "HTX024", "HTX025"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Open Houses — Client 5",
                    "type": "likely_buyer",
                    "created_by": 1,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 5,
                    "broker_id": 1,
                    "subject": "Saturday Open-House Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/oh_c5_20250823",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
            Action(
                name="append_audit_event",
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
        outputs=[
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_78",
        instruction=(
            "You set a River Oaks luxury route for client 18 with broker 5. End state: "
            "a route dated 2025-08-24 with stops ['HTX018','HTX032','HTX025'] and map "
            "'https://maps.google.com/route/riveroaks_lux_c18_20250824' is saved and read; "
            "hop feasibility passes ≤30 minutes; "
            "a 'likely_buyer' campaign named 'Aug 2025 River Oaks Luxury — Client 18' exists and is used for one email "
            "with subject 'Luxury Viewing Route' (template_code 'likely_buyer') and that map URL as body_uri; "
            "a 11:10–11:20Z 'Pre-drive sync' hold at 'Phone' (source 'follow_up') exists. Verify with reads."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 18,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX018", "HTX032", "HTX025"],
                    "map_url": "https://maps.google.com/route/riveroaks_lux_c18_20250824",
                    "created_by_broker_id": 5,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX018", "HTX032", "HTX025"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 River Oaks Luxury — Client 18",
                    "type": "likely_buyer",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Luxury Viewing Route",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/riveroaks_lux_c18_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 18}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 18}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_79",
        instruction=(
            "You deliver two contrast CMAs for client 22 under broker 9. End state: two draft comp reports exist and are readable—subjects 'RICE_MIL_C22_AUG25_A' and 'MIDTOWN_C22_AUG25_B'; "
            "a campaign titled 'Aug 2025 Two‑CMA Contrast — Client 22' exists and is used to send one email with subject 'Two CMA Snapshots' (template 'general_update') and body URI "
            "'https://test.storage.com/emails/two_cma_c22.html'; and a follow‑up Zoom hold on 2025-08-26 from 11:30Z to 11:50Z titled 'CMA contrast debrief' (source 'follow_up') "
            "appears on the calendar. Verify via both comp report reads, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 22,
                    "subject_property_id": "RICE_MIL_C22_AUG25_A",
                    "created_by_broker_id": 9,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 22,
                    "subject_property_id": "MIDTOWN_C22_AUG25_B",
                    "created_by_broker_id": 9,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 10}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Two‑CMA Contrast — Client 22",
                    "type": "general_update",
                    "created_by": 9,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 22,
                    "broker_id": 9,
                    "subject": "Two CMA Snapshots",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/two_cma_c22.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 22}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 22}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_80",
        instruction=(
            "You set a micro-tour for client 7 under broker 15. End state: "
            "a route for 2025-08-28 with stops ['HTX036','HTX035'] and map "
            "'https://maps.google.com/route/eado_microtour_c7_20250828' is saved/read; hops pass ≤30 minutes; "
            "a 'likely_buyer' campaign named 'Aug 2025 EaDo Micro-Tour — Client 7' exists and is used for one email "
            "with subject 'Micro-Tour Plan' (template_code 'likely_buyer') and body_uri "
            "'https://maps.google.com/route/eado_microtour_c7_20250828'; "
            "a 16:00–17:00Z 'Contract Review - Mr. Sean Hardy' hold at '5033 Fleming Islands Suite 325, New Michaelstad, NY 03979' "
            "(source 'client_meeting') exists. Verify via reads."
        ),
        actions=[
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 7,
                    "date": "2025-08-28",
                    "stops_ordered_json": ["HTX036", "HTX035"],
                    "map_url": "https://maps.google.com/route/eado_microtour_c7_20250828",
                    "created_by_broker_id": 15,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={"property_ids": ["HTX036", "HTX035"], "max_minutes": 30},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 EaDo Micro-Tour — Client 7",
                    "type": "likely_buyer",
                    "created_by": 15,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 7,
                    "broker_id": 15,
                    "subject": "Micro-Tour Plan",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/eado_microtour_c7_20250828",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 7}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 15,
                    "client_id": 7,
                    "title": "Contract Review - Mr. Sean Hardy",
                    "start_at": "2025-08-28T16:00:00Z",
                    "end_at": "2025-08-28T17:00:00Z",
                    "location": "5033 Fleming Islands Suite 325, New Michaelstad, NY 03979",
                    "source": "client_meeting",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 7}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_81",
        instruction=(
            "You prepare a comps draft for client 2 under broker 14 and add an internal broker debrief. End state: "
            "a comp report for subject_property_id 'HTX017' is saved 'draft' and read; "
            "a 'likely_buyer' campaign named 'Aug 2025 Comps Draft — Client 2' exists; "
            "one email to client 2 with subject 'Comps Draft' (template_code 'likely_buyer') and body_uri "
            "'https://test.storage.com/emails/comps_draft_c2.html' is recorded; "
            "two holds exist — 2025-08-27 15:00–15:30Z titled 'Urban Living Property Tour' at '2222 Smith Street Unit 405, Houston, TX 77002' (source 'viewing'), "
            "and 2025-08-27 18:10–18:30Z titled 'Broker internal debrief' at 'Office' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "HTX017",
                    "created_by_broker_id": 14,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Comps Draft — Client 2",
                    "type": "likely_buyer",
                    "created_by": 14,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Comps Draft",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/comps_draft_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 14,
                    "client_id": 2,
                    "title": "Urban Living Property Tour",
                    "start_at": "2025-08-27T15:00:00Z",
                    "end_at": "2025-08-27T15:30:00Z",
                    "location": "2222 Smith Street Unit 405, Houston, TX 77002",
                    "source": "viewing",
                },
            ),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_82",
        instruction=(
            "You plan a Sunday open‑house circuit for client 12 under broker 6. "
            "Final state to achieve: the system reflects that neighborhoods [4,5] were consulted for open‑house timing (context only); "
            "a route dated 2025‑08‑24 exists with the exact ordered stops ['HTX041','HTX040','HTX048'] and map URL "
            "'https://maps.google.com/route/oh_plan_c12_20250824', and the hops are feasible at ≤30 minutes each; "
            "a 'likely_buyer' campaign named 'Aug 2025 Sunday Open Houses — Client 12' exists and is used for outbound email; "
            "one email to client 12 is on record with subject 'Open House Plan — 2025‑08‑24' and body_uri "
            "'https://maps.google.com/route/oh_plan_c12_20250824'; a same‑day hold exists for 2025‑08‑24 09:20–09:30Z titled "
            "'Pre-drive sync' at 'Phone' with source 'follow_up'; and an audit event records the route build. "
            "Prove your writes by reading back the campaign, the saved route, the email, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="open_house_windows_by_neighborhoods",
                kwargs={"neighborhood_ids": [4, 5]},
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 12,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX041", "HTX040", "HTX048"],
                    "map_url": "https://maps.google.com/route/oh_plan_c12_20250824",
                    "created_by_broker_id": 6,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX041", "HTX040", "HTX048"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Sunday Open Houses — Client 12",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 12,
                    "broker_id": 6,
                    "subject": "Open House Plan — 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/oh_plan_c12_20250824",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 12}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 12}),
            Action(
                name="append_audit_event",
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
        outputs=[
            "Noted",
            "Saved",
            "Confirmed and saved",
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_83",
        instruction=(
            "You prepare a 15‑year financing plan for client 6 under broker 2. Final state: you fetch the mortgage profile (context) and compute a "
            "mortgage estimate for client 6 at list_price 480000 with term_years 15 and region 'TX-HOU'; a 'general_update' campaign named "
            "'Aug 2025 Financing Plan — Client 6' exists; one email to client 6 with subject 'Financing Options — 15‑year plan' and body_uri "
            "'https://test.storage.com/emails/finance_c6_15yr.html' is recorded under the campaign; and a consult hold exists on "
            "2025‑08‑22 21:00–21:30Z titled 'Financing consult' at 'Video — Zoom' (source 'follow_up'). Prove by reading back the campaign, "
            "the email, and the calendar events."
        ),
        actions=[
            Action(name="retrieve_mortgage_profile", kwargs={"client_id": 6}),
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 6,
                    "list_price": 480000,
                    "term_years": 15,
                    "region": "TX-HOU",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Financing Plan — Client 6",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Financing Options — 15-year plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_c6_15yr.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 6}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 6}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_84",
        instruction=(
            "You send a Midtown CMA snapshot for client 2 under broker 14. End state: a draft comp report exists and is readable for subject 'MDTN_CMA_C2_AUG25'; "
            "a campaign titled 'Aug 2025 Midtown CMA — Client 2' exists and sends one email with subject 'Midtown CMA Snapshot' (template 'likely_buyer') and body URI "
            "'https://test.storage.com/emails/midtown_cma_c2.html'; and a follow‑up phone hold on 2025-08-23 from 18:20Z to 18:40Z titled 'CMA debrief' (source 'follow_up') appears on the calendar. "
            "Verify via the comp report read, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 2,
                    "subject_property_id": "MDTN_CMA_C2_AUG25",
                    "created_by_broker_id": 14,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Midtown CMA — Client 2",
                    "type": "likely_buyer",
                    "created_by": 14,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 14,
                    "subject": "Midtown CMA Snapshot",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/midtown_cma_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_85",
        instruction=(
            "You set up a Cypress commute test for client 6 under broker 2. End state: drive‑time feasibility is checked for ['HTX551','HTX562','HTX574'] with a 25‑minute cap; "
            "a route dated 2025-08-27 exists for those stops with map link 'https://maps.example.com/route/c6_aug27' stored verbatim and is readable; "
            "a campaign titled 'Aug 2025 Commute Test — Client 6' exists and sends one email 'Commute Test Plan' (template 'general_update') using "
            "'https://test.storage.com/emails/commute_test_c6.html'; and a pre‑commute client‑meeting call on 2025-08-27 from 07:40Z to 08:00Z titled 'Pre-commute check-in' at 'Phone' "
            "(source 'client_meeting') appears on the calendar. Verify via the drive‑time check, route details, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX551", "HTX562", "HTX574"],
                    "max_minutes": 25,
                },
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 6,
                    "date": "2025-08-27",
                    "stops_ordered_json": ["HTX551", "HTX562", "HTX574"],
                    "map_url": "https://maps.example.com/route/c6_aug27",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Commute Test — Client 6",
                    "type": "general_update",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 6,
                    "broker_id": 2,
                    "subject": "Commute Test Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/commute_test_c6.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 6}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 2,
                    "client_id": 6,
                    "title": "Pre-commute check-in",
                    "start_at": "2025-08-27T07:40:00Z",
                    "end_at": "2025-08-27T08:00:00Z",
                    "location": "Phone",
                    "source": "client_meeting",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 6}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_86",
        instruction=(
            "You prepare a concise market progress update for client 14 with broker 7. End state: a 'general_update' campaign named "
            "'Aug 2025 Midtown Market Update — Client 14' exists; current comps are retrieved via listing_ids [4, 5, 6]; a showing route "
            "for 2025‑08‑25 with ordered stops ['HTX012','HTX027','HTX044'] is stored at map URL "
            "'https://maps.google.com/route/htx_014_20250825'; and one email to client 14 is on file under the created campaign with subject "
            "'Midtown Market Update & Showing Plan', template_code 'general_update', and body_uri "
            "'https://maps.google.com/route/htx_014_20250825'. Prove the writes by reading back the campaign, email, and route."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Midtown Market Update — Client 14",
                    "type": "general_update",
                    "created_by": 7,
                },
            ),
            Action(
                name="gather_listings_with_properties",
                kwargs={"listing_ids": [4, 5, 6]},
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 14,
                    "date": "2025-08-25",
                    "stops_ordered_json": ["HTX012", "HTX027", "HTX044"],
                    "map_url": "https://maps.google.com/route/htx_014_20250825",
                    "created_by_broker_id": 7,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 14,
                    "broker_id": 7,
                    "subject": "Midtown Market Update & Showing Plan",
                    "template_code": "general_update",
                    "body_uri": "https://maps.google.com/route/htx_014_20250825",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 14}),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_87",
        instruction=(
            "You deliver a v3 client briefing for client 16 under broker 8. End state: "
            "a briefing document is generated with version_tag 'v3' so it stores at "
            "'https://test.storage.com/details/client_briefing_016_v3.pdf'; "
            "a 'general_update' campaign named 'Aug 2025 Briefing v3 — Client 16' exists and is used for one email with subject 'Briefing v3' "
            "(template_code 'general_update') using that file URI as body_uri; "
            "a reminder hold exists on 2025-08-31 12:30–12:50Z titled 'Briefing v3 review' at 'Video — Zoom' (source 'follow_up'). "
            "Prove by reading campaign, emails, and calendar."
        ),
        actions=[
            Action(
                name="create_briefing_doc",
                kwargs={"client_id": 16, "broker_id": 8, "version_tag": "v3"},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Briefing v3 — Client 16",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 16,
                    "broker_id": 8,
                    "subject": "Briefing v3",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_016_v3.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 16}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 16}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_88",
        instruction=(
            "You share a Museum District vs EaDo townhouse comparison for client 12 under broker 3. "
            "End state: a documented snapshot for subject property ID 'MD_VS_EADO_TH_C12_AUG25' exists "
            "in draft status and is readable; context reflects up to six active townhouses across "
            "neighborhoods [13,9]; a quick finance estimate accompanies the update using a target "
            "price of 530000 over 30 years in region TX; one client message is tied to a campaign "
            "titled 'Aug 2025 Museum vs EaDo - Client 12' with subject 'Townhouse Compare: Museum vs EaDo' "
            "using body URI 'https://test.storage.com/emails/museum_vs_eado_c12.html' and the "
            "likely-buyer template; and a viewing hold on 2025-08-25 from 14:00Z to 14:20Z titled "
            "'Compare plan' at '3030 Caroline Street, Houston, TX 77004' (source 'viewing') is on "
            "the calendar. Verify by reading the saved snapshot, retrieving the campaign and email "
            "records, confirming the calendar entry, and returning the finance estimate."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 12,
                    "subject_property_id": "MD_VS_EADO_TH_C12_AUG25",
                    "created_by_broker_id": 3,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [13, 9],
                    "property_type": "townhouse",
                    "limit": 6,
                },
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 12,
                    "list_price": 530000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Museum vs EaDo - Client 12",
                    "type": "likely_buyer",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 12,
                    "broker_id": 3,
                    "subject": "Townhouse Compare: Museum vs EaDo",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/museum_vs_eado_c12.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 12}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 3,
                    "client_id": 12,
                    "title": "Compare plan",
                    "start_at": "2025-08-25T14:00:00Z",
                    "end_at": "2025-08-25T14:20:00Z",
                    "location": "3030 Caroline Street, Houston, TX 77004",
                    "source": "viewing",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 12}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_89",
        instruction=(
            "You set up a Saturday open-house route for client 5 under broker 2. Final state: a 'likely_buyer' campaign named "
            "'Aug 2025 Saturday Open Houses - Client 5' exists; a route for 2025-08-23 is stored with ordered stops "
            "['HTX012','HTX009','HTX020'] and map URL 'https://maps.google.com/route/htx_012_20250823'; drive-time feasibility is OK at max 30 minutes per hop; "
            "and one email to client 5 is on record under that campaign with subject 'Open House Route - 2025-08-23' "
            "and body_uri 'https://maps.google.com/route/htx_012_20250823'. Also place a same-day hold 10:00-10:15Z titled "
            "'Day-of check-in' at 'Phone' (source 'follow_up'). Prove by reading back the campaign, the route details, the email, and the calendar events."
        ),
        actions=[
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Saturday Open Houses - Client 5",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 5,
                    "date": "2025-08-23",
                    "stops_ordered_json": ["HTX012", "HTX009", "HTX020"],
                    "map_url": "https://maps.google.com/route/htx_012_20250823",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX012", "HTX009", "HTX020"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 5,
                    "broker_id": 2,
                    "subject": "Open House Route - 2025-08-23",
                    "template_code": "likely_buyer",
                    "body_uri": "https://maps.google.com/route/htx_012_20250823",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 5}),
            Action(
                name="insert_calendar_event",
                kwargs={
                    "broker_id": 2,
                    "client_id": 5,
                    "title": "Day-of check-in",
                    "start_at": "2025-08-23T10:00:00Z",
                    "end_at": "2025-08-23T10:15:00Z",
                    "location": "Phone",
                    "source": "follow_up",
                },
            ),
            Action(name="list_client_calendar_events", kwargs={"client_id": 5}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_90",
        instruction=(
            "You send a first-time buyer education pack to client 17 under broker 10. End state: "
            "compute a mortgage estimate at list_price 450000 with region 'TX' (term_years 30) for context; "
            "a 'likely_buyer' campaign named 'Aug 2025 First-Time Buyer — Client 17' exists and is used for one email "
            "with subject 'First-Time Buyer Guide' (template_code 'likely_buyer') and body_uri "
            "'https://test.storage.com/emails/ftb_guide_c17.html'; "
            "a consult hold exists 2025-08-22 22:00–22:30Z titled 'Financing consult (SF)' at 'Video — Zoom' (source 'follow_up'). Verify with reads."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 17,
                    "list_price": 450000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 First-Time Buyer — Client 17",
                    "type": "likely_buyer",
                    "created_by": 10,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 17,
                    "broker_id": 10,
                    "subject": "First-Time Buyer Guide",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/ftb_guide_c17.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 17}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 17}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_91",
        instruction=(
            "You deliver an inspection recap to client 14 under broker 5. End state: a briefing document (version 'inspection_aug25') is generated and referenced; "
            "a campaign titled 'Aug 2025 Inspection Delivered — Client 14' exists and sends one email with subject 'Inspection Report' (template 'general_update') using the briefing URI as the body; "
            "and a follow‑up phone hold on 2025-08-22 from 19:15Z to 19:35Z titled 'Inspection Q&A' (source 'follow_up') appears on the calendar. Verify via campaign read, email log, and calendar."
        ),
        actions=[
            Action(
                name="create_briefing_doc",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "version_tag": "inspection_aug25",
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Inspection Delivered — Client 14",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 14,
                    "broker_id": 5,
                    "subject": "Inspection Report",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/details/client_briefing_014_inspection_aug25.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 14}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 14}),
        ],
        outputs=[
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_92",
        instruction=(
            "You prepare mortgage guidance and next steps for client 8 under broker 12. Required final state: a mortgage estimate is "
            "computed for client 8 at list_price 550000 (context); a brief comps package is saved as a comp report for subject_property_id "
            "'HTX088' (created_by_broker_id 12) and its details are confirmed; a 'general_update' campaign named 'Aug 2025 Mortgage & Viewing - Client 8' "
            "exists; an email to client 8 with subject 'Mortgage & Viewing Plan' and body_uri "
            "'https://test.storage.com/emails/mortgage_viewing_c8.html' is recorded under that campaign; and two calendar holds exist — "
            "2025-08-22 14:00–14:30Z titled 'Mortgage consult' at 'Office' (source 'follow_up') and 2025-08-24 18:00–19:00Z titled "
            "'Placeholder viewing window' at 'TBD' (source 'viewing')."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 8, "list_price": 550000},
            ),
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 8,
                    "subject_property_id": "HTX088",
                    "created_by_broker_id": 12,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Mortgage & Viewing - Client 8",
                    "type": "general_update",
                    "created_by": 12,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Mortgage & Viewing Plan",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/mortgage_viewing_c8.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 8}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 8}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_93",
        instruction=(
            "You broaden search guidance for client 2 under broker 3 by relying only on the actual bordering "
            "neighborhoods of neighborhood 1. Final state: details for neighborhood 1 and its bordering IDs are read; "
            "listings are searched strictly within those bordering neighborhoods using beds=2 and baths=2 (context); a "
            "'general_update' campaign named 'Aug 2025 Bordering Areas - Client 2' exists; one email exists for client 2 "
            "with subject 'Bordering Area Options' and body_uri 'https://test.storage.com/emails/border_c2.html' under "
            "that campaign; and a consult hold exists for 2025-08-23 16:00–16:30Z titled 'Bordering areas consult' at "
            "'Video - Zoom' with source 'follow_up'."
        ),
        actions=[
            Action(name="fetch_neighborhood", kwargs={"neighborhood_id": 1}),
            Action(name="list_adjacent_neighborhoods", kwargs={"neighborhood_id": 1}),
            Action(
                name="query_listings_by_neighborhoods",
                kwargs={"neighborhood_ids": [2], "beds": 2, "baths": 2},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Bordering Areas - Client 2",
                    "type": "general_update",
                    "created_by": 3,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="compose_client_email",
                kwargs={
                    "template_code": "general_update",
                    "client_id": 2,
                    "subject": "Bordering Area Options",
                    "slug": "border_c2",
                },
            ),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 2,
                    "broker_id": 3,
                    "subject": "Bordering Area Options",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/border_c2.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 2}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 2}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_94",
        instruction=(
            "You assemble a briefing packet for client 7 under broker 5. Final state: a briefing document is generated for client 7 "
            "(version_tag defaults to 'v1'), so the file exists at 'https://test.storage.com/details/client_briefing_007_v1.pdf'; "
            "you attach an external next‑steps checklist to the client with file_uri 'https://test.storage.com/checklists/next_steps_c7.pdf' "
            "(created_by 5); a 'general_update' campaign named 'Aug 2025 Briefing & Next Steps — Client 7' exists; one email to client 7 with "
            "subject 'Briefing Packet & Next Steps' and body_uri 'https://test.storage.com/details/client_briefing_007_v1.pdf' is recorded under the "
            "campaign; a review hold exists for 2025‑08‑22 20:00–20:20Z titled 'Briefing review' at 'Video — Teams' (source 'follow_up'); and an "
            "audit 'briefing_sent' is posted referencing the campaign. Prove by reading back the campaign, the email, and the calendar events."
        ),
        actions=[
            Action(name="create_briefing_doc", kwargs={"client_id": 7, "broker_id": 5}),
            Action(
                name="link_document_to_client",
                kwargs={
                    "client_id": 7,
                    "file_uri": "https://test.storage.com/checklists/next_steps_c7.pdf",
                    "created_by": 5,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Briefing & Next Steps — Client 7",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(
                name="persist_outbound_email",
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
                name="insert_calendar_event",
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
                name="append_audit_event",
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
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(name="list_client_emails", kwargs={"client_id": 7}),
            Action(name="list_client_calendar_events", kwargs={"client_id": 7}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_95",
        instruction=(
            "You assemble a condo investment package for client 15 under broker 8. "
            "Final state to achieve: for context you run a listings search for neighborhoods [5,7], property_type 'condo', price 350000–600000, limit 6; "
            "you compute a mortgage estimate for client 15 using list_price 500000 (context); "
            "you save a comps snapshot as a comp report for subject_property_id 'HTX057' (created_by_broker_id 8) with status 'draft' and verify the saved report; "
            "a 'general_update' campaign named 'Aug 2025 Condo Picks — Client 15' exists and is used for outbound email; "
            "one email to client 15 is on record with subject 'Condo Investment Picks' and body_uri "
            "'https://test.storage.com/emails/condo_invest_c15.html'; "
            "a consult hold exists for 2025‑08‑24 20:30–21:00Z titled 'Investment consult' at 'Video — Zoom' with source 'follow_up'; "
            "and an audit event records the campaign send. "
            "Prove your writes by reading back the comp report details, the campaign, the email for client 15, and the client’s calendar events."
        ),
        actions=[
            Action(
                name="query_active_listings",
                kwargs={
                    "neighborhood_ids": [5, 7],
                    "property_type": "condo",
                    "price_min": 350000,
                    "price_max": 600000,
                    "limit": 6,
                },
            ),
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 15, "list_price": 500000},
            ),
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 15,
                    "subject_property_id": "HTX057",
                    "created_by_broker_id": 8,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Condo Picks — Client 15",
                    "type": "general_update",
                    "created_by": 8,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 15,
                    "broker_id": 8,
                    "subject": "Condo Investment Picks",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/condo_invest_c15.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 15}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 15}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 8,
                    "action": "campaign_sent",
                    "entity_type": "campaigns",
                    "entity_id": 9,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
        ],
        outputs=[
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_96",
        instruction=(
            "You prepare an investor financing check‑in for client 18 under broker 5. Final state: you compute a mortgage estimate for client 18 "
            "at list_price 500000 (context); a 'general_update' campaign named 'Aug 2025 Investor Financing — Client 18' exists; one email to client 18 "
            "with subject 'Investor Financing Snapshot' and body_uri 'https://test.storage.com/emails/finance_investor_c18.html' is recorded "
            "under the campaign; and two holds exist — 2025‑08‑22 19:00–19:20Z titled 'Lender Q&A' at 'Video — Zoom' (source 'follow_up') and "
            "2025‑08‑24 17:00–17:30Z titled 'Docs review' at 'Office' (source 'client_meeting'). Prove by reading back the campaign, the email, "
            "and the calendar events."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={"client_id": 18, "list_price": 500000},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Investor Financing — Client 18",
                    "type": "general_update",
                    "created_by": 5,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 18,
                    "broker_id": 5,
                    "subject": "Investor Financing Snapshot",
                    "template_code": "general_update",
                    "body_uri": "https://test.storage.com/emails/finance_investor_c18.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 18}),
            Action(
                name="insert_calendar_event",
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
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 18}),
        ],
        outputs=[
            "Updated",
            "Completed",
            "Archived",
            "Verified",
            "Captured",
            "Applied",
            "Action executed",
            "Queued",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_97",
        instruction=(
            "You deliver a Spring Branch CMA for client 13 under broker 2 with an audit trail. End state: a draft comp report for 'SPRBR_CMA_C13_AUG25' is saved and readable; "
            "a campaign titled 'Aug 2025 Spring Branch CMA — Client 13' exists and sends one email with subject 'Your Market Analysis is Ready' (template 'likely_buyer') and body URI "
            "'https://test.storage.com/emails/sprbr_cma_c13.html'; an audit event 'client_notified' is recorded against the comp report and the report is re‑read; "
            "and a follow‑up phone hold on 2025-08-26 from 18:10Z to 18:30Z titled 'CMA debrief' (source 'follow_up') is on the calendar. Verify via comp report reads, campaign/email, and calendar."
        ),
        actions=[
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 13,
                    "subject_property_id": "SPRBR_CMA_C13_AUG25",
                    "created_by_broker_id": 2,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Spring Branch CMA — Client 13",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 13,
                    "broker_id": 2,
                    "subject": "Your Market Analysis is Ready",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/sprbr_cma_c13.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 13}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 2,
                    "action": "client_notified",
                    "entity_type": "comp_reports",
                    "entity_id": 9,
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 13}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_98",
        instruction=(
            "You prepare a briefing update for client 8 under broker 12. Required end state: a briefing document is "
            "generated and attached to client 8; a 'general_update' campaign named 'Aug 2025 Briefings — Client 8' exists; "
            "the broker‑authored email to client 8 is filed under that campaign with subject 'Client Briefing Packet', "
            "template_code 'briefing_broker', and body_uri "
            "'https://test.storage.com/details/client_briefing_008_v1.pdf'; and a review hold exists for client 8 on "
            "2025‑08‑22 14:00–14:30Z titled 'Briefing review' with location 'Office', notes 'Review briefing packet', source "
            "'client_meeting'. Prove the writes by reading back the campaign, the email for client 8, and the calendar event; "
            "record an audit noting the briefing was sent."
        ),
        actions=[
            Action(
                name="create_briefing_doc", kwargs={"client_id": 8, "broker_id": 12}
            ),
            Action(
                name="link_document_to_client",
                kwargs={"client_id": 8, "document_id": 21},
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Briefings — Client 8",
                    "type": "general_update",
                    "created_by": 12,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 8,
                    "broker_id": 12,
                    "subject": "Client Briefing Packet",
                    "template_code": "briefing_broker",
                    "body_uri": "https://test.storage.com/details/client_briefing_008_v1.pdf",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 8}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 8}),
            Action(
                name="append_audit_event",
                kwargs={
                    "actor_id": 12,
                    "action": "briefing_sent",
                    "entity_type": "documents",
                    "entity_id": 21,
                    "metadata_json": {"client_id": 8, "campaign_id": 9},
                },
            ),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_99",
        instruction=(
            "You prepare an open‑house plan for client 9 under broker 2. The verifiable end state should include: "
            "open‑house windows retrieved for neighborhoods [2,3] (context); a stored route dated 2025‑08‑24 with ordered stops "
            "['HTX021','HTX025','HTX030'] using map URL 'https://maps.google.com/route/htx_plan_c9_20250824' that meets a ≤30‑minute hop constraint; "
            "a 'likely_buyer' campaign named 'Aug 2025 Open House Plan - Client 9' under which one email to client 9 exists with subject "
            "'Sunday Route - 2025-08-24' and body_uri 'https://test.storage.com/emails/sunday_route_c9.html'; and a same‑day hold "
            "09:30–09:45Z titled 'Pre-drive sync' at 'Phone' (source 'follow_up')."
        ),
        actions=[
            Action(
                name="open_house_windows_by_neighborhoods",
                kwargs={"neighborhood_ids": [2, 3]},
            ),
            Action(
                name="persist_viewing_route",
                kwargs={
                    "client_id": 9,
                    "date": "2025-08-24",
                    "stops_ordered_json": ["HTX021", "HTX025", "HTX030"],
                    "map_url": "https://maps.google.com/route/htx_plan_c9_20250824",
                    "created_by_broker_id": 2,
                },
            ),
            Action(name="read_route", kwargs={"route_id": 11}),
            Action(
                name="validate_drive_time_hops",
                kwargs={
                    "property_ids": ["HTX021", "HTX025", "HTX030"],
                    "max_minutes": 30,
                },
            ),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Open House Plan - Client 9",
                    "type": "likely_buyer",
                    "created_by": 2,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 9,
                    "broker_id": 2,
                    "subject": "Sunday Route - 2025-08-24",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/sunday_route_c9.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 9}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 9}),
        ],
        outputs=[
            "Filed",
            "Processed",
            "OK — recorded",
            "Created",
            "Operation complete",
            "Marked complete",
            "Done",
            "Noted",
            "Saved",
            "Confirmed and saved",
        ],
    ),
    Task(
        annotator="v2",
        user_id="task_100",
        instruction=(
            "You prepare a financing‑ready update for client 18 under broker 6 around a target price of 720000. End state: a 30‑year TX mortgage estimate is computed; "
            "a comp report for subject 'BRAESWOOD_TARGET_C18_AUG25' is saved in draft and readable; a campaign titled 'Aug 2025 Financing + CMA — Client 18' exists and is used to send one email "
            "with subject 'Financing & CMA' (template 'likely_buyer') and body URI 'https://test.storage.com/emails/financing_cma_c18.html'; "
            "and a client meeting on 2025-08-25 from 16:00Z to 16:30Z titled 'Financing plan' at 'Office' (source 'client_meeting') is on the calendar. "
            "Verify via the comp report read, the campaign/email, and the calendar."
        ),
        actions=[
            Action(
                name="estimate_mortgage_payment",
                kwargs={
                    "client_id": 18,
                    "list_price": 720000,
                    "term_years": 30,
                    "region": "TX",
                },
            ),
            Action(
                name="create_or_update_comp_report",
                kwargs={
                    "client_id": 18,
                    "subject_property_id": "BRAESWOOD_TARGET_C18_AUG25",
                    "created_by_broker_id": 6,
                    "final_status": "draft",
                },
            ),
            Action(name="read_comp_report_bundle", kwargs={"report_id": 9}),
            Action(
                name="new_campaign_creator",
                kwargs={
                    "name": "Aug 2025 Financing + CMA — Client 18",
                    "type": "likely_buyer",
                    "created_by": 6,
                },
            ),
            Action(name="read_campaign", kwargs={"campaign_id": 9}),
            Action(
                name="persist_outbound_email",
                kwargs={
                    "client_id": 18,
                    "broker_id": 6,
                    "subject": "Financing & CMA",
                    "template_code": "likely_buyer",
                    "body_uri": "https://test.storage.com/emails/financing_cma_c18.html",
                    "campaign_id": 9,
                },
            ),
            Action(name="list_client_emails", kwargs={"client_id": 18}),
            Action(
                name="insert_calendar_event",
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
            Action(name="list_client_calendar_events", kwargs={"client_id": 18}),
        ],
        outputs=[
            "Queued",
            "Acknowledged",
            "Synced",
            "Persisted successfully",
            "Stored",
            "Draft saved",
            "Logged with trace ID",
            "Filed",
            "Processed",
        ],
    ),
]