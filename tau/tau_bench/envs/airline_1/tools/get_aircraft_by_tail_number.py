# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAircraftByTailNumber(Tool):
    """
    A tool to retrieve aircraft details using its tail number.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], tail_number: str) -> str:
        aircraft_list = list(data.get("aircraft", {}).values())
        for aircraft in aircraft_list:
            if aircraft.get("tail_number") == tail_number:
                return json.dumps(aircraft)
        return json.dumps({"error": "Aircraft not found", "tail_number": tail_number})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_aircraft_by_tail_number",
                "description": "Retrieves the full details of an aircraft using its unique tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tail_number": {
                            "type": "string",
                            "description": "The unique tail number of the aircraft (e.g., 'G-ZNKH')."
                        }
                    },
                    "required": ["tail_number"]
                }
            }
        }
