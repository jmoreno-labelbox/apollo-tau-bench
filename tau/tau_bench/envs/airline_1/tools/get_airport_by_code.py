# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAirportByCode(Tool):
    """
    A tool to retrieve airport details using its IATA code.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], iata_code: str) -> str:
        airports = list(data.get("airports", {}).values())
        for airport in airports:
            if airport.get("iata_code") == iata_code:
                return json.dumps(airport)
        return json.dumps({"error": "Airport not found", "iata_code": iata_code})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_airport_by_code",
                "description": "Retrieves the full details of an airport using its 3-letter IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "The 3-letter IATA code of the airport (e.g., 'JFK')."
                        }
                    },
                    "required": ["iata_code"]
                }
            }
        }
