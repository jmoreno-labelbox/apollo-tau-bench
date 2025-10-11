# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCheapestCarrierByService(Tool):
    """Finds the cheapest, active carrier for a specific transport mode and service level."""

    @staticmethod
    def invoke(data: Dict[str, Any], mode_of_transport, service_level) -> str:
        carriers = list(data.get("carriers", {}).values())

        if not mode_of_transport or not service_level:
            return json.dumps(
                {"error": "Mode of transport and service level are required"}
            )

        cheapest_carrier = None
        # Start with an extremely high value for the cost.
        min_cost = float("inf")

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
                # This is a simulated cost; in an actual situation, it would involve a detailed calculation or an API request.
                # In this simulation, the length of the carrier name will serve as a substitute for cost.
                current_cost = len(carrier.get("carrier_name", ""))
                if current_cost < min_cost:
                    min_cost = current_cost
                    cheapest_carrier = carrier

        if cheapest_carrier:
            return json.dumps(
                {
                    "carrier_id": cheapest_carrier.get("carrier_id"),
                    "carrier_name": cheapest_carrier.get("carrier_name"),
                    "carrier_scac": cheapest_carrier.get("scac"),
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
                "name": "find_cheapest_carrier_by_service",
                "description": "Finds the active carrier with the lowest cost for a given transport mode and a specific service level (e.g., 'LTL', 'FTL').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode_of_transport": {
                            "type": "string",
                            "description": "The required mode of transport (e.g., 'Truck', 'Rail').",
                        },
                        "service_level": {
                            "type": "string",
                            "description": "The specific service level required (e.g., 'LTL', 'Economy').",
                        },
                    },
                    "required": ["mode_of_transport", "service_level"],
                },
            },
        }
