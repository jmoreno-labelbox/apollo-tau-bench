# Copyright owned by Sierra

from .search_listings import SearchListings
from .get_listing_details import GetListingDetails
from .search_clients import SearchClients
from .calculate_mortgage import CalculateMortgage
from .schedule_open_house import ScheduleOpenHouse
from .generate_property_report import GeneratePropertyReport
from .create_campaign import CreateCampaign
from .send_email import SendEmail
from .get_emails_for_client import GetEmailsForClient
from .create_calendar_event import CreateCalendarEvent
from .get_calendar_events_for_client import GetCalendarEventsForClient
from .get_campaign_details import GetCampaignDetails
from .build_route import BuildRoute
from .get_route_details import GetRouteDetails
from .post_audit_event import PostAuditEvent
from .check_drive_time_constraints import CheckDriveTimeConstraints
from .list_listings_by_ids import ListListingsByIds
from .update_listing_status import UpdateListingStatus
from .generate_briefing_doc import GenerateBriefingDoc
from .attach_document_to_client import AttachDocumentToClient
from .get_mortgage_rates import GetMortgageRates
from .search_neighborhoods import SearchNeighborhoods
from .create_client_note import CreateClientNote
from .get_comparable_properties import GetComparableProperties
from .schedule_property_showing import SchedulePropertyShowing

ALL_TOOLS = [
    SearchListings,
    GetListingDetails,
    SearchClients,
    CalculateMortgage,
    ScheduleOpenHouse,
    GeneratePropertyReport,
    CreateCampaign,
    SendEmail,
    GetEmailsForClient,
    CreateCalendarEvent,
    GetCalendarEventsForClient,
    GetCampaignDetails,
    BuildRoute,
    GetRouteDetails,
    PostAuditEvent,
    CheckDriveTimeConstraints,
    ListListingsByIds,
    UpdateListingStatus,
    GenerateBriefingDoc,
    AttachDocumentToClient,
    GetMortgageRates,
    SearchNeighborhoods,
    CreateClientNote,
    GetComparableProperties,
    SchedulePropertyShowing,
]
