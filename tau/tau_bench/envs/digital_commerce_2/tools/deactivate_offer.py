# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeactivateOffer(Tool):
    """Deactivate an offer by its offer_code."""

    @staticmethod
    def invoke(data: Dict[str, Any], offer_code: Any) -> str:
        offer_code = offer_code
        if not offer_code:
            return json.dumps({"error": "Missing required field: offer_code"}, indent=2)
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_code") == offer_code:
                offer["is_active"] = False
                return json.dumps(offer, indent=2)

        return json.dumps({"error": f"No offer found with code '{offer_code}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deactivate_offer",
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
