# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAvailableCrew(Tool):
    """
    A tool to find available crew members based on role, home base, and status.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], role: str, home_base_iata: str, status: str) -> str:
        crew_members = list(data.get("crew_members", {}).values())
        results = [
            m for m in crew_members
            if m["role"] == role
            and m["home_base"]["iata_code"] == home_base_iata
            and m["status"] == status
        ]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_available_crew",
                "description": "Finds available crew members matching specified criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {
                            "type": "string",
                            "description": "The role of the crew member (e.g., 'Captain', 'First Officer')."
                        },
                        "home_base_iata": {
                            "type": "string",
                            "description": "The IATA code of the crew member's home base."
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the crew member (e.g., 'Active')."
                        }
                    },
                    "required": ["role", "home_base_iata", "status"]
                }
            }
        }
