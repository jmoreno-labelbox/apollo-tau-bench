from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GetPromotionById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                payload = promo
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionById",
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
