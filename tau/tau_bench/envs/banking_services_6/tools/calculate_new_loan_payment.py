# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateNewLoanPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_balance = kwargs.get("current_balance")
        new_interest_rate = kwargs.get("new_interest_rate")
        remaining_term_months = kwargs.get("remaining_term_months")

        monthly_rate = (new_interest_rate / 100) / 12
        if monthly_rate == 0:
            payment = current_balance / remaining_term_months
        else:
            payment = current_balance * (monthly_rate * (1 + monthly_rate) ** remaining_term_months) / ((1 + monthly_rate) ** remaining_term_months - 1)
        return json.dumps({"new_monthly_payment": round(payment, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "calculate_new_loan_payment",
                        "description": "Calculates a new monthly loan payment based on new terms.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "current_balance": {"type": "number"},
                                        "new_interest_rate": {"type": "number"},
                                        "remaining_term_months": {"type": "integer"}
                                },
                                "required": ["current_balance", "new_interest_rate", "remaining_term_months"]
                        }
                }
        }
