# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLoanBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        loan_id = kwargs.get("loan_id")
        amount = kwargs.get("amount")
        loan = next((l for l in list(data.get('loans', {}).values()) if l['loan_id'] == loan_id), None)
        if loan:
            loan['current_balance'] += amount
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_loan_balance",
                        "description": "Updates the current balance of a loan, typically after a payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "loan_id": {"type": "string", "description": "The unique ID of the loan."},
                                        "amount": {"type": "number", "description": "The amount to adjust the balance by. Use a negative value for payments."}
                                },
                                "required": ["loan_id", "amount"]
                        }
                }
        }
