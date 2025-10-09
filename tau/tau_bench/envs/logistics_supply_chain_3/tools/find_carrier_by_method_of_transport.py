from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindCarrierByMethodOfTransport(Tool):
    """Identifies the highest-rated, active carrier for a given transport method."""

    @staticmethod
    def invoke(data: dict[str, Any], method_of_transport: str = None) -> str:
        carriers = data.get("carriers", [])
        if not method_of_transport:
            payload = {"error": "Method of transport is required"}
            out = json.dumps(payload)
            return out
        best_carrier = None
        max_rating = -1.0

        for carrier in carriers:
            is_active = carrier.get("active_status", False)
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
            payload = {
                "carrier_id": best_carrier.get("carrier_id"),
                "carrier_name": best_carrier.get("carrier_name"),
                "carrier_scac": best_carrier.get("scac"),
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "error": f"No active carrier found for transport method: {method_of_transport}"
            }
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCarrierByMethodOfTransport",
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
