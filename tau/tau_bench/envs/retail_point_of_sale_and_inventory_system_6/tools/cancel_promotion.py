# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class cancel_promotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get("promotion_id")

        if promotion_id is None:
            return json.dumps({"error": "promotion_id must be sent"})

        promotions = data.get("promotions", [])
        products = list(data.get("products", {}).values())

        for promotion in promotions:
            # Filter to the correct promotion
            if promotion["promotion_id"] == promotion_id:
                # Remove discounts from products
                # TODO: check if there can be multiple promotions per product
                applicable_skus = promotion["applicable_skus"]
                for product in products:
                    if product["sku"] in applicable_skus:
                        product["is_discountable"] = False

                # TODO: should the row just be removed?
                promotion["status"] = "canceled"

        return json.dumps({"success": "complete"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_promotion",
                "description": "Cancels a current promotion",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The id of the promotion to cancel",
                        }
                    },
                },
            },
        }
