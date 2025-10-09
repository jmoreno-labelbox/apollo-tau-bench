from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
