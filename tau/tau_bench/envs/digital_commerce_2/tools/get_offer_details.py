from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOfferDetails(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], offer_id: Any) -> str:
        offer_id = _idstr(offer_id)
        if not offer_id:
            payload = {"error": "Missing required field: offer_id"}
            out = json.dumps(payload, indent=2)
            return out
        offers = data.get("offers", {}).values()
        for offer in offers.values():
            if offer.get("offer_id") == offer_id:
                payload = offer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No offer found with ID '{offer_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOfferDetails",
                "description": "Fetch full details of an offer by offer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_id": {
                            "type": "string",
                            "description": "Exact offer ID to retrieve.",
                        }
                    },
                    "required": ["offer_id"],
                },
            },
        }
