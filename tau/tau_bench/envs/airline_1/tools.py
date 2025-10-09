import json
import re
from datetime import datetime, timedelta
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


class GetAirportByCode(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], iata_code: str) -> str:
        airports = data.get("airports", [])
        for airport in airports:
            if airport.get("iata_code") == iata_code:
                payload = airport
                out = json.dumps(payload)
                return out
        payload = {"error": "Airport not found", "iata_code": iata_code}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAirportByCode",
                "description": "Retrieves the full details of an airport using its 3-letter IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "The 3-letter IATA code of the airport (e.g., 'JFK').",
                        }
                    },
                    "required": ["iata_code"],
                },
            },
        }


class FindFlights(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        departure_date: str,
        status: list[str],
        origin: str | None = None,
        destination: str | None = None,
    ) -> str:
        flights_data = data.get("flights", [])
        results = []

        for flight_route in flights_data:
            route_match = True
            if origin and flight_route.get("origin") != origin:
                route_match = False
            if destination and flight_route.get("destination") != destination:
                route_match = False

            if route_match:
                date_info = flight_route.get("dates", {}).get(departure_date)
                if date_info and date_info.get("status") in status:
                    flight_info = {
                        "flight_number": flight_route.get("flight_number"),
                        "origin": flight_route.get("origin"),
                        "destination": flight_route.get("destination"),
                        "date": departure_date,
                        "scheduled_departure_time_est": flight_route.get(
                            "scheduled_departure_time_est"
                        ),
                        "scheduled_arrival_time_est": flight_route.get(
                            "scheduled_arrival_time_est"
                        ),
                        "status": date_info.get("status"),
                        "available_seats": date_info.get("available_seats"),
                        "prices": date_info.get("prices"),
                    }
                    results.append(flight_info)
        payload = results
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFlights",
                "description": "Finds flights based on origin, destination, departure date, and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "departure_date": {
                            "type": "string",
                            "description": "The departure date in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of flight statuses to search for (e.g., ['available']).",
                        },
                        "origin": {
                            "type": "string",
                            "description": "The IATA code of the origin airport.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code of the destination airport.",
                        },
                    },
                    "required": ["departure_date", "status"],
                },
            },
        }


class UpdateFlightSchedule(Tool):

    @staticmethod
    def parse_time_with_day_offset(time_str: str, base_date: str) -> datetime:
        pass
        match = re.match(r"(\d{2}:\d{2}:\d{2})(\+(\d+))?", time_str)
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")

        time_part = match.group(1)
        day_offset = int(match.group(3)) if match.group(3) else 0

        dt = datetime.fromisoformat(f"{base_date}T{time_part}") + timedelta(
            days=day_offset
        )
        return dt

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str | list[str],
        flight_date: str,
        new_departure_date: str | None = None,
        new_arrival_date: str | None = None,
        new_status: str | None = None,
        new_departure_time_est: str | None = None,
        new_arrival_time_est: str | None = None,
        delay_hours: int | None = None,
        delay_minutes: int | None = None,
        new_gate: str | None = None,
        reason_event_id: str | None = None,
    ) -> str:
        if isinstance(flight_number, str):
            flight_numbers = [flight_number]
        else:
            flight_numbers = flight_number

        flights_data = data.get("flights", [])
        results = {}

        for fn in flight_numbers:
            updated = False
            for flight_route in flights_data:
                if flight_route.get("flight_number") == fn:
                    date_info = flight_route.get("dates", {}).get(flight_date)
                    if not date_info:
                        results[fn] = {"error": "Date not found", "date": flight_date}
                        updated = True
                        break
                    if new_status:
                        date_info["status"] = new_status

                    if new_gate:
                        date_info["gate"] = new_gate

                    if delay_hours is not None or delay_minutes is not None:
                        delay = timedelta(
                            hours=delay_hours or 0, minutes=delay_minutes or 0
                        )

                        dep_time_str = date_info.get(
                            "estimated_departure_time_est"
                        ) or flight_route.get("scheduled_departure_time_est")
                        arr_time_str = date_info.get(
                            "estimated_arrival_time_est"
                        ) or flight_route.get("scheduled_arrival_time_est")

                        try:
                            dep_dt = UpdateFlightSchedule.parse_time_with_day_offset(
                                dep_time_str, flight_date
                            )
                            arr_dt = UpdateFlightSchedule.parse_time_with_day_offset(
                                arr_time_str, flight_date
                            )

                            new_dep = dep_dt + delay
                            new_arr = arr_dt + delay

                            date_info["estimated_departure_time_est"] = (
                                new_dep.isoformat()
                            )
                            date_info["estimated_arrival_time_est"] = (
                                new_arr.isoformat()
                            )
                        except Exception as e:
                            results[fn] = {
                                "error": f"Error processing delayed time: {str(e)}",
                                "date": flight_date,
                                "input_dep": dep_time_str,
                                "input_arr": arr_time_str,
                            }
                            updated = True
                            break

                    if new_departure_time_est:
                        date_info["estimated_departure_time_est"] = (
                            f"{new_departure_date}T{new_departure_time_est}"
                        )
                    if new_arrival_time_est:
                        date_info["estimated_arrival_time_est"] = (
                            f"{new_arrival_date}T{new_arrival_time_est}"
                        )

                    if reason_event_id:
                        date_info["reason_event_id"] = reason_event_id

                    results[fn] = {flight_date: date_info}
                    updated = True
                    break

            if not updated:
                results[fn] = {
                    "error": "Flight not found for the given number",
                    "date": flight_date,
                }
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightSchedule",
                "description": "Updates the schedule and status of a specific flight on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number to update.",
                        },
                        "flight_date": {
                            "type": "string",
                            "description": "The date of the flight to update in YYYY-MM-DD format.",
                        },
                        "new_departure_date": {
                            "type": "string",
                            "description": "Optional: The new departure of the flight in YYYY-MM-DD format.",
                        },
                        "new_arrival_date": {
                            "type": "string",
                            "description": "Optional: The new arrival of the flight in YYYY-MM-DD format.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "Optional: The new status for the flight (e.g., 'delayed', 'cancelled').",
                        },
                        "new_departure_time_est": {
                            "type": "string",
                            "description": "Optional: The new departure time in HH:MM:SS format.",
                        },
                        "new_arrival_time_est": {
                            "type": "string",
                            "description": "Optional: The new arrival time in HH:MM:SS format.",
                        },
                        "delay_hours": {
                            "type": "integer",
                            "description": "Optional: Number of hours to delay the flight.",
                        },
                        "delay_minutes": {
                            "type": "integer",
                            "description": "Optional: Number of minutes to delay the flight.",
                        },
                        "new_gate": {
                            "type": "string",
                            "description": "Optional: The new gate for the flight.",
                        },
                        "reason_event_id": {
                            "type": "string",
                            "description": "Optional: The ID of the operational event causing this change (e.g., 'OE026').",
                        },
                    },
                    "required": ["flight_number", "flight_date"],
                },
            },
        }


class CreateOperationalEvent(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        airport_id: str,
        event_type: str,
        details: str,
        flight_number: str | None = None,
        date: str | None = None,
    ) -> str:
        events = data.get("operational_events", [])

        last_id_numeric = 0
        if events:
            numeric_ids = []
            for e in events:
                event_id = e.get("event_id", "")
                if event_id.startswith("OE"):
                    try:
                        num_part = int(event_id[2:])
                        numeric_ids.append(num_part)
                    except ValueError:
                        continue

            if numeric_ids:
                last_id_numeric = max(numeric_ids)

        new_event_id = f"OE{last_id_numeric + 1:03d}"

        new_event = {
            "event_id": new_event_id,
            "event_type": event_type,
            "details": details,
            "status": "LOGGED",
            "airport_id": airport_id,
        }

        if flight_number and date:
            new_event["flight"] = {"flight_number": flight_number, "date": date}

        events.append(new_event)
        payload = new_event
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOperationalEvent",
                "description": "Creates a new operational event log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {
                            "type": "string",
                            "description": "The unique airport ID where the event occurred.",
                        },
                        "event_type": {
                            "type": "string",
                            "description": "The type of event (e.g., 'WEATHER_ALERT', 'MAINTENANCE').",
                        },
                        "details": {
                            "type": "string",
                            "description": "A detailed description of the event.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Optional: The flight number this event is related to.",
                        },
                        "date": {
                            "type": "string",
                            "description": "Optional: The date of the related flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["airport_id", "event_type", "details"],
                },
            },
        }


class GetAircraftByTailNumber(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], tail_number: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("tail_number") == tail_number:
                payload = aircraft
                out = json.dumps(payload)
                return out
        payload = {"error": "Aircraft not found", "tail_number": tail_number}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByTailNumber",
                "description": "Retrieves the full details of an aircraft using its unique tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tail_number": {
                            "type": "string",
                            "description": "The unique tail number of the aircraft (e.g., 'G-ZNKH').",
                        }
                    },
                    "required": ["tail_number"],
                },
            },
        }


class UpdateAircraftStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str, new_status: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                aircraft["status"] = new_status
                payload = aircraft
                out = json.dumps(payload)
                return out
        payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftStatus",
                "description": "Updates the operational status of a specific aircraft.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the aircraft (e.g., 'IN_MAINTENANCE', 'ACTIVE').",
                        },
                    },
                    "required": ["aircraft_id", "new_status"],
                },
            },
        }


class CreateMaintenanceLog(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str,
        maintenance_type: str,
        description: str,
        technician_id: str,
        event_date: str,
        status: str,
        work_order_id: str,
    ) -> str:
        logs = data.get("maintenance_logs", [])
        aircraft_list = data.get("aircraft", [])

        target_aircraft = next(
            (a for a in aircraft_list if a.get("aircraft_id") == aircraft_id), None
        )
        if not target_aircraft:
            payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
            out = json.dumps(payload)
            return out

        last_id_numeric = 0
        if logs:
            numeric_ids = []
            for log in logs:
                log_id = log.get("log_id", "")
                if log_id.startswith("ML"):
                    try:
                        num_part = int(log_id[2:])
                        numeric_ids.append(num_part)
                    except ValueError:
                        continue

            if numeric_ids:
                last_id_numeric = max(numeric_ids)

        new_log_id = f"ML{last_id_numeric + 1:03d}"

        new_log = {
            "log_id": new_log_id,
            "aircraft": {
                "aircraft_id": target_aircraft["aircraft_id"],
                "tail_number": target_aircraft["tail_number"],
            },
            "event_timestamp_utc": event_date + "T00:00:00Z",
            "maintenance_type": maintenance_type,
            "description": description,
            "status": status,
            "technician_id": technician_id,
            "work_order_id": work_order_id,
        }
        logs.append(new_log)
        payload = new_log
        out = json.dumps(payload)
        return out

       

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMaintenanceLog",
                "description": "Creates a new log entry for aircraft maintenance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft.",
                        },
                        "maintenance_type": {
                            "type": "string",
                            "description": "Type of maintenance (e.g., 'UNSCHEDULED', 'A_CHECK').",
                        },
                        "description": {
                            "type": "string",
                            "description": "A detailed description of the maintenance task.",
                        },
                        "technician_id": {
                            "type": "string",
                            "description": "The ID of the technician assigned.",
                        },
                        "event_date": {
                            "type": "string",
                            "description": "The date of the maintenance event in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the maintenance (e.g., 'Scheduled', 'Completed').",
                        },
                        "work_order_id": {
                            "type": "string",
                            "description": "The associated work order ID.",
                        },
                    },
                    "required": [
                        "aircraft_id",
                        "maintenance_type",
                        "description",
                        "technician_id",
                        "event_date",
                        "status",
                        "work_order_id",
                    ],
                },
            },
        }


class GetFlightByNumber(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        flights_data = data.get("flights", [])
        for flight in flights_data:
            if flight.get("flight_number") == flight_number and date in flight["dates"]:
                result = flight.copy()
                result["date_info"] = result["dates"][date]
                del result["dates"]
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": "Flight not found", "flight_number": flight_number, "date": date}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightByNumber",
                "description": "Retrieves the full details of a specific flight on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number (e.g., 'HAT170').",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }


class UpdateFlightStatus(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, new_status: str
    ) -> str:
        flights_data = data.get("flights", [])
        for flight_route in flights_data:
            if flight_route.get("flight_number") == flight_number:
                if date in flight_route.get("dates", {}):
                    flight_route["dates"][date]["status"] = new_status
                    payload = {
                        "flight_number": flight_number,
                        "date": date,
                        "new_status": new_status,
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Flight not found", "flight_number": flight_number, "date": date}
        out = json.dumps(payload)
        return out
                    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightStatus",
                "description": "Updates the status of a specific flight on a given date (e.g., 'cancelled', 'delayed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The flight date in YYYY-MM-DD format.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status.",
                        },
                    },
                    "required": ["flight_number", "date", "new_status"],
                },
            },
        }


class FindReservationsByFlight(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        reservations = data.get("reservations", [])
        matching_reservations = []
        for res in reservations:
            for flight in res.get("flights", []):
                if (
                    flight.get("flight_number") == flight_number
                    and flight.get("date") == date
                ):
                    matching_reservations.append(res)
                    break
        payload = matching_reservations
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationsByFlight",
                "description": "Finds all reservations for a specific flight number on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number (e.g., 'HAT170').",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }


class UpdateReservationStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str, new_status: str) -> str:
        reservations = data.get("reservations", [])
        for res in reservations:
            if res.get("reservation_id") == reservation_id:
                res["status"] = new_status
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Reservation not found", "reservation_id": reservation_id}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservationStatus",
                "description": "Updates the status of a specific reservation (e.g., 'CONFIRMED', 'CANCELLED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The ID of the reservation to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the reservation.",
                        },
                    },
                    "required": ["reservation_id", "new_status"],
                },
            },
        }


class FindCrewMember(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        first_name: str | None = None,
        last_name: str | None = None,
        employee_code: str | None = None,
        crew_member_id: str | None = None,
    ) -> str:
        crew_members = data.get("crew_members", [])

        if employee_code:
            for crew_member in crew_members:
                if crew_member.get("employee_code") == employee_code:
                    payload = crew_member
                    out = json.dumps(payload)
                    return out
            payload = {"error": "Crew member not found", "employee_code": employee_code}
            out = json.dumps(payload)
            return out

        if crew_member_id:
            for crew_member in crew_members:
                if crew_member.get("crew_member_id") == crew_member_id:
                    payload = crew_member
                    out = json.dumps(payload)
                    return out
            payload = {"error": "Crew member not found", "crew_member_id": crew_member_id}
            out = json.dumps(payload)
            return out

        if first_name and last_name:
            results = [
                c
                for c in crew_members
                if c.get("first_name") == first_name and c.get("last_name") == last_name
            ]
            payload = results
            out = json.dumps(payload)
            return out
        payload = {
            "error": "Insufficient search parameters. Provide either employee_code, crew_member_id, or both first_name and last_name."
        }
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrewMember",
                "description": "Finds a crew member by employee code, crew member ID, or full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_code": {
                            "type": "string",
                            "description": "The unique employee code of the crew member.",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique crew member ID.",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the crew member.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the crew member.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateCrewAssignment(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        assignment_id: str,
        new_crew_member_id: str,
        new_crew_member_full_name: str,
    ) -> str:
        assignments = data.get("flight_crew_assignments", [])
        for assignment in assignments:
            if assignment.get("assignment_id") == assignment_id:
                assignment["crew_member"] = {
                    "crew_member_id": new_crew_member_id,
                    "full_name": new_crew_member_full_name,
                }
                payload = {
                    "status": "success",
                    "assignment_id": assignment_id,
                    "new_crew_member_id": new_crew_member_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Assignment not found", "assignment_id": assignment_id}
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewAssignment",
                "description": "Updates an existing flight crew assignment with a new crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignment_id": {
                            "type": "string",
                            "description": "The unique ID of the assignment to update (e.g., 'AS001').",
                        },
                        "new_crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the new crew member.",
                        },
                        "new_crew_member_full_name": {
                            "type": "string",
                            "description": "The full name of the new crew member.",
                        },
                    },
                    "required": [
                        "assignment_id",
                        "new_crew_member_id",
                        "new_crew_member_full_name",
                    ],
                },
            },
        }


class UpdateCrewMemberStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, new_status: str) -> str:
        crew_members = data.get("crew_members", [])
        for member in crew_members:
            if member.get("crew_member_id") == crew_member_id:
                member["status"] = new_status
                payload = member
                out = json.dumps(payload)
                return out
        payload = {"error": "Crew member not found", "crew_member_id": crew_member_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewMemberStatus",
                "description": "Updates the operational status of a specific crew member (e.g., to 'ON_SICK_LEAVE').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the crew member.",
                        },
                    },
                    "required": ["crew_member_id", "new_status"],
                },
            },
        }


class FindCrewAssignments(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], crew_member_id: str, flight_number: str | None = None
    ) -> str:
        assignments = data.get("flight_crew_assignments", [])
        results = [
            a
            for a in assignments
            if a["crew_member"]["crew_member_id"] == crew_member_id
        ]
        if flight_number:
            results = [
                a for a in results if a["flight"]["flight_number"] == flight_number
            ]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrewAssignments",
                "description": "Finds all flight assignments for a given crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Optional: Filter assignments by a specific flight number.",
                        },
                    },
                    "required": ["crew_member_id"],
                },
            },
        }


class FindAvailableCrew(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], role: str, home_base_iata: str, status: str
    ) -> str:
        crew_members = data.get("crew_members", [])
        results = [
            m
            for m in crew_members
            if m["role"] == role
            and m["home_base"]["iata_code"] == home_base_iata
            and m["status"] == status
        ]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAvailableCrew",
                "description": "Finds available crew members matching specified criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {
                            "type": "string",
                            "description": "The role of the crew member (e.g., 'Captain', 'First Officer').",
                        },
                        "home_base_iata": {
                            "type": "string",
                            "description": "The IATA code of the crew member's home base.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the crew member (e.g., 'Active').",
                        },
                    },
                    "required": ["role", "home_base_iata", "status"],
                },
            },
        }


class AssignCrewToFlight(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str,
        flight_number: str,
        date: str,
        role: str,
    ) -> str:
        assignments = data.get("flight_crew_assignments", [])

        for assignment in assignments:
            if (
                assignment.get("crew_member_id") == crew_member_id
                and assignment.get("flight_number") == flight_number
                and assignment.get("date") == date
            ):
                payload = {"error": "Crew member already assigned to this flight."}
                out = json.dumps(payload)
                return out

        new_assignment = {
            "assignment_id": f"AS_0{len(assignments) + 1}",
            "flight_number": flight_number,
            "date": date,
            "crew_member_id": crew_member_id,
            "role": role,
        }
        assignments.append(new_assignment)
        payload = new_assignment
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignCrewToFlight",
                "description": "Assigns a crew member to a specific flight with a designated role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format.",
                        },
                        "role": {
                            "type": "string",
                            "description": "Role of the crew member (e.g., 'Captain', 'First Officer').",
                        },
                    },
                    "required": ["crew_member_id", "flight_number", "date", "role"],
                },
            },
        }


class FindReservationByCode(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_code: str) -> str:
        reservations = data.get("reservations", [])
        for res in reservations:
            if res.get("reservation_id") == reservation_code:
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Reservation not found", "reservation_code": reservation_code}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationByCode",
                "description": "Retrieves the full details of a reservation using its unique code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_code": {
                            "type": "string",
                            "description": "The unique reservation code (e.g., '4WQ150').",
                        }
                    },
                    "required": ["reservation_code"],
                },
            },
        }


class CreateReservation(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_email: str,
        flight_details: list[dict[str, str]],
        passengers: list[dict[str, str]],
        cabin: str,
    ) -> str:
        users = data.get("users", [])
        reservations = data.get("reservations", [])

        target_user = None
        for user in users:
            if user.get("email") == user_email:
                first_name = user.get("name", {}).get("first_name", "").lower()
                last_name = user.get("name", {}).get("last_name", "").lower()
                user_id = f"{first_name}_{last_name}_1234"
                target_user = {"email": user_email, "id": user_id}
                break

        if not target_user:
            payload = {"error": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        last_reservation_numeric_id = 0
        if reservations:
            numeric_ids = [
                int(r["reservation_id"][3:])
                for r in reservations
                if r.get("reservation_id", "").startswith("RES")
                and r["reservation_id"][3:].isdigit()
            ]
            if numeric_ids:
                last_reservation_numeric_id = max(numeric_ids)
            else:
                last_reservation_numeric_id = 0
        else:
            last_reservation_numeric_id = 0

        new_reservation_id = f"RES{last_reservation_numeric_id + 1:04d}"

        new_reservation = {
            "reservation_id": new_reservation_id,
            "user_id": target_user["id"],
            "origin": flight_details[0]["origin"],
            "destination": flight_details[-1]["destination"],
            "flight_type": "one_way" if len(flight_details) == 1 else "round_trip",
            "cabin": cabin,
            "flights": flight_details,
            "passengers": passengers,
            "payment_history": [],
            "total_baggages": len(passengers),
            "nonfree_baggages": 0,
            "insurance": "no",
            "status": "CONFIRMED",
        }

        reservations.append(new_reservation)

        for user in users:
            if user.get("email") == user_email:
                if "reservations" not in user:
                    user["reservations"] = []
                user["reservations"].append(new_reservation_id)
                break
        payload = new_reservation
        out = json.dumps(payload)
        return out


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReservation",
                "description": "Creates a new flight reservation for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "The email of the user making the reservation.",
                        },
                        "flight_details": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {
                                        "type": "string",
                                        "description": "Date in YYYY-MM-DD format.",
                                    },
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"},
                                },
                                "required": [
                                    "flight_number",
                                    "date",
                                    "origin",
                                    "destination",
                                ],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {
                                        "type": "string",
                                        "description": "Date of birth in YYYY-MM-DD format.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                        "cabin": {
                            "type": "string",
                            "description": "The cabin class (e.g., 'economy', 'business').",
                        },
                    },
                    "required": ["user_email", "flight_details", "passengers", "cabin"],
                },
            },
        }


class UpdateAircraftLocation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        aircraft_id: str, 
        new_location_airport_id: str
    ) -> str:
        aircraft_list = data.get("aircraft", [])
        airports = data.get("airports", [])
        
        target_airport = next(
            (a for a in airports if a.get("airport_id") == new_location_airport_id),
            None,
        )
        if not target_airport:
            payload = {
                "error": "Destination airport not found",
                "airport_id": new_location_airport_id,
            }
            out = json.dumps(payload)
            return out

        target_aircraft = next(
            (ac for ac in aircraft_list if ac.get("aircraft_id") == aircraft_id), None
        )
        if not target_aircraft:
            payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
            out = json.dumps(payload)
            return out

        target_aircraft["location"] = {
            "airport_id": target_airport["airport_id"],
            "iata_code": target_airport["iata_code"],
        }
        payload = target_aircraft
        out = json.dumps(payload)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftLocation",
                "description": "Updates the current physical location of a specific aircraft to a new airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft to update.",
                        },
                        "new_location_airport_id": {
                            "type": "string",
                            "description": "The unique airport ID of the aircraft's new location.",
                        },
                    },
                    "required": ["aircraft_id", "new_location_airport_id"],
                },
            },
        }


class CreateFlight(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        origin: str,
        destination: str,
        scheduled_departure_time_est: str,
        scheduled_arrival_time_est: str,
    ) -> str:
        flights_data = data.get("flights", [])

        if any(f.get("flight_number") == flight_number for f in flights_data):
            payload = {"error": f"Flight number {flight_number} already exists."}
            out = json.dumps(payload)
            return out

        new_flight_route = {
            "flight_number": flight_number,
            "origin": origin,
            "destination": destination,
            "scheduled_departure_time_est": scheduled_departure_time_est,
            "scheduled_arrival_time_est": scheduled_arrival_time_est,
            "dates": {},
        }

        flights_data.append(new_flight_route)
        payload = new_flight_route
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFlight",
                "description": "Creates a new flight route with a unique flight number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The unique flight number (e.g., 'HAT301').",
                        },
                        "origin": {
                            "type": "string",
                            "description": "The IATA code for the origin airport.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code for the destination airport.",
                        },
                        "scheduled_departure_time_est": {
                            "type": "string",
                            "description": "Scheduled departure time in HH:MM:SS format.",
                        },
                        "scheduled_arrival_time_est": {
                            "type": "string",
                            "description": "Scheduled arrival time in HH:MM:SS format.",
                        },
                    },
                    "required": [
                        "flight_number",
                        "origin",
                        "destination",
                        "scheduled_departure_time_est",
                        "scheduled_arrival_time_est",
                    ],
                },
            },
        }


class VerifyCrewDutyTime(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, reference_date: str) -> str:
        crew_members = data.get("crew_members", [])
        target_logs = []
        for member in crew_members:
            if member.get("crew_member_id") == crew_member_id:
                target_logs.extend(member.get("flight_log", []))

        if not target_logs:
            payload = {
                "crew_member_id": crew_member_id,
                "is_compliant": True,
                "hours_past_24h": 0,
                "hours_past_30d": 0,
                "hours_past_365d": 0,
                "details": "No flight logs found, compliant by default.",
            }
            out = json.dumps(payload)
            return out

        ref_date = datetime.fromisoformat(reference_date)
        hours_24h, hours_30d, hours_365d = 0.0, 0.0, 0.0

        for log in target_logs:
            log_date = datetime.fromisoformat(log.get("date"))
            delta = ref_date - log_date

            raw_hours = log.get("hours_flown", {}).get("total")
            hours = raw_hours if isinstance(raw_hours, (int, float)) else 0.0

            if delta.days < 1:
                hours_24h += hours
            if delta.days < 30:
                hours_30d += hours
            if delta.days < 365:
                hours_365d += hours

        is_compliant = all([hours_24h <= 8, hours_30d <= 100, hours_365d <= 1000])
        payload = {
            "crew_member_id": crew_member_id,
            "is_compliant": is_compliant,
            "hours_past_24h": round(hours_24h, 2),
            "hours_past_30d": round(hours_30d, 2),
            "hours_past_365d": round(hours_365d, 2),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyCrewDutyTime",
                "description": "Verifies if a crew member is compliant with cumulative flight duty time limits based on their flight log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member to verify.",
                        },
                        "reference_date": {
                            "type": "string",
                            "description": "The date of the prospective flight assignment (YYYY-MM-DD), used as the reference point for calculations.",
                        },
                    },
                    "required": ["crew_member_id", "reference_date"],
                },
            },
        }


class FindCrewCertifications(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], crew_member_id: str, certification_code: str | None = None
    ) -> str:
        cert_records = data.get("crew_certifications", [])
        results = []
        for record in cert_records:
            if record.get("crew_member", {}).get("crew_member_id") == crew_member_id:
                if (
                    certification_code
                    and record.get("certification", {}).get("certification_code")
                    != certification_code
                ):
                    continue
                results.append(record)
        payload = results
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrewCertifications",
                "description": "Finds all certification records for a given crew member, optionally filtering by a specific certification code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member.",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Optional: The specific code of the certification to find (e.g., 'B787_FAMILY_TR').",
                        },
                    },
                    "required": ["crew_member_id"],
                },
            },
        }


class FindFlightCrew(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str) -> str:
        assignments = data.get("flight_crew_assignments", [])
        crew_results = [
            a.get("crew_member")
            for a in assignments
            if a.get("flight", {}).get("flight_number") == flight_number
        ]
        payload = list({v["crew_member_id"]: v for v in crew_results}.values())
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFlightCrew",
                "description": "Finds all crew members assigned to a flight, identified by its flight number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number to search for (e.g., 'HAT004').",
                        }
                    },
                    "required": ["flight_number"],
                },
            },
        }


class SendGroundNotification(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], airport_id: str, message: str, priority: str = "NORMAL"
    ) -> str:
        payload = {
            "status": "Notification Sent",
            "airport_id": airport_id,
            "priority": priority,
            "message": (
                f"NOTIFICATION SENT to {airport_id} with priority {priority}: {message}"
            ),
        }
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendGroundNotification",
                "description": "Sends an operational notification to the ground crew at a specified airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {
                            "type": "string",
                            "description": "The unique ID of the airport where the notification should be sent.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority of the message (e.g., 'HIGH', 'NORMAL').",
                        },
                    },
                    "required": ["airport_id", "message", "priority"],
                },
            },
        }


class SendPassengerNotification(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str, message: str) -> str:
        payload = {
            "status": "Notification Sent",
            "reservation_id": reservation_id,
            "message": (
                f"PASSENGER NOTIFICATION for reservation {reservation_id}: {message}"
            ),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendPassengerNotification",
                "description": "Sends a notification to the passenger of a specific reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                    },
                    "required": ["reservation_id", "message"],
                },
            },
        }


class SendDepartmentNotification(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], department_name: str, message: str) -> str:
        payload = {
            "status": "Notification Sent",
            "department": department_name,
            "message": (
                f"INTERNAL NOTIFICATION to {department_name} Department: {message}"
            ),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendDepartmentNotification",
                "description": "Sends a notification to an internal company department (e.g., Finance, Scheduling).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_name": {
                            "type": "string",
                            "description": "The name of the target department.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                    },
                    "required": ["department_name", "message"],
                },
            },
        }


class UpdateReservationDetails(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        new_cabin: str | None = None,
        new_status: str | None = None,
    ) -> str:
        reservations = data.get("reservations", [])
        for res in reservations:
            if res.get("reservation_id") == reservation_id:
                if new_cabin:
                    res["cabin"] = new_cabin
                if new_status:
                    res["status"] = new_status
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Reservation not found", "reservation_id": reservation_id}
        out = json.dumps(payload)
        return out
                

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservationDetails",
                "description": "Updates details of a specific reservation, such as cabin or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to update.",
                        },
                        "new_cabin": {
                            "type": "string",
                            "description": "Optional: The new cabin class for the reservation.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "Optional: The new status for the reservation.",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class GetUserDetails(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str | None = None, user_email: str | None = None
    ) -> str:
        _user_emailL = user_email or ''.lower()
        pass
        users = data.get("users", [])
        if user_id:
            for u in users:
                for res_id in u.get("reservations", []):
                    reservation = next(
                        (
                            r
                            for r in data.get("reservations", [])
                            if r.get("reservation_id") == res_id
                        ),
                        None,
                    )
                    if reservation and reservation.get("user_id") == user_id:
                        payload = u
                        out = json.dumps(payload)
                        return out
        if user_email:
            user = next(
                (u for u in users if u.get("email", "").lower() == user_email.lower()),
                None,
            )
            if user:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDetails",
                "description": "Get the details of a user, including their reservations and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user's unique ID, typically a handle like 'mia.li3818'.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "The user's email address.",
                        },
                    },
                    "required": [],
                },
            },
        }


class SearchDirectFlight(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights_data = data.get("flights", [])
        results = []
        for flight_route in flights_data:
            if (
                flight_route.get("origin") == origin
                and flight_route.get("destination") == destination
            ):
                date_info = flight_route.get("dates", {}).get(date)
                if date_info and date_info.get("status") == "available":
                    flight_details = {
                        k: v for k, v in flight_route.items() if k != "dates"
                    }
                    flight_details.update(date_info)
                    flight_details["date"] = date
                    results.append(flight_details)
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchDirectFlight",
                "description": "Search for direct flights between two airports on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "The IATA code of the origin airport (e.g., 'JFK').",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code of the destination airport (e.g., 'SEA').",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["origin", "destination", "date"],
                },
            },
        }


class SearchOnestopFlight(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights_data = data.get("flights", [])
        results = []

        for flight1 in flights_data:
            if flight1.get("origin") == origin:
                date_info1 = flight1.get("dates", {}).get(date)
                if date_info1 and date_info1.get("status") == "available":
                    for flight2 in flights_data:
                        if flight2.get("destination") == destination and flight2.get(
                            "origin"
                        ) == flight1.get("destination"):
                            try:
                                arrival_time1 = datetime.strptime(
                                    flight1.get("scheduled_arrival_time_est", "").split(
                                        "+"
                                    )[0],
                                    "%H:%M:%S",
                                ).time()
                                departure_time2 = datetime.strptime(
                                    flight2.get(
                                        "scheduled_departure_time_est", ""
                                    ).split("+")[0],
                                    "%H:%M:%S",
                                ).time()

                                date2 = date
                                if arrival_time1 < departure_time2:
                                    date_info2 = flight2.get("dates", {}).get(date2)
                                    if (
                                        date_info2
                                        and date_info2.get("status") == "available"
                                    ):
                                        leg1 = {
                                            k: v
                                            for k, v in flight1.items()
                                            if k != "dates"
                                        }
                                        leg1.update(date_info1)
                                        leg1["date"] = date

                                        leg2 = {
                                            k: v
                                            for k, v in flight2.items()
                                            if k != "dates"
                                        }
                                        leg2.update(date_info2)
                                        leg2["date"] = date2

                                        results.append([leg1, leg2])
                            except ValueError:
                                continue
        payload = results
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchOnestopFlight",
                "description": "Search for one-stop connecting flights between two airports on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "The IATA code of the origin airport (e.g., 'JFK').",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code of the destination airport (e.g., 'SEA').",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the first flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["origin", "destination", "date"],
                },
            },
        }


class Think(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], thought: str) -> str:
        pass
        return ""
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "Allows the agent to think and document its reasoning process without altering data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {
                            "type": "string",
                            "description": "The thought process to be logged.",
                        }
                    },
                    "required": ["thought"],
                },
            },
        }


class Calculate(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], expression: str) -> str:
        allowed_chars = set("0123456789+-*/(). ")
        if not set(expression).issubset(allowed_chars):
            payload = {"error": "Invalid characters in expression."}
            out = json.dumps(payload)
            return out
        try:
            result = round(float(eval(expression, {"__builtins__": None}, {})), 2)
            return str(result)
        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload)
            return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Calculates the result of a simple mathematical expression.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "The mathematical expression to evaluate (e.g., '155 + 225 + 70').",
                        }
                    },
                    "required": ["expression"],
                },
            },
        }


class BookReservation(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        origin: str,
        destination: str,
        flight_type: str,
        cabin: str,
        flights: list[dict[str, any]],
        passengers: list[dict[str, any]],
        payment_methods: list[dict[str, any]],
        total_baggages: int,
        nonfree_baggages: int,
        insurance: str,
    ) -> str:
        reservations = data.get("reservations", [])
        8000 + len(reservations)
        new_res_id = "RES0001"

        if not passengers or not flights:
            payload = {"error": "Passengers and flights are required."}
            out = json.dumps(payload)
            return out

        new_reservation = {
            "reservation_id": new_res_id,
            "user_id": user_id,
            "origin": origin,
            "destination": destination,
            "flight_type": flight_type,
            "cabin": cabin,
            "flights": flights,
            "passengers": passengers,
            "payment_history": payment_methods,
            "total_baggages": total_baggages,
            "nonfree_baggages": nonfree_baggages,
            "insurance": insurance,
            "status": "CONFIRMED",
        }

        reservations.append(new_reservation)
        payload = new_reservation
        out = json.dumps(payload)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BookReservation",
                "description": "Books a flight reservation after all details have been validated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "flight_type": {
                            "type": "string",
                            "enum": ["one_way", "round_trip"],
                        },
                        "cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "flights": {"type": "array", "items": {"type": "object"}},
                        "passengers": {"type": "array", "items": {"type": "object"}},
                        "payment_methods": {
                            "type": "array",
                            "items": {"type": "object"},
                        },
                        "total_baggages": {"type": "integer"},
                        "nonfree_baggages": {"type": "integer"},
                        "insurance": {"type": "string", "enum": ["yes", "no"]},
                    },
                    "required": [
                        "user_id",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_methods",
                        "total_baggages",
                        "nonfree_baggages",
                        "insurance",
                    ],
                },
            },
        }


class GetReservationDetails(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        reservations = data.get("reservations", [])
        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                payload = reservation
                out = json.dumps(payload)
                return out
        payload = {"error": "Reservation not found", "reservation_id": reservation_id}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReservationDetails",
                "description": "Retrieve the details of a reservation using its reservation ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation (e.g., 'RNL6HR').",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class CancelReservation(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        reservations = data.get("reservations", [])
        users = data.get("users", [])

        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )

        if not reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        if reservation.get("status") == "cancelled":
            payload = {
                "error": "Reservation is already cancelled.",
                "reservation_id": reservation_id,
            }
            out = json.dumps(payload)
            return out

        user_id = reservation.get("user_id")
        user = next((u for u in users if u.get("email", "").startswith(user_id)), None)

        refund_transactions = []
        for payment in reservation.get("payment_history", []):
            amount = payment.get("amount", 0)
            payment_id = payment.get("payment_id")

            refund_transactions.append(
                {"payment_id": payment_id, "amount": -amount, "type": "REFUND"}
            )

            if user and payment_id:
                payment_method = user.get("payment_methods", {}).get(payment_id)
                if payment_method and payment_method.get("source") in [
                    "gift_card",
                    "certificate",
                ]:
                    payment_method["amount"] = payment_method.get("amount", 0) + amount

        reservation["status"] = "cancelled"
        if "payment_history" not in reservation:
            reservation["payment_history"] = []
        reservation["payment_history"].extend(refund_transactions)
        payload = reservation
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelReservation",
                "description": "Cancels a reservation and processes refunds to the original payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to cancel.",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class UpdateReservationFlights(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        cabin: str,
        flights: list[dict[str, Any]],
        payment_id: str,
    ) -> str:
        reservations = data.get("reservations", [])
        flights_data = data.get("flights", [])

        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )
        if not reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        original_price = sum(f.get("price", 0) for f in reservation.get("flights", []))
        num_passengers = len(reservation.get("passengers", []))
        original_total_cost = original_price * num_passengers

        new_total_cost = 0
        for flight_info in flights:
            flight_number = flight_info.get("flight_number")
            date = flight_info.get("date")

            flight_route = next(
                (f for f in flights_data if f.get("flight_number") == flight_number),
                None,
            )
            if not flight_route:
                payload = {"error": f"Flight {flight_number} not found"}
                out = json.dumps(payload)
                return out

            date_details = flight_route.get("dates", {}).get(date)
            if not date_details:
                payload = {"error": f"Flight {flight_number} on date {date} not found"}
                out = json.dumps(payload)
                return out

            new_total_cost += (
                date_details.get("prices", {}).get(cabin, 0) * num_passengers
            )

        price_difference = original_total_cost - new_total_cost

        if (
            "payment_history" not in reservation
            or reservation["payment_history"] is None
        ):
            reservation["payment_history"] = []
        if price_difference != 0:
            refund_transaction = {
                "payment_id": payment_id,
                "amount": -price_difference,
                "type": "REFUND" if price_difference > 0 else "CHARGE",
            }
            reservation["payment_history"].append(refund_transaction)

        reservation["cabin"] = cabin
        reservation["flights"] = [
            {"flight_number": f.get("flight_number"), "date": f.get("date")}
            for f in flights
        ]

        response_fields = [
            "reservation_id",
            "user_id",
            "origin",
            "destination",
            "flight_type",
            "cabin",
            "flights",
            "passengers",
            "created_at",
            "total_baggages",
            "nonfree_baggages",
            "insurance",
        ]
        response = {key: reservation.get(key) for key in response_fields}
        payload = response
        out = json.dumps(payload)
        return out


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservationFlights",
                "description": "Updates the flight details (like cabin class) for an existing reservation and processes payment adjustments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "cabin": {
                            "type": "string",
                            "description": "The new cabin class.",
                        },
                        "flights": {
                            "type": "array",
                            "description": "The complete new list of flight segments for the reservation.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {"type": "string"},
                                },
                                "required": ["flight_number", "date"],
                            },
                        },
                        "payment_id": {
                            "type": "string",
                            "description": "The original payment ID for refund processing or a new one for charges.",
                        },
                    },
                    "required": ["reservation_id", "cabin", "flights", "payment_id"],
                },
            },
        }


class UpdateReservationBaggages(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        total_baggages: int,
        nonfree_baggages: int,
        payment_id: str,
    ) -> str:
        users = data.get("users", [])
        reservations = data.get("reservations", [])

        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )
        if not reservation:
            payload = {"error": "Reservation not found"}
            out = json.dumps(payload)
            return out

        user = next(
            (u for u in users if reservation_id in u.get("reservations", [])), None
        )
        if not user:
            payload = {"error": "User not found for this reservation"}
            out = json.dumps(payload)
            return out

        bag_fee = 35
        current_nonfree = reservation.get("nonfree_baggages", 0)
        additional_cost = (nonfree_baggages - current_nonfree) * bag_fee

        if additional_cost > 0:
            payment_method = user.get("payment_methods", {}).get(payment_id)
            if not payment_method:
                payload = {"error": "Payment method not found"}
                out = json.dumps(payload)
                return out

            if payment_method.get("source") == "gift_card":
                if payment_method.get("amount", 0) < additional_cost:
                    payload = {"error": "Insufficient gift card balance"}
                    out = json.dumps(payload)
                    return out
                payment_method["amount"] -= additional_cost

            if "payment_history" not in reservation:
                reservation["payment_history"] = []
            reservation["payment_history"].append(
                {
                    "payment_id": payment_id,
                    "amount": additional_cost,
                    "type": "BAGGAGE_FEE",
                }
            )

        reservation["total_baggages"] = total_baggages
        reservation["nonfree_baggages"] = nonfree_baggages
        payload = reservation
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReservationBaggages",
                "description": "Updates the baggage information for a reservation and handles payment for any additional fees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "total_baggages": {
                            "type": "integer",
                            "description": "The new total number of bags.",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "The new number of non-free bags.",
                        },
                        "payment_id": {
                            "type": "string",
                            "description": "The payment ID to charge for the new bags.",
                        },
                    },
                    "required": [
                        "reservation_id",
                        "total_baggages",
                        "nonfree_baggages",
                        "payment_id",
                    ],
                },
            },
        }


class TransferToHumanAgents(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], summary: str) -> str:
        payload = {"status": "Transfer successful", "summary": summary}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transferToHumanAgents",
                "description": "Transfers the user to a human agent, with a summary of the issue. Use only when the user's issue cannot be resolved with the available tools.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "A concise summary of the user's issue and why the transfer is necessary.",
                        }
                    },
                    "required": ["summary"],
                },
            },
        }


class SendCertificate(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], user_email: str, amount: float) -> str:
        users = data.get("users", [])
        user = next(
            (u for u in users if u.get("email", "").startswith(user_email)), None
        )
        if not user:
            payload = {"error": "User not found", "user_email": user_email}
            out = json.dumps(payload)
            return out

        payment_methods = user.get("payment_methods", {})
        cert_ids = [
            int(k.split("_")[-1])
            for k in payment_methods
            if k.startswith("certificate_")
        ]
        next_id_num = max(cert_ids) + 1 if cert_ids else 1000001
        new_cert_id = f"certificate_{next_id_num}"

        payment_methods[new_cert_id] = {
            "source": "certificate",
            "amount": amount,
            "id": new_cert_id,
        }
        user["payment_methods"] = payment_methods
        payload = {
                "status": "success",
                "user_email": user_email,
                "certificate_id": new_cert_id,
                "amount": amount,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendCertificate",
                "description": "Issues a new travel certificate of a specific value to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "The user's email address to receive the certificate.",
                        },
                        "amount": {
                            "type": "number",
                            "description": "The value of the certificate to be issued.",
                        },
                    },
                    "required": ["user_email", "amount"],
                },
            },
        }


class UpdateReservationPassengers(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], reservation_id: str, passengers: list[dict[str, str]]
    ) -> str:
        reservations = data.get("reservations", [])
        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )

        if not reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        reservation["passengers"] = passengers
        payload = reservation
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReservationPassengers",
                "description": "Updates the passenger list for a specific reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to update.",
                        },
                        "passengers": {
                            "type": "array",
                            "description": "The new, complete list of passengers for the reservation.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {
                                        "type": "string",
                                        "description": "Date of birth in YYYY-MM-DD format.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                    },
                    "required": ["reservation_id", "passengers"],
                },
            },
        }


class AssignAircraftToFlight(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, new_aircraft_id: str
    ) -> str:
        flights_data = data.get("flights", [])
        for flight in flights_data:
            if flight.get("flight_number") == flight_number:
                if date in flight.get("dates", {}):
                    flight["dates"][date][
                        "notes"
                    ] = f"Aircraft reassigned to {new_aircraft_id}"
                    payload = {
                        "status": "success",
                        "flight_number": flight_number,
                        "date": date,
                        "new_aircraft_id": new_aircraft_id,
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Flight not found on the specified date."}
        out = json.dumps(payload)
        return out
      

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAircraftToFlight",
                "description": "Assigns a new aircraft to a specific flight instance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format.",
                        },
                        "new_aircraft_id": {
                            "type": "string",
                            "description": "The ID of the new aircraft.",
                        },
                    },
                    "required": ["flight_number", "date", "new_aircraft_id"],
                },
            },
        }


class UpdateMaintenanceLogStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], log_id: str, new_status: str) -> str:
        logs = data.get("maintenance_logs", [])
        for log in logs:
            if log.get("log_id") == log_id:
                log["status"] = new_status
                payload = log
                out = json.dumps(payload)
                return out
        payload = {"error": "Maintenance log not found", "log_id": log_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateMaintenanceLogStatus",
                "description": "Updates the status of a specific maintenance log (e.g., 'Halted', 'Completed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "The unique ID of the maintenance log to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the log.",
                        },
                    },
                    "required": ["log_id", "new_status"],
                },
            },
        }


TOOLS = [
    FindFlights(),
    UpdateFlightSchedule(),
    GetAirportByCode(),
    CreateOperationalEvent(),
    GetAircraftByTailNumber(),
    UpdateAircraftStatus(),
    CreateMaintenanceLog(),
    GetFlightByNumber(),
    UpdateFlightStatus(),
    FindReservationsByFlight(),
    UpdateReservationStatus(),
    FindCrewMember(),
    UpdateCrewAssignment(),
    UpdateCrewMemberStatus(),
    FindCrewAssignments(),
    FindAvailableCrew(),
    AssignCrewToFlight(),
    FindReservationByCode(),
    CreateReservation(),
    UpdateAircraftLocation(),
    CreateFlight(),
    VerifyCrewDutyTime(),
    FindCrewCertifications(),
    FindFlightCrew(),
    SendGroundNotification(),
    SendPassengerNotification(),
    SendDepartmentNotification(),
    UpdateReservationDetails(),
    GetUserDetails(),
    SearchDirectFlight(),
    SearchOnestopFlight(),
    Calculate(),
    BookReservation(),
    GetReservationDetails(),
    CancelReservation(),
    UpdateReservationFlights(),
    UpdateReservationBaggages(),
    TransferToHumanAgents(),
    SendCertificate(),
    UpdateReservationPassengers(),
    AssignAircraftToFlight(),
    UpdateMaintenanceLogStatus(),
]
