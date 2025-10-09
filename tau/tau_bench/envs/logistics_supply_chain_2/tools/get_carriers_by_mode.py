from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCarriersByMode(Tool):
    """Utility for fetching carriers according to their supported transportation mode."""

    @staticmethod
    def invoke(data: dict[str, Any], mode: str = None, list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if mode:
            active_carriers = [
                carrier["scac"]
                for carrier in carriers
                if carrier.get("active_status")
                and mode in carrier.get("supported_modes")
            ]
        else:
            active_carriers = [
                carrier["scac"] for carrier in carriers if carrier.get("active_status")
            ]
        if list_of_scacs:
            active_carriers = [
                carrier for carrier in active_carriers if carrier in list_of_scacs
            ]
        payload = active_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarriersByMode",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "Mode eg. Air, Sea, Truck",
                        },
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of SCACs to choose from.",
                        },
                    },
                },
            },
        }
