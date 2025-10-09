from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class ActivatePromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "active"
                payload = {"promotion_id": promotion_id, "status": "active"}
                out = json.dumps(payload)
                return out
        payload = {"promotion_id": promotion_id, "status": "not_found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ActivatePromotion",
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
