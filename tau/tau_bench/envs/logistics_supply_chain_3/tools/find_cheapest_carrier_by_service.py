from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindCheapestCarrierByService(Tool):
    """Identifies the lowest-cost, active carrier for a specific transport mode and service level."""

    @staticmethod
    def invoke(data: dict[str, Any], mode_of_transport: str = None, service_level: str = None) -> str:
        carriers = data.get("carriers", [])

        if not mode_of_transport or not service_level:
            payload = {"error": "Mode of transport and service level are required"}
            out = json.dumps(payload)
            return out

        cheapest_carrier = None
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
                current_cost = len(carrier.get("carrier_name", ""))
                if current_cost < min_cost:
                    min_cost = current_cost
                    cheapest_carrier = carrier

        if cheapest_carrier:
            payload = {
                "carrier_id": cheapest_carrier.get("carrier_id"),
                "carrier_name": cheapest_carrier.get("carrier_name"),
                "carrier_scac": cheapest_carrier.get("scac"),
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "error": f"No active carrier found for mode '{mode_of_transport}' and service '{service_level}'"
            }
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCheapestCarrierByService",
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
