# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import get_current_timestamp
from . import generate_unique_id


class ApplyForLoanTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        loan_type = kwargs.get('loan_type')
        requested_amount = kwargs.get('requested_amount')
        purpose = kwargs.get('purpose')
        income = kwargs.get('annual_income')

        loan_applications = data.get('loan_applications', [])

        application_id = f"loan_app_{generate_unique_id()}"

        credit_score = 720
        if income > 80000:
            credit_score = 750
        elif income < 40000:
            credit_score = 650

        status = "Under Review"
        if requested_amount > income * 5:
            status = "Requires Additional Documentation"

        new_application = {
            "application_id": application_id,
            "customer_id": customer_id,
            "loan_type": loan_type,
            "requested_amount": requested_amount,
            "purpose": purpose,
            "annual_income": income,
            "credit_score": credit_score,
            "status": status,
            "application_date": get_current_timestamp(),
            "decision": None,
            "approved_amount": None
        }

        loan_applications.append(new_application)

        return json.dumps({
            "application_id": application_id,
            "status": status,
            "credit_score": credit_score,
            "application_date": new_application["application_date"]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_for_loan",
                "description": "Submit a loan application",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "loan_type": {"type": "string", "description": "Type of loan", "enum": ["Personal", "Auto", "Mortgage", "Business"]},
                        "requested_amount": {"type": "number", "description": "Requested loan amount"},
                        "purpose": {"type": "string", "description": "Purpose of the loan"},
                        "annual_income": {"type": "number", "description": "Applicant's annual income"}
                    },
                    "required": ["customer_id", "loan_type", "requested_amount", "purpose", "annual_income"]
                }
            }
        }
