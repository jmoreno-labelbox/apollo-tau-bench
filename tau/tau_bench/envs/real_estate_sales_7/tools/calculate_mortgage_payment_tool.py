# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateMortgagePaymentTool(Tool):
    """Calculates mortgage payment using client profile and rates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        loan_amount = kwargs.get("loan_amount")
        down_payment = kwargs.get("down_payment")
        best_rate = kwargs.get("interest_rate")
        term_years = _as_int(kwargs.get("term_years"))
        if None in (loan_amount, down_payment, best_rate) or term_years is None:
            return _err("loan_amount, down_payment, best_rate, term_years are required")

        # Standard fixed-rate mortgage monthly payment: P * (r/12) / (1 - (1+r/12)^(-n))
        r = float(best_rate) / 100.0
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
            "interest_rate": float(best_rate),
            "term_years": term_years,
            "monthly_payment": int(round(monthly)),
            "total_interest": int(round(total_interest)),
            "total_cost": int(round(total_cost)),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Business Rule: use actual mortgage profile inputs upstream
        return {
            "type": "function",
            "function": {
                "name": "calculate_mortgage_payment",
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
