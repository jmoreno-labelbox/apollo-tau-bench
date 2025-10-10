# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeactivatePromotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], promotion_id) -> str:
        promotions = list(data.get("promotions", {}).values())
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "inactive"
                return json.dumps({"promotion_id": promotion_id, "status": "inactive"})
        return json.dumps({"promotion_id": promotion_id, "status": "not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deactivate_promotion",
                "description": "Deactivates a promotion by setting its status to 'inactive'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to deactivate.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }
