# Copyright Sierra

import re
import json
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from tau_bench.envs.tool import Tool


class UpdateFlightSchedule(Tool):
    """
    A tool to update the schedule of one or more flight instances (on a specific date).
    """

    @staticmethod
    def parse_time_with_day_offset(time_str: str, base_date: str) -> datetime:
        match = re.match(r"(\d{2}:\d{2}:\d{2})(\+(\d+))?", time_str)
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")

        time_part = match.group(1)
        day_offset = int(match.group(3)) if match.group(3) else 0

        dt = datetime.fromisoformat(f"{base_date}T{time_part}") + timedelta(days=day_offset)
        return dt

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        flight_number: Union[str, List[str]],
        flight_date: str,
        new_departure_date: Optional[str] = None,
        new_arrival_date: Optional[str] = None,
        new_status: Optional[str] = None,
        new_departure_time_est: Optional[str] = None,
        new_arrival_time_est: Optional[str] = None,
        delay_hours: Optional[int] = None,
        delay_minutes: Optional[int] = None,
        new_gate: Optional[str] = None,
        reason_event_id: Optional[str] = None
    ) -> str:
        if isinstance(flight_number, str):
            flight_numbers = [flight_number]
        else:
            flight_numbers = flight_number

        flights_data = list(data.get("flights", {}).values())
        results = {}

        for fn in flight_numbers:
            updated = False
            for flight_route in flights_data:
                if flight_route.get("flight_number") == fn:
                    date_info = flight_route.get("dates", {}).get(flight_date)
                    if not date_info:
                        results[fn] = {"error": "Date not found", "date": flight_date}
                        updated = True
                        break
                    if new_status:
                        date_info["status"] = new_status

                    if new_gate:
                        date_info["gate"] = new_gate

                    if delay_hours is not None or delay_minutes is not None:
                        delay = timedelta(hours=delay_hours or 0, minutes=delay_minutes or 0)

                        dep_time_str = date_info.get("estimated_departure_time_est") or flight_route.get("scheduled_departure_time_est")
                        arr_time_str = date_info.get("estimated_arrival_time_est") or flight_route.get("scheduled_arrival_time_est")

                        try:
                            dep_dt = UpdateFlightSchedule.parse_time_with_day_offset(dep_time_str, flight_date)
                            arr_dt = UpdateFlightSchedule.parse_time_with_day_offset(arr_time_str, flight_date)

                            new_dep = dep_dt + delay
                            new_arr = arr_dt + delay

                            date_info["estimated_departure_time_est"] = new_dep.isoformat()
                            date_info["estimated_arrival_time_est"] = new_arr.isoformat()
                        except Exception as e:
                            results[fn] = {
                                "error": f"Error processing delayed time: {str(e)}",
                                "date": flight_date,
                                "input_dep": dep_time_str,
                                "input_arr": arr_time_str
                            }
                            updated = True
                            break

                    if new_departure_time_est:
                        date_info["estimated_departure_time_est"] = f"{new_departure_date}T{new_departure_time_est}"
                    if new_arrival_time_est:
                        date_info["estimated_arrival_time_est"] = f"{new_arrival_date}T{new_arrival_time_est}"

                    if reason_event_id:
                        date_info["reason_event_id"] = reason_event_id

                    results[fn] = {flight_date: date_info}
                    updated = True
                    break

            if not updated:
                results[fn] = {"error": "Flight not found for the given number", "date": flight_date}

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_flight_schedule",
                "description": "Updates the schedule and status of a specific flight on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string", "description": "The flight number to update."},
                        "flight_date": {"type": "string", "description": "The date of the flight to update in YYYY-MM-DD format."},
                        "new_departure_date": {"type": "string", "description": "Optional: The new departure of the flight in YYYY-MM-DD format."},
                        "new_arrival_date": {"type": "string", "description": "Optional: The new arrival of the flight in YYYY-MM-DD format."},
                        "new_status": {"type": "string", "description": "Optional: The new status for the flight (e.g., 'delayed', 'cancelled')."},
                        "new_departure_time_est": {"type": "string", "description": "Optional: The new departure time in HH:MM:SS format."},
                        "new_arrival_time_est": {"type": "string", "description": "Optional: The new arrival time in HH:MM:SS format."},
                        "delay_hours": {"type": "integer", "description": "Optional: Number of hours to delay the flight."},
                        "delay_minutes": {"type": "integer", "description": "Optional: Number of minutes to delay the flight."},
                        "new_gate": {"type": "string", "description": "Optional: The new gate for the flight."},
                        "reason_event_id": {
                            "type": "string",
                            "description": "Optional: The ID of the operational event causing this change (e.g., 'OE026')."
                        }
                    },
                    "required": ["flight_number", "flight_date"]
                }
            }
        }
