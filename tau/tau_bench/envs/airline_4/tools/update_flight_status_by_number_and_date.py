from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateFlightStatusByNumberAndDate(Tool):
    """API tool for updating the status and optionally modifying the estimated departure and arrival times of a specific flight on a designated date."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        date: str,
        new_status: str,
        new_departure_time_est: str | None = None,
        new_arrival_time_est: str | None = None,
        delay_hours: int | None = None,
        reason_event_id: str | None = None,
    ) -> str:
        pass
        flights = data.get("flights", {}).values()
        for flight in flights.values():
            if flight.get("flight_number") == flight_number:
                date_info = flight.get("dates", {}).values().get(date)
                if not date_info:
                    payload = {
                            "error": "Flight not found for the given number and date",
                            "flight_number": flight_number,
                            "date": date,
                        }
                    out = json.dumps(
                        payload)
                    return out

                date_info["status"] = new_status

                #Identify property names according to the status
                if new_status == "delayed":
                    dep_prop = "estimated_departure_time_est"
                    arr_prop = "estimated_arrival_time_est"
                else:  #landed, cancelled, or various other statuses
                    dep_prop = "actual_departure_time_est"
                    arr_prop = "actual_arrival_time_est"

                #Implement delay if indicated
                if delay_hours is not None:
                    try:
                        #Retrieve current time or default to scheduled time
                        existing_dep = (
                            date_info.get(dep_prop)
                            or date_info.get("actual_departure_time_est")
                            or f"{date}T{flight.get('scheduled_departure_time_est')}"
                        )
                        existing_arr = (
                            date_info.get(arr_prop)
                            or date_info.get("actual_arrival_time_est")
                            or f"{date}T{flight.get('scheduled_arrival_time_est')}"
                        )

                        dep_dt = datetime.fromisoformat(existing_dep)
                        arr_dt = datetime.fromisoformat(existing_arr)

                        delay_delta = timedelta(hours=delay_hours)
                        date_info[dep_prop] = (dep_dt + delay_delta).isoformat()
                        date_info[arr_prop] = (arr_dt + delay_delta).isoformat()
                    except Exception as e:
                        payload = {"error": f"Invalid datetime format: {str(e)}"}
                        out = json.dumps(
                            payload)
                        return out

                #Replace departure/arrival time if indicated
                if new_departure_time_est:
                    date_info[dep_prop] = f"{date}T{new_departure_time_est}"
                if new_arrival_time_est:
                    date_info[arr_prop] = f"{date}T{new_arrival_time_est}"

                #Remove properties that are not applicable for this status
                if new_status == "delayed":
                    #Eliminate actual times if present
                    date_info.pop("actual_departure_time_est", None)
                    date_info.pop("actual_arrival_time_est", None)
                    #Delete booking information
                    date_info.pop("available_seats", None)
                    date_info.pop("prices", None)
                elif new_status == "landed":
                    #Discard estimated times if available
                    date_info.pop("estimated_departure_time_est", None)
                    date_info.pop("estimated_arrival_time_est", None)
                    #Eliminate booking information
                    date_info.pop("available_seats", None)
                    date_info.pop("prices", None)
                elif new_status == "cancelled":
                    #Delete all time and booking details for cancelled flights
                    date_info.pop("actual_departure_time_est", None)
                    date_info.pop("actual_arrival_time_est", None)
                    date_info.pop("estimated_departure_time_est", None)
                    date_info.pop("estimated_arrival_time_est", None)
                    date_info.pop("available_seats", None)
                    date_info.pop("prices", None)

                if reason_event_id:
                    date_info["reason_event_id"] = reason_event_id
                payload = {flight_number: {date: date_info}}
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
                "name": "UpdateFlightStatusByNumberAndDate",
                "description": "Update the status and optionally times of a flight instance on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number to update.",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date of the flight in YYYY-MM-DD format.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New flight status (e.g., 'delayed', 'cancelled').",
                        },
                        "new_departure_time_est": {
                            "type": "string",
                            "description": "Optional new departure time in HH:MM:SS. Uses 'estimated_*' for delayed status, 'actual_*' for others.",
                        },
                        "new_arrival_time_est": {
                            "type": "string",
                            "description": "Optional new arrival time in HH:MM:SS. Uses 'estimated_*' for delayed status, 'actual_*' for others.",
                        },
                        "delay_hours": {
                            "type": "integer",
                            "description": "Optional delay in hours to apply to departure and arrival times (uses appropriate property names for status).",
                        },
                        "reason_event_id": {
                            "type": "string",
                            "description": "Optional event ID that caused this status update.",
                        },
                    },
                    "required": ["flight_number", "date", "new_status"],
                },
            },
        }
