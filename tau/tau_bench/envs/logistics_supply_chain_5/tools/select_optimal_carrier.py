from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SelectOptimalCarrier(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        destination_city: str = None,
        destination_country: str = None,
        priority_level: str = None,
        total_weight_kg: float = None,
        preferred_carrier: str = None,
        carriers_list: list = None,
        weight_kg: Any = None,
        max_transit_days: Any = None,
    ) -> str:
        carriers = data.get("carriers", [])

        # Select only the active carriers
        active_carriers = [c for c in carriers if c.get("active_status", False)]

        # Implement business guidelines for choosing carriers
        suitable_carriers = []
        for carrier in active_carriers:
            # Guideline: Carriers with less than 95% on-time delivery are not eligible for Critical priority
            if priority_level == "Critical" and carrier.get("performance_metrics", {}).get("on_time_delivery_percentage", 0) < 95:
                continue

            if carriers_list:
                if carrier.get('scac') not in carriers_list:
                    continue

            # Guideline: Assess regional coverage and the ability to service cities
            coverage = carrier.get("regional_coverage", "")
            carrier_address = carrier.get("contact_information", {}).get("address", {})
            carrier_country = carrier_address.get("country", "")
            carrier_city = carrier_address.get("city", "")

            # As service_cities is absent in the database, utilize logical service area assessment
            # derived from the operational presence and coverage of the carrier
            coverage_match = False

            # International carriers cater to all locations
            if coverage == "Global":
                coverage_match = True
            # Matching regional coverage
            elif coverage == "North America" and destination_country in ["United States", "Maple Nation", "Mexico"]:
                coverage_match = True
            # Matching at the country level
            elif destination_country == carrier_country:
                coverage_match = True
            # Exception: carriers located in major hub cities can cover wider areas
            elif carrier_city in ["San Diego", "New York", "Milwaukee", "Fort Lauderdale", "Portland", "Dallas"] and destination_country == "United States":
                coverage_match = True
            # Carriers are able to service their home city along with the nearby region
            elif destination_city == carrier_city:
                coverage_match = True
            elif preferred_carrier and carrier.get("scac") == preferred_carrier:
                # When a preferred carrier is indicated, verify it meets the requirements
                if carrier.get("scac") == preferred_carrier:
                    coverage_match = True
            elif carriers_list:
                # When a list of carriers is available, confirm if this carrier is included
                if carrier.get("scac") in carriers_list:
                    coverage_match = True

            if coverage_match:
                suitable_carriers.append(carrier)

        if not suitable_carriers:
            return json.dumps({"error": "No suitable carriers found for the specified criteria"})

        # Choose the optimal carrier according to performance ratings and priority guidelines
        if preferred_carrier:
            best_carrier = next((c for c in suitable_carriers if c.get("scac") == preferred_carrier), None)
        else:
            if priority_level == "Critical":
                # For urgent shipments, give precedence to performance
                best_carrier = max(suitable_carriers,
                                key=lambda c: (
                                    c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0),
                                    c.get("performance_metrics", {}).get("average_rating", 0)
                                ))
            else:
                # For regular shipments, find a balance between performance and cost
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
                "name": "SelectOptimalCarrier",
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
