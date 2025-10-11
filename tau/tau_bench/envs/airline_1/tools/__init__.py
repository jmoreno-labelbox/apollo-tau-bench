# Copyright Sierra

from .get_airport_by_code import GetAirportByCode
from .find_flights import FindFlights
from .update_flight_schedule import UpdateFlightSchedule
from .create_operational_event import CreateOperationalEvent
from .get_aircraft_by_tail_number import GetAircraftByTailNumber
from .update_aircraft_status import UpdateAircraftStatus
from .create_maintenance_log import CreateMaintenanceLog
from .get_flight_by_number import GetFlightByNumber
from .update_flight_status import UpdateFlightStatus
from .find_reservations_by_flight import FindReservationsByFlight
from .update_reservation_status import UpdateReservationStatus
from .find_crew_member import FindCrewMember
from .update_crew_assignment import UpdateCrewAssignment
from .update_crew_member_status import UpdateCrewMemberStatus
from .find_crew_assignments import FindCrewAssignments
from .find_available_crew import FindAvailableCrew
from .assign_crew_to_flight import AssignCrewToFlight
from .find_reservation_by_code import FindReservationByCode
from .create_reservation import CreateReservation
from .update_aircraft_location import UpdateAircraftLocation
from .create_flight import CreateFlight
from .verify_crew_duty_time import VerifyCrewDutyTime
from .find_crew_certifications import FindCrewCertifications
from .find_flight_crew import FindFlightCrew
from .send_ground_notification import SendGroundNotification
from .send_passenger_notification import SendPassengerNotification
from .send_department_notification import SendDepartmentNotification
from .update_reservation_details import UpdateReservationDetails
from .get_user_details import GetUserDetails
from .search_direct_flight import SearchDirectFlight
from .search_onestop_flight import SearchOnestopFlight
from .think import Think
from .calculate import Calculate
from .book_reservation import BookReservation
from .get_reservation_details import GetReservationDetails
from .cancel_reservation import CancelReservation
from .update_reservation_flights import UpdateReservationFlights
from .update_reservation_baggages import UpdateReservationBaggages
from .send_certificate import SendCertificate
from .update_reservation_passengers import UpdateReservationPassengers
from .assign_aircraft_to_flight import AssignAircraftToFlight
from .update_maintenance_log_status import UpdateMaintenanceLogStatus

ALL_TOOLS = [
    GetAirportByCode,
    FindFlights,
    UpdateFlightSchedule,
    CreateOperationalEvent,
    GetAircraftByTailNumber,
    UpdateAircraftStatus,
    CreateMaintenanceLog,
    GetFlightByNumber,
    UpdateFlightStatus,
    FindReservationsByFlight,
    UpdateReservationStatus,
    FindCrewMember,
    UpdateCrewAssignment,
    UpdateCrewMemberStatus,
    FindCrewAssignments,
    FindAvailableCrew,
    AssignCrewToFlight,
    FindReservationByCode,
    CreateReservation,
    UpdateAircraftLocation,
    CreateFlight,
    VerifyCrewDutyTime,
    FindCrewCertifications,
    FindFlightCrew,
    SendGroundNotification,
    SendPassengerNotification,
    SendDepartmentNotification,
    UpdateReservationDetails,
    GetUserDetails,
    SearchDirectFlight,
    SearchOnestopFlight,
    Think,
    Calculate,
    BookReservation,
    GetReservationDetails,
    CancelReservation,
    UpdateReservationFlights,
    UpdateReservationBaggages,
    SendCertificate,
    UpdateReservationPassengers,
    AssignAircraftToFlight,
    UpdateMaintenanceLogStatus,
]
