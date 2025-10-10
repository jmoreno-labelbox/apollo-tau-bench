# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_bonus_payment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], bonus: Dict[str, Any]) -> str:
        bonuses = data.setdefault("bonus_payments", [])
        bonuses.append(bonus)
        return json.dumps(bonus, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_bonus_payment",
                "description": "Insert a one-time bonus payment record for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bonus": {
                            "type": "object",
                            "description": "Complete bonus payment object including bonus_id, employee_id, amount, currency, payment_date, and reason."
                        }
                    },
                    "required": ["bonus"],
                    "additionalProperties": False
                }
            }
        }
