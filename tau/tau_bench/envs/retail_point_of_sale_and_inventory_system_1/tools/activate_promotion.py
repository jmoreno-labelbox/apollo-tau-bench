# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ActivatePromotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get('promotion_id')
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "active"
                return json.dumps({"promotion_id": promotion_id, "status": "active"})
        return json.dumps({"promotion_id": promotion_id, "status": "not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activate_promotion",
                "description": "Activates a promotion by setting its status to 'active'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to activate.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }
