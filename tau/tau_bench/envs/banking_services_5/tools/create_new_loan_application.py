# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewLoanApplication(Tool):
    """Submits a new loan application using customer_id by auto-extracting customer data from the database."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        loan_type = kwargs.get("loan_type")
        requested_amount = kwargs.get("requested_amount")
        requested_term_months = kwargs.get("requested_term_months")
        purpose = kwargs.get("purpose")


        if not all([customer_id, loan_type, requested_amount, requested_term_months, purpose]):
            return json.dumps({"error": "All loan-related fields and customer_id are required."}, indent=2)

        # Retrieve customer information from the database.
        customers = list(data.get("customers", {}).values())
        customer = next((c for c in customers if c.get("customer_id") == customer_id), None)

        if not customer:
            return json.dumps({"error": f"Customer with ID '{customer_id}' not found."}, indent=2)

        # Retrieve information from the customer profile.
        personal_info = customer.get("personal_info", {})
        contact_info = customer.get("contact_info", {})
        financial_profile = customer.get("financial_profile", {})

        first_name = personal_info.get("first_name")
        last_name = personal_info.get("last_name")
        date_of_birth = personal_info.get("date_of_birth")
        email_address = contact_info.get("email_address")
        phone_number = next((p.get("number") for p in contact_info.get("phone_numbers", []) if p.get("is_primary")), None)
        address = contact_info.get("mailing_address") or {}

        employment_status = personal_info.get("occupation", "Employed")  # Standard presumption
        employer_name = personal_info.get("employer")
        annual_income = financial_profile.get("annual_income", 0)
        monthly_debt_payments = 0  # Absent in customer database, set to 0 by default.

        # Create application starting point.
        application_id = get_next_loan_application_id()
        submission_date = get_current_timestamp()

        new_application = {
            "application_id": application_id,
            "customer_id": customer_id,
            "existing_customer": True,
            "submission_date": submission_date,
            "application_status": "Submitted",

            "applicant_info": {
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "email_address": email_address,
                "phone_number": phone_number,
                "address": address
            },

            "loan_details": {
                "loan_type": loan_type,
                "requested_amount": requested_amount,
                "requested_term_months": requested_term_months,
                "purpose": purpose

            },

            "financial_snapshot": {
                "employment_status": employment_status,
                "employer_name": employer_name,
                "annual_income": annual_income,
                "monthly_debt_payments": monthly_debt_payments
            },

            "decision": "Pending"
        }

        data.setdefault("loan_applications", []).append(new_application)

        return json.dumps({
            "application_id": application_id,
            "application_status": "Submitted"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_loan_application",
                "description": (
                    "Submits a new loan application using the customer's existing record. "
                    "Only customer_id and loan details are required as input."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Existing customer ID"},
                        "loan_type": {"type": "string", "description": "Type of loan"},
                        "requested_amount": {"type": "number", "description": "Requested loan amount"},
                        "requested_term_months": {"type": "integer", "description": "Requested loan term in months"},
                        "purpose": {"type": "string", "description": "Purpose of the loan"}
                    },
                    "required": ["customer_id", "loan_type", "requested_amount", "requested_term_months", "purpose"]
                }
            }
        }
