# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOfferDetails(Tool):
    """Fetch full details of an offer by offer_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], offer_id: Any) -> str:
        offer_id = _idstr(offer_id)
        if not offer_id:
            return json.dumps({"error": "Missing required field: offer_id"}, indent=2)
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_id") == offer_id:
                return json.dumps(offer, indent=2)

        return json.dumps({"error": f"No offer found with ID '{offer_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_offer_details",
                "description": "Fetch full details of an offer by offer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_id": {"type": "string", "description": "Exact offer ID to retrieve."}
                    },
                    "required": ["offer_id"],
                },
            },
        }
