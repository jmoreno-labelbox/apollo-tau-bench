# Copyright Sierra



# Utility function
def _next_int_id(items, id_key='id', prefix=''):
    """Generate next integer ID based on existing items."""
    if not items:
        return f"{prefix}1"
    max_id = 0
    for item in items:
        item_id = str(item.get(id_key, ''))
        # Retrieve number from identifier
        if prefix:
            item_id = item_id.replace(prefix, '')
        try:
            num = int(item_id)
            max_id = max(max_id, num)
        except (ValueError, AttributeError):
            pass
    return f"{prefix}{max_id + 1}"


# Utility function
from datetime import datetime

def _fixed_now_iso():
    """Return current time in ISO format."""
    return datetime.now().isoformat()

from .get_client_preferences import GetClientPreferences
from .get_mortgage_profile import GetMortgageProfile
from .get_property_and_listing import GetPropertyAndListing
from .search_listings import SearchListings
from .search_listings_in_neighborhoods import SearchListingsInNeighborhoods
from .get_neighborhood_details import GetNeighborhoodDetails
from .get_bordering_neighborhoods import GetBorderingNeighborhoods
from .get_broker_details import GetBrokerDetails
from .compute_mortgage_estimate import ComputeMortgageEstimate
from .fetch_recent_sales_by_property import FetchRecentSalesByProperty
from .save_comp_report import SaveCompReport
from .get_comp_report_details import GetCompReportDetails
from .update_comp_report_status import UpdateCompReportStatus
from .create_campaign import CreateCampaign
from .get_campaign_details import GetCampaignDetails
from .render_client_email import RenderClientEmail
from .send_email import SendEmail
from .get_emails_for_client import GetEmailsForClient
from .create_calendar_event import CreateCalendarEvent
from .get_calendar_events_for_client import GetCalendarEventsForClient
from .fetch_open_houses_by_properties import FetchOpenHousesByProperties
from .build_route import BuildRoute
from .get_route_details import GetRouteDetails
from .draft_seller_broker_emails import DraftSellerBrokerEmails
from .post_audit_event import PostAuditEvent
from .list_listings_by_ids import ListListingsByIds
from .get_open_house_windows_for_neighborhoods import GetOpenHouseWindowsForNeighborhoods
from .check_drive_time_constraints import CheckDriveTimeConstraints
from .generate_briefing_doc import GenerateBriefingDoc
from .attach_document_to_client import AttachDocumentToClient

ALL_TOOLS = [
    GetClientPreferences,
    GetMortgageProfile,
    GetPropertyAndListing,
    SearchListings,
    SearchListingsInNeighborhoods,
    GetNeighborhoodDetails,
    GetBorderingNeighborhoods,
    GetBrokerDetails,
    ComputeMortgageEstimate,
    FetchRecentSalesByProperty,
    SaveCompReport,
    GetCompReportDetails,
    UpdateCompReportStatus,
    CreateCampaign,
    GetCampaignDetails,
    RenderClientEmail,
    SendEmail,
    GetEmailsForClient,
    CreateCalendarEvent,
    GetCalendarEventsForClient,
    FetchOpenHousesByProperties,
    BuildRoute,
    GetRouteDetails,
    DraftSellerBrokerEmails,
    PostAuditEvent,
    ListListingsByIds,
    GetOpenHouseWindowsForNeighborhoods,
    CheckDriveTimeConstraints,
    GenerateBriefingDoc,
    AttachDocumentToClient,
]
