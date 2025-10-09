from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAirportByCode(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], iata_code: str) -> str:
        airports = data.get("airports", {}).values()
        for airport in airports.values():
            if airport.get("iata_code") == iata_code:
                payload = airport
                out = json.dumps(payload)
                return out
        payload = {"error": "Airport not found", "iata_code": iata_code}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAirportByCode",
                "description": "Retrieves the full details of an airport using its 3-letter IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "The 3-letter IATA code of the airport (e.g., 'JFK').",
                        }
                    },
                    "required": ["iata_code"],
                },
            },
        }
