from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAirportDetailsByIATACode(Tool):
    """API tool for retrieving complete airport details from 'airports.json' using the airport's 3-letter IATA code."""

    @staticmethod
    def invoke(data: dict[str, Any], iata_code: str) -> str:
        pass
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
                "name": "GetAirportDetailsByIataCode",
                "description": "Get full airport details using the 3-letter IATA code from 'airports.json'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "3-letter IATA airport code (e.g., 'LAX').",
                        }
                    },
                    "required": ["iata_code"],
                },
            },
        }
