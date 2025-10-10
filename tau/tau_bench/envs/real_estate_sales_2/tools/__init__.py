# Copyright Sierra Technologies

from .validate_drive_time_hops import ValidateDriveTimeHops
from .fetch_client_prefs import FetchClientPrefs
from .retrieve_mortgage_profile import RetrieveMortgageProfile
from .lookup_property_with_latest_listing import LookupPropertyWithLatestListing
from .query_active_listings import QueryActiveListings
from .query_listings_by_neighborhoods import QueryListingsByNeighborhoods
from .fetch_neighborhood import FetchNeighborhood
from .list_adjacent_neighborhoods import ListAdjacentNeighborhoods
from .fetch_broker_profile import FetchBrokerProfile
from .estimate_mortgage_payment import EstimateMortgagePayment
from .recent_sales_for_property import RecentSalesForProperty
from .create_or_update_comp_report import CreateOrUpdateCompReport
from .read_comp_report_bundle import ReadCompReportBundle
from .set_comp_report_status import SetCompReportStatus
from .new_campaign_creator import NewCampaignCreator
from .read_campaign import ReadCampaign
from .compose_client_email import ComposeClientEmail
from .persist_outbound_email import PersistOutboundEmail
from .list_client_emails import ListClientEmails
from .insert_calendar_event import InsertCalendarEvent
from .list_client_calendar_events import ListClientCalendarEvents
from .open_houses_for_properties import OpenHousesForProperties
from .persist_viewing_route import PersistViewingRoute
from .read_route import ReadRoute
from .draft_seller_broker_batch import DraftSellerBrokerBatch
from .append_audit_event import AppendAuditEvent
from .gather_listings_with_properties import GatherListingsWithProperties
from .open_house_windows_by_neighborhoods import OpenHouseWindowsByNeighborhoods
from .create_briefing_doc import CreateBriefingDoc
from .link_document_to_client import LinkDocumentToClient

ALL_TOOLS = [
    ValidateDriveTimeHops,
    FetchClientPrefs,
    RetrieveMortgageProfile,
    LookupPropertyWithLatestListing,
    QueryActiveListings,
    QueryListingsByNeighborhoods,
    FetchNeighborhood,
    ListAdjacentNeighborhoods,
    FetchBrokerProfile,
    EstimateMortgagePayment,
    RecentSalesForProperty,
    CreateOrUpdateCompReport,
    ReadCompReportBundle,
    SetCompReportStatus,
    NewCampaignCreator,
    ReadCampaign,
    ComposeClientEmail,
    PersistOutboundEmail,
    ListClientEmails,
    InsertCalendarEvent,
    ListClientCalendarEvents,
    OpenHousesForProperties,
    PersistViewingRoute,
    ReadRoute,
    DraftSellerBrokerBatch,
    AppendAuditEvent,
    GatherListingsWithProperties,
    OpenHouseWindowsByNeighborhoods,
    CreateBriefingDoc,
    LinkDocumentToClient,
]
