# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCarrierByService(Tool):
    """Finds the best-rated, active carrier for a specific transport mode AND service level."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        mode_of_transport = kwargs.get("mode_of_transport")
        service_level = kwargs.get("service_level")

        if not mode_of_transport or not service_level:
            return json.dumps(
                {"error": "Mode of transport and service level are required"}
            )

        best_carrier = None
        max_rating = -1.0

        for carrier in carriers:
            is_active = carrier.get("active_status", False)
            supported_modes = [
                mode.lower() for mode in carrier.get("supported_modes", [])
            ]
            supported_services = [
                service.lower() for service in carrier.get("service_levels", [])
            ]

            if (
                is_active
                and mode_of_transport.lower() in supported_modes
                and service_level.lower() in supported_services
            ):
                current_rating = carrier.get("performance_metrics", {}).get(
                    "average_rating", 0.0
                )
                if current_rating > max_rating:
                    max_rating = current_rating
                    best_carrier = carrier

        if best_carrier:
            return json.dumps(
                {
                    "carrier_id": best_carrier.get("carrier_id"),
                    "carrier_name": best_carrier.get("carrier_name"),
                    "carrier_scac": best_carrier.get("scac"),
                }
            )
        else:
            return json.dumps(
                {
                    "error": f"No active carrier found for mode '{mode_of_transport}' and service '{service_level}'"
                }
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_carrier_by_service",
                "description": "Finds the active carrier with the highest rating for a given transport mode AND a specific service level (e.g., 'Pharma', 'Perishables', 'Express').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode_of_transport": {
                            "type": "string",
                            "description": "The required mode of transport (e.g., 'Air', 'Sea', 'Truck').",
                        },
                        "service_level": {
                            "type": "string",
                            "description": "The specific service level required (e.g., 'Pharma', 'Reefer', 'Express').",
                        },
                    },
                    "required": ["mode_of_transport", "service_level"],
                },
            },
        }
