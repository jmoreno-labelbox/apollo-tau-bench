from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class ApplyForLoanTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, loan_type: str = None, 
               requested_amount: float = None, purpose: str = None, 
               annual_income: float = None) -> str:
        loan_applications = data.get('loan_applications', [])

        application_id = f"loan_app_{generate_unique_id()}"

        credit_score = 720
        if annual_income > 80000:
            credit_score = 750
        elif annual_income < 40000:
            credit_score = 650

        status = "Under Review"
        if requested_amount > annual_income * 5:
            status = "Requires Additional Documentation"

        new_application = {
            "application_id": application_id,
            "customer_id": customer_id,
            "loan_type": loan_type,
            "requested_amount": requested_amount,
            "purpose": purpose,
            "annual_income": annual_income,
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
                "name": "ApplyForLoan",
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
