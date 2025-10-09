from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class cancel_promotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        if promotion_id is None:
            payload = {"error": "promotion_id must be sent"}
            out = json.dumps(payload)
            return out

        promotions = data.get("promotions", [])
        products = data.get("products", [])

        for promotion in promotions:
            # Narrow down to the appropriate promotion
            if promotion["promotion_id"] == promotion_id:
                # Eliminate discounts from the products
                # TODO: investigate the possibility of multiple promotions for each product
                applicable_skus = promotion["applicable_skus"]
                for product in products:
                    if product["sku"] in applicable_skus:
                        product["is_discountable"] = False

                # TODO: consider if the row should simply be deleted?
                promotion["status"] = "canceled"
        payload = {"success": "complete"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelPromotion",
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
