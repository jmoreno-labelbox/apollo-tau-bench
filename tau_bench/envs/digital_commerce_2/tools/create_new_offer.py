from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class CreateNewOffer(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], offer_code: Any, discount_type: Any, discount_value: Any
    ) -> str:
        if not all([offer_code, discount_type, discount_value is not None]):
            payload = {
                "error": "Missing required fields: offer_code, discount_type, discount_value"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        offers = data.get("offers", [])
        offer_id = get_next_offer_id(data)
        new_offer = {
            "offer_id": offer_id,
            "offer_code": offer_code,
            "discount_type": discount_type,
            "discount_value": float(discount_value),
            "is_active": True,
        }
        offers.append(new_offer)
        payload = new_offer
        out = json.dumps(payload, indent=2)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewOffer",
                "description": "Create a new offer and append it to the offers DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_code": {
                            "type": "string",
                            "description": "Unique offer_code for the offer (e.g., SUMMER10).",
                        },
                        "discount_type": {
                            "type": "string",
                            "description": "Type of discount: 'PERCENTAGE' or 'FIXED_AMOUNT'.",
                        },
                        "discount_value": {
                            "type": "number",
                            "description": "Value of the discount (percentage or fixed amount).",
                        },
                    },
                    "required": ["offer_code", "discount_type", "discount_value"],
                },
            },
        }
