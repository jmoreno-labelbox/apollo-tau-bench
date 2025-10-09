from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdatePromotionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str, key: str = None, value: Any = None,
    usage_limit: Any = None,
    times_used: Any = None,
    name: Any = None,
    description: Any = None,
    applicable_skus: Any = None,
    status: Any = None,
    end_date: Any = None,
    discount_value: Any = None,
    start_date: Any = None,
    requires_code: Any = None,
    type: Any = None,
    ) -> str:
        promotions = data.get("promotions", [])
        updated_promo = None
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                if key is not None and value is not None:
                    promo[key] = value
                updated_promo = promo
                break
        payload = {"updated_promotion": updated_promo}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePromotionDetails",
                "description": "Updates various details of an existing promotion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to update.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new name of the promotion.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The new type of the promotion (e.g., 'percentage', 'fixed_bundle').",
                        },
                        "discount_value": {
                            "type": "number",
                            "description": "The new discount value.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A new description for the promotion.",
                        },
                        "applicable_skus": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of SKUs the promotion applies to.",
                        },
                        "start_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The new start date of the promotion (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The new end date of the promotion (YYYY-MM-DD).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the promotion (e.g., 'active', 'scheduled', 'planned', 'inactive').",
                        },
                        "usage_limit": {
                            "type": "integer",
                            "description": "The new usage limit for the promotion.",
                        },
                        "times_used": {
                            "type": "integer",
                            "description": "The new number of times the promotion has been used.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }
