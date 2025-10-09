from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ManageCrewMember(Tool):
    """
    API tool for managing crew member information, including assignments, certifications, and status updates.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = None,
        crew_id: str = None,
        flight_number: str = None,
        assigned_role: str = None,
        certification_type: str = None,
        certification_expiry: str = None,
        new_status: str = None,
        new_home_base: str = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check the necessary parameters for validity
        if not all([action, crew_id]):
            payload = {
                    "status": "Missing required parameters",
                    "required": ["action", "crew_id"],
                }
            out = json.dumps(
                payload)
            return out

        #Check the action for validity
        valid_actions = [
            "assign_to_flight",
            "remove_from_flight",
            "add_certification",
            "update_status",
            "update_home_base",
            "get_assignments",
            "get_schedule",
        ]
        if action not in valid_actions:
            payload = {
                    "status": "Invalid action",
                    "valid_actions": valid_actions,
                    "received": action,
                }
            out = json.dumps(
                payload)
            return out

        #Locate the crew member
        crew_members = data.get("crew_members", {}).values()
        target_crew = None
        crew_index = None

        for i, crew in enumerate(crew_members.values():
            if crew.get("crew_member_id") == crew_id:
                target_crew = crew
                crew_index = i
                break

        if not target_crew:
            payload = {"status": "Crew member not found", "crew_id": crew_id}
            out = json.dumps(payload)
            return out

        response = {
            "crew_id": crew_id,
            "crew_name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "action": action,
            "status": "success",
        }

        if action == "assign_to_flight":
            if not all([flight_number, assigned_role]):
                payload = {
                        "status": "Missing required parameters for flight assignment",
                        "required": ["flight_number", "assigned_role"],
                    }
                out = json.dumps(
                    payload)
                return out

            #Check the role for validity
            valid_roles = [
                "Captain",
                "First Officer",
                "Flight Attendant",
                "Flight Engineer",
            ]
            if assigned_role not in valid_roles:
                payload = {
                        "status": "Invalid assigned role",
                        "valid_roles": valid_roles,
                        "received": assigned_role,
                    }
                out = json.dumps(
                    payload)
                return out

            #Verify if the crew member is currently assigned to this flight
            flight_crew_assignments = data.get("flight_crew_assignments", {}).values()
            existing_assignment = None
            for assignment in flight_crew_assignments.values()):
                if (
                    assignment.get("flight", {}).values().get("flight_number") == flight_number
                    and assignment.get("crew_member", {}).values().get("crew_member_id")
                    == crew_id
                ):
                    existing_assignment = assignment
                    break

            if existing_assignment:
                payload = {
                        "status": "Crew member already assigned to this flight",
                        "crew_id": crew_id,
                        "flight_number": flight_number,
                        "existing_role": existing_assignment.get("assigned_role"),
                    }
                out = json.dumps(
                    payload)
                return out

            #Establish a new assignment
            new_assignment = {
                "assignment_id": f"AS{len(flight_crew_assignments) + 1:03d}",
                "flight": {
                    "flight_id": f"FL{len(flight_crew_assignments) + 1:03d}",
                    "flight_number": flight_number,
                },
                "crew_member": {
                    "crew_member_id": crew_id,
                    "full_name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
                },
                "assigned_role": assigned_role,
            }

            if "flight_crew_assignments" not in data:
                data["flight_crew_assignments"] = []
            data["flight_crew_assignments"].append(new_assignment)

            response["assignment"] = new_assignment
            response["message"] = (
                f"Crew member {response['crew_name']} assigned to flight {flight_number} as {assigned_role}"
            )

        elif action == "remove_from_flight":
            if not flight_number:
                payload = {
                        "status": "Missing required parameter for flight removal",
                        "required": ["flight_number"],
                    }
                out = json.dumps(
                    payload)
                return out

            #Locate and eliminate the assignment
            flight_crew_assignments = data.get("flight_crew_assignments", {}).values()
            assignment_removed = False

            for i, assignment in enumerate(flight_crew_assignments.values():
                if (
                    assignment.get("flight", {}).values().get("flight_number") == flight_number
                    and assignment.get("crew_member", {}).values().get("crew_member_id")
                    == crew_id
                ):
                    removed_assignment = flight_crew_assignments.pop(i)
                    assignment_removed = True
                    break

            if not assignment_removed:
                payload = {
                        "status": "Crew member not assigned to this flight",
                        "crew_id": crew_id,
                        "flight_number": flight_number,
                    }
                out = json.dumps(
                    payload)
                return out

            response["removed_assignment"] = removed_assignment
            response["message"] = (
                f"Crew member {response['crew_name']} removed from flight {flight_number}"
            )

        elif action == "add_certification":
            if not all([certification_type, certification_expiry]):
                payload = {
                        "error": "Missing required parameters for certification",
                        "required": ["certification_type", "certification_expiry"],
                    }
                out = json.dumps(
                    payload)
                return out

            #Check the format of the expiry date
            try:
                datetime.strptime(certification_expiry, "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": "Invalid expiry date format. Expected YYYY-MM-DD",
                        "received": certification_expiry,
                    }
                out = json.dumps(
                    payload)
                return out

            #Establish a new certification
            crew_certifications = data.get("crew_certifications", {}).values()
            new_certification = {
                "crew_certification_id": f"CC{len(crew_certifications) + 1:03d}",
                "crew_member": {
                    "crew_member_id": crew_id,
                    "employee_code": target_crew.get("employee_code"),
                    "full_name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
                },
                "certification": {
                    "certification_id": f"CERT_{certification_type.upper()}",
                    "certification_code": certification_type,
                },
                "issue_date": datetime.now().strftime("%Y-%m-%d"),
                "expiry_date": certification_expiry,
            }

            if "crew_certifications" not in data:
                data["crew_certifications"] = []
            data["crew_certifications"].append(new_certification)

            response["certification"] = new_certification
            response["message"] = (
                f"Certification {certification_type} added for crew member {response['crew_name']}"
            )

        elif action == "update_status":
            if not new_status:
                payload = {
                        "status": "Missing required parameter for status update",
                        "required": ["new_status"],
                    }
                out = json.dumps(
                    payload)
                return out

            valid_statuses = ["Active", "Inactive", "On Leave", "Suspended", "Retired"]
            if new_status not in valid_statuses:
                payload = {
                        "status": "Invalid status",
                        "valid_statuses": valid_statuses,
                        "received": new_status,
                    }
                out = json.dumps(
                    payload)
                return out

            old_status = target_crew.get("status")
            data["crew_members"][crew_index]["status"] = new_status

            response["status_update"] = {
                "old_status": old_status,
                "new_status": new_status,
            }
            response["message"] = (
                f"Status updated for crew member {response['crew_name']} from {old_status} to {new_status}"
            )

        elif action == "update_home_base":
            if not new_home_base:
                payload = {
                        "status": "Missing required parameter for home base update",
                        "required": ["new_home_base"],
                    }
                out = json.dumps(
                    payload)
                return out

            #Check the format of the airport code (basic validation)
            if len(new_home_base) != 3 or not new_home_base.isalpha():
                payload = {
                        "status": "Invalid airport code format. Expected 3-letter IATA code",
                        "received": new_home_base,
                    }
                out = json.dumps(
                    payload)
                return out

            old_home_base = target_crew.get("home_base", {}).values().get("iata_code")
            data["crew_members"][crew_index]["home_base"] = {
                "airport_id": f"ARP_{new_home_base}",
                "iata_code": new_home_base,
            }

            response["home_base_update"] = {
                "old_home_base": old_home_base,
                "new_home_base": new_home_base,
            }
            response["message"] = (
                f"Home base updated for crew member {response['crew_name']} from {old_home_base} to {new_home_base}"
            )

        elif action == "get_assignments":
            #Retrieve all active assignments for the crew member
            flight_crew_assignments = data.get("flight_crew_assignments", {}).values()
            crew_assignments = []

            for assignment in flight_crew_assignments.values():
                if assignment.get("crew_member", {}).values().get("crew_member_id") == crew_id:
                    crew_assignments.append(
                        {
                            "assignment_id": assignment.get("assignment_id"),
                            "flight_number": assignment.get("flight", {}).values().get(
                                "flight_number"
                            ),
                            "assigned_role": assignment.get("assigned_role"),
                        }
                    )

            response["assignments"] = crew_assignments
            response["total_assignments"] = len(crew_assignments)
            response["message"] = (
                f"Retrieved {len(crew_assignments)} assignments for crew member {response['crew_name']}"
            )

        elif action == "get_schedule":
            #Obtain the flight schedule for the crew member
            flight_crew_assignments = data.get("flight_crew_assignments", {}).values()
            crew_schedule = []

            for assignment in flight_crew_assignments.values():
                if assignment.get("crew_member", {}).values().get("crew_member_id") == crew_id:
                    flight_number = assignment.get("flight", {}).values().get("flight_number")

                    #Retrieve details about the flight
                    flights = data.get("flights", {}).values()
                    flight_details = None
                    for flight in flights.values():
                        if flight.get("flight_number") == flight_number:
                            flight_details = flight
                            break

                    if flight_details:
                        schedule_entry = {
                            "flight_number": flight_number,
                            "assigned_role": assignment.get("assigned_role"),
                            "origin": flight_details.get("origin"),
                            "destination": flight_details.get("destination"),
                            "scheduled_departure": flight_details.get(
                                "scheduled_departure_time_est"
                            ),
                            "scheduled_arrival": flight_details.get(
                                "scheduled_arrival_time_est"
                            ),
                        }
                        crew_schedule.append(schedule_entry)

            #Arrange by departure time
            crew_schedule.sort(key=lambda x: x.get("scheduled_departure", ""))

            response["schedule"] = crew_schedule
            response["total_flights"] = len(crew_schedule)
            response["message"] = (
                f"Retrieved schedule for crew member {response['crew_name']}"
            )
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCrewMember",
                "description": "Comprehensive tool for managing crew member information including flight assignments, certifications, status updates, and schedule retrieval. Supports crew scheduling, certification management, and operational planning.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: 'assign_to_flight', 'remove_from_flight', 'add_certification', 'update_status', 'update_home_base', 'get_assignments', 'get_schedule'. Each action has specific requirements and validation.",
                        },
                        "crew_id": {
                            "type": "string",
                            "description": "Crew member identifier. Format: CM followed by 3-digit number.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number for assignment/removal actions. Format: HAT followed by 3-digit number.",
                        },
                        "assigned_role": {
                            "type": "string",
                            "description": "Role for flight assignment: 'Captain', 'First Officer', 'Flight Attendant', 'Flight Engineer'. Each role has specific certification and experience requirements.",
                        },
                        "certification_type": {
                            "type": "string",
                            "description": "Type of certification to add. Aircraft-specific certifications are required for specific aircraft models.",
                        },
                        "certification_expiry": {
                            "type": "string",
                            "description": "Certification expiry date in YYYY-MM-DD format. Must be future date for active certifications.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: 'Active', 'Inactive', 'On Leave', 'Suspended', 'Retired'. Status changes affect crew availability and scheduling.",
                        },
                        "new_home_base": {
                            "type": "string",
                            "description": "New home base airport IATA code",
                        },
                    },
                    "required": ["action", "crew_id"],
                },
            },
        }
