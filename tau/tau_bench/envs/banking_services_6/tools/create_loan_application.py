# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateLoanApplication(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, annual_income, customer_id, loan_type, purpose, term) -> str:
        application_id = _get_next_loan_application_id(data)
        customer = next((c for c in data['customers'] if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        new_application = {
                "application_id": application_id,
                "customer_id": customer_id,
                "existing_customer": True,
                "applicant_info": {
                        "first_name": customer['personal_info']['first_name'],
                        "last_name": customer['personal_info']['last_name'],
                },
                "loan_details": {
                        "loan_type": loan_type,
                        "requested_amount": amount,
                        "requested_term_months": term,
                        "purpose": purpose
                },
                "financial_snapshot": {"annual_income": annual_income},
                "application_status": "Submitted",
                "submission_date": NOW.strftime(DT_STR_FORMAT)
        }
        data['loan_applications'].append(new_application)
        return json.dumps(new_application)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_loan_application",
                        "description": "Creates a new loan application for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "loan_type": {"type": "string"}, "amount": {"type": "number"},
                                        "term": {"type": "integer"}, "purpose": {"type": "string"}, "annual_income": {"type": "integer"}
                                },
                                "required": ["customer_id", "loan_type", "amount", "term", "purpose", "annual_income"]
                        }
                }
        }
