from typing import Dict, List

RULES = [
    # Property & Listings
    "You must use `lookup_property_with_latest_listing` when fetching a property's record along with its most recent listing.",
    "Use `query_active_listings` to search listings by filters (price, beds, baths, sqft, property_type).",
    "Use `query_listings_by_neighborhoods` if the search is scoped to specific neighborhoods.",
    "Always use `gather_listings_with_properties` when you need listing details together with property attributes.",

    # Neighborhoods
    "Use `fetch_neighborhood` to retrieve full details of a neighborhood.",
    "Use `list_adjacent_neighborhoods` when identifying bordering neighborhoods.",
    "Use `open_house_windows_by_neighborhoods` to get open houses at the neighborhood level.",

    # Clients & Brokers
    "Use `fetch_client_prefs` to retrieve a client’s stored preferences.",
    "Use `fetch_broker_profile` to fetch details for a broker.",
    "Use `retrieve_mortgage_profile` to pull a client’s mortgage profile.",
    "Use `estimate_mortgage_payment` when calculating estimated mortgage payments for a client.",

    # Sales & Reports
    "Use `recent_sales_for_property` to return recent sales history for a property.",
    "Use `create_or_update_comp_report` to generate or update a comp report (also persists comparables and documents).",
    "Use `read_comp_report_bundle` to fetch a comp report with its comps and documents.",
    "Use `set_comp_report_status` to update the status of a comp report.",

    # Campaigns & Emails
    "Use `new_campaign_creator` to create a new campaign record.",
    "Use `read_campaign` to fetch details of a campaign by ID.",
    "Use `compose_client_email` to render an email body for a client/template pair.",
    "Use `persist_outbound_email` to record an email that was sent.",
    "Use `list_client_emails` to fetch all emails sent to a client.",
    "Use `draft_seller_broker_batch` to generate draft outreach emails to seller/broker contacts when a batch is requested."

    # Calendar & Routes
    "Use `insert_calendar_event` to create a new calendar event.",
    "Use `list_client_calendar_events` to fetch all events for a client.",
    "Use `open_houses_for_properties` to fetch open houses for given properties.",
    "Use `persist_viewing_route` to create a client viewing route with stops.",
    "Use `read_route` to fetch details of a route by ID.",

    # Docs & Audit
    "Use `create_briefing_doc` to generate a client briefing document.",
    "Use `link_document_to_client` to attach any document to a client.",
    "Use `append_audit_event` to record any action in audit_events.",

    # Utilities
    "Use `validate_drive_time_hops` to check if route hops fit within max drive time."
]

# --- Evaluator-facing guidance to reduce false negatives ---
EVALUATOR_SETTINGS: Dict[str, object] = {
    "human_label_equivalence": {
        "Packet follow-up": ["Review Starter Packet"],
        "Confirm Saturday logistics": ["Saturday Schedule Check-In"],
        "CMA discussion": ["Market Analysis Review"],
        "Comp pack review": ["Comp Package Review"],
    },
    "disallow_noop_audit": True,
    "require_deterministic_params": True,
    "preferred_padding_actions": [
        "list_client_emails",
        "list_client_calendar_events",
        "read_campaign",
        "read_comp_report_bundle",
        "read_route"
    ]
}

# --- Allowed tools for the evaluator ---
EVALUATOR_SETTINGS.setdefault("allowed_tools", [
    "lookup_property_with_latest_listing",
    "query_active_listings",
    "query_listings_by_neighborhoods",
    "gather_listings_with_properties",
    "fetch_neighborhood",
    "list_adjacent_neighborhoods",
    "open_house_windows_by_neighborhoods",
    "fetch_client_prefs",
    "fetch_broker_profile",
    "retrieve_mortgage_profile",
    "estimate_mortgage_payment",
    "recent_sales_for_property",
    "create_or_update_comp_report",
    "read_comp_report_bundle",
    "set_comp_report_status",
    "new_campaign_creator",
    "read_campaign",
    "compose_client_email",
    "persist_outbound_email",
    "list_client_emails",
    "insert_calendar_event",
    "list_client_calendar_events",
    "open_houses_for_properties",
    "persist_viewing_route",
    "read_route",
    "create_briefing_doc",
    "link_document_to_client",
    "append_audit_event",
    "validate_drive_time_hops",
])