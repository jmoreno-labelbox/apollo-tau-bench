# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewContactInfo(Tool):
    """
    API tool to get crew member contact information and emergency contacts.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str = None) -> str:
        if not crew_id:
            return json.dumps({
                "status": "missing_parameter",
                "message": "The crew_id parameter is required to retrieve crew contact information.",
                "required": "crew_id"
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
                "message": f"No crew member found with ID '{crew_id}'. Please check the crew ID and try again.",
                "crew_id": crew_id
            })

        contact_info = {
            "crew_id": crew_id,
            "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "primary_contact": {
                "email": target_crew.get("email", ""),
                "phone": target_crew.get("phone", "")
            },
            "emergency_contact": {
                "name": target_crew.get("emergency_contact_name", ""),
                "relationship": target_crew.get("emergency_contact_relationship", ""),
                "phone": target_crew.get("emergency_contact_phone", "")
            }
        }

        return json.dumps({
            "status": "success",
            "contact_info": contact_info
        })

    def get_info(self):
        return {
            "type": "function",
            "function": {
                "name": "get_crew_contact_info",
                "description": "Get crew member contact information including emergency contacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew member ID."}
                    },
                    "required": ["crew_id"]
                }
            }
        }
