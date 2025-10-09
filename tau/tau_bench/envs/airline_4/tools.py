import json
from datetime import datetime, timedelta
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetAirportDetailsByIATACode(Tool):
    """API tool for retrieving complete airport details from 'airports.json' using the airport's 3-letter IATA code."""

    @staticmethod
    def invoke(data: dict[str, Any], iata_code: str) -> str:
        pass
        airports = data.get("airports", {}).values()
        for airport in airports.values():
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
                "name": "GetAirportDetailsByIataCode",
                "description": "Get full airport details using the 3-letter IATA code from 'airports.json'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "3-letter IATA airport code (e.g., 'LAX').",
                        }
                    },
                    "required": ["iata_code"],
                },
            },
        }


class GetAircraftDetails(Tool):
    """API tool for obtaining complete aircraft details from 'aircraft.json' using the aircraft ID."""

    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str) -> str:
        pass
        aircraft_list = data.get("aircraft", {}).values()
        for aircraft in aircraft_list.values():
            if aircraft.get("aircraft_id") == aircraft_id:
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
                "name": "GetAircraftDetails",
                "description": "Get full aircraft details using the aircraft ID from 'aircraft.json'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Aircraft ID (e.g., 'AC001').",
                        }
                    },
                    "required": ["aircraft_id"],
                },
            },
        }


class GetFlightsByCriteria(Tool):
    """API tool for fetching flights based on departure date, status, origin, and destination, reflecting the JSON format where each flight contains a 'dates' dictionary indexed by date strings."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        departure_date: str,
        status: list[str],
        origin: str | None = None,
        destination: str | None = None,
    ) -> str:
        pass
        flights = data.get("flights", {}).values()
        matched_flights = []

        for flight in flights.values():
            #Apply filters based on origin and destination if available
            if origin and flight.get("origin") != origin:
                continue
            if destination and flight.get("destination") != destination:
                continue

            #Verify if the flight contains information for the specified departure date
            date_info = flight.get("dates", {}).values().get(departure_date)
            if not date_info:
                continue

            #Determine if the flight's status on that date aligns with any in the given status list
            if date_info.get("status") not in status:
                continue

            #Build the flight information to be returned
            flight_info = {
                "flight_number": flight.get("flight_number"),
                "origin": flight.get("origin"),
                "destination": flight.get("destination"),
                "scheduled_departure_time_est": flight.get(
                    "scheduled_departure_time_est"
                ),
                "scheduled_arrival_time_est": flight.get("scheduled_arrival_time_est"),
                "date": departure_date,
                "status": date_info.get("status"),
            }

            #Include fields specific to the status only if they are present
            status = date_info.get("status")

            if status == "available":
                if "available_seats" in date_info:
                    flight_info["available_seats"] = date_info["available_seats"]
                if "prices" in date_info:
                    flight_info["prices"] = date_info["prices"]

            elif status == "landed":
                if "actual_departure_time_est" in date_info:
                    flight_info["actual_departure_time_est"] = date_info[
                        "actual_departure_time_est"
                    ]
                if "actual_arrival_time_est" in date_info:
                    flight_info["actual_arrival_time_est"] = date_info[
                        "actual_arrival_time_est"
                    ]

            elif status == "delayed":
                if "estimated_departure_time_est" in date_info:
                    flight_info["estimated_departure_time_est"] = date_info[
                        "estimated_departure_time_est"
                    ]
                if "estimated_arrival_time_est" in date_info:
                    flight_info["estimated_arrival_time_est"] = date_info[
                        "estimated_arrival_time_est"
                    ]

            elif status == "cancelled":
                if "reason_event_id" in date_info:
                    flight_info["reason_event_id"] = date_info["reason_event_id"]

            #Incorporate any other status or properties that fall outside standard patterns
            for key in [
                "actual_departure_time_est",
                "actual_arrival_time_est",
                "estimated_departure_time_est",
                "estimated_arrival_time_est",
                "available_seats",
                "prices",
                "reason_event_id",
            ]:
                if key in date_info and key not in flight_info:
                    flight_info[key] = date_info[key]

            matched_data["flights"][flight_id] = flight_info
        payload = matched_flights
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightsByCriteria",
                "description": "Retrieve flights based on departure date, flight status, and optional origin and destination filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "departure_date": {
                            "type": "string",
                            "description": "Flight date in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of acceptable flight statuses (e.g., ['available', 'landed']).",
                        },
                        "origin": {
                            "type": "string",
                            "description": "Optional IATA code of the flight origin.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Optional IATA code of the flight destination.",
                        },
                    },
                    "required": ["departure_date", "status"],
                },
            },
        }


class UpdateFlightStatusByNumberAndDate(Tool):
    """API tool for updating the status and optionally modifying the estimated departure and arrival times of a specific flight on a designated date."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        date: str,
        new_status: str,
        new_departure_time_est: str | None = None,
        new_arrival_time_est: str | None = None,
        delay_hours: int | None = None,
        reason_event_id: str | None = None,
    ) -> str:
        pass
        flights = data.get("flights", {}).values()
        for flight in flights.values():
            if flight.get("flight_number") == flight_number:
                date_info = flight.get("dates", {}).values().get(date)
                if not date_info:
                    payload = {
                            "error": "Flight not found for the given number and date",
                            "flight_number": flight_number,
                            "date": date,
                        }
                    out = json.dumps(
                        payload)
                    return out

                date_info["status"] = new_status

                #Identify property names according to the status
                if new_status == "delayed":
                    dep_prop = "estimated_departure_time_est"
                    arr_prop = "estimated_arrival_time_est"
                else:  #landed, cancelled, or various other statuses
                    dep_prop = "actual_departure_time_est"
                    arr_prop = "actual_arrival_time_est"

                #Implement delay if indicated
                if delay_hours is not None:
                    try:
                        #Retrieve current time or default to scheduled time
                        existing_dep = (
                            date_info.get(dep_prop)
                            or date_info.get("actual_departure_time_est")
                            or f"{date}T{flight.get('scheduled_departure_time_est')}"
                        )
                        existing_arr = (
                            date_info.get(arr_prop)
                            or date_info.get("actual_arrival_time_est")
                            or f"{date}T{flight.get('scheduled_arrival_time_est')}"
                        )

                        dep_dt = datetime.fromisoformat(existing_dep)
                        arr_dt = datetime.fromisoformat(existing_arr)

                        delay_delta = timedelta(hours=delay_hours)
                        date_info[dep_prop] = (dep_dt + delay_delta).isoformat()
                        date_info[arr_prop] = (arr_dt + delay_delta).isoformat()
                    except Exception as e:
                        payload = {"error": f"Invalid datetime format: {str(e)}"}
                        out = json.dumps(
                            payload)
                        return out

                #Replace departure/arrival time if indicated
                if new_departure_time_est:
                    date_info[dep_prop] = f"{date}T{new_departure_time_est}"
                if new_arrival_time_est:
                    date_info[arr_prop] = f"{date}T{new_arrival_time_est}"

                #Remove properties that are not applicable for this status
                if new_status == "delayed":
                    #Eliminate actual times if present
                    date_info.pop("actual_departure_time_est", None)
                    date_info.pop("actual_arrival_time_est", None)
                    #Delete booking information
                    date_info.pop("available_seats", None)
                    date_info.pop("prices", None)
                elif new_status == "landed":
                    #Discard estimated times if available
                    date_info.pop("estimated_departure_time_est", None)
                    date_info.pop("estimated_arrival_time_est", None)
                    #Eliminate booking information
                    date_info.pop("available_seats", None)
                    date_info.pop("prices", None)
                elif new_status == "cancelled":
                    #Delete all time and booking details for cancelled flights
                    date_info.pop("actual_departure_time_est", None)
                    date_info.pop("actual_arrival_time_est", None)
                    date_info.pop("estimated_departure_time_est", None)
                    date_info.pop("estimated_arrival_time_est", None)
                    date_info.pop("available_seats", None)
                    date_info.pop("prices", None)

                if reason_event_id:
                    date_info["reason_event_id"] = reason_event_id
                payload = {flight_number: {date: date_info}}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Flight number not found", "flight_number": flight_number}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightStatusByNumberAndDate",
                "description": "Update the status and optionally times of a flight instance on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number to update.",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date of the flight in YYYY-MM-DD format.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New flight status (e.g., 'delayed', 'cancelled').",
                        },
                        "new_departure_time_est": {
                            "type": "string",
                            "description": "Optional new departure time in HH:MM:SS. Uses 'estimated_*' for delayed status, 'actual_*' for others.",
                        },
                        "new_arrival_time_est": {
                            "type": "string",
                            "description": "Optional new arrival time in HH:MM:SS. Uses 'estimated_*' for delayed status, 'actual_*' for others.",
                        },
                        "delay_hours": {
                            "type": "integer",
                            "description": "Optional delay in hours to apply to departure and arrival times (uses appropriate property names for status).",
                        },
                        "reason_event_id": {
                            "type": "string",
                            "description": "Optional event ID that caused this status update.",
                        },
                    },
                    "required": ["flight_number", "date", "new_status"],
                },
            },
        }


class GetCertificationDetails(Tool):
    """API tool for retrieving certification details using either the certification ID or certification code."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        certification_id: str | None = None,
        certification_code: str | None = None,
    ) -> str:
        pass
        if not certification_id and not certification_code:
            payload = {
                    "error": "Either certification_id or certification_code must be provided"
                }
            out = json.dumps(
                payload)
            return out

        certifications = data.get("certifications", {}).values()

        for cert in certifications.values():
            #Verify by ID if supplied
            if certification_id and cert.get("certification_id") == certification_id:
                payload = cert
                out = json.dumps(payload)
                return out
            #Verify by code if given
            if (
                certification_code
                and cert.get("certification_code") == certification_code
            ):
                payload = cert
                out = json.dumps(payload)
                return out

        #Provide a suitable error message according to the search conducted
        search_term = certification_id if certification_id else certification_code
        search_type = "certification_id" if certification_id else "certification_code"
        payload = {"error": "Certification not found", search_type: search_term}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetails",
                "description": "Get certification details using either certification ID (e.g., 'CERT_B738') or certification code (e.g., 'B737-800').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Certification ID (e.g., 'CERT_B738', 'CERT_ATPL'). Either this or certification_code must be provided.",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Certification code (e.g., 'B737-800', 'ATPL'). Either this or certification_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateAircraftStatus(Tool):
    """API tool for updating the aircraft status and optionally altering its location."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        new_status: str,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        new_location_iata: str | None = None,
    ) -> str:
        pass
        if not aircraft_id and not tail_number:
            payload = {"error": "Either aircraft_id or tail_number must be provided"}
            out = json.dumps(
                payload)
            return out

        #Acceptable status values derived from real data
        valid_statuses = ["Active", "Maintenance", "In Maintenance", "Stored"]
        if new_status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "provided_status": new_status,
                    "valid_statuses": valid_statuses,
                }
            out = json.dumps(
                payload)
            return out

        aircraft_list = data.get("aircraft", {}).values()
        airports = data.get("airports", {}).values()

        #Locate the aircraft
        target_aircraft = None
        for aircraft in aircraft_list.values():
            if (aircraft_id and aircraft.get("aircraft_id") == aircraft_id) or (
                tail_number and aircraft.get("tail_number") == tail_number
            ):
                target_aircraft = aircraft
                break

        if not target_aircraft:
            search_term = aircraft_id if aircraft_id else tail_number
            search_type = "aircraft_id" if aircraft_id else "tail_number"
            payload = {"error": "Aircraft not found", search_type: search_term}
            out = json.dumps(payload)
            return out

        #Revise status
        target_aircraft["status"] = new_status

        #Revise location if supplied
        if new_location_iata:
            #Locate the airport using the IATA code
            target_airport = None
            for airport in airports.values():
                if airport.get("iata_code") == new_location_iata:
                    target_airport = airport
                    break

            if not target_airport:
                payload = {
                        "error": "Airport not found for location update",
                        "iata_code": new_location_iata,
                    }
                out = json.dumps(
                    payload)
                return out

            #Revise the location of the aircraft
            target_aircraft["location"] = {
                "airport_id": target_airport["airport_id"],
                "iata_code": target_airport["iata_code"],
            }
        payload = {
                "aircraft_id": target_aircraft["aircraft_id"],
                "tail_number": target_aircraft["tail_number"],
                "status": target_aircraft["status"],
                "location": target_aircraft["location"],
                "updated": True,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftStatus",
                "description": "Update aircraft status and optionally change location using either aircraft ID or tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Aircraft ID (e.g., 'AC001'). Either this or tail_number must be provided.",
                        },
                        "tail_number": {
                            "type": "string",
                            "description": "Aircraft tail number (e.g., 'PR-GOL'). Either this or aircraft_id must be provided.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New aircraft status. Valid values: 'Active', 'Maintenance', 'In Maintenance', 'Stored'.",
                        },
                        "new_location_iata": {
                            "type": "string",
                            "description": "Optional new location IATA code (e.g., 'ATL'). Updates aircraft location if provided.",
                        },
                    },
                    "required": ["new_status"],
                },
            },
        }


class GetCrewMemberDetails(Tool):
    """API tool for retrieving the crew member profile and flight history using the crew member ID or employee code."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str | None = None,
        employee_code: str | None = None,
    ) -> str:
        pass
        if not crew_member_id and not employee_code:
            payload = {"error": "Either crew_member_id or employee_code must be provided"}
            out = json.dumps(
                payload)
            return out

        crew_members = data.get("crew_members", {}).values()

        #Locate the crew member
        target_crew_member = None
        for crew_member in crew_members.values():
            if (
                crew_member_id and crew_member.get("crew_member_id") == crew_member_id
            ) or (employee_code and crew_member.get("employee_code") == employee_code):
                target_crew_member = crew_member
                break

        if not target_crew_member:
            search_term = crew_member_id if crew_member_id else employee_code
            search_type = "crew_member_id" if crew_member_id else "employee_code"
            payload = {"error": "Crew member not found", search_type: search_term}
            out = json.dumps(
                payload)
            return out

        #Compute summary statistics for the flight
        flight_log = target_crew_member.get("flight_log", [])
        total_flights = len(flight_log)

        #Determine total hours categorized by type
        total_hours = {"total": 0, "pic": 0, "sic": 0, "night": 0, "instrument": 0}

        total_landings = 0
        total_takeoffs = 0
        aircraft_types = set()

        for flight_entry in flight_log:
            hours = flight_entry.get("hours_flown", {}).values()
            for hour_type in total_hours:
                total_hours[hour_type] += hours.get(hour_type, 0)

            total_landings += flight_entry.get("landings", 0)
            total_takeoffs += flight_entry.get("takeoffs", 0)

            aircraft_model = flight_entry.get("aircraft_model")
            if aircraft_model:
                aircraft_types.add(aircraft_model)

        #Formulate response including crew member information and computed statistics
        response = {
            "crew_member_id": target_crew_member.get("crew_member_id"),
            "employee_code": target_crew_member.get("employee_code"),
            "first_name": target_crew_member.get("first_name"),
            "last_name": target_crew_member.get("last_name"),
            "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
            "role": target_crew_member.get("role"),
            "home_base": target_crew_member.get("home_base"),
            "status": target_crew_member.get("status"),
            "flight_statistics": {
                "total_flights": total_flights,
                "total_hours": total_hours,
                "total_landings": total_landings,
                "total_takeoffs": total_takeoffs,
                "aircraft_types_flown": sorted(list(aircraft_types)),
            },
            "flight_log": flight_log,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewMemberDetails",
                "description": "Get crew member profile, flight history, and calculated statistics using either crew member ID or employee code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001'). Either this or employee_code must be provided.",
                        },
                        "employee_code": {
                            "type": "string",
                            "description": "Employee code (e.g., 'EMP001'). Either this or crew_member_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class AssignCrewToFlight(Tool):
    """API tool for establishing crew assignments for a flight."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_id: str,
        flight_number: str,
        crew_member_id: str,
        assigned_role: str,
    ) -> str:
        pass
        #Legitimate assigned role values based on real data
        valid_roles = ["Captain", "First Officer", "Flight Attendant"]
        if assigned_role not in valid_roles:
            payload = {
                    "error": "Invalid assigned role",
                    "provided_role": assigned_role,
                    "valid_roles": valid_roles,
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve data collections
        crew_members = data.get("crew_members", {}).values()
        flights = data.get("flights", {}).values()
        flight_crew_assignments = data.get("flight_crew_assignments", {}).values()

        #Confirm the existence of the crew member
        target_crew_member = None
        for crew_member in crew_members.values():
            if crew_member.get("crew_member_id") == crew_member_id:
                target_crew_member = crew_member
                break

        if not target_crew_member:
            payload = {"error": "Crew member not found", "crew_member_id": crew_member_id}
            out = json.dumps(
                payload)
            return out

        #Ensure the flight is present
        flight_exists = False
        for flight in flights.values():
            if flight.get("flight_number") == flight_number:
                flight_exists = True
                break

        if not flight_exists:
            payload = {"error": "Flight not found", "flight_number": flight_number}
            out = json.dumps(
                payload)
            return out

        #Verify if the crew member is already allocated to this flight
        for assignment in flight_crew_assignments.values():
            if (
                assignment.get("flight", {}).values().get("flight_id") == flight_id
                and assignment.get("crew_member", {}).values().get("crew_member_id")
                == crew_member_id
            ):
                payload = {
                        "error": "Crew member already assigned to this flight",
                        "flight_id": flight_id,
                        "crew_member_id": crew_member_id,
                        "existing_role": assignment.get("assigned_role"),
                    }
                out = json.dumps(
                    payload)
                return out

        #Determine if the role is already occupied for this flight (Captain and First Officer must be distinct)
        if assigned_role in ["Captain", "First Officer"]:
            for assignment in flight_crew_assignments.values():
                if (
                    assignment.get("flight", {}).values().get("flight_id") == flight_id
                    and assignment.get("assigned_role") == assigned_role
                ):
                    payload = {
                            "error": f"{assigned_role} role already assigned to this flight",
                            "flight_id": flight_id,
                            "assigned_role": assigned_role,
                            "existing_crew_member": assignment.get(
                                "crew_member", {}
                            ).get("full_name"),
                        }
                    out = json.dumps(
                        payload)
                    return out

        #Create a new assignment identifier
        existing_ids = [
            assignment.get("assignment_id", "")
            for assignment in flight_crew_assignments.values()
        ]
        assignment_numbers = []
        for id_str in existing_ids:
            if id_str.startswith("AS") and id_str[2:].isdigit():
                assignment_numbers.append(int(id_str[2:]))

        next_number = max(assignment_numbers) + 1 if assignment_numbers else 1
        new_assignment_id = f"AS{next_number:03d}"

        #Establish a new assignment
        new_assignment = {
            "assignment_id": new_assignment_id,
            "flight": {"flight_id": flight_id, "flight_number": flight_number},
            "crew_member": {
                "crew_member_id": crew_member_id,
                "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
            },
            "assigned_role": assigned_role,
        }

        #Include in the assignments list
        data["flight_crew_assignments"][new_assignment["flight_crew_assignment_id"]] = new_assignment
        payload = {"success": True, "assignment_created": new_assignment}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCrewToFlight",
                "description": "Create crew assignment for a flight. Validates crew member and flight exist, prevents duplicate assignments, and enforces role uniqueness for Captain and First Officer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_id": {
                            "type": "string",
                            "description": "Flight identifier (e.g., 'FL001').",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number (e.g., 'HAT004').",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001').",
                        },
                        "assigned_role": {
                            "type": "string",
                            "description": "Role to assign. Valid values: 'Captain', 'First Officer', 'Flight Attendant'.",
                        },
                    },
                    "required": [
                        "flight_id",
                        "flight_number",
                        "crew_member_id",
                        "assigned_role",
                    ],
                },
            },
        }


class GetFlightCrewAssignments(Tool):
    """API tool for retrieving crew assignments related to a specific flight."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_id: str | None = None,
        flight_number: str | None = None,
    ) -> str:
        pass
        if not flight_id and not flight_number:
            payload = {"error": "Either flight_id or flight_number must be provided"}
            out = json.dumps(
                payload)
            return out

        flight_crew_assignments = data.get("flight_crew_assignments", {}).values()
        flights = data.get("flights", {}).values()

        #Confirm flight existence if flight_number is given
        if flight_number:
            flight_exists = False
            for flight in flights.values():
                if flight.get("flight_number") == flight_number:
                    flight_exists = True
                    break

            if not flight_exists:
                payload = {"error": "Flight not found", "flight_number": flight_number}
                out = json.dumps(
                    payload)
                return out

        #Locate all assignments related to the specified flight
        matching_assignments = []
        for assignment in flight_crew_assignments.values():
            flight_info = assignment.get("flight", {}).values()

            #Verify if this assignment meets the criteria
            flight_matches = True
            if flight_id and flight_info.get("flight_id") != flight_id:
                flight_matches = False
            if flight_number and flight_info.get("flight_number") != flight_number:
                flight_matches = False

            if flight_matches:
                matching_assignments.append(assignment)

        if not matching_assignments:
            search_term = flight_id if flight_id else flight_number
            search_type = "flight_id" if flight_id else "flight_number"
            payload = {
                    "error": "No crew assignments found for flight",
                    search_type: search_term,
                }
            out = json.dumps(
                payload)
            return out

        #Categorize assignments by role for improved organization
        assignments_by_role = {
            "Captain": [],
            "First Officer": [],
            "Flight Attendant": [],
        }

        for assignment in matching_assignments:
            role = assignment.get("assigned_role")
            if role in assignments_by_role:
                assignments_by_role[role].append(assignment)

        #Retrieve flight details for the response
        flight_info = (
            matching_assignments[0].get("flight", {}).values() if matching_assignments else {}
        )

        #Compute a summary of the crew
        total_crew = len(matching_assignments)
        crew_count_by_role = {
            role: len(assignments) for role, assignments in assignments_by_role.items()
        }

        response = {
            "flight": flight_info,
            "crew_summary": {
                "total_crew_members": total_crew,
                "crew_count_by_role": crew_count_by_role,
            },
            "assignments_by_role": assignments_by_role,
            "all_assignments": matching_assignments,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightCrewAssignments",
                "description": "Get crew assignments for a specific flight using either flight ID or flight number. Returns organized crew assignments by role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_id": {
                            "type": "string",
                            "description": "Flight identifier (e.g., 'FL001'). Either this or flight_number must be provided.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number (e.g., 'HAT004'). Either this or flight_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetCrewCertifications(Tool):
    """API tool for obtaining crew member certifications and their validity status."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str | None = None,
        employee_code: str | None = None,
    ) -> str:
        pass
        if not crew_member_id and not employee_code:
            payload = {"error": "Either crew_member_id or employee_code must be provided"}
            out = json.dumps(
                payload)
            return out

        crew_certifications = data.get("crew_certifications", {}).values()
        crew_members = data.get("crew_members", {}).values()

        #Confirm the crew member's existence and retrieve their information
        target_crew_member = None
        for crew_member in crew_members.values():
            if (
                crew_member_id and crew_member.get("crew_member_id") == crew_member_id
            ) or (employee_code and crew_member.get("employee_code") == employee_code):
                target_crew_member = crew_member
                break

        if not target_crew_member:
            search_term = crew_member_id if crew_member_id else employee_code
            search_type = "crew_member_id" if crew_member_id else "employee_code"
            payload = {"error": "Crew member not found", search_type: search_term}
            out = json.dumps(
                payload)
            return out

        #Locate all certifications associated with this crew member
        crew_member_id_to_search = target_crew_member.get("crew_member_id")
        matching_certifications = []

        for cert_record in crew_certifications.values():
            cert_crew_member = cert_record.get("crew_member", {}).values()
            if cert_crew_member.get("crew_member_id") == crew_member_id_to_search:
                matching_data["certifications"][certification_id] = cert_record

        if not matching_certifications:
            payload = {
                    "crew_member": {
                        "crew_member_id": target_crew_member.get("crew_member_id"),
                        "employee_code": target_crew_member.get("employee_code"),
                        "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
                        "role": target_crew_member.get("role"),
                    },
                    "certifications": [],
                    "certification_summary": {
                        "total_certifications": 0,
                        "valid_certifications": 0,
                        "expired_certifications": 0,
                        "permanent_certifications": 0,
                    },
                }
            out = json.dumps(
                payload)
            return out

        #Obtain the current date for validity assessments
        from datetime import date

        current_date = date(2025, 9, 15)

        #Handle certifications and assess their validity
        processed_certifications = []
        valid_count = 0
        expired_count = 0
        permanent_count = 0

        for cert_record in matching_certifications:
            #Generate a record for processed certification
            processed_cert = dict(cert_record)  #Duplicate the original record

            #Assess the validity status
            expiry_date_str = cert_record.get("expiry_date")

            if expiry_date_str is None:
                #Absence of an expiry date indicates permanent certification
                processed_cert["validity_status"] = "permanent"
                processed_cert["is_valid"] = True
                processed_cert["days_until_expiry"] = None
                permanent_count += 1
                valid_count += 1
            else:
                #Analyze the expiry date and verify its validity
                try:
                    expiry_date = datetime.fromisoformat(expiry_date_str).date()
                    days_until_expiry = (expiry_date - current_date).days

                    if days_until_expiry > 0:
                        processed_cert["validity_status"] = "valid"
                        processed_cert["is_valid"] = True
                        processed_cert["days_until_expiry"] = days_until_expiry
                        valid_count += 1

                        #Include a warning for certifications nearing expiration
                        if days_until_expiry <= 30:
                            processed_cert["validity_status"] = "expiring_soon"
                            processed_cert["warning"] = (
                                f"Certification expires in {days_until_expiry} days"
                            )
                    else:
                        processed_cert["validity_status"] = "expired"
                        processed_cert["is_valid"] = False
                        processed_cert["days_until_expiry"] = days_until_expiry
                        processed_cert["expired_days_ago"] = abs(days_until_expiry)
                        expired_count += 1

                except ValueError:
                    #Date format is not valid
                    processed_cert["validity_status"] = "unknown"
                    processed_cert["is_valid"] = False
                    processed_cert["days_until_expiry"] = None
                    processed_cert["error"] = "Invalid expiry date format"

            processed_data["certifications"][certification_id] = processed_cert

        #Categorize certifications based on their validity status
        certifications_by_status = {
            "valid": [],
            "expiring_soon": [],
            "expired": [],
            "permanent": [],
        }

        for cert in processed_certifications:
            status = cert.get("validity_status", "unknown")
            if status in certifications_by_status:
                certifications_by_status[status].append(cert)

        #Formulate response
        response = {
            "crew_member": {
                "crew_member_id": target_crew_member.get("crew_member_id"),
                "employee_code": target_crew_member.get("employee_code"),
                "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
                "role": target_crew_member.get("role"),
            },
            "certification_summary": {
                "total_certifications": len(processed_certifications),
                "valid_certifications": valid_count,
                "expired_certifications": expired_count,
                "permanent_certifications": permanent_count,
            },
            "certifications_by_status": certifications_by_status,
            "all_certifications": processed_certifications,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertifications",
                "description": "Get crew member certifications and validity status using either crew member ID or employee code. Includes validity checks and expiry warnings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001'). Either this or employee_code must be provided.",
                        },
                        "employee_code": {
                            "type": "string",
                            "description": "Employee code (e.g., 'EMP001'). Either this or crew_member_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateCrewFlightLog(Tool):
    """API tool for updating crew member flight hours and experience by adding a new entry to the flight log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str,
        flight_id: str,
        flight_number: str,
        date: str,
        role: str,
        aircraft_model: str,
        hours_flown: dict[str, float],
        landings: int = 0,
        takeoffs: int = 0,
    ) -> str:
        pass
        #Check that necessary parameters are valid
        if not all(
            [crew_member_id, flight_id, flight_number, date, role, aircraft_model]
        ):
            payload = {
                    "error": "Missing required parameters",
                    "required": [
                        "crew_member_id",
                        "flight_id",
                        "flight_number",
                        "date",
                        "role",
                        "aircraft_model",
                    ],
                }
            out = json.dumps(
                payload)
            return out

        #Ensure the structure of hours_flown is valid
        required_hour_types = ["total", "pic", "sic", "night", "instrument"]
        if not isinstance(hours_flown, dict):
            payload = {
                    "error": "hours_flown must be a dictionary",
                    "required_structure": {
                        hour_type: "float" for hour_type in required_hour_types
                    },
                }
            out = json.dumps(
                payload)
            return out

        for hour_type in required_hour_types:
            if hour_type not in hours_flown:
                payload = {
                        "error": f"Missing hour type '{hour_type}' in hours_flown",
                        "required_hour_types": required_hour_types,
                    }
                out = json.dumps(
                    payload)
                return out

            if not isinstance(hours_flown[hour_type], (int, float)):
                payload = {
                        "error": f"Invalid hour value for '{hour_type}'. Must be a number",
                        "received": type(hours_flown[hour_type]).__name__,
                    }
                out = json.dumps(
                    payload)
                return out

        #Confirm the role is valid
        valid_roles = ["Captain", "First Officer", "Flight Attendant"]
        if role not in valid_roles:
            payload = {"error": "Invalid role", "valid_roles": valid_roles, "received": role}
            out = json.dumps(
                payload)
            return out

        #Check the date format (YYYY-MM-DD) for validity
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            payload = {"error": "Invalid date format. Expected YYYY-MM-DD", "received": date}
            out = json.dumps(
                payload)
            return out

        #Locate the crew member
        crew_members = data.get("crew_members", {}).values()
        target_crew_member = None
        crew_member_index = None

        for i, crew_member in enumerate(crew_members.values():
            if crew_member.get("crew_member_id") == crew_member_id:
                target_crew_member = crew_member
                crew_member_index = i
                break

        if not target_crew_member:
            payload = {"error": "Crew member not found", "crew_member_id": crew_member_id}
            out = json.dumps(
                payload)
            return out

        #Verify if a flight log entry exists for this flight and date
        existing_flight_log = target_crew_member.get("flight_log", [])
        for log_entry in existing_flight_log:
            if (
                log_entry.get("flight_id") == flight_id
                and log_entry.get("date") == date
            ):
                payload = {
                        "error": "Flight log entry already exists for this flight and date",
                        "existing_entry": {
                            "flight_id": flight_id,
                            "flight_number": log_entry.get("flight_number"),
                            "date": date,
                            "role": log_entry.get("role"),
                        },
                    }
                out = json.dumps(
                    payload)
                return out

        #Establish a new flight log entry
        new_flight_entry = {
            "flight_id": flight_id,
            "flight_number": flight_number,
            "date": date,
            "role": role,
            "aircraft_model": aircraft_model,
            "hours_flown": {
                "total": float(hours_flown["total"]),
                "pic": float(hours_flown["pic"]),
                "sic": float(hours_flown["sic"]),
                "night": float(hours_flown["night"]),
                "instrument": float(hours_flown["instrument"]),
            },
            "landings": int(landings),
            "takeoffs": int(takeoffs),
        }

        #Include the new flight entry in the crew member's flight log
        if "flight_log" not in target_crew_member:
            target_crew_member["flight_log"] = []

        target_crew_member["flight_log"].append(new_flight_entry)

        #Revise the crew member's information in the data
        data["crew_members"][crew_member_index] = target_crew_member

        #Compute updated totals for the response
        flight_log = target_crew_member.get("flight_log", [])
        total_flights = len(flight_log)

        total_hours = {"total": 0, "pic": 0, "sic": 0, "night": 0, "instrument": 0}

        total_landings = 0
        total_takeoffs = 0
        aircraft_types = set()

        for flight_entry in flight_log:
            hours = flight_entry.get("hours_flown", {}).values()
            for hour_type in total_hours:
                total_hours[hour_type] += hours.get(hour_type, 0)

            total_landings += flight_entry.get("landings", 0)
            total_takeoffs += flight_entry.get("takeoffs", 0)

            aircraft_model_entry = flight_entry.get("aircraft_model")
            if aircraft_model_entry:
                aircraft_types.add(aircraft_model_entry)

        #Formulate response
        response = {
            "success": True,
            "message": "Flight log entry added successfully",
            "crew_member": {
                "crew_member_id": target_crew_member.get("crew_member_id"),
                "employee_code": target_crew_member.get("employee_code"),
                "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
                "role": target_crew_member.get("role"),
            },
            "new_flight_entry": new_flight_entry,
            "updated_experience_summary": {
                "total_flights": total_flights,
                "total_flight_hours": total_hours,
                "total_landings": total_landings,
                "total_takeoffs": total_takeoffs,
                "aircraft_types_flown": sorted(list(aircraft_types)),
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewFlightLog",
                "description": "Update crew member flight hours and experience by adding a new flight log entry. Records flight time, landings, takeoffs, and updates overall experience.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001')",
                        },
                        "flight_id": {
                            "type": "string",
                            "description": "Unique flight identifier (e.g., 'FL001')",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number (e.g., 'HAT004')",
                        },
                        "date": {
                            "type": "string",
                            "description": "Flight date in YYYY-MM-DD format (e.g., '2024-05-01')",
                        },
                        "role": {
                            "type": "string",
                            "description": "Crew member's role on the flight. Must be one of: 'Captain', 'First Officer', 'Flight Attendant'",
                        },
                        "aircraft_model": {
                            "type": "string",
                            "description": "Aircraft model flown (e.g., 'B737-800', 'A320neo')",
                        },
                        "hours_flown": {
                            "type": "object",
                            "description": "Flight time breakdown by category",
                            "properties": {
                                "total": {
                                    "type": "number",
                                    "description": "Total flight hours",
                                },
                                "pic": {
                                    "type": "number",
                                    "description": "Pilot-in-command hours",
                                },
                                "sic": {
                                    "type": "number",
                                    "description": "Second-in-command hours",
                                },
                                "night": {
                                    "type": "number",
                                    "description": "Night flying hours",
                                },
                                "instrument": {
                                    "type": "number",
                                    "description": "Instrument flight hours",
                                },
                            },
                            "required": ["total", "pic", "sic", "night", "instrument"],
                        },
                        "landings": {
                            "type": "integer",
                            "description": "Number of landings performed (default: 0)",
                        },
                        "takeoffs": {
                            "type": "integer",
                            "description": "Number of takeoffs performed (default: 0)",
                        },
                    },
                    "required": [
                        "crew_member_id",
                        "flight_id",
                        "flight_number",
                        "date",
                        "role",
                        "aircraft_model",
                        "hours_flown",
                    ],
                },
            },
        }


class CreateReservation(Tool):
    """API tool for establishing new flight reservations for customers."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        user_id: str,
        user_email: str,
        origin: str,
        destination: str,
        flight_type: str,
        cabin: str,
        flights: list[dict[str, Any]],
        passengers: list[dict[str, str]],
        payment_method_id: str,
        created_at: str,
        total_baggages: int = 0,
        nonfree_baggages: int = 0,
        insurance: str = "no",
    ) -> str:
        pass
        #Check that necessary parameters are valid
        if not all(
            [
                reservation_id,
                user_id,
                user_email,
                origin,
                destination,
                flight_type,
                cabin,
                flights,
                passengers,
                payment_method_id,
                created_at,
            ]
        ):
            payload = {
                    "error": "Missing required parameters",
                    "required": [
                        "reservation_id",
                        "user_id",
                        "user_email",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_method_id",
                        "created_at",
                    ],
                }
            out = json.dumps(
                payload)
            return out

        #Confirm the flight_type is valid
        valid_flight_types = ["one_way", "round_trip", "multi_city"]
        if flight_type not in valid_flight_types:
            payload = {
                    "error": "Invalid flight_type",
                    "valid_flight_types": valid_flight_types,
                    "received": flight_type,
                }
            out = json.dumps(
                payload)
            return out

        #Ensure the cabin class is valid
        valid_cabins = ["basic_economy", "economy", "business", "first"]
        if cabin not in valid_cabins:
            payload = {
                    "error": "Invalid cabin class",
                    "valid_cabins": valid_cabins,
                    "received": cabin,
                }
            out = json.dumps(
                payload)
            return out

        #Check that insurance is valid
        valid_insurance = ["yes", "no"]
        if insurance not in valid_insurance:
            payload = {
                    "error": "Invalid insurance option",
                    "valid_insurance": valid_insurance,
                    "received": insurance,
                }
            out = json.dumps(
                payload)
            return out

        #Locate user using their email
        users = data.get("users", {}).values()
        target_user = None
        user_index = None

        for i, user in enumerate(users.values():
            if user.get("email") == user_email:
                target_user = user
                user_index = i
                break

        if not target_user:
            payload = {"error": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        #Utilize the supplied user_id (should be deterministic)

        #Ensure the structure of flights is valid
        if not isinstance(flights, list) or len(flights) == 0:
            payload = {"error": "flights must be a non-empty array"}
            out = json.dumps(payload)
            return out

        for i, flight in enumerate(flights.values():
            required_flight_fields = [
                "origin",
                "destination",
                "flight_number",
                "date",
                "price",
            ]
            for field in required_flight_fields:
                if field not in flight:
                    payload = {
                            "error": f"Missing field '{field}' in flight {i+1}",
                            "required_flight_fields": required_flight_fields,
                        }
                    out = json.dumps(
                        payload)
                    return out

            #Check the date format for validity
            try:
                datetime.strptime(flight["date"], "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": f"Invalid date format in flight {i+1}. Expected YYYY-MM-DD",
                        "received": flight["date"],
                    }
                out = json.dumps(
                    payload)
                return out

            #Confirm that the price is numeric
            if not isinstance(flight["price"], (int, float)):
                payload = {
                        "error": f"Invalid price in flight {i+1}. Must be a number",
                        "received": flight["price"],
                    }
                out = json.dumps(
                    payload)
                return out

        #Ensure the structure of passengers is valid
        if not isinstance(passengers, list) or len(passengers) == 0:
            payload = {"error": "passengers must be a non-empty array"}
            out = json.dumps(payload)
            return out

        for i, passenger in enumerate(passengers):
            required_passenger_fields = ["first_name", "last_name", "dob"]
            for field in required_passenger_fields:
                if field not in passenger:
                    payload = {
                            "error": f"Missing field '{field}' in passenger {i+1}",
                            "required_passenger_fields": required_passenger_fields,
                        }
                    out = json.dumps(
                        payload)
                    return out

            #Check the format of the date of birth for validity
            try:
                datetime.strptime(passenger["dob"], "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": f"Invalid date of birth format for passenger {i+1}. Expected YYYY-MM-DD",
                        "received": passenger["dob"],
                    }
                out = json.dumps(
                    payload)
                return out

        #Confirm the existence of a payment method for the user
        payment_methods = target_user.get("payment_methods", {}).values()
        if payment_method_id not in payment_methods:
            available_methods = list(payment_methods.keys())
            payload = {
                    "error": "Payment method not found for user",
                    "payment_method_id": payment_method_id,
                    "available_payment_methods": available_methods,
                }
            out = json.dumps(
                payload)
            return out

        payment_method = payment_methods[payment_method_id]

        #Compute the total amount
        total_amount = sum(flight["price"] for flight in flights.values()

        #Ensure the payment method has adequate funds (for gift cards and certificates)
        if payment_method["source"] in ["gift_card", "certificate"]:
            available_amount = payment_method.get("amount", 0)
            if available_amount < total_amount:
                payload = {
                        "error": "Insufficient funds in payment method",
                        "payment_method_id": payment_method_id,
                        "available_amount": available_amount,
                        "required_amount": total_amount,
                    }
                out = json.dumps(
                    payload)
                return out

        #Confirm that the reservation ID is unique
        existing_reservations = data.get("reservations", {}).values()
        if any(
            res.get("reservation_id") == reservation_id for res in existing_reservations.values()
        ):
            payload = {
                    "error": "Reservation ID already exists",
                    "reservation_id": reservation_id,
                }
            out = json.dumps(
                payload)
            return out

        #Establish a reservation
        reservation = {
            "reservation_id": reservation_id,
            "user_id": user_id,
            "origin": origin,
            "destination": destination,
            "flight_type": flight_type,
            "cabin": cabin,
            "flights": flights,
            "passengers": passengers,
            "payment_history": [
                {"payment_id": payment_method_id, "amount": total_amount}
            ],
            "created_at": created_at,
            "total_baggages": total_baggages,
            "nonfree_baggages": nonfree_baggages,
            "insurance": insurance,
        }

        #Include the reservation in the database
        if "reservations" not in data:
            data["reservations"] = []
        data["reservations"][reservation_id] = reservation

        #Revise the user's list of reservations
        if "reservations" not in target_user:
            target_user["reservations"] = []
        target_user["reservations"].append(reservation_id)

        #Revise the balance of the payment method for gift cards and certificates
        if payment_method["source"] in ["gift_card", "certificate"]:
            new_amount = payment_method["amount"] - total_amount
            data["users"][user_index]["payment_methods"][payment_method_id][
                "amount"
            ] = new_amount

        #Formulate response
        response = {
            "success": True,
            "message": "Reservation created successfully",
            "reservation": reservation,
            "user": {
                "email": target_user.get("email"),
                "name": target_user.get("name"),
                "membership": target_user.get("membership"),
            },
            "payment_details": {
                "payment_method_id": payment_method_id,
                "payment_source": payment_method["source"],
                "amount_charged": total_amount,
            },
        }

        #Include the remaining balance for gift cards and certificates
        if payment_method["source"] in ["gift_card", "certificate"]:
            response["payment_details"]["remaining_balance"] = new_amount
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReservation",
                "description": "Create a new flight reservation for a customer. Validates user, flights, passengers, and payment method, then creates the reservation and updates user records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier (e.g., 'RSV001', '4WQ150'). Must be unique across all reservations.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., 'chen_jackson_3290'). Must match existing user.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "Customer email address to identify the user",
                        },
                        "origin": {
                            "type": "string",
                            "description": "Trip origin IATA code (e.g., 'DFW')",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Trip destination IATA code (e.g., 'LAX')",
                        },
                        "flight_type": {
                            "type": "string",
                            "description": "Type of trip. Must be one of: 'one_way', 'round_trip', 'multi_city'",
                        },
                        "cabin": {
                            "type": "string",
                            "description": "Cabin class. Must be one of: 'basic_economy', 'economy', 'business', 'first'",
                        },
                        "flights": {
                            "type": "array",
                            "description": "Array of flight segments",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "origin": {
                                        "type": "string",
                                        "description": "Flight segment origin IATA code",
                                    },
                                    "destination": {
                                        "type": "string",
                                        "description": "Flight segment destination IATA code",
                                    },
                                    "flight_number": {
                                        "type": "string",
                                        "description": "Flight number (e.g., 'HAT170')",
                                    },
                                    "date": {
                                        "type": "string",
                                        "description": "Flight date in YYYY-MM-DD format",
                                    },
                                    "price": {
                                        "type": "number",
                                        "description": "Flight segment price",
                                    },
                                },
                                "required": [
                                    "origin",
                                    "destination",
                                    "flight_number",
                                    "date",
                                    "price",
                                ],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Array of passengers",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {
                                        "type": "string",
                                        "description": "Passenger first name",
                                    },
                                    "last_name": {
                                        "type": "string",
                                        "description": "Passenger last name",
                                    },
                                    "dob": {
                                        "type": "string",
                                        "description": "Passenger date of birth in YYYY-MM-DD format",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID from user's available payment methods",
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Total number of baggage items (default: 0)",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Number of paid baggage items (default: 0)",
                        },
                        "insurance": {
                            "type": "string",
                            "description": "Travel insurance option. Must be 'yes' or 'no' (default: 'no')",
                        },
                        "created_at": {
                            "type": "string",
                            "description": "Reservation creation timestamp in YYYY-MM-DDTHH:MM:SS format. Required for deterministic behavior.",
                        },
                    },
                    "required": [
                        "reservation_id",
                        "user_id",
                        "user_email",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_method_id",
                        "created_at",
                    ],
                },
            },
        }


class GetReservationDetails(Tool):
    """API tool for retrieving reservation details using the reservation ID."""

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        pass
        #Check that the necessary parameter is valid
        if not reservation_id:
            payload = {"error": "Missing required parameter", "required": "reservation_id"}
            out = json.dumps(
                payload)
            return out

        #Locate the reservation
        reservations = data.get("reservations", {}).values()
        target_reservation = None

        for reservation in reservations.values():
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                break

        if not target_reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(
                payload)
            return out

        #Retrieve user details if the user_id is present
        user_id = target_reservation.get("user_id")
        user_details = None

        if user_id:
            users = data.get("users", {}).values()
            for user in users.values():
                #Attempt to match the user by verifying if any reservation in their list corresponds
                user_reservations = user.get("reservations", [])
                if reservation_id in user_reservations:
                    user_details = {
                        "email": user.get("email"),
                        "name": user.get("name"),
                        "membership": user.get("membership"),
                        "address": user.get("address"),
                    }
                    break

        #Compute a summary of the trip
        flights = target_reservation.get("flights", [])
        #Utilize the reservation's total_cost if present (includes upgrades), otherwise total the flight prices
        calculated_total = target_reservation.get(
            "total_cost", sum(flight.get("price", 0) for flight in flights.values()
        )
        trip_summary = {
            "total_flights": len(flights),
            "total_cost": calculated_total,
            "departure_date": flights[0].get("date") if flights else None,
            "return_date": flights[-1].get("date") if len(flights) > 1 else None,
        }

        #Retrieve the number of passengers
        passengers = target_reservation.get("passengers", [])
        passenger_count = len(passengers)

        #Compute baggage fees (assuming $50 for each non-free bag)
        nonfree_baggages = target_reservation.get("nonfree_baggages", 0)
        baggage_cost = nonfree_baggages * 50

        #Retrieve payment information
        payment_history = target_reservation.get("payment_history", [])
        total_paid = sum(payment.get("amount", 0) for payment in payment_history.values()

        #Formulate an improved response
        response = {
            "reservation_id": target_reservation.get("reservation_id"),
            "status": "confirmed",  #All recorded reservations are validated
            "booking_details": {
                "origin": target_reservation.get("origin"),
                "destination": target_reservation.get("destination"),
                "flight_type": target_reservation.get("flight_type"),
                "cabin": target_reservation.get("cabin"),
                "created_at": target_reservation.get("created_at"),
                "insurance": target_reservation.get("insurance"),
            },
            "trip_summary": trip_summary,
            "flights": target_reservation.get("flights", []),
            "passengers": {"count": passenger_count, "details": passengers},
            "baggage": {
                "total_baggages": target_reservation.get("total_baggages", 0),
                "nonfree_baggages": nonfree_baggages,
                "estimated_baggage_cost": baggage_cost,
            },
            "payment": {
                "total_amount_paid": total_paid,
                "payment_history": payment_history,
            },
        }

        #Include user details if located
        if user_details:
            response["customer"] = user_details
        else:
            response["customer"] = {
                "user_id": user_id,
                "note": "User details not found or user account may have been modified",
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReservationDetails",
                "description": "Get detailed reservation information by reservation ID, including customer details, flight information, payment history, and trip summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier (e.g., '4WQ150', 'A7K2M9')",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class GetUserProfile(Tool):
    """API tool for obtaining customer profiles and preferences using their email address."""

    @staticmethod
    def invoke(data: dict[str, Any], user_email: str) -> str:
        pass
        #Check that the necessary parameter is valid
        if not user_email:
            payload = {"error": "Missing required parameter", "required": "user_email"}
            out = json.dumps(
                payload)
            return out

        #Locate user using their email
        users = data.get("users", {}).values()
        target_user = None

        for user in users.values():
            if user.get("email") == user_email:
                target_user = user
                break

        if not target_user:
            payload = {"error": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        #Handle payment methods with additional details
        payment_methods = target_user.get("payment_methods", {}).values()
        processed_payment_methods = []
        total_available_balance = 0

        for method_id, method_info in payment_methods.items():
            method_data = {
                "id": method_info.get("id", method_id),
                "source": method_info.get("source"),
                "primary_info": {},
            }

            if method_info.get("source") == "credit_card":
                method_data["primary_info"] = {
                    "brand": method_info.get("brand"),
                    "last_four": method_info.get("last_four"),
                }
            elif method_info.get("source") in ["gift_card", "certificate"]:
                amount = method_info.get("amount", 0)
                method_data["primary_info"] = {
                    "balance": amount,
                    "status": "active" if amount > 0 else "depleted",
                }
                total_available_balance += amount

            processed_payment_methods.append(method_data)

        #Handle saved passenger information
        saved_passengers = target_user.get("saved_passengers", [])
        passenger_count = len(saved_passengers)

        #Determine age based on the date of birth
        from datetime import datetime

        dob_str = target_user.get("dob")
        age = None
        if dob_str:
            try:
                dob = datetime.strptime(dob_str, "%Y-%m-%d")
                today = datetime(2025, 9, 15, 0, 0, 0)
                age = (
                    today.year
                    - dob.year
                    - ((today.month, today.day) < (dob.month, dob.day))
                )
            except ValueError:
                age = None

        #Retrieve a summary of reservation history
        reservations = target_user.get("reservations", [])
        reservation_count = len(reservations)

        #Assess membership benefits according to the level
        membership_level = target_user.get("membership", "basic")
        membership_benefits = {
            "basic": ["Standard check-in", "Basic customer service"],
            "silver": [
                "Priority check-in",
                "1 free bag",
                "Preferred seating",
                "Silver customer service",
            ],
            "gold": [
                "Priority check-in",
                "2 free bags",
                "Preferred seating",
                "Lounge access",
                "Gold customer service",
                "Priority boarding",
            ],
            "platinum": [
                "Priority check-in",
                "3 free bags",
                "Premium seating",
                "Lounge access",
                "Platinum customer service",
                "Priority boarding",
                "Upgrade eligibility",
            ],
        }

        #Formulate a detailed response
        response = {
            "profile": {
                "personal_info": {
                    "name": target_user.get("name"),
                    "email": target_user.get("email"),
                    "date_of_birth": target_user.get("dob"),
                    "age": age,
                },
                "contact_info": {"address": target_user.get("address")},
                "membership": {
                    "level": membership_level,
                    "benefits": membership_benefits.get(membership_level, []),
                },
            },
            "preferences": {
                "saved_passengers": {
                    "count": passenger_count,
                    "passengers": saved_passengers,
                },
                "payment_methods": {
                    "total_methods": len(processed_payment_methods),
                    "total_available_balance": total_available_balance,
                    "methods": processed_payment_methods,
                },
            },
            "account_summary": {
                "total_reservations": reservation_count,
                "reservation_ids": reservations,
                "account_status": "active",
                "profile_completeness": {
                    "has_address": bool(target_user.get("address")),
                    "has_payment_methods": len(payment_methods) > 0,
                    "has_saved_passengers": passenger_count > 0,
                    "completion_percentage": round(
                        (
                            sum(
                                [
                                    bool(target_user.get("name")),
                                    bool(target_user.get("email")),
                                    bool(target_user.get("address")),
                                    bool(target_user.get("dob")),
                                    len(payment_methods) > 0,
                                    len(saved_passengers) > 0,
                                ]
                            )
                            / 6
                        )
                        * 100
                    ),
                },
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Get comprehensive customer profile and preferences by email address, including personal information, membership details, payment methods, saved passengers, and account summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "Customer email address to identify the user (e.g., 'mia.li3818@example.com')",
                        }
                    },
                    "required": ["user_email"],
                },
            },
        }


class GetUserReservations(Tool):
    """API tool for retrieving all reservations for a user using user_id or email address."""

    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str | None = None, user_email: str | None = None
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not user_id and not user_email:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either user_id or user_email must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #If an email is given, locate the user_id initially
        target_user = None
        users = data.get("users", {}).values()

        if user_email:
            #Locate user using their email
            for user in users.values():
                if user.get("email") == user_email:
                    target_user = user
                    #Obtain user_id from reservation data for cross-referencing
                    reservations = data.get("reservations", {}).values()
                    user_reservation_ids = user.get("reservations", [])

                    #Determine the actual user_id by checking any reservation
                    if user_reservation_ids:
                        for reservation in reservations.values():
                            if (
                                reservation.get("reservation_id")
                                in user_reservation_ids
                            ):
                                user_id = reservation.get("user_id")
                                break
                    break

            if not target_user:
                payload = {"error": "User not found", "email": user_email}
                out = json.dumps(payload)
                return out
        else:
            #Locate user using user_id via reservations
            reservations = data.get("reservations", {}).values()
            user_reservation_ids = []

            #Initially, locate all reservations associated with this user_id
            for reservation in reservations.values():
                if reservation.get("user_id") == user_id:
                    user_reservation_ids.append(reservation.get("reservation_id"))

            #Subsequently, locate the user profile that includes these reservations
            for user in users.values():
                user_reservations = user.get("reservations", [])
                if any(res_id in user_reservation_ids for res_id in user_reservations.values():
                    target_user = user
                    break

        if not user_id:
            payload = {
                    "error": "User ID not found",
                    "provided_email": user_email if user_email else None,
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve all reservations for this user
        reservations = data.get("reservations", {}).values()
        user_reservations = []

        for reservation in reservations.values():
            if reservation.get("user_id") == user_id:
                #Generate a summary for each reservation
                flights = reservation.get("flights", [])
                passengers = reservation.get("passengers", [])
                total_cost = sum(flight.get("price", 0) for flight in flights.values()

                reservation_summary = {
                    "reservation_id": reservation.get("reservation_id"),
                    "origin": reservation.get("origin"),
                    "destination": reservation.get("destination"),
                    "flight_type": reservation.get("flight_type"),
                    "cabin": reservation.get("cabin"),
                    "created_at": reservation.get("created_at"),
                    "total_cost": total_cost,
                    "passenger_count": len(passengers),
                    "flight_count": len(flights),
                    "departure_date": flights[0].get("date") if flights else None,
                    "return_date": (
                        flights[-1].get("date") if len(flights) > 1 else None
                    ),
                    "insurance": reservation.get("insurance"),
                    "flights": flights,
                    "passengers": passengers,
                }

                user_data["reservations"][reservation_id] = reservation_summary

        #Organize reservations by creation date (latest first)
        user_reservations.sort(key=lambda x: x.get("created_at", ""), reverse=True)

        #Formulate response containing user information and reservations
        response = {
            "user_id": user_id,
            "total_reservations": len(user_reservations),
            "reservations": user_reservations,
        }

        #Include user profile details if accessible
        if target_user:
            response["user_profile"] = {
                "email": target_user.get("email"),
                "name": target_user.get("name"),
                "membership": target_user.get("membership"),
                "total_payment_methods": len(target_user.get("payment_methods", {})),
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserReservations",
                "description": "Get all reservations for a user by user_id or email address. Returns a comprehensive list of reservations with summary information for each booking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., 'chen_jackson_3290'). Either user_id or user_email must be provided.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "User email address (e.g., 'mia.li3818@example.com'). Either user_id or user_email must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateReservation(Tool):
    """API tool for altering existing flight reservations for customers. Enables updates to flights, passengers, baggage, insurance, and other reservation details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        flights: list[dict[str, Any]] | None = None,
        passengers: list[dict[str, str]] | None = None,
        cabin: str | None = None,
        total_baggages: int | None = None,
        nonfree_baggages: int | None = None,
        insurance: str | None = None,
        payment_method_id: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that the necessary parameter is valid
        if not reservation_id:
            payload = {"error": "Missing required parameter", "required": "reservation_id"}
            out = json.dumps(
                payload)
            return out

        #Locate the reservation
        reservations = data.get("reservations", {}).values()
        target_reservation = None
        reservation_index = None

        for i, reservation in enumerate(reservations.values():
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                reservation_index = i
                break

        if not target_reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(
                payload)
            return out

        #Identify the user linked to this reservation
        user_id = target_reservation.get("user_id")
        users = data.get("users", {}).values()
        target_user = None
        user_index = None

        for i, user in enumerate(users.values():
            user_reservations = user.get("reservations", [])
            if reservation_id in user_reservations:
                target_user = user
                user_index = i
                break

        if not target_user:
            payload = {
                    "error": "User not found for reservation",
                    "reservation_id": reservation_id,
                    "user_id": user_id,
                }
            out = json.dumps(
                payload)
            return out

        #Keep original values for potential rollback
        original_total_cost = sum(
            flight.get("price", 0) for flight in target_reservation.get("flights", [])
        )
        updates_made = []

        #Retain original cabin for calculating upgrade costs
        original_cabin = target_reservation.get("cabin")
        cabin_upgrade_cost = 0

        #Check and revise cabin class if supplied
        if cabin is not None:
            valid_cabins = ["basic_economy", "economy", "business", "first"]
            if cabin not in valid_cabins:
                payload = {
                        "error": "Invalid cabin class",
                        "valid_cabins": valid_cabins,
                        "received": cabin,
                    }
                out = json.dumps(
                    payload)
                return out

            #Determine the cost of upgrading the cabin if a change is made
            if original_cabin and original_cabin != cabin:
                #Establish the pricing framework for cabin upgrades
                cabin_multipliers = {
                    "basic_economy": 1.0,
                    "economy": 1.2,
                    "business": 1.8,
                    "first": 2.5,
                }

                original_multiplier = cabin_multipliers.get(original_cabin, 1.0)
                new_multiplier = cabin_multipliers.get(cabin, 1.0)

                #Compute the upgrade cost based on flight prices and the difference in cabin
                base_cost = sum(
                    flight.get("price", 0)
                    for flight in target_reservation.get("flights", [])
                )
                cabin_upgrade_cost = base_cost * (new_multiplier - original_multiplier)

                #Verify that the upgrade cost is non-negative (refunds should apply for downgrades)
                if cabin_upgrade_cost < 0:
                    cabin_upgrade_cost = cabin_upgrade_cost  #Maintain negative values for refunds

            target_reservation["cabin"] = cabin
            updates_made.append("cabin")

        #Check and revise insurance if supplied
        if insurance is not None:
            valid_insurance = ["yes", "no"]
            if insurance not in valid_insurance:
                payload = {
                        "error": "Invalid insurance option",
                        "valid_insurance": valid_insurance,
                        "received": insurance,
                    }
                out = json.dumps(
                    payload)
                return out
            target_reservation["insurance"] = insurance
            updates_made.append("insurance")

        #Check and revise baggage if supplied
        if total_baggages is not None:
            if not isinstance(total_baggages, int) or total_baggages < 0:
                payload = {
                        "error": "total_baggages must be a non-negative integer",
                        "received": total_baggages,
                    }
                out = json.dumps(
                    payload)
                return out
            target_reservation["total_baggages"] = total_baggages
            updates_made.append("total_baggages")

        if nonfree_baggages is not None:
            if not isinstance(nonfree_baggages, int) or nonfree_baggages < 0:
                payload = {
                        "error": "nonfree_baggages must be a non-negative integer",
                        "received": nonfree_baggages,
                    }
                out = json.dumps(
                    payload)
                return out
            target_reservation["nonfree_baggages"] = nonfree_baggages
            updates_made.append("nonfree_baggages")

        #Check and revise flights if supplied
        new_total_cost = original_total_cost
        if flights is not None:
            if not isinstance(flights, list) or len(flights) == 0:
                payload = {"error": "flights must be a non-empty array"}
                out = json.dumps(payload)
                return out

            for i, flight in enumerate(flights.values():
                required_flight_fields = [
                    "origin",
                    "destination",
                    "flight_number",
                    "date",
                    "price",
                ]
                for field in required_flight_fields:
                    if field not in flight:
                        payload = {
                                "error": f"Missing field '{field}' in flight {i+1}",
                                "required_flight_fields": required_flight_fields,
                            }
                        out = json.dumps(
                            payload)
                        return out

                #Check the date format for validity
                try:
                    datetime.strptime(flight["date"], "%Y-%m-%d")
                except ValueError:
                    payload = {
                            "error": f"Invalid date format in flight {i+1}. Expected YYYY-MM-DD",
                            "received": flight["date"],
                        }
                    out = json.dumps(
                        payload)
                    return out

                #Confirm that the price is numeric
                if not isinstance(flight["price"], (int, float)):
                    payload = {
                            "error": f"Invalid price in flight {i+1}. Must be a number",
                            "received": flight["price"],
                        }
                    out = json.dumps(
                        payload)
                    return out

            #Revise flights and compute the new total cost
            target_reservation["flights"] = flights
            new_total_cost = sum(flight["price"] for flight in flights.values()
            updates_made.append("flights")

            #Revise origin and destination according to new flights
            if flights:
                target_reservation["origin"] = flights[0]["origin"]
                target_reservation["destination"] = flights[-1]["destination"]
                updates_made.extend(["origin", "destination"])

        #Check and revise passengers if supplied
        if passengers is not None:
            if not isinstance(passengers, list) or len(passengers) == 0:
                payload = {"error": "passengers must be a non-empty array"}
                out = json.dumps(payload)
                return out

            for i, passenger in enumerate(passengers):
                required_passenger_fields = ["first_name", "last_name", "dob"]
                for field in required_passenger_fields:
                    if field not in passenger:
                        payload = {
                                "error": f"Missing field '{field}' in passenger {i+1}",
                                "required_passenger_fields": required_passenger_fields,
                            }
                        out = json.dumps(
                            payload)
                        return out

                #Check the format of the date of birth for validity
                try:
                    datetime.strptime(passenger["dob"], "%Y-%m-%d")
                except ValueError:
                    payload = {
                            "error": f"Invalid date of birth format for passenger {i+1}. Expected YYYY-MM-DD",
                            "received": passenger["dob"],
                        }
                    out = json.dumps(
                        payload)
                    return out

            target_reservation["passengers"] = passengers
            updates_made.append("passengers")

        #Manage payment adjustments if the cost has changed, cabin upgraded, or a new payment method is supplied
        cost_difference = new_total_cost - original_total_cost + cabin_upgrade_cost
        payment_processed = False

        if payment_method_id is not None or cost_difference != 0:
            #If a new payment method is supplied, confirm its existence
            if payment_method_id is not None:
                payment_methods = target_user.get("payment_methods", {}).values()
                if payment_method_id not in payment_methods:
                    available_methods = list(payment_methods.keys())
                    payload = {
                            "error": "Payment method not found for user",
                            "payment_method_id": payment_method_id,
                            "available_payment_methods": available_methods,
                        }
                    out = json.dumps(
                        payload)
                    return out

                payment_method = payment_methods[payment_method_id]

                #For cost increases or a new payment method, ensure there are sufficient funds
                if cost_difference > 0 or payment_method_id is not None:
                    if payment_method["source"] in ["gift_card", "certificate"]:
                        available_amount = payment_method.get("amount", 0)
                        required_amount = (
                            cost_difference if cost_difference > 0 else new_total_cost
                        )

                        if available_amount < required_amount:
                            payload = {
                                    "error": "Insufficient funds in payment method",
                                    "payment_method_id": payment_method_id,
                                    "available_amount": available_amount,
                                    "required_amount": required_amount,
                                }
                            out = json.dumps(
                                payload)
                            return out

                #Handle the payment adjustment
                if cost_difference != 0:
                    #Include an entry in the payment history
                    if "payment_history" not in target_reservation:
                        target_reservation["payment_history"] = []

                    target_reservation["payment_history"].append(
                        {"payment_id": payment_method_id, "amount": cost_difference}
                    )

                    #Revise the balance of the payment method for gift cards and certificates
                    if payment_method["source"] in ["gift_card", "certificate"]:
                        if cost_difference > 0:  #Extra fee
                            new_amount = payment_method["amount"] - cost_difference
                            data["users"][user_index]["payment_methods"][
                                payment_method_id
                            ]["amount"] = new_amount
                        elif cost_difference < 0:  #Reimbursement
                            new_amount = payment_method["amount"] + abs(cost_difference)
                            data["users"][user_index]["payment_methods"][
                                payment_method_id
                            ]["amount"] = new_amount

                    payment_processed = True
                    updates_made.append("payment")

        #Revise the total cost of the reservation
        target_reservation["total_cost"] = new_total_cost + cabin_upgrade_cost

        #Revise the reservation within the database
        data["reservations"][reservation_index] = target_reservation

        #Compute the updated trip summary
        flights = target_reservation.get("flights", [])
        passengers = target_reservation.get("passengers", [])
        trip_summary = {
            "total_flights": len(flights),
            "total_cost": new_total_cost + cabin_upgrade_cost,
            "departure_date": flights[0].get("date") if flights else None,
            "return_date": flights[-1].get("date") if len(flights) > 1 else None,
            "passenger_count": len(passengers),
        }

        #Formulate response
        response = {
            "success": True,
            "message": "Reservation updated successfully",
            "reservation_id": reservation_id,
            "updates_made": updates_made,
            "trip_summary": trip_summary,
            "updated_reservation": target_reservation,
        }

        if payment_processed:
            response["payment_adjustment"] = {
                "cost_difference": cost_difference,
                "new_total_cost": new_total_cost + cabin_upgrade_cost,
                "original_total_cost": original_total_cost,
                "cabin_upgrade_cost": (
                    cabin_upgrade_cost if cabin_upgrade_cost != 0 else None
                ),
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservation",
                "description": "Modify existing flight reservations. Allows updating flights, passengers, cabin class, baggage, insurance, and payment methods. Automatically handles payment adjustments for cost changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier to update (e.g., '4WQ150', 'A7K2M9')",
                        },
                        "flights": {
                            "type": "array",
                            "description": "Updated flight segments. Each flight must include origin, destination, flight_number, date (YYYY-MM-DD), and price",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"},
                                    "flight_number": {"type": "string"},
                                    "date": {"type": "string"},
                                    "price": {"type": "number"},
                                },
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Updated passenger list. Each passenger must include first_name, last_name, and dob (YYYY-MM-DD)",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {"type": "string"},
                                },
                            },
                        },
                        "cabin": {
                            "type": "string",
                            "description": "Updated cabin class: 'basic_economy', 'economy', 'business', or 'first'",
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Updated total number of baggage items",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Updated number of paid baggage items",
                        },
                        "insurance": {
                            "type": "string",
                            "description": "Updated travel insurance option: 'yes' or 'no'",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID for processing cost differences (e.g., 'credit_card_4421486', 'gift_card_5309492')",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class GetAircraftMaintenanceHistory(Tool):
    """API tool for retrieving maintenance logs for a specific aircraft using aircraft_id or tail_number."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str | None = None,
        tail_number: str | None = None,
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not aircraft_id and not tail_number:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either aircraft_id or tail_number must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Locate the aircraft initially to confirm its existence and obtain both identifiers
        aircraft_data = data.get("aircraft", {}).values()
        target_aircraft = None

        for aircraft in aircraft_data.values():
            if (aircraft_id and aircraft.get("aircraft_id") == aircraft_id) or (
                tail_number and aircraft.get("tail_number") == tail_number
            ):
                target_aircraft = aircraft
                break

        if not target_aircraft:
            payload = {
                    "error": "Aircraft not found",
                    "aircraft_id": aircraft_id,
                    "tail_number": tail_number,
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve both identifiers for a thorough search
        target_aircraft_id = target_aircraft.get("aircraft_id")
        target_tail_number = target_aircraft.get("tail_number")

        #Locate all maintenance records for this aircraft
        maintenance_logs = data.get("maintenance_logs", {}).values()
        aircraft_maintenance = []

        for log in maintenance_logs.values():
            aircraft_info = log.get("aircraft", {}).values()
            log_aircraft_id = aircraft_info.get("aircraft_id")
            log_tail_number = aircraft_info.get("tail_number")

            #Identify using either aircraft_id or tail_number
            if (
                log_aircraft_id == target_aircraft_id
                or log_tail_number == target_tail_number
            ):
                #Establish a detailed maintenance record
                maintenance_record = {
                    "log_id": log.get("log_id"),
                    "event_timestamp_utc": log.get("event_timestamp_utc"),
                    "maintenance_type": log.get("maintenance_type"),
                    "description": log.get("description"),
                    "status": log.get("status"),
                    "technician_id": log.get("technician_id"),
                    "work_order_id": log.get("work_order_id"),
                    "ata_chapter": log.get("ata_chapter"),
                    "corrective_action": log.get("corrective_action"),
                    "mel_cdl_reference": log.get("mel_cdl_reference"),
                    "next_due": log.get("next_due"),
                }

                aircraft_maintenance.append(maintenance_record)

        #Organize maintenance logs by timestamp (latest first)
        aircraft_maintenance.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Compute summary statistics
        total_maintenance_events = len(aircraft_maintenance)
        maintenance_types = {}
        status_counts = {}
        latest_maintenance = aircraft_maintenance[0] if aircraft_maintenance else None

        for record in aircraft_maintenance:
            #Tally by type of maintenance
            mtype = record.get("maintenance_type", "Unknown")
            maintenance_types[mtype] = maintenance_types.get(mtype, 0) + 1

            #Tally by status
            status = record.get("status", "Unknown")
            status_counts[status] = status_counts.get(status, 0) + 1

        #Locate the upcoming scheduled maintenance
        next_scheduled = None
        for record in aircraft_maintenance:
            if record.get("status") == "Scheduled":
                if not next_scheduled or record.get(
                    "event_timestamp_utc", ""
                ) < next_scheduled.get("event_timestamp_utc", ""):
                    next_scheduled = record

        #Identify any overdue maintenance (status is Scheduled but timestamp is past)
        overdue_maintenance = []
        from datetime import datetime

        current_time = datetime(2025, 9, 15, 0, 0, 0).isoformat().replace("+00:00", "Z")

        for record in aircraft_maintenance:
            if (
                record.get("status") == "Scheduled"
                and record.get("event_timestamp_utc", "") < current_time
            ):
                overdue_maintenance.append(record)

        #Formulate a detailed response
        response = {
            "aircraft": {
                "aircraft_id": target_aircraft.get("aircraft_id"),
                "tail_number": target_aircraft.get("tail_number"),
                "model": target_aircraft.get("model"),
                "status": target_aircraft.get("status"),
                "location": target_aircraft.get("location"),
            },
            "maintenance_summary": {
                "total_maintenance_events": total_maintenance_events,
                "maintenance_types": maintenance_types,
                "status_counts": status_counts,
                "latest_maintenance": latest_maintenance,
                "next_scheduled": next_scheduled,
                "overdue_count": len(overdue_maintenance),
            },
            "maintenance_history": aircraft_maintenance,
        }

        if overdue_maintenance:
            response["overdue_maintenance"] = overdue_maintenance
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftMaintenanceHistory",
                "description": "Get comprehensive maintenance logs and history for a specific aircraft by aircraft_id or tail_number. Returns maintenance records, summary statistics, and scheduling information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Unique aircraft identifier (e.g., 'AC001', 'AC004'). Either aircraft_id or tail_number must be provided.",
                        },
                        "tail_number": {
                            "type": "string",
                            "description": "Aircraft registration/tail number (e.g., 'PR-GOL', 'PS-AEF'). Either aircraft_id or tail_number must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class CreateMaintenanceEntry(Tool):
    """API tool for recording new maintenance activities for aircraft."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str,
        maintenance_type: str,
        description: str,
        work_order_id: str,
        ata_chapter: str,
        corrective_action: str,
        event_timestamp_utc: str,
        technician_id: str | None = None,
        status: str = "Scheduled",
        mel_cdl_reference: str | None = None,
        next_due: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that necessary parameters are valid
        required_params = [
            "aircraft_id",
            "maintenance_type",
            "description",
            "work_order_id",
            "ata_chapter",
            "corrective_action",
            "event_timestamp_utc",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        for param in required_params:
            if not params_dict.get(param):
                payload = {"error": "Missing required parameter", "required": param}
                out = json.dumps(
                    payload)
                return out

        #Create technician_id if not supplied (deterministic based on aircraft and timestamp)
        if not technician_id:
            #Establish a deterministic technician assignment based on the aircraft and work order
            import hashlib

            seed = f"{aircraft_id}_{work_order_id}"
            hash_value = int(hashlib.md5(seed.encode()).hexdigest()[:4], 16)
            technician_number = (hash_value % 50) + 1  #Create identifiers from TECH001 to TECH050
            technician_id = f"TECH{technician_number:03d}"

        #Confirm the aircraft is present
        aircraft_data = data.get("aircraft", {}).values()
        target_aircraft = None

        for aircraft in aircraft_data.values():
            if aircraft.get("aircraft_id") == aircraft_id:
                target_aircraft = aircraft
                break

        if not target_aircraft:
            payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
            out = json.dumps(
                payload)
            return out

        #Check the status for validity
        valid_statuses = ["Scheduled", "In Progress", "Completed", "Deferred"]
        if status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status,
                }
            out = json.dumps(
                payload)
            return out

        #Confirm the maintenance_type is valid
        valid_maintenance_types = [
            "A-Check",
            "B-Check",
            "C-Check",
            "D-Check",
            "Line Maintenance",
            "Engine Repair",
            "Avionics Repair",
            "Structural Repair",
            "Avionics Update",
            "Emergency Repair",
            "Unscheduled",
        ]
        if maintenance_type not in valid_maintenance_types:
            payload = {
                    "error": "Invalid maintenance type",
                    "valid_maintenance_types": valid_maintenance_types,
                    "received": maintenance_type,
                }
            out = json.dumps(
                payload)
            return out

        #Check the format of event_timestamp_utc (now required)
        try:
            datetime.fromisoformat(event_timestamp_utc.replace("Z", "+00:00"))
        except ValueError:
            payload = {
                    "error": "Invalid event_timestamp_utc format. Expected ISO format with Z suffix (e.g., '2024-07-28T10:00:00Z')",
                    "received": event_timestamp_utc,
                }
            out = json.dumps(
                payload)
            return out

        #Check the format of next_due if supplied
        if next_due:
            try:
                datetime.strptime(next_due, "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": "Invalid next_due format. Expected YYYY-MM-DD",
                        "received": next_due,
                    }
                out = json.dumps(
                    payload)
                return out

        #Create a unique identifier for the maintenance log
        maintenance_logs = data.get("maintenance_logs", {}).values()
        existing_numbers = []

        #Obtain existing log numbers
        for log in maintenance_logs.values():
            log_id = log.get("log_id", "")
            if log_id.startswith("ML") and len(log_id) == 5:
                try:
                    number = int(log_id[2:])  #Retrieve the number portion following "ML"
                    existing_numbers.append(number)
                except ValueError:
                    continue

        #Determine the next available number (highest + 1)
        next_number = max(existing_numbers) + 1 if existing_numbers else 1
        log_id = f"ML{next_number:03d}"

        #Confirm that the work_order_id is unique
        existing_work_orders = [log.get("work_order_id") for log in maintenance_logs.values()]
        if work_order_id in existing_work_orders:
            payload = {
                    "error": "Work order ID already exists",
                    "work_order_id": work_order_id,
                    "existing_work_orders": existing_work_orders,
                }
            out = json.dumps(
                payload)
            return out

        #Establish a maintenance entry
        maintenance_entry = {
            "log_id": log_id,
            "aircraft": {
                "aircraft_id": target_aircraft.get("aircraft_id"),
                "tail_number": target_aircraft.get("tail_number"),
            },
            "event_timestamp_utc": event_timestamp_utc,
            "maintenance_type": maintenance_type,
            "description": description,
            "status": status,
            "technician_id": technician_id,
            "work_order_id": work_order_id,
            "ata_chapter": ata_chapter,
            "corrective_action": corrective_action,
            "mel_cdl_reference": mel_cdl_reference,
            "next_due": next_due,
        }

        #Include in the maintenance logs
        if "maintenance_logs" not in data:
            data["maintenance_logs"] = []
        data["maintenance_logs"].append(maintenance_entry)

        #Formulate response
        response = {
            "success": True,
            "message": "Maintenance entry created successfully",
            "maintenance_entry": maintenance_entry,
            "aircraft": {
                "aircraft_id": target_aircraft.get("aircraft_id"),
                "tail_number": target_aircraft.get("tail_number"),
                "model": target_aircraft.get("model"),
                "status": target_aircraft.get("status"),
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMaintenanceEntry",
                "description": "Log new maintenance activity for aircraft. Creates a maintenance record with all required details including work orders, technician assignments, and scheduling information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Unique aircraft identifier (e.g., 'AC001', 'AC004')",
                        },
                        "maintenance_type": {
                            "type": "string",
                            "description": "Type of maintenance: 'A-Check', 'B-Check', 'C-Check', 'D-Check', 'Line Maintenance', 'Engine Repair', 'Avionics Repair', 'Structural Repair', 'Avionics Update', 'Emergency Repair'",
                        },
                        "description": {
                            "type": "string",
                            "description": "Detailed description of the maintenance activity",
                        },
                        "technician_id": {
                            "type": "string",
                            "description": "ID of the assigned technician (e.g., 'TECH012'). If not provided, will be auto-assigned deterministically.",
                        },
                        "work_order_id": {
                            "type": "string",
                            "description": "Unique work order reference (e.g., 'WO-2024-07-28-001')",
                        },
                        "ata_chapter": {
                            "type": "string",
                            "description": "ATA chapter reference (e.g., '05', '72', '34')",
                        },
                        "corrective_action": {
                            "type": "string",
                            "description": "Detailed description of corrective action to be taken or performed",
                        },
                        "event_timestamp_utc": {
                            "type": "string",
                            "description": "Maintenance event timestamp in UTC (ISO format with Z suffix, e.g., '2024-07-28T10:00:00Z'). Required for deterministic behavior.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Initial maintenance status: 'Scheduled', 'In Progress', 'Completed', or 'Deferred'. Defaults to 'Scheduled'.",
                        },
                        "mel_cdl_reference": {
                            "type": "string",
                            "description": "MEL/CDL reference if applicable (e.g., 'MEL-72-001')",
                        },
                        "next_due": {
                            "type": "string",
                            "description": "Next maintenance due date in YYYY-MM-DD format (optional)",
                        },
                    },
                    "required": [
                        "aircraft_id",
                        "maintenance_type",
                        "description",
                        "work_order_id",
                        "ata_chapter",
                        "corrective_action",
                        "event_timestamp_utc",
                    ],
                },
            },
        }


class UpdateMaintenanceStatus(Tool):
    """API tool for revising maintenance status and completion details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_id: str,
        status: str,
        corrective_action: str | None = None,
        next_due: str | None = None,
        mel_cdl_reference: str | None = None,
        technician_id: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that necessary parameters are valid
        if not log_id or not status:
            payload = {
                    "error": "Missing required parameters",
                    "required": ["log_id", "status"],
                }
            out = json.dumps(
                payload)
            return out

        #Check the status for validity
        valid_statuses = ["Scheduled", "In Progress", "Completed", "Deferred"]
        if status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status,
                }
            out = json.dumps(
                payload)
            return out

        #Locate the maintenance entry
        maintenance_logs = data.get("maintenance_logs", {}).values()
        target_entry = None
        entry_index = None

        for i, entry in enumerate(maintenance_logs.values():
            if entry.get("log_id") == log_id:
                target_entry = entry
                entry_index = i
                break

        if not target_entry:
            payload = {"error": "Maintenance entry not found", "log_id": log_id}
            out = json.dumps(
                payload)
            return out

        #Retain the original status for comparison
        original_status = target_entry.get("status")
        updates_made = []

        #Revise the status
        target_entry["status"] = status
        updates_made.append("status")

        #Revise the corrective action if supplied
        if corrective_action is not None:
            target_entry["corrective_action"] = corrective_action
            updates_made.append("corrective_action")

        #Revise the technician if supplied
        if technician_id is not None:
            target_entry["technician_id"] = technician_id
            updates_made.append("technician_id")

        #Revise the MEL/CDL reference if supplied
        if mel_cdl_reference is not None:
            target_entry["mel_cdl_reference"] = mel_cdl_reference
            updates_made.append("mel_cdl_reference")

        #Note: completion_timestamp_utc is excluded from the database schema, thus not processed

        #Revise the next due date if supplied
        if next_due is not None:
            if next_due:  #String that is not empty
                try:
                    datetime.strptime(next_due, "%Y-%m-%d")
                    target_entry["next_due"] = next_due
                except ValueError:
                    payload = {
                            "error": "Invalid next_due format. Expected YYYY-MM-DD",
                            "received": next_due,
                        }
                    out = json.dumps(
                        payload)
                    return out
            else:  #String that is empty or None
                target_entry["next_due"] = None
            updates_made.append("next_due")

        #Revise the entry within the database
        data["maintenance_logs"][entry_index] = target_entry

        #Retrieve information about the aircraft
        aircraft_info = target_entry.get("aircraft", {}).values()
        aircraft_data = data.get("aircraft", {}).values()
        full_aircraft_info = None

        for aircraft in aircraft_data.values():
            if aircraft.get("aircraft_id") == aircraft_info.get("aircraft_id"):
                full_aircraft_info = aircraft
                break

        #Formulate response
        response = {
            "success": True,
            "message": "Maintenance status updated successfully",
            "log_id": log_id,
            "status_change": {"from": original_status, "to": status},
            "updates_made": updates_made,
            "updated_entry": target_entry,
        }

        if full_aircraft_info:
            response["aircraft"] = {
                "aircraft_id": full_aircraft_info.get("aircraft_id"),
                "tail_number": full_aircraft_info.get("tail_number"),
                "model": full_aircraft_info.get("model"),
                "status": full_aircraft_info.get("status"),
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMaintenanceStatus",
                "description": "Update maintenance status and details. Allows updating status, corrective actions, and scheduling information for existing maintenance entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "Unique maintenance log identifier (e.g., 'ML001', 'ML005')",
                        },
                        "status": {
                            "type": "string",
                            "description": "Updated maintenance status: 'Scheduled', 'In Progress', 'Completed', or 'Deferred'",
                        },
                        "corrective_action": {
                            "type": "string",
                            "description": "Updated description of corrective action taken or to be taken",
                        },
                        "next_due": {
                            "type": "string",
                            "description": "Next maintenance due date in YYYY-MM-DD format. Set to empty string or null to clear.",
                        },
                        "mel_cdl_reference": {
                            "type": "string",
                            "description": "MEL/CDL reference if applicable (e.g., 'MEL-72-001'). Set to empty string or null to clear.",
                        },
                        "technician_id": {
                            "type": "string",
                            "description": "Updated technician ID if reassignment is needed (e.g., 'TECH025')",
                        },
                    },
                    "required": ["log_id", "status"],
                },
            },
        }


class CreateOperationalEvent(Tool):
    """API tool for recording new operational events that impact flights, aircraft, or airports."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        event_type: str,
        event_timestamp_utc: str,
        details: str,
        status: str = "Active",
        flight_id: str | None = None,
        flight_number: str | None = None,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        airport_id: str | None = None,
        iata_code: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that necessary parameters are valid
        if not all([event_type, event_timestamp_utc, details]):
            payload = {
                    "error": "Missing required parameters",
                    "required": ["event_type", "event_timestamp_utc", "details"],
                }
            out = json.dumps(
                payload)
            return out

        #Check the event_type for validity
        valid_event_types = [
            "Gate Change",
            "Minor Delay",
            "Technical Issue",
            "Weather Delay",
            "Crew Replacement",
            "Diversion Landing",
            "Aircraft AOG",
        ]
        if event_type not in valid_event_types:
            payload = {
                    "error": "Invalid event type",
                    "valid_event_types": valid_event_types,
                    "received": event_type,
                }
            out = json.dumps(
                payload)
            return out

        #Check the status for validity
        valid_statuses = ["Active", "Resolved", "Monitoring"]
        if status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status,
                }
            out = json.dumps(
                payload)
            return out

        #Check the format of event_timestamp_utc for validity
        try:
            datetime.fromisoformat(event_timestamp_utc.replace("Z", "+00:00"))
        except ValueError:
            payload = {
                    "error": "Invalid event_timestamp_utc format. Expected ISO format with Z suffix (e.g., '2024-05-01T14:30:00Z')",
                    "received": event_timestamp_utc,
                }
            out = json.dumps(
                payload)
            return out

        #Ensure that at least one association is supplied
        if not any(
            [
                flight_id and flight_number,
                aircraft_id and tail_number,
                airport_id and iata_code,
            ]
        ):
            payload = {
                    "error": "At least one association must be provided",
                    "required": "Either (flight_id AND flight_number) OR (aircraft_id AND tail_number) OR (airport_id AND iata_code)",
                }
            out = json.dumps(
                payload)
            return out

        #Check the aircraft association if supplied
        if aircraft_id or tail_number:
            if not (aircraft_id and tail_number):
                payload = {
                        "error": "Both aircraft_id and tail_number must be provided together",
                        "received": {
                            "aircraft_id": aircraft_id,
                            "tail_number": tail_number,
                        },
                    }
                out = json.dumps(
                    payload)
                return out

            #Confirm the aircraft is present
            aircraft_data = data.get("aircraft", {}).values()
            aircraft_exists = any(
                aircraft.get("aircraft_id") == aircraft_id
                and aircraft.get("tail_number") == tail_number
                for aircraft in aircraft_data.values()
            )
            if not aircraft_exists:
                payload = {
                        "error": "Aircraft not found",
                        "aircraft_id": aircraft_id,
                        "tail_number": tail_number,
                    }
                out = json.dumps(
                    payload)
                return out

        #Check the airport association if supplied
        if airport_id or iata_code:
            if not (airport_id and iata_code):
                payload = {
                        "error": "Both airport_id and iata_code must be provided together",
                        "received": {"airport_id": airport_id, "iata_code": iata_code},
                    }
                out = json.dumps(
                    payload)
                return out

            #Confirm the airport is present
            airports = data.get("airports", {}).values()
            airport_exists = any(
                airport.get("airport_id") == airport_id
                and airport.get("iata_code") == iata_code
                for airport in airports.values()
            )
            if not airport_exists:
                payload = {
                        "error": "Airport not found",
                        "airport_id": airport_id,
                        "iata_code": iata_code,
                    }
                out = json.dumps(
                    payload)
                return out

        #Create a unique event ID (sequential format: OE001, OE002, etc.)
        operational_events = data.get("operational_events", {}).values()
        existing_numbers = []

        for event in operational_events.values():
            event_id = event.get("event_id", "")
            if event_id.startswith("OE") and len(event_id) == 5:
                try:
                    number = int(event_id[2:])  #Retrieve the number portion following "OE"
                    existing_numbers.append(number)
                except ValueError:
                    continue

        #Determine the next available number (highest + 1)
        next_number = max(existing_numbers) + 1 if existing_numbers else 1
        event_id = f"OE{next_number:03d}"

        #Establish a new operational event
        new_event = {
            "event_id": event_id,
            "event_type": event_type,
            "event_timestamp_utc": event_timestamp_utc,
            "status": status,
            "details": details,
        }

        #Include associations if supplied
        if flight_id and flight_number:
            new_event["flight"] = {
                "flight_id": flight_id,
                "flight_number": flight_number,
            }

        if aircraft_id and tail_number:
            new_event["aircraft"] = {
                "aircraft_id": aircraft_id,
                "tail_number": tail_number,
            }

        if airport_id and iata_code:
            new_event["airport"] = {"airport_id": airport_id, "iata_code": iata_code}

        #Include in the operational events
        data["operational_events"][new_event["operational_event_id"]] = new_event
        data["operational_events"] = operational_events

        #Formulate response
        response = {
            "success": True,
            "message": "Operational event created successfully",
            "event": new_event,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOperationalEvent",
                "description": "Log new operational events affecting flights, aircraft, or airports. Creates comprehensive event records with proper associations and validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {
                            "type": "string",
                            "description": "Type of operational event: 'Gate Change', 'Minor Delay', 'Technical Issue', 'Weather Delay', 'Crew Replacement', 'Diversion Landing', 'Aircraft AOG'",
                        },
                        "event_timestamp_utc": {
                            "type": "string",
                            "description": "Event timestamp in UTC (ISO format with Z suffix, e.g., '2024-05-01T14:30:00Z'). Required for deterministic behavior.",
                        },
                        "details": {
                            "type": "string",
                            "description": "Detailed description of the operational event",
                        },
                        "status": {
                            "type": "string",
                            "description": "Event status: 'Active', 'Resolved', or 'Monitoring'. Defaults to 'Active'.",
                        },
                        "flight_id": {
                            "type": "string",
                            "description": "Associated flight ID (e.g., 'FL001'). Must be provided with flight_number if flight association is needed.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Associated flight number (e.g., 'HAT004'). Must be provided with flight_id if flight association is needed.",
                        },
                        "aircraft_id": {
                            "type": "string",
                            "description": "Associated aircraft ID (e.g., 'AC001'). Must be provided with tail_number if aircraft association is needed.",
                        },
                        "tail_number": {
                            "type": "string",
                            "description": "Associated aircraft tail number (e.g., 'PR-GOL'). Must be provided with aircraft_id if aircraft association is needed.",
                        },
                        "airport_id": {
                            "type": "string",
                            "description": "Associated airport ID (e.g., 'ARP_ATL'). Must be provided with iata_code if airport association is needed.",
                        },
                        "iata_code": {
                            "type": "string",
                            "description": "Associated airport IATA code (e.g., 'ATL'). Must be provided with airport_id if airport association is needed.",
                        },
                    },
                    "required": ["event_type", "event_timestamp_utc", "details"],
                },
            },
        }


class GetOperationalEventsByFlight(Tool):
    """API tool for retrieving all operational events related to a specific flight."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_id: str | None = None,
        flight_number: str | None = None,
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not flight_id and not flight_number:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either flight_id or flight_number must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve operational events
        operational_events = data.get("operational_events", {}).values()
        flight_events = []

        #Apply filters to events based on flight
        for event in operational_events.values():
            flight_info = event.get("flight", {}).values()
            event_flight_id = flight_info.get("flight_id")
            event_flight_number = flight_info.get("flight_number")

            #Verify if this event aligns with the search criteria
            match_found = False
            if flight_id and event_flight_id == flight_id:
                match_found = True
            elif flight_number and event_flight_number == flight_number:
                match_found = True
            elif (
                flight_id
                and flight_number
                and event_flight_id == flight_id
                and event_flight_number == flight_number
            ):
                match_found = True

            if match_found:
                flight_events.append(event)

        #Organize events by timestamp (latest first)
        flight_events.sort(key=lambda x: x.get("event_timestamp_utc", ""), reverse=True)

        #Retrieve flight details if events are located
        flight_info = None
        if flight_events and flight_events[0].get("flight"):
            flight_info = flight_events[0]["flight"]
        elif flight_id or flight_number:
            #Attempt to locate flight information from flight data
            flights = data.get("flights", {}).values()
            for flight in flights.values():
                if (flight_id and flight.get("flight_id") == flight_id) or (
                    flight_number and flight.get("flight_number") == flight_number
                ):
                    flight_info = {
                        "flight_id": flight.get("flight_id"),
                        "flight_number": flight.get("flight_number"),
                        "origin": flight.get("origin"),
                        "destination": flight.get("destination"),
                    }
                    break

        #Compute statistics for events
        total_events = len(flight_events)
        active_events = len([e for e in flight_events.values() if e.get("status") == "Active"])
        resolved_events = len(
            [e for e in flight_events.values() if e.get("status") == "Resolved"]
        )
        monitoring_events = len(
            [e for e in flight_events.values() if e.get("status") == "Monitoring"]
        )

        #Categorize events based on type
        events_by_type = {}
        for event in flight_events:
            event_type = event.get("event_type", "Unknown")
            if event_type not in events_by_type:
                events_by_type[event_type] = 0
            events_by_type[event_type] += 1

        #Locate the most recent active event
        most_recent_active = None
        for event in flight_events:
            if event.get("status") == "Active":
                most_recent_active = {
                    "event_id": event.get("event_id"),
                    "event_type": event.get("event_type"),
                    "event_timestamp_utc": event.get("event_timestamp_utc"),
                    "details": event.get("details"),
                }
                break

        #Formulate response
        response = {
            "flight": flight_info,
            "search_criteria": {"flight_id": flight_id, "flight_number": flight_number},
            "summary": {
                "total_events": total_events,
                "active_events": active_events,
                "resolved_events": resolved_events,
                "monitoring_events": monitoring_events,
                "events_by_type": events_by_type,
                "most_recent_active": most_recent_active,
            },
            "events": flight_events,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOperationalEventsByFlight",
                "description": "Get all operational events for a specific flight. Returns comprehensive event history with statistics and filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_id": {
                            "type": "string",
                            "description": "Flight ID to search for (e.g., 'FL001'). Either this or flight_number must be provided.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number to search for (e.g., 'HAT004'). Either this or flight_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateOperationalEventStatus(Tool):
    """API tool for revising the status and details of operational events."""

    @staticmethod
    def invoke(
        data: dict[str, Any], event_id: str, status: str, details: str | None = None
    ) -> str:
        pass
        #Check that necessary parameters are valid
        if not event_id or not status:
            payload = {
                    "error": "Missing required parameters",
                    "required": ["event_id", "status"],
                }
            out = json.dumps(
                payload)
            return out

        #Check the status for validity
        valid_statuses = ["Active", "Resolved", "Monitoring"]
        if status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status,
                }
            out = json.dumps(
                payload)
            return out

        #Locate the operational event
        operational_events = data.get("operational_events", {}).values()
        target_event = None
        event_index = None

        for i, event in enumerate(operational_events.values():
            if event.get("event_id") == event_id:
                target_event = event
                event_index = i
                break

        if not target_event:
            payload = {"error": "Operational event not found", "event_id": event_id}
            out = json.dumps(
                payload)
            return out

        #Retain original values for the response
        original_status = target_event.get("status")
        target_event.get("details")
        updates_made = []

        #Revise the status
        target_event["status"] = status
        updates_made.append("status")

        #Revise details if supplied
        if details is not None:
            target_event["details"] = details
            updates_made.append("details")

        #Revise the event within the database
        data["operational_events"][event_index] = target_event

        #Retrieve information about associated entities for a more detailed response
        flight_info = target_event.get("flight")
        aircraft_info = target_event.get("aircraft")
        airport_info = target_event.get("airport")

        #Formulate response
        response = {
            "success": True,
            "message": "Operational event updated successfully",
            "event_id": event_id,
            "status_change": {"from": original_status, "to": status},
            "updates_made": updates_made,
            "updated_event": target_event,
        }

        #Include association details if accessible
        if flight_info:
            response["flight"] = flight_info
        if aircraft_info:
            response["aircraft"] = aircraft_info
        if airport_info:
            response["airport"] = airport_info
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateOperationalEventStatus",
                "description": "Update operational event status and details. Allows changing event status between Active, Resolved, and Monitoring states with optional detail updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {
                            "type": "string",
                            "description": "Unique operational event identifier (e.g., 'OE001', 'OE025')",
                        },
                        "status": {
                            "type": "string",
                            "description": "Updated event status: 'Active', 'Resolved', or 'Monitoring'",
                        },
                        "details": {
                            "type": "string",
                            "description": "Updated event details or description (optional)",
                        },
                    },
                    "required": ["event_id", "status"],
                },
            },
        }


class CheckCertificationValidity(Tool):
    """API tool for verifying the validity of a certification for a crew member."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_certification_id: str | None = None,
        crew_member_id: str | None = None,
        certification_id: str | None = None,
        check_date: str | None = None,
    ) -> str:
        pass
        from datetime import date, datetime

        #Check the validity of input parameters
        if crew_certification_id:
            #Approach 1: Direct lookup of certification ID
            search_method = "certification_id"
            search_criteria = {"crew_certification_id": crew_certification_id}
        elif crew_member_id and certification_id:
            #Approach 2: Lookup of crew member and certification
            search_method = "crew_and_cert"
            search_criteria = {
                "crew_member_id": crew_member_id,
                "certification_id": certification_id,
            }
        else:
            payload = {
                    "error": "Invalid parameters",
                    "required": "Either 'crew_certification_id' OR both 'crew_member_id' and 'certification_id' must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Analyze the check date (defaulting to today)
        if check_date:
            try:
                check_date_obj = datetime.strptime(check_date, "%Y-%m-%d").date()
            except ValueError:
                payload = {
                        "error": "Invalid check_date format. Expected YYYY-MM-DD",
                        "received": check_date,
                    }
                out = json.dumps(
                    payload)
                return out
        else:
            check_date_obj = date.today()
            check_date = check_date_obj.strftime("%Y-%m-%d")

        #Locate the certification record
        crew_certifications = data.get("crew_certifications", {}).values()
        target_certification = None

        for cert in crew_certifications.values():
            if search_method == "certification_id":
                if cert.get("crew_certification_id") == crew_certification_id:
                    target_certification = cert
                    break
            elif search_method == "crew_and_cert":
                crew_info = cert.get("crew_member", {}).values()
                cert_info = cert.get("certification", {}).values()
                if (
                    crew_info.get("crew_member_id") == crew_member_id
                    and cert_info.get("certification_id") == certification_id
                ):
                    target_certification = cert
                    break

        if not target_certification:
            payload = {
                    "error": "Certification record not found",
                    "search_criteria": search_criteria,
                }
            out = json.dumps(
                payload)
            return out

        #Obtain details of the certification
        issue_date_str = target_certification.get("issue_date")
        expiry_date_str = target_certification.get("expiry_date")
        crew_info = target_certification.get("crew_member", {}).values()
        cert_info = target_certification.get("certification", {}).values()

        #Analyze dates
        try:
            issue_date = (
                datetime.strptime(issue_date_str, "%Y-%m-%d").date()
                if issue_date_str
                else None
            )
        except ValueError:
            issue_date = None

        try:
            expiry_date = (
                datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
                if expiry_date_str
                else None
            )
        except ValueError:
            expiry_date = None

        #Assess the validity status
        is_valid = True
        status = "Valid"
        reasons = []

        #Verify if issued prior to the check date
        if issue_date and check_date_obj < issue_date:
            is_valid = False
            status = "Not Yet Valid"
            reasons.append(f"Certification not issued until {issue_date}")

        #Verify if expired
        if expiry_date and check_date_obj > expiry_date:
            is_valid = False
            status = "Expired"
            reasons.append(f"Certification expired on {expiry_date}")

        #Compute the number of days until or since expiry
        days_info = None
        if expiry_date:
            days_diff = (expiry_date - check_date_obj).days
            if days_diff > 0:
                days_info = f"Expires in {days_diff} days"
            elif days_diff == 0:
                days_info = "Expires today"
            else:
                days_info = f"Expired {abs(days_diff)} days ago"
        else:
            days_info = "No expiry date (permanent certification)"

        #Retrieve complete certification details
        certifications = data.get("certifications", {}).values()
        certification_details = None
        for cert_detail in certifications.values():
            if cert_detail.get("certification_id") == cert_info.get("certification_id"):
                certification_details = cert_detail
                break

        #Formulate response
        response = {
            "certification_record": {
                "crew_certification_id": target_certification.get(
                    "crew_certification_id"
                ),
                "crew_member": crew_info,
                "certification": cert_info,
                "issue_date": issue_date_str,
                "expiry_date": expiry_date_str,
            },
            "validity_check": {
                "check_date": check_date,
                "is_valid": is_valid,
                "status": status,
                "reasons": reasons if reasons else ["Certification is valid"],
                "days_info": days_info,
            },
        }

        #Include complete certification details if located
        if certification_details:
            response["certification_details"] = certification_details
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckCertificationValidity",
                "description": "Check if a crew member's certification is valid on a specific date. Can search by certification ID directly or by crew member and certification combination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_certification_id": {
                            "type": "string",
                            "description": "Direct certification record ID (e.g., 'CC001'). Use this for direct lookup.",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001'). Must be used with certification_id.",
                        },
                        "certification_id": {
                            "type": "string",
                            "description": "Certification ID (e.g., 'CERT_ATPL'). Must be used with crew_member_id.",
                        },
                        "check_date": {
                            "type": "string",
                            "description": "Date to check validity against in YYYY-MM-DD format. Defaults to current date if not provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class SearchFlightsByRoute(Tool):
    """API tool for locating flights between airports with specified date ranges and filtering options."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        origin: str,
        destination: str,
        start_date: str,
        end_date: str | None = None,
        status_filter: list[str] | None = None,
    ) -> str:
        pass
        from datetime import datetime, timedelta

        #Check that necessary parameters are valid
        if not all([origin, destination, start_date]):
            payload = {
                    "error": "Missing required parameters",
                    "required": ["origin", "destination", "start_date"],
                }
            out = json.dumps(
                payload)
            return out

        #Analyze the start date
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            payload = {
                    "error": "Invalid start_date format. Expected YYYY-MM-DD",
                    "received": start_date,
                }
            out = json.dumps(
                payload)
            return out

        #Analyze the end date (defaulting to start_date if not supplied)
        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                payload = {
                        "error": "Invalid end_date format. Expected YYYY-MM-DD",
                        "received": end_date,
                    }
                out = json.dumps(
                    payload)
                return out
            if end_date_obj < start_date_obj:
                payload = {
                        "error": "end_date cannot be before start_date",
                        "start_date": start_date,
                        "end_date": end_date,
                    }
                out = json.dumps(
                    payload)
                return out
        else:
            end_date_obj = start_date_obj
            end_date = start_date

        #Check the status filter for validity
        valid_statuses = [
            "available",
            "delayed",
            "landed",
            "cancelled",
            "departed",
            "boarding",
            "in_air",
        ]
        if status_filter:
            for status in status_filter:
                if status not in valid_statuses:
                    payload = {
                            "error": "Invalid status in status_filter",
                            "valid_statuses": valid_statuses,
                            "received": status,
                        }
                    out = json.dumps(
                        payload)
                    return out

        #Create a range of dates
        date_range = []
        current_date = start_date_obj
        while current_date <= end_date_obj:
            date_range.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

        #Look for flights
        flights = data.get("flights", {}).values()
        matching_flights = []

        for flight in flights.values():
            #Verify if the route matches
            if (
                flight.get("origin") == origin
                and flight.get("destination") == destination
            ):

                #Verify each date within the range
                flight_dates = flight.get("dates", {}).values()
                for check_date in date_range:
                    if check_date in flight_dates:
                        date_info = flight_dates[check_date]
                        flight_status = date_info.get("status")

                        #Implement the status filter
                        if status_filter and flight_status not in status_filter:
                            continue

                        #Construct the flight result
                        flight_result = {
                            "flight_number": flight.get("flight_number"),
                            "origin": flight.get("origin"),
                            "destination": flight.get("destination"),
                            "scheduled_departure_time_est": flight.get(
                                "scheduled_departure_time_est"
                            ),
                            "scheduled_arrival_time_est": flight.get(
                                "scheduled_arrival_time_est"
                            ),
                            "date": check_date,
                            "status": flight_status,
                        }

                        #Include information specific to the status
                        if flight_status == "available":
                            if "available_seats" in date_info:
                                flight_result["available_seats"] = date_info[
                                    "available_seats"
                                ]
                            if "prices" in date_info:
                                flight_result["prices"] = date_info["prices"]
                        elif flight_status == "delayed":
                            if "estimated_departure_time_est" in date_info:
                                flight_result["estimated_departure_time_est"] = (
                                    date_info["estimated_departure_time_est"]
                                )
                            if "estimated_arrival_time_est" in date_info:
                                flight_result["estimated_arrival_time_est"] = date_info[
                                    "estimated_arrival_time_est"
                                ]
                        elif flight_status == "landed":
                            if "actual_departure_time_est" in date_info:
                                flight_result["actual_departure_time_est"] = date_info[
                                    "actual_departure_time_est"
                                ]
                            if "actual_arrival_time_est" in date_info:
                                flight_result["actual_arrival_time_est"] = date_info[
                                    "actual_arrival_time_est"
                                ]

                        matching_data["flights"][flight_id] = flight_result

        #Organize flights by date, followed by departure time
        matching_flights.sort(
            key=lambda x: (x["date"], x["scheduled_departure_time_est"])
        )

        #Compute summary statistics
        total_flights = len(matching_flights)
        status_counts = {}
        for flight in matching_flights:
            status = flight["status"]
            status_counts[status] = status_counts.get(status, 0) + 1

        #Categorize flights by date
        flights_by_date = {}
        for flight in matching_flights:
            date = flight["date"]
            if date not in flights_by_date:
                flights_by_date[date] = []
            flights_by_date[date].append(flight)

        #Locate available flights with the best prices (if any)
        available_flights = [
            f for f in matching_flights if f["status"] == "available" and "prices" in f
        ]
        best_prices = None
        if available_flights:
            all_prices = []
            for flight in available_flights:
                prices = flight.get("prices", {}).values()
                for cabin_class, price in prices.items():
                    all_prices.append(
                        {
                            "cabin_class": cabin_class,
                            "price": price,
                            "flight": flight["flight_number"],
                            "date": flight["date"],
                        }
                    )

            if all_prices:
                all_prices.sort(key=lambda x: x["price"])
                best_prices = {"lowest_overall": all_prices[0], "by_cabin_class": {}}

                #Identify the best price according to cabin class
                cabin_classes = {p["cabin_class"] for p in all_prices}
                for cabin_class in cabin_classes:
                    cabin_prices = [
                        p for p in all_prices if p["cabin_class"] == cabin_class
                    ]
                    best_prices["by_cabin_class"][cabin_class] = cabin_prices[0]

        #Formulate response
        response = {
            "search_criteria": {
                "origin": origin,
                "destination": destination,
                "start_date": start_date,
                "end_date": end_date,
                "status_filter": status_filter,
                "date_range": date_range,
            },
            "summary": {
                "total_flights_found": total_flights,
                "dates_searched": len(date_range),
                "status_breakdown": status_counts,
            },
            "flights": matching_flights,
            "flights_by_date": flights_by_date,
        }

        #Include pricing details if accessible
        if best_prices:
            response["pricing_analysis"] = best_prices
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchFlightsByRoute",
                "description": "Find flights between airports with date ranges and filtering options. Returns comprehensive flight information with pricing analysis and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "Origin airport IATA code (e.g., 'ATL', 'DFW')",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination airport IATA code (e.g., 'LAX', 'PHX')",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date for search in YYYY-MM-DD format",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for search in YYYY-MM-DD format. Defaults to start_date if not provided.",
                        },
                        "status_filter": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional filter by flight status: 'available', 'delayed', 'landed', 'cancelled', 'departed', 'boarding', 'in_air'",
                        },
                    },
                    "required": ["origin", "destination", "start_date"],
                },
            },
        }


class GetAirportOperationalStatus(Tool):
    """API tool for retrieving airport status and runway information along with operational details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        iata_code: str | None = None,
        airport_id: str | None = None,
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not iata_code and not airport_id:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either iata_code or airport_id must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Locate the airport
        airports = data.get("airports", {}).values()
        target_airport = None

        for airport in airports.values():
            if (iata_code and airport.get("iata_code") == iata_code) or (
                airport_id and airport.get("airport_id") == airport_id
            ):
                target_airport = airport
                break

        if not target_airport:
            search_criteria = (
                {"iata_code": iata_code} if iata_code else {"airport_id": airport_id}
            )
            payload = {"error": "Airport not found", "search_criteria": search_criteria}
            out = json.dumps(
                payload)
            return out

        #Obtain information about the airport
        airport_info = {
            "airport_id": target_airport.get("airport_id"),
            "iata_code": target_airport.get("iata_code"),
            "icao_code": target_airport.get("icao_code"),
            "airport_name": target_airport.get("airport_name"),
            "location": target_airport.get("location", {}),
            "timezone": target_airport.get("timezone"),
            "operational_status": target_airport.get("operational_status"),
        }

        #Handle information regarding runways
        runways = target_airport.get("runways", [])
        runway_analysis = {
            "total_runways": len(runways),
            "runway_details": runways,
            "surface_types": {},
            "longest_runway": None,
            "shortest_runway": None,
        }

        #Examine the runways
        if runways:
            #Tally the types of surfaces
            for runway in runways:
                surface = runway.get("surface_type", "Unknown")
                runway_analysis["surface_types"][surface] = (
                    runway_analysis["surface_types"].get(surface, 0) + 1
                )

            #Identify the longest and shortest runways
            runway_lengths = [(r.get("length_meters", 0), r) for r in runways]
            runway_lengths.sort(key=lambda x: x[0])

            if runway_lengths:
                runway_analysis["shortest_runway"] = {
                    "designator": runway_lengths[0][1].get("designator"),
                    "length_meters": runway_lengths[0][0],
                    "surface_type": runway_lengths[0][1].get("surface_type"),
                }
                runway_analysis["longest_runway"] = {
                    "designator": runway_lengths[-1][1].get("designator"),
                    "length_meters": runway_lengths[-1][0],
                    "surface_type": runway_lengths[-1][1].get("surface_type"),
                }

        #Locate current flights at this airport
        flights = data.get("flights", {}).values()
        current_flights = {"departures": [], "arrivals": []}

        for flight in flights.values():
            flight_origin = flight.get("origin")
            flight_dest = flight.get("destination")

            #Verify if this airport is associated with any flights
            if flight_origin == target_airport.get("iata_code"):
                #This represents a departure
                current_flights["departures"].append(
                    {
                        "flight_number": flight.get("flight_number"),
                        "destination": flight_dest,
                        "scheduled_departure_time_est": flight.get(
                            "scheduled_departure_time_est"
                        ),
                    }
                )
            elif flight_dest == target_airport.get("iata_code"):
                #This signifies an arrival
                current_flights["arrivals"].append(
                    {
                        "flight_number": flight.get("flight_number"),
                        "origin": flight_origin,
                        "scheduled_arrival_time_est": flight.get(
                            "scheduled_arrival_time_est"
                        ),
                    }
                )

        #Locate aircraft that are currently at this airport
        aircraft_data = data.get("aircraft", {}).values()
        aircraft_at_airport = []

        for aircraft in aircraft_data.values():
            location = aircraft.get("location", {}).values()
            if location.get("airport_id") == target_airport.get(
                "airport_id"
            ) or location.get("iata_code") == target_airport.get("iata_code"):
                aircraft_at_airport.append(
                    {
                        "aircraft_id": aircraft.get("aircraft_id"),
                        "tail_number": aircraft.get("tail_number"),
                        "model": aircraft.get("model", {}).values()),
                        "status": aircraft.get("status"),
                    }
                )

        #Verify for operational events occurring at this airport
        operational_events = data.get("operational_events", {}).values()
        airport_events = []

        for event in operational_events.values():
            event_airport = event.get("airport", {}).values()
            if event_airport.get("airport_id") == target_airport.get(
                "airport_id"
            ) or event_airport.get("iata_code") == target_airport.get("iata_code"):
                airport_events.append(
                    {
                        "event_id": event.get("event_id"),
                        "event_type": event.get("event_type"),
                        "status": event.get("status"),
                        "event_timestamp_utc": event.get("event_timestamp_utc"),
                        "details": event.get("details"),
                    }
                )

        #Organize events by timestamp (latest first)
        airport_events.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Compute statistics related to operations
        operational_stats = {
            "total_departures": len(current_flights["departures"]),
            "total_arrivals": len(current_flights["arrivals"]),
            "aircraft_on_ground": len(aircraft_at_airport),
            "active_events": len(
                [e for e in airport_events.values() if e.get("status") == "Active"]
            ),
            "recent_events": len(airport_events),
        }

        #Assess the overall health of operations
        operational_health = "Normal"
        health_factors = []

        if target_airport.get("operational_status") != "Operational":
            operational_health = "Limited"
            health_factors.append(
                f"Airport status: {target_airport.get('operational_status')}"
            )

        active_events = [e for e in airport_events.values() if e.get("status") == "Active"]
        if active_events:
            operational_health = "Impacted"
            health_factors.append(f"{len(active_events)} active operational events")

        if not health_factors:
            health_factors.append("No operational issues detected")

        #Formulate response
        response = {
            "airport": airport_info,
            "runway_information": runway_analysis,
            "current_operations": {
                "flights": current_flights,
                "aircraft_on_ground": aircraft_at_airport,
                "statistics": operational_stats,
            },
            "operational_events": {
                "recent_events": airport_events[:10],  #Latest 10 events
                "total_events": len(airport_events),
            },
            "operational_health": {
                "status": operational_health,
                "factors": health_factors,
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAirportOperationalStatus",
                "description": "Get comprehensive airport status and runway information with operational details including current flights, aircraft, and events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "Airport IATA code (e.g., 'ATL', 'DFW'). Either this or airport_id must be provided.",
                        },
                        "airport_id": {
                            "type": "string",
                            "description": "Airport ID (e.g., 'ARP_ATL'). Either this or iata_code must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetFleetUtilization(Tool):
    """API tool for obtaining the status of the aircraft fleet and metrics on utilization."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        model_filter: str | None = None,
        status_filter: list[str] | None = None,
    ) -> str:
        pass
        #Retrieve data about the aircraft
        aircraft_data = data.get("aircraft", {}).values()

        if not aircraft_data:
            payload = {"error": "No aircraft data available"}
            out = json.dumps(payload)
            return out

        #Check the status filter for validity
        valid_statuses = ["Active", "Grounded", "Maintenance"]
        if status_filter:
            for status in status_filter:
                if status not in valid_statuses:
                    payload = {
                            "error": "Invalid status in status_filter",
                            "valid_statuses": valid_statuses,
                            "received": status,
                        }
                    out = json.dumps(
                        payload)
                    return out

        #Apply filters to aircraft
        filtered_aircraft = []
        for aircraft in aircraft_data.values():
            #Implement the model filter
            if model_filter:
                model_info = aircraft.get("model", {}).values()
                if (
                    model_info.get("model_id") != model_filter
                    and model_info.get("model_name") != model_filter
                ):
                    continue

            #Implement the status filter
            if status_filter and aircraft.get("status") not in status_filter:
                continue

            filtered_aircraft.append(aircraft)

        #Compute statistics for the fleet
        total_aircraft = len(filtered_aircraft)
        status_breakdown = {}
        model_breakdown = {}
        location_breakdown = {}
        age_analysis = {"aircraft_ages": []}

        for aircraft in filtered_aircraft:
            #Analysis of status
            status = aircraft.get("status", "Unknown")
            status_breakdown[status] = status_breakdown.get(status, 0) + 1

            #Analysis of model
            model_info = aircraft.get("model", {}).values()
            model_name = model_info.get("model_name", "Unknown")
            if model_name not in model_breakdown:
                model_breakdown[model_name] = {
                    "count": 0,
                    "model_id": model_info.get("model_id"),
                    "aircraft": [],
                }
            model_breakdown[model_name]["count"] += 1
            model_breakdown[model_name]["aircraft"].append(
                {
                    "aircraft_id": aircraft.get("aircraft_id"),
                    "tail_number": aircraft.get("tail_number"),
                    "status": aircraft.get("status"),
                }
            )

            #Analysis of location
            location = aircraft.get("location", {}).values()
            location_key = location.get("iata_code", "Unknown")
            location_breakdown[location_key] = (
                location_breakdown.get(location_key, 0) + 1
            )

            #Calculation of age
            manufacture_date_str = aircraft.get("manufacture_date")
            if manufacture_date_str:
                try:
                    from datetime import date, datetime

                    manufacture_date = datetime.strptime(
                        manufacture_date_str, "%Y-%m-%d"
                    ).date()
                    today = date.today()
                    age_years = (today - manufacture_date).days / 365.25
                    age_analysis["aircraft_ages"].append(
                        {
                            "aircraft_id": aircraft.get("aircraft_id"),
                            "tail_number": aircraft.get("tail_number"),
                            "age_years": round(age_years, 1),
                            "manufacture_date": manufacture_date_str,
                        }
                    )
                except ValueError:
                    pass

        #Compute statistics related to age
        if age_analysis["aircraft_ages"]:
            ages = [a["age_years"] for a in age_analysis["aircraft_ages"]]
            age_analysis["statistics"] = {
                "average_age": round(sum(ages) / len(ages), 1),
                "oldest_aircraft": max(ages),
                "newest_aircraft": min(ages),
                "total_with_age_data": len(ages),
            }
        else:
            age_analysis["statistics"] = {
                "average_age": None,
                "oldest_aircraft": None,
                "newest_aircraft": None,
                "total_with_age_data": 0,
            }

        #Locate maintenance and operational events associated with the aircraft
        maintenance_logs = data.get("maintenance_logs", {}).values()
        operational_events = data.get("operational_events", {}).values()

        #Latest maintenance activities
        aircraft_ids = [a.get("aircraft_id") for a in filtered_aircraft]
        recent_maintenance = []

        for log in maintenance_logs.values():
            aircraft_info = log.get("aircraft", {}).values()
            if aircraft_info.get("aircraft_id") in aircraft_ids:
                recent_maintenance.append(
                    {
                        "log_id": log.get("log_id"),
                        "aircraft_id": aircraft_info.get("aircraft_id"),
                        "tail_number": aircraft_info.get("tail_number"),
                        "maintenance_type": log.get("maintenance_type"),
                        "status": log.get("status"),
                        "event_timestamp_utc": log.get("event_timestamp_utc"),
                    }
                )

        #Organize by timestamp (latest first)
        recent_maintenance.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Latest operational events concerning the aircraft
        recent_aircraft_events = []

        for event in operational_events.values():
            aircraft_info = event.get("aircraft", {}).values()
            if aircraft_info.get("aircraft_id") in aircraft_ids:
                recent_aircraft_events.append(
                    {
                        "event_id": event.get("event_id"),
                        "aircraft_id": aircraft_info.get("aircraft_id"),
                        "tail_number": aircraft_info.get("tail_number"),
                        "event_type": event.get("event_type"),
                        "status": event.get("status"),
                        "event_timestamp_utc": event.get("event_timestamp_utc"),
                    }
                )

        #Organize by timestamp (latest first)
        recent_aircraft_events.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Compute percentages of utilization
        utilization_metrics = {
            "active_percentage": (
                round((status_breakdown.get("Active", 0) / total_aircraft * 100), 1)
                if total_aircraft > 0
                else 0
            ),
            "grounded_percentage": (
                round((status_breakdown.get("Grounded", 0) / total_aircraft * 100), 1)
                if total_aircraft > 0
                else 0
            ),
            "maintenance_percentage": (
                round(
                    (status_breakdown.get("Maintenance", 0) / total_aircraft * 100), 1
                )
                if total_aircraft > 0
                else 0
            ),
        }

        #Identify aircraft with problems (maintenance status or recent occurrences)
        aircraft_with_issues = []

        for aircraft in filtered_aircraft:
            issues = []
            aircraft_id = aircraft.get("aircraft_id")

            #Verify if under maintenance
            if aircraft.get("status") == "Maintenance":
                issues.append("Currently in maintenance")

            #Verify for recent operational occurrences
            aircraft_events = [
                e
                for e in recent_aircraft_events
                if e.get("aircraft_id") == aircraft_id and e.get("status") == "Active"
            ]
            if aircraft_events:
                issues.append(f"{len(aircraft_events)} active operational events")

            if issues:
                aircraft_with_issues.append(
                    {
                        "aircraft_id": aircraft_id,
                        "tail_number": aircraft.get("tail_number"),
                        "model": aircraft.get("model", {}).values()),
                        "status": aircraft.get("status"),
                        "issues": issues,
                    }
                )

        #Formulate response
        response = {
            "search_criteria": {
                "model_filter": model_filter,
                "status_filter": status_filter,
            },
            "fleet_summary": {
                "total_aircraft": total_aircraft,
                "status_breakdown": status_breakdown,
                "utilization_metrics": utilization_metrics,
            },
            "model_analysis": model_breakdown,
            "location_distribution": location_breakdown,
            "age_analysis": age_analysis,
            "recent_activity": {
                "maintenance_logs": recent_maintenance[:10],  #Latest 10
                "operational_events": recent_aircraft_events[:10],  #Latest 10
            },
            "fleet_health": {
                "aircraft_with_issues": aircraft_with_issues,
                "total_with_issues": len(aircraft_with_issues),
            },
            "aircraft_details": filtered_aircraft,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFleetUtilization",
                "description": "Get comprehensive aircraft fleet status and utilization metrics including age analysis, location distribution, and operational health.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_filter": {
                            "type": "string",
                            "description": "Filter by aircraft model ID or model name (e.g., 'B737-800', '737-800'). Optional.",
                        },
                        "status_filter": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by aircraft status: 'Active', 'Grounded', 'Maintenance'. Optional.",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetFlightStatusByNumberAndDate(Tool):
    """API tool for retrieving the current status and details of a specific flight on a designated date."""

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        pass
        flights = data.get("flights", {}).values()
        for flight in flights.values():
            if flight.get("flight_number") == flight_number:
                date_info = flight.get("dates", {}).values().get(date)
                if not date_info:
                    payload = {
                            "error": "Flight not found for the given number and date",
                            "flight_number": flight_number,
                            "date": date,
                        }
                    out = json.dumps(
                        payload)
                    return out

                #Provide flight status and pertinent information
                flight_status = {
                    "flight_number": flight_number,
                    "date": date,
                    "status": date_info.get("status", "unknown"),
                    "origin": flight.get("origin"),
                    "destination": flight.get("destination"),
                    "aircraft_id": flight.get("aircraft_id"),
                    "scheduled_departure": flight.get("scheduled_departure_time_est"),
                    "scheduled_arrival": flight.get("scheduled_arrival_time_est"),
                    "estimated_departure": date_info.get(
                        "estimated_departure_time_est"
                    ),
                    "estimated_arrival": date_info.get("estimated_arrival_time_est"),
                    "actual_departure": date_info.get("actual_departure_time_est"),
                    "actual_arrival": date_info.get("actual_arrival_time_est"),
                    "reason_event_id": date_info.get("reason_event_id"),
                    "available_seats": date_info.get("available_seats"),
                    "prices": date_info.get("prices"),
                }
                payload = flight_status
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Flight number not found", "flight_number": flight_number}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightStatusByNumberAndDate",
                "description": "Get the current status and details of a specific flight on a given date from 'flights.json'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number (e.g., 'HAT001').",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format (e.g., '2024-05-01').",
                        },
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }


TOOLS = [
    GetAirportDetailsByIATACode(),
    GetAircraftDetails(),
    GetFlightsByCriteria(),
    UpdateFlightStatusByNumberAndDate(),
    GetCertificationDetails(),
    UpdateAircraftStatus(),
    GetCrewMemberDetails(),
    AssignCrewToFlight(),
    GetFlightCrewAssignments(),
    GetCrewCertifications(),
    UpdateCrewFlightLog(),
    CreateReservation(),
    GetReservationDetails(),
    GetUserReservations(),
    UpdateReservation(),
    GetAircraftMaintenanceHistory(),
    CreateMaintenanceEntry(),
    UpdateMaintenanceStatus(),
    GetUserProfile(),
    CreateOperationalEvent(),
    GetOperationalEventsByFlight(),
    UpdateOperationalEventStatus(),
    CheckCertificationValidity(),
    SearchFlightsByRoute(),
    GetAirportOperationalStatus(),
    GetFleetUtilization(),
    GetFlightStatusByNumberAndDate(),
]
