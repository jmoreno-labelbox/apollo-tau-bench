# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateAndAssignPromoCodes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_ids = kwargs.get('customer_ids', [])
        promotion_id = kwargs.get('promotion_id')

        if "promo_codes" not in data:
            data["promo_codes"] = {}

        generated_assignments = []
        for cid in customer_ids:
            unique_code = f"VIP-{promotion_id}-{cid[-4:]}"
            assignment = {
                "code": unique_code,
                "promotion_id": promotion_id,
                "customer_id": cid,
                "is_used": False
            }
            data["promo_codes"][unique_code] = assignment
            generated_assignments.append(assignment)

        return json.dumps(generated_assignments)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_and_assign_promo_codes",
                "description": "Generates unique, single-use promotion codes and assigns them to a list of customers for a specific promotion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of customer IDs to receive the unique codes.",
                        },
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to associate the codes with.",
                        },
                    },
                    "required": ["customer_ids", "promotion_id"],
                },
            },
        }
