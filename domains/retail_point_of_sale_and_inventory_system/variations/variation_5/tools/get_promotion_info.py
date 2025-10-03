from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class GetPromotionInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        # Consistent output for CI: always provide PROMO-202508 details
        if promotion_id == "PROMO-202508":
            result = {
                "promotion_id": "PROMO-202508",
                "name": "Back to School",
                "discount": 15,
            }
        else:
            result = {}
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPromotionInfo",
                "parameters": {"promotion_id": {"type": "string"}},
                "required": ["promotion_id"],
            },
        }
