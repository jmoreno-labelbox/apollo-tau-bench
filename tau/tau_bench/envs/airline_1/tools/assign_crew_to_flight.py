from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

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
