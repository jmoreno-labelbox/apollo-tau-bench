# Copyright Sierra

import datetime, random
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewLoanForCustomer(Tool):
    """Adds a new loan entry for a customer based on loan application and collateral details."""

    @staticmethod
    def invoke(data: Dict[str, Any], application_id, collateral_info, collateral_type, customer_id, currency = "USD") -> str:
        loan_application_id = application_id

        if not all([customer_id, loan_application_id, collateral_type, collateral_info]):
            return json.dumps({
                "error": "customer_id, application_id, collateral_type, and collateral_info are required."
            }, indent=2)

        customers = list(data.get("customers", {}).values())
        loan_applications = data.get("loan_applications", [])

        # Retrieve customer instance.
        customer = next((c for c in customers if c["customer_id"] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found."}, indent=2)

        # Retrieve loan application.
        application = next((a for a in loan_applications if a["application_id"] == loan_application_id), None)
        if not application:
            return json.dumps({"error": "Loan application not found."}, indent=2)

        loan_details = application.get("loan_details", {})
        decision = application.get("decision", {})
        loan_type = loan_details.get("loan_type")

        # Create identifiers
        loan_id = get_next_loan_id()
        loan_account_id = get_next_loanacc_id()

        # Establish loan account.
        new_account = {
            "account_id": loan_account_id,
            "customer_id": customer_id,
            "account_type": "Loan",
            "account_number_last_4": str(random.randint(1000, 9999)),
            "balance": 0.0,
            "currency": currency,
            "date_opened": datetime.utcnow().strftime("%Y-%m-%d"),
            "status": "Active"
        }

        data.setdefault("accounts", []).append(new_account)
        customer.setdefault("account_ids", []).append(loan_account_id)

        # Loan attributes derived from database schema.
        principal_amount = decision.get("approved_amount")
        interest_rate = decision.get("interest_rate")
        term_months = loan_details.get("requested_term_months")
        origination_date = datetime.utcnow().strftime("%Y-%m-%d")
        maturity_date = (datetime.utcnow().replace(year=datetime.utcnow().year + (term_months // 12))).strftime("%Y-%m-%d")

        # Compute the monthly payment using the basic amortization equation.
        r = interest_rate / 100 / 12
        n = term_months
        if r > 0:
            monthly_payment = (principal_amount * r * (1 + r)**n) / ((1 + r)**n - 1)
        else:
            monthly_payment = principal_amount / n

        # Insert loan into database.
        new_loan = {
            "loan_id": loan_id,
            "customer_id": customer_id,
            "account_id": loan_account_id,
            "loan_type": loan_type,
            "principal_amount": principal_amount,
            "current_balance": principal_amount,  # Presuming complete allocation
            "interest_rate": interest_rate,
            "term_months": term_months,
            "origination_date": origination_date,
            "maturity_date": maturity_date,
            "monthly_payment": round(monthly_payment, 2),
            "status": "Active",
            "collateral": {
                "type": collateral_type,
                "address": collateral_info
            },
            "purpose": loan_details.get("purpose")
        }

        data.setdefault("loans", []).append(new_loan)

        return json.dumps({
            "status": "Loan successfully added.",
            "loan_id": loan_id,
            "loan_account_id": loan_account_id,
            "loan_type": loan_type
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_loan_for_customer",
                "description": (
                    "Creates a new loan entry based on a customer's loan application and collateral details. "
                    "Generates new loan and account IDs and links them to the customer."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "ID of the customer taking the loan"},
                        "application_id": {"type": "string", "description": "ID of the related loan application"},
                        "collateral_type": {"type": "string", "description": "Type of collateral (e.g., 'Car', 'Property')"},
                        "collateral_info": {"type": "string", "description": "Detailed information about the collateral"},
                        "currency": {
                            "type": "string",
                            "description": "Currency for the account (e.g., 'USD')"
                        }
                    },
                    "required": ["customer_id", "application_id", "collateral_type", "collateral_info", "currency"]
                }
            }
        }
