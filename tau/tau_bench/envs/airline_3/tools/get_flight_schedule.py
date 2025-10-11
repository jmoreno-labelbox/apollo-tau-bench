# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFlightSchedule(Tool):
    """
    API tool to get the schedule of flights for a specific date range.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        start_date: str = None,
        end_date: str = None,
        origin: str = None,
        destination: str = None
    ) -> str:
        from datetime import datetime, timedelta
        from typing import Optional

        if not start_date:
            return json.dumps({
                "status": "missing_parameter",
                "required": "start_date"
            })

        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            return json.dumps({
                "status": "invalid_date",
                "message": "Invalid start_date format. Expected YYYY-MM-DD",
                "received": start_date
            })

        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return json.dumps({
                    "status": "invalid_date",
                    "message": "Invalid end_date format. Expected YYYY-MM-DD",
                    "received": end_date
                })
            if end_date_obj < start_date_obj:
                return json.dumps({
                    "status": "invalid_date_range",
                    "message": "end_date cannot be before start_date",
                    "start_date": start_date,
                    "end_date": end_date
                })
        else:
            end_date_obj = start_date_obj

        # Create a range of dates.
        date_range = []
        current_date = start_date_obj
        while current_date <= end_date_obj:
            date_range.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

        flights = list(data.get("flights", {}).values())
        scheduled_flights = []

        for flight in flights:
            # Implement origin/destination filters if they are specified.
            if origin and flight.get("origin") != origin:
                continue
            if destination and flight.get("destination") != destination:
                continue

            flight_dates = flight.get("dates", {})
            for date in date_range:
                if date in flight_dates:
                    date_info = flight_dates[date]
                    scheduled_flights.append({
                        "flight_number": flight.get("flight_number"),
                        "origin": flight.get("origin"),
                        "destination": flight.get("destination"),
                        "date": date,
                        "scheduled_departure": flight.get("scheduled_departure_time_est"),
                        "scheduled_arrival": flight.get("scheduled_arrival_time_est"),
                        "status": date_info.get("status", "unknown"),
                        "aircraft_id": flight.get("aircraft_id")
                    })

        # Order by date and departure time.
        scheduled_flights.sort(key=lambda x: (x["date"], x["scheduled_departure"]))

        response = {
            "schedule_period": {
                "start_date": start_date,
                "end_date": end_date or start_date
            },
            "filters_applied": {
                "origin": origin,
                "destination": destination
            },
            "total_flights": len(scheduled_flights),
            "flights": scheduled_flights
        }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_flight_schedule",
                "description": "Get the schedule of flights for a specific date range with optional origin/destination filtering. Returns flight details including aircraft assignments, crew schedules, and operational status for planning purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {
                            "type": "string",
                            "description": "Start date for schedule in YYYY-MM-DD format"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for schedule in YYYY-MM-DD format. Optional, defaults to start_date if not specified."
                        },
                        "origin": {
                            "type": "string",
                            "description": "Optional origin airport filter using IATA codes"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Optional destination airport filter using IATA codes"
                        }
                    },
                    "required": ["start_date"]
                }
            }
        }
