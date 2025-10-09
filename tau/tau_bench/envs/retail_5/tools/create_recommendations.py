from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class CreateRecommendations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, preferred_category: str = None, max_price: int = 1000) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        recommendations = []

        for product in products.values():
            if (
                not preferred_category
                or preferred_category.lower() in product["name"].lower()
            ):
                for variant_id, variant in product["variants"].items():
                    if variant["available"] and variant["price"] <= max_price:
                        recommendations.append(
                            {
                                "product_id": product["product_id"],
                                "name": product["name"],
                                "item_id": variant["item_id"],
                                "price": variant["price"],
                                "options": variant["options"],
                            }
                        )

        recommendations.sort(key=lambda x: x["price"])
        payload = {
                "user_id": user_id,
                "recommendations": recommendations[:5],
                "based_on_category": preferred_category,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createRecommendations",
                "description": "Create product recommendations for a user based on their preferences.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to create recommendations for",
                        },
                        "preferred_category": {
                            "type": "string",
                            "description": "Preferred product category",
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price for recommendations",
                            "default": 1000,
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
