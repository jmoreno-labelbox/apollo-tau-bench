from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class SearchFlightsByRoute(Tool):
    """API tool for locating flights between airports with specified date ranges and filtering options."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        origin: str,
        destination: str,
        start_date: str,
        end_date: str | None = None,
        status_filter: list[str] | None = None,
    ) -> str:
        pass
        from datetime import datetime, timedelta

        #Check that necessary parameters are valid
        if not all([origin, destination, start_date]):
            payload = {
                    "error": "Missing required parameters",
                    "required": ["origin", "destination", "start_date"],
                }
            out = json.dumps(
                payload)
            return out

        #Analyze the start date
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            payload = {
                    "error": "Invalid start_date format. Expected YYYY-MM-DD",
                    "received": start_date,
                }
            out = json.dumps(
                payload)
            return out

        #Analyze the end date (defaulting to start_date if not supplied)
        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                payload = {
                        "error": "Invalid end_date format. Expected YYYY-MM-DD",
                        "received": end_date,
                    }
                out = json.dumps(
                    payload)
                return out
            if end_date_obj < start_date_obj:
                payload = {
                        "error": "end_date cannot be before start_date",
                        "start_date": start_date,
                        "end_date": end_date,
                    }
                out = json.dumps(
                    payload)
                return out
        else:
            end_date_obj = start_date_obj
            end_date = start_date

        #Check the status filter for validity
        valid_statuses = [
            "available",
            "delayed",
            "landed",
            "cancelled",
            "departed",
            "boarding",
            "in_air",
        ]
        if status_filter:
            for status in status_filter:
                if status not in valid_statuses:
                    payload = {
                            "error": "Invalid status in status_filter",
                            "valid_statuses": valid_statuses,
                            "received": status,
                        }
                    out = json.dumps(
                        payload)
                    return out

        #Create a range of dates
        date_range = []
        current_date = start_date_obj
        while current_date <= end_date_obj:
            date_range.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

        #Look for flights
        flights = data.get("flights", [])
        matching_flights = []

        for flight in flights:
            #Verify if the route matches
            if (
                flight.get("origin") == origin
                and flight.get("destination") == destination
            ):

                #Verify each date within the range
                flight_dates = flight.get("dates", {})
                for check_date in date_range:
                    if check_date in flight_dates:
                        date_info = flight_dates[check_date]
                        flight_status = date_info.get("status")

                        #Implement the status filter
                        if status_filter and flight_status not in status_filter:
                            continue

                        #Construct the flight result
                        flight_result = {
                            "flight_number": flight.get("flight_number"),
                            "origin": flight.get("origin"),
                            "destination": flight.get("destination"),
                            "scheduled_departure_time_est": flight.get(
                                "scheduled_departure_time_est"
                            ),
                            "scheduled_arrival_time_est": flight.get(
                                "scheduled_arrival_time_est"
                            ),
                            "date": check_date,
                            "status": flight_status,
                        }

                        #Include information specific to the status
                        if flight_status == "available":
                            if "available_seats" in date_info:
                                flight_result["available_seats"] = date_info[
                                    "available_seats"
                                ]
                            if "prices" in date_info:
                                flight_result["prices"] = date_info["prices"]
                        elif flight_status == "delayed":
                            if "estimated_departure_time_est" in date_info:
                                flight_result["estimated_departure_time_est"] = (
                                    date_info["estimated_departure_time_est"]
                                )
                            if "estimated_arrival_time_est" in date_info:
                                flight_result["estimated_arrival_time_est"] = date_info[
                                    "estimated_arrival_time_est"
                                ]
                        elif flight_status == "landed":
                            if "actual_departure_time_est" in date_info:
                                flight_result["actual_departure_time_est"] = date_info[
                                    "actual_departure_time_est"
                                ]
                            if "actual_arrival_time_est" in date_info:
                                flight_result["actual_arrival_time_est"] = date_info[
                                    "actual_arrival_time_est"
                                ]

                        matching_flights.append(flight_result)

        #Organize flights by date, followed by departure time
        matching_flights.sort(
            key=lambda x: (x["date"], x["scheduled_departure_time_est"])
        )

        #Compute summary statistics
        total_flights = len(matching_flights)
        status_counts = {}
        for flight in matching_flights:
            status = flight["status"]
            status_counts[status] = status_counts.get(status, 0) + 1

        #Categorize flights by date
        flights_by_date = {}
        for flight in matching_flights:
            date = flight["date"]
            if date not in flights_by_date:
                flights_by_date[date] = []
            flights_by_date[date].append(flight)

        #Locate available flights with the best prices (if any)
        available_flights = [
            f for f in matching_flights if f["status"] == "available" and "prices" in f
        ]
        best_prices = None
        if available_flights:
            all_prices = []
            for flight in available_flights:
                prices = flight.get("prices", {})
                for cabin_class, price in prices.items():
                    all_prices.append(
                        {
                            "cabin_class": cabin_class,
                            "price": price,
                            "flight": flight["flight_number"],
                            "date": flight["date"],
                        }
                    )

            if all_prices:
                all_prices.sort(key=lambda x: x["price"])
                best_prices = {"lowest_overall": all_prices[0], "by_cabin_class": {}}

                #Identify the best price according to cabin class
                cabin_classes = {p["cabin_class"] for p in all_prices}
                for cabin_class in cabin_classes:
                    cabin_prices = [
                        p for p in all_prices if p["cabin_class"] == cabin_class
                    ]
                    best_prices["by_cabin_class"][cabin_class] = cabin_prices[0]

        #Formulate response
        response = {
            "search_criteria": {
                "origin": origin,
                "destination": destination,
                "start_date": start_date,
                "end_date": end_date,
                "status_filter": status_filter,
                "date_range": date_range,
            },
            "summary": {
                "total_flights_found": total_flights,
                "dates_searched": len(date_range),
                "status_breakdown": status_counts,
            },
            "flights": matching_flights,
            "flights_by_date": flights_by_date,
        }

        #Include pricing details if accessible
        if best_prices:
            response["pricing_analysis"] = best_prices
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchFlightsByRoute",
                "description": "Find flights between airports with date ranges and filtering options. Returns comprehensive flight information with pricing analysis and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "Origin airport IATA code (e.g., 'ATL', 'DFW')",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination airport IATA code (e.g., 'LAX', 'PHX')",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date for search in YYYY-MM-DD format",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for search in YYYY-MM-DD format. Defaults to start_date if not provided.",
                        },
                        "status_filter": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional filter by flight status: 'available', 'delayed', 'landed', 'cancelled', 'departed', 'boarding', 'in_air'",
                        },
                    },
                    "required": ["origin", "destination", "start_date"],
                },
            },
        }
