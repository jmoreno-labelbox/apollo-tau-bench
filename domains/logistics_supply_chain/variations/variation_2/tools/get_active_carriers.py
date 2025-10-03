from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetActiveCarriers(Tool):
    """Utility for fetching all currently active carriers."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if list_of_scacs:
            active_carriers = [
                carrier["scac"]
                for carrier in carriers
                if carrier.get("active_status") and carrier["scac"] in list_of_scacs
            ]
        else:
            active_carriers = [
                carrier["scac"] for carrier in carriers if carrier.get("active_status")
            ]
        payload = active_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetActiveCarriers",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of SCACs to choose from.",
                        }
                    },
                },
            },
        }
