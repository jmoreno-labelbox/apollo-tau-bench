from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
