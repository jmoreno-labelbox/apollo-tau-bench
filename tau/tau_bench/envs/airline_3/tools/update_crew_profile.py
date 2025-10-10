# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCrewProfile(Tool):
    """
    API tool to update crew member profile information.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        crew_id: str = None,
        first_name: str = None,
        last_name: str = None,
        role: str = None,
        home_base: str = None,
        status: str = None
    ) -> str:
        
        # Validate required parameter
        if not crew_id:
            return json.dumps({
                "status": "Missing required parameter",
                "required": "crew_id"
            })

        # Find crew member
        crew_members = data.get("crew_members", [])
        target_crew = None
        crew_index = None

        for i, crew in enumerate(crew_members):
            if crew.get("crew_member_id") == crew_id:
                target_crew = crew
                crew_index = i
                break

        if not target_crew:
            return json.dumps({
                "status": "Crew member not found",
                "crew_id": crew_id
            })

        # Store original values for response
        original_profile = {
            "first_name": target_crew.get("first_name"),
            "last_name": target_crew.get("last_name"),
            "role": target_crew.get("role"),
            "home_base": target_crew.get("home_base", {}).get("iata_code"),
            "status": target_crew.get("status")
        }

        updates_made = []

        # Update first name if provided
        if first_name is not None:
            if not isinstance(first_name, str) or len(first_name.strip()) == 0:
                return json.dumps({
                    "status": "first_name must be a non-empty string",
                    "received": first_name
                })
            data["crew_members"][crew_index]["first_name"] = first_name.strip()
            updates_made.append("first_name")

        # Update last name if provided
        if last_name is not None:
            if not isinstance(last_name, str) or len(last_name.strip()) == 0:
                return json.dumps({
                    "status": "last_name must be a non-empty string",
                    "received": last_name
                })
            data["crew_members"][crew_index]["last_name"] = last_name.strip()
            updates_made.append("last_name")

        # Update role if provided
        if role is not None:
            valid_roles = ["Captain", "First Officer", "Flight Attendant", "Flight Engineer"]
            if role not in valid_roles:
                return json.dumps({
                    "status": "Invalid role",
                    "valid_roles": valid_roles,
                    "received": role
                })
            data["crew_members"][crew_index]["role"] = role
            updates_made.append("role")

        # Update home base if provided
        if home_base is not None:
            # Validate airport code format (basic validation)
            if not isinstance(home_base, str) or len(home_base) != 3 or not home_base.isalpha():
                return json.dumps({
                    "status": "Invalid airport code format. Expected 3-letter IATA code",
                    "received": home_base
                })
            
            data["crew_members"][crew_index]["home_base"] = {
                "airport_id": f"ARP_{home_base.upper()}",
                "iata_code": home_base.upper()
            }
            updates_made.append("home_base")

        # Update status if provided
        if status is not None:
            valid_statuses = ["Active", "Inactive", "On Leave", "Suspended", "Retired"]
            if status not in valid_statuses:
                return json.dumps({
                    "status": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status
                })
            data["crew_members"][crew_index]["status"] = status
            updates_made.append("status")

        if not updates_made:
            return json.dumps({
                "message": "No updates provided",
                "crew_id": crew_id,
                "current_profile": original_profile
            })

        # Get updated profile
        updated_crew = data["crew_members"][crew_index]
        updated_profile = {
            "first_name": updated_crew.get("first_name"),
            "last_name": updated_crew.get("last_name"),
            "role": updated_crew.get("role"),
            "home_base": updated_crew.get("home_base", {}).get("iata_code"),
            "status": updated_crew.get("status")
        }

        response = {
            "success": True,
            "message": "Crew profile updated successfully",
            "crew_id": crew_id,
            "updates_made": updates_made,
            "profile_changes": {
                "before": original_profile,
                "after": updated_profile
            }
        }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crew_profile",
                "description": "Update crew member profile information including name, role, home base, and status. Essential for maintaining accurate crew records, scheduling, and regulatory compliance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "Crew member identifier. Format: CM followed by 3-digit number."
                        },
                        "first_name": {
                            "type": "string",
                            "description": "New first name for the crew member"
                        },
                        "last_name": {
                            "type": "string",
                            "description": "New last name for the crew member"
                        },
                        "role": {
                            "type": "string",
                            "description": "New role: 'Captain', 'First Officer', 'Flight Attendant', 'Flight Engineer'. Each role has specific certification and experience requirements."
                        },
                        "home_base": {
                            "type": "string",
                            "description": "New home base airport IATA code"
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: 'Active', 'Inactive', 'On Leave', 'Suspended', 'Retired'. Status changes affect crew availability and scheduling."
                        }
                    },
                    "required": ["crew_id"]
                }
            }
        }
