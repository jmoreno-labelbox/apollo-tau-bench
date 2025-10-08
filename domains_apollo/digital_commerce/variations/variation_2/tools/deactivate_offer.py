from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class DeactivateOffer(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], offer_code: Any) -> str:
        if not offer_code:
            payload = {"error": "Missing required field: offer_code"}
            out = json.dumps(payload, indent=2)
            return out
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_code") == offer_code:
                offer["is_active"] = False
                payload = offer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No offer found with code '{offer_code}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeactivateOffer",
                "description": "Deactivate an offer by its offer_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_code": {
                            "type": "string",
                            "description": "Exact offer code to deactivate.",
                        }
                    },
                    "required": ["offer_code"],
                },
            },
        }
