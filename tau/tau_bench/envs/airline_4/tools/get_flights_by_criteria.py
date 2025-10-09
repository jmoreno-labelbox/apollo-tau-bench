from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetFlightsByCriteria(Tool):
    """API tool for fetching flights based on departure date, status, origin, and destination, reflecting the JSON format where each flight contains a 'dates' dictionary indexed by date strings."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        departure_date: str,
        status: list[str],
        origin: str | None = None,
        destination: str | None = None,
    ) -> str:
        pass
        flights = data.get("flights", [])
        matched_flights = []

        for flight in flights:
            #Apply filters based on origin and destination if available
            if origin and flight.get("origin") != origin:
                continue
            if destination and flight.get("destination") != destination:
                continue

            #Verify if the flight contains information for the specified departure date
            date_info = flight.get("dates", {}).get(departure_date)
            if not date_info:
                continue

            #Determine if the flight's status on that date aligns with any in the given status list
            if date_info.get("status") not in status:
                continue

            #Build the flight information to be returned
            flight_info = {
                "flight_number": flight.get("flight_number"),
                "origin": flight.get("origin"),
                "destination": flight.get("destination"),
                "scheduled_departure_time_est": flight.get(
                    "scheduled_departure_time_est"
                ),
                "scheduled_arrival_time_est": flight.get("scheduled_arrival_time_est"),
                "date": departure_date,
                "status": date_info.get("status"),
            }

            #Include fields specific to the status only if they are present
            status = date_info.get("status")

            if status == "available":
                if "available_seats" in date_info:
                    flight_info["available_seats"] = date_info["available_seats"]
                if "prices" in date_info:
                    flight_info["prices"] = date_info["prices"]

            elif status == "landed":
                if "actual_departure_time_est" in date_info:
                    flight_info["actual_departure_time_est"] = date_info[
                        "actual_departure_time_est"
                    ]
                if "actual_arrival_time_est" in date_info:
                    flight_info["actual_arrival_time_est"] = date_info[
                        "actual_arrival_time_est"
                    ]

            elif status == "delayed":
                if "estimated_departure_time_est" in date_info:
                    flight_info["estimated_departure_time_est"] = date_info[
                        "estimated_departure_time_est"
                    ]
                if "estimated_arrival_time_est" in date_info:
                    flight_info["estimated_arrival_time_est"] = date_info[
                        "estimated_arrival_time_est"
                    ]

            elif status == "cancelled":
                if "reason_event_id" in date_info:
                    flight_info["reason_event_id"] = date_info["reason_event_id"]

            #Incorporate any other status or properties that fall outside standard patterns
            for key in [
                "actual_departure_time_est",
                "actual_arrival_time_est",
                "estimated_departure_time_est",
                "estimated_arrival_time_est",
                "available_seats",
                "prices",
                "reason_event_id",
            ]:
                if key in date_info and key not in flight_info:
                    flight_info[key] = date_info[key]

            matched_flights.append(flight_info)
        payload = matched_flights
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightsByCriteria",
                "description": "Retrieve flights based on departure date, flight status, and optional origin and destination filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "departure_date": {
                            "type": "string",
                            "description": "Flight date in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of acceptable flight statuses (e.g., ['available', 'landed']).",
                        },
                        "origin": {
                            "type": "string",
                            "description": "Optional IATA code of the flight origin.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Optional IATA code of the flight destination.",
                        },
                    },
                    "required": ["departure_date", "status"],
                },
            },
        }
