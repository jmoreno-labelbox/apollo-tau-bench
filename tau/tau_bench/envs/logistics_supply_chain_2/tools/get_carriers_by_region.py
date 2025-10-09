from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCarriersByRegion(Tool):
    """Utility for obtaining carriers based on their geographical region."""

    @staticmethod
    def invoke(data: dict[str, Any], region: str = None, list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if region:
            active_carriers = [
                carrier["scac"]
                for carrier in carriers
                if carrier.get("active_status")
                and region.lower() in carrier.get("regional_coverage").lower()
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
                "name": "GetCarriersByRegion",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "string",
                            "description": "Region eg. Global",
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
