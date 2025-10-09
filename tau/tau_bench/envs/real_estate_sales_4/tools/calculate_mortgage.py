from tau_bench.envs.tool import Tool
import json
from typing import Any

class CalculateMortgage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], principal: float = None, interest_rate: float = None, loan_term_years: int = 30) -> str:
        if not principal or not interest_rate:
            payload = {"error": "principal and interest_rate are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        monthly_rate = interest_rate / 100 / 12
        num_payments = loan_term_years * 12

        if monthly_rate == 0:
            monthly_payment = principal / num_payments
        else:
            monthly_payment = (
                principal
                * (monthly_rate * (1 + monthly_rate) ** num_payments)
                / ((1 + monthly_rate) ** num_payments - 1)
            )

        result = {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(monthly_payment * num_payments, 2),
            "total_interest": round((monthly_payment * num_payments) - principal, 2),
            "loan_details": {
                "principal": principal,
                "interest_rate": interest_rate,
                "loan_term_years": loan_term_years,
            },
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateMortgage",
                "description": "Calculate monthly mortgage payment and loan details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "principal": {
                            "type": "number",
                            "description": "Loan amount in dollars",
                        },
                        "interest_rate": {
                            "type": "number",
                            "description": "Annual interest rate as percentage (e.g., 5.5 for 5.5%)",
                        },
                        "loan_term_years": {
                            "type": "integer",
                            "description": "Loan term in years (default: 30)",
                        },
                    },
                    "required": ["principal", "interest_rate"],
                },
            },
        }
