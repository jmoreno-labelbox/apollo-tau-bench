# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListActivePromotions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], store_id) -> str:
        if store_id == "STORE-002":
            result = [{"promotion_id": "PROMO-202508", "name": "Back to School"}]
        else:
            result = []
        return json.dumps(result)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "list_active_promotions",
                "description": "Tool function: list_active_promotions",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
