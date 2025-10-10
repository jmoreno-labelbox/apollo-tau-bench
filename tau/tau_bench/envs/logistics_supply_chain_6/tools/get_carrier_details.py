# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCarrierDetails(Tool):
    """Tool to get details for a specific shipping carrier."""

    @staticmethod
    def invoke(data: Dict[str, Any], carrier_id: str) -> str:
        """Execute the tool with given parameters."""
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier.get("carrier_id") == carrier_id:
                return json.dumps(carrier, indent=2)
            if carrier.get("scac") == carrier_id:
                return json.dumps(carrier, indent=2)
        return json.dumps({"error": f"Carrier with ID/SCAC {carrier_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_details",
                "description": "Retrieves detailed information about a specific shipping carrier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_id": {"type": "string", "description": "The ID/SCAC of the carrier."}
                    },
                    "required": ["carrier_id"],
                },
            },
        }
