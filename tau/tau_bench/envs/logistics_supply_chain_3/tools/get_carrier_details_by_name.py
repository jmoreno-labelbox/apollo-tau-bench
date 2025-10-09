from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetCarrierDetailsByName(Tool):
    """Obtains complete details for a carrier using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None) -> str:
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier.get("carrier_name") == carrier_name:
                payload = carrier
                out = json.dumps(payload)
                return out
        payload = {"error": "Carrier not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierDetailsByName",
                "description": "Retrieves the full record for a carrier by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {
                            "type": "string",
                            "description": "The full name of the carrier.",
                        }
                    },
                    "required": ["carrier_name"],
                },
            },
        }
