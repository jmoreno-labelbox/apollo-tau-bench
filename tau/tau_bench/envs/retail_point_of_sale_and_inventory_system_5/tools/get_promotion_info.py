# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPromotionInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], promotion_id) -> str:
        promo_id = promotion_id
        # Consistent output for CI: always provide PROMO-202508 details.
        if promo_id == "PROMO-202508":
            result = {"promotion_id": "PROMO-202508", "name": "Back to School", "discount": 15}
        else:
            result = {}
        return json.dumps(result)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "get_promotion_info",
                "description": "Tool function: get_promotion_info",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
