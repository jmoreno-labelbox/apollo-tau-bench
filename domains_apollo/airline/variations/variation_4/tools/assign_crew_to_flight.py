from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

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
        crew_members = data.get("crew_members", [])
        flights = data.get("flights", [])
        flight_crew_assignments = data.get("flight_crew_assignments", [])

        #Confirm the existence of the crew member
        target_crew_member = None
        for crew_member in crew_members:
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
        for flight in flights:
            if flight.get("flight_number") == flight_number:
                flight_exists = True
                break

        if not flight_exists:
            payload = {"error": "Flight not found", "flight_number": flight_number}
            out = json.dumps(
                payload)
            return out

        #Verify if the crew member is already allocated to this flight
        for assignment in flight_crew_assignments:
            if (
                assignment.get("flight", {}).get("flight_id") == flight_id
                and assignment.get("crew_member", {}).get("crew_member_id")
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
            for assignment in flight_crew_assignments:
                if (
                    assignment.get("flight", {}).get("flight_id") == flight_id
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
            for assignment in flight_crew_assignments
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
        flight_crew_assignments.append(new_assignment)
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
