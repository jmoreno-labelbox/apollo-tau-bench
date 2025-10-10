# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SelectOptimalCarrier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], destination_city, destination_country, preferred_carrier, priority_level, total_weight_kg, carriers_list = None) -> str:

        carriers = data.get("carriers", [])

        # Select active carriers.
        active_carriers = [c for c in carriers if c.get("active_status", False)]

        # Implement criteria for choosing carriers.
        suitable_carriers = []
        for carrier in active_carriers:
            # Condition: Carriers with less than 95% on-time delivery are ineligible for Critical priority.
            if priority_level == "Critical" and carrier.get("performance_metrics", {}).get("on_time_delivery_percentage", 0) < 95:
                continue

            if carriers_list:
                if carrier.get('scac') not in carriers_list:
                    continue

            # Verify geographical reach and urban service capacity.
            coverage = carrier.get("regional_coverage", "")
            carrier_address = carrier.get("contact_information", {}).get("address", {})
            carrier_country = carrier_address.get("country", "")
            carrier_city = carrier_address.get("city", "")

            # As service_cities is absent in the database, apply logical criteria for service area identification.
            # dependent on the carrier's operational footprint and coverage area
            coverage_match = False

            # International carriers operate in all locations.
            if coverage == "Global":
                coverage_match = True
            # Alignment of regional coverage
            elif coverage == "North America" and destination_country in ["USA", "Canada", "Mexico"]:
                coverage_match = True
            # Matching at the country level
            elif destination_country == carrier_country:
                coverage_match = True
            # Unique situation: carriers in key hub cities can cover larger areas.
            elif carrier_city in ["Los Angeles", "New York", "Chicago", "Miami", "Seattle", "Houston"] and destination_country == "USA":
                coverage_match = True
            # Carriers can operate within their local city and nearby areas.
            elif destination_city == carrier_city:
                coverage_match = True
            elif preferred_carrier and carrier.get("scac") == preferred_carrier:
                # Verify that the specified preferred carrier meets the required criteria.
                if carrier.get("scac") == preferred_carrier:
                    coverage_match = True
            elif carriers_list:
                # Verify if the specified carrier exists within the given list of carriers.
                if carrier.get("scac") in carriers_list:
                    coverage_match = True

            if coverage_match:
                suitable_carriers.append(carrier)

        if not suitable_carriers:
            return json.dumps({"error": "No suitable carriers found for the specified criteria"})

        # Choose the optimal carrier according to performance ratings and priority criteria.
        if preferred_carrier:
            best_carrier = next((c for c in suitable_carriers if c.get("scac") == preferred_carrier), None)
        else:
            if priority_level == "Critical":
                # Prioritize performance for essential shipments.
                best_carrier = max(suitable_carriers,
                                key=lambda c: (
                                    c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0),
                                    c.get("performance_metrics", {}).get("average_rating", 0)
                                ))
            else:
                # Optimize performance and cost for standard shipments.
                best_carrier = max(suitable_carriers,
                                key=lambda c: c.get("performance_metrics", {}).get("average_rating", 0))



        return json.dumps({
            "selected_carrier": best_carrier.get("scac"),
            "carrier_name": best_carrier.get("carrier_name"),
            "performance_rating": best_carrier.get("performance_metrics", {}).get("average_rating"),
            "on_time_delivery": best_carrier.get("performance_metrics", {}).get("on_time_delivery_percentage"),
            "coverage": best_carrier.get("regional_coverage")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "select_optimal_carrier",
                "description": "Select the best carrier based on destination, priority, and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_city": {"type": "string", "description": "Destination city"},
                        "destination_country": {"type": "string", "description": "Destination country"},
                        "priority_level": {"type": "string", "description": "Shipment priority level"},
                        "total_weight_kg": {"type": "number", "description": "Total shipment weight in kg"},
                        "preferred_carrier": {
                            "type": "string",
                            "description": "Preferred carrier SCAC (optional)"
                        },
                        "carriers_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "scac": {"type": "string", "description": "Carrier SCAC code"},
                                }
                            }
                        }
                    },
                    "required": ["destination_city", "destination_country", "priority_level"]
                }
            }
        }
