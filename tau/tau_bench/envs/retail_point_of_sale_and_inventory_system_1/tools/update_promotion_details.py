# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePromotionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], promotion_id) -> str:
        promotions = list(data.get("promotions", {}).values())
        updated_promo = None
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                for key, value in kwargs.items():
                    if key != 'promotion_id':
                        promo[key] = value
                updated_promo = promo
                break
        return json.dumps({"updated_promotion": updated_promo})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_promotion_details",
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
