from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class UpdateLoanBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, amount: float = None) -> str:
        loan = next((l for l in data.get('loans', []) if l['loan_id'] == loan_id), None)
        if loan:
            loan['current_balance'] += amount
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateLoanBalance",
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
