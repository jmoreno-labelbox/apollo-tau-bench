from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCrewAvailability(Tool):
    """
    API tool for retrieving crew member availability and workload details.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_id: str = None,
        role: str = None,
        home_base: str = None,
        status: str = None,
    ) -> str:
        from datetime import datetime
        import json

        crew_members = data.get("crew_members", [])
        flight_crew_assignments = data.get("flight_crew_assignments", [])
        filtered_crew = []

        for crew in crew_members:
            # Implement filters
            if crew_id and crew.get("crew_member_id") != crew_id:
                continue
            if role and crew.get("role") != role:
                continue
            if home_base and crew.get("home_base", {}).get("iata_code") != home_base:
                continue
            if status and crew.get("status") != status:
                continue

            # Retrieve active assignments
            current_assignments = []
            total_flight_hours = 0
            for assignment in flight_crew_assignments:
                if assignment.get("crew_member", {}).get("crew_member_id") == crew.get(
                    "crew_member_id"
                ):
                    current_assignments.append(
                        {
                            "flight_number": assignment.get("flight", {}).get(
                                "flight_number"
                            ),
                            "role": assignment.get("assigned_role"),
                        }
                    )

            # Determine workload using the flight log
            flight_log = crew.get("flight_log", [])
            recent_flights = []
            for flight in flight_log:
                try:
                    flight_date = datetime.strptime(
                        flight.get("date", ""), "%Y-%m-%d"
                    ).date()
                    days_ago = (datetime.now().date() - flight_date).days
                    if days_ago <= 30:  # Previous 30 days
                        recent_flights.append(flight)
                        total_flight_hours += flight.get("hours_flown", {}).get(
                            "total", 0
                        )
                except (ValueError, TypeError):
                    continue

            # Ascertain availability status
            if crew.get("status") != "Active":
                availability = "unavailable"
            elif len(current_assignments) >= 3:  # Exceeding 3 active assignments
                availability = "high_workload"
            elif total_flight_hours >= 80:  # Over 80 hours in the past 30 days
                availability = "high_workload"
            elif len(current_assignments) == 0:
                availability = "available"
            else:
                availability = "moderate_workload"

            crew_info = {
                "crew_id": crew.get("crew_member_id"),
                "name": f"{crew.get('first_name', '')} {crew.get('last_name', '')}".strip(),
                "role": crew.get("role"),
                "status": crew.get("status"),
                "home_base": crew.get("home_base", {}).get("iata_code"),
                "availability": availability,
                "current_assignments": len(current_assignments),
                "recent_flight_hours": round(total_flight_hours, 1),
                "recent_flights_count": len(recent_flights),
            }

            filtered_crew.append(crew_info)

        # Arrange by availability priority and name
        availability_priority = {
            "available": 1,
            "moderate_workload": 2,
            "high_workload": 3,
            "unavailable": 4,
        }
        filtered_crew.sort(
            key=lambda x: (availability_priority.get(x["availability"], 5), x["name"])
        )

        # Determine summary statistics
        total_crew = len(filtered_crew)
        availability_counts = {}
        role_counts = {}
        home_base_counts = {}

        for crew in filtered_crew:
            availability_counts[crew["availability"]] = (
                availability_counts.get(crew["availability"], 0) + 1
            )
            role_counts[crew["role"]] = role_counts.get(crew["role"], 0) + 1
            home_base_counts[crew["home_base"]] = (
                home_base_counts.get(crew["home_base"], 0) + 1
            )

        response = {
            "filters_applied": {
                "crew_id": crew_id,
                "role": role,
                "home_base": home_base,
                "status": status,
            },
            "summary": {
                "total_crew_found": total_crew,
                "availability_breakdown": availability_counts,
                "role_breakdown": role_counts,
                "home_base_breakdown": home_base_counts,
            },
            "crew_members": filtered_crew,
        }

        # Include quick suggestions if no particular filters are applied
        if not any([crew_id, role, home_base, status]) and total_crew > 0:
            available_crew = [
                c for c in filtered_crew if c["availability"] == "available"
            ]
            if available_crew:
                response["recommendations"] = {
                    "available_crew_count": len(available_crew),
                    "sample_available": available_crew[
                        :3
                    ],  # Top 3 available crew members
                }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewAvailability",
                "description": "Get crew member availability and workload information with filtering options. Provides quick overview of crew status, current assignments, and recent flight hours. Essential for crew scheduling and operational planning.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "Optional crew member identifier to get specific crew availability. Format: CM followed by 3-digit number.",
                        },
                        "role": {
                            "type": "string",
                            "description": "Optional role filter: 'Captain', 'First Officer', 'Flight Attendant', 'Flight Engineer'. Each role has different availability patterns and requirements.",
                        },
                        "home_base": {
                            "type": "string",
                            "description": "Optional home base airport filter using IATA codes",
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional status filter: 'Active', 'Inactive', 'On Leave', 'Suspended', 'Retired'. Only Active crew members are available for new assignments.",
                        },
                    },
                    "required": [],
                },
            },
        }
