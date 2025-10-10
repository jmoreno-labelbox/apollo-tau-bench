# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCrewToFlight(Tool):
    """
    A tool to assign a crew member to a flight.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, flight_number: str, date: str, role: str) -> str:
        assignments = data.get("flight_crew_assignments", [])

        for assignment in assignments:
            if (assignment.get("crew_member_id") == crew_member_id and
                assignment.get("flight_number") == flight_number and
                assignment.get("date") == date):
                return json.dumps({"error": "Crew member already assigned to this flight."})

        new_assignment = {
            "assignment_id": f"AS_0{len(assignments) + 1}",
            "flight_number": flight_number,
            "date": date,
            "crew_member_id": crew_member_id,
            "role": role
        }
        assignments.append(new_assignment)

        return json.dumps(new_assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_crew_to_flight",
                "description": "Assigns a crew member to a specific flight with a designated role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format."},
                        "role": {"type": "string", "description": "Role of the crew member (e.g., 'Captain', 'First Officer')."}
                    },
                    "required": ["crew_member_id", "flight_number", "date", "role"]
                }
            }
        }
