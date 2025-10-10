# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFlights(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        origin: str,
        destination: str,
        start_date: str,
        end_date: Optional[str] = None,
        status: Optional[List[str]] = None
    ) -> str:
        # Check mandatory parameters.
        if not (origin and destination and start_date):
            return _j({
                "error": "Missing required parameters",
                "required": ["origin", "destination", "start_date"]
            })

        # Extract date information.
        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            return _j({
                "error": "Invalid start_date format. Expected YYYY-MM-DD",
                "received": start_date
            })

        if end_date is None or end_date == "":
            end_dt = start_dt
            end_date = start_date
        else:
            try:
                end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return _j({
                    "error": "Invalid end_date format. Expected YYYY-MM-DD",
                    "received": end_date
                })
            if end_dt < start_dt:
                return _j({
                    "error": "end_date cannot be before start_date",
                    "start_date": start_date,
                    "end_date": end_date
                })

        # Create an inclusive range of dates.
        date_range: List[str] = []
        d = start_dt
        while d <= end_dt:
            date_range.append(d.strftime("%Y-%m-%d"))
            d += timedelta(days=1)

        flights = list(data.get("flights", {}).values())
        matching_flights: List[Dict[str, Any]] = []

        # Route and date range search
        for f in flights:
            if f.get("origin") != origin or f.get("destination") != destination:
                continue

            per_day = f.get("dates", {})
            for day in date_range:
                if day not in per_day:
                    continue

                info = per_day[day]
                f_status = info.get("status")

                if status and f_status not in status:
                    continue

                result = {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "scheduled_departure_time_est": f.get("scheduled_departure_time_est"),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                    "date": day,
                    "status": f_status
                }

                if f_status == "available":
                    if "available_seats" in info:
                        result["available_seats"] = info["available_seats"]
                    if "prices" in info:
                        result["prices"] = info["prices"]
                elif f_status == "delayed":
                    if "estimated_departure_time_est" in info:
                        result["estimated_departure_time_est"] = info["estimated_departure_time_est"]
                    if "estimated_arrival_time_est" in info:
                        result["estimated_arrival_time_est"] = info["estimated_arrival_time_est"]
                elif f_status == "landed":
                    if "actual_departure_time_est" in info:
                        result["actual_departure_time_est"] = info["actual_departure_time_est"]
                    if "actual_arrival_time_est" in info:
                        result["actual_arrival_time_est"] = info["actual_arrival_time_est"]

                matching_flights.append(result)

        matching_flights.sort(key=lambda x: (x["date"], x["scheduled_departure_time_est"]))

        flights_by_date: Dict[str, List[Dict[str, Any]]] = {}
        for r in matching_flights:
            flights_by_date.setdefault(r["date"], []).append(r)

        best_prices = None
        avail_with_prices = [r for r in matching_flights if r.get("status") == "available" and "prices" in r]
        if avail_with_prices:
            all_prices = []
            for r in avail_with_prices:
                for cabin_class, price in OrderedDict(r.get("prices", {})).items():
                    all_prices.append({
                        "cabin_class": cabin_class,
                        "price": price,
                        "flight": r["flight_number"],
                        "date": r["date"]
                    })
            if all_prices:
                all_prices.sort(key=lambda p: p["price"])
                best_prices = {
                    "lowest_overall": all_prices[0],
                    "by_cabin_class": {}
                }
                # Minimum per cabin category
                seen = {}
                for p in all_prices:
                    cc = p["cabin_class"]
                    if cc not in seen:
                        seen[cc] = p
                best_prices["by_cabin_class"] = seen

        resp: Dict[str, Any] = {
            "flights": matching_flights,
            "flights_by_date": flights_by_date
        }
        if best_prices:
            resp["pricing_analysis"] = best_prices

        return _j(resp)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_flights",
                "description": "Find flights between airports with date ranges and filtering options. Returns comprehensive flight information with pricing analysis and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "Origin airport IATA code"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination airport IATA code"
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date for search in YYYY-MM-DD format"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for search in YYYY-MM-DD format."
                        },
                        "status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional filter by flight status: 'available', 'delayed', 'landed', 'cancelled', 'departed', 'boarding', 'in_air'"
                        }
                    },
                    "required": ["origin", "destination", "start_date"]
                }
            }
        }
