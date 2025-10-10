# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLoanStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id, new_status) -> str:
        loan = next((l for l in list(data.get('loans', {}).values()) if l['loan_id'] == loan_id), None)
        if loan:
            loan['status'] = new_status
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_loan_status",
                        "description": "Updates the status of a loan (e.g., Active, Paid Off).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "loan_id": {"type": "string", "description": "The unique ID of the loan."},
                                        "new_status": {"type": "string", "description": "The new status for the loan."}
                                },
                                "required": ["loan_id", "new_status"]
                        }
                }
        }
