from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCarrierBySCAC(Tool):
    """Utility for obtaining carrier information using the carrier SCAC."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_scac: str) -> str:
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                payload = carrier
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Carrier with scac {carrier_scac} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierByScac",
                "description": "Retrieve Carrier details by carrier SCAC.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {
                            "type": "string",
                            "description": "Unique Carrier identifier.",
                        }
                    },
                    "required": ["carrier_scac"],
                },
            },
        }
