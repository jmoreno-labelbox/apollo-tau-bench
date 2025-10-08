from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CalculateMortgagePaymentTool(Tool):
    """Computes mortgage payments based on client profile and rates."""

    @staticmethod
    def invoke(data: dict[str, Any], loan_amount: float = None, down_payment: float = None, interest_rate: float = None, term_years: int = None) -> str:
        if None in (loan_amount, down_payment, interest_rate) or term_years is None:
            return _err("loan_amount, down_payment, best_rate, term_years are required")

        # Typical fixed-rate mortgage monthly payment formula: P * (r/12) / (1 - (1+r/12)^(-n))
        r = float(interest_rate) / 100.0
        n = term_years * 12
        if r <= 0:
            monthly = float(loan_amount) / n
        else:
            m = r / 12.0
            monthly = float(loan_amount) * (m) / (1 - math.pow(1 + m, -n))

        total_payment = monthly * n
        total_cost = total_payment + float(down_payment)
        total_interest = total_payment - float(loan_amount)

        out = {
            "loan_amount": round(float(loan_amount)),
            "down_payment": round(float(down_payment)),
            "interest_rate": float(interest_rate),
            "term_years": term_years,
            "monthly_payment": int(round(monthly)),
            "total_interest": int(round(total_interest)),
            "total_cost": int(round(total_cost)),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Business Guideline: utilize real mortgage profile inputs upstream
        return {
            "type": "function",
            "function": {
                "name": "CalculateMortgagePayment",
                "description": (
                    "Compute mortgage monthly payment and totals given rate and term."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_amount": {"type": "number"},
                        "down_payment": {"type": "number"},
                        "interest_rate": {"type": "number"},
                        "term_years": {"type": "integer"},
                    },
                    "required": [
                        "loan_amount",
                        "down_payment",
                        "interest_rate",
                        "term_years",
                    ],
                },
            },
        }
