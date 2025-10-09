from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateCrewMemberHomeBase(Tool):
    """
    A straightforward tool for updating a crew member's home base.
    """

    @staticmethod
    def invoke(data: dict[str, Any], crew_id: str, new_home_base: str) -> str:
        crew_members = data.get("crew_members", [])
        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                old_home_base = crew.get("home_base", {}).get("iata_code", "Unknown")
                crew["home_base"]["iata_code"] = new_home_base
                payload = {
                    "status": "success",
                    "crew_id": crew_id,
                    "old_home_base": old_home_base,
                    "new_home_base": new_home_base,
                }
                out = json.dumps(payload)
                return out
        payload = {"status": "Crew member not found", "crew_id": crew_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewMemberHomeBase",
                "description": "Update a crew member's home base airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "The crew member ID (e.g., CM001).",
                        },
                        "new_home_base": {
                            "type": "string",
                            "description": "New home base airport IATA code (e.g., LAX).",
                        },
                    },
                    "required": ["crew_id", "new_home_base"],
                },
            },
        }
