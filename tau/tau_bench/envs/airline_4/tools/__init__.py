# Copyright owned by Sierra.

from .get_current_ticket_price import GetCurrentTicketPrice
from .list_all_fares_by_route import ListAllFaresByRoute
from .compute_cheapest_by_date_for_route import ComputeCheapestByDateForRoute
from .get_cheapest_flight_from_reservation import GetCheapestFlightFromReservation
from .list_operating_dates import ListOperatingDates
from .get_historical_ticket_prices import GetHistoricalTicketPrices
from .get_average_ticket_price import GetAverageTicketPrice
from .get_operational_events import GetOperationalEvents
from .get_flown_revenue_for_flight import GetFlownRevenueForFlight
from .get_flight_schedule import GetFlightSchedule
from .get_flight_status_by_date import GetFlightStatusByDate
from .get_aircraft_by_tail_number import GetAircraftByTailNumber
from .get_available_seat import GetAvailableSeat
from .get_price_change_history import GetPriceChangeHistory
from .adjust_seasonal_pricing import AdjustSeasonalPricing
from .set_ticket_price import SetTicketPrice
from .apply_discount_to_flight import ApplyDiscountToFlight
from .remove_discount_from_flight import RemoveDiscountFromFlight
from .adjust_fare_class_pricing import AdjustFareClassPricing
from .bulk_upgrade_ticket_prices import BulkUpgradeTicketPrices
from .update_flight_schedule import UpdateFlightSchedule
from .reprice_reservation import RepriceReservation
from .log_upgrade_no_charge import LogUpgradeNoCharge
from .get_aircraft_profile import GetAircraftProfile
from .list_aircraft_at_airport import ListAircraftAtAirport
from .reposition_aircraft import RepositionAircraft
from .update_aircraft_status import UpdateAircraftStatus
from .get_crew_certifications import GetCrewCertifications
from .upsert_crew_certification import UpsertCrewCertification
from .update_flight_inventory_and_prices import UpdateFlightInventoryAndPrices
from .assign_aircraft_to_flight import AssignAircraftToFlight
from .get_flight_assignment_by_date import GetFlightAssignmentByDate

ALL_TOOLS = [
    GetCurrentTicketPrice,
    ListAllFaresByRoute,
    ComputeCheapestByDateForRoute,
    GetCheapestFlightFromReservation,
    ListOperatingDates,
    GetHistoricalTicketPrices,
    GetAverageTicketPrice,
    GetOperationalEvents,
    GetFlownRevenueForFlight,
    GetFlightSchedule,
    GetFlightStatusByDate,
    GetAircraftByTailNumber,
    GetAvailableSeat,
    GetPriceChangeHistory,
    AdjustSeasonalPricing,
    SetTicketPrice,
    ApplyDiscountToFlight,
    RemoveDiscountFromFlight,
    AdjustFareClassPricing,
    BulkUpgradeTicketPrices,
    UpdateFlightSchedule,
    RepriceReservation,
    LogUpgradeNoCharge,
    GetAircraftProfile,
    ListAircraftAtAirport,
    RepositionAircraft,
    UpdateAircraftStatus,
    GetCrewCertifications,
    UpsertCrewCertification,
    UpdateFlightInventoryAndPrices,
    AssignAircraftToFlight,
    GetFlightAssignmentByDate,
]
