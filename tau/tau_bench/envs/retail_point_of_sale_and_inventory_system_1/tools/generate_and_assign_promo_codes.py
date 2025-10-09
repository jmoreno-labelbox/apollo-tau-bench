from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GenerateAndAssignPromoCodes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_ids: list[str] = None, promotion_id: str = None) -> str:
        if customer_ids is None:
            customer_ids = []

        if "promo_codes" not in data:
            data["promo_codes"] = {}

        generated_assignments = []
        for cid in customer_ids:
            unique_code = f"VIP-{promotion_id}-{cid[-4:]}"
            assignment = {
                "code": unique_code,
                "promotion_id": promotion_id,
                "customer_id": cid,
                "is_used": False,
            }
            data["promo_codes"][unique_code] = assignment
            generated_assignments.append(assignment)
        payload = generated_assignments
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateAndAssignPromoCodes",
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
