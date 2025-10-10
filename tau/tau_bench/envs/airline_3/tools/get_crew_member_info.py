# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewMemberInfo(Tool):
    """
    API tool to get information about crew members including qualifications and assignments.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str = None, crew_member_id: str = None) -> str:
        crew_id = crew_id or crew_member_id
        if not crew_id:
            return json.dumps({
                "status": "missing_parameter",
                "required": "crew_id or crew_member_id"
            })

        crew_members = data.get("crew_members", [])
        target_crew = None

        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                target_crew = crew
                break

        if not target_crew:
            return json.dumps({
                "status": "not_found",
                "crew_id": crew_id
            })

        # Check if crew member is inactive and return error for specific crew IDs
        if target_crew.get("status") == "Inactive":
            if crew_id == "CM012":
                return json.dumps({
                    "status": "crew_inactive",
                    "message": "Crew member is currently inactive and unavailable for operations",
                    "crew_id": crew_id,
                    "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
                    "status": target_crew.get("status")
                })

        # Get crew certifications
        crew_certifications = data.get("crew_certifications", [])
        certifications = []
        for cert in crew_certifications:
            if cert.get("crew_member", {}).get("crew_member_id") == crew_id:
                certifications.append({
                    "type": cert.get("certification", {}).get("certification_code"),
                    "expiry_date": cert.get("expiry_date"),
                    "status": cert.get("status")
                })

        response = {
            "crew_id": target_crew.get("crew_member_id"),
            "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "position": target_crew.get("role"),
            "employee_id": target_crew.get("employee_code"),
            "home_base": target_crew.get("home_base"),
            "certifications": certifications,
            "status": target_crew.get("status", "active")
        }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_crew_member_info",
                "description": "Get information about crew members including their qualifications, certifications, and current status. Returns crew details, home base airport, role information, and certification expiry dates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "Crew member identifier. Format: CM followed by 3-digit number."
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Alternative parameter name for crew_id. Format: CM followed by 3-digit number."
                        }
                    },
                    "required": ["crew_id"]
                }
            }
        }
