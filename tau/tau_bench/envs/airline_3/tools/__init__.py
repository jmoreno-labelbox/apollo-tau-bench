# Copyright Sierra

from .get_user_profile import GetUserProfile
from .update_reservation import UpdateReservation
from .get_reservation_details import GetReservationDetails
from .update_crew_member_status import UpdateCrewMemberStatus
from .cancel_reservation import CancelReservation
from .get_flight_status_by_number_and_date import GetFlightStatusByNumberAndDate
from .find_flights import FindFlights
from .get_crew_member_info import GetCrewMemberInfo
from .get_flight_schedule import GetFlightSchedule
from .get_maintenance_logs import GetMaintenanceLogs
from .get_operational_events import GetOperationalEvents
from .manage_crew_member import ManageCrewMember
from .get_crew_availability import GetCrewAvailability
from .get_crew_certification_status import GetCrewCertificationStatus
from .update_user_membership import UpdateUserMembership
from .get_airport_details_by_iata_code import GetAirportDetailsByIATACode
from .get_aircraft_model_info import GetAircraftModelInfo
from .update_crew_profile import UpdateCrewProfile
from .get_crew_member_schedule import GetCrewMemberSchedule
from .update_crew_member_home_base import UpdateCrewMemberHomeBase
from .update_aircraft_status import UpdateAircraftStatus
from .update_crew import UpdateCrew
from .update_aircraft_location import UpdateAircraftLocation
from .get_aircraft_by_model import GetAircraftByModel
from .get_crew_contact_info import GetCrewContactInfo
from .get_crew_performance_metrics import GetCrewPerformanceMetrics
from .get_crew_schedule import GetCrewSchedule
from .get_crew_training_records import GetCrewTrainingRecords
from .update_reservation_baggage import UpdateReservationBaggage
from .get_reservations_by_flight import GetReservationsByFlight

ALL_TOOLS = [
    GetUserProfile,
    UpdateReservation,
    GetReservationDetails,
    UpdateCrewMemberStatus,
    CancelReservation,
    GetFlightStatusByNumberAndDate,
    FindFlights,
    GetCrewMemberInfo,
    GetFlightSchedule,
    GetMaintenanceLogs,
    GetOperationalEvents,
    ManageCrewMember,
    GetCrewAvailability,
    GetCrewCertificationStatus,
    UpdateUserMembership,
    GetAirportDetailsByIATACode,
    GetAircraftModelInfo,
    UpdateCrewProfile,
    GetCrewMemberSchedule,
    UpdateCrewMemberHomeBase,
    UpdateAircraftStatus,
    UpdateCrew,
    UpdateAircraftLocation,
    GetAircraftByModel,
    GetCrewContactInfo,
    GetCrewPerformanceMetrics,
    GetCrewSchedule,
    GetCrewTrainingRecords,
    UpdateReservationBaggage,
    GetReservationsByFlight,
]
