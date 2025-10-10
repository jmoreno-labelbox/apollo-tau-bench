# Copyright Sierra

from .get_airport_by_code import GetAirportByCode
from .get_aircraft_by_tail import GetAircraftByTail
from .get_aircraft_by_airport import GetAircraftByAirport
from .lookup_flight_day import LookupFlightDay
from .scan_flights_by_date import ScanFlightsByDate
from .get_flight_scheduled_times import GetFlightScheduledTimes
from .find_reservations_by_user import FindReservationsByUser
from .find_reservations_by_flight_day import FindReservationsByFlightDay
from .get_crew_member_by_employee_code import GetCrewMemberByEmployeeCode
from .get_crew_assignments import GetCrewAssignments
from .get_crew_certifications import GetCrewCertifications
from .events_at_airport_on import EventsAtAirportOn
from .maintenance_logs_for_aircraft import MaintenanceLogsForAircraft
from .maintenance_logs import MaintenanceLogs
from .compute_crew_duty_counts import ComputeCrewDutyCounts
from .create_operational_event import CreateOperationalEvent
from .set_aircraft_status import SetAircraftStatus
from .relocate_aircraft import RelocateAircraft
from .append_maintenance_log import AppendMaintenanceLog
from .update_crew_member_status import UpdateCrewMemberStatus
from .remove_crew_assignment import RemoveCrewAssignment
from .create_crew_assignment import CreateCrewAssignment
from .update_flight_status_for_date import UpdateFlightStatusForDate
from .delay_flight_actual_times_for_date import DelayFlightActualTimesForDate
from .cancel_reservation import CancelReservation
from .refund_reservation import RefundReservation
from .refund_reservations_by_flight_day import RefundReservationsByFlightDay
from .send_user_notification import SendUserNotification
from .find_available_crew import FindAvailableCrew
from .update_reservation_status import UpdateReservationStatus
from .update_reservation_details import UpdateReservationDetails
from .find_flights import FindFlights
from .create_reservation import CreateReservation
from .find_user_by_email import FindUserByEmail
from .update_flight_scheduled_times import UpdateFlightScheduledTimes

ALL_TOOLS = [
    GetAirportByCode,
    GetAircraftByTail,
    GetAircraftByAirport,
    LookupFlightDay,
    ScanFlightsByDate,
    GetFlightScheduledTimes,
    FindReservationsByUser,
    FindReservationsByFlightDay,
    GetCrewMemberByEmployeeCode,
    GetCrewAssignments,
    GetCrewCertifications,
    EventsAtAirportOn,
    MaintenanceLogsForAircraft,
    MaintenanceLogs,
    ComputeCrewDutyCounts,
    CreateOperationalEvent,
    SetAircraftStatus,
    RelocateAircraft,
    AppendMaintenanceLog,
    UpdateCrewMemberStatus,
    RemoveCrewAssignment,
    CreateCrewAssignment,
    UpdateFlightStatusForDate,
    DelayFlightActualTimesForDate,
    CancelReservation,
    RefundReservation,
    RefundReservationsByFlightDay,
    SendUserNotification,
    FindAvailableCrew,
    UpdateReservationStatus,
    UpdateReservationDetails,
    FindFlights,
    CreateReservation,
    FindUserByEmail,
    UpdateFlightScheduledTimes,
]
