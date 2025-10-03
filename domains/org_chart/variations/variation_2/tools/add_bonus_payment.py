from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_bonus_payment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], bonus: dict[str, Any]) -> str:
        bonuses = data.setdefault("bonus_payments", [])
        bonuses.append(bonus)
        payload = bonus
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddBonusPayment",
                "description": "Insert a one-time bonus payment record for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bonus": {
                            "type": "object",
                            "description": "Complete bonus payment object including bonus_id, employee_id, amount, currency, payment_date, and reason.",
                        }
                    },
                    "required": ["bonus"],
                    "additionalProperties": False,
                },
            },
        }
