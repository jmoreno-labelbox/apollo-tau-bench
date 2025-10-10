# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewMemberSchedule(Tool):
    """
    A simple tool to get a crew member's flight schedule.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str) -> str:
        crew_members = data.get("crew_members", [])
        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                flight_log = crew.get("flight_log", [])
                return json.dumps({
                    "crew_id": crew_id,
                    "name": f"{crew.get('first_name')} {crew.get('last_name')}",
                    "schedule": flight_log
                })
        return json.dumps({"status": "Crew member not found", "crew_id": crew_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_crew_member_schedule",
                "description": "Get a crew member's flight schedule and history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew member ID (e.g., CM001)."}
                    },
                    "required": ["crew_id"]
                }
            }
        }
