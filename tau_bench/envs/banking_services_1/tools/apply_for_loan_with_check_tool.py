from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class ApplyForLoanWithCheckTool(Tool):
    """
    Tool for applying for a loan with a built-in risk evaluation.

    This tool takes the customer's ID, the requested amount, and the purpose
    of the loan, then calculates a basic credit score adjustment and risk level
    based on the amount. This does not persist the loan; it only simulates evaluation.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Simulates loan application and risk assessment.

        get_info() -> Dict[str, Any]:
            Returns metadata about the tool, including expected parameters.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, amount: int = None, purpose: str = None) -> str:
        if not all([customer_id, amount, purpose]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        credit_score = 700
        risk_level = "Low"
        if amount > 50000:
            credit_score -= 50
            risk_level = "Medium"
        if amount > 100000:
            credit_score -= 50
            risk_level = "High"

        return json.dumps(
            {
                "customer_id": customer_id,
                "amount": amount,
                "purpose": purpose,
                "credit_score": credit_score,
                "risk_level": risk_level,
            },
            indent=2,
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyForLoanWithCheck",
                "description": "Submit a loan request and automatically evaluate the customer's risk score.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer id"},
                        "amount": {"type": "number", "description": "Amount"},
                        "purpose": {"type": "string", "description": "Purpose"},
                    },
                    "required": ["customer_id", "amount", "purpose"],
                },
            },
        }
