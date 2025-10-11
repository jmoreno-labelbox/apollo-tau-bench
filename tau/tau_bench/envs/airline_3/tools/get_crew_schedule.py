# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewSchedule(Tool):
    """
    API tool to get crew member schedule and assignment information.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str = None) -> str:
        if not crew_id:
            return json.dumps({
                "status": "missing_parameter",
                "message": "The crew_id parameter is required to retrieve crew schedule.",
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

        schedule_info = {
            "crew_id": crew_id,
            "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "role": target_crew.get("role", ""),
            "status": target_crew.get("status", ""),
            "home_base": target_crew.get("home_base", {}).get("iata_code", ""),
            "current_assignments": target_crew.get("current_assignments", []),
            "upcoming_flights": target_crew.get("upcoming_flights", []),
            "availability_status": target_crew.get("availability_status", "Available")
        }

        return json.dumps({
            "status": "success",
            "schedule_info": schedule_info
        })

    def get_info(self):
        return {
            "type": "function",
            "function": {
                "name": "get_crew_schedule",
                "description": "Get crew member schedule and assignment information including current assignments and upcoming flights.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew member ID."}
                    },
                    "required": ["crew_id"]
                }
            }
        }
