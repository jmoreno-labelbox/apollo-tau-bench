# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SelectOptimalCarrier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        destination_city = kwargs.get("destination_city")
        destination_country = kwargs.get("destination_country")
        priority_level = kwargs.get("priority_level")
        total_weight_kg = kwargs.get("total_weight_kg")
        preferred_carrier = kwargs.get("preferred_carrier")
        carriers_list = kwargs.get("carriers_list", None)

        carriers = data.get("carriers", [])

        # Filter active carriers
        active_carriers = [c for c in carriers if c.get("active_status", False)]

        # Apply business rules for carrier selection
        suitable_carriers = []
        for carrier in active_carriers:
            # Rule: Carriers with <95% on-time delivery cannot handle Critical priority
            if priority_level == "Critical" and carrier.get("performance_metrics", {}).get("on_time_delivery_percentage", 0) < 95:
                continue

            if carriers_list:
                if carrier.get('scac') not in carriers_list:
                    continue

            # Rule: Check regional coverage and city service capability
            coverage = carrier.get("regional_coverage", "")
            carrier_address = carrier.get("contact_information", {}).get("address", {})
            carrier_country = carrier_address.get("country", "")
            carrier_city = carrier_address.get("city", "")

            # Since service_cities doesn't exist in DB, use logical service area determination
            # based on carrier operational presence and coverage
            coverage_match = False

            # Global carriers serve all destinations
            if coverage == "Global":
                coverage_match = True
            # Regional coverage matching
            elif coverage == "North America" and destination_country in ["USA", "Canada", "Mexico"]:
                coverage_match = True
            # Country-level matching
            elif destination_country == carrier_country:
                coverage_match = True
            # Special case: carriers in major hub cities can serve broader regions
            elif carrier_city in ["Los Angeles", "New York", "Chicago", "Miami", "Seattle", "Houston"] and destination_country == "USA":
                coverage_match = True
            # Carriers can serve their home city and surrounding region
            elif destination_city == carrier_city:
                coverage_match = True
            elif preferred_carrier and carrier.get("scac") == preferred_carrier:
                # If a preferred carrier is specified, ensure it matches the criteria
                if carrier.get("scac") == preferred_carrier:
                    coverage_match = True
            elif carriers_list:
                # If a list of carriers is provided, check if this carrier is in the list
                if carrier.get("scac") in carriers_list:
                    coverage_match = True

            if coverage_match:
                suitable_carriers.append(carrier)

        if not suitable_carriers:
            return json.dumps({"error": "No suitable carriers found for the specified criteria"})

        # Select best carrier based on performance rating and priority rules
        if preferred_carrier:
            best_carrier = next((c for c in suitable_carriers if c.get("scac") == preferred_carrier), None)
        else:
            if priority_level == "Critical":
                # For critical shipments, prioritize performance
                best_carrier = max(suitable_carriers,
                                key=lambda c: (
                                    c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0),
                                    c.get("performance_metrics", {}).get("average_rating", 0)
                                ))
            else:
                # For standard shipments, balance performance and cost
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
