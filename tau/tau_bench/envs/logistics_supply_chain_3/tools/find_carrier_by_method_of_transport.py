# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCarrierByMethodOfTransport(Tool):
    """Finds the best-rated, active carrier for a specific transport method."""

    @staticmethod
    def invoke(data: Dict[str, Any], method_of_transport) -> str:
        carriers = list(data.get("carriers", {}).values())
        if not method_of_transport:
            return json.dumps({"error": "Method of transport is required"})
        best_carrier = None
        max_rating = -1.0  # Set to a value that is less than the minimum possible rating.

        for carrier in carriers:
            is_active = carrier.get("active_status", False)
            # Verify that supported_modes is a list and account for case insensitivity.
            supported_modes = [
                mode.lower() for mode in carrier.get("supported_modes", [])
            ]

            if is_active and method_of_transport.lower() in supported_modes:
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
                    "error": f"No active carrier found for transport method: {method_of_transport}"
                }
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_carrier_by_method_of_transport",
                "description": "Finds the active carrier with the highest average rating for a given method of transport (e.g., 'sea', 'air', 'truck').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method_of_transport": {
                            "type": "string",
                            "description": "The method of transport to search for (e.g., 'sea', 'air', 'truck').",
                        }
                    },
                    "required": ["method_of_transport"],
                },
            },
        }
