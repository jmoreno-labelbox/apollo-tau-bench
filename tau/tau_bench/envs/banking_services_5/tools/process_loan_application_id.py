# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessLoanApplicationId(Tool):
    """Evaluates a loan application using structured loan approval criteria and updates its status."""

    @staticmethod
    def invoke(data: Dict[str, Any], application_id = "", customer_id = "") -> str:
        customer_id    = customer_id.strip()
        application_id = application_id.strip()
        if not customer_id or not application_id:
            return json.dumps({"error": "customer_id and application_id are required."}, indent=2)

        loan_applications = data.get("loan_applications", [])
        customers = list(data.get("customers", {}).values())

        # check if customer is present
        if not any(c.get("customer_id") == customer_id for c in customers):
            return json.dumps({"error": "Customer not found."}, indent=2)

        # Locate loan application
        loan_application = next(
            (l for l in loan_applications
             if l.get("application_id") == application_id
             and l.get("customer_id") == customer_id),
            None
        )
        if not loan_application:
            return json.dumps({"error": "Loan application not found for this customer."}, indent=2)

        # Retrieve financial details for loans and customers.
        loan_details = loan_application.get("loan_details", {})
        financials = loan_application.get("financial_snapshot", {})
        annual_income = financials.get("annual_income", 0)
        monthly_debt = financials.get("monthly_debt_payments", 0)
        employment_status = financials.get("employment_status", "").strip().lower()
        requested_amount = loan_details.get("requested_amount", 0)
        loan_type = loan_details.get("loan_type","Others")

        # Calculated metrics
        dti = monthly_debt / (annual_income / 12) if annual_income else 1.0
        now = datetime.utcnow().isoformat() + "Z"

        decision = {"decision_date": now}
        approved = True
        rejection_reason = None

        # Logic for approving loans
        if annual_income < 15000:
            approved = False
            rejection_reason = "Insufficient income"
        elif dti >= 0.50:
            approved = False
            rejection_reason = "High debt-to-income ratio"
        elif employment_status == "unemployed":
            approved = False
            rejection_reason = "Unstable employment"
        elif requested_amount > (annual_income * 5):
            approved = False
            rejection_reason = "Requested amount disproportionate to income"

        interest_rate = 0.0
        if loan_type == "Auto":
            interest_rate = 0.10
        elif loan_type == "Home":
            interest_rate = 0.12
        elif loan_type == "Student":
            interest_rate = 0.08
        elif loan_type == "Business":
            interest_rate = 0.09
        elif loan_type == "Personal":
            interest_rate = 0.15
        else:
            interest_rate = 0.18

        if approved:
            loan_application["application_status"] = "Approved"
            decision.update({
                "approved_amount": requested_amount,
                "interest_rate": interest_rate
            })
        else:
            loan_application["application_status"] = "Rejected"
            decision["reason"] = rejection_reason

        # Store choice
        loan_application["decision"] = decision

        return json.dumps({
            "customer_id": customer_id,
            "application_id": application_id,
            "application_status": loan_application["application_status"],
            "decision": decision
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_loan_application_id",
                "description": (
                    "Evaluates a loan application and determines whether it should be approved or rejected "
                    "based on standard lending criteria like income, DTI, and employment."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose application is being processed"
                        },
                        "application_id": {
                            "type": "string",
                            "description": "Loan application ID to evaluate and process"
                        }
                    },
                    "required": ["customer_id", "application_id"]
                }
            }
        }
