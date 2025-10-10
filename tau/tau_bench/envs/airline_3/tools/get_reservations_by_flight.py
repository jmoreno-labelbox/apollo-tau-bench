# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReservationsByFlight(Tool):
    """
    Simple API tool to get reservations by flight details with optional filtering.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str = None, date: str = None, origin: str = None, destination: str = None) -> str:
        if not flight_number:
            return json.dumps({
                "status": "missing_parameter",
                "message": "The flight_number parameter is required to retrieve reservations.",
                "required": "flight_number"
            })

        reservations = list(data.get("reservations", {}).values())
        flight_reservations = []

        for reservation in reservations:
            flights = reservation.get("flights", [])
            for flight in flights:
                if flight.get("flight_number") == flight_number:
                    # Apply optional filters
                    if date and flight.get("date") != date:
                        continue
                    if origin and flight.get("origin") != origin:
                        continue
                    if destination and flight.get("destination") != destination:
                        continue
                    
                    flight_reservations.append(reservation)
                    break

        if not flight_reservations:
            return json.dumps({
                "status": "not_found",
                "message": f"No reservations found for flight '{flight_number}' with the specified criteria.",
                "flight_number": flight_number,
                "filters": {
                    "date": date,
                    "origin": origin,
                    "destination": destination
                }
            })

        return json.dumps({
            "status": "success",
            "message": f"Found {len(flight_reservations)} reservation(s) for flight '{flight_number}'.",
            "flight_number": flight_number,
            "reservations": flight_reservations,
            "filters_applied": {
                "date": date,
                "origin": origin,
                "destination": destination
            }
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reservations_by_flight",
                "description": "Simple API tool to get reservations by flight details with optional filtering.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number to retrieve reservations for. Format: airline code followed by 3-digit number."
                        },
                        "date": {
                            "type": "string",
                            "description": "Optional filter for flight date (YYYY-MM-DD format)"
                        },
                        "origin": {
                            "type": "string",
                            "description": "Optional filter for departure airport code (3-letter IATA code)"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Optional filter for arrival airport code (3-letter IATA code)"
                        }
                    },
                    "required": ["flight_number"]
                }
            }
        }
