# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLoanDetailsByCustomerIdAndType(Tool):
    """Fetches loan details for a specific customer and loan type."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id", "").strip()
        loan_type = kwargs.get("loan_type", "").strip().lower()

        if not customer_id or not loan_type:
            return json.dumps({
                "error": "Both customer_id and loan_type are required."
            }, indent=2)

        loans = list(data.get("loans", {}).values())
        matched_loan = next(
            (loan for loan in loans
             if loan.get("customer_id") == customer_id and
                loan.get("loan_type", "").strip().lower() == loan_type),
            None
        )

        if not matched_loan:
            return json.dumps({
                "message": "No matching loan found for the customer and loan type."
            }, indent=2)

        return json.dumps(matched_loan, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_loan_details_by_customer_id_and_type",
                "description": (
                    "Returns a customer's loan details for a specific loan type. "
                    "Loan type values can include: 'Mortgage', 'Auto', 'Personal', 'Business', etc."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the loan"
                        },
                        "loan_type": {
                            "type": "string",
                            "description": (
                                "Type of loan to search for. "
                                "Acceptable values: 'Mortgage', 'Auto', 'Personal', 'Business', etc."
                            )
                        }
                    },
                    "required": ["customer_id", "loan_type"]
                }
            }
        }
