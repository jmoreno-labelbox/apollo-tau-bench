from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class create_promotion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str,
        type: str,
        discount_value: float,
        description: str,
        applicable_skus: list[str],
        start_date: str,
        end_date: str,
        status: str,
        usage_limit: int
    ) -> str:
        promotion_fields_unpacked = {
            "name": name,
            "type": type,
            "discount_value": discount_value,
            "description": description,
            "applicable_skus": applicable_skus,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "usage_limit": usage_limit,
        }

        # Convert applicable_skus from json to a list if provided as json
        if isinstance(promotion_fields_unpacked["applicable_skus"], str):
            promotion_fields_unpacked["applicable_skus"] = json.loads(
                promotion_fields_unpacked["applicable_skus"]
            )

        promotions = data.get("promotions", [])
        products = data.get("products", [])

        promotion_id = (
            max([int(x["promotion_id"].split("-")[1]) for x in promotions]) + 1
        )

        # TODO: automate status setting based on the start date
        promotion_row = {
            "promotion_id": f"PROMO-{promotion_id:03}",
            "name": promotion_fields_unpacked["name"],
            "type": promotion_fields_unpacked["type"],
            "discount_value": promotion_fields_unpacked["discount_value"],
            "description": promotion_fields_unpacked["description"],
            "applicable_skus": promotion_fields_unpacked["applicable_skus"],
            "start_date": promotion_fields_unpacked["start_date"],
            "end_date": promotion_fields_unpacked["end_date"],
            "status": promotion_fields_unpacked["status"],
            "usage_limit": promotion_fields_unpacked["usage_limit"],
            "times_used": 0,
        }

        # Revise the skus
        for product in products:
            if product["sku"] in promotion_fields_unpacked["applicable_skus"]:
                product["is_discountable"] = True

                # TODO: will need to manage various discount types
                product["discount_rate"] = (
                    promotion_fields_unpacked["discount_value"] / 100.0
                )
        payload = {"success": "complete"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePromotion",
                "description": "Creates a new promotion",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The human readable name for the promotion",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of promotion. 'fixed_bundle', 'tax_free', 'percentage', 'bogo_percentage'",
                        },
                        "discount_value": {
                            "type": "int",
                            "description": "The discount amount as an integer for percentage and bogo_percentage",
                        },
                        "description": {
                            "type": "string",
                            "description": "A human readable description of the sale",
                        },
                        "applicable_skus": {
                            "type": "string",
                            "description": "A json list containing the skus that the discount applies to",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The date the promotion starts on. YYYY-MM-DD",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The date the promotion ends on. YYYY-MM-DD",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the promotion. Should be 'active' if the sale is going or 'planned' if it is happening in the future",
                        },
                        "usage_limit": {
                            "type": "int",
                            "description": "The number of times the sale can be used.",
                        },
                    },
                },
            },
        }
