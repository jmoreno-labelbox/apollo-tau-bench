# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddPromotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], promotion_id: str, name: str, description: str, discount_type: str, value: float, start_date: str, end_date: str) -> str:
        promotions = data.get("promotions", [])

        if any(p.get("promotion_id") == promotion_id for p in promotions):
            return json.dumps({"error": f"Promotion with ID {promotion_id} already exists."})

        new_promotion = {
            "promotion_id": promotion_id,
            "name": name,
            "description": description,
            "discount_type": discount_type,
            "value": value,
            "start_date": start_date,
            "end_date": end_date,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        promotions.append(new_promotion)
        data["promotions"] = promotions

        return json.dumps(new_promotion, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_promotion",
                "description": "Add a new promotion to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {"type": "string", "description": "Unique identifier for the promotion."},
                        "name": {"type": "string", "description": "Name of the promotion."},
                        "description": {"type": "string", "description": "Description of the promotion."},
                        "discount_type": {"type": "string", "description": "Type of discount (percentage or fixed)."},
                        "value": {"type": "number", "description": "Discount value."},
                        "start_date": {"type": "string", "description": "Start date of the promotion (YYYY-MM-DD)."},
                        "end_date": {"type": "string", "description": "End date of the promotion (YYYY-MM-DD)."}
                    },
                    "required": ["promotion_id", "name", "description", "discount_type", "value", "start_date", "end_date"]
                }
            }
        }
