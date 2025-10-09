from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetFlightStatusByNumberAndDate(Tool):
    """API tool for retrieving the current status and details of a specific flight on a designated date."""

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        pass
        flights = data.get("flights", [])
        for flight in flights:
            if flight.get("flight_number") == flight_number:
                date_info = flight.get("dates", {}).get(date)
                if not date_info:
                    payload = {
                            "error": "Flight not found for the given number and date",
                            "flight_number": flight_number,
                            "date": date,
                        }
                    out = json.dumps(
                        payload)
                    return out

                #Provide flight status and pertinent information
                flight_status = {
                    "flight_number": flight_number,
                    "date": date,
                    "status": date_info.get("status", "unknown"),
                    "origin": flight.get("origin"),
                    "destination": flight.get("destination"),
                    "aircraft_id": flight.get("aircraft_id"),
                    "scheduled_departure": flight.get("scheduled_departure_time_est"),
                    "scheduled_arrival": flight.get("scheduled_arrival_time_est"),
                    "estimated_departure": date_info.get(
                        "estimated_departure_time_est"
                    ),
                    "estimated_arrival": date_info.get("estimated_arrival_time_est"),
                    "actual_departure": date_info.get("actual_departure_time_est"),
                    "actual_arrival": date_info.get("actual_arrival_time_est"),
                    "reason_event_id": date_info.get("reason_event_id"),
                    "available_seats": date_info.get("available_seats"),
                    "prices": date_info.get("prices"),
                }
                payload = flight_status
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Flight number not found", "flight_number": flight_number}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightStatusByNumberAndDate",
                "description": "Get the current status and details of a specific flight on a given date from 'flights.json'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number (e.g., 'HAT001').",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format (e.g., '2024-05-01').",
                        },
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }
