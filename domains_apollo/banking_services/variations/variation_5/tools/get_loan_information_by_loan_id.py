from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class GetLoanInformationByLoanId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", loan_id: str = "") -> str:
        customer_id = customer_id.strip()
        loan_id = loan_id.strip()

        if not customer_id or not loan_id:
            return json.dumps({"error": "customer_id and loan_id are required."}, indent=2)

        # Verify and fetch the loan
        loans = data.get("loans", [])
        loan = next(
            (ln for ln in loans
             if ln.get("loan_id") == loan_id and ln.get("customer_id") == customer_id),
            None
        )
        if not loan:
            return json.dumps({"error": "Loan not found for this customer."}, indent=2)

        return json.dumps(loan, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanInformationByLoanId",
                "description": "Returns loan details for the given loan_id after verifying customer ownership.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the loan"
                        },
                        "loan_id": {
                            "type": "string",
                            "description": "Loan ID to retrieve the loan information for"
                        }
                    },
                    "required": ["customer_id", "loan_id"]
                }
            }
        }
