from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLoanDetailsByCustomerIdAndType(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", loan_type: str = "") -> str:
        customer_id = customer_id.strip()
        loan_type = loan_type.strip().lower()

        if not customer_id or not loan_type:
            return json.dumps({
                "error": "Both customer_id and loan_type are required."
            }, indent=2)

        loans = data.get("loans", [])
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
                "name": "getLoanDetailsByCustomerIdAndType",
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
