# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCrewMemberHomeBase(Tool):
    """
    A simple tool to update a crew member's home base.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str, new_home_base: str) -> str:
        crew_members = data.get("crew_members", [])
        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                old_home_base = crew.get("home_base", {}).get("iata_code", "Unknown")
                crew["home_base"]["iata_code"] = new_home_base
                return json.dumps({
                    "status": "success",
                    "crew_id": crew_id,
                    "old_home_base": old_home_base,
                    "new_home_base": new_home_base
                })
        return json.dumps({"status": "Crew member not found", "crew_id": crew_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crew_member_home_base",
                "description": "Update a crew member's home base airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew member ID (e.g., CM001)."},
                        "new_home_base": {"type": "string", "description": "New home base airport IATA code (e.g., LAX)."}
                    },
                    "required": ["crew_id", "new_home_base"]
                }
            }
        }
