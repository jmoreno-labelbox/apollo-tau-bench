# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewOffer(Tool):
    """Create a new offer and append it to the offers DB."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], offer_code: Any, discount_type: Any, discount_value: Any
    ) -> str:
        offer_code = offer_code
        discount_type = discount_type
        discount_value = discount_value

        if not all([offer_code, discount_type, discount_value is not None]):
            return json.dumps(
                {"error": "Missing required fields: offer_code, discount_type, discount_value"},
                indent=2,
            )
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
        return json.dumps(new_offer, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_offer",
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
