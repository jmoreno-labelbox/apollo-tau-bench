# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPromotionById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get('promotion_id')
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                return json.dumps(promo)
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_promotion_by_id",
                "description": "Retrieves details of a promotion by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The unique ID of the promotion.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }
