# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCourierByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], courier_name: str) -> str:
        """
        Get courier details based on courier name (case-insensitive search)

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info, tracking_ids)
        """
        if not courier_name or not courier_name.strip():
            return json.dumps({
                "error": "Courier name is required",
                "status": "failed"
            })

        courier_name = courier_name.strip()

        # Locate courier by name (search disregarding case sensitivity)
        couriers = data.get("couriers", [])
        matching_couriers = []

        for courier in couriers:
            stored_name = courier.get("name", "")

            # Case-insensitive exact match
            if stored_name.lower() == courier_name.lower():
                matching_couriers.insert(0, courier)  # Prioritize exact matches.
            # Case-insensitive partial match
            elif courier_name.lower() in stored_name.lower():
                matching_couriers.append(courier)

        if not matching_couriers:
            return json.dumps({
                "error": f"No courier found with name containing '{courier_name}'",
                "status": "not_found",
                "search_term": courier_name
            })

        # Provide the initial (optimal) match along with comprehensive details.
        best_match = matching_couriers[0]

        # Compute delivery performance indicators.
        tracking_ids = best_match.get("tracking_ids", [])
        coverage_area = best_match.get("coverage_area", [])

        # Verify if the courier possesses any current tracking IDs.
        has_available_tracking = len(tracking_ids) > 0

        # Assess service features according to availability.
        service_capabilities = {
            "domestic_delivery": "USA" in coverage_area,
            "international_delivery": len([country for country in coverage_area if country != "USA"]) > 0,
            "total_coverage_countries": len(coverage_area),
            "available_tracking_ids": len(tracking_ids)
        }

        result = {
            "status": "success",
            "search_term": courier_name,
            "exact_match": best_match.get("name", "").lower() == courier_name.lower(),
            "courier_details": {
                "courier_id": best_match.get("courier_id"),
                "name": best_match.get("name"),
                "contact_info": best_match.get("contact_info", {}),
                "coverage_area": coverage_area,
                "service_types": best_match.get("service_types", ["standard"]),
                "base_cost": best_match.get("base_cost", 0),
                "rating": best_match.get("rating", 0),
                "specialties": best_match.get("specialties", [])
            },
            "service_capabilities": service_capabilities,
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_courier_by_name",
                "description": "Get courier details based on courier name with case-insensitive search. Returns exact matches first, then partial matches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "courier_name": {
                            "type": "string",
                            "description": "Courier name to search for (case-insensitive, supports partial matching)"
                        }
                    },
                    "required": ["courier_name"]
                }
            }
        }
