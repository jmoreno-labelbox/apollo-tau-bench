# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPromotionsByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], status) -> str:
        promotions = list(data.get("promotions", {}).values())
        results = [promo for promo in promotions if promo.get("status") == status]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_promotions_by_status",
                "description": "Retrieves all promotions with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status of the promotions to retrieve (e.g., 'active', 'scheduled', 'planned', 'inactive').",
                        },
                    },
                    "required": ["status"],
                },
            },
        }
