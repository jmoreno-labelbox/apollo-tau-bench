# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePromotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get('name')
        promotion_type = kwargs.get('type')
        discount_value = kwargs.get('discount_value')
        description = kwargs.get('description')
        applicable_skus = kwargs.get('applicable_skus')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        status = kwargs.get('status')
        usage_limit = kwargs.get('usage_limit')
        times_used = kwargs.get('times_used')

        promotions = list(data.get("promotions", {}).values())  # Alterei para uma lista [].

        max_promotion_id_num = 0
        for promo in promotions:  # Percorra a lista diretamente.
            if isinstance(promo.get("promotion_id"), str):
                match = re.match(r"PROMO-(\d+)", promo["promotion_id"])
                if match:
                    num = int(match.group(1))
                    if num > max_promotion_id_num:
                        max_promotion_id_num = num

        next_promotion_id_num = max_promotion_id_num + 1
        new_promotion_id = f"PROMO-{next_promotion_id_num:03d}"  # Assegura que haja 3 dígitos, preenchendo com zeros à esquerda.

        new_promotion = {
            "promotion_id": new_promotion_id,
            "name": name,
            "type": promotion_type,
            "discount_value": discount_value,
            "description": description,
            "applicable_skus": applicable_skus,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "usage_limit": usage_limit,
            "times_used": times_used
        }

        promotions.append(new_promotion)  # Insere na lista
        data["promotions"] = promotions
        return json.dumps({"promotion_id": new_promotion_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_promotion",
                "description": "Creates a new promotion record with specified details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "The name of the new promotion."},
                        "type": {"type": "string", "description": "The type of the promotion (e.g., 'percentage', 'fixed_bundle', 'bogo_percentage', 'tax_free')."},
                        "discount_value": {"type": "number", "description": "The discount value (e.g., 10.0 for 10% or $10)."},
                        "description": {"type": "string", "description": "A brief description of the promotion."},
                        "applicable_skus": {"type": "array", "items": {"type": "string"}, "description": "A list of SKUs the promotion applies to."},
                        "start_date": {"type": "string", "format": "date", "description": "The start date of the promotion (YYYY-MM-DD)."},
                        "end_date": {"type": "string", "format": "date", "description": "The end date of the promotion (YYYY-MM-DD)."},
                        "status": {"type": "string", "description": "The initial status of the promotion (e.g., 'active', 'scheduled', 'planned')."},
                        "usage_limit": {"type": ["integer", "null"], "description": "The maximum number of times this promotion can be used, or null if unlimited."},
                        "times_used": {"type": "integer", "description": "The initial count of how many times the promotion has been used."},
                    },
                    "required": ["name", "type", "discount_value", "description", "applicable_skus", "start_date", "end_date", "status", "times_used"],
                },
            },
        }
