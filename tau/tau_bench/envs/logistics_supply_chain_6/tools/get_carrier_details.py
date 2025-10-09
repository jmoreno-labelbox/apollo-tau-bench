from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCarrierDetails(Tool):
    """Utility for retrieving information about a particular shipping carrier."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_id: str) -> str:
        """Run the tool with the provided parameters."""
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier.get("carrier_id") == carrier_id:
                payload = carrier
                out = json.dumps(payload, indent=2)
                return out
            if carrier.get("scac") == carrier_id:
                payload = carrier
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Carrier with ID/SCAC {carrier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierDetails",
                "description": "Retrieves detailed information about a specific shipping carrier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_id": {
                            "type": "string",
                            "description": "The ID/SCAC of the carrier.",
                        }
                    },
                    "required": ["carrier_id"],
                },
            },
        }
