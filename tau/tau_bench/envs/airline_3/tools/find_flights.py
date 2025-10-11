# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFlights(Tool):
    """
    API tool to search for available flights with various filtering options.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        origin: str = None,
        destination: str = None,
        date: str = None,
        cabin_class: str = None,
        max_price: float = None
    ) -> str:
        from datetime import datetime

        # Check mandatory parameters.
        if not all([origin, destination, date]):
            return json.dumps({
                "status": "missing_parameters",
                "message": "Missing required parameters",
                "required": ["origin", "destination", "date"]
            })

        # Check the format of the date.
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return json.dumps({
                "status": "invalid_date",
                "message": "Invalid date format. Expected YYYY-MM-DD",
                "received": date
            })

        # Check if the cabin class is specified and validate it.
        valid_cabins = ["basic_economy", "economy", "business", "first"]
        if cabin_class and cabin_class not in valid_cabins:
            return json.dumps({
                "status": "invalid_cabin",
                "valid_cabins": valid_cabins,
                "received": cabin_class
            })

        # Look for available flights.
        flights = list(data.get("flights", {}).values())
        matching_flights = []

        for flight in flights:
            # Verify route correspondence
            if (flight.get("origin") == origin and
                flight.get("destination") == destination):

                # Verify if the flight is scheduled for the given date.
                flight_dates = flight.get("dates", {})
                if date in flight_dates:
                    date_info = flight_dates[date]
                    
                    # Verify flight availability.
                    if date_info.get("status") == "available":
                        flight_result = {
                            "flight_number": flight.get("flight_number"),
                            "origin": flight.get("origin"),
                            "destination": flight.get("destination"),
                            "date": date,
                            "scheduled_departure": flight.get("scheduled_departure_time_est"),
                            "scheduled_arrival": flight.get("scheduled_arrival_time_est"),
                            "available_seats": date_info.get("available_seats", 0),
                            "prices": date_info.get("prices", {}),
                            "aircraft_id": flight.get("aircraft_id")
                        }

                        # Implement cabin class filtering.
                        if cabin_class:
                            if cabin_class in flight_result["prices"]:
                                flight_result["selected_cabin_price"] = flight_result["prices"][cabin_class]
                                matching_flights.append(flight_result)
                        else:
                            # Incorporate every accessible cabin class.
                            matching_flights.append(flight_result)

        # Implement price filter
        if max_price is not None:
            filtered_flights = []
            for flight in matching_flights:
                prices = flight.get("prices", {})
                sorted_prices = sorted([prices[key] for key in prices])
                if any(price <= max_price for price in sorted_prices):
                    filtered_flights.append(flight)
            matching_flights = filtered_flights

        # Arrange flights in ascending order of price.
        if matching_flights:
            # Retrieve the minimum fare for each flight to facilitate sorting.
            for flight in matching_flights:
                prices = flight.get("prices", {})
                if prices:
                    sorted_prices = sorted([prices[key] for key in prices])
                    flight["lowest_price"] = min(sorted_prices)
                else:
                    flight["lowest_price"] = float('inf')

            matching_flights.sort(key=lambda x: x["lowest_price"])

        # Compose reply.
        response = {
            "search_criteria": {
                "origin": origin,
                "destination": destination,
                "date": date,
                "cabin_class": cabin_class,
                "max_price": max_price
            },
            "total_flights_found": len(matching_flights),
            "flights": matching_flights
        }

        # Include a pricing summary when flights are available.
        if matching_flights:
            all_prices = []
            for flight in matching_flights:
                prices = flight.get("prices", {})
                for cabin in sorted([key for key in prices]):
                    price = prices[cabin]
                    all_prices.append({
                        "cabin": cabin,
                        "price": price,
                        "flight_number": flight["flight_number"]
                    })

            if all_prices:
                all_prices.sort(key=lambda x: x["price"])
                response["pricing_summary"] = {
                    "lowest_price": all_prices[0],
                    "highest_price": all_prices[-1],
                    "price_range": {
                        "min": all_prices[0]["price"],
                        "max": all_prices[-1]["price"]
                    }
                }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_flights",
                "description": "Search for available flights between airports on a specific date with optional cabin class and price filtering. Returns flight details including aircraft information, crew assignments, and operational status. Supports major US airports and international destinations.",
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
                        "date": {
                            "type": "string",
                            "description": "Date for flight search in YYYY-MM-DD format"
                        },
                        "cabin_class": {
                            "type": "string",
                            "description": "Optional cabin class filter: 'basic_economy', 'economy', 'business', or 'first'. Each class offers different amenities and baggage allowances."
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Optional maximum price filter in USD. Filters results to show only flights within budget."
                        }
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
