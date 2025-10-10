# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemovePromotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], promotion_id: str) -> str:
        promotions = data.get("promotions", [])
        original_len = len(promotions)
        promotions[:] = [p for p in promotions if p.get("promotion_id") != promotion_id]

        if len(promotions) == original_len:
            return json.dumps({"error": f"Promotion with ID {promotion_id} not found."})

        data["promotions"] = promotions
        return json.dumps({"success": f"Promotion {promotion_id} removed successfully."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_promotion",
                "description": "Remove a promotion from the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {"type": "string", "description": "Unique identifier of the promotion to remove."}
                    },
                    "required": ["promotion_id"]
                }
            }
        }
