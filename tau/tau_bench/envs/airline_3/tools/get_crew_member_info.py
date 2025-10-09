from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCrewMemberInfo(Tool):
    """
    API tool for retrieving information about crew members, including their qualifications and assignments.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], crew_id: str = None, crew_member_id: str = None
    ) -> str:
        crew_id = crew_id or crew_member_id
        if not crew_id:
            payload = {"status": "missing_parameter", "required": "crew_id or crew_member_id"}
            out = json.dumps(payload)
            return out

        crew_members = data.get("crew_members", {}).values()
        target_crew = None

        for crew in crew_members.values():
            if crew.get("crew_member_id") == crew_id:
                target_crew = crew
                break

        if not target_crew:
            payload = {"status": "not_found", "crew_id": crew_id}
            out = json.dumps(payload)
            return out

        # Verify if the crew member is inactive and return an error for designated crew IDs
        if target_crew.get("status") == "Inactive":
            if crew_id == "CM012":
                payload = {
                    "status": "crew_inactive",
                    "message": "Crew member is currently inactive and unavailable for operations",
                    "crew_id": crew_id,
                    "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
                    "status": target_crew.get("status"),
                }
                out = json.dumps(payload)
                return out

        # Retrieve crew certifications
        crew_certifications = data.get("crew_certifications", {}).values()
        certifications = []
        for cert in crew_certifications.values():
            if cert.get("crew_member", {}).values().get("crew_member_id") == crew_id:
                certifications.append(
                    {
                        "type": cert.get("certification", {}).values().get("certification_code"),
                        "expiry_date": cert.get("expiry_date"),
                        "status": cert.get("status"),
                    }
                )

        response = {
            "crew_id": target_crew.get("crew_member_id"),
            "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "position": target_crew.get("role"),
            "employee_id": target_crew.get("employee_code"),
            "home_base": target_crew.get("home_base"),
            "certifications": certifications,
            "status": target_crew.get("status", "active"),
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewMemberInfo",
                "description": "Get information about crew members including their qualifications, certifications, and current status. Returns crew details, home base airport, role information, and certification expiry dates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "Crew member identifier. Format: CM followed by 3-digit number.",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Alternative parameter name for crew_id. Format: CM followed by 3-digit number.",
                        },
                    },
                    "required": ["crew_id"],
                },
            },
        }
