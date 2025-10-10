# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFlightCrew(Tool):
    """
    A tool to find all crew members assigned to a specific flight number.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str) -> str:
        assignments = data.get("flight_crew_assignments", [])
        crew_results = [
            a.get("crew_member") for a in assignments
            if a.get("flight", {}).get("flight_number") == flight_number
        ]
        return json.dumps(list({v['crew_member_id']:v for v in crew_results}.values()))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_flight_crew",
                "description": "Finds all crew members assigned to a flight, identified by its flight number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number to search for (e.g., 'HAT004')."
                        }
                    },
                    "required": ["flight_number"]
                }
            }
        }
