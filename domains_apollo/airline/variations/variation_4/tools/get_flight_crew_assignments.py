from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

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

        flight_crew_assignments = data.get("flight_crew_assignments", [])
        flights = data.get("flights", [])

        #Confirm flight existence if flight_number is given
        if flight_number:
            flight_exists = False
            for flight in flights:
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
        for assignment in flight_crew_assignments:
            flight_info = assignment.get("flight", {})

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
            matching_assignments[0].get("flight", {}) if matching_assignments else {}
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
